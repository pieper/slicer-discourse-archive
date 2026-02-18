# How would I go about modifying the ROSMED tutorial robot with my own robot?

**Topic ID**: 13379
**Date**: 2020-09-07
**URL**: https://discourse.slicer.org/t/how-would-i-go-about-modifying-the-rosmed-tutorial-robot-with-my-own-robot/13379

---

## Post #1 by @CHRIS_HUYNH (2020-09-07 18:48 UTC)

<p>I’ve gone through the ROSMED tutorials and it’s very similar to what I’m trying to achieve with my project. My goal is to recreate the tutorials using my own robot and from the tutorial, I can see that I’d have to set up my robot in 3D slicer and apply linear transformations to each link, in which I have done.</p>
<p>I’ve set it up so that each OpenIGTLink linear transform contains the absolute position+orientation of each part of the robot arm (no transform hierarchy). Is there anything else I need to do to on the 3D slicer side of the project?</p>
<p>Also, what files would I need to modify on the ROS side of the project? I know the ros_igtl_bridge package runs the bridge between 3D slicer and ROS, and I’m aware of the igtl_exporter.py script that exports the transforms. Which of these files would I have to modify to replace the UR5 robot with my own robot on ROS?</p>

---
