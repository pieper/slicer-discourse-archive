---
topic_id: 9702
title: "Inaccurate Volume Measurement"
date: 2020-01-03
url: https://discourse.slicer.org/t/9702
---

# Inaccurate volume measurement

**Topic ID**: 9702
**Date**: 2020-01-03
**URL**: https://discourse.slicer.org/t/inaccurate-volume-measurement/9702

---

## Post #1 by @Hansveerman (2020-01-03 13:11 UTC)

<p>Hi all,</p>
<p>I am new to 3Dslicer.<br>
I loaded prostate MRI images with 3mm slice thickness.<br>
Then i tried to check the accuracy of the volume measurement option before I did any other calculations.<br>
When i create spherical structures (40mm and 10mm) with segment editor --&gt; paint --&gt; sphere brush, the calculated volumes (segment statistics) are 33272.5mm3 and 530.55mm3. Using 4/3<em>pi</em>r^3, the volumes should be 268082mm3 and 4188mm3.<br>
I can live with a small discrepancy, but this is 8 times too small.</p>
<p>What’s the cause of this difference?</p>

---

## Post #2 by @Hansveerman (2020-01-03 13:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f9310606a0057eeeac50652a6a506cea824cc4a.png" data-download-href="/uploads/short-url/2dMfcoVarEZOYJwdfds5OzwsO38.png?dl=1" title="Vraag aan 3dslicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f9310606a0057eeeac50652a6a506cea824cc4a_2_635x500.png" alt="Vraag aan 3dslicer" data-base62-sha1="2dMfcoVarEZOYJwdfds5OzwsO38" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f9310606a0057eeeac50652a6a506cea824cc4a_2_635x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f9310606a0057eeeac50652a6a506cea824cc4a_2_952x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f9310606a0057eeeac50652a6a506cea824cc4a_2_1270x1000.png 2x" data-dominant-color="9A979A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Vraag aan 3dslicer</span><span class="informations">1334×1050 350 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @aiden.zhu (2020-01-03 13:39 UTC)

<p>Check the diameter or the radius? the difference is 2^3 = 8 times</p>

---

## Post #4 by @Hansveerman (2020-01-03 13:54 UTC)

<p>Woops…</p>
<p>2^3 = 8 ran through my head, but I couldn’t figure it out…</p>
<p>Thanks!</p>

---
