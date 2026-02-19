---
topic_id: 42013
title: "Help With Alignment Of Frankfurt Plane"
date: 2025-03-07
url: https://discourse.slicer.org/t/42013
---

# Help with alignment of Frankfurt Plane

**Topic ID**: 42013
**Date**: 2025-03-07
**URL**: https://discourse.slicer.org/t/help-with-alignment-of-frankfurt-plane/42013

---

## Post #1 by @elijahlee (2025-03-07 09:24 UTC)

<p>Hello, everyone.</p>
<p>I’m afraid I’m new to 3D Slicer and Python. I am currently working on analyzing sexual dimorphism using laser scanned STL format models without DICOM data.</p>
<p>Before operating morphological analysis, I found that imported STL models are not aligned well, so I tried to figure out some solutions from the community. Below is what I saw after importing the model.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f10b98f259e6e893da28737ee10b285b704049d8.png" data-download-href="/uploads/short-url/yonUU0t7KmcLFGo9DOnofArDM5G.png?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f10b98f259e6e893da28737ee10b285b704049d8_2_514x500.png" alt="Screenshot_1" data-base62-sha1="yonUU0t7KmcLFGo9DOnofArDM5G" width="514" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f10b98f259e6e893da28737ee10b285b704049d8_2_514x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f10b98f259e6e893da28737ee10b285b704049d8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f10b98f259e6e893da28737ee10b285b704049d8.png 2x" data-dominant-color="9C9DC3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">657×638 58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to solve the problem by referring to this article (<a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab09_Slicer_Scripting" class="inline-onebox" rel="noopener nofollow ugc">W_2020/Lab09_Slicer_Scripting at master · SlicerMorph/W_2020 · GitHub</a>) to align the model with Frankpurt Plane, but unfortunately, it seems that the Slicer API has been updated and is no longer working. (my current version is 5.8.1.)</p>
<p>After trying to apply code from this discussion, (<a href="https://discourse.slicer.org/t/superimposition-of-cbct-of-orthodontic-patients-using-a-slicer-diagnocat-blender/33510/12" class="inline-onebox">Superimposition of CBCT of orthodontic patients using a slicer, diagnocat, blender - #12 by muratmaga</a>) I repeatedly get the same result as below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/210df6c28c192385e79908a179ce2940221a5b50.png" data-download-href="/uploads/short-url/4IpFN4jvncyIeILUYtFpwIjXlaU.png?dl=1" title="Screenshot_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/210df6c28c192385e79908a179ce2940221a5b50_2_537x500.png" alt="Screenshot_2" data-base62-sha1="4IpFN4jvncyIeILUYtFpwIjXlaU" width="537" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/210df6c28c192385e79908a179ce2940221a5b50_2_537x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/210df6c28c192385e79908a179ce2940221a5b50.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/210df6c28c192385e79908a179ce2940221a5b50.png 2x" data-dominant-color="9C9DC4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_2</span><span class="informations">686×638 56.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Only control points seem to be aligned well, not the model. I may have missed something important due to my mistake.</p>
<p>I kindly ask for troubleshooting after a few days of agony. I would like to ask for some advice on aligning the model to the Frankfurt Plane, which fits into the 3D cube.</p>
<p>Thank you.</p>

---
