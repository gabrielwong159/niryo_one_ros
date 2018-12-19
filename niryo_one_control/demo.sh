#!/bin/bash
for i in {1..6}
do
    echo $i $1
    rostopic pub -1 /niryo_one/joint${i}_position_controller/command std_msgs/Float64 "data: $1"
done
