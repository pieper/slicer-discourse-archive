# LOTS of Camera nodes?

**Topic ID**: 12512
**Date**: 2020-07-13
**URL**: https://discourse.slicer.org/t/lots-of-camera-nodes/12512

---

## Post #1 by @hherhold (2020-07-13 19:48 UTC)

<p>My current scene has somewhere around 45 camera nodes, nearly all of them named “Camera”, although I have 10 "Default Scene Camera"s and 4 "Camera_1"s, in addition to a Camera_2, Camera_3, and Camera_4.</p>
<p>Where do these all come from? I’m assuming I can delete them if they’re not linked to a particular view?</p>
<p>(This is in the June 27 nightly, MacOS.)</p>

---

## Post #2 by @pieper (2020-07-13 20:13 UTC)

<p>Yes, you should be able to remove them if they aren’t being used.  I don’t recall the exact details but I recall there was a lot of debugging around <code>vtkCamera</code>s being auto-created sometimes and probably the camera node bookkeeping has some boundary conditions when changing layouts or something.</p>

---

## Post #3 by @hherhold (2020-07-13 20:22 UTC)

<p>Got it - that makes sense, I’ve been messing with layouts a lot.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---
