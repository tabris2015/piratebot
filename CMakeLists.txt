cmake_minimum_required(VERSION 2.8.3)
project(piratebot)

add_compile_options(-std=c++11)
find_package(catkin REQUIRED COMPONENTS
  joy
  roscpp
  rospy
  std_msgs
  turtlesim
)

catkin_package(

)

###########
## Build ##
###########

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(joystick_ctl 
              src/joystick_ctl.cpp)

target_link_libraries(joystick_ctl 
              ${catkin_LIBRARIES})

add_dependencies(joystick_ctl piratebot_generate_messages_cpp)
