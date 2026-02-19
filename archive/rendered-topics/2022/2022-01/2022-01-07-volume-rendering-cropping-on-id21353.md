---
topic_id: 21353
title: "Volume Rendering Cropping On"
date: 2022-01-07
url: https://discourse.slicer.org/t/21353
---

# Volume Rendering Cropping "ON"

**Topic ID**: 21353
**Date**: 2022-01-07
**URL**: https://discourse.slicer.org/t/volume-rendering-cropping-on/21353

---

## Post #1 by @Fluvio_Lobo (2022-01-07 14:44 UTC)

<p>I was implementing the volume rendering module using python and I could not get the ROI volume cropping as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#limit-volume-rendering-to-a-specific-region-of-the-volume" rel="noopener nofollow ugc">here</a>;</p>
<pre><code class="lang-auto">displayNode.SetAndObserveROINodeID(roiNode.GetID())
displayNode.CroppingEnabled = True
</code></pre>
<p>But I did get it working using this version of the call;</p>
<pre><code class="lang-auto">roiNode.GetDisplayNode().SetVisibility(True)
displayNode.SetAndObserveROINodeID( roiNode.GetID() )
displayNode.CroppingEnabledOn()
</code></pre>
<p>I also had to set the ROI to visible for these to apply.</p>
<p>Perhaps the script repo. is  outdated?<br>
I saw a few posts on volume rendering but no questions on enabling cropping, so I thought I would share.</p>

---
