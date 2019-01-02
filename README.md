# malshattabot

# About
A thread on reddit's /r/iceland inspired me to create a simple Icelandic discord bot, I already had an API service that delivers Icelandic sayings, called "málshættir" so I just found some premade code for a discord bot and tweaked it a little bit

## How to install

pip3 install requirements.txt
or
pip3 install discord.py==0.16.12

## How to configure 

Go to malshattabot.py, line 12 and put your bot's token there. if you want to replace the default '!malshattur' to call the bot, just change it in line 13

## How to run

Just run: python3 ./malshattabot.py, use screen or nohup to have it run persistantly, I was feeling lazy and didn't spend the time to make it a proper service
