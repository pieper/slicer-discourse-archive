---
topic_id: 24110
title: "Volume Rendering Problem"
date: 2022-06-29
url: https://discourse.slicer.org/t/24110
---

# Volume Rendering Problem

**Topic ID**: 24110
**Date**: 2022-06-29
**URL**: https://discourse.slicer.org/t/volume-rendering-problem/24110

---

## Post #1 by @morganw3st (2022-06-29 21:38 UTC)

<p>Hello, I have been having issues with Volume Rendering. When I render the scan, it looks fragmented and does not align with the other views. With that, the red, green, and yellow slices all look normal. I also only have one file downloaded into Slicer, so there shouldn’t be an issue of looking at the wrong file. Does anyone have any solutions to solve the glitch in the 3D view?<br>
<a class="mention" href="/u/akralick">@akralick</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a345af8039a4be66011ed895cc272f10b363408b.jpeg" data-download-href="/uploads/short-url/nin7X8bxPfqzyy1VRmaOLTbS3zB.jpeg?dl=1" title="ABB95AE5-52B0-4BBF-8734-7DC80E5E2F7C_1_102_a" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a345af8039a4be66011ed895cc272f10b363408b_2_690x375.jpeg" alt="ABB95AE5-52B0-4BBF-8734-7DC80E5E2F7C_1_102_a" data-base62-sha1="nin7X8bxPfqzyy1VRmaOLTbS3zB" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a345af8039a4be66011ed895cc272f10b363408b_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a345af8039a4be66011ed895cc272f10b363408b_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a345af8039a4be66011ed895cc272f10b363408b_2_1380x750.jpeg 2x" data-dominant-color="848388"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ABB95AE5-52B0-4BBF-8734-7DC80E5E2F7C_1_102_a</span><span class="informations">2404×1308 406 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-06-29 22:54 UTC)

<p>That does not look normal.  Can you share the data to see if it’s something about the data or something with your machine?</p>

---

## Post #3 by @muratmaga (2022-06-29 23:48 UTC)

<p>You are using the experimental Multi Volume rendering technique. Can you try with VTK GPU Raycasting?</p>

---

## Post #4 by @morganw3st (2022-07-11 21:55 UTC)

<p>I tried VTK GPU Raycasting, and unfortunately, it didn’t work. Do you have any other suggestions?</p>

---

## Post #5 by @muratmaga (2022-07-12 00:01 UTC)

<p>Can you share a screenshot what is not working with VTK GPU rendering.</p>
<p>And also share your data?<br>
M</p>

---
