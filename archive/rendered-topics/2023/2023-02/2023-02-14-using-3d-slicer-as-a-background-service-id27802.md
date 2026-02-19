---
topic_id: 27802
title: "Using 3D Slicer As A Background Service"
date: 2023-02-14
url: https://discourse.slicer.org/t/27802
---

# Using 3D Slicer as a background service

**Topic ID**: 27802
**Date**: 2023-02-14
**URL**: https://discourse.slicer.org/t/using-3d-slicer-as-a-background-service/27802

---

## Post #1 by @GradyC (2023-02-14 02:15 UTC)

<p>Hello, I am currently developing a project where I think 3D Slicer’s rasterization would come in handy. To keep things simple I am developing a 3D printer where we must convert an .STL file to a .TIFF stack. There is plenty of documentation on that process so that is not my concern.</p>
<p>What I aim to do is create my own front end allowing the user to input parameters for the rasterization process (DPI, input/output directories, slice height, bit-depth etc.), and modify the python script to rasterize based on user input. My main question is how can I start 3D Slicer as a service in the background so I can run the Python script to rasterize my .STL file?</p>
<p>I apologize if this is a stupid question, but essentially I want the 3D Slicer to be “invisible” (i.e. a background service I call) and have the front end GUI that I have created be the only user facing item. I look forward to any responses!</p>

---

## Post #2 by @ebrahim (2023-02-14 02:20 UTC)

<p>It sounds like you would be interested in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/webserver.html" rel="noopener nofollow ugc">the WebServer module</a>!</p>

---

## Post #3 by @GradyC (2023-02-14 02:27 UTC)

<p>Thank you for the response. I actually found this module earlier and it seemed like it fit my needs perfectly. I ran the start server command and 3D Slicer started to open on my local machine as well (I am assuming because I had to input the Slicer’s exec file as a parameter). I am going to look into ways to start Slicer silently in the background. Thanks again!</p>

---

## Post #4 by @ebrahim (2023-02-14 02:57 UTC)

<p>I didn’t try this before but if you can run WebServer module functionality via python script then maybe you can get what you want <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/gui.html#run-python-commands-in-the-slicer-environment" rel="noopener nofollow ugc">by using using --no-main-window and --no-splash</a></p>

---

## Post #5 by @GradyC (2023-02-15 16:51 UTC)

<p>Actually this seems perfect for the intentions I need it. I can get my program to run this command in the background so the user doesn’t have to interface with 3D Slicer. Thank you!</p>

---
