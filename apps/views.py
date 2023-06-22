# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request
from jinja2  import TemplateNotFound
from flask import Flask, render_template, request
import openai
from apps import prompt
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user



# App modules
# App modules
views = Blueprint('views', __name__)


# App main route + generic routing
@views.route('/', defaults={'path': 'index.html'})

@views.route('/<path>')
def index(path):

    try:

        # Detect the current page
        segment = get_segment( request )

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template( 'home/' + path, segment=segment )
    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

def get_segment( request ): 

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment    

    except:
        return None  

@views.route('/apps/')
@login_required
def apps():
    return render_template("/home/index.html")

@views.route('/flashcard', methods=["GET", "POST"])
@login_required
def yttitlegenerator():
    if request.method == 'POST':
        yt_name = request.form['channelName']
        query='''Generate 10 flashcards on the topic of {} so that a 3rd grade student can learn this concept.: <br><br>'''.format(yt_name)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/title_generator.html', **locals())


@views.route('/summarizer', methods=["GET", "POST"])
@login_required
def ytdescgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''Summarize the following topic for the 3rd grade student:- "{}":'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/yt_description.html', **locals())

@views.route('/lesson_explainer', methods=["GET", "POST"])
@login_required
def ytscriptgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Explain the lesson "{}" in brief to 3rd grade student in brief: <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/video_script.html', **locals())

@views.route('/qna', methods=["GET", "POST"])
@login_required
def yttweetgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate A QnA Test on the Topic for a 12th Grade Student to practice for main exams:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/tweet_ideas.html', **locals())

@views.route('/post_generator', methods=["GET", "POST"])
@login_required
def postgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Short Clicky Professional-Looking Eye-Catching Facebook Post Ideas on Title:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/post.html', **locals())

@views.route('/caption_generator', methods=["GET", "POST"])
@login_required
def instagenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Short Clicky Professional-Looking Eye-Catching Instagram Caption Ideas on Title:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/caption.html', **locals())

@views.route('/hashtag_generator', methods=["GET", "POST"])
@login_required
def hashgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Short Clicky Professional-Looking Viral Eye-Catching Instagram HashTags on Title:- "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/hash.html', **locals())

@views.route('/maths', methods=["GET", "POST"])
@login_required
def headgenerator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Solve the Mathematical solutions correctly with explanation: "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/blogHeadline.html', **locals())

@views.route('/physics', methods=["GET", "POST"])
@login_required
def blog_script_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''May you please solve and explain this physics numerical with detailed formulas process step-by-step "{}"?: <br><br>'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/blogScript.html', **locals())

@views.route('/chemistry', methods=["GET", "POST"])
@login_required
def story_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='May you please solve and explain this chemistry question "{}"?: <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/story.html', **locals())

@views.route('/lyrics_generator', methods=["GET", "POST"])
@login_required
def lyrics_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Brainstorm Rhyming Medolius Song Lyrics with minimum 500 words containing keywords or characters or emotion: "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/song.html', **locals())

@views.route('/startup_idea_generator', methods=["GET", "POST"])
@login_required
def start_idea_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Startup Ideas For: "{}":- <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/startup_idea.html', **locals())

@views.route('/slogan_generator', methods=["GET", "POST"])
@login_required
def slogan_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='Generate Slogans for a business: "{}": <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/slogan.html', **locals())

@views.route('/computer', methods=["GET", "POST"])
@login_required
def nexIdea_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='May you please give me the answer of the computer question "{}"?: <br><br>'.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/nexIdea.html', **locals())

@views.route('/product_description_generator', methods=["GET", "POST"])
@login_required
def prodesc():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        yt_serve = request.form['serve']
        yt_cost = request.form['cost']
        query='''Generate Detailed Product Description For "Techiral" which is "A Startup That Helps Building New SAAS Startups". The homepage link is "techiral.github.io". Services Provided Are "Build ReadMe Markdown For Your Projects", "Generate Product Descriptions For Products", "Generate YouTube Video Descriptions", "Get Tweet Ideas", "Generate Cold Emails For Products", "Get Business Pitch Ideas", "Get Video Ideas" This has "Both Freemium and Premium Versions. Premium Price Starts From $30 as basic plan.":-

# Techiral

## What is Techiral?

Techiral is a startup that helps build new SAAS startups. We provide services like building ReadMe Markdown for your projects, generating product descriptions for products, generating YouTube video descriptions, getting tweet ideas, generating cold emails for products, getting business pitch ideas, and getting video ideas. We have both freemium and premium versions. The premium price starts from $30 as the basic plan.

## How can Techiral help me?

If you are a startup founder, you can use Techiral to get help with your product marketing. We can help you with things like creating a product description, generating YouTube video descriptions, getting tweet ideas, and more. We also offer a premium plan that gives you access to more features and services.

## What are the features of Techiral?

Some of the features of Techiral include:

- Build ReadMe Markdown for your projects
- Generate product descriptions for products
- Generate YouTube video descriptions
- Get tweet ideas
- Generate cold emails for products
- Get business pitch ideas
- Get video ideas

## How much does Techiral cost?

Techiral has both a free and a premium version. The premium version starts at $30 per month.

## How to reach Techiral?

You can stick to the updates on techiral.github.io.
Generate Detailed Product Description For "{}" which is "{}". The homepage link is "{}". Services Provided Are "{}". This has "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home, yt_serve, yt_cost)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/prodesc.html', **locals())

@views.route('/hindi_lit', methods=["GET", "POST"])
@login_required
def coldmail_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''May you please answer this Hindi Literature question: "{}"?:- <br><br>'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/cold_email.html', **locals())

@views.route('/english_lit', methods=["GET", "POST"])
@login_required
def welmail_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        yt_serve = request.form['serve']
        yt_page = request.form['page']
        query='''Generate A Welcome Email To "Aakash" from "Techiral" for the product "IncreHub" with services "An Online Tool that helps to rank YouTube Content and Videos With The Help Of AI" on the homepage "www.increhub.io":-

