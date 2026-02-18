# How to set ROI of volume in python?

**Topic ID**: 13787
**Date**: 2020-10-01
**URL**: https://discourse.slicer.org/t/how-to-set-roi-of-volume-in-python/13787

---

## Post #1 by @Chintha_Siva_Prasad (2020-10-01 07:26 UTC)

<p>How can I set cropping ROi mode for a volume in python script?</p>

---

## Post #2 by @cpinter (2020-10-01 07:33 UTC)

<p>If this is for volume rendering then something like this should work:</p>
<pre><code class="lang-auto">    volRenLogic = slicer.modules.volumerendering.logic()
    displayNode = volRenLogic.GetFirstVolumeRenderingDisplayNode(volumeNode)
    roiNode = displayNode.GetROINode()
    numberOfDisplayNodes = roiNode.GetNumberOfDisplayNodes()
    for i in range(numberOfDisplayNodes):
      roiNode.GetNthDisplayNode(i).SetVisibility(visible)
</code></pre>

---

## Post #3 by @Chintha_Siva_Prasad (2020-10-01 07:55 UTC)

<p>That helped a lot ,thank you. I don’t want to show it in the red slice view.<br>
How can I do that?<br>
And also how can I crop to selected ROI in python script?</p>

---

## Post #4 by @cpinter (2020-10-01 09:04 UTC)

<p>If you have a question that does not fit under the title of the topic then please create a new topic. Thanks</p>

---
