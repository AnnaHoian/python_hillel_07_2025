"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

import json
import logging

class JsonReading:
    """
    class JsonReading to read JSON files and logging errors

    Attributes:
    json_files - json files to read
    log_file - new file with logs

    Methods:
    LogConfig() - set log configuration
    FileReading() - reading json files with catching and logging errors
    """

    def __init__(self, json_files, log_file):
        self.json_files = json_files
        self.log_file = log_file
        self.LogConfig()

    def LogConfig(self):
        logging.basicConfig(
            filename= self.log_file,
            level= logging.ERROR,
            format= '%(asctime)s - %(levelname)s - %(message)s',
            filemode = 'w'
        )

    def FileReading(self):
        for filename in self.json_files:
            try:
                with open(filename, newline='', encoding='utf-8') as jsonfile:
                    data = json.load(jsonfile)
            except json.JSONDecodeError as e:
                logging.error(f"Error decoding JSON in file {filename}: {e}")
            except UnicodeError as e:
                logging.error(f"Encoding error in file{filename}: {e}")


jsonfiles = 'localizations_en.json', 'localizations_ru.json', 'login.json', 'login.json'
file_with_logs = 'json_logs.log'

JsonRead = JsonReading(jsonfiles, file_with_logs)

JsonRead.FileReading()