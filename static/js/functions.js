// show news feed on page
function listNews() {
    $.getJSON('/api/news', function (newsJSON) {
        $('#news_block').empty();
        $.each(newsJSON, function (index, news) {
            var $newsContainer = $('<div></div>').addClass('panel panel-default').attr('id', 'news_container');
            var $panelHeading = $('<div></div>').addClass('panel-heading').attr('id', 'news_panel-header');
            var $panelHeadingRow = $('<div></div>').addClass('row')
            $('<div>' + news.title + '</div>').addClass('col-md-6 col-lg-6 col-sm-6 col-xs-6').appendTo($panelHeadingRow);
            $('<div>' + news.timestamp + '</div>').addClass('col-md-6 col-lg-6 col-sm-6 col-xs-6 text-right').appendTo($panelHeadingRow);
            $panelHeadingRow.appendTo($panelHeading);
            $panelHeading.appendTo($newsContainer);

            var $bodyContainer = $('<div></div>').addClass('container').attr('id', 'news_body_container');
            $('<div>' + news.body + '</div>').addClass('col-md-12 col-lg-12 col-sm-12 col-xs-12').appendTo($bodyContainer);
            $bodyContainer.appendTo($newsContainer);

            $newsContainer.appendTo($('#news_block'))
        });
    })
}


// save news
var saveNews = function () {
    var $title = $('#news_title').val();
    var $body = $('#news_body').val();
    var news = {title: $title, body: $body};
    console.log(news)
    $.ajax({
        url: '/api/news-save',
        type: 'POST',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        data: JSON.stringify(news),
        success: function (response) {
            return response
        }
    })
    listNews()
};
