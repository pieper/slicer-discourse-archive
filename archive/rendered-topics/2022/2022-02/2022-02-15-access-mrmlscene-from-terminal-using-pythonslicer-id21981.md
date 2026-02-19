---
topic_id: 21981
title: "Access Mrmlscene From Terminal Using Pythonslicer"
date: 2022-02-15
url: https://discourse.slicer.org/t/21981
---

# Access mrmlScene from terminal using PythonSlicer

**Topic ID**: 21981
**Date**: 2022-02-15
**URL**: https://discourse.slicer.org/t/access-mrmlscene-from-terminal-using-pythonslicer/21981

---

## Post #1 by @Karthik (2022-02-15 15:06 UTC)

<p>Hi everybody.<br>
I have used PythonSlicer from terminal before. I’ve used it to run scripts using the environment and dependencies that come with slicer. Ex: ./PythonSlicer ~/test.py</p>
<p>Now I want to run a python script using PythonSlicer, but I want to be able to use mrmlScene from within the script. I do not need to access any buttons, sliderwidgets, etc. Those values can be hardcoded. For example, I want to be able to run the following<br>
<code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")</code></p>
<p>Basically, I want to test python scripts in Slicer without having to launch the application so that the tests can run in a docker image.<br>
Please suggest ways to make this happen.</p>
<p>Also, I have observed in various modules such as <strong>Vascular Modeling Toolkit</strong> that there is usually a <strong>Reload and Test</strong> button and its code in written in a test class within the module.py<br>
Is there any way to run this test without launching the slicer application?</p>

---

## Post #2 by @lorinbaum (2023-11-30 12:52 UTC)

<p>Hello,</p>
<p>having the same problem, have any solution to this been found? The reason I care about PythonSlicer.exe is that it provides live feedback unlike runnings scripts in Slicer.exe. Any way to get the same functionality as in Slicer.exe?</p>

---

## Post #3 by @cpinter (2023-11-30 12:56 UTC)

<p>As far as I know you will need to launch the Slicer application one way or another, and not just the Python environment. Something like this could work:</p>
<p><code>[path/]Slicer.exe --no-main-window --python-script [path/]YourScript.py</code></p>
<p>But let’s wait for people who are more expert on Slicer’s Python environment than I…</p>

---

## Post #4 by @pieper (2023-11-30 22:37 UTC)

<p>Yes, if you need the functionality of slicer then you need to use the full application as your python environment.</p>

---

## Post #5 by @lorinbaum (2023-12-01 11:23 UTC)

<p>In the bigger picture, I was trying to use PythonSlicer as a “weak link” between Slicers capabilities and, in this case, a Unity application. I would send code, it would send feedback and store results in a designated folder, where I would pick them up. The lack of feedback from Slicer.exe is unfortunate imo.<br>
I expected a “strong link” to be much more labor intensive, that is sharing a direct data stream, storing data only in memory and perhaps sharing a process that can be seen and manipulated from both the Slicer GUI und the Unity App.<br>
Your reponses have redirected me towards that approach, which I still need to research. Thanks.</p>

---

## Post #6 by @pieper (2023-12-01 20:31 UTC)

<p>Why not use the Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html">WebServer</a> module for this link?  Or maybe <a href="http://openigtlink.org/">OpenIGTLink</a>?</p>

---

## Post #7 by @lorinbaum (2023-12-06 05:37 UTC)

<p>Because I, correctly, assumed they would be a mountain of work for me. With this post, I aim to check my approach to avoid needlessly committing to the mountain. This need comes from my inability to find easily understood existing discussion/documentation in this area so I expect it to be useful for others as well.</p>
<p>Generally, I was hoping to cheaply test a way to build an AR/VR viewer/simulator for volumes/segmentations in Unity. Unity and not SlicerVR because I see easier future expansion by using its physics engine and performance efficient realism or making the app standalone for narrower applications. I am also guided by a vision of using the 3D Slicer Desktop UI (keyboard + mouse) while viewing models in VR similar to what the combo <a href="https://www.youtube.com/watch?v=nh_vSi0tzg0" rel="noopener nofollow ugc">Desktop+ and BlenderVR</a> can do.</p>
<p>Trying to link the applications, I went for OpenIGTLink, as suggested, because its protocol (by my understanding) is more suitable (than WebServers HTTP) for exchanging live feeds of eg transformations or from multiple users in one session.<br>
The currently targeted process looks like this:</p>
<ol>
<li>Launch AR/VR app</li>
<li>To connect to Slicer, find the .exe - currently by manual path entering</li>
<li>Launch Slicer.exe with python script that launches OpenIGTLink Server (alternatively enter Server details in Unity app interface)</li>
<li>Launch any python script from the AR/VR interface to be executed in Slicer</li>
<li>Get an AR/VR view of any mesh that is in the 3D View in Slicer, later maybe other node types</li>
<li>Interact by transforming, slicing, measuring the model in AR/VR while any changes are synchronized with 3D Slicer which displays their equivalent (if available) in the 3D view.</li>
</ol>
<p>Critique of the above approach is welcome.</p>
<p>Finally, I am faced with a steep learning curve that comes from trying to use OpenIGTLink to receive+execute scripts and later send polydata and me being a network noob and C++ illiterate. I am trying to learn by reading through the <a href="https://github.com/BSEL-UC3M/HoloLens2and3DSlicer-PedicleScrewPlacementPlanning/tree/b08e8e872be1ef9e1e8cd4d30706741a3cde3766" rel="noopener nofollow ugc">AR Planner</a> code, but would welcome any beginner friendly ressources on this topic.</p>

---
