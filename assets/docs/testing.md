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

- Home > Results > Recipe 
- Pages have an easy path through buttons and calls to action. Some pages have breadcrumbs to facilitate the navegation between them.
Most common path through the website: 

Although the About page isn't part of the regular flow of the page, it gives a context and a background about the system. The information is straight-forward to not affect the user's experience.


### Testing user stories from "User Stories" section of README.md

1. _"I've tried to turn vegan a few times, but it is so hard to do it without planning! I wish there was a platform where I could simply type the ingredients I have and it turn out with bunch of recipes to try it."_
    1. The website conveys a standard "search engine" layout. The search bar is easily spotted in the home page. [Screenshot](../img/user_story-1.1.jpg)
    2. There is a sticky navigation bar across the entire website. From there, you can navigate back to look for recipes. [Screenshot](../img/user_story-1.2.jpg)
    3. Breadcrumbs provided between results - recipe in order for the user to navigate back towards the results. [Screenshot](../img/user_story-1.3.jpg)
    
2. _"My partner is vegan, and I always spend ages trying to find the best recipe to cook for her. It'd be awesome if there's a way for me to have different ideas with a simple tap of my finger."_
    1. From the home page, a simple tap on the button "Search" will load top rated recipes. [Screenshot](../img/user_story-2.1.jpg)
    2. Inside each recipe, there's a recommendation of the day widget, that loads random recipes for the user. [Screenshot](../img/user_story-2.2.jpg)
    
3. _"My friends and I are all big gym goers, and I've been trying to convince them to turn vegan for ages now, but it is so difficult to find resources out there that have (real) nutritional information online."_
    1. The recipes are rendered with Macros from the Result page, which helps the user decide if the recipe fit his requirements. [Screenshot](../img/user_story-3.1.jpg)
    2. There's a full nutritional information widget (collapsible information) which can be accesed from the recipe page. [Screenshot](../img/user_story-3.2.jpg)

4.  _"Working and studying take a lot of time, so cooking is not always possible - being vegan, that means my options are often reduced. I'd like to be able to find new ideas that fit in my schedule."_
    1. The recipe cards, rendered after the search, have visual information about the prep time, which help the users decide if fit their time frames. [Screenshot](../img/user_story-4.1.jpg)

5. _"I have a severe nut allergy, so I usually spend a lot of time researching about recipes, often looking for detailed information. It'd be handy if I could find recipes matching different options, such as allergens and ingredients."_
    1. The refined search page offers five different filters to customise the user experience - allergens being one of them. [Screenshot](../img/user_story-5.1.jpg)
    2. With controls such as max calories, max proteins, max fats and max carbs the user can further filter the results and follow personalised meal plan. [Screenshot](../img/user_story-5.2.jpg)


### Manual testing

#### Home Page:

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

#### Refined Search:

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

#### About Page:

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


#### Results Page:

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

#### Recipe Page:

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
    

## Further testing: 

1. Published page on Heroku and shared on diverse social media - asked friends, family and fellow Code Institute students to test the website and let me know if any bugs should appear. _(Unsolved bug/Not able to reproduce) Bug reported on "index.html" - button "search" does not trigger function._