
from django.db.models import Manager, Q


class AirportManager(Manager):
    """
    Provides a method for retrieving airports within a given boundary.
    """
    
    def _boundary_filter(self, south, west, north, east):
        """
        Return the given boundary as a Q object suitable for querysets.
        """
        return Q(latitude__gt=south, longitude__gt=west, 
            latitude__lt=north, longitude__lt=east)

    def for_boundary(self, south, west, north, east):
        """
        Return the airports in the given boundary, combining multiple checks 
        if the boundary overlaps a hemisphere line.
        """
        south = float(south)
        west = float(west)
        north = float(north)
        east = float(east)
        if west * east < 0:
            # Boundary overlaps a hemisphere line, look up either side of it.
            if (180 - west) < west:
                # Closest to International Date Line.
                lookup = (self._boundary_filter(south, west, north, 180) | 
                    self._boundary_filter(south, -180, north, east))
            else:
                # Closest to Prime Meridian.
                lookup = (self._boundary_filter(south, west, north, 0) | 
                    self._boundary_filter(south, 0, north, east))
        else:
            lookup = self._boundary_filter(south, west, north, east)
        return self.filter(lookup)
        
