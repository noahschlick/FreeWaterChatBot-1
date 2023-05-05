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

## Conclusion:
FreeWater Chatbot is a simple chatbot that demonstrates how to use an AI model to respond to user messages on Discord. It can be easily deployed on any hosting platform that supports Python.