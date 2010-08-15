function GetHTMLForFlightTip(item) {
    // this function takes the json object for a flight item and it returns nice
    // html which can then be dropped onto the page.
    content = 
        '<div class="flight-info">' +
        '    <div class="avatar"><img src="' + item.avatar_url + '"/></div>' +
        '    <div class="flight">' +
        '        <h4>' + item.name + '</h4>' +
        '        <p class="codes">' + item.airport_from.iata_code + '-&gt;' +
                                    item.airport_to.iata_code + '</p>' + 
        '        <p class="rating">' + item.value + '</p>' +
        '        <p class="comment">' + item.comment + '</p>' +
        '    </div>' +
        '</div>';

    return (content);


}
