import os
from flask import Flask, request, render_template
app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "/home/junaid/Projects/DevOps/Flask-App/services/media"


@app.route("/home")
def home():
   return render_template('index.html')


@app.route("/")
def visit_home():
   return "Visit /home for home page"


# Route to upload image
@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            return render_template("upload.html", uploaded_image=image.filename)
    return render_template("upload.html")


@app.route('/static/IMG/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["IMAGE_UPLOADS"], filename)



if __name__ == "__main__":
   app.run(debug=True)
