# Using resampling cli in python script

**Topic ID**: 11918
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/using-resampling-cli-in-python-script/11918

---

## Post #1 by @1116 (2020-06-08 05:08 UTC)

<p>I’m new with 3d slicer cli,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd006b78f4633ce765a462f7a2328dd5924a76b0.png" data-download-href="/uploads/short-url/vx4q45evKcLmKFGyBfSxus2QA0w.png?dl=1" title="캡처" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd006b78f4633ce765a462f7a2328dd5924a76b0_2_690x70.png" alt="캡처" data-base62-sha1="vx4q45evKcLmKFGyBfSxus2QA0w" width="690" height="70" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd006b78f4633ce765a462f7a2328dd5924a76b0_2_690x70.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd006b78f4633ce765a462f7a2328dd5924a76b0_2_1035x105.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/d/dd006b78f4633ce765a462f7a2328dd5924a76b0_2_1380x140.png 2x" data-dominant-color="191B22"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">캡처</span><span class="informations">2233×227 30.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>using this code , I get a volume with Image dimensions (0,0,0)<br>
please tell me what’s wrong with this code</p>
<p>thank you!</p>

---

## Post #2 by @lassoan (2020-06-08 06:07 UTC)

<p>Here is a complete working example of a resampling: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Apply_random_deformations_to_image">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Apply_random_deformations_to_image</a></p>
<p>First check if it works as is, and then modify it step-by-step to make it do what you need.</p>

---

## Post #3 by @1116 (2020-06-09 10:03 UTC)

<p>thank u for your help</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a843efebc808f95398e30435cd3f4167d01bc28.png" data-download-href="/uploads/short-url/aDcFsyWS7WO9EeOiT3DnkiIVzqo.png?dl=1" title="캡처" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a843efebc808f95398e30435cd3f4167d01bc28.png" alt="캡처" data-base62-sha1="aDcFsyWS7WO9EeOiT3DnkiIVzqo" width="406" height="500" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">캡처</span><span class="informations">522×642 5.35 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but if to set parameter regarding manual output para meter (spacing, size…) and transform_matrix manually, how should i set the parameter name?</p>
<p>this command don’t work<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0c8209282185b6aa3cf97c051fbb76505f3cb75.png" data-download-href="/uploads/short-url/tMY5eJuooalHjNInmKyyLHNOvcN.png?dl=1" title="캡처" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0c8209282185b6aa3cf97c051fbb76505f3cb75_2_690x145.png" alt="캡처" data-base62-sha1="tMY5eJuooalHjNInmKyyLHNOvcN" width="690" height="145" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0c8209282185b6aa3cf97c051fbb76505f3cb75_2_690x145.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0c8209282185b6aa3cf97c051fbb76505f3cb75_2_1035x217.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0c8209282185b6aa3cf97c051fbb76505f3cb75_2_1380x290.png 2x" data-dominant-color="171922"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">캡처</span><span class="informations">1642×346 39 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-06-09 12:46 UTC)

<p>What is the error? What do you expect to happen and what happens instead?</p>
<p>Maybe the problem is that you do not to set the output image geometry (origin, spacing, axis directions).</p>

---
