import unittest

from python_hillel_07_2025.lesson_16.homework_16_1 import TeamLead

class TeamLeadChecker(unittest.TestCase):
    """
    Unittests for function TeamLead:
    - check inheriting attributes from Employee, Manager, Developer:
    - check TeamLead attribute
    - check that another attribute is not exist
    """
    def test_team_lead_data(self):
        # given
        TeamLead1 = TeamLead(
        name = "Mike",
        salary = 3000,
        department = "QA",
        programming_language = "Python",
        team_size = 5
        )

        # when / then

        self.assertEqual(TeamLead1.name, "Mike")
        self.assertEqual(TeamLead1.salary, 3000)
        self.assertEqual(TeamLead1.department, "QA")
        self.assertEqual(TeamLead1.programming_language, "Python")
        self.assertEqual(TeamLead1.team_size, 5)

        self.assertFalse(hasattr(TeamLead1, "random"))

if __name__ == '__main__':
    unittest.main()
