function GetHTMLForFlightTip(item) {
    // this function takes the json object for a flight item and it returns nice
    // html which can then be dropped onto the page.
    
    // determine whether we use the iata code or the icao code.
    
    from = item.airport_from.iata_code;
    if (from == "N/A") from = item.airport_from.icao_code;
    
    dest = item.airport_to.iata_code;
    if (dest == "N/A") dest = item.airport_to.icao_code;
    
    
    content = 
        '<div class="flight-info">' +
        '    <div class="avatar"><img src="' + item.avatar_url + '"/></div>' +
        '    <div class="flight">' +
        '        <h4>' + item.name + '</h4>' +
        '        <p class="codes">' + from + ' -&gt; ' + dest + '</p>' + 
        '        <p class="rating">' + item.value + '</p>' +
        '        <p class="comment">fdhjfsk fdksljfhd dslkfhd fdfdhs fdfks ' + item.comment + '</p>' +
        '    </div>' +
        '</div>';

    return (content);


}
