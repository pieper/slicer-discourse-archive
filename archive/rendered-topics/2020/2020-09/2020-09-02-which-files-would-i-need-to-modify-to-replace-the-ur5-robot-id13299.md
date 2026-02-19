---
topic_id: 13299
title: "Which Files Would I Need To Modify To Replace The Ur5 Robot"
date: 2020-09-02
url: https://discourse.slicer.org/t/13299
---

# Which files would I need to modify to replace the UR5 robot with my ABB IRB 120 robot?

**Topic ID**: 13299
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/which-files-would-i-need-to-modify-to-replace-the-ur5-robot-with-my-abb-irb-120-robot/13299

---

## Post #1 by @CHRIS_HUYNH (2020-09-02 14:21 UTC)

<p>Continuing the discussion from <a href="https://discourse.slicer.org/t/is-there-a-way-to-integrate-3d-slicer-and-ros/11266">Is there a way to integrate 3D slicer and ROS?</a>:,</p>
<p>Hi,</p>
<p>I’ve gone through Junichi Tokuda’s tutorial on how to integrate ROS and 3D slicer for planning purposes, but I now want to integrate my own robot model instead of using the model provided in the tutorials. Which ROS files/scripts (or 3D Slicer files/scripts) would I need to modify in order to fully replace the UR5 robot transformations with my own robot transformations? and is there a specific way I have to set up my Linear Transformations for my robot links in 3D slicer in order to get the 3D Slicer and ROS integration fully functional?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2020-09-02 15:18 UTC)

<p>You can download the ABB IRB 120 robot model with all transformations set up in Slicer from the link at the end of this post:</p>
<aside class="quote quote-modified" data-post="3" data-topic="11395">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-do-i-add-robot-arm-stl-into-a-scene/11395/3">How do I add robot arm STL into a scene?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Also make sure the STL uses mm as coordinate system units (or scale it using a transforms module). 
Note that you can also animate the robot (simulate rotation around each joint) if you load each section of the robot as a separate model, with the rotation joint in the origin. You just need to create a hierarchy of transforms in Transforms module and add each model at the appropriate level in the transform tree. 
I’ve uploaded a short video of ABB IRB 120 robot visualization in Slicer: 

  <a href="https://www.youtube.com/watch?v=yS3SKqNztJU" target="_blank" rel="noopener">
    […</a>
  </blockquote>
</aside>

<p>There is nothing specific to Slicer in this. You transform between different joint coordinate systems the same way as you do it for the robot’s path planning.</p>

---

## Post #3 by @CHRIS_HUYNH (2020-09-02 16:08 UTC)

<p>Hi Andras,</p>
<p>Thank you for your response. I’ve downloaded that scene but when I load it up, I dont see the model. I do see the list of imported STL’s in the “model module” however, I just dont see the actual robot in the scene itself.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-09-02 16:18 UTC)

<p>I’ve just checked again and the .mrb file works well. Make sure you use a recent Slicer Preview Release.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd34f1169bac6279d1bf03390ff865bcc3f98fbc.gif" alt="2020-09-02-12-14-56" data-base62-sha1="A7Ye5mIeAqyLapkvLcGSljzkEvG" width="640" height="390"></p>

---

## Post #5 by @lassoan (2024-10-15 23:37 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/how-to-use-rokae-robot-with-python-3-8-library-in-slicer/39606/2">How to use ROKAE robot with Python 3.8 library in Slicer?</a></p>

---
