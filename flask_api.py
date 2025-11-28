#flask_api.py
# A flask web app for my digital resume/portfolio
# httml and css code are from llm model  // stated by sir 
from flask import Flask
app = Flask(__name__)

@app.route("/")      
def home():
    return"""


{% extends "base.html" %}
{% block content %}

<style>
/* Dark background */
body {
    background: linear-gradient(135deg, #101325, #0b0e20);
    color: white;
    margin: 0;
    font-family: Arial, sans-serif;
}

.hero {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 80px 10%;
}

.hero-left h1 {
    font-size: 3.8rem;
    font-weight: 800;
    margin-bottom: 10px;
}

.hero-left h1 span {
    color: #00eaff;
    text-shadow: 0 0 15px #00eaff;
}

.hero-left p {
    font-size: 1.2rem;
    margin: 10px 0 25px;
    max-width: 500px;
    opacity: .9;
}

.btn {
    padding: 12px 28px;
    border-radius: 50px;
    display: inline-block;
    text-decoration: none;
    font-size: 1rem;
    border: none;
    margin-right: 12px;
    transition: .3s;
}

.primary-btn {
    background: #00eaff;
    color: black;
}

.outline-btn {
    background: transparent;
    border: 2px solid #00eaff;
    color: #00eaff;
}

.btn:hover {
    transform: translateY(-4px);
}

.profile-card {
    background: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 25px;
    width: 290px;
    text-align: center;
    backdrop-filter: blur(10px);
}

.profile-card img {
    width: 130px;
    height: 130px;
    object-fit: cover;
    border-radius: 50%;
    border: 3px solid #00eaff;
    margin-bottom: 15px;
}

.profile-card p {
    font-size: .95rem;
    margin: 5px 0;
}

.social-link {
    color: #00eaff;
    text-decoration: none;
    font-weight: bold;
}

.social-link:hover {
    text-decoration: underline;
}

/* Mobile responsive */
@media(max-width: 900px){
    .hero {
        flex-direction: column;
        text-align: center;
    }
    .hero-left {
        margin-bottom: 25px;
    }
}
</style>


<section class="hero">
    <div class="hero-left">
        <h1>Hi, I'm <span>Aditya Raj</span></h1>
        <p>Aspiring Software Developer & Tech Enthusiast</p>

        <a href="{{ url_for('projects') }}" class="btn primary-btn">Projects</a>
        <a href="{{ url_for('skills') }}" class="btn outline-btn">Skills</a>
        <a href="{{ url_for('contact') }}" class="btn outline-btn">Contact</a>
    </div>

    <div class="profile-card">
        <img src="{{ url_for('static', filename='images/profile.jpg') }}">
        <p><strong>Location:</strong> Jaipur, India</p>
        <p><strong>Email:</strong> youremail@example.com</p>
        <p><strong>GitHub:</strong>  
           <a class="social-link" href="https://github.com/Adityaraj917" target="_blank">@Adityaraj917</a>
        </p>
        <p><strong>LinkedIn:</strong> linkedin.com/in/yourprofile</p>
    </div>
</section>

{% endblock %}

    """


@app.route("/about")

