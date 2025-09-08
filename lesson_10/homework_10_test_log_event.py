import unittest

from homework_10_task import log_event

class TestLogEvent(unittest.TestCase):
    """
    class TestLogEvent contains unittests for log_event function:
    - correct logging level (info, warning, error) for each status;
    - correct message format;
    - log file contains logs records.
    """

    def test_log_event_success(self):
        """
        function test_log_event_success checks the "success" status
        username: "user1",
        status: "success",
        expected: output contains correct info message.
        """

        # given:
        name = "user1"
        state = "success"

        # when / then
        with self.assertLogs("log_event", level="INFO") as lg:
            log_event(name, state)
        self.assertEqual(
            "INFO:log_event:Login event - Username: user1, Status: success", lg.output[0])

    def test_log_event_expired(self):
        """
        function test_log_event_expired checks the "expired" status
        username: "user2",
        status: "expired",
        expected: output contains correct warning message
        """

        # given
        name = "user2"
        state = "expired"

        # when / then
        with self.assertLogs("log_event", level="WARNING") as lg:
            log_event(name, state)
        self.assertEqual(
            "WARNING:log_event:Login event - Username: user2, Status: expired", lg.output[0])

    def test_log_event_expected_error(self):
        """
        function test_log_event_expected_error checks the "error" status
        username: "user3",
        status: "error",
        expected: output contains the error message
        """

        # given
        name = "user3"
        state = "error"

        # when / then
        with self.assertLogs("log_event", level="ERROR") as lg:
            log_event(name, state)
        self.assertEqual("ERROR:log_event:Login event - Username: user3, Status: error", lg.output[0])

    def test_log_event_unexpected_error(self):
        """
        function unexpected_error checks the "error" status with unexpected error
        username: "user3"
        status: "test",
        expected: output contains the error message
        """

        # given
        name = "user4"
        state = "test"

        # when / then
        with self.assertLogs("log_event", level="ERROR") as lg:
            log_event(name, state)
        self.assertEqual("ERROR:log_event:Login event - Username: user4, Status: test", lg.output[0])

    def test_log_event_login_system_content(self):
        """
        function test_log_event_login_system_content checks the content availability
        expected: file contains any records
        """
        # given: executed tests messages

        # when / then
        with open("login_system.log") as file:
            logs = file.read()
            self.assertTrue(len(logs) > 0)
            self.assertIn("Status", logs)

if __name__ == '__main__':
    unittest.main()

