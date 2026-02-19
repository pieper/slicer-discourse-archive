---
topic_id: 6794
title: "Enable Leap Motion And 3D Slicer To Work Together"
date: 2019-05-15
url: https://discourse.slicer.org/t/6794
---

# Enable Leap motion and 3D slicer to work together

**Topic ID**: 6794
**Date**: 2019-05-15
**URL**: https://discourse.slicer.org/t/enable-leap-motion-and-3d-slicer-to-work-together/6794

---

## Post #1 by @mikecsu (2019-05-15 03:05 UTC)

<p>Operating system:win10<br>
Slicer version:4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,everyone.  These days i am trying to get leap motion to work with Slicer, and i attended to add an old module python code to 3D slicer, then i have this problem -----ImportError: No module named ‘LeapPython’ , so i search for solution on Internet. It turns out that i need older python version(i.e 3.3.0),therefore i would like to ask “is there a way to change the python version (now is Python 3.6.7)  on slicer 4.11.0 to old python version?”   .Any help would be appreciated .</p>

---

## Post #2 by @jcfr (2019-05-15 03:21 UTC)

<p>We recently discussed what is missing to add support for Leap motion. In a nutshell, the bindings available with the v3.2 of Leap motion SDK would need to be re-generated and compiled for python 3.</p>
<p>This is discussed at length in this post: <a href="https://discourse.slicer.org/t/slicerleapmotioncontrol-in-slicer-4-11-0/6770/10" class="inline-onebox">SlicerLeapMotionControl in Slicer 4.11.0</a></p>
<p>We welcome contributions and if you would like to help out, we are happy to provide guidance. To move forward, consider adding comments and questions in the post referenced above.</p>

---
