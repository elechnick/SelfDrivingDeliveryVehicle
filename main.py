from navigation import BasicNavigation
from obstacle_avoidance import ObstacleAvoidance
import time

def main():
    nav = BasicNavigation()
    obstacle_sensor = ObstacleAvoidance(trigger_pin=13, echo_pin=14)

    print("🟢  System ready. Press Ctrl+C to stop.")
    time.sleep(1)

    invalid_count = 0  # how many invalid readings in a row
    INVALID_LIMIT = 20  # stop only after 20 consecutive invalid readings (~4 s)

    try:
        while True:
            distance = obstacle_sensor.get_distance()

            # Check if sensor returned something realistic
            if 2 <= distance <= 400:
                invalid_count = 0  # reset counter
                print(f"Measured distance: {distance:.2f} cm")

                if distance < 20:
                    print("🚧  Obstacle detected! Avoiding...")
                    obstacle_sensor.avoid_obstacle(nav)
                else:
                    nav.go_straight()
            else:
                invalid_count += 1
                print("⚠️  Invalid sensor reading (possibly car off)")
                nav.stop()

                # Only exit if the sensor stays invalid for several seconds
                if invalid_count >= INVALID_LIMIT:
                    print("🛑  No valid sensor input for several seconds. Stopping program.")
                    break

            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        nav.stop()
        print("Vehicle stopped safely.")

if __name__ == "__main__":
    main()
