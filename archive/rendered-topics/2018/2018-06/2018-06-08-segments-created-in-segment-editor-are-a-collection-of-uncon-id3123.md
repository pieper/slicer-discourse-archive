# Segments created in segment editor are a collection of unconnected stripes

**Topic ID**: 3123
**Date**: 2018-06-08
**URL**: https://discourse.slicer.org/t/segments-created-in-segment-editor-are-a-collection-of-unconnected-stripes/3123

---

## Post #1 by @Bo_Martins (2018-06-08 11:53 UTC)

<p>Hello<br>
I am new to 3Dslicer but I think it is a cool tool that could be useful for segmentation purposes. I hope you can help me.</p>
<p>When creating segments in the segment editor I encounter problems. I am running version 4.8.1 and I have the exact same problems in two different computers one of which is running Ubuntu and the other Windows:</p>
<p>I can draw the outline of the segment and right-click to create a connected segment but doing so most often does not result in the interior being colored but instead that the interior is divided into a pattern of colored and non-colored stripes. In the 3D view, the stripes also occur so it is not just a display problem. It is also not possible to interpolate between slices once this phenomenon occurs. Once the stripey look appears it also blends over to other slices that have not been contoured yet. I have has similar problems with “paint” but it is more repeatable with the “Draw” tool. Yesterday, the segment editor suddenly worked correctly but having restarted 3DSlicer today the problem is there again. Is the problem well known and do you have a work-around.</p>
<p>Thank you,<br>
Bo</p>

---

## Post #2 by @cpinter (2018-06-08 12:46 UTC)

<p>Hi Bo,</p>
<p>Probably your volume is non-axis aligned, and the slice you are drawing on is not one slice in the volume, but more. See discussion <a href="https://discourse.slicer.org/t/display-issue-with-rt-structs-and-mr-volume/546/10">Display issue with RT structs and MR volume</a></p>
<p>Also I’d like to suggest using the nightly Slicer 4.9.0, there have been many fixes and minor improvements since 4.8.1.</p>

---

## Post #3 by @Bo_Martins (2018-06-11 14:55 UTC)

<p>Hi Csaba</p>
<p>Thank you for the response. I did actually also try the nightly build and the behavior was the same. I was using the sample “MR US prostate” data and that data was indeed rotated in the axial view. However after rotating it as you suggest, I cannot contour it. the moment I right-click or type “a” the contour disappears. Is that behavior expected?</p>
<p>Kind regards,<br>
Bo</p>
<p>PS. I would not have bothered you had I only had problem with the ultrasound data.The stripey phenomenon was also a problem with sample data MRHead which should be axis-aligned. But right now this moment contouring works on MRHead, so I am somewhat confused about what caused the problem to go away for that sequence.</p>

---

## Post #4 by @lassoan (2018-06-12 04:59 UTC)

<p>Axis directions of the binary labelmap representation inside a segmentation node is determined from the volume that you <em>first</em> select as master volume. Most likely you have (or segment editor module by default) selected a volume, which defined axis directions. If you later select a different master volume, then origin, spacing, and axis directions of the existing segmentation is not changed.</p>
<p>In the coming weeks, we plan to add setting dialog to the Segment editor that will allow changing axis directions, spacing, origin of the segmentation at any time, which should make things much more clear.</p>
<p>Until then, the easiest workaround is to create a new segmentation, make sure the volume that you select first as master volume is the volume that you’ll have as background volume during segmentation; and align the slice viewers to that volume’s axes.</p>

---

## Post #5 by @Bo_Martins (2018-06-12 06:25 UTC)

<p>Okay thank you, Andras.</p>

---

## Post #6 by @cpinter (2018-06-12 13:52 UTC)

<p>Yes, the “feature” that Andras mentioned is not self-explanatory and is a serious factor for confusions in Segment Editor. I’m working on a solution right now, stay tuned!</p>

---
