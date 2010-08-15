/** map initialisation JS file **/

var initialLoc;
var browserSupportFlag = new Boolean();   
var EventID = false;  // used as a flag for the boundary changes   

var airportList = new Array();
var airportsLoaded = {};
var flightList = new Array();

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
       var airporturl = '/api/airport/list/' + sw.lat() + '/' + sw.lng() + 
                                          '/' + ne.lat() + '/' + ne.lng() + "/";
                                          
        var flighturl = '/api/flight/list/' + sw.lat() + '/' + sw.lng() + 
                                          '/' + ne.lat() + '/' + ne.lng() + "/";
                                          
        $("#map_data").text(airporturl);

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
                  icon: airportimage
              });  
           }
           airportsLoaded[item.pk] = marker;
        }
       
       }
       
       allist=0;
       for (k in airportsLoaded){
        allist++;
      }
        
       
       $("#map_data").text($("#map_data").text() + " // " + allist + " airports //") ;
    }
    
    function DisplayFlights(data) {
      // this function plots the flights on the map
      
      // 
      
      $("#map_data").text($("#map_data").text() + " flights loaded") ;
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
      
      
      allist=0;
       for (k in airportsLoaded){
        allist++;
      }
      $("#map_data").text("Airports: " + allist + " // ");
    
    
    }



    // THIS IS WHERE WE START THE ACTUAL INIT OF THE MAP ETC

    var airportimage = "/site_media/img/airport.png";

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



}
    
function loadGMapScript() {
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "http://maps.google.com/maps/api/js?sensor=false&callback=initialize";
    document.body.appendChild(script);
}
    
