from flask import Flask, request, render_template,jsonify
import nltk
from autocorrect import spell
from gensim.summarization import summarize as g_sumn
import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
from requests.auth import HTTPBasicAuth
from pathlib import Path
import openai
import os
from IPython.display import Markdown
import pythonFiles.jinxin as jinxinFunction
import pythonFiles.tmpceazar as ceazarFunction

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('/index.html')

#####################################################################################
###############################Begin Jinxin Ai#######################################
#####################################################################################
@app.route('/giveInfo_jinxin', methods=["GET"])
def jinxinHtml():
    return render_template('giveInfo_jinxin.html')

@app.route('/webstory_jinxin', methods=["GET"])
def installation():
    return render_template('webstory_jinxin.html')

@app.route('/topic', methods=["GET", "POST"])
def topic2story():
    text = request.form['text']
    jinxinFunction.chatgpt(text)
    return 'Already generated text'

@app.route('/generate4imgs', methods=["GET", "POST"])
def generate4imgs():
    jinxinFunction.deliverImages()
    return "Already generated Images"
@app.route('/showSections', methods=["GET", "POST"])
def showSections():
    return jinxinFunction.postSections()

@app.route('/showTitle', methods=["GET", "POST"])
def showTitle():
    return jinxinFunction.postTitle()
#####################################################################################
#################################End Jinxin Ai#######################################
#####################################################################################

#####################################################################################
###########################Begin Ceazar Haddad#######################################
#####################################################################################
# from flask import Flask, render_template, request, jsonify, make_response
# from python.generate_article import generate_article


# app = Flask(__name__)

# @app.route('/')
# @app.route('/home')

# def home():
#     return render_template('/index.html')

# @app.route('/generate-article')
# def generate_article_route():
#     topic = request.args.get('topic')
#     article = generate_article(topic)
#     return jsonify(article=article)

# if __name__ == '__main__':
#     app.run(debug=True)
##########################################################################
# import os
# import openai
# from flask import Flask, render_template, request

# # Set OpenAI credentials
# openai.api_key = "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"
# openai.organization = "org-umtU2aMACFq7eNAg7bptz37h"

# # Initialize Flask app
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/generate", methods=["POST"])
# def generate_article():
#     prompt = request.form.get("prompt")

#     # Create image using OpenAI API
#     res = openai.Image.create(
#         prompt=f"{prompt}, very render, high resolution",
#         n=3,
#         size="512x512",
#     )

#     # Get image URLs
#     image_urls = [i["url"] for i in res["data"]]

#     # Generate article using OpenAI API
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     article = response.choices[0].text

#     # Render template with article and images
#     return render_template("result.html", article=article, image_urls=image_urls)

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template, request
# from python.generate_images import generate_image
# import openai

# # Set OpenAI credentials
# openai.api_key = "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"
# openai.organization = "org-umtU2aMACFq7eNAg7bptz37h"

# # Initialize Flask app
# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/generate", methods=["POST"])
# def generate_article():
#     prompt = request.form.get("prompt")

#     # Generate article using OpenAI API
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     article = response.choices[0].text

#     # Generate images using OpenAI API
#     image_urls = generate_image(prompt)

#     # Render template with article and images
#     return render_template("result.html", article=article, image_urls=image_urls)

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template, request, jsonify
# from python.generate_article import generate_article
# from python.generate_images import generate_images

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('/index.html')

# @app.route('/generate-article')
# def generate_article_route():
#     topic = request.args.get('topic')

#     # Generate article
#     article = generate_article(topic)

#     # Return JSON response with article
#     return jsonify(article=article)

# @app.route('/generate-images')
# def generate_images_route():
#     topic = request.args.get('topic')

#     # Generate images
#     image_urls = generate_images(topic)
#     print(image_urls)
#     # Return JSON response with image URLs
#     return jsonify(images=image_urls)

# if __name__ == '__main__':
#     app.run(debug=True)


# @app.route('/')
# def home():
    # return render_template('/index.html')
from flask import Flask, render_template, request, jsonify
from pythonFiles.ceazar.generate_article import generate_article
from pythonFiles.ceazar.generate_images import generate_images

@app.route('/ceazar', methods=["GET"])
def ceazarHtml():
    return render_template('ceazar.html')

@app.route('/generate-article')
def generate_article_route():
    topic = request.args.get('topic')
    
    # Generate article
    article = generate_article(topic)

    # Return JSON response with article
    print(article)
    return jsonify(article=article)

@app.route('/generate-images')
def generate_images_route():
    topic = request.args.get('topic')

    # Generate images
    image_urls = generate_images(topic)
    print(image_urls)
    # Return JSON response with image URLs
    return jsonify(images=image_urls)



#####################################################################################
#############################END Ceazar Haddad#######################################
#####################################################################################

if __name__ == '__main__':
    app.run(debug=True)
