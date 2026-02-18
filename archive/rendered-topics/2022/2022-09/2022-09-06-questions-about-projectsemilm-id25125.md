# Questions about projectSemiLM

**Topic ID**: 25125
**Date**: 2022-09-06
**URL**: https://discourse.slicer.org/t/questions-about-projectsemilm/25125

---

## Post #1 by @yyl (2022-09-06 15:06 UTC)

<p>Dear all,<br>
I successfully transferred semilandmarks from the temple to the specimen, but some semilandmarks have no contact with the surface of the model. Some points run inside the model. I tried to change the Projection scale. It does not work. What should I do next?<br>
Thank you very much!<br>
Best wishes<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d12db30a7624fbc09a437f82ef95862f6bb90b8.jpeg" data-download-href="/uploads/short-url/fyUruUqCMJJQv9cUylohu52UWJG.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d12db30a7624fbc09a437f82ef95862f6bb90b8_2_690x476.jpeg" alt="image" data-base62-sha1="fyUruUqCMJJQv9cUylohu52UWJG" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d12db30a7624fbc09a437f82ef95862f6bb90b8_2_690x476.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6d12db30a7624fbc09a437f82ef95862f6bb90b8_2_1035x714.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d12db30a7624fbc09a437f82ef95862f6bb90b8.jpeg 2x" data-dominant-color="9E9C9D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1226×847 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @smrolfe (2022-09-06 18:14 UTC)

<p>The most likely issue would be a very large difference or incorrect mapping between the individual and the template. Would you be able to share the template model and landmarks, plus this model?</p>

---

## Post #3 by @yyl (2022-09-07 01:48 UTC)

<p>I can not upload files here, so I upload them somewhere else.<br>
These are my template module, specimen module, and landmarks.Thanks!<br>
<a href="https://www.researchgate.net/post/Questions_about_projectSemiLM" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.researchgate.net/post/Questions_about_projectSemiLM</a></p>

---

## Post #4 by @smrolfe (2022-09-07 16:56 UTC)

<p>Thanks for sharing these samples. The order of the last two landmarks on the specimen is reversed compared to the template, so the TPS transform is estimated incorrectly. Swapping these two landmarks will correct the issue.</p>

---

## Post #5 by @yyl (2022-09-08 07:59 UTC)

<p>I changed the order of these two landmarks, and it does work! Thank you very much!</p>

---
