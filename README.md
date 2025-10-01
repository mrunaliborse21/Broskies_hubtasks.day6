# Broskies_hubtasks.day6
Task 6: Build a Portfolio Website with Flask

Overview
For Task 6, we were required to build a personal portfolio website using Flask, a micro web framework written in Python. The objective was to create a simple yet functional web application that showcases personal information and includes a contact form.

What We Built
We built a basic portfolio website that includes:

1. Home Page (index.html): A simple webpage that displays a brief introduction about the individual.
2. Contact Form: A form that allows visitors to send messages to the portfolio owner.
3. Flask Application (app.py): A Flask app that handles routing, rendering templates, and processing form submissions.

Why We Built It
The portfolio website was built to:

1. Demonstrate Flask skills: By using Flask, we demonstrated our ability to work with a Python web framework.
2. Create a personal online presence: A portfolio website is an excellent way to showcase one's skills, experience, and personality to potential employers or clients.
3. Practice web development: Building a portfolio website helped us practice web development skills, including HTML, CSS, and Python.

How We Built It
Here's a step-by-step breakdown of how we built the portfolio website:

Step 1: Setting Up the Project Structure
We created a new directory for the project and set up the following structure:
/portfolio_website
    /templates
        index.html
    /static
        /css
            style.css
    app.py
    requirements.txt

Step 2: Installing Flask
We created a requirements.txt file and added Flask to it. Then, we installed Flask using pip.

Step 3: Creating the Flask Application (app.py)
We wrote a Flask application that:

1. Handles routing: We defined routes for the home page (/) and contact form submission (/contact).
2. Renders templates: We used Flask's render_template function to render the index.html template.
3. Processes form submissions: We handled form submissions by retrieving the form data and printing it to the console.

Step 4: Creating index.html
We created an index.html file that:

1. Displays personal information: We added a brief introduction about the individual.
2. Includes a contact form: We created a form that allows visitors to send messages to the portfolio owner.

Step 5: Adding CSS (style.css)
We created a style.css file that adds basic styling to the website, including layout, typography, and colors.

Technical Details
- We used Flask 2.x (the latest version available) for building the web application.
- We used HTML5 and CSS3 for structuring and styling the website.
- We used Python 3.x (the latest version available) for writing the Flask application.

Challenges and Solutions
- Challenge: Handling form submissions and processing the data.
- Solution: We used Flask's request object to retrieve the form data and printed it to the console.

Conclusion
In conclusion, we built a basic portfolio website using Flask that showcases personal information and includes a contact form. We demonstrated our ability to work with Flask, HTML, CSS, and Python, and practiced web development skills. The website is a simple yet functional example of a personal online presence
