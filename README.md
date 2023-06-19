# Chatbot app for terminal
A basic implementation of a LangChain chatbot app operated from terminal.

This project also includes end-to-end Aim observability package.

### Repo Structure
There are two python packages in this repo:
- **chatbot**: the chatbot implementation with LangChain
- **chatbot_logger**: end-to-end custome observability package for chatbot built with Aim framework.

### About Aim
Aim is an easy-to-use open-source development framework for building AI Systems observability and automation.

Aim enables the following:
- Define and Log AI metadata from everywhere in AI Infra into centralize
- Build low-code custom observability for logged metadata
- Build automations for logged metadata.

These are the Aim building blocks.

Aim enables a new artifact in AI Systems - composable custom observability layer that deeply reflects the relationship between different components.
Aim is fundamentally composable. The building blocks can be packaged as python packages and reused across different projects.
Such as `chatbot_logger`.

Aim's mission is to democratize AI Dev tools and recover the broken AI Systems development lifecycle.

## Getting Started with the Chatbot
### Installation

1. Clone the repo
2. Add `.env` file at `chatbot` with `serpapi_key` and `openai_key` keys
2. Install the logger `pip install -e ./chatbot_logger` (in editable mode)
3. Install the chatbot `pip install -e ./chatbot` (in editable mode)

### Run

1. Start Aim server `aim server --package chatbot_logger`
2. Execute `cd chatbot && chatbot run` to run the chatbot

## Observability with Aim

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
