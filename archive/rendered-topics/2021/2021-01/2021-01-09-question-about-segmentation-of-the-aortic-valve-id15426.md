# Question about segmentation of the aortic valve

**Topic ID**: 15426
**Date**: 2021-01-09
**URL**: https://discourse.slicer.org/t/question-about-segmentation-of-the-aortic-valve/15426

---

## Post #1 by @Anonymous_Person (2021-01-09 18:15 UTC)

<p>Operating system: MacOS<br>
Slicer version:4.11.20200930<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hey everyone!<br>
Pretty new to Slicer, but I’m currently using it to segment a section of the aortic root so that the cusps of the aortic valve and the calcifications are clearly visible.</p>
<p>I used the “Grow from seeds” method to segment the aorta and the the calcified portions and then subsequently rendered the aorta hollow so that a “scissor” operation across it could reveal the valvular commisures.<br>
I’m however having some difficulties with this as I’m unable to smoothen and render the valve correctly.<br>
My current model looks fine for the most part with the exception of the aortic root area where the valve (my region of interest) is.<br>
My goal is to create a model that looks somewhat like the result shown here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a1119c7f2506fae7f5f21e4b7c13801ad799fd1.jpeg" data-download-href="/uploads/short-url/cQLBQw8jKsc5XIXCBLLdcPA93YB.jpeg?dl=1" title="Screen Shot 2021-01-09 at 7.06.50 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a1119c7f2506fae7f5f21e4b7c13801ad799fd1_2_690x381.jpeg" alt="Screen Shot 2021-01-09 at 7.06.50 PM" data-base62-sha1="cQLBQw8jKsc5XIXCBLLdcPA93YB" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a1119c7f2506fae7f5f21e4b7c13801ad799fd1_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a1119c7f2506fae7f5f21e4b7c13801ad799fd1.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a1119c7f2506fae7f5f21e4b7c13801ad799fd1.jpeg 2x" data-dominant-color="171417"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-01-09 at 7.06.50 PM</span><span class="informations">918×508 43.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<a href="https://www.youtube.com/watch?v=BtRkkBCq9cQ&amp;pbjreload=101" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=BtRkkBCq9cQ&amp;pbjreload=101</a></p>
<p>I would really appreciate any help with regards to this.</p>
<p>Thank you so much!</p>

---

## Post #2 by @Arash (2024-04-24 20:43 UTC)

<p>Thank you for your interesting question and sorry that people have not responded to you too. I have a similar problem and cannot utilize 3D Slicer to segment the aortic valve properly, will you share your further experience if you could solve this problem? Many thanks in advance!</p>

---

## Post #3 by @lassoan (2024-04-24 20:53 UTC)

<p>If you find that the current resolution of the labelmap is not fine enough to represent all details then you can follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">these instructions</a>.</p>

---

## Post #4 by @Arash (2024-04-26 08:48 UTC)

<p>Thank you very much Andras for many of your problem-solving comments from which I have learned a lot. The problem is that there are several approaches for what I want to do, and all of them end up with serious errors. For example, I really want to segment aortic valve with each leaflet segmented differently. If I try to use SlicerHeart, it does not work with 3D slicer’s crosshair at all and as soon as I try to put the Valve Annulus Analisis’ Contour Points to locate the Aortic Annulus it terribly changes the focus and I cannot locate the second point correctly. (The same problem happens when using Cardiac’s Valve Segmentation tools.<br>
If I give up using SlicerHeart and try to use regular 3D Slicer’s tools such as Segmentation Editor, as soon as I paint one of the leaflets, it cannot paint anyone of the 2 remaining leaflets. You have given a solution for this problem in a reply to another post mentioning this problem and your suggestion enables the painting again but it could ruin the previously segmented parts.<br>
I don’t know why Paint stops painting after painting the first cusp nor could use SlicerHeart’s Valve Annulus Analyzer &amp; Valve Segmentation because of these problems.</p>

---