def about():
    return """
{% extends "base.html" %}

{% block content %}
<style>
/* Reuse global style theme from homepage */
body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    color: #fff;
}

/* Page Header */
.page-header {
    text-align: center;
    padding: 60px 10%;
    animation: fadeSlideDown 1s ease-in-out forwards;
    opacity: 0;
}

@keyframes fadeSlideDown {
    from { opacity: 0; transform: translateY(-40px); }
    to { opacity: 1; transform: translateY(0); }
}

.page-header h1 {
    font-size: 3rem;
    margin-bottom: 10px;
}

/* Grid Layout */
.grid-2 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 35px;
    padding: 0px 10% 70px;
}

/* Card Styling */
.card {
    background: rgba(255,255,255,0.09);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 35px;
    border-radius: 20px;
    animation: floatUp 1.2s ease-in-out;
    transform: translateY(30px);
    opacity: 0;
    animation-fill-mode: forwards;
}

.card:nth-child(1){
    animation-delay: 0.3s;
}
.card:nth-child(2){
    animation-delay: 0.6s;
}

@keyframes floatUp {
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.card h2 {
    font-size: 1.8rem;
    color: #00e1ff;
    margin-bottom: 12px;
}

.card p,
.card li {
    font-size: 1.05rem;s
    line-height: 1.6;
}

/* List */
.list {
    list-style: none;
    padding: 0;
}
.list li {
    margin-bottom: 15px;
}

/* Hover interaction */
.card:hover {
    transform: translateY(-8px);
    transition: 0.3s;
}

/* Responsive */
@media(max-width: 768px){
    .page-header h1 {
        font-size: 2.3rem;
    }
    .card h2 {
        font-size: 1.5rem;
    }
}
</style>

<section class="page-header">
    <h1>About Me</h1>
    <p>A quick introduction to who I am and what I do.</p>
</section>

<section class="grid-2">
    <div class="card">
        <h2>Profile</h2>
        <p>
            I am a motivated learner with a strong interest in web development,
            Python programming, and building practical projects that solve problems.
        </p>
        <p>
            I enjoy working on both frontend and backend, exploring new tools,
            and continuously improving my skills.
        </p>
    </div>

    <div class="card">
        <h2>Education</h2>
        <ul class="list">
            <li>
                <strong>Bachelor of Technology in Computer Science</strong><br>
                Your College Name, 2022–2026 (Expected)
            </li>
            <li>
                <strong>Higher Secondary Education</strong><br>
                Your School Name, Completed 2022
            </li>
        </ul>
    </div>
</section>
{% endblock %}


    """

@app.route("/skills")      
def skills():
    return """
{% extends "base.html" %}

{% block content %}
<style>
/* ===== Global Dark Theme (Same as other pages) ===== */
body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: linear-gradient(135deg, #0d0d21, #11152d);
    color: #ffffff;
}

/* Page Header */
.page-header {
    text-align: center;
    padding: 60px 10%;
    animation: fadeDown 1s ease forwards;
    opacity: 0;
}

.page-header h1 {
    font-size: 3rem;
    margin-bottom: 10px;
}

@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-35px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ===== Grid Layout ===== */
.grid-3 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 35px;
    padding: 0 10% 70px;
}

/* ===== Skill Card Styling ===== */
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 35px;
    border-radius: 20px;
    text-align: center;
    opacity: 0;
    transform: translateY(35px);
    animation: cardFadeUp 1.2s forwards;
}
.card:nth-child(1) { animation-delay: .3s; }
.card:nth-child(2) { animation-delay: .5s; }
.card:nth-child(3) { animation-delay: .7s; }

@keyframes cardFadeUp {
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.card h2 {
    font-size: 1.6rem;
    color: #00eaff;
    margin-bottom: 18px;
    text-shadow: 0px 0px 8px #00eaff;
}

/* ===== Tags (Skills Badges) ===== */
.tags {
    list-style: none;
    margin: 0;
    padding: 0;
}

.tags li {
    display: inline-block;
    background: rgba(0, 234, 255, 0.2);
    border: 1px solid #00eaff;
    color: #00eaff;
    padding: 8px 18px;
    font-size: 0.95rem;
    border-radius: 50px;
    margin: 6px;
    transition: 0.3s;
}

.tags li:hover {
    background: #00eaff;
    color: #000;
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0px 0px 12px #00eaff;
}

/* Responsive */
@media(max-width: 768px){
    .page-header h1 {
        font-size: 2.4rem;
    }
}
</style>

<section class="page-header">
    <h1>Skills</h1>
    <p>Technologies and tools I work with.</p>
</section>

<section class="grid-3">
    <div class="card">
        <h2>Programming Languages</h2>
        <ul class="tags">
            <li>Python</li>
            <li>JavaScript</li>
            <li>C/C++</li>
        </ul>
    </div>

    <div class="card">
        <h2>Web Development</h2>
        <ul class="tags">
            <li>HTML5</li>
            <li>CSS3</li>
            <li>Flask</li>
            <li>React (Basics)</li>
        </ul>
    </div>

    <div class="card">
        <h2>Other Skills</h2>
        <ul class="tags">
            <li>Git & GitHub</li>
            <li>Problem Solving</li>
            <li>Team Collaboration</li>
            <li>Communication</li>
        </ul>
    </div>
</section>
{% endblock %}



    """

