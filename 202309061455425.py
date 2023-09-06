from geometry_msgs.msg import PoseStamped
import signal
import rclpy
import time
from nav2_msgs.action import NavigateToPose
import rclpy.action
from movearm import GrpcClient

import time
from copy import deepcopy
 
from geometry_msgs.msg import PoseStamped,Pose
from rclpy.duration import Duration
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult

# resume pony ai

# youjiantaoci 

# ites


# 设置导航目标点的位姿
# chngdian
nav_goal1 =Pose()
# nav_goal1.position.x = -0.16064334
# nav_goal1.position.y = 0.058278
# nav_goal1.position.z = 0.0
# nav_goal1.orientation.x = 0.0
# nav_goal1.orientation.y = 0.0
# nav_goal1.orientation.z = -0.6174548
# nav_goal1.orientation.w = 0.7866063048

nav_goal1.position.x = 0.33964937925338745
nav_goal1.position.y = 1.439727544784546
nav_goal1.position.z = 0.0
nav_goal1.orientation.x = 0.0
nav_goal1.orientation.y = 0.0
nav_goal1.orientation.z = 0.0
nav_goal1.orientation.w = 1.0



# 设置导航目标点的位姿
nav_goal2 = Pose()
# nav_goal2.position.x = -1.928211
# nav_goal2.position.y = -0.743806
# nav_goal2.position.z = 0.0
# nav_goal2.orientation.x = 0.0
# nav_goal2.orientation.y = 0.0
# nav_goal2.orientation.z = -0.7052
# nav_goal2.orientation.w = 0.7090
nav_goal2.position.x = 1.3578894138336182
nav_goal2.position.y = -1.2570228576660156

nav_goal2.position.z = 0.0
nav_goal2.orientation.x = 0.0
nav_goal2.orientation.y = 0.0
nav_goal2.orientation.z = 0.7232984884120085
nav_goal2.orientation.w = 0.6905355144095803



def main():

    # 设置时间间隔
    sleep_time = 1.0
    counter = 0

    rclpy.init()
    navigator = BasicNavigator()

    point_list = [nav_goal1, nav_goal2]
    # point_list = [nav_goal1, nav_goal2, nav_goal3]
    
    while(True):
        cur_pose = point_list.pop(0)
        # if counter ==0 :
        #     pass
        # else:
        point_list.append(cur_pose)
        # 发送导航目标点
        cur_goal = PoseStamped()
        cur_goal.header.frame_id = 'map'
        cur_goal.pose=cur_pose
        navigator.goToPose(cur_goal)
        # Do something during your route
        # (e.x. queue up future tasks or detect person for fine-tuned positioning)
        # Print information for workers on the robot's ETA for the demonstration
        i = 0
        while not navigator.isTaskComplete():
            i = i + 1
            feedback = navigator.getFeedback()
            if feedback and i % 20 == 0:
                print('Distance Reamin %f' % feedback.distance_remaining)
    
        result = navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print('REACH POINT at %d', counter)
    
        elif result == TaskResult.CANCELED:
            print('Task at ' + 
                ' was canceled. Returning to staging point...')
    
        elif result == TaskResult.FAILED:
            print('Task at ' + ' failed!')
            exit(-1)
    
        while not navigator.isTaskComplete():
            pass


        # 等待导航完成
        # time.sleep(sleep_time)


        # 
        time.sleep(2)

        counter+=1
        # if counter > 4:
        #     break

if __name__ == '__main__':
    main()
