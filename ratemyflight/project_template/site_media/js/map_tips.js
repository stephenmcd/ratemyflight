function GetHTMLForFlightTip(item) {
    // this function takes the json object for a flight item and it returns nice
    // html which can then be dropped onto the page.
    
    // determine whether we use the iata code or the icao code.
    
    from = item.airport_from.iata_code;
    if (from == "N/A") from = item.airport_from.icao_code;
    
    dest = item.airport_to.iata_code;
    if (dest == "N/A") dest = item.airport_to.icao_code;
    
    ratingval = Math.floor(item.value * 10); // convert to a percentage
    var avatar = item.avatar_url;
    if (!avatar) {
        avatar = '/site_media/img/default_avatar.png';
    }
    
    content = 
        '<div class="flight-info">' +
        '    <div class="avatar"><img src="' + item.avatar_url + '"/></div>' +
        '    <div class="flight">' +
        '        <h4>' + item.name + '</h4>' +
        '        <p class="codes">' + from + ' &#x2708; ' + dest + '</p>' + 
        '        <p class="comment">' + item.comment + '</p>' +
        '    </div>' +
        '    <div class="cl"></div>' +
        '    <div class="rating">' +
        '        <div style="width:' + ratingval + '%">' +
        '            <img src="/site_media/img/stars_c.png" style=""/>' +
        '        </div>' +
        '    </div>' +
        '</div>';

    return (content);


}
