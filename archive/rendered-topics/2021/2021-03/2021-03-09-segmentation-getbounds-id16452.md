---
topic_id: 16452
title: "Segmentation Getbounds"
date: 2021-03-09
url: https://discourse.slicer.org/t/16452
---

# Segmentation getBounds

**Topic ID**: 16452
**Date**: 2021-03-09
**URL**: https://discourse.slicer.org/t/segmentation-getbounds/16452

---

## Post #1 by @Ludovic_Ferrer (2021-03-09 15:25 UTC)

<p>Hi everyone,<br>
I am interested in cropping images around each segmentation I have at hand. Naively, I though that the method GetBounds would provide me a bounding box around each segmentation. Here is the snippet I used to get the information.</p>
<blockquote>
<p>def getbounds_segmentations(node_string=‘<em>RTSTRUCT</em>’):<br>
segmentationNode = slicer.util.getNode(node_string)<br>
segmentation = segmentationNode.GetSegmentation()<br>
dico_seg = {}<br>
for i in range(segmentation.GetNumberOfSegments()):<br>
bounds = [0]*6<br>
seg_name = segmentation.GetNthSegment(i).GetName()<br>
current_seg = segmentation.GetNthSegment(i)<br>
current_seg.GetBounds(bounds)<br>
dico_seg[seg_name] = bounds<br>
return dico_seg</p>
</blockquote>
<p>here is the output dictionnary:</p>
<blockquote>
<p>{‘FOIE (% Max=40) - R’: [-178.71093750000003, 88.8671875, 141.59375, 193.3515625, -677.5, -355.5], ‘FOIE (Adaptatif) - R’: [-178.71093750000003, 83.3479995727539, 142.82000732421875, 189.4453125, -675.5, -355.5], ‘FOIE (Black) - R’: [-178.71093750000003, 88.23500061035156, 142.5703125, 192.50799560546875, -675.5, -353.5], ‘FOIE (Fitting) - R’: [-178.71093750000003, 78.45999908447266, 146.4765625, 187.62100219726562, -673.5, -357.5], ‘FOIE (Nestle) - R’: [-178.71093750000003, 82.53299713134766, 145.4669952392578, 188.46875, -675.5, -355.5], ‘Structure 001-os (% Max=40) - R’: [-178.9429931640625, 88.8671875, 141.59375, 193.3515625, -677.5, -355.5], ‘Structure 001-os (Adaptatif) - R’: [-178.73899841308594, 82.03125, 143.546875, 189.4453125, -675.5, -355.5], ‘Structure 001-os (Black) - R’: [-178.9429931640625, 87.890625, 142.5703125, 192.375, -675.5, -353.5], ‘Structure 001-os (Fitting) - R’: [-178.73899841308594, 77.1484375, 146.4765625, 187.4921875, -673.5, -356.40350341796875], ‘Structure 001-os (Nestle) - R’: [-178.9429931640625, 82.03125, 145.5, 188.46875, -675.5, -355.5]}</p>
</blockquote>
<p>As you can see, despite the fact that the structures are way apart, the bounding box values are quite the same. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71dd52c205bd6b84b56ec81e2a4ab4a21938410e.png" alt="slicer1" data-base62-sha1="gfi8uXvNrRCdcPrPHb9Y5TiCqCy" width="400" height="320"></p>
<p>What am I missing here ?<br>
Best regards<br>
Ludovic</p>

---

## Post #2 by @lassoan (2021-03-09 18:04 UTC)

<p>The feature that you are considering implementing is already available in “Split volume” effect (provided by SegmentEditorExtraEffects extension).</p>
<aside class="quote no-group" data-username="Ludovic_Ferrer" data-post="1" data-topic="16452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ludovic_ferrer/48/5018_2.png" class="avatar"> Ludovic_Ferrer:</div>
<blockquote>
<p>I though that the method GetBounds would provide me a bounding box around each segmentation.</p>
</blockquote>
</aside>
<p>GetBounds provides union of bounds of the all representation of the segment. This is guaranteed to contain the segment but not guaranteed to be minimum size. Computing the minimum size can be an expensive operation that you can perform whenever it is necessary. For example, for binary labelmap representation, you can use vtkSegmentationCore.vtkOrientedImageDataResample.CalculateEffectiveExtent as it is done in Crop volume effect (that Split volume effect uses internally).</p>

---

## Post #3 by @Ludovic_Ferrer (2021-03-10 10:03 UTC)

<p>Thank you Andras.<br>
This is a nice feature. Is it possible to use it by scripting ?<br>
One more thing, my main objective here would be to create a majority voting (or staple) labelmap for each segmentation (I have 5 segmentations for each localisation of interest, eg: 5 for liver, 5 for tumor1, etc …). One way of doing whould be to create one labelmap for each segmentation considering the whole volume (which is not really efficient). And, as the number of segmentation is really large (up to 200), I came to the idea of cropping the volume before the creation of the labelmap. Is it a correct way of handling this ? if yes, what would be the best approach ?<br>
Best regards<br>
Ludovic</p>

---

## Post #4 by @lassoan (2021-03-10 14:25 UTC)

<aside class="quote no-group" data-username="Ludovic_Ferrer" data-post="3" data-topic="16452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ludovic_ferrer/48/5018_2.png" class="avatar"> Ludovic_Ferrer:</div>
<blockquote>
<p>Is it possible to use it by scripting ?</p>
</blockquote>
</aside>
<p>All Slicer features are available using Python scripting. See examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">script repository</a>.</p>
<aside class="quote no-group" data-username="Ludovic_Ferrer" data-post="3" data-topic="16452">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ludovic_ferrer/48/5018_2.png" class="avatar"> Ludovic_Ferrer:</div>
<blockquote>
<p>Is it a correct way of handling this ? if yes, what would be the best approach ?</p>
</blockquote>
</aside>
<p>I’m not sure I understand the question. Please use segment and segmentation terms as defined <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#basic-concepts">here</a> to make things more clear. If possible, also add a few pictures to explain what you would like to do.</p>

---
