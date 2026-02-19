---
topic_id: 32443
title: "I Would Like To Ask A Question About Some Ways To Use Markup"
date: 2023-10-27
url: https://discourse.slicer.org/t/32443
---

# I would like to ask a question about some ways to use Markups

**Topic ID**: 32443
**Date**: 2023-10-27
**URL**: https://discourse.slicer.org/t/i-would-like-to-ask-a-question-about-some-ways-to-use-markups/32443

---

## Post #1 by @yeong9316 (2023-10-27 07:53 UTC)

<p>I would like to ask a question about some ways to use Marksup.</p>
<ol>
<li>
<p>When using Plane among the Marksup items, I would like to know how to change the angle of the plane created first. For example, what should I do if I want to change P_3, located on the Transverse Plane, to P_5?</p>
</li>
<li>
<p>I would like to know how to increase the length of a line while fixing the two points that make up the line in Marksup.</p>
</li>
<li>
<p>What should I do if I want to measure the angle between a specific plane and line created with Marksup?</p>
</li>
<li>
<p>Is there a magnetic function between points created with Marksup in 3D Slicer? I want to manipulate another Marksup without changing the position of a specific Point on Coordinate, but the Point continues to move during the manipulation process.</p>
</li>
</ol>
<p>I am always grateful for your kind replies. Any help would be greatly appreciated.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e311840aceda6b48bcea671d398a51f5b849d747.jpeg" data-download-href="/uploads/short-url/woJUCkPGB6c7yiwLLZWtCZDeV03.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e311840aceda6b48bcea671d398a51f5b849d747_2_494x500.jpeg" alt="image" data-base62-sha1="woJUCkPGB6c7yiwLLZWtCZDeV03" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e311840aceda6b48bcea671d398a51f5b849d747_2_494x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e311840aceda6b48bcea671d398a51f5b849d747_2_741x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e311840aceda6b48bcea671d398a51f5b849d747_2_988x1000.jpeg 2x" data-dominant-color="9993B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">996×1007 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rfenioux (2023-10-30 13:07 UTC)

<p>Regarding the first question, you can manipulate a markupsPlane using the interaction handles.</p>
<p>In the markups module, select the plane node and under display &gt; Interaction handles tick the checkboxes “Visibility”, “Enable Translation” and “Enable Rotation”. You can then use the handles in the 2D or 3D views</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f020037906cbcd8e044d6f4fc0e6c712a2e6b0b.png" alt="image" data-base62-sha1="mGEcGtsIcje0Xwa6KxfS78t7YQH" width="527" height="371"></p>

---
