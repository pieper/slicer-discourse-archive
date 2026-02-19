---
topic_id: 36116
title: "Calculate Dihedral Angles Using Plug Ins"
date: 2024-05-13
url: https://discourse.slicer.org/t/36116
---

# Calculate dihedral angles using plug-ins

**Topic ID**: 36116
**Date**: 2024-05-13
**URL**: https://discourse.slicer.org/t/calculate-dihedral-angles-using-plug-ins/36116

---

## Post #1 by @YLX (2024-05-13 13:22 UTC)

<p>Hello, I want to calculate the dihedral Angle between two Planes, the plug-in Angle Planes is used, but there are no options P1 and P2 when adding planes (P1 is the yellow plane in the figure, P2 is the name of the purple plane in the figure), but the option of marking points appears. How can I solve this problem? And the built-in Python code you mentioned can also calculate dihedral angles, but why is my python running wrong? Screenshots of the above problems are shown below.</p>
<p>Using the plugin Angle Planes or Python code, which will solve my problem faster and more efficiently? Looking forward to your reply.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00e5682ca0ada7e7144cad37692bcfa60701f3b5.jpeg" data-download-href="/uploads/short-url/7Vv80ofKzbqzzSGLYkLyD8Zonb.jpeg?dl=1" title="N%`~6~S" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00e5682ca0ada7e7144cad37692bcfa60701f3b5_2_566x500.jpeg" alt="N%`~6~S" data-base62-sha1="7Vv80ofKzbqzzSGLYkLyD8Zonb" width="566" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00e5682ca0ada7e7144cad37692bcfa60701f3b5_2_566x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00e5682ca0ada7e7144cad37692bcfa60701f3b5_2_849x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00e5682ca0ada7e7144cad37692bcfa60701f3b5_2_1132x1000.jpeg 2x" data-dominant-color="B3BCC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">N%`~6~S</span><span class="informations">1139×1005 232 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7699d35b10938df0308f7ff9af788d089e52a7fc.jpeg" alt="`(4ICR8BT0R6~H3(WF8Y6O" data-base62-sha1="gVbUvgjCLwQUjAjrOEux9BkTpRq" width="455" height="322"></p>
<p>Operating system:<br>
Slicer version:5.4.0<br>
Expected behavior:<br>
Actual behavior:<br>
Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2024-05-13 19:30 UTC)

<p>I would recommend to just mark point, lines, curves, planes on your models and then write a short Python script that can compute all the distances, angles, etc. that you need. You would need to do much more work (lot of clicks) if you wanted to perform all these measurements using graphical user interface. Code snippets int the [script repository](<a href="https://slicer">https://slicer</a> readthedocs) should be to do most computations and if you need any more complicated custom computation then you can ask Microsoft Copilot or ChatGPT to write the Python script for you.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I assume that such needs are common in morphometry. Can you recommend any tutorials for this; or some modules or maybe some different approaches?</p>

---
