<div align="center">
  <img src="https://github.com/alberttorosyan/langchain-chatbot/assets/3179216/8a31f9e6-50a0-42b9-afd8-9f2e0e7ab0c0">
  <h3>
    A basic implementation of a LangChain chatbot app operated from terminal.
  </h3>
  
  This is a demo project to show how Aim enables building an observability and automation layer for your entire AI System.
  
</div>

<br/>

<div align="center">
<img width="918" src="https://github.com/alberttorosyan/langchain-chatbot/assets/3179216/3c8c26f1-15a5-406d-9864-889e0d5212d9">
</div>

<h3 align="center">
  <a href="#ℹ️-about"><b>About</b></a> &bull;
  <a href="#using-the-chatbot"><b>Using the Chatbot</b></a> &bull;
  <a href="#observe-and-automate-with-aim"><b>Observe and Automate with Aim</b></a> &bull;
</h3>  


# ℹ️ About
## Repo Structure
This repo contains two python packages:
- **chatbot**: the chatbot implementation with LangChain
- **chatbot_logger**: end-to-end custome observability package for chatbot built with Aim framework.

## About Aim
Aim is an easy-to-use open-source development framework for building AI Systems observability and automation.

Aim enables three building blocks:
- Define and Log AI metadata from everywhere in AI Infra into centralize
- Build low-code custom observability for logged metadata
- Build automations for logged metadata.

The observability built with Aim is a new artifact in AI Systems - a composable custom observability & automation layer that deeply reflects the relationship between different components of the AI System.

Aim is composable. The building blocks can be packaged as python packages and reused across different projects.

Such as `chatbot_logger`.

Aim's mission is to democratize AI Dev tools to recover the broken AI Systems development lifecycle.

# Using the Chatbot

## Installation
1. Clone the repo
2. Add `.env` file at `chatbot` with `serpapi_key` and `openai_key` keys
2. Install the logger `pip install -e ./chatbot_logger` (in editable mode)
3. Install the chatbot `pip install -e ./chatbot` (in editable mode)

## Usage and development

There are two modes of chatbot iteration: Dev and Production.

### Production
Execute `cd chatbot && chatbot run` to run the chatbot.
Each chatbot run is a "production" run and uses the version number from `chatbot/VERSION` as its release version.

### Dev
Execute `cd chatbot && chatbot run --dev` to run the chatbot

# Observe and Automate with Aim
The chatbot_logger built with Aim tracks the chatbot both across development and production.

## Using Aim
- Start Aim UI: `aim up --package chatbot_logger`
- Checkout Aim docs: `aim up --port 43001 --package docs`

## The chatbot development toolkit
- **Chatbot System Lineage page:** full overview of the development and releases of the chatbot
<div align="center">
  <img width="918" src="https://github.com/alberttorosyan/langchain-chatbot/assets/3179216/328f8b10-b42c-4f9a-a8f0-b4f44c621e36">
</div>

- **Production Sessions page:** full overview of the production sessions by the users
<div align="center">
  <img width="918" src="https://github.com/alberttorosyan/langchain-chatbot/assets/3179216/a6a16d7f-81ba-436e-ae3d-b7cd8508a0e6">
</div>

- **User Analytics page:** select user and see the users' activity breakdown.
<div align="center">
  <img width="918" src="https://github.com/alberttorosyan/langchain-chatbot/assets/3179216/e3f0d6fe-62e4-424c-a5ed-4fb54554e486">
</div>

- **Production Session:** observe the User sessions on the chatbot in detail
<div align="center">
  <img width="918" src="https://github.com/alberttorosyan/langchain-chatbot/assets/3179216/ee050e2f-d3a6-47a3-82d7-79dfa0268d8a">
</div>

## Using the built-in playground documentation
Aim comes with a built-in playgroun
d documentation.
Here is how to start it: `aim up --port 43001 --package docs`
This command will start an Aim instance that's also a playground documentation to experiment with and customize your toolkit.
<div align="center">
  <img width="918" src="https://github.com/alberttorosyan/langchain-chatbot/assets/3179216/24175479-339a-4797-aca7-0262eadd1bca">
</div>


## Next steps: make it your own
There are many ways this package can be extended
- Add new metrics that track chatbot efficiencies
- Add aggregate metrics of the openai cost
- potentially restructure the whole package to better see the lineage of the experiment -> dev session -> release -> user session -> issue -> experiment ->...
