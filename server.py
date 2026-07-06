from flask import Flask, request, render_template

from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Hello World!"}


@app.route("/emotionDetector")
def emotion_detector():
    query = request.args.get("text")

    if query is None:
        return ({"message": "Please provide a query"}, 400)

    try:
        response = emotion_detector(query)
        return (response, 200)
    except Exception as e:
        return ({"message": f"Error - {str(e)}"}, 500)


if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=5000, debug=True)
    # app.run(host="localhost", port=5000, debug=True)