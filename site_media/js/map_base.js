/** map initialisation JS file **/

var initialLoc;
var browserSupportFlag = new Boolean();      

function initialize() {
    // this function initialises the map to the starting position and zoom
    // to the div in the page. 

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

    function noGeoHandler() {
      // this function deals with if the user either does't have or
      // doesn't allow the geolocation to fire.
      // no geolocation data so just go world view
      
      browserSupportFlag = false;
      var worldView = new google.maps.LatLng(0,150);
      map.setZoom(2);
      map.setCenter(worldView); 
    }

}
    
function loadGMapScript() {
    var script = document.createElement("script");
    script.type = "text/javascript";
    script.src = "http://maps.google.com/maps/api/js?sensor=false&callback=initialize";
    document.body.appendChild(script);
}
    
