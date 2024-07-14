# MyAssistantBot

## Overview
MyAssistantBot is a personal assistant Telegram bot built using the aiogram 2.24 library. The bot helps automate various tasks, provides convenient features to assist in daily activities, and facilitates communication through a Telegram channel.

## Features
- **Task Automation**: Automate routine tasks.
- **Reminders**: Set reminders for important events and deadlines.
- **Information Retrieval**: Get information on various topics.
- **Custom Commands**: Easily extendable with custom commands to fit your personal needs.
- **SQLite Database**: Stores user data and bot-related information.
- **Channel Announcements**: Send advertisements or announcements to a Telegram channel.
- **User Messaging**: Users can send messages to you through the bot.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)
- A Telegram account and a bot token from BotFather

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/dostonshernazarov/Shernazarov_robot.git
    cd Shernazarov_robot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your bot token and channel ID:
    - Create a `.env` file in the root directory.
    - Add your bot token and channel ID to the `.env` file:
      ```env
      BOT_TOKEN=your_bot_token_here
      CHANNEL_ID=@your_channel_id_here
      ```

### Usage
1. Run the bot:
    ```bash
    python app.py
    ```

2. Open your Telegram app and search for your bot using its username. Start a chat with your bot and use the available commands.

## Project Structure
- **app.py**: The main bot application file.
- **handlers/**: Directory containing handler modules for different bot commands and events.
- **utils/**: Utility functions and helpers.
- **database/**: Contains SQLite database files and scripts.
- **requirements.txt**: Lists all the dependencies required for the project.

## Dependencies
All the dependencies required for this project are listed in the `requirements.txt` file. Below are the main libraries used:
- **aiogram==2.24**: For building the Telegram bot.
- **python-dotenv**: For loading environment variables from a `.env` file.
- **sqlite3**: For database management.

To install the dependencies, run:
```bash
pip install -r requirements.txt
