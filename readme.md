# MasterBot

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

7. Fill in the `CONFIG.py` file
8. Place the `cert.pem` file if bot wants to use webhook
9. Start the master, `python main.py`

### Assumptions
1. All the bots should have a separate virtualenv (called env) within its folder
2. The last argument should be the alias (only alias will be used, not the name of the .py file)

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