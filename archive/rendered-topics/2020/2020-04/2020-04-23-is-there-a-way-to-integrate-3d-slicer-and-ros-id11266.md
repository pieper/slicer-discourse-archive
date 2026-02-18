# Is there a way to integrate 3D slicer and ROS?

**Topic ID**: 11266
**Date**: 2020-04-23
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-integrate-3d-slicer-and-ros/11266

---

## Post #1 by @CHRIS_HUYNH (2020-04-23 10:25 UTC)

<p>Hi,</p>
<p>I’m using the pedicle screw simulator to plan pedicle screw trajectories and I was wondering if i was able to use these planned trajectories in 3D Slicer to position an ABB 120 robot to align with these trajectories using ROS and a navigation camera.</p>
<p>I’ve got a phantom spine that I’m currently working with and I was going to use the PedicleScrewSimulator to plan pedicle screw trajectories into this phantom spine. Then I was hoping to use this planning to execute a planning path for a robot, using ROS, to position itself over the spine in these planned trajectories. I’d need to get the positioning of the real-world spine phantom to align with that on the simulator in order to do this, but is there a possibility of this being doable?</p>

---

## Post #2 by @tokjun (2020-04-23 13:22 UTC)

<p>Hi,</p>
<p>That is doable. We developed ROS-IGTL-Bridge ( <a href="https://github.com/openigtlink/ROS-IGTL-Bridge" rel="nofollow noopener">https://github.com/openigtlink/ROS-IGTL-Bridge</a> ), which works as a ROS node to exchange transforms, images, and models with 3D Slicer using OpenIGTLink. We also made a tutorial on image-guided robot-assisted needle placement using ROS-IGTL-Bridge and presented at the ISMR conference last year. You can still download the slides and materials at: <a href="https://rosmed.github.io/" rel="nofollow noopener">https://rosmed.github.io/</a></p>
<p>Thanks!</p>
<p>Junichi</p>

---
