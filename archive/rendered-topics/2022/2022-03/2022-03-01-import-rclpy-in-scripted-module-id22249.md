---
topic_id: 22249
title: "Import Rclpy In Scripted Module"
date: 2022-03-01
url: https://discourse.slicer.org/t/22249
---

# Import rclpy in scripted module

**Topic ID**: 22249
**Date**: 2022-03-01
**URL**: https://discourse.slicer.org/t/import-rclpy-in-scripted-module/22249

---

## Post #1 by @LauraConnolly (2022-03-01 20:10 UTC)

<p>Hi there! I’m trying to import a python library called rclpy into a scripted module, the import is working in a regular python file (outside of Slicer) on Linux but I don’t think it’s supported by pip - I followed these build instructions: <a href="https://github.com/ros2/rclpy" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ros2/rclpy: rclpy (ROS Client Library for Python)</a></p>
<p>I know this trick for importing python packages:<br>
try:<br>
import rclpy<br>
except:<br>
slicer.util.pip_install(‘rclpy’)<br>
import rclpy</p>
<p>but is there a solution that doesn’t rely on pip?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @LauraConnolly (2022-03-03 13:46 UTC)

<p>I ended up solving this by changed the PYTHON_ENV variable to my ROS2 python path!</p>

---

## Post #3 by @LauraConnolly (2022-03-03 18:09 UTC)

<p>Changing the PYTHON_ENV seemed to solve some issues but now I’m having an incompatibility problem between Python 3.8 in the rclpy and Python 3.9 in latest nightly Slicer - is there a way to change the python version if I build Slicer from source?</p>

---

## Post #4 by @jamesobutler (2022-03-03 18:43 UTC)

<p>Changing python version is not something supported currently in Slicer. Things are tested and set up for Python 3.9. There would be a bit of work to get all the correct hashes for the whl files (matching Python 3.8) of all the c extension python packages included in Slicer core.</p>
<p>In terms of effort spent, you are probably better off setting your external environment to be Python 3.9 with rclpy to match what Slicer uses.</p>

---
