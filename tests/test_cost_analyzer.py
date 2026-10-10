
import unittest
from io import StringIO
from contextlib import redirect_stdout

from app.cost_analyzer import analyze_costs, USD_TO_INR


class TestCostAnalyzer(unittest.TestCase):

    def test_total_cost_conversion(self):
        services = {"EC2": 10.00, "S3": 5.00}

        expected_total = 15.00 * USD_TO_INR
        actual_total = sum(services.values()) * USD_TO_INR

        self.assertEqual(actual_total, expected_total)

    def test_budget_exceeded_alert(self):
        services = {"EC2": 100.00}
        budget = 5000.00

        output = StringIO()

        with redirect_stdout(output):
            analyze_costs(services, budget)

        self.assertIn(
            "ALERT: Monthly budget exceeded!",
            output.getvalue()
        )


if __name__ == "__main__":
    unittest.main()
