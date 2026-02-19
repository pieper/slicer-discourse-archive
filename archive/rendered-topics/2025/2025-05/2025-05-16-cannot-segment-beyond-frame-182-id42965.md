---
topic_id: 42965
title: "Cannot Segment Beyond Frame 182"
date: 2025-05-16
url: https://discourse.slicer.org/t/42965
---

# Cannot segment beyond frame 182

**Topic ID**: 42965
**Date**: 2025-05-16
**URL**: https://discourse.slicer.org/t/cannot-segment-beyond-frame-182/42965

---

## Post #1 by @mbol (2025-05-16 12:50 UTC)

<p>Hello,</p>
<p>My apologies if this was brought up earlier but I could not find smothing similar in the question bank. I have started using the latest version of 3D slicer 5.8.1 and I noticed that I can only annotate up to frame 182, after that there is no choice to do anything with the dcom file and the frames after that. I have tried everything. used different dcom files, tried to do some digging into with settings . no luck. chat GTP was advising some changes within the</p>
<p>“Export/Import models and labelmaps”**, find the <strong>“Specify geometry”</strong>.</p>
<p>However I cannot find this option under export/import and labelmaps. I do not even know if this would resolve the problem.</p>
<p>I am in an urgent situation to fix this as it is messing around the annoatation stage of my project and half of the video have not been annotated.. <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=14" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>Any help would be so appreciated.</p>
<p>Kind Regards</p>

---

## Post #2 by @lassoan (2025-05-16 12:51 UTC)

<p>See detailed instructions for this in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">Segment Editor documentation</a>.</p>

---

## Post #3 by @muratmaga (2025-05-16 15:57 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> a different version of this comes up often in our short courses. For better or worse, there is a tendency amongst biologist to crop the image frame extremely tight during the import process (mostly to minimize memory footprint of the volume, since they tend to work with big volumes).</p>
<p>When we run margin or smoothing (for example to fill holes through dilation/erosion) on such image, these operations do not work effectively, since it comes to the edge of the frame. They simply become flat lines. There is also no error/warning (which makes sense because there is actually no error, just a unexpected consequence).</p>
<p>Documentation does not cover anything about how to pad the segmentation geometry, but specifically  how to increase/decrease the spacing. The real solution of course is to pad the source volume prior to segmentation via crop volume, but that’s too involved once you are in the thick of the segmentation.</p>
<p>Would it be possible to implement a feature that will notify the user (and if possible automatically pad the segmentation geometry) if it detects the resultant labelmap of the operation will not fit the current segment geometry?</p>

---
