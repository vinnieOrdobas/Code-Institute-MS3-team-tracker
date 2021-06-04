# Team Tracker - Testing details

[Main README.md file](/README.md)

[View website in Heroku](https://team-tracker-ms3.herokuapp.com/)

## Testing

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) - To check validity of CSS Code.
- [W3C Markup Validation](https://validator.w3.org/) - To check validity of HTML Code.
- [web.dev](https://web.dev/) - To check responsiveness and audit the website.
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) - To check if mobile-friendly.
- [Web Page Test by Catchpoint](https://www.webpagetest.org/) - To test performance.

### Flow testing:

Usual flow through the app:

- Home > Log In > Profile > Training 
- Each page cluster (trainings/teams/profile) have an uncomplicated way to navigate the system and they all have trigger buttons linking to the adjacent endpoints/pages.

The landing page provides the background of the system -  The information is laid out as a Documentation page to not affect the user's experience.

### Testing user stories from "User Stories" section of README.md

1. _"As a trainer, my primary concern is to create content and to make sure my students have the best possible session, but I find myself wasting time trying to keep track of who attended training, and it'd be awesome to have a system to automate that."_
    1. At the moment of creation of a training, the instructor can assign it to student(s) and compare their attendance with the list of students. [Screenshot](user_stories1.1.JPG)
    2. Within each training, there is a button-trigger to check the list of students. [Screenshot](user_stories1.2.JPG)
    3. The list of students can be compared with the attendance and after each cycle, the trainer can mark it as complete and check back on the assigned student's profiles. [Screenshot](user_stories1.3.JPG)
2. _"I spend the majority of my time trying to allocate people to one particular task, but I can't never tell my own team's expertise. Having a visual aid to see their profile would be ideal because it would save me precious time."_
    1. The students registered in the system have a "training folder" collapsible which can provide information on what training/cycles the student is enrolled in. [Screenshot](user_stories2.1.JPG)
    2. In the student's profile, there's a button which triggers the student's certifications. [Screenshot](user_stories2.2.JPG)
3. _"At least once I week, I have either a team leader or a trainer sending me a spreadsheet with thousands of rows for ME to update my current training profile - it takes me ages to do it so and it's stressful. An user-friendly system would be welcome."_
    1. Each student's profile has a training folder that's visible for everyone - the student himself does not need to update his/hers profile as Team Tracker has a built-in automated tracking system, and as soon as the training/cycle is marked as complete, the training folder gets updated. [Screenshot](user_stories3.1.JPG)
    2. In the training page, there are button triggers that once activated mark the training/cycle as complete or incomplete, and those actions update. [Screenshot](user_stories3.2.JPG)

4. _"As someone who works cross-teams, I need a tool that can show me team boundaries so I can easily gather information and present metrics - organizational information shouldn't be time-consuming to be looked at."_
    1. There is a segregation between teams, they work as "islands" - members of the same team can see their teammates, but it isn't possible to see other teams. The System Administrator has a bird's-eye view of Teams and is able to access information across the board. [Screenshot](user_stories4.1.JPG)

### Manual testing

#### Home Page

1. Sticky Navigation bar:
    1. Check nav bar links to double check links are not broken.
    2. Change display sizes to check if elements positions are correct, specially the responsiveness of the nav bar.
    3. Within the 'burger' icon, check if elements are positioned to the left of the screen and check if sizes are adequate.
    4. Check functionality and responsiveness on mobile phones, tablets and other devices.

2. Background image:
    1. Go to "Home" page from a desktop.
    2. Check if image renders well on that breakpoint, if has 100vh of the screen and if logo and search form are positioned correctly.
    3. Emulate different resolutions to check if image is properly rendered on mobile.

3. Search form:
    1. Check "Spin" and "Refined Search" buttons are calling respective functions and leading the user where it was planned to.

4. Footer:
    1. Make sure the footer was on the right place - there are two versions of it, one for mobile and one for larger screens. _Here I encountered margin issues and positioning issues for the mobile footers_
    2. Try links on the footer to make sure they open a new tab and that they're not broken.
    3. Play along with different widths to make sure the footer behaves as meant in each breakpoint.

5. Review bullet points in different devices, such as tablets, phones and consoles.

#### Refined Search

1. Sticky Navigation bar:
    1. Replicate process applied to Home page, check if links are working.

2. Search form:
    1. Check if all the inputs in the form have appropriate width, if it is possible to type on them and if the range-sliders have enough space, both on Desktop and on smaller screens.
    2. Check if data input is valid and if API's accept request format. _Testing the data input I encountered a bug with the 'max calories' field, where you could pass a string rather than an integer. Changed input 'type' on HTML to fix it._
3. Call to action buttons:
    1. Check if call to action button is working and triggers function.
4. Footer:
    1. Replicate process applied to Home page, check if links are working.
    2. Check if footer poisitioning worked in all breakpoints. _Here I encountered a bug with the positioning, as the footer was fixed to the bottom of the screen and covered call to action button "Spin". Added a media query and styling for the containers within the footer to fix the issue._

5. Review bullet points in different devices, such as tablets, phones and consoles.

#### About Page

1. Sticky Navigation bar:
    1. Replicate process applied to Home page, check if links are working.
    2. Confirm that the Navigation Bar code and styling are the same on all breakpoints. 

2. Logo and Description:
    1. Make sure the logo is correctly positioned, check sizes and if the elements behave properly with larger screens.
    2. Double check if mobile version of the about page works properly, with positioning, borders and styling. 

3. Footer:
    1. Replicate process applied to Home page, check if links are working.
    2. Confirm that footer code and styling is identical on all pages.

4. Review bullet points in different devices, such as tablets, phones and consoles.

#### Results Page

1. Sticky Navigation bar:
    1. Replicate process applied to Home page, check if links are working.
    2. Confirm that the Navigation Bar code and styling are the same on all breakpoints.

2. Card deck:
    1. Double-check if API request has retrieved the appropriated recipes (according to the user's data input).
    2. Check if recipe cards render side-to-side and with identical width, icon-sizes and positioning.
    3. Check if card deck behaves as predicted on smaller devices.

3. Call to action buttons:
    1. Check if call to action button is working and triggers function.

4. Breadcrumbs:
    1. Check if breadcrumb links properly and if it renders properly on different breakpoints.
5. Footer:
    1. Replicate process applied to Home page, check if links are working.
    2. Confirm that footer code and styling is identical on all pages.
6. Review bullet points in different devices, such as tablets, phones and consoles.

#### Recipe Page

1. Sticky Navigation bar:
    1. Replicate process applied to Home page, check if links are working.
    2. Confirm that the Navigation Bar code and styling are the same on all breakpoints.

2. Rendered recipe:
    1. Check if card recipe was rendered correctly, if the image ratio is appropriate to the breakpoint.
    2. Check if recipe title rendered the right size and if the card header has appropriate width according to the breakpoint.
    3. Check if icon stats were rendered on the right format and on a formatted list.

3. Recommendation of the day widget:
    1. Test the size of the image rendered for the recommendation of the day is correct.
    2. Test if on smaller breakpoints, the widget gets moved to the bottom of the page with a call to action button.

4. Nutritional Information widget:
    1. Check if the nutritional information card widget rendered properly on various breakpoints.
    2. Check if collapsible element is populated with API's request and if the units are properly rounded.

5. Method and Ingredient list
    1. Check if method and ingredients are properly rendered according to the API request and if layout, styling and positioning are as planned.
    2. Check if units are properly rounded and transformated into fractions for the ingredient list. _Here I encountered a bug for repeating decimals (0.333); to solve the issue, rounded to the nearest float point._
    3. Check if the elements render on smaller breakpoints, as their order is meant to change.

6. Call to action buttons:
    1. Check if call to action button in the Recommendation of the Day widget works properly and triggers function.
    2. On smaller screen sizes, check if the adjacent call to action button works as intended.
    3. Check if call to action button to toggle nutritional information table functions regularly.

7. Breadcrumbs:
    1. Check if breadcrumb links properly and if it renders properly on different breakpoints.
8. Footer:
    1. Replicate process applied to Home page, check if links are working.
    2. Confirm that footer code and styling is identical on all pages.
9. Review bullet points in different devices, such as tablets, phones and consoles.

## Further testing

1. Published page on Heroku and shared on diverse social media - asked friends, family and fellow Code Institute students to test the website and let me know if any bugs should appear. _(Unsolved bug/Not able to reproduce) Bug reported on "index.html" - button "search" does not trigger function._
