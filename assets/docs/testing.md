# Team Tracker - Testing details

[Main README.md file](/README.md)

[View website in Heroku](https://team-tracker-ms3.herokuapp.com/)

## Testing

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) - To check validity of CSS Code.
- [W3C Markup Validation](https://validator.w3.org/) - To check validity of HTML Code.
- [web.dev](https://web.dev/) - To check responsiveness and audit the website.
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) - To check if mobile-friendly.
- [Web Page Test by Catchpoint](https://www.webpagetest.org/) - To test performance.

### Flow testing

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

1. Navigation bar:
    1. Click nav bar links to double check if they're not broken.
    2. Change display sizes to check if elements positions are correct, specially the responsiveness of the nav bar.
    3. Within the 'burger' icon, check if elements are positioned to the right of the screen and if the JavaScript embedded in the menu loads properly.
    4. Check functionality and responsiveness on mobile phones, tablets and other devices.

2. Landing Page Links:
    1. Check the links on table in the "Access Tiers" section to trigger modals.
    2. Check if "Button Lexicon" modal gets triggered by clicking the link.
    3. Check the "Test the app!" pulsing button to trigger demo accounts modal.
    4. Check "About" section round buttons for external links.

3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Log In Page

1. Log In form:
    1. Check if all the inputs in the form have appropriate width and if they're resposive on smaller screens.
    2. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
2. Call to action buttons:
    1. Check if the log in button triggers function and compares the input with data written in the database.
    2. Check if wrong login/password returns a valid response and directs the user to try again/or to register to use the app.
    3. Checks if "Register Account" link directs the user to the register endpoint.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Register Page

1. Register form:
    1. Check if all the inputs in the form have appropriate width and if they're resposive on smaller screens.
    2. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
    3. Check if the switches for "I'm a team leader" and "I'm an instructor" works properly.
    4. Check if the "Choose the Team" select form works properly and loads all of the Teams from the database.
2. Call to action buttons:
    1. Check if the Register button triggers function and writes the input to database.
    2. Check if username/alias are already registered and returns a valid response if that's the case it prompts the user to try again/login.
    3. Checks if "Log In" link directs the user to the login endpoint.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Profile Page

1. Profile Card:
    1. Check if the profile card renders correctly according to the user's profile, including "username", "alias", "team" and "access".
    2. Check if the "Profile Control Panel" renders properly according to the user's level of access.
    3. Check if profile card behaves as predicted on smaller devices.
2. Call to action buttons:
    1. Check if "See Certifications" button triggers the "Student Certification Modal" and renders the student's certifications.
    2. Check if "Change access level" button triggers the "Access Modal": check if the "OK" button triggers the "reset_access" function to reset user's access and assign new level according to the select form in the modal. Check if the "Cancel" button within the modal triggers the closing of the modal.
3. Training Folder:
    1. Checks if Training Folder renders correctly according to the user's enrolled training/cycles.
4. Review bullet points in different devices, such as tablets, phones and consoles.

#### Teams Page

1. Team Cards:
    1. Check if the team cards render properly with the Team's Name/Region/Description.
    2. Check if the "tabs" section of the card renders with the Team's staff under Team Leaders/Instructors/Students categories.
    3. Check if the links for each member leads to the right profile and are not broken.
2. Call to action buttons:
    1. Check if the "Add Team" button leads the user to the "Create Team" page.
    2. Check if the "Edit Team" button leads the user to the "Edit Team" page.
    3. Check if the "Delete Team" triggers the delete modal - check if the "Yes" button deletes the team and all of its staff/check if the "No" button closes the modal.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Create Team Page

1. Create Team form:
    1. Check if all the inputs in the form have appropriate width and if they're resposive on smaller screens.
    2. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
2. Call to action buttons:
    1. Check if "Submit" button creates team and if the inputs from the form are adequately written to database.
    2. Check if "Cancel" button leads back to the Teams page.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Edit Team Page

1. Edit Team form:
    1. Check if all the inputs in the form have appropriate width and if they're resposive on smaller screens.
    2. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
2. Call to action buttons:
    1. Check if "Submit" button edits team and its members correctly according to the form inputs and edits the right document in the database.
    2. Check if "Cancel" button leads back to the Teams page.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Trainings Page

1. Training Collapsibles:
    1. Check if for each training document in the database a collapsible renders correctly, with Team/Training Name/Date/Icon on the collapsible header.
    2. Check if the opening of the collapsible works as it should, even with multiple trainings "open".
    3. Check if the "Training Control Panel" card renders inside of the collapsible.
    4. Check if for each Cycle under the path: "{Training}/training_cycle" renders correctly.
    5. Check if "Cycle Control Panel" renders properly for each cycle inside of the collapsible.
    6. Check if the "Created By" data point renders properly and if the link to the user who created the training is not broken and leads to the right profile endpoint.
2. Call to action buttons:
    1. Check if the "Add Training" button leads to the "Create Training Page".
    2. Training Control Panel:
        1. Check if "Add Cycle" button leads to "Add Cycle" page.
        2. Check if "Enroll Students" button triggers "Enroll Student Modal" - check if the select form within the modal works, and if the button "Enroll" triggers function "enroll_training" and if the students selected in the select element have a key created under the path: "student/trainings/{Training}"; check if the "Cancel" button closes the modal.
        3. Check if the "Get Student List" button triggers "Student List" modal; check if the list of students with the enrolled users lead to each student's profiles; check if the "OK" button closes the modal.
        4. Check if the "Mark {Training} as Complete" button triggers the "complete_training" function and changes the status of the training to complete/edits training document under the path "{Training}/complete_training" and edits key in the database with the new boolean(True) value.
        5. Check if the "Mark {Training} as Incomplete" button triggers the "incomplete_training" function and changes the status of the training to incomplete/edits training document under the path "{Training}/complete_training" and edits key in the database with the new boolean(False) value.
        6. Check if the "Edit Training" button leads to the "Edit Training" page.
        7. Check if the "Delete Training" button triggers "Delete Training" modal - check if the "Yes" button in the modal deletes training document and wipes the training record within the enrolled students's training folder under the path: "student/trainings/{Training}"; check if the "No" button closes the modal.
    3. Cycle Control Panel:
        1. Check if "Complete Cycle" button triggers the "complete_cycle" function and updates the training document under the "{Training}/Training Cycle/{Cycle}/completed" key in the database with the new boolean(True) value.
        2. Check if "Incomplete Cycle" button triggers the "incomplete_cycle" function and updates the training document under the "{Training}/Training Cycle/{Cycle}/completed" key in the database with the new boolean(False) value.
        3. Checks if the "Edit Cycle" button leads to the "Edit Cycle" page.
        4. Checks if the "Delete Cycle" button triggers the "Delete Cycle" modal - check if the "Yes" button in the modal removes the folder under the path: "{Training}/Training Cycle/{Cycle}" from the training document and wipes the cycle record within the enrolled students's training folder under the path: "student/trainings/{Training}/{Cycle}"; check if the "No" button closes the modal.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Add Training Page

1. Add Training form:
    1. Check if the "Training Team" is in accordance with the user's team (the one creating the training).
    2. Check if the "Assign Training to" select element shows all of the students within the user's team (the one creating the training).
    3. Check if all the inputs in the form have appropriate width and if they're resposive on smaller screens.
    4. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
2. Call to action buttons:
    1. Check if "Submit" button creates training document and the students selected under the "Assign to" select element are correctly enrolled in the training - check if the training key is created under the path: "student/trainings/{Training}".
    2. Check if "Cancel" button leads back to the Trainings page.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Edit Training Page

1. Edit Training form:
    1. Check if the "Training Team" is in accordance with the user's team (the one editing the training).
    2. Check if all the inputs in the form have appropriate width and if they're resposive on smaller screens.
    3. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
2. Call to action buttons:
    1. Check if "Submit" button edits training and modifies enrolled students's training folder according to the form inputs and edits the right document in the database.
    2. Check if "Cancel" button leads back to the Trainings page.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Add Cycle Page

1. Add Cycle form:
    1. Check if the "Training Team" is in accordance with the user's team (the one adding the cycle to the training).
    2. Check if the "Training Name" is in accordance with the training's name that the user is adding the cycle to.
    3. Check if the "Cycle Type" select element shows all of the possible cycle types.
    4. Check if the "Instructor" select element shows all of the possible instructors within the user's team (the one creating the cycle).
    5. Check if all the inputs in the form have appropriate width and if they're resposive on smaller screens.
    6. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
2. Call to action buttons:
    1. Check if "Submit" button creates cycle and the enrolled students have the cycle created within their training folder under the path: "student/trainings/{Training}/{Cycle}" according to the form inputs and edits the right training document in the database.
    2. Check if "Cancel" button leads back to the Trainings page.
3. Review bullet points in different devices, such as tablets, phones and consoles.

#### Edit Cycle Page

1. Edit Cycle form:
    1. Check if the "Instructor" select element shows all of the possible instructors within the user's team (the one editing the cycle).
    2. Check if all the inputs in the form have appropriate width and if they're resposive on smaller screens.
    3. Check if the form validates inputs and if shows the red line underneath if the form is not filled properly.
2. Call to action buttons:
    1. Check if "Submit" button edits cycle and modifies enrolled students's training folder according to the form inputs and edits the right document in the database.
    2. Check if "Cancel" button leads back to the Trainings page.
3. Review bullet points in different devices, such as tablets, phones and consoles.

## Further testing

1. Published page on Heroku and shared on diverse social media - asked friends, family and fellow Code Institute students to test the website and let me know if any bugs should appear.