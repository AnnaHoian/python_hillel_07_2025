import logging
from datetime import datetime
import time

class HeartbeatParser:
    """
    Class for analyzing heartbeat messages into a log file.

    Parameters:
        input_file : str
        Path to the input log file.

        output_file : str
        Path to the output log file for recording WARNING/ERROR.

        key : str
        Key for filtering the lines to be analyzed.

    -------

    Methods:

        load_and_filter():
        Loads a file and selects rows with the desired key.

        parser_heartbeat():
        Analyzes the time difference between messages (heartbeat) and writes logs to the output file.
    """

    def __init__(self, input_file, output_file, key):
        self.input_file = input_file
        self.output_file = output_file
        self.key = key
        self.filtered_log = [] # List of filtered lines in the form (line_number, text).

        # log file configurations
        logging.basicConfig(
            filename=self.output_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def load_and_filter(self):
        """
        Loads the log file and selects the lines that contain the given key.
        """

        with open(self.input_file, "r") as f:
            for index, line in enumerate(f, start=1):
                if self.key in line:
                    self.filtered_log.append((index, line.strip()))

    def parse_heartbeat(self):
        """
        Analyzes heartbeat between lines:
        - if difference > 31 sec and < 33 sec → WARNING
        - if difference >= 33 sec → ERROR

        Results are written to self.output_file.
        """

        start_time = time.time()  # to log Execution time info

        # Open the output file for writing (to create it (if doesn't exist))
        with open(self.output_file, "w") as output_log:
            for indexes in range(1, len(self.filtered_log)):
                index_previous, line_previous = self.filtered_log[indexes -1]
                index_current, line_current = self.filtered_log[indexes]

                # Extract time
                time_previous = line_previous[line_previous.find("Timestamp ") + 10
                                                  : line_previous.find("Timestamp ") + 18]
                time_current = line_current[line_current.find("Timestamp ") + 10
                                                  : line_current.find("Timestamp ") + 18]

                # Convert time to datetime
                t_previous = datetime.strptime(time_previous, "%H:%M:%S")
                t_current = datetime.strptime(time_current, "%H:%M:%S")

                # Calculate the difference in seconds
                sec_diff = (t_previous - t_current).total_seconds()

                # If the transition is through the north
                if sec_diff < 0:
                    sec_diff += 24 * 60 * 60

                # Log entry with the type of problem
                if 31 < sec_diff < 33:
                    output_log.write(f"WARNING: heartbeat = {sec_diff:.0f} sec at {time_current} "
                                     f"(line {index_current})\n")
                elif sec_diff >= 33:
                    output_log.write(f"ERROR: heartbeat = {sec_diff:.0f} sec at {time_current} "
                                     f"(line {index_current})\n")

                logging.info(f"Execution time: {time.time() - start_time:.4f} sec")


parser = HeartbeatParser(
    input_file = "hblog.txt",
    output_file = "hb_test.log",
    key = "TSTFEED0300|7E3E|0400"
)

parser.load_and_filter()
parser.parse_heartbeat()





