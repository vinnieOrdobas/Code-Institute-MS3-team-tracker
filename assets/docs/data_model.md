# Team Tracker Data Model

## Overview

Managing large quantities of structured and unstructured data is a primary function of information systems - data models describe the structure, manipulation and integrity aspects of the data stored in a data management system.

## Collections

### Teams

> - The "Teams" collection is where we keep documents that describe teams and segregate their staff. It has a one-to-many relationship with the "Users" collection (an user can only have one team, but a team can have many users) and with the "Trainings" collection (a training course belongs to one team, but a team can have multiple training courses).
>

### Training Types

> - The "Training Types" collection holds data regarding the types of Cycles embedded in each training - they serve as a reference, therefore it is a static collection. It relates to the "Trainings" collection through a one-to-many relationship (a Cycle can only be of one training type, but there can be multiple Cycles with one particular training type).
>

### Trainings

> - This is the collection where training documents are stored - they're segregated by teams (a many-to-one relationship, as describe in the "Teams" collection) which means that trainings are rendered differently depending on what team the user requesting the data is placed. This collection is connected to the "Users" collection through a many-to-many relationship (trainings can be assigned to many users, and users can be enrolled in many trainings). This set of documents has a particularity under the key "training_cycle" - this is a series of embedded documents that contains metadata regarding the multiple Cycles a training can have (limited to three - the same amount of documents in the static collection "Training Types", which is related to the trainings collection through one-to-many relationship, described above). Fields in this object are "keys" that are named after the training types (Training Deck, Shadowing and Reverse Shadowing) that are themselves embedded objects containing metadata about the Cycle in question. The paths are as follows: "Training/training_cycle/Cycle(aka training type)".
>

### Users

> - This is the largest collection in the data model, and this is where the majority of the data points are recorded. The users collection defines access levels, training folders, teams and many other data points that are vital for Team Tracker. This collection is related to the teams collection via a many-to-one relationship (Teams can have multiple users, but users can only have one Team), and this serves to segregate teams and their roster. This encapsulation is needed to render information that's relevant to one team/user. Here we define access for using the system, with boolean values under the fields: "student", "instructor, "team_leader" and "admin". For an user to be granted an acess level, it only needs to have the key value pair with "True" - users can have multiple access levels, and the keys are not exclusive. The field "trainings" (this key is only created for users that have the "student" access level) is the training folder that keeps records for students. Through this key, the collection relates to the "Trainings" collection, via a many-to-many relationship (trainings can be assigned to many users, and users can be enrolled in many trainings). This field is an embedded document, where the field "training_name" in the training document (stored in the "Trainings" collection) serves as a key for the next level embedding: the value pair for the training key contains metadata about the Cycles created for the particular training. Cycles serve as keys for yet another embedded document (just like the "Trainings" collection, under the "training_cycle" field). The paths are as follows: "User/trainings/Training/Cycle(aka training type)".

## Data Schema

> - For the data schema, please follow this [link](data_schema.png)