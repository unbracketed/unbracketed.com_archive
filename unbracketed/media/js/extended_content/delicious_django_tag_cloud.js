function handleTagCloud( data, status )
{
    var hovertipConfig = {'attribute':'hovertip',
                            'showDelay': 0,
                            'hideDelay': 200};
    var hovertipSelect = 'ul.hovertip';
    
    $('div#delicious-tags').html( data );
    window.setTimeout(function() {
    $(hovertipSelect).hovertipActivate(hovertipConfig,
                                       targetSelectByTargetAttribute,
                                       hovertipPrepare,
                                       hovertipTargetPrepare);
    }, 0);
    
    $('div#delicious-tags  a').click( function() {    
        //$.get( this.href, handleTagCloud );
        return false;
    } );
}

$(document).ready( function()
{
    $.get( '/extended_content/delicious-django-all-tag-cloud/', handleTagCloud );
});