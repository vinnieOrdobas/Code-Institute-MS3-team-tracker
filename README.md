# Team Tracker

A cloud-based database desgined to serve as an aid for LMS systems, to keep track of team's information, access and profiles.

### Table of Contents

> - [Motivation](#motivation)
> - [Description](#description)
> - [User Stories](#userstories)
> - [UX](#ux)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [Resources](#resources)
> - [Testing](#testing)
> - [Bugs and Turnarounds](#bugs-and-turnarounds)
> - [Code validity](#code-validity)
> - [Version Control](#version-control)
> - [Deployment](#deployment)
> - [Credits](#credits)
> - [Acknowledgments](#acknowledgments)
> - [Support](#support)

### Motivation

> Companies spend a lot of resource and time to train their teams and to make sure they're ready to hit the ground running, but unfortunately the tools they use to keep track of that information is often archaic and leads to the fragmentation of the information.

### Description

> Team tracker is a system that simplifies data gathering and storage of information, specifically design to aid companies tracking the training aspect and integrate relevant information about their teams.

---

#### User Stories

> - _"As a trainer, my primary concern is to create content and to make sure my students have the best possible session, but I find myself wasting time trying to keep track of who attended training sessions, and it'd be awesome to have a system to automate that."_
> - _"I spend the majority of my time trying to allocate people to one particular task, but I can't never tell my own team's expertise. Having a visual aid to see their profile would be ideal because it would save me precious time. "_
> - _"At least once I week, I have either a team leader or a trainer sending me a spreadsheet with thousands of rows for ME to update my current training profile - it takes me ages to do it so and it's stressful. An user-friendly system would be welcome."_
> - _"As someone who works cross-teams, I need a tool that can show me team boundaries so I can easily gather information and present metrics - organizational information shouldn't be time-consuming to be looked at."_

---

### UX

> - Team Tracker is a system that simplifies team's interactions, providing a platform in which everyone can store and request information regarding trainings, users and teams.

#### 1. Strategy

> The aim of this app is to offer a platform for users, teams and admins to integrate relevant information in one channel.
>
> ##### Project Goals
>
> - To be a interactive platform for data storage, data mining and a tool to assess training metrics.
>
> - Help users, team leaders and managers to find relevant information, metadata and to keep track of progression and evolution of their teams.
>
> - To simplify workflows, save time and fast-track training and progression.
>
> ##### Customer Goals
>
> - Layout using Mobile-first approach.
> - Simple and functional design to increase usability.
> - Access-based platform to display personalised data.
> - Straightfowrad path to create trainings and to keep track of trainee's calendars.
> - Effortless way to sign-up and to login, for an accelerated workflow.
> - Track information personal information and cross-data with other teams.

#### 2. Scope

> The objective is to reach the threshold version of the app with enough usability - the Minimum viable product (MVP), that includes:
>
> - Authentication system for user to login/logout and sign-up.
> - Tier-based platform with different types of users and different types of accesses.
> - CRUD functionality to add, edit and create trainings/teams/users.
> - Users/teams profiles in order to centralize information.

#### 3. Structure

> The goal of the app is to render complex information in one simplified data stream, so the structure needs to translate that in a visual design - it was planned to stem from an already known convention to clarify the usage.
> It takes the structure of a simplistic convention of data, in a schema known to the user such as a webmail design - it takes the same layout and adds functionality in straight-forward format to convey information in a condensed shape.

#### 4. Skeleton

> - [Wire frames](assets/docs/wireframes.pdf): Webapp categorised in five different clusters.
>
> - Home, Login, Profile, Teams and Training.
>
> - Navigation bar - Links to each page.
>
> - Connected to external database (powered by MongoDB).

---

#### 5. Surface

> I've used Windows 98 layout as an inspiration, specially the colour scheme - the contrast between royal blue and pastel tones, which relates to user's experience of simplicity.

> ##### Colours
>
> - For the nav bar I've opted for a blue-grey tonality(#455a64) to create a contrast with the mild palettes I've used for the background.
> - For collapsible headers, profile cards, control panels and team cards I've chosen a darker blue-grey tone (#263238)
> - For body text, I've used a combination of shades of black for mild-coloured backgrounds - white for darker backgrounds. 
> - For the buttons in the control panel, please refer to the table below:

| Button      | Colour |
|    :----:   |    :----:   |
| Add Team      | #4caf50       |
| Add Training   | #4caf50        |
| Add Team   | #4caf50        |
| Add Cycle   | #4caf50        |
| Enroll Student   | #f57f17        |
| Get Student List  | #9575cd        |
| Get Training Description   | #fbc02d        |
| Edit Training   | #2196f3        |
| Edit Cycle   | #2196f3        |
| Delete Training   | #f44336        |
| Delete Cycle   | #f44336        |
| Mark as Complete   | #4caf50        |
| Mark as Incomplete   | #f9a825        |
| Change access level   | #f9a825        |
| See Student's certifications   | #4caf50         |  
---
> ##### Typography
> 
> - "Nunito" font (with fall-back font of Sans-Serif) for body content and titles.

### Features

#### Existing Features

> - Designed with HTML5, CSS3, Python, JavaScript and Materialize.
> - Navigation bar provides users the ability to engage with the system.
> - Landing page describing the project.
> - Connected to [MongoDB](https://www.mongodb.com/) Database/API
> - Register/sign-in functions to access the system.
> - Access tier based system to give users different experiences depending on their access level.
> - Profile page describing each user, with training folder attached.
> - CRUD functions wired to the database (MongoDB), ability to edit teams/trainings.

#### Features to implement

> - Metrics page to further enhance KDD.
> - In-app comms, such as messages/requests. 

---

### Technologies Used

#### 1. Languages

> - [HTML5](https://en.wikipedia.org/wiki/HTML5)
>
> - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
>
> - [JavaScript](https://www.javascript.com/)
>
> - [Python](https://www.python.org/)

##### 2. Integrations

> - [Materialize](https://materializecss.com/) - Classes for the overall layout of the website
>
> - [MongoDB](https://www.mongodb.com/) - Database
>
> - [FontAwesome](https://fontawesome.com/) - Card Icons, footer social media links
>
> - [Google Fonts](https://fonts.google.com/) - Typography
>
> - [jQuery](https://jquery.com/) - JavaScript Library
>
> - [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Python Library
>
> - [PyMongo](https://pymongo.readthedocs.io/en/stable/) - Python Library/Integration with MongoDB

##### 3. Workspace, version control and Repository storage

> - [VSCode](https://code.visualstudio.com/) - IDE
>
> - [Git](https://git-scm.com/) - Version Control
>
> - [GitHub](https://github.com/) - Repository Storage

##### 4. Other

> - [Autoprefixer](https://autoprefixer.github.io/) Parses CSS and adds vendor prefixes.
>
> - [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) Mobile-friendly check on site.
>
> - [Website Page Test](https://www.webpagetest.org/) Runs a website speed test from multiple locations around the globe using real browsers (IE and Chrome) and at real consumer connection speeds.
>
> - [Online-Spellcheck](https://www.online-spellcheck.com/) Online spelling and grammar checks.
>
> - [web.dev](https://web.dev/) Runs an audit on the website's performance.

### Resources

> - [Code Institute Course Content](https://courses.codeinstitute.net/) - Primary resource for this project.
> - [Balsamiq](https://balsamiq.com/wireframes/) - Wire framing design tool.
> - [Bootsrap Grid Explanation by Anna Greaves](https://ajgreaves.github.io/bootstrap-grid-demo/) - Resource for Bootstrap Grids.
> - [Stack Overflow](https://stackoverflow.com/) - Common questions.
> - [Youtube](https://www.youtube.com/) - Tutorials.
> - [CSS-Tricks](https://css-tricks.com/) - Quick CSS resources.
> - [Common Mark](https://commonmark.org/help/) - For Markdown language reference.
> - [Grid Citters](https://gridcritters.com/) - To learn CSS Grid technology.
> - [Coolors](https://coolors.co/) - Colours palette research.
> - [Adobe Resize Images](https://www.adobe.com/ie/photoshop/online/resize-image.html) - Resource for resizing images
> - [Tiny PNG](https://www.tinypng.com) - Resource to compress gallery images.
> - [Markdown Tutorial](https://www.markdowntutorial.com/) - Used to learn Markdown.
> - Code Institute **SLACK Channel** - Assistance.

### Testing

> External testing documentation can be found following this [link](assets/docs/testing.md).

---

### Bugs and turnarounds

> - In the "add_training" function, the form item "assign_to" was only getting the first select option, opposed to getting an array as this is a multiple HTML form; request.form.get('assign_to') was supposed to get a list of names.Found the solution on: [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/reqcontext/). I used the request.form.getlist method, to get all of the aliases on an array and pass it to a handler function.
> - The "edit_training" function wasn't able to find students enrolled in the "training_id" passed as parameter of this function, and wouldn't update any entries in the database as the PyMongo cursor object wouldn't return documents. I was trying to match the field "training_name" with the keys present in the students "training" embedded object. To fix this bug, I used "Query on Embedded/Nested Documents" commands on MongoDB with the "$exists" operator. Found the solution here: [MongoDB Documentation](https://docs.mongodb.com/manual/tutorial/query-embedded-documents/).
> - The "complete_cycle" function wasn't able to pass the name of the "cycle" to the backend to serve as a key for the request to the database. The turnaround was to create a hidden HTML form element called 'cycle_name' with the rendered jinja variable "{{ cycle }}" for each iteration and access the parameter with a "request.form.get('cycle_name')" to the function. To build this function, I've used this link: [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/reqcontext/).
> - The "get_teams" function wasn't able to initialise "System Admin" mode due to "UnboundLocalError: variable was referenced before assignment" - I was trying to pull data from the database depending on the type of user accessing the endpoint - the "System Admin" needs to have access to every team/staff in the system. With nested cases for each type of user, the script had to go down two "if" levels before finding what type of data it needed to search for, while trying to render this data on the frontend before finding the user access. To circumvent this barrier, I used a MongoDB aggregation pipeline to engineer the exact piece of data needed by this type of user. Found the solution and tutorial on: [MongoDB Documentation](https://docs.mongodb.com/manual/reference/operator/aggregation/lookup/)
> - On the 'get_trainings' endpoint, I had a bug rendering multiple Materialize Modals on the page, as there are three per training plus one modal per cycle (per training). Modal trigger buttons wouldn't function properly, as some of them would have the same "id" parameter in the HTML element. To fix this, I've attached the string "_{{ training.training_name }}" to render multiple modals depending on the element of iteration the 'get_trainings' function would render to the page. To circumvent the other part of the issue, I replaced the initialisation method of the Modals using the Materialize plugin rather than jQuery. Found the solution here: [Materialize Documentation](https://materializecss.com/modals.html).
> - To intialise the profile endpoint as a profile visitor, the "profile" function wasn't able to search for the user whose profile would be "visited" - it'd render the visitor profile. To overcome this barrier, I instantiated an HTML link element passing two arguments: "username" and "alias", the latter being the alias of the profile to be visited by the "username" in session. The "username" variable tells the "profile" function what's the level of access of the user in session, whereas the "alias" parameter sends the name of the user's profile to be visited to the database to be rendered on the page. Within the function, I've created a if case to tell if there was a parameter called 'alias', to which the function would be able to tell if this was a case in which the profile to be rendered would be the user in session or some other user. I've found part of the solution on: [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/reqcontext/).

---

### Code validity

> HTML - [W3C](https://validator.w3.org/) - Markup Validation
>
> CSS - [W3C](https://jigsaw.w3.org/css-validator/) - CSS Validation
>
> TAGS - [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) - Validates if tags are correctly closed.
---

### Version Control

> - Used Git for version control.

---

### Deployment

This project has been deployed on GitHub Pages with the following process:

> - All code was written on VS Code, an IDE.
> - The code was then pushed to GitHub where it is stored in my [Repository](hhttps://github.com/vinnieOrdobas/Code-Institute-MS3-team-tracker).
> - Under **Settings** I scrolled down to **GitHub** Pages section.
> - Under **Source** drop-down, the **Master branch** was selected.
> - Once selected, this publishes the project to **GitHub** Pages and displays the site url.
> - There is no difference between the deployed version and the development version.

#### How to run this project locally

To clone this project into your IDE you will need:

> - A **GitHub** account. Create one [here](https://github.com/join).
> - **Google Chrome** browser.

Follow this steps:

1. Install the [Gitpod Browser Extentions for Chrome](https://chrome.google.com/webstore/detail/gitpod-dev-environments-i/dodmmooeoklaejobgleioelladacbeki).
2. After installation, restart the browser.
3. Log into [Gitpod](https://www.gitpod.io/) with your gitpod account.
4. Navigate to the [Project GitHub repository](https://github.com/vinnieOrdobas/Code-Institute-MS3-team-tracker).
5. Click the green button "Gitpod" in the top right corner of the repository.
6. This will create a gitpod workspace with the code from github where you can work locally.

To work on the project within a local IDE (such as VScode):

1. Follow this link to the [Project GitHub repository](https://github.com/vinnieOrdobas/Code-Institute-MS3-team-tracker).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open the terminal.
5. Change the current working directory to the location where you want the cloned directory to ve made.
6. Type "git clone" on your terminal, then paste the URL of the project.

### Credits

> #### Media
>
>
> - Icons rendered by [Font Awesome](https://fontawesome.com/)
>
>
> ##### Content
>
> - Text content was written by me.
>
>
>

> ##### Acknowledgments
>
> I would like to thank:
>
> - **Victor Miclovich**, my Mentor, for his insights, composure and experience. His invaluable assistance helped make this project reality.
> - **Anderson Gonçalves** for taking the time to meet me and talk about this project, for tips and incredible insights, but above all, for his friendship.
> - **Camila Severo de Araujo Leite (Camichu)** for her overall help on creating the app, pointing out features and layout of the website.
> - **CI Mentors** for helping me identify and define problems.
> - **CI staff** for their care and affableness, and for always make sure I was in the right path.
> - **Slack Community** for their help with my code, for support and to make me feel part of the community.

##### Support

> For bug resolution, please reach Vinnie Ordobas on viniordobas@icloud.com

---