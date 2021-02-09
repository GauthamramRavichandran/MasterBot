# MasterBot

Help control bots on your server

### Functions:
    
1. Pull the latest commit and restart the bot

### How to deploy?
1. `git clone https://github.com/GauthamramRavichandran/MasterBot`
2. `virtualenv env`
3. Activate the virtual environment by,
    
    `source env/bin/activate`
4. Install the requirements,

    `pip3 install -r requirements.txt`

5. Fill in the `CONFIG.py` file
6. Start the master, `python main.py`

### ⚠️ Known Issue
Once the masterbot restarts anyother program, the new program will be under the masterbot process tree. 
If masterbot killed for any reason, all the programs started via this bot will be terminated too. 

One way to safe kill this bot is to send SIGTERM signal, which will terminate this bot while preserving the child to continue execution.

#### How to send SIGTERM signal?
1. Open `htop`
2. Locate this bot by searching (F3 key)
3. F9 to kill > select SIGTERM

## DISCLAIMER

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.
