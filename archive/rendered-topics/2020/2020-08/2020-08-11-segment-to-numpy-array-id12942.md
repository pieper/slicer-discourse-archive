# segment to numpy array

**Topic ID**: 12942
**Date**: 2020-08-11
**URL**: https://discourse.slicer.org/t/segment-to-numpy-array/12942

---

## Post #1 by @gabrielzhu1977 (2020-08-11 13:39 UTC)

<p>Hello All,</p>
<p>I need to study the density histogram of ROI on CT so I am trying to get a numpy array out of a segment. But when I convert segmentation node to labelmap node and then to numpy array, I only have  binary array(0, or 1). I want a array with exact value of ROI on CT.<br>
Could anyone help me with this?<br>
Thanks for any help and advice.</p>
<p>Gabriel</p>

---

## Post #2 by @lassoan (2020-08-11 16:05 UTC)

<p>You can use the array of 0/1 as a mask in numpy processing operations, or just blank out values in the CT (set to -10000) where the mask is 0.</p>
<p>See this complete example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Mask_volume_using_segmentation">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Mask_volume_using_segmentation</a></p>

---
