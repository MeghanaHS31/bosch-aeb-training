import unittest

from src.aeb import brake_command, should_brake


class TestAebDecision(unittest.TestCase):
    def test_decision_scenarios(self):
        scenarios = [
            ("AC01 moving without obstacle", 50, False, None, False),
            ("AC02 obstacle outside threshold", 50, True, 10.1, False),
            ("AC03 obstacle within threshold", 50, True, 9.9, True),
            ("AC04 stationary vehicle", 0, True, 1, False),
            ("AC05 obstacle disappears", 50, False, None, False),
            ("boundary at threshold", 1, True, 10, True),
            ("obstacle closer than threshold", 50, True, 0, True),
        ]

        for name, speed, detected, distance, expected in scenarios:
            with self.subTest(scenario=name):
                self.assertEqual(
                    should_brake(speed, detected, distance),
                    expected,
                )

    def test_example_returns_on_command(self):
        self.assertEqual(brake_command(50, True, 10), "ON")

    def test_no_braking_returns_off_command(self):
        self.assertEqual(brake_command(50, False, None), "OFF")

    def test_invalid_values_are_rejected(self):
        with self.assertRaises(ValueError):
            should_brake(-1, True, 1)
        with self.assertRaises(ValueError):
            should_brake(50, True, -1)
        with self.assertRaises(ValueError):
            should_brake(50, True, 1, -1)


if __name__ == "__main__":
    unittest.main()