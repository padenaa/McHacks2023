from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_song():
    return {"song_ids": []}

if __name__ == "__main__":
    app.run(debug=True)