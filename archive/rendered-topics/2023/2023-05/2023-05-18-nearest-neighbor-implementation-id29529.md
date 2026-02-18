# Nearest Neighbor implementation

**Topic ID**: 29529
**Date**: 2023-05-18
**URL**: https://discourse.slicer.org/t/nearest-neighbor-implementation/29529

---

## Post #1 by @osmandogan (2023-05-18 14:15 UTC)

<p>Hello. I am doing a volume crop operation in a study I have been working on. And I want to use the “Nearest Neighborn” feature from the interpolator features in the “Volume Crop” module. How can I add the “Nearest Neighborn” attribute to my code?</p>

---

## Post #2 by @lassoan (2023-05-18 19:01 UTC)

<p>You can change the interpolation mode programmatically by modifying properties of the crop volume parameter node:</p>
<pre><code class="lang-python">parameterNode = getNode('CropVolumeParameters')
mode = slicer.vtkMRMLCropVolumeParametersNode.InterpolationNearestNeighbor
parameterNode.SetInterpolationMode(mode)
</code></pre>

---

## Post #3 by @osmandogan (2023-05-18 22:23 UTC)

<p>Thank you very much, that’s exactly what I was looking for <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---
