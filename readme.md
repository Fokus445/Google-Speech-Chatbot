# Google Speech Chatbot App

## Video

https://github.com/Fokus445/Google-Speech-Chatbot/assets/79461074/7684ddbe-3de3-4f8f-9355-e6333260bc3e

## Overview

This project builds a voice-powered chatbot using Google APIs and PyAudio for a microphone stream and a Pygame.mixer as a response player.

Here's how it works:

* Speech to Text: The user speaks a question or command. PyAudio captures the audio and converts it to text using Google Speech-to-Text API.
* Dialogflow Integration: The transcribed text is sent to Dialogflow ES, a natural language processing platform from Google. Dialogflow analyzes the intent and retrieves the appropriate response.
* Text to Speech: The response generated by Dialogflow is converted back to natural-sounding speech using Google Text-to-Speech API.
* Interactive Conversation: The synthesized speech is played back to the user using the Pygame music player, creating a real-time conversation experience.

## Problem Solved

Imagine a future where scheduling a doctor's appointment is as easy as having a conversation! Chatbots powered by AI will be able to handle these tasks, freeing up receptionists and giving you more control. Instead of waiting on hold, you'll chat with a bot that can access your schedule, answer your questions about procedures, and patiently wait as you explain your needs. No more feeling rushed – chatbots will take the time to get things right for you.

## Installation

Enable above mentioned Google API services. Create a service account and JSON key. Add intents to Dialogflow ES.

    pip install -r requirements.txt

Run the chatbot:

    python run.py