@app.route("/projects")      
def projects():
    return """
{% extends "base.html" %}

{% block content %}
<style>
/* ===== Global Dark Theme ===== */
body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: linear-gradient(135deg, #0d0d21, #11152d);
    color: #fff;
}

/* Page Header */
.page-header {
    text-align: center;
    padding: 60px 12%;
    animation: fadeDown 1s ease forwards;
    opacity: 0;
}
@keyframes fadeDown {
    from { opacity: 0; transform: translateY(-40px); }
    to { opacity: 1; transform: translateY(0); }
}
.page-header h1 {
    font-size: 3rem;
    margin-bottom: 12px;
}

/* ===== Project Grid Layout ===== */
.projects {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(330px, 1fr));
    gap: 30px;
    padding: 0 12% 70px;
}

/* Project Cards */
.project-card {
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    transition: 0.35s;
    transform: translateY(30px);
    opacity: 0;
    animation: fadeUp 1.2s forwards;
}

.project-card:nth-child(1){ animation-delay: .3s; }
.project-card:nth-child(2){ animation-delay: .5s; }
.project-card:nth-child(3){ animation-delay: .7s; }

@keyframes fadeUp {
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

.project-card h2 {
    color: #00eaff;
    text-shadow: 0px 0px 10px #00eaff;
    margin-bottom: 10px;
}

/* Hover Effects */
.project-card:hover {
    transform: translateY(-12px);
    box-shadow: 0px 0px 15px #00eaff77;
}

/* Project Text */
.project-card p {
    font-size: 1rem;
    line-height: 1.5;
}

/* GitHub Links */
.text-link {
    display: inline-block;
    margin-top: 15px;
    color: #00eaff;
    font-weight: bold;
    text-decoration: none;
    border-bottom: 2px solid #00eaff;
    transition: 0.3s;
}
.text-link:hover {
    color: #000;
    background: #00eaff;
    padding: 5px 10px;
    border-radius: 5px;
}

/* Responsive */
@media(max-width: 780px){
    .page-header h1 { font-size: 2.3rem; }
    .project-card h2 { font-size: 1.4rem; }
}
</style>

<section class="page-header">
    <h1>Projects</h1>
    <p>Some of the work I've done recently.</p>
</section>

<section class="projects">
    <article class="card project-card">
        <h2>Flask Digital Resume Website</h2>
        <p>
            A personal portfolio website built using Flask, showcasing my
            resume, skills, and projects with a modern UI.
        </p>
        <p><strong>Tech:</strong> Flask, HTML, CSS</p>
        <a href="#" class="text-link">View Code (GitHub)</a>
    </article>

    <article class="card project-card">
        <h2>Task Manager App</h2>
        <p>
            A simple command-line task manager to add, edit, and delete tasks,
            built in Python with file-based storage.
        </p>
        <p><strong>Tech:</strong> Python</p>
        <a href="#" class="text-link">View Code (GitHub)</a>
    </article>

    <article class="card project-card">
        <h2>Student Result Dashboard</h2>
        <p>
            A small web app to display student marks and performance summary
            using clean tables and charts.
        </p>
        <p><strong>Tech:</strong> HTML, CSS, JavaScript</p>
        <a href="#" class="text-link">View Code (GitHub)</a>
    </article>
</section>
{% endblock %}

    """
    
if __name__=='__main__':
    app.run()