# Unit Test Design - ADAS AEB

**Requirement:** ADAS-AEB-001  
**Default emergency-braking threshold:** 10 m

## Test Strategy

The decision scenarios use equivalence partitioning and boundary value
analysis. A data-driven test executes the normal and boundary cases from one
table. Invalid input and output-format behavior remain separate tests because
they verify different interfaces.

## Decision Scenarios

| Test ID | Test Scenario | Speed (km/h) | Obstacle Detected | Obstacle Distance (m) | Expected AEB | Type |
|---|---|---:|---|---:|---|---|
| AC01 | Vehicle moving, no obstacle | 50 | No | N/A | OFF | Negative |
| AC02 | Obstacle outside braking condition | 50 | Yes | 10.1 | OFF | Negative |
| AC03 | Obstacle within braking condition | 50 | Yes | 9.9 | ON | Positive |
| AC04 | Vehicle stationary with obstacle | 0 | Yes | 1 | OFF | Negative |
| AC05 | Obstacle disappears before braking | 50 | No | N/A | OFF | Negative |
| B01 | Distance exactly at threshold | 1 | Yes | 10.0 | ON | Boundary |
| B02 | Obstacle immediately in front | 50 | Yes | 0 | ON | Boundary |

## Validation Scenarios

| Test ID | Input | Expected Result | Type |
|---|---|---|---|
| V01 | Vehicle speed = -1 km/h | `ValueError` | Invalid |
| V02 | Obstacle distance = -1 m | `ValueError` | Invalid |
| V03 | Threshold = -1 m | `ValueError` | Invalid |
| V04 | No obstacle distance (`None`) | `OFF` when no obstacle is detected | Equivalence |

## Automation Mapping

The decision scenarios are implemented with `unittest.subTest` in
`tests/test_aeb.py`. Repeatable simulation inputs are stored in
`data/aeb_scenarios.csv` and executed by:

```text
python -m scripts.run_aeb_scenarios
```