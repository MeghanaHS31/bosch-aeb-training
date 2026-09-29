# Unit Test Design – ADAS AEB

## Role

Act as a senior ADAS test engineer.

## Goal

Design unit test cases for the AEB functionality based on the requirement in
`docs/ADAS_AEB_MVP_Testing_Requirement.md`.

## Requirement

The AEB system shall apply braking when:
- The vehicle is moving forward.
- An obstacle is detected.
- The obstacle is within the emergency-braking condition.

If these conditions are not satisfied, automatic braking shall not be activated.

## Test Scope

Design tests for:

1. Vehicle moving with no obstacle.
2. Vehicle moving with an obstacle outside the braking condition.
3. Vehicle moving with an obstacle within the braking condition.
4. Vehicle stationary with an obstacle.
5. Obstacle disappears before the braking condition.
6. Boundary conditions around the braking threshold.
7. Invalid or unexpected input values.

## Test Design Guidelines

For each test case provide:

- Test case ID
- Test objective
- Input values
- Expected result
- Positive/Negative/Boundary classification

Use equivalence partitioning and boundary value analysis where applicable.

## Expected Output

Create a test design table in the following format:

| Test ID | Test Scenario | Speed | Obstacle Detected | Obstacle Distance | Expected AEB | Type |
|---|---|---:|---|---:|---|---|

Do not create automation code yet.
Focus only on test design.