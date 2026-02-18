# Seeking guidance on visualizing MyBuddy 280 robot in 3D Slicer with WLAN connection

**Topic ID**: 45789
**Date**: 2026-01-15
**URL**: https://discourse.slicer.org/t/seeking-guidance-on-visualizing-mybuddy-280-robot-in-3d-slicer-with-wlan-connection/45789

---

## Post #1 by @Dristi_R (2026-01-15 20:46 UTC)

<p>Hello everyone,</p>
<p>I am currently working on integrating the <strong>MyBuddy 280 robotic arm</strong> by Elephant Robotics with <strong>3D Slicer</strong> using the <strong>SlicerROS2 module</strong>. My goal is to visualize the robot in Slicer while simultaneously controlling it via <strong>WLAN sockets</strong>.</p>
<p>So far, I have been able to:</p>
<ul>
<li>
<p>Connect the robot via WLAN and send/receive joint states.</p>
</li>
<li>
<p>Visualize the robot in <strong>RViz</strong> using ROS2, with movements of the physical robot accurately reflected in real time.</p>
</li>
<li>
<p>Prepare the URDF and DAE files for the robot model.</p>
</li>
</ul>
<p>However, I am encountering difficulties when trying to visualize MyBuddy directly in Slicer. I would like to know if anyone here has successfully visualized <strong>MyBuddy 280</strong> (or a similar myCobot robot) in <strong>3D Slicer</strong>.</p>
<p>Any guidance, tips, or example configurations for connecting a ROS2-controlled MyBuddy robot to Slicer would be greatly appreciated.</p>

---

## Post #2 by @Laura_Connolly (2026-01-17 17:41 UTC)

<p>Hi there! SlicerROS2 currently doesn’t support DAE files so you will need to convert the cobot links to STL (an online converter should work fine for this). You can verify your other setup steps by reviewing this web page from project week: <a href="https://projectweek.na-mic.org/PW39_2023_Montreal/Projects/Slicerros2/" class="inline-onebox" rel="noopener nofollow ugc">Project Description | NA-MIC Project Weeks</a></p>

---
