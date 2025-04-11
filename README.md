# Discord Role Assignment Bot

A simple Discord bot that automatically assigns a specified role to new members when they join the server. It also periodically checks existing members and assigns the role to those who don’t have it.

**Note:** After running the bot for a few hours, I personally had to restart the code due to it stopping working correctly. This may happen in some cases.

## Features
- Auto-assigns a role to new members upon joining.
- Periodically checks and assigns the role to members missing it.
- Logs role assignments in the console for easy tracking.

Perfect for managing user roles in Discord servers automatically.

## Setup
1. Clone or download the repository.
2. Install dependencies by running the provided `.bat` file or by typing `pip install colorama discord.py` in your Terminal.
3. Replace `YOUR_TARGET_ROLE_ID` and `YOUR_BOT_ROLE_ID` with the corresponding role IDs in your server.
4. Run the bot and enjoy automatic role assignments!
