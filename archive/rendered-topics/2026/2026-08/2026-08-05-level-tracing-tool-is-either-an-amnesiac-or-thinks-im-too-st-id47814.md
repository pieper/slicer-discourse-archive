---
topic_id: 47814
title: "Level tracing tool is either an amnesiac or thinks I'm too stupid to segment on my own"
date: 2026-08-05
url: https://discourse.slicer.org/t/47814
last_bumped: 2026-08-08T08:13:36.845Z
---

# Level tracing tool is either an amnesiac or thinks I'm too stupid to segment on my own

**Topic ID**: 47814
**Date**: 2026-08-05
**URL**: https://discourse.slicer.org/t/level-tracing-tool-is-either-an-amnesiac-or-thinks-im-too-stupid-to-segment-on-my-own/47814

---

## Post #1 by @Chelonian (2026-08-05 20:15 UTC)

<p>Operating system: Windows 11 Pro<br>
Slicer version: 5.12.0<br>
Expected behavior: Each level I trace using the “level tracing” tool is saved and placed into the 3d model of that segment<br>
Actual behavior: random sections (consistent across multiple layers) are missing on the axial plane even after segmenting them with the level tracing tool multiple times.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75d21c7189614ae2d7f09d53b25b66b7a8b10329.jpeg" data-download-href="/uploads/short-url/gOi1y9yCnmmeH23G7AtuuWMrhqN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d21c7189614ae2d7f09d53b25b66b7a8b10329_2_343x250.jpeg" alt="image" data-base62-sha1="gOi1y9yCnmmeH23G7AtuuWMrhqN" width="343" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d21c7189614ae2d7f09d53b25b66b7a8b10329_2_343x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d21c7189614ae2d7f09d53b25b66b7a8b10329_2_514x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/75d21c7189614ae2d7f09d53b25b66b7a8b10329_2_686x500.jpeg 2x" data-dominant-color="6E6B7D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×598 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The circled sections are the ones that appear to be missing. (There are some layers that are added back but I did that manually, when it first shows up, the same section is missing across the entire length of the model).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7195e3b8e804316de1590967b47913e416688e5d.jpeg" data-download-href="/uploads/short-url/gcP5DSvoWOE6d1Ik7y5dpZvDelT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/7195e3b8e804316de1590967b47913e416688e5d.jpeg" alt="image" data-base62-sha1="gcP5DSvoWOE6d1Ik7y5dpZvDelT" width="308" height="222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">616×445 80.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edd0d706cd363a30a4a1a5f5f5d99ec937704275.jpeg" data-download-href="/uploads/short-url/xVOB4N1dQOyDR29j5EjLqpoTA9f.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edd0d706cd363a30a4a1a5f5f5d99ec937704275.jpeg" alt="image" data-base62-sha1="xVOB4N1dQOyDR29j5EjLqpoTA9f" width="310" height="225"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">621×451 88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what the missing sections look like on the axial plane. I will go through and use the level tracing tool to section off each layer until I have the full model. Then while I’m checking it I will notice the 3D model has the strange segments missing across every layer (which were not there while I was segmenting the model). If I go back over the layers) which I have multiple times) more sections will go missing as soon as I’m done (I can’t be sure but I think they might be the same sections each time). I can never actually see them disappear, but as I go through the data they just don’t show up again. If anyone has any idea why this may be happening or how to fix it please let me know, this is a cool project I’m working on and the level tracing tool is crucial to it!</p>
<p>(This is what the segments are supposed to look like without the missing sections)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d8acebc97bc6be243be909383ebfdf2688749cf.jpeg" data-download-href="/uploads/short-url/fD3ra7gu0BN8eglYCpStF5aEgt9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d8acebc97bc6be243be909383ebfdf2688749cf.jpeg" alt="image" data-base62-sha1="fD3ra7gu0BN8eglYCpStF5aEgt9" width="322" height="232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">645×464 78.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df2fb2798cc5280428917abb1a5b8a1ec87aa16.jpeg" data-download-href="/uploads/short-url/1ZoN59DaWj4CAdB4JVwENSIWFx4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0df2fb2798cc5280428917abb1a5b8a1ec87aa16.jpeg" alt="image" data-base62-sha1="1ZoN59DaWj4CAdB4JVwENSIWFx4" width="292" height="227"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">585×454 81.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-08-05 21:01 UTC)

<p>The level tracing tool can be very finicky.  If you can develop a concrete set of steps with sample data to reproduce it’s possible someone might know how to fix this, but the original developers of the tool aren’t available.  It’s good that it’s helpful for your use case, but not a lot of people use it.</p>
<p>For most applications grow from seeds was found to be a much more controllable and reliable tool.  Plus it’s natively 3D so less work to use.</p>
<p>Even more recently nnInteractive has proven useful and should definitely be tried.</p>

---

## Post #3 by @Chelonian (2026-08-08 08:13 UTC)

<p>Thank you for the advice, as soon as i figured out how to use grow from seeds it worked much better for my task. Also glad to know I might not be crazy with the level tracing tool.</p>

---
