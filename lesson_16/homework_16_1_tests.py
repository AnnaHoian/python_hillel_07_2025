import unittest

from python_hillel_07_2025.lesson_16.homework_16_1 import TeamLead

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s',
    handlers = [
        logging.StreamHandler(),
        logging.FileHandler('log.log')
    ])

class TeamLeadChecker(unittest.TestCase):
    """
    Unittests for function TeamLead:
    - check inheriting attributes from Employee, Manager, Developer:
    - check TeamLead attribute
    - check that another attribute is not exist
    """
    def test_team_lead_data(self):
        try:
            # given
            TeamLead1 = TeamLead(
            name = "Mike",
            salary = 3000,
            department = "QA",
            programming_language = "Python",
            team_size = 5)
            logger.info(f"Team Lead data are successfully inherited")
        except TypeError as e:
            logger.debug(f"TypeError by creating TeamLead {e}")
            self.fail(f"Creating TypeError raises {e}")

        # when / then
        else:
            self.assertEqual(TeamLead1.name, "Mike")
            self.assertEqual(TeamLead1.salary, 3000)
            self.assertEqual(TeamLead1.department, "QA")
            self.assertEqual(TeamLead1.programming_language, "Python")
            self.assertEqual(TeamLead1.team_size, 5)

            self.assertFalse(hasattr(TeamLead1, "random"))

if __name__ == '__main__':
    unittest.main()
