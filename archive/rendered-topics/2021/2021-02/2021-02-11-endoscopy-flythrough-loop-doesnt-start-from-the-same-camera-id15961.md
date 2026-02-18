# Endoscopy flythrough loop doesn't start from the same camera angle and changes every loop

**Topic ID**: 15961
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/endoscopy-flythrough-loop-doesnt-start-from-the-same-camera-angle-and-changes-every-loop/15961

---

## Post #1 by @akshay_pillai (2021-02-11 22:34 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930<br>
I am using the endoscopy module and in it, the flythrough works fine but once one loop is over the camera angle(or up, down) changes and starts from a different angle. is there any way to fix the camera orientation?<br>
Also, can the camera be set to one view and not rotate every loop.</p>

---

## Post #2 by @lassoan (2021-02-14 06:17 UTC)

<p>There are many methods for moving a camera along a curve. The current method just updates the camera view plane normal and orthogonalizes the axes (<a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L300" class="inline-onebox">Slicer/Endoscopy.py at master · Slicer/Slicer · GitHub</a>).</p>
<p>We compute a transform that keeps one axis of the frame orthogonal to the curve’s plane (<a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L314-L318" class="inline-onebox">Slicer/Endoscopy.py at master · Slicer/Slicer · GitHub</a>). You could change the Endoscopy module (it is just a Python script, you can edit with any text editor then click “Reload”) to use these axes as camera plane normal and view up directions.</p>
<p>Markups curves can provide coordinate frame for each curve point, too<br>
(computed by parallel transport method). You could modify the code to use these axes (returned by<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsCurveNode.html#ab23760b90d69d1b2e8392c75ce0a7123">GetCurvePointToWorldTransformAtPointIndex()</a>).</p>

---

## Post #3 by @akshay_pillai (2021-02-17 21:54 UTC)

<p>Thanks, this pointed me in  the right direction</p>

---

## Post #4 by @lassoan (2021-02-17 23:34 UTC)

<p>If you make any improvements to the camera trajectory creation in Endoscopy module then it would be great if you could contribute it back. It allows other users benefit from your work and you can save time by not having to maintain your own version of the module.</p>

---
