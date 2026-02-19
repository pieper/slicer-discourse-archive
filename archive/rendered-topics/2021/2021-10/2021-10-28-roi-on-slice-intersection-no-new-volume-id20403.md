---
topic_id: 20403
title: "Roi On Slice Intersection No New Volume"
date: 2021-10-28
url: https://discourse.slicer.org/t/20403
---

# ROI on slice intersection - no new volume

**Topic ID**: 20403
**Date**: 2021-10-28
**URL**: https://discourse.slicer.org/t/roi-on-slice-intersection-no-new-volume/20403

---

## Post #1 by @Thibaut_Faller (2021-10-28 16:18 UTC)

<p>Dear all,</p>
<p>Currently, I am using a ROI to crop the volume rendering in the 3D view : the volume array is not changed, only the rendering.<br>
I would like to have a similar behavior in the 2D views: only see the portion of the image where the ROI is defined without modifying the input volume array (nor creating a new one as it is done in the crop volume widget): something similar to the threshold.</p>
<p>This could be done by adding a step in the pipeline of the ScalarVolumeDisplayNode (/Libs/MRML/Core/vtkMRMLScalarVolumeDisplayNode.cxx), before applying the Threshold (line 97)<br>
<code>this-&gt;AlphaLogic-&gt;SetInputConnection(0, this-&gt;Threshold-&gt;GetOutputPort() );</code></p>
<p>This would require some modification in Slicer code. Do you think this could be an interesting feature to add ? Would it be better to add it to AnnotationROI or to MarkupsROI ? or both ?</p>
<p>Thank you !</p>

---

## Post #2 by @pieper (2021-10-28 17:12 UTC)

<p>I’d be reluctant to make that slice rendering pipeline any more complex than it already is.  Can you explain why having another volume is a problem?  it seems to me that you could have a module that observes the volume and roi nodes and generates a new cropped volume dynamically and then delete it when the operation is over.  Such a module could also recenter the views to track the roi as it’s updated.  Can you elaborate on why you want to actually crop in the slice views even though the roi is already visible?</p>

---

## Post #3 by @lassoan (2021-10-29 03:46 UTC)

<p>We usually use the threshold feature of the slice view pipeline to show only a region of a volume in a slice view:</p>
<ul>
<li>create a mask volume: labelmap volume, the mask volume is non-zero in the region where you want to show the volume</li>
<li>choose the mask volume as background volume</li>
<li>choose the volume that you want to show using foreground volume</li>
<li>set opacity of the foreground volume to 100%</li>
</ul>
<p>You can create the mask volume using VolumeClip extension’s “Volume clip with ROI” module. It is a very quick operation (takes a fraction of a second) and it is a short Python script, so you can easily put it into your own modules, if you prefer not to depend on another extension. The only thing is that it still uses the old AnnotationROI, so you would need to update it to use the current Markups ROI node.</p>

---

## Post #4 by @Thibaut_Faller (2021-11-05 17:13 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>  and <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Thank you very much for your responses !</p>
<p>In fact, having another volume complexifies a bit our pipeline, but we should be able to deal with it. We would like to crop in the slice views so that the user may only concentrate on the relevant information.<br>
At a first look, using the VolumeClip extension should work. So we will update it with the Markups ROI node and see how it works.</p>
<p>Thanks again !</p>

---

## Post #5 by @lassoan (2021-11-05 18:04 UTC)

<p>Instead of VolumeClip extension you can also use the Mask Volume effect in Segment Editor. It can be used in combination with the Surface Cut effect, which generates surface from points the same ways as “Volume clip with model” module.</p>

---

## Post #6 by @Thibaut_Faller (2021-11-09 09:40 UTC)

<p>Thanks a lot for your suggestion <a class="mention" href="/u/lassoan">@lassoan</a> !<br>
Indeed, the Mask Volume effect could be very interesting if we want to use another shape than the standard cubic ROI to mask our volume !</p>

---
