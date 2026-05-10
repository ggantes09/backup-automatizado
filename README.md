# Automated Backup

Python script for automated folder backup, with log generation and old file control.

## What it does

- Compresses the source folder into `.zip` with date and time in the filename
- Saves the backup to the configured destination folder
- Logs each execution in a log file
- Automatically removes old backups based on a defined limit

## How to use

1. Clone the repository
2. Edit `config.py` with your local paths
3. Run the script:
python backup.py

## Automation

To run automatically, configure the Windows Task Scheduler pointing to `backup.py`.

## Technologies

- Python
- shutil
- os
- datetime