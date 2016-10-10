
function listNews (newsList) {
    $('#news_block').empty();
    $.each(newsList, function (index, news) {
        var $newsContainer = $('<div></div>').addClass('panel panel-default').attr('id', 'news_container');
        var $panelHeading = $('<div></div>').addClass('panel-heading').attr('id', 'news_panel-header');
        $('<h4>' + news.title + '</h4>').appendTo($panelHeading);
        $('<p>' + news.timestamp + '</p>').appendTo($panelHeading);
        $panelHeading.appendTo($newsContainer);

        var $bodyContainer = $('<div></div>').addClass('container').attr('id', 'news_body_container');
        $('<div>' + news.body + '</div>').addClass('col-md-12 col-lg-12 col-sm-12 col-xs-12').appendTo($bodyContainer);
        $bodyContainer.appendTo($newsContainer);

        $newsContainer.appendTo($('#news_block'))

    });
}