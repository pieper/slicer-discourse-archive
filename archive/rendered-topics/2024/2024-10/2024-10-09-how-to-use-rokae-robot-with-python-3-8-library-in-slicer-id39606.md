---
topic_id: 39606
title: "How To Use Rokae Robot With Python 3 8 Library In Slicer"
date: 2024-10-09
url: https://discourse.slicer.org/t/39606
---

# How to use ROKAE robot with Python 3.8 library in Slicer?

**Topic ID**: 39606
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/how-to-use-rokae-robot-with-python-3-8-library-in-slicer/39606

---

## Post #1 by @ningw-git (2024-10-09 12:08 UTC)

<p>Hello, does slicer have a version that uses python3.8? I’m using a ROKAE robot recently, and they provided a program and library file based on python3.8 (similar to: robot.cp38-win_amd64.pyd). I want to use this robot in slicer, so please help.</p>

---

## Post #2 by @ningw-git (2024-10-10 01:54 UTC)

<p>Hello, how can I call my own robot in slicer? We have two models of ABB and ROKEA robot arms. Is there any way to connect to these robot arms and display the robot arm models in slicer? Thank you.</p>

---

## Post #3 by @ningw-git (2024-10-10 02:18 UTC)

<p>sorry it is  ROKAE  robot</p>

---

## Post #4 by @lassoan (2024-10-15 23:40 UTC)

<p>You can import the mesh of each rigid component of the robot and put them under a transform tree as shown here:</p>
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

<p>If you have a URDF file for your robot then you can use the importer that I’ve created to automate the process. You can find details here:</p>
<aside class="quote quote-modified" data-post="4" data-topic="36798">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/loading-robot-into-slicer/36798/4">Loading Robot into Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Slicer can do exactly this. The file that you drag-and-drop is a Slicer scene file that contains models, transforms, and OpenIGTLink configuration. 

You can build the transform tree from information in the urdf file. To make this very easy, I’ve implemented an automatic importer script. You can download it from here: 


The script does not support all possible features (e.g., I’ve only added “revolute” joint types), but can be easily extended as needed. 
All you need is to copy-paste the scrip…
  </blockquote>
</aside>


---
