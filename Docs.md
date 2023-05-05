## Introduction

FreeWater Chatbot is a user-friendly and interactive chatbot designed to answer questions and provide information about the innovative FreeWater advertising platform. The platform provides an eco-friendly alternative to bottled water. The chatbot is built using Python and utilizes an AI model to provide accurate and timely responses to user messages. The chatbot is hosted on Replit, a powerful online code editor and hosting platform, making it easy to deploy and manage. With its intuitive interface and rich features, FreeWater Chatbot is an excellent tool for anyone looking to learn more about this revolutionary platform.
## Project Structure
The project contains four Python files: main.py, bot.py, freeWaterAPI.py, and webserver.py.
### main.py:
This file is the main entry point for the application. It loads the environment variables using the python-dotenv package and starts the Discord bot using the run_discord_bot() function in the bot.py file.
### bot.py:
This file contains the main functionality for the Discord chatbot. The run_discord_bot() function initializes a Discord client and starts listening for messages. It uses the freeWaterAPI.py file to get responses to user messages and sends them back as a private message or a message in the channel. The send_message() function in the bot.py file sends the message response.
### freeWaterAPI.py:
This file contains the function to call the FreeWater AI API and get a response to a user's input message. You can view the FreeWater AI API in https://github.com/noahschlick/FreeWaterChatBotAPI
### webserver.py:
This file contains a Flask application that listens on a specified port and responds with a "Im Alive" message. It is used to keep the bot alive. UptimeRobot is used to monitor the bot and keep ping the bot every 5 minuets to keep the bot alive.

## Deployment
The project can be deployed on any hosting platform that supports Python, such as Replit. Before deploying, the following steps should be taken:
1. Create a Discord bot and obtain the bot token.
2. Create an account on Replit and create a new project.
3. Add the following dependencies to the requirements.txt file: discord, python-dotenv, Flask, and requests.
4. Create a .env file and add the Discord bot token to it.
5. Copy the code from the four Python files into the corresponding files in the Replit project.
6. Start the Flask application using the keep_alive() function in the webserver.py file.
7. Start the Discord bot using the run_discord_bot() function in the bot.py file.

## Set up and installation
 1. The first thing that I did was set up a discord bot. The Discord bot was can be seted up in the discord developer portal in the discord website (log in with regular discord accout). You can then create a new application and give the application a name. Once I created the application, I created the bot by going to the bot tab on the left side then clicked add bot. Under the bot tab you can customize the bot by adding a bot name and image. You can generate a token on this page by clicking the token button which will generate a token. I invited the bot to a server I created in my discord account. Under the OAuth2 tab in discord, select the bot scope and give it the permissions that you want your bot to have. Then copy the generated URL and paste it into your web browser. Choose the server that you want to invite your bot to and click authorize.
 2. To protect the token I added the token as an envirnment variable in replit. I also installed the package used for programming bots on python by entering pip install discord in to the shell. I then wrote to code for the bot to resond to messages in discord.
 3. I wrote The run_discord_bot function which initiates the discord bot using the DISCORD-TOKEN environment variable.
 4. I wrote the send_message function whichsends a resonse to the user in discord. I had already created the REST API that generates an response based off of the FreeWater training data at this point. The API takes in the user_message parameter and generates an educated resonse. I used the discord message object from the discord package to to write the response in discord. I wrote a try and except clause incase the API was not working to notify the discord users that the bot is not connected to the API.
 5. I used the Flask library in this project to create a directory for the bot to run. I used the threading to run the webserver while running the discord bot at the same time.
 6. I deployed the code on replit, which created a url for the program. I used a website called uptime-robot to monitor the url, and ping the url every 5 minuets so that program will continue to run on the replit server.  

## Conclusion:
FreeWater Chatbot is a simple chatbot that demonstrates how to use an AI model to respond to user messages on Discord. It can be easily deployed on any hosting platform that supports Python.