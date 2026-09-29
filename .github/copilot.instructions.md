# This project is a ADAS (Advanced Driver Assistance System) simulation focusing on Automatic Emergency Braking (AEB) logic.

The AEB system is designed to automatically apply the brakes when an obstacle is detected within a critical distance while the vehicle is in motion. The simulation includes decision logic to determine when braking should occur and provides corresponding brake commands.

The project includes unit tests to verify the correctness of the AEB decision logic and brake command outputs under various scenarios, including normal operation, boundary conditions, and invalid input handling. These tests help ensure the reliability and safety of the simulated AEB system.   

## tech stack

- Python 3.10+
- unittest for testing
- Type hints for function signatures
- Markdown for documentation    

## Design Pattern

The project follows a modular design pattern, separating the AEB decision logic from the brake command generation. This separation allows for easier testing, maintenance, and potential future enhancements. The decision logic is encapsulated in functions that can be independently tested, ensuring that the core functionality is reliable before integrating it with other components.

## File Structure

- `src/aeb.py`: Contains the AEB decision logic and brake command functions.
- `tests/test_aeb.py`: Contains unit tests for the AEB system.
- `.github/copilot.instructions.md`: Provides project instructions and documentation. 

## Folder Structure

- `src/`: Contains the source code for the AEB simulation.
- `tests/`: Contains unit tests for the AEB system.
- `.github/`: Contains GitHub-specific files, including the Copilot instructions.     

## Safety Considerations

The AEB system simulation prioritizes safety by ensuring that braking decisions are made based on accurate obstacle detection and distance measurements. The system includes checks for invalid input values, such as negative speeds or distances, to prevent unrealistic or unsafe behavior. Unit tests further validate the system's reliability under various scenarios, contributing to the overall safety of the simulated AEB system.      

## Usage Instructions

To use the AEB simulation, import the `should_brake` and `brake_command` functions from `src/aeb.py` and call them with the appropriate parameters. The `should_brake` function returns a boolean indicating whether braking should occur, while the `brake_command` function returns a string command ("ON" or "OFF") based on the braking decision. 

Example usage:
```python
from src.aeb import should_brake, brake_command

speed = 50
obstacle_detected = True
distance_to_obstacle = 10

if should_brake(speed, obstacle_detected, distance_to_obstacle):
    command = brake_command(speed, obstacle_detected, distance_to_obstacle)
    print(command)  # Output: "ON"
else:
    command = brake_command(speed, obstacle_detected, distance_to_obstacle)
    print(command)  # Output: "OFF"
```   