# Threshold changes when we change contrast value

**Topic ID**: 6621
**Date**: 2019-04-26
**URL**: https://discourse.slicer.org/t/threshold-changes-when-we-change-contrast-value/6621

---

## Post #1 by @prorai (2019-04-26 11:45 UTC)

<p>i’m using contrast change in python code,</p>
<p>i.e.</p>
<pre><code>a = slicer.util.arrayFromVolume(self.importedVolume)
self.contrastScale = 2.0
a[:] = a * self.contrastScale
</code></pre>
<p>i notice that it changes the threshold value impact on volume in segmentation, how can we relate it with original threshold value input for segmentation.</p>

---

## Post #2 by @lassoan (2019-04-26 12:27 UTC)

<p>Do <em>not</em> change the voxel values of your volume if you just want to change its display brightness/contrast! Adjust window/level values in the volume’s display node instead.</p>
<p>For example, increase contrast by halving the display window width:</p>
<pre><code>displayNode = self.importedVolume.GetDisplayNode()
displayNode.SetAutoWindowLevelOff()
displayNode.SetWindow(displayNode.GetWindow()/2.0)</code></pre>

---

## Post #3 by @prorai (2019-04-26 12:37 UTC)

<p>i’m not using it only to change display brightness , i’m using it cause it helps in body part segmentation.<br>
like it helps to get thin layer of skin etc.</p>

---

## Post #4 by @lassoan (2019-04-26 12:41 UTC)

<p>You cannot help segmentation by applying linear offset/scaling to voxels. In general, you must not modify the original image.</p>
<p>Complete all <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation" rel="nofollow noopener">segmentation tutorials</a> to learn more about segmentation.</p>

---
