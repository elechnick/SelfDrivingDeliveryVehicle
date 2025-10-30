from navigation import BasicNavigation
from obstacle_avoidance import ObstacleAvoidance
import model
import time

def main():
    nav = BasicNavigation()
    obstacle_sensor = ObstacleAvoidance(trigger_pin=13, echo_pin=14)

    try:
        while True:
            obstacle_detected = False
            
            nav.go_straight()
            
            if obstacle_sensor.detect_obstacle == True:
                obstacle_detected = True
                if model.Model_Run.confidence_score >= 80:
                    nav.stop()
                    obstacle_sensor.avoid_obstacle(nav)
                    time.sleep(1)
                    
                obstacle_detected = False
                
    except KeyboardInterrupt:
        nav.stop()
        print("Stopped by user")

if __name__ == "__main__":
    main()
    print('running')
