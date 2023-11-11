from flask import Flask, render_template, jsonify

app = Flask(__name__)

skills = [
    "Java", "Python", "Salesforce Developer", "Web Development", "Team player",
    "Time Management skills", "Communication skills", "Problem-solving",
    "Critical Thinking", "Competitive Coding"
]
achievements = [
    "Salesforce Developer Virtual Internship (August - October 2023)",
    "Wipro Java Full Stack Certification (May – September 2023)",
    "E-box Java certifications in Java basics and advanced (February – September 2023)",
    "Part of Cybernauts organizing workshops, guest lectures, and industrial tours to ISRO, HYD, etc.",
    "Represented the class in various committees while conducting events like Ciencia2k23 for the complete tenure of 4 years B.Tech.",
    "Participated in various Olympiads during schooling."
]


@app.route("/")
def hello_world():
  return render_template('index.html', skills=skills, ach=achievements)


@app.route("/api/business")
def business_data():
  return jsonify(skills)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
