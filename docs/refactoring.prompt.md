# Refactoring Prompt - ADAS AEB MVP

## Role

Act as a senior Python and ADAS test engineer performing a behavior-preserving
refactoring of the simulated Automatic Emergency Braking (AEB) MVP.

## Objective

Improve the structure, readability, maintainability, and test quality of the
AEB project without changing the externally observable behavior defined by
requirement `ADAS-AEB-001`.

## Source Files

Review these files before making changes:

- `src/aeb.py` - AEB decision logic and `ON/OFF` command adapter
- `tests/test_aeb.py` - automated unit tests
- `data/aeb_scenarios.csv` - repeatable scenario inputs and expected outputs
- `scripts/run_aeb_scenarios.py` - CSV scenario runner and report generation
- `docs/ADAS_AEB_MVP_Testing_Requirement.md` - source requirement
- `docs/swdd.md` - software design description
- `docs/ut-design/unit-test-design.md` - unit-test design

## Required Behavior

The AEB command shall be `ON` only when all conditions are true:

1. Vehicle speed is greater than `0 km/h`.
2. An obstacle is detected.
3. Obstacle distance is available.
4. Obstacle distance is less than or equal to the configured emergency-braking
   threshold.

Otherwise, the command shall be `OFF`.

The default threshold is `10 m`. Negative speed, obstacle distance, or
threshold values shall raise `ValueError`.

## Refactoring Scope

Consider the following improvements where they provide real value:

- Remove duplicated validation or decision logic.
- Make names, types, and constants clearer.
- Improve the separation between decision logic and `ON/OFF` formatting.
- Keep the data-driven test structure readable and easy to extend.
- Improve scenario-runner error handling or report clarity.
- Preserve the existing CSV format unless a change is necessary and documented.
- Update the SWDD or test-design documentation if the design changes.

Do not add production vehicle behavior, sensor fusion, timing logic, actuator
control, or safety certification claims.

## Constraints

- Use Python 3.10+ and the standard library unless a dependency is clearly
  justified.
- Preserve the public functions `should_brake` and `brake_command`, including
  their current parameters and meaning.
- Do not weaken validation or remove acceptance-criteria coverage.
- Do not change the default threshold or the inclusive `<=` boundary behavior.
- Do not introduce global mutable state.
- Keep the change focused; avoid unrelated formatting or redesign.

## Required Test Coverage

Retain or improve coverage for:

| Scenario | Expected result |
|---|---|
| Moving vehicle, no obstacle | `OFF` |
| Moving vehicle, obstacle outside threshold | `OFF` |
| Moving vehicle, obstacle within threshold | `ON` |
| Stationary vehicle with obstacle | `OFF` |
| Obstacle disappears | `OFF` |
| Distance exactly at `10 m` | `ON` |
| Obstacle at `0 m` | `ON` |
| Negative speed, distance, or threshold | `ValueError` |
| Requirement example: 50 km/h, obstacle at 10 m | `ON` |

## Required Workflow

1. Inspect the current implementation and tests.
2. State the refactoring hypothesis and expected benefit.
3. Make the smallest coherent refactoring.
4. Update tests only when needed to verify the refactored behavior; do not
   rewrite tests merely to hide a regression.
5. Update documentation if public behavior or structure changes.
6. Run the validation commands below.
7. Summarize changed files, behavior preservation, and any remaining risks.

## Validation Commands

Run these commands from the repository root:

```text
python -m unittest discover -s tests -v
python -m scripts.run_aeb_scenarios
python -m scripts.run_aeb_scenarios --report reports/aeb-scenario-report.txt
```

The refactoring is complete only when all unit tests pass and all CSV scenarios
report `PASS`.

## Expected Output

Provide:

- A concise summary of the refactoring.
- The files changed and why.
- Confirmation that the public AEB behavior was preserved.
- Test and scenario-runner results.
- Any follow-up risks or improvements that were intentionally left out.
