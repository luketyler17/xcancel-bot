# Discord Link Replacement Bot

This Discord bot listens to messages in a specific channel, detects Twitter URLs, replaces them with custom URLs, posts the modified message with the original user's mention, and embeds the new link for a clean display. The original message is deleted to avoid redundancy.

## Features
- Detects Twitter URLs in messages.
- Replaces the detected URL with a custom redirect URL.
- Posts a rich embed with the new URL, tagging the original user.
- Deletes the original message to maintain channel cleanliness.


## Feature Roadmap
- [X] Differentiate between image & video embedding and regular non-image/video based tweet to have the redirect to xcancel work for all users
- [X] Remove UTM Tracking from all twitter links seen
- Create duplicate link tracker (3/4 day max memory) and send user DM with location of previously sent tweet so they can view the discussion
---

## Setup and Installation

Follow these steps to set up the bot for your Discord server:

### 1. Prerequisites
- **Python 3.8 or later**: [Download Python](https://www.python.org/downloads/)
- **Pipenv or pip**: Ensure you have a package manager for Python installed.

### 2. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/luketyler17/xcancel-bot.git
cd discord-link-replacement-bot
```

### 3. Install Dependencies
Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```

The main dependencies include:
- `discord.py`: To interact with Discord's API.
- `python-dotenv`: To load environment variables.

### 4. Create a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **New Application** and give your bot a name.
3. Navigate to the **Bot** tab on the left and click **Add Bot**.
4. Under the bot settings:
   - Enable the **MESSAGE CONTENT INTENT**.
   - Enable **Server Members Intent** (optional, for advanced features).
5. Copy the **Bot Token**:
   - Under the **Bot** tab, click **Reset Token** and copy the generated token.
   - Save this token securely; it’s required to run the bot.

### 5. Create an `.env` File
Create a file named `.env` in the project directory and add the following:
```
BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
```
Replace `YOUR_DISCORD_BOT_TOKEN` with the token you copied from the Discord Developer Portal.

### 6. Add the Bot to Your Server
1. Navigate to the **OAuth2** tab under your application settings.
2. Under **OAuth2 > URL Generator**:
   - Select the `bot` scope.
   - Assign permissions:
     - **Read Messages/View Channels**
     - **Send Messages**
     - **Embed Links**
     - **Manage Messages**
3. Copy the generated URL and paste it into your browser.
4. Select the server where you want to add the bot.

---

## Running the Bot
To start the bot, run the following command:
```bash
python bot.py
```

---

## How It Works
1. The bot listens to messages in a specific channel.
2. If the message contains a Twitter URL, it:
   - Replaces the Twitter URL with a custom redirect URL.
   - Posts an embedded version of the modified message and tags the original user.
   - Deletes the original message to keep the channel clean.

---

## Customization
- **Replacement URL Base**: Customize `BASE_URL` in the code to match your redirection needs.

---

## Example in Action

### Input:
```
Check this out: https://x.com/example/status/1234567890
```

### Output:
The bot sends an embed:
```
New Link Replacement
Original message by @UserName

Replaced Link
https://xcancel.com/example/status/1234567890

(Link replaced by bot)
```

The original message is deleted.

---

## Notes
- Ensure the bot has the following permissions in your server:
  - **Read Messages**
  - **Send Messages**
  - **Embed Links**
  - **Manage Messages**
---

## Troubleshooting
- **Bot not responding**: Ensure the bot token in the `.env` file is correct and the bot has the necessary permissions.
- **No embed displayed**: Make sure the bot has the **Embed Links** permission.

---

## License
This project is licensed under the MIT License. Feel free to customize and use it for your purposes. 

---