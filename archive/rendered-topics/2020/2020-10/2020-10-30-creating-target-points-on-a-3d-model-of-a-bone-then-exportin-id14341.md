# Creating target points on a 3D model of a bone then exporting these out as a python script?

**Topic ID**: 14341
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/creating-target-points-on-a-3d-model-of-a-bone-then-exporting-these-out-as-a-python-script/14341

---

## Post #1 by @tharisata_c (2020-10-30 23:07 UTC)

<p>HI,</p>
<p>I’m very new to Slicer 3D but I’m planning to use it for a surgical robot.</p>
<p>Ideally, I want to be able to visualize a bone at position referenced to a frame (which I define). Then, I want to create target points on that bone manually (if this is possible, I’m still not sure).</p>
<p>Finally, I’d like to export these target points in a Python-readable format so I can import it to a different software (RoboDK).</p>
<p>Any advice on any of these points would be greatly appreciated! Thank you in advance.</p>

---

## Post #2 by @lassoan (2020-10-31 04:25 UTC)

<p>Most Slicer-based surgical robotics projects uses OpenIGTLink protocol (via SlicerOpenIGTLink extension) to communicate with devices, such as position trackers, cameras, ultrasound imaging systems, surface scanners, and robots. Tool calibrations and patient registrations are performed using <a href="http://www.slicerigt.org/wp/">SlicerIGT extension</a> and <a href="http://www.plustoolkit.org/">Plus toolkit</a>.</p>
<p>Robots are usually controlled by ROS and commands and positions are transferred via <a href="https://github.com/openigtlink/ROS-IGTL-Bridge">ROS/OpenIGTLink bridge</a>. You can have a look at this <a href="https://rosmed.github.io/">step-by-step tutorial</a> for an example of how to set up a medical robotics guidance system using Slicer.</p>
<p>I’m sure you can set up something with RoboDK, too, but it is a closed, proprietary software, which seems quite limited compared to what you can do with ROS. If you still choose to try RoboDK (you don’t need real-time guidance and visualization) then then you can save all target point coordinates that you placed on the bone surface in Slicer as a json file using File / Save date. You can read this json file into Python using a single command.</p>

---

## Post #3 by @tharisata_c (2020-10-31 18:07 UTC)

<p>Hi, Thank you for your quick and detailed response, it’s going to help me a lot!</p>
<p>I have no experience with ROS but after some research, I found that it’s still only in the development stage with regards to KUKA Robots. Do you know if it’s still worth using then?</p>
<p>Thank you!</p>

---

## Post #4 by @lassoan (2020-11-01 20:15 UTC)

<p>Which Kuka LBR (lightweight)? As far as I know, most research groups use this robot using ROS.</p>

---

## Post #6 by @tharisata_c (2020-11-01 21:33 UTC)

<p>My apologies, I forgot to mention!</p>
<p>The robot that we have is a Kuka KR 60-3 with a KRC4 Controller. It’s quite a large 6-axis robot and is definitely not light weight.<br>
<strong>Would it still be possible to use with ROS?</strong></p>
<p>I hope this won’t affect the way we use Slicer, especially if it’s just taking points on the 3D space.</p>
<p>Thank you again, Andras!</p>

---

## Post #7 by @lassoan (2020-11-02 20:31 UTC)

<p>I haven’t seen this robot model used by any medical research groups (Kuka lightweight robots are safer around people, smaller, less expensive), but Kuka robots are very popular in general, so I assume that yo can find readily usable ROS node to control it. This may be a good starting point: <a href="http://wiki.ros.org/kuka">http://wiki.ros.org/kuka</a></p>

---
