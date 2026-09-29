"""Minimal simulated Automatic Emergency Braking decision logic."""


def should_brake(
    vehicle_speed_kmh: float,
    obstacle_detected: bool,
    obstacle_distance_m: float | None,
    emergency_braking_distance_m: float = 10.0,
) -> bool:
    """Return whether the simulated AEB system should activate braking.

    The MVP uses a configured distance threshold. A vehicle must be moving,
    an obstacle must be present, and its distance must be at or below the
    threshold.
    """
    if vehicle_speed_kmh < 0:
        raise ValueError("vehicle speed cannot be negative")
    if emergency_braking_distance_m < 0:
        raise ValueError("emergency braking distance cannot be negative")
    if obstacle_distance_m is not None and obstacle_distance_m < 0:
        raise ValueError("obstacle distance cannot be negative")

    return (
        vehicle_speed_kmh > 0
        and obstacle_detected
        and obstacle_distance_m is not None
        and obstacle_distance_m <= emergency_braking_distance_m
    )


def brake_command(
    vehicle_speed_kmh: float,
    obstacle_detected: bool,
    obstacle_distance_m: float | None,
    emergency_braking_distance_m: float = 10.0,
) -> str:
    """Return the MVP output command as ``ON`` or ``OFF``."""
    return "ON" if should_brake(
        vehicle_speed_kmh,
        obstacle_detected,
        obstacle_distance_m,
        emergency_braking_distance_m,
    ) else "OFF"