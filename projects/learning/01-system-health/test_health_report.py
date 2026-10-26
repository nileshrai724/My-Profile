import unittest

from health_report import build_report


class HealthReportTests(unittest.TestCase):
    def test_report_has_expected_fields_and_valid_disk_percent(self):
        report = build_report(".")

        self.assertTrue(report["hostname"])
        self.assertGreater(report["disk_total_bytes"], 0)
        self.assertGreaterEqual(report["disk_free_bytes"], 0)
        self.assertGreaterEqual(report["disk_used_percent"], 0)
        self.assertLessEqual(report["disk_used_percent"], 100)


if __name__ == "__main__":
    unittest.main()
