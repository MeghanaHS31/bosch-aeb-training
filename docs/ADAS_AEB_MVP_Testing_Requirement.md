# ADAS AEB – MVP Testing Requirement

**Requirement ID:** ADAS-AEB-001  
**Feature:** Automatic Emergency Braking (AEB)

## 1. Requirement

When the vehicle is moving forward and an obstacle is detected in the vehicle's path, the AEB system shall apply braking when the vehicle reaches the defined emergency-braking condition.

If no obstacle is detected, the system shall not apply automatic emergency braking.

## 2. Acceptance Criteria

| ID | Condition | Expected Result |
|---|---|---|
| AC01 | Vehicle moving, no obstacle | No automatic braking |
| AC02 | Vehicle moving, obstacle detected outside braking condition | No automatic braking |
| AC03 | Vehicle moving, obstacle detected within emergency-braking condition | Automatic braking is activated |
| AC04 | Vehicle stationary | No automatic braking |
| AC05 | Obstacle disappears before braking condition | Automatic braking is not activated |

## 3. MVP Scope

The MVP shall use a simulated test environment. No real vehicle or physical hardware is required.

### Inputs

- Vehicle speed
- Obstacle detected: Yes/No
- Obstacle distance

### Output

- AEB braking command: ON/OFF

## 4. Example

```text
Vehicle Speed = 50 km/h
Obstacle Detected = YES
Obstacle Distance = 10 m

Expected Result:
AEB Brake Command = ON
```

## 5. Training Scope – 16 Hours

| Stage | Activity |
|---|---|
| Requirement Analysis | Analyze AEB requirement and identify testable conditions |
| Test Design | Create scenarios, test cases and boundary conditions |
| Automation/Development | Develop automated tests using GitHub Copilot |
| Test Execution | Execute tests and analyze failures |
| Refactoring | Improve test code/framework using Copilot |
| CI/CD | Create GitHub Actions pipeline and execute tests |
| AWS Deployment | Deploy test application/report to AWS |

## 6. Recommended Training Flow

**Requirement → Test Design → Automation → Test Execution → Failure Analysis → Refactoring → GitHub Actions CI/CD → AWS**

## 7. Out of Scope

- Real vehicle integration
- Physical sensors or ECU hardware
- Complex vehicle dynamics
- Production AEB algorithms
- ADAS safety certification
