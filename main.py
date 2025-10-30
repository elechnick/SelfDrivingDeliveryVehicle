from navigation import BasicNavigation
from obstacle_avoidance import ObstacleAvoidance
import time

def main():
    nav = BasicNavigation()
    obstacle_sensor = ObstacleAvoidance(trigger_pin=13, echo_pin=14)

    try:
        while True:
            obstactle_detected = False
            if (obstacle_sensor.detect_obstacle == True):
                obstacle_sensor.avoid_obstacle(nav)
                obstactle_detected == False
            else:
                nav.go_straight()
            time.sleep(0.1)
    except KeyboardInterrupt:
        nav.stop()
        print("Stopped by user")

if __name__ == "__main__":
    main()
