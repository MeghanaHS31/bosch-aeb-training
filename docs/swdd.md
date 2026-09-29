# Software Design Description

## 1. Document Information

| Item | Value |
|---|---|
| Feature | Automatic Emergency Braking (AEB) |
| Requirement | ADAS-AEB-001 |
| Scope | MVP simulated test environment |
| Status | Initial implementation design |
| Source requirement | [ADAS AEB MVP Testing Requirement](ADAS_AEB_MVP_Testing_Requirement.md) |

## 2. Purpose

This document describes the software design for the simulated AEB decision
logic. The software evaluates vehicle speed, obstacle presence, and obstacle
distance and produces an automatic braking command.

The design is intentionally limited to the MVP. It does not model real
vehicle dynamics, sensor hardware, braking actuators, or a production safety
algorithm.

## 3. System Context

The AEB software is a synchronous, deterministic decision component. A test
or simulation supplies one set of input values for each evaluation. The
component returns a braking decision without maintaining state between
evaluations.

```text
+----------------------+       +----------------------+       +----------------+
| Simulated test input | ----> | AEB decision logic   | ----> | Brake command  |
| speed, detection,    |       | should_brake()       |       | ON or OFF      |
| distance             |       |                      |       |                |
+----------------------+       +----------------------+       +----------------+
				      |
				      v
			      Configured threshold
			      default: 10 m
```

## 4. Design Decisions

### 4.1 Decision rule

Automatic braking is activated only when all of the following conditions are
true:

1. Vehicle speed is greater than `0 km/h`.
2. An obstacle is detected.
3. An obstacle distance is available.
4. Obstacle distance is less than or equal to the emergency-braking distance.

The MVP default emergency-braking distance is `10 m`, based on the example in
the source requirement. The threshold is configurable so that boundary and
scenario tests can use other values without changing the decision logic.

The equivalent decision rule is:

```text
brake = (speed > 0)
	AND obstacle_detected
	AND (distance is available)
	AND (distance <= emergency_braking_distance)
```

### 4.2 No state retention

Each call is evaluated independently. If an obstacle disappears, the next
call receives `obstacle_detected = False` and returns `OFF`; no previous
obstacle detection is retained.

### 4.3 Invalid input handling

The component rejects negative values with `ValueError`:

- Negative vehicle speed
- Negative obstacle distance
- Negative emergency-braking threshold

An unavailable obstacle distance is represented by `None`. This is valid when
no usable obstacle distance exists, but it cannot result in braking.

## 5. Software Components

### 5.1 `should_brake`

**Location:** `src/aeb.py`

| Item | Description |
|---|---|
| Responsibility | Evaluate the AEB decision conditions |
| Inputs | `vehicle_speed_kmh: float`, `obstacle_detected: bool`, `obstacle_distance_m: float \| None`, `emergency_braking_distance_m: float` |
| Default threshold | `10.0 m` |
| Output | `True` when braking is required; otherwise `False` |
| Errors | Raises `ValueError` for negative numeric inputs |

This function contains the decision rule and is suitable for direct unit
testing.

### 5.2 `brake_command`

**Location:** `src/aeb.py`

| Item | Description |
|---|---|
| Responsibility | Convert the boolean decision to the requirement's output format |
| Inputs | Same inputs as `should_brake` |
| Output | `"ON"` or `"OFF"` |
| Errors | Propagates input validation errors from `should_brake` |

This function is the output adapter for simulated test consumers that require
the specified `ON/OFF` command.

## 6. Interface Definition

### Input interface

| Name | Type | Unit / Values | Required |
|---|---|---|---|
| `vehicle_speed_kmh` | `float` | km/h, `>= 0` | Yes |
| `obstacle_detected` | `bool` | `True` or `False` | Yes |
| `obstacle_distance_m` | `float \| None` | metres, `>= 0`, or unavailable | Yes |
| `emergency_braking_distance_m` | `float` | metres, `>= 0`; default `10.0` | No |

### Output interface

| Output | Meaning |
|---|---|
| `ON` | Automatic braking is activated |
| `OFF` | Automatic braking is not activated |

## 7. Processing Behavior

The processing sequence is:

1. Validate that numeric inputs are not negative.
2. Check that the vehicle is moving.
3. Check that an obstacle is detected.
4. Check that obstacle distance is available.
5. Compare obstacle distance with the configured threshold.
6. Return the boolean decision or map it to `ON/OFF`.

The function does not perform unit conversion, filtering, timing, sensor
fusion, braking-force calculation, or actuator control.

## 8. Requirements Traceability

| Requirement / Acceptance Criterion | Design implementation | Verification |
|---|---|---|
| ADAS-AEB-001 | `should_brake` activates only for a moving vehicle with a detected obstacle within the threshold | Unit tests |
| AC01: Moving, no obstacle | `obstacle_detected = False` returns `False` / `OFF` | `test_ac01_moving_without_obstacle_does_not_brake` |
| AC02: Obstacle outside condition | Distance greater than threshold returns `False` / `OFF` | `test_ac02_obstacle_outside_condition_does_not_brake` |
| AC03: Obstacle within condition | Distance at or below threshold returns `True` / `ON` | `test_ac03_obstacle_within_condition_brakes` |
| AC04: Vehicle stationary | Speed equal to zero returns `False` / `OFF` | `test_ac04_stationary_vehicle_does_not_brake` |
| AC05: Obstacle disappears | Missing detection returns `False` / `OFF` | `test_ac05_obstacle_disappears_does_not_brake` |
| Example: 50 km/h, obstacle at 10 m | Default threshold includes the boundary distance | `test_example_returns_on_command` |

## 9. Test Design

Automated tests are located in `tests/test_aeb.py` and use Python's built-in
`unittest` framework.

The test suite covers:

- All five acceptance criteria
- The inclusive threshold boundary at `10 m`
- The example input and required `ON` output
- The `OFF` output for a non-braking scenario
- Rejection of negative speed and distance values
- Rejection of a negative emergency-braking threshold

Run the tests from the repository root with:

```text
python -m unittest discover -s tests -v
```

## 10. Assumptions and Constraints

- Inputs represent one instantaneous simulation sample.
- Forward movement is represented by a speed greater than zero.
- The 10 m threshold is an MVP configuration, not a validated production
  braking threshold.
- No physical vehicle, sensor, ECU, actuator, or real-time scheduler is used.
- Safety certification and production deployment are out of scope.

## 11. Future Extensions

The following may be added in later iterations without changing the core
acceptance criteria:

- Explicit units and range validation for all input fields
- Logging of validation errors
