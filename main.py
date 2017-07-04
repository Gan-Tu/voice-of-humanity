from flask import Flask, render_template, url_for
app = Flask(__name__)


##################### Main Pages #####################
@app.route("/")
def index():
    params = {
        "use_page_loader": True,
        "news_logos": list(),
        "logo_urls": {
            11: "https://www.space.com/33445-voices-of-humanity-kickstarter-interstellar-flight.html",
            13: "https://uk.news.yahoo.com/kickstarter-project-aims-back-humanity-cosmic-cloud-183236176.html",
            15: "https://www.wired.com/2016/07/physicists-want-send-dna-space-lasers/",
            21: "https://www.noozhawk.com/article/voices_of_humanity_space_microchip_072716",
            22: "http://www.popsci.com/humanity-chip-wants-to-send-your-time-capsule-into-space"
        }
    }
    for i in range(1, 23):
        path = "img/news/logo{0}.png".format(i)
        params["news_logos"].append(url_for("static", filename=path))
    return render_template('index.html', params=params)

@app.route("/news")
def news():
    params = {
        "use_page_loader": True
    }
    return render_template('placeholder.html', params=params)

@app.route("/placeholder")
def placeholder():
    params = {
        "use_page_loader": True
    }
    return render_template('placeholder.html', params=params)

##################### Error Handling #####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

##################### Helper Functions #####################
def strip_html(html):
    return html.strip('#').strip('.html')

##################### Specific Pages #####################

@app.route("/store")
def store():
    params = {
        "use_page_loader": True
    }
    return render_template('placeholder.html', params=params)

# Projects

@app.route("/space_based_laser_applications")
def space_based_laser_applications():
    params = {
        "use_page_loader": True
    }
    return render_template('projects/space_based_laser_applications.html', params=params)

@app.route("/kickstarter")
def kickstarter():
    params = {
        "use_page_loader": True
    }
    return render_template('projects/kickstarter.html', params=params)

@app.route("/humanity_chip")
def humanity_chip():
    params = {
        "use_page_loader": True
    }
    return render_template('projects/humanity_chip.html', params=params)

# About
@app.route("/about_us")
def about_us():
    params = {
        "use_page_loader": True
    }
    return render_template('about/about_us.html', params=params)

@app.route("/technical_papers")
def technical_papers():
    params = {
        "use_page_loader": True
    }
    return render_template('about/technical_papers.html', params=params)

@app.route("/contact_us")
def contact_us():
    params = {
        "use_page_loader": True
    }
    return render_template('about/contact_us.html', params=params)

##################### Main App #####################
if __name__ == "__main__":
    app.run(debug=True)
