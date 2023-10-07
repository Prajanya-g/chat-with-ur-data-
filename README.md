A Python application that allows you to interact with your tabular data using OpenAI's GPT-3 language model.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project combines the power of OpenAI's GPT-3 with a SQL database to enable natural language interactions with tabular data. You can ask questions or issue queries in plain English, and the application will provide relevant responses and data.

## Features

- Interact with your SQL database using natural language queries.
- Provides responses and data insights based on the user's questions.
- A user-friendly graphical interface for easy interaction.
- Error handling and feedback during query processing.

## Getting Started

### Prerequisites

- Python 3.7+
- SQLite3
- OpenAI API Key (Get it from [OpenAI](https://openai.com))

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Set up your environment by adding your OpenAI API key to `credentials.py`:

   ```python
   openAIKey = 'YOUR_API_KEY'
   ```

## Usage

1. Run the application:

   ```shell
   python main.py
   ```

2. The graphical interface will appear, allowing you to enter natural language queries. Type your questions and click the "Chat" button.

3. The application will process your query using GPT-3 and provide the results in the text box below.

4. Enjoy exploring and analyzing your tabular data effortlessly!

## Configuration

You can customize the behavior of the application by modifying the `config.py` file.

- Adjust GPT-3 settings, such as temperature and max tokens.
- Configure database settings if you're not using SQLite.
- Add additional features and improvements as needed.
