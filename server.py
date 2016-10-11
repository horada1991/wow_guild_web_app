from flask import Flask, render_template, jsonify, redirect, url_for, request
from handle_tables import NewsHandler

app = Flask('Lunatic Guild Web App')
news_handler = NewsHandler()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# get all news in JSON object with this api route
@app.route('/api/news', methods=['GET'])
def get_news():
    news_json = [news.convert_object_to_dict() for news in news_handler.get_all_entry()]
    response = jsonify(news_json)
    return response


@app.route('/api/news-save', methods=['POST'])
def save_news():
    news_handler.save_entry(request.json)
    return jsonify(request.json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)