# What's this?

Hi,
as i needed some more help and information how exactly i getting this bot working, i want to edit the original readme a little bit, maybe it helps someone else to understand some steps better :D

### MasterBot

Control bots on your server. Easiest way to manage multiple bots. _Works for any .py scripts/bots, not just telegram bots_

### Functions:
    
1. Pull the latest commit and restart the bot
2. Gets current statistics of the server
3. Notifies admins when a bot is either killed/stopped

### How to deploy?
1. Clone the repo
`git clone https://github.com/GauthamramRavichandran/MasterBot`
2. Change directory 

   `cd MasterBot`
3. Create a new virtual environment

   `virtualenv env`
5. Activate the virtual environment by,
    
    `source env/bin/activate`
6. Install the requirements,

    `pip3 install -r requirements.txt`

7. Fill in the `CONFIG.py` file -> This file is in the "const" folder
8. Place the `cert.pem` file if bot wants to use webhook
9. Start the master, `python main.py`

### Assumptions
1. All the bots should have a separate virtualenv (called env) within its folder
1.1. Create a folder for your bot

    `mkdir my_bot_folder`
1.2. Make a virtualenv called "env" for your bot in your newly created folder

    `virtualenv env'
1.2.1 Activate it

    `source env/bin/activate`
1.3. clone your bot into the folder

    `git clone {repo}
2. The last argument should be the alias (only alias will be used, not the name of the .py file)
2.1. For example if you would start your bot with "`python3 main.py`" you should instead start it with "`python3 main.py AnyName`"
2.2. On telegram, you can text you bot private with `/get`to see all running .py files. And if you check the list
3. The list should be like this:

`List of py processes running
cmd     filename    alias

python3 main.py AnyName`
it could be longerm but this is what we are searching for.
If you see this, everything shout work fine

### Important Commands
The most important commands are:
`/get` - List all running py files
`/restart {alias}`- Restart you py file
If you started your bot with "`python3 main.py AnyName`", you can restart it by sending "/restart AnyName" to your bot on telegram.
Except yoou shouldnt use a name more than once, you can use everything as name.

You can list all commands by sending "`/help`" to your bot on telegram.


### ⚠️ Known Issue
Once the masterbot restarts anyother program, the new program will be under the masterbot process tree. 
If masterbot killed for any reason, all the programs started via this bot will be terminated too. 

One way to safe kill this bot is to send SIGTERM signal, which will terminate this bot while preserving its children to continue execution.

#### How to send SIGTERM signal?
1. Open `htop`
2. Locate this bot by searching (F3 key)
3. F9 to kill > select SIGTERM

## DISCLAIMER

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.


**Please feel free to raise an issue here if you have any queries**

### In addition to "What's this?":
Mainly i rewrote that to help other people that may have similar problems like me.
The second reason is:
IF I FORGET HOW THIS WORKS AGAIN; I DONT NEED TO ASK AGAIN AHAHAH
