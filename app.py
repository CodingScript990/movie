from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb://test:test@localhost', 27017)

db = client.dbmovie


# index.html
@app.route('/')
def home():
    return render_template('index.html')

# review.html
@app.route('/review')
def comment():
    return render_template('review.html')

# movie_info.html
@app.route('/info')
def info():
    return render_template('movie_info.html')

# movie api position
@app.route('/api/list', methods=['GET'])
def show_movies():
    movie_list = list(db.movielist.find({},{'_id':False}))
    return jsonify({'movie_lists': movie_list})

# movie info position
@app.route('/info/list', methods=['GET'])
def show_infos():
    info_list = list(db.movielist.find({},{'_id':False}))
    return jsonify({'movie_infos': info_list})

# movie review comment position

# movie review comment DB storage
@app.route('/comment', methods=['POST'])
def write_review():
    name_receive = request.form['name_give']  # name-list
    comment_receive = request.form['comment_give'] # comment-list

    doc = {
        'name' : name_receive,
        'comment': comment_receive
    }

    db.moviecomment.insert_one(doc)

    return jsonify({'msg': 'Success!!'})

# movie review comment client
@app.route('/comment', methods=['GET'])
def read_reviews():
    reviews = list(db.moviecomment.find({}, {'_id': False}))
    return jsonify({'review_comments': reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)