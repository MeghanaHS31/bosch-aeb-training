"""Execute CSV-backed AEB scenarios and optionally write a text report."""

import argparse
import csv
from pathlib import Path

from src.aeb import brake_command


def run_scenarios(input_path: Path) -> tuple[list[str], int]:
    results = []
    passed = 0

    with input_path.open(newline="", encoding="utf-8") as scenario_file:
        for row in csv.DictReader(scenario_file):
            distance = (
                float(row["obstacle_distance_m"])
                if row["obstacle_distance_m"]
                else None
            )
            actual = brake_command(
                float(row["vehicle_speed_kmh"]),
                row["obstacle_detected"].lower() == "true",
                distance,
            )
            expected = row["expected_command"]
            status = "PASS" if actual == expected else "FAIL"
            passed += status == "PASS"
            results.append(
                f"{row['id']} | {status} | expected={expected} | actual={actual}"
            )

    results.append(f"Summary | {passed}/{len(results)} scenarios passed")
    return results, 0 if passed == len(results) - 1 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/aeb_scenarios.csv"),
        help="CSV file containing AEB scenarios",
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Optional path for a plain-text execution report",
    )
    args = parser.parse_args()

    results, exit_code = run_scenarios(args.input)
    report = "\n".join(results) + "\n"
    print(report, end="")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())