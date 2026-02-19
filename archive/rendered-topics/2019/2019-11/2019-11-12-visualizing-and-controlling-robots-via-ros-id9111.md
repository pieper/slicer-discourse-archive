---
topic_id: 9111
title: "Visualizing And Controlling Robots Via Ros"
date: 2019-11-12
url: https://discourse.slicer.org/t/9111
---

# Visualizing and controlling robots via ROS

**Topic ID**: 9111
**Date**: 2019-11-12
**URL**: https://discourse.slicer.org/t/visualizing-and-controlling-robots-via-ros/9111

---

## Post #1 by @Zhao_Su (2019-11-12 07:37 UTC)

<p>Last month I asked about how to set up robot arm in Slicer on the Slicer discourse. Thanks for Ungi’s reply. Now I just finish the slides on <a href="http://rosmed.github.io/" rel="noopener nofollow ugc">rosmed.github.io</a> with the REAL UR5 robot. It is an amazing project. There are some question I wanna to ask about the project:</p>
<p>1, I want to use my own tool(needle), I dont know how to compute the needletip’s transform in slicer. I appreciate that if you tell me.  So I can click “place from” , the markup will appear at my tool’s tip.</p>
<p>2, When I send the Target and Entry Markups to the ROS, the robot execute it directly. Could I achieve that like I send the points , then I see the path in the Rviz, the program ask me “Would you execute it?”, I set Y, the robot will move. If that could happen, which program should I modify?</p>
<p>3, Mostly the path from the motion planning is not really good , even a lot of times the robot won’t be there(the Target and Entry). I know it is about Moveit. Is this normal? And could you give me some advice?</p>
<p>4, When I get the PlanReference(the Plan Markups harden transform from RasToReference), is this Markups in the Robot coordinate?  If I compute the (x, y , z, rx, ry, rz) from the PlanReference Markups, and directly send it to robot(not via ROS), Will the robot be in the position I want?</p>
<p>Thank you very much for your patience in answering my questions every time. I really appreciate about that.</p>

---

## Post #2 by @CHRIS_HUYNH (2020-09-07 14:52 UTC)

<p>Hi,</p>
<p>This isn’t an answer to your question, but have you managed to replace the UR5 robot thats in the tutorial with a robot of your own? (having it plan in moveit! and see the planning in both moveit and 3d Slicer)</p>
<p>I’ve also gone through the tutorial and I’m now having trouble trying to replace the UR5 robot with my own, but am having trouble exporting my robot’s link transformations via igtl_exporter to 3D slicer.</p>

---

## Post #3 by @Jet_Geng (2021-12-02 12:14 UTC)

<p>hi <a class="mention" href="/u/zhao_su">@Zhao_Su</a> <a class="mention" href="/u/chris_huynh">@CHRIS_HUYNH</a><br>
i also interested in this project，where can find more information about project <a href="http://rosmed.github.io" rel="noopener nofollow ugc">rosmed.github.io</a>。<br>
thanks in advance!</p>

---

## Post #4 by @lassoan (2021-12-02 18:46 UTC)

<p><a class="mention" href="/u/ungi">@ungi</a> and <a class="mention" href="/u/tokjun">@tokjun</a> have updated the <a href="https://github.com/rosmed/rosmed.github.io">tutorial</a> a few weeks ago for latest version of Slicer and ROS. If you have any specific questions then you can ask them here.</p>

---

## Post #5 by @tokjun (2021-12-02 21:34 UTC)

<p><a class="mention" href="/u/jet_geng">@Jet_Geng</a> I’m happy to take any questions. Thanks for your interest in the project!</p>

---

## Post #6 by @Jet_Geng (2021-12-03 01:47 UTC)

<p>thank you very much！ it’s really helpful！</p>

---

## Post #7 by @Jet_Geng (2021-12-03 01:50 UTC)

<p>thank you very much！I will trouble you if i have any question。 <img src="https://emoji.discourse-cdn.com/twitter/handshake.png?v=10" title=":handshake:" class="emoji" alt=":handshake:"></p>

---

## Post #8 by @Jet_Geng (2021-12-06 07:04 UTC)

<p>hi, <a class="mention" href="/u/tokjun">@tokjun</a> i found a ppt file named “Building Software Systems for Image-Guided Robot-Assisted Interventions”, but it’s for SSMR/ISMR 19 workshop。 There are many things are changed. ex:  In the section which called “Setting up a universal robot arm on ROS”,  the cli command for launch movit has changed, and i have no idea about how to fix it. so Is there a new version ppt about ISMR2021.<br>
Thx in advance, looking forward to your response.</p>

---
