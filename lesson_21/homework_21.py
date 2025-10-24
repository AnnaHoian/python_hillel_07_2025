import logging
from datetime import datetime

class HeartbeatParser:
    """
    Class for analyzing heartbeat messages into a log file.

    Parameters:
        input_file : str
        Path to the input log file.

        key : str
        Key for filtering the lines to be analyzed.

    -------

    Methods:

        load_and_filter():
        Loads a file and selects rows with the desired key.

        parser_heartbeat():
        Analyzes heartbeat differences between log lines.

        write_results():
        Writes results to a log file.
    """

    def __init__(self, input_file, key):
        self.input_file = input_file
        self.key = key
        self.filtered_log = [] # List of filtered lines in the form (line_number, text).

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
       Analyzes heartbeat differences between log lines.

        Returns:
            list of dicts with fields:
                - level: "WARNING" or "ERROR"
                - diff: time difference in seconds
                - time: timestamp of current line
                - line: full log line
        """
        results = []
        for i in range(1, len(self.filtered_log)):
            index_previous, line_previous = self.filtered_log[i - 1]
            index_current, line_current = self.filtered_log[i]

            # Extract timestamps
            time_previous = line_previous[line_previous.find("Timestamp ") + 10
                                                      : line_previous.find("Timestamp ") + 18]
            time_current = line_current[line_current.find("Timestamp ") + 10
                                                      : line_current.find("Timestamp ") + 18]

            # Convert time to datetime
            t_previous = datetime.strptime(time_previous, "%H:%M:%S")
            t_current = datetime.strptime(time_current, "%H:%M:%S")

            # Calculate the difference in seconds
            sec_diff = (t_previous - t_current).total_seconds()

            # handle midnight crossing
            if sec_diff < 0:
                sec_diff += 24 * 60 * 60

            # Log entry with the type of problem
            if 31 < sec_diff < 33:
                results.append({"level": "WARNING", "diff": sec_diff, "time": time_current, "line": line_current})
            elif sec_diff >= 33:
                results.append({"level": "ERROR", "diff": sec_diff, "time": time_current, "line": line_current})

        return results

    def write_results(self, results):
        """Writes results to the log file"""
        for entry in results:
            if entry["level"] == "WARNING":
                logging.warning(f"Heartbeat = {entry['diff']:0f} sec and {entry['time']} | {entry['line']}")
            elif entry["level"] == "ERROR":
                logging.error(f"Heartbeat = {entry['diff']:0f} sec and {entry['time']} | {entry['line']}")

if __name__ == '__main__':

    # log file configurations
    logging.basicConfig(
        filename="hb_test.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    parser = HeartbeatParser(
        input_file = "hblog.txt",
        key = "TSTFEED0300|7E3E|0400"
    )

    parser.load_and_filter()
    heartbeat_results = parser.parse_heartbeat()
    parser.write_results(heartbeat_results)

    logging.info(f"Heartbeat analysis complete. Total alerts: {len(heartbeat_results)}")



