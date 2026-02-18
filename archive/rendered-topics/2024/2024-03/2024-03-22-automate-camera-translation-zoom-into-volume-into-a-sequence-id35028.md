# Automate camera translation (zoom into volume) into a sequence

**Topic ID**: 35028
**Date**: 2024-03-22
**URL**: https://discourse.slicer.org/t/automate-camera-translation-zoom-into-volume-into-a-sequence/35028

---

## Post #1 by @AndrewWeitz (2024-03-22 19:25 UTC)

<p>Is there a way to vectorize the zoom in/out of the camera. i.e. camera starts at position (1,0,0) and then zooms into position (5,0,0). Looking to create an automated sequence that starts with the volume zoomed out and then zoom in without manually moving the camera using the scroll wheel or up/down arrows.</p>

---

## Post #2 by @mikebind (2024-03-22 22:23 UTC)

<p>You can easily set the position of the camera (as well as other camera parameters) via python code.  You may find this thread informative: <a href="https://discourse.slicer.org/t/how-to-define-camera-perspective-of-3d-view-window/17136" class="inline-onebox">How to define camera perspective of 3D view window</a></p>

---
