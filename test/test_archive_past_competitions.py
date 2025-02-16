import unittest
import json
import datetime
from server import archive_past_competitions, loadArchivedCompetitions  

class TestArchivePastCompetitions(unittest.TestCase):
    def test_archive_past_competitions(self):
        archive_past_competitions()
        competitions = loadArchivedCompetitions()
        current_time = datetime.datetime.now()
        for competition in competitions:
            self.assertLessEqual(competition['date'], current_time)

if __name__ == '__main__':
    unittest.main()
