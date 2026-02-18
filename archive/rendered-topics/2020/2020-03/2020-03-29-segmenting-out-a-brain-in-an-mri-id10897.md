# Segmenting out a brain in an MRI

**Topic ID**: 10897
**Date**: 2020-03-29
**URL**: https://discourse.slicer.org/t/segmenting-out-a-brain-in-an-mri/10897

---

## Post #1 by @BGreen (2020-03-29 17:59 UTC)

<p>Hello all,</p>
<p>I’d like to segment out my brain from an MRI and 3D print it. I had been trying to segment it following <a href="https://discourse.slicer.org/t/new-video-tutorial-for-segment-editor-lumbar-spine-segmentation-for-3d-printing/700">this tutorial</a> but have not been able to isolate my brain - it makes contact with my skull so I haven’t been able to use the island tool, and their signals are close enough that I can’t isolate it with a threshold either. Does anyone have suggestions on how to do this?</p>
<p>This is my first time using 3D Slicer and it’s an amazing tool to have. Thank you to everyone who has made this software available!</p>

---

## Post #2 by @lassoan (2020-03-30 04:52 UTC)

<p>If you are only interested in the brain (not in the skull or skin surface) then remove the skull using one of the automatic skull stripping modules. I would recommend to use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper">SwissSkullStripper extension</a>.</p>

---

## Post #3 by @BGreen (2020-03-30 19:36 UTC)

<p>Thank you very much for your help! This is exactly the sort of thing I was looking for and it worked very well.</p>
<p>I was able to use the output image to a segment and then export that to an STL file following <a href="https://www.youtube.com/watch?v=WfuYPVYA5cA" rel="nofollow noopener">these instructions</a>, but the STL file is empty or at least invisible when I try to view it in either FreeCAD or Microsoft’s Print 3D. Unless I think of an alternative way to export it, I will post a new question about this later.</p>

---

## Post #4 by @lassoan (2020-03-30 19:55 UTC)

<p>After you stripped the skull, you still need to segment the volume. Segmentation of brain surface should be possible using thresholding (optionally followed by smoothing).</p>

---

## Post #5 by @BGreen (2020-03-30 20:37 UTC)

<p>Thank you again!</p>
<p>That’s exactly the tool I used - the threshold, that is. I was able to construct a segment by using a threshold that encompassed my entire brain, and then export that as an STL.</p>
<p>I tried again, and apparently I had not clicked “apply” or something, so that the thresholding was not actually applied to and I was exporting an empty file. I now have a successful export.</p>
<p>Oddly enough, it seems to have been smoothed automatically.</p>

---

## Post #6 by @dangerweenie (2024-05-16 18:01 UTC)

<p>have you tried meshmixer? it’s free and great for this!</p>

---

## Post #7 by @dangerweenie (2024-05-16 20:43 UTC)

<p>I’m trying to do the same thing - do you have any advice for segmenting? when I run it automatically, the brain comes out way too small (the mask needs to be grown)</p>

---
