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
> - [Bugs and Turnarounds](#bugs)
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

> - Team Tracker is a system that simplifies team's interactions, providing a platform in which everyone can store and request information regarding training and it is embedded with tools and metrics for data mining.


#### 1. Strategy

> The aim of this app is to offer a platform for users, teams and admins to integrate relevant information in one channel.
>
> ##### Project Goals:
>
> - To be a interactive platform for data storage, data mining and a tool to assess training metrics. 
>
> - Help users, team leaders and managers to find relevant information, metadata and to keep track of progression and evolution of their teams.
>
> - To simplify workflows, save time and fast-track training and progression.
>
> ##### Customer Goals:
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

> I've used Windows 98 layout as an inspiration, specially the colour scheme - the contrast between royal blue and pastel tones, which relates to user's experience to what a simple app should look like.

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

> - Add training endpoint only writing to database first option of the "assign_to" form - request.form.get('assign_to') is only writing the first item (it is supposed to write an array) - using the request.form.getlist method, I was able to get all of the aliases on an array and pass it to a handler function.
> - Nested accordion to show current cycle data in get_trainings page not opening due to an incompatibility between Materialize collapsibles and Google Chrome.
> - Star rating for each recipe were not accessing pseudo-classes in CSS (:after) to change width and fill color(yellow) according to property returned from the request. Found solution on: [A Simple JavaScript Technique for Filling Star Ratings](https://webdesign.tutsplus.com/tutorials/a-simple-javascript-technique-for-filling-star-ratings--cms-29450).
> - Script file wasn't able to find DOM Id's to be to render the recipe to another HTML page. The turnaround was offered by Victor (my mentor), by saving the target HTML element(the JSON object returned by the API and renderized as HTML) to 'localStorage', changing to another page using 'window.location.href' property and loading the saved content from 'localStorage'. 
> - Requesting information from the API through the page "refined_searhc.html" would return errors: "Illegal Invocation" and "Failed to fetch" - the first one was the error handling function that would create a modal. Hard-coded the model in a hidden state to turn around and spit the error message. Second bug occurred when creating the string to pass as parameter for the API's endpoint. Turn around was to create a hidden form element in the form object which validates user inputs to send the request. To do so, I used this tutorial: [How to Transform FormData into a Query String](https://ultimatecourses.com/blog/transform-formdata-into-query-string). After creating the string object, I chained it with a promise - followed this tutorial: [JavaScript Promise Tutorial: Resolve, Reject, and Chaining in JS and ES6](https://www.freecodecamp.org/news/javascript-es6-promises-for-beginners-resolve-reject-and-chaining-explained/).
> - Some particular recipes would come back with an "undefined" when rendering method for the recipe with the inside the function "renderRecipe", splitting the code and not loading the rest. The property [analyzedInstructions] of those recipes return and empty array. To handle the bug, I created a conditional statement to short-circuit the issue.
> - Main recipe's image and recommended recipe image would render stretched on the main axis in medium devices. Implemented media queries to shrink the ratio of the image on smaller screens.

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
> - The code was then pushed to GitHub where it is stored in my [Repository](https://github.com/vinnieOrdobas/Code-Institute-MS2-myVeganBuddy).
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
4. Navigate to the [Project GitHub repository](https://github.com/vinnieOrdobas/Code-Institute-MS2-myVeganBuddy).
5. Click the green button "Gitpod" in the top right corner of the repository.
6. This will create a gitpod workspace with the code from github where you can work locally.

To work on the project within a local IDE (such as VScode):

1. Follow this link to the [Project GitHub repository](https://github.com/vinnieOrdobas/Code-Institute-MS2-myVeganBuddy).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open the terminal.
5. Change the current working directory to the location where you want the cloned directory to ve made.
6. Type "git clone" on your terminal, then paste the URL of the project.

### Credits

> #### Media
>
> - Recipe images were provided by the API.
> - Background image was taken from [Pexels](https://www.pexels.com/).
> - Logos were created by illustrious [https://www.fiverr.com/illustriouss]. 
>
> ##### Content
>
> Text content was written by myself.
>
>
>
> ##### Code Snippets
>
> - [Rounding Decimals in JavaScript](https://www.jacklmoore.com/notes/rounding-in-javascript/) - To round ingredient units.
> - [How to transform integers with decimal points into fractions](https://gist.github.com/redteam-snippets/3934258) - To transform units to fractions.
> - [Sticky Navigation bar](https://bbbootstrap.com/snippets/responsive-navigation-bar-search-box-72587512)
>
>
---

> ##### Acknowledgments
>
> I would like to thank:
>
> - **Victor Miclovich**, my Mentor, for his insights, composure and experience. His invaluable assistance helped make this project reality.
> - **Anderson Gonçalves** for taking the time to meet me and talk about this project, for tips and incredible insights, but above all, for his friendship.
> - **Sofia Pereira** for her help on the general layout of the website.
> - **CI Mentors** for helping me identify and define problems.
> - **CI staff** for their care and affableness, and for always make sure I was in the right path.
> - **Slack Community** for their help with my code, for support and to make me feel part of the community.

##### Support

> For bug resolution, please reach Vinnie Ordobas on viniordobas@icloud.com

---