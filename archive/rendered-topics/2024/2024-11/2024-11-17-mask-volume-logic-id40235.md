---
topic_id: 40235
title: "Mask Volume Logic"
date: 2024-11-17
url: https://discourse.slicer.org/t/40235
---

# Mask Volume Logic

**Topic ID**: 40235
**Date**: 2024-11-17
**URL**: https://discourse.slicer.org/t/mask-volume-logic/40235

---

## Post #1 by @Filippo_Parronchi (2024-11-17 21:39 UTC)

<p>Hi everyone,<br>
I’m using a 3D Slicer instance without GUI (headless representation)  on my Apache2 server.<br>
In my Python script, I can’t use the widget representation, so I need to directly call the logic functions of the modules I’m using.</p>
<p>I need to create an independent volume for my “liver” segment obtained after segmentation with TotalSegmentator.<br>
I use the “Mask Volume” effect of the Segment Editor module. Is it possible to know which logic functions (not widget) should be called from Python to execute it and obtain my ScalarVolumeNode “liver Masked”?</p>
<p>I thought this was the correct code:</p>
<pre><code class="lang-auto">fillValue = 0
SegmentEditorEffects.SegmentEditorMaskVolumeEffect.maskVolumeWithSegment(
    segmentationNode, segmentID, "FILL_OUTSIDE", [fillValue], inputVolume, outputVolume
)
</code></pre>
<p>But when I call it, I get a LabelMapVolumeNode, which is different from what happens when I execute the command from the GUI, where I correctly get a new ScalarvolumeNode.<br>
I want to retain the original pixel values of my “liver,” not the binary mask.</p>
<p>If</p>
<p>Any help is appreciated.</p>

---

## Post #2 by @lassoan (2024-11-18 21:31 UTC)

<p>You provide the node for <code>outputVolume</code>. The <code>maskVolumeWithSegment</code> function cannot change the type of this object, it will remain the type that you chose when you created that node.</p>

---
