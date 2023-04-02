from flask import Flask, render_template, request, url_for
import requests

# get stuff
app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html", visibility="hidden")

# display movie details
@app.route('/image', methods=['POST', 'GET'])
def image():
  user_input = request.form['movietitle']

  # API
  url = "https://moviesdb5.p.rapidapi.com/om"
  
  querystring = {"t":str(user_input)}
  
  headers = {
  	"X-RapidAPI-Key": "eaa420fd6bmsh4f21f4e548031ffp18d9dajsnb5eb42e676d2",
  	"X-RapidAPI-Host": "moviesdb5.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  r = response.json() ## converts to json so we can extract data using "get()"
  movie_title=str(r.get("Title"))
  movie_poster=str(r.get("Poster"))
  
  movie_year=str(r.get("Year"))
  movie_rated=str(r.get("Rated"))
  movie_genre=str(r.get("Genre"))
  movie_runtime=str(r.get("Runtime"))
  movie_id=str(r.get("imdbID"))
  # API END
  
  return render_template("index.html", visibility="visible", title=movie_title, movie_poster=movie_poster, movie_year=movie_year, movie_rated=movie_rated, movie_genre=movie_genre, movie_runtime=movie_runtime, movie_id=movie_id)
  



# watch movie
@app.route('/<title>', methods=['POST', 'GET'])
def watch(title):
  id = request.form['watch_button']
  return render_template("watch.html", id=id, title=title)


if __name__ == '__main__':
  app.run(debug=True)
