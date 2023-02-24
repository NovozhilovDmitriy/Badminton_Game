# Badminton Game Statistics
This code use Elo rating formula for count personal score of each player.

## Description
If several players want to play local championship and the same time to know progress of their playing, 
they need collect players data and count rating. This code exactly for such task.
The team will know personal rating and also could start (by start day/ end day) championship
Code use SQLite DB for store games data (date of play/players/ score of play) and then
process this data every time for create final result.
This was done for optimization process. In any time you can change formula of calculation
and all statistics will recreate automatically.

## Usage
For windows use I compile main.exe file. For details use Compile chapter. 
For correct use should exist several files:
- description.txt - this is template with description of each report what will import to excel
statistics file every time what code run
- Games.xlsx - this is list of all games. Please use correct templates because code don't process all
unexpected data and could generate error
- list_of_games.db - this is SQLite DB file what will generate automatically each time. 
Keep it in the same folder of code
- Total_Stat.xlsx - this is report file, it will delete and create from begining every time.
- config.ini - this if config file, where you can configure champiship start time and end time
and configure name of Games excel list. (PS: name should be Latin characters)

## Compiler
From my enviroment I use this command for create one package
``` python
pyinstaller --onefile --hidden-import=xlsxwriter --hidden-import=pandas --hidden-import=openpyxl --hidden-import=configparser main.py
```
## Run
When you run script, you can choose 3 options:
- Add new day games list. System will check this date from DB. If not exist, will check this date
in Excel. If exist - process and add it to DB and generate report. If not exist in Game excel
code will skip this step and generate report for with last DB data of games.
- Delete day of games. This is need if you make mistake in Game excel (for example name of player or score)
and need to delete this data and import again.
- Exit from script.

## Logic of statistics
In the report you can find two main score:
- Championat ship score - this is counting ONLY by WIN ot Lose. No matter how you win or
how you lose. Win = 1, Lose = 0. Simple logic. Who win more - winner.
- Personal score - here we use Elo logic for count personal score. Here very importance 
who win and how win. If you win pair with avarage rating worse than your, you will get 
low score. If you win pair with higher rating then your - you will get more score.
Balance win/lose or win more than 10 score also will count independent.