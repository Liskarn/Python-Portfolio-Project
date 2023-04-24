# Python Quiz game 

A simple movie quiz game made in python, wich runs in the terminal on Heroku.\
Users can test their knowledge about popular movie titels and actors. \
[Here is the game on Heroku!](https://python-quiz-game-liskarn.herokuapp.com/)\
![picture of the app onn am i responsive website!](/assets/images/am_i_responsive.png)\

## How to play 

Movie Quiz-game is a simple quiz game you play in the terminal.\
So you load the game on Heroku and you read the question and answer\
with A,B,C,D to the corresponding guess. When you have answerd all the\
questions you will see the result and wich one you missed.

# Features 

## Existing Features

- A set of questions in that are challenging and related to movies.\
![Picture of the landing screen for the game](/assets/images/landing_screen.png)

- The game gives you feedback if it is correct or not.\
![picture of incorrect answer](/assets/images/incorrect.png)
# Future features
- Randomize and build a bigger pool of questions, would like to try and pull questions from a database.
- more input controll was really rushed doing this project.
- 

# Data model 
I have to tuples that contain the data and the questions. 
The questions are pulled from on tuple and the answers from the other.
When the answer is inputed the guess is compared to the question number and the gueasses.

# Testing 
i have manually tested the application 
- The code padde trough the PEP8 linter and only had some line indention problem on my tuples.
and the strings where to long but it dont trow and error in the terminal.

# Bugs

- Did not get the score to show corectly think it is a math problem

# Remaining bugs

- Did not get the score to show corectly think it is a math problem

# validator testing 

- PEP8 
    - No Errors where returned from PEP8online.com

# Deployment

This project was deployed to Code institute's mock terminal for Heroku

- Steps for deployment:
    - Fork or Clone this repository
    - Create Heroku app
    - Set the building blocks to python and node JS in that order or it will not work
    - Link the Heroku app to the repository 
    - Click Deploy

# Credits 

- Code institute for the deployment terminal