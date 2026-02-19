---
topic_id: 2508
title: "How To Get Brain Mask From Mr Images Using Skull Stripping"
date: 2018-04-03
url: https://discourse.slicer.org/t/2508
---

# How to get brain mask from MR images using skull stripping?

**Topic ID**: 2508
**Date**: 2018-04-03
**URL**: https://discourse.slicer.org/t/how-to-get-brain-mask-from-mr-images-using-skull-stripping/2508

---

## Post #1 by @Yingli_Lu (2018-04-03 20:43 UTC)

<p>Hi,<br>
OS: Windows 10<br>
slicer: 4.8.1</p>
<pre><code> I have a MR volume:

   dimensions: 120x256x256
   spacing: 1mm x 1mm x 1mm
   origin: 0mm 0mm 0mm
   IJK to RAS direction matrix: 
     0 0 1
     0 1 0
     1 0 0 
</code></pre>
<p>after apply skullStripper:</p>
<pre><code> got a brain mask(LabelMapVolumeNode):
    dimensions: 256x256x80
    spacing: 1mm x 1mm x 1.5mm
    origin: 256mm 256mm 0mm
    IJK to RAS direction matrix: 
            -1 0 0
            0 -1 0
            0 0 -1 
</code></pre>
<p><em>Confusion</em>:  Why the brain mask’s image properties are different with the original MR image?<br>
<em>Question</em>:  Is there a quick/easy way to apply the brain mask on the original MR image in python script(mask out the MR image background)?</p>
<p>Any suggestions are greatly appreciated!</p>
<p>Thanks!</p>
<p>YingLi</p>

---

## Post #2 by @lassoan (2018-04-03 22:07 UTC)

<p>Have you tried the SwissSkullStripper extension? That may give you the mask as you expect, with the warping transform already applied. If not, then use an image resample module to apply the computed transform to the skull mask.</p>

---

## Post #3 by @Yingli_Lu (2018-04-10 13:23 UTC)

<p>SwissSkullStripper gave the mask needed.</p>
<p>Thanks Andras!</p>

---

## Post #4 by @ezproxy (2018-08-12 18:25 UTC)

<p>Thank you, u are so  kind for us.</p>

---
