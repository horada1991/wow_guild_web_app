$(document).ready(function () {
    // write out all news
    $.getJSON('/api/news', function (response) {
        listNews(response)
    });
    
    // clicking on add new news on the home page:
    $('#add_news_btn').click(function () {
        
    });
});