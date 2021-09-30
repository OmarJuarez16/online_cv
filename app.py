from flask import Flask, redirect, url_for, render_template, send_file
from markupsafe import escape 

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    skills = {
    "Programming Languages": {
        "Python": 90, 
        "Ruby": 70},
    "Data & AI": {
        "Pytorch": 90, 
        "OpenCV": 90, 
        "PySpark":70, 
        "Pandas & Numpy": 90, 
        "Matplotlib & Seaborn": 90, 
        "Anaconda": 70}, 
    "Cloud Systems": {
        "Amazon S3": 60, 
        "Amazon Cloud 9": 60, 
        "Amazon EC2": 60}, 
    "Operating Systems": {
        "Windows": 80,
        "Linux": 95},
    "Web Development": {
        "HTML5": 85,
        "CSS": 80,
        "Falcon": 80,
        "Ruby on Rails": 75, 
        "Flask": 70},
    "Version Control": {
        "GIT": 80},
    "Databases & Containers": {
        "SQL": 70, 
        "Postgresql": 70, 
        "MySQL": 70, 
        "Docker": 70}, 
    "Languages": {
        "Spanish (Native)": 100,
        "English": 95, 
        "French": 50}
    }
    return render_template("about.html", skills=skills)

@app.route("/trajectory")
def trajectory():
    src_images = '/static/img/'
    experience =  {
        "Universidad de Monterrey": {
            "Dates": ["August 2016", "December 2020"], 
            "src": src_images + 'UDEM.jpg', 
            "description": """BSc. in Mechatronics. For the final project, as a team it was developed an algorithm that generated 
                                the phenotyping of grape clusters using <i>Python</i>, <i>OpenCV</i>, <i>AI</i>, and other tools."""},
        "University of Michigan": {
            "Dates": ["May 2020", "August 2020"], 
            "src": src_images + "UMICH.jpg", 
            "description": """Summer Undergraduate Research (SURE) 2020. Research was made on adversarial training, 
            using <i>Projected Gradient Descent (PGD)</i> technique. Some tools used for this research was <i>Python</i>, <i>Pytorch</i>, 
            <i>OpenCV</i>, <i>Google Colab</i>, among others."""}, 
        "GEO AI Analytics": {
            "Dates": ["October 2020", "August 2021"], 
            "src": src_images + "GEO.jpg", 
            "description": """Use thermal images to make an algorithm that detected solar panels. Also, worked with 
            satellite images to generate an AI algorithm which made car detection."""},
        "Globant": {
            "Dates": ["August 2021", "Present"], 
            "src": src_images + "Globant.jpg_large", 
            "description": """"""}

    }
    return render_template("trajectory.html", experience=experience)

@app.route("/certificate")
def certificate():
    certificates =  {
        "SURE Program": {
            "pdf": "SURE-UMICH-2020.pdf",
            "title": "SURE Program 2020",
            "institution": "University of Michigan", 
            "description": "Summer Undergraduate Research Program", 
            "area": "AI"    
        }, 
        "OWASP Top 10": {
            "pdf": "OWASP-Top-10.pdf",
            "title": "OWASP Top 10 Courses",
            "institution": "KnowBe4", 
            "description": "5 courses of OWASP Top 10 Web Application Security Risks", 
            "area": "Web Development" 
        }
    }
    return render_template("certificate.html", certificates=certificates)

@app.route("/download/<file>", methods=["GET"])
def download_certificate(file): 
    p = "static/pdf/"+ file
    return send_file(p, as_attachment=False)


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__": 
    app.run(debug=True)