Hi Aakash,

Welcome to Increhub – we’re excited to have you on board and we’d love to say thank you on behalf of our whole company for choosing us. We believe our Increhub will help you to optimize your videos for the YouTube search algorithm.
To ensure you gain the very best out of our Increhub, we’ve put together some of the most helpful guides:
This video www.increhub.io walks you through setting up your IncreHub for the first time. Our FAQ www.increhub.io/faq/ is a great place to find the answers to common questions you might have as a new customer. The knowledge base www.increhub.io has the answers to all of your tech-related questions. Our blog www.blog.increhub.io has some great tips and best practices on how you can use and benefit from Increhub.
Have any questions or need more information? Just shoot us an email! We’re always here to help.

Take care,
Increhub


Generate A Welcome Email To "{}" from "{}" for the product "{}" with services "{}" on the homepage "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home, yt_serve, yt_page)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/wel_mail.html', **locals())

@views.route('/cancellation_e-mail_generator', methods=["GET", "POST"])
@login_required
def cancelmail_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        yt_serve = request.form['serve']
        query='''Generate A Cancellation Email To "{}" from "{}" for the product "{}" with the survey link "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home, yt_serve)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/cancelMail.html', **locals())

@views.route('/verification_e-mail_generator', methods=["GET", "POST"])
@login_required
def verimail_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        query='''Generate A Verification Email To "{}" from "{}" for the product "{}" with the unique OTP:- <br><br>'''.format(yt_title, yt_desc, yt_home)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/veriMail.html', **locals())

@views.route('/github_readme_generator', methods=["GET", "POST"])
@login_required
def readme_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        yt_home = request.form['home']
        yt_url = request.form['url']
        yt_mail = request.form['mail']
        query='''
Generate Detailed GitHub Readme Markdown For A "web app" "Milk" "which is a business generator, and management tool. With this tool, you can build apps for yourself, build websites, and others". It is available on "https:/techiral.github.io/milk" E-mail for support "techiraltofuture@gmail.com":-

# Milk

Milk is a business generator, and management tool. With this tool, you can build apps for yourself, build websites, and others.

## Features

-   Build apps for yourself
-   Build websites
-   Manage your business
-   Get support from the community

## Usage

- Clone Repo From https:/techiral.github.io/milk.
```
git clone https://github.com/techiral/milk.git
```

## Documentation

You can find the documentation for Milk on the website"https:/techiral.github.io/milk/docs.".

## Help

Email: techiraltofuture@gmail.com

Generate Detailed GitHub Readme Markdown For A "{}" "{}" "{}". It is available on "{}" E-mail for support "{}":- <br><br>'''.format(yt_title, yt_desc, yt_home, yt_url, yt_mail)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/readme.html', **locals())

@views.route('/python_code_generator', methods=["GET", "POST"])
@login_required
def code_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''Generate detailed notes on the topic "{}" for the 10th grade boy:- <br><br>'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/pythoncode.html', **locals())

@views.route('/tips', methods=["GET", "POST"])
@login_required
def coach():
    if request.method == 'POST':
        yt_title = request.form['title']
        query='''Generate the best tips to achieve: "{}":- <br><br>'''.format(yt_title)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/coach.html', **locals())

@views.route('/cybersecurity', methods=["GET", "POST"])
@login_required
def herovillian_story_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        query="Generate An easy to learn and understand Detailed expalnation on the concept of the cybersecurity topic: {}:- <br><br>".format(yt_title, yt_desc)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/hero-story.html', **locals())

@views.route('/financial', methods=["GET", "POST"])
@login_required
def horror_story_generator():
    if request.method == 'POST':
        query="Generate A Detailed RoadMap To Achieve Financial Freedom more quickly:- <br><br>"
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/horror-story.html', **locals())

@views.route('/influencer', methods=["GET", "POST"])
@login_required
def fairytales_generator():
    if request.method == 'POST':
        query="Generate Detailed RoadMap to be a Social Media Influencer ethically and can start earning:- <br><br>"
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/fairy.html', **locals())

@views.route('/love_letter_generator', methods=["GET", "POST"])
@login_required
def love_generator():
    if request.method == 'POST':
        yt_title = request.form['title']
        yt_desc = request.form['desc']
        query='''Generate a detailed romantic love letter to your "{}" "{}" with your love assent:- <br><br>'''.format(yt_title, yt_desc)
        print(query)
        openAIAnswerUnformatted = prompt.openAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')

    return render_template('/home/love.html', **locals())

