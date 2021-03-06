/** map initialisation JS file **/

var initialLoc;
var browserSupportFlag = new Boolean();   
var EventID = false;  // used as a flag for the boundary changes   

var airportList = new Array();
var airportsLoaded = {};
var flightsLoaded = {};
var flightList = new Array();
var flightPath = null;


function toRad (degrees) {
  radians = (2 * Math.PI * degrees)/360;
  return radians;

}

function toDeg(radians) {
   degrees = 360 * radians/(2 * Math.PI);
   return degrees;
}




function initialize() {
    // this function initialises the map to the starting position and zoom
    // to the div in the page. 

    // these are the inline functions
    
    function noGeoHandler() {
      // this function deals with if the user either does't have or
      // doesn't allow the geolocation to fire.
      // no geolocation data so just go world view
      
      browserSupportFlag = false;
      var worldView = new google.maps.LatLng(0,150);
      map.setZoom(2);
      map.setCenter(worldView); 
    }
    
    function boundaryChange() {
        // this function deals with a boundary change and will do things based
        // on that event
       
        //console.log("boundary_change");       
       // update the data area with the boundary details:
       var bounds = map.getBounds();
       var sw = bounds.getSouthWest();
       var ne = bounds.getNorthEast()
       
       // hit the ajax call for the airports and we'll retrieve them:
       var airporturl = '/api/airport/boundary/' + sw.lat() + '/' + sw.lng() + 
                                          '/' + ne.lat() + '/' + ne.lng() + "/";
                                          
        var flighturl = '/api/flight/boundary/' + sw.lat() + '/' + sw.lng() + 
                                          '/' + ne.lat() + '/' + ne.lng() + "/";
                                          
        //$("#map_data").text(flighturl);

       $.getJSON(airporturl, null, DisplayAirports);
       $.getJSON(flighturl, null, DisplayFlights);

        CleanupBounding();
   
    }

    function DisplayAirports(data) {
      // this function plots the airports on the map.
            
       for (i=0; i< data.length; i++) {
         item = data[i];
         
         if (! airportsLoaded[item.pk]) {
         
           if (item.fields["iata_code"] != null) {
              lat = item.fields["latitude"];
              lng = item.fields["longitude"];
              n = item.fields["name"];

              var marker = new google.maps.Marker({
                  position: new google.maps.LatLng(lat, lng), 
                  map: map,
                  title:n,
                  icon: airportimage,
                  zIndex: 1
              });  
           }
           airportsLoaded[item.pk] = marker;
        }
       
       }
       
    }
    
    function GetPlaneImage(deg) {
      // this function gets the plane image that is appropriate
      
      if (deg < 0) {
        // switch it back to 360 deg;
        deg = 360 + deg;
      }
      
      
      var planeimage = new google.maps.MarkerImage(
      "/site_media/img/planes/" + Math.floor(deg) +  ".png",
      new google.maps.Size(24, 24),
      new google.maps.Point(0, 0),
      new google.maps.Point(12, 12) );
    
    
      return (planeimage);
    }
    
    
    function DisplayFlights(data) {
      // this function displays the flights on the map.
      
      for (i=0; i< data.length; i++){
        item = data[i];
        
        if (! flightsLoaded[item.id]) {
        
          dept = new google.maps.LatLng(item.airport_from.latitude, item.airport_from.longitude);
          arr = new google.maps.LatLng(item.airport_to.latitude, item.airport_to.longitude);
          flightCoords = [dept, arr];
          
          flightPath = new google.maps.Polyline({
            path: flightCoords,
            geodesic: true,
            strokeColor: "#b10000",
            strokeOpacity: 0.2,
            strokeWeight: 3
          });

          flightPath.setMap(map);
          
          midpoint = dept.midpointLocation(arr, distance(dept, arr) * 0.10);
          
          var midpointmarker = new google.maps.Marker({
                      position: midpoint.LatLng, 
                      map: map,
                      icon: GetPlaneImage(midpoint.bearing),
                      zIndex: 2,
                  }); 
                  
                  
          var infoMarker = new RichMarker({
            position: midpoint.LatLng,
            map: map,
            anchor: 4,
            flat: true,
            zIndex: 200,
            content: GetHTMLForFlightTip(item)
          });
         
         // add a listener to bring the item forward
          google.maps.event.addListener(infoMarker, 'click', function() {
            amount = this.getZIndex();
            this.setZIndex(amount+50);
          });
         
          
          // sort out the object storage
          flightinfo = {};
          flightinfo.midpointmarker = midpointmarker;
          flightinfo.infomarker = infoMarker;
          flightinfo.flightpath = flightPath;
          
          flightsLoaded[item.id] = flightinfo;
          
          
          
        }
      }
    }
    

    function distance(point1, point2) {
    // gets the distance between two points
          lat1 = point1.lat();
          lat2 = point2.lat();
          lon1 = point1.lng();
          lon2 = point2.lng();
	        var R = 6371000; // km (change this constant to get miles)
	        var dLat = (lat2-lat1) * Math.PI / 180;
	        var dLon = (lon2-lon1) * Math.PI / 180;
	        var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
	            Math.cos(lat1 * Math.PI / 180 ) * Math.cos(lat2 * Math.PI / 180 ) *
	            Math.sin(dLon/2) * Math.sin(dLon/2);
	        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
	        var d = R * c;
	        return d;
    }




    google.maps.LatLng.prototype.midpointLocation = function(point, distance) {   
    // gets a midpoint location between two points. Actually defined by the 
    // distance you pass in as to how fr between points you go.
       var lat1 = toRad(this.lat());          
       var lon1 = toRad(this.lng());
       var lat2 = toRad(point.lat());
       var lon2 = toRad(point.lng());         
       var dLon = (toRad(point.lng()) - toRad(this.lng()));

       // Find the bearing from this point to the next.
       var brng = Math.atan2(Math.sin(dLon) * Math.cos(lat2),
                             Math.cos(lat1) * Math.sin(lat2) -
                             Math.sin(lat1) * Math.cos(lat2) * 
                             Math.cos(dLon));

       var angDist = distance / 6371000;  // Earth's radius.

       // Calculate the destination point, given the source and bearing.
       lat2 = Math.asin(Math.sin(lat1) * Math.cos(angDist) + 
                        Math.cos(lat1) * Math.sin(angDist) * 
                        Math.cos(brng));

       lon2 = lon1 + Math.atan2(Math.sin(brng) * Math.sin(angDist) *
                                Math.cos(lat1), 
                                Math.cos(angDist) - Math.sin(lat1) *
                                Math.sin(lat2));

       if (isNaN(lat2) || isNaN(lon2)) return null;

        midpointObject  = {};
        midpointObject.LatLng = new google.maps.LatLng(toDeg(lat2), toDeg(lon2));
        midpointObject.bearing = toDeg(brng);
        
       return midpointObject;
    }




    function CleanupBounding() {
      // this function removes all of the items that are outside of the bounding
      // area of the map.
      
      bounds = map.getBounds();
      
      for (k in airportsLoaded) {
  
        if (! bounds.contains(airportsLoaded[k].getPosition())) {
          // remove the point off the map
          airportsLoaded[k].setMap(null);
          
          // remove the point from the array
          delete airportsLoaded[k]; // = null
        }
      }
      
      for (k in flightsLoaded) {
        // remove all flights each time.
        flightsLoaded[k].midpointmarker.setMap(null);
        flightsLoaded[k].infomarker.setMap(null);
        flightsLoaded[k].flightpath.setMap(null);
      
        delete flightsLoaded[k];
      }      
      /**allist=0;
       for (k in airportsLoaded){
        allist++;
      }**/
      //$("#map_data").text("Airports: " + allist + " // ");
    
    
    }



    // THIS IS WHERE WE START THE ACTUAL INIT OF THE MAP ETC

    var airportimage = new google.maps.MarkerImage(
      "/site_media/img/airport6.png",
      new google.maps.Size(10, 10),
      new google.maps.Point(0,0),
      new google.maps.Point(5,5) );


    var mapOptions = {
        zoom: 4,
        mapTypeControl: false,
        mapTypeId: google.maps.MapTypeId.TERRAIN
    }
    
    var map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);


    // Try W3C Geolocation (Preferred)
    if(navigator.geolocation) {
        browserSupportFlag = true;
        // use the geo log and depending and if the user allows the service
        // to work and it returns properly or they choose not to or it fails
        // for whatever reason call one function or the other to set pass or
        // fail.
        navigator.geolocation.getCurrentPosition(
            function(position) {
                initialLoc = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                map.setCenter(initialLoc);
            }, 
            function() {
                noGeoHandler();
            });
    } else {
        // if geo log W3C stylee doesn't work then we're not bothering with
        // other styles for the moment. GL W3C has enough coverage.
        noGeoHandler();

    }


    // now we set up event handlers to deal with the changes
    google.maps.event.addListener(map, 'bounds_changed', 
      function() {
        if (EventID) {
          clearTimeout(EventID);
          //console.log("cleared");
        } 
        EventID = setTimeout(boundaryChange, 1000);
      }        
    );
    
    // add in our additional library for the rich markers
    loadRichMarkerScript();
    

}
    
function loadGMapScript() {
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "http://maps.google.com/maps/api/js?sensor=false&callback=initialize";
    document.body.appendChild(script);
    
}

function loadRichMarkerScript() {
    // add the other
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "/site_media/js/richmarker-compiled.js";
    document.body.appendChild(script);
}

    
