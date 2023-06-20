# The Terminal Chatbot app
A basic implementation of a LangChain chatbot app operated from terminal.

This project is a demonstration of how Aim enables building an observability and automation artifact for every AI System.

## What's in the repo
### Structure
This repo contains two python packages:
- **chatbot**: the chatbot implementation with LangChain
- **chatbot_logger**: end-to-end custome observability package for chatbot built with Aim framework.

### About Aim
Aim is an easy-to-use open-source development framework for building AI Systems observability and automation.

Aim enables three building blocks:
- Define and Log AI metadata from everywhere in AI Infra into centralize
- Build low-code custom observability for logged metadata
- Build automations for logged metadata.

The observability built with Aim is a new artifact in AI Systems - a composable custom observability & automation layer that deeply reflects the relationship between different components of the AI System.

Aim is composable. The building blocks can be packaged as python packages and reused across different projects.

Such as `chatbot_logger`.

Aim's mission is to democratize AI Dev tools to recover the broken AI Systems development lifecycle.

## Getting Started with the Chatbot

### Installation
1. Clone the repo
2. Add `.env` file at `chatbot` with `serpapi_key` and `openai_key` keys
2. Install the logger `pip install -e ./chatbot_logger` (in editable mode)
3. Install the chatbot `pip install -e ./chatbot` (in editable mode)

### Chatbot usage and development

There are two modes of chatbot iteration: Dev and Production.

#### Production
Execute `cd chatbot && chatbot run` to run the chatbot.
Each chatbot run is a "production" run and uses the version number from `chatbot/VERSION` as its release version.

#### Dev
Execute `cd chatbot && chatbot run --dev` to run the chatbot

## Observability with Aim
The chatbot_logger built with Aim tracks the chatbot both across development and production.

### Using Aim
- Start Aim UI: `aim up --package chatbot_logger`
- Checkout Aim docs: `aim up --port 43001 --package docs`

### The chatbot development toolkit
- **Overview page:** full overview of the development and releases of the chatbot
- **Production page:** full overview of the production sessions by the users 
- **User Activity page:** select user and see the users' activity
- **User Session page:** observe the User sessions on the chatbot in detail
- **Logs Discovery page:** all the logs tracked by Aim.

### Using the built-in playground documentation
Aim comes with a built-in playground documentation.
Here is how to start it: `aim up --port 43001 --package docs`
This command will start an Aim instance that's also a playground documentation to experiment with and customize your toolkit.

### Next steps: make it your own
There are many ways this package can be extended
- Add new metrics that track chatbot efficiencies
- Add aggregate metrics of the openai cost
- potentially restructure the whole package to better see the lineage of the experiment -> dev session -> release -> user session -> issue -> experiment ->...
