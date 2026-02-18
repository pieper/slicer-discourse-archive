# Align Loaded Object (.stl) with Needle

**Topic ID**: 21560
**Date**: 2022-01-21
**URL**: https://discourse.slicer.org/t/align-loaded-object-stl-with-needle/21560

---

## Post #1 by @Srijeet_Chatterjee (2022-01-21 14:05 UTC)

<p>Hello everyone,</p>
<p>Currently I am trying to load an stl file and show a positions of a probe using a tracking device (using Plus Server). The needle provided by OpenIGTLinkIF seems to be 90° apart from the model I am loading. Would be great if anyone can provide some advice on how to fix this issue. Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ef30d4c92614d58bbe68caad0f4802c7601375c.png" data-download-href="/uploads/short-url/28fq6gWcDa2oZ0RyA0YEExyVAU4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ef30d4c92614d58bbe68caad0f4802c7601375c.png" alt="image" data-base62-sha1="28fq6gWcDa2oZ0RyA0YEExyVAU4" width="690" height="303" data-dominant-color="8899CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">865×380 7.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e04a7b1ff8c6a0538420dc0ae3766bf9ab4f984a.png" data-download-href="/uploads/short-url/w0awJZCEVOJyMDfGSzi6CqEfafU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e04a7b1ff8c6a0538420dc0ae3766bf9ab4f984a.png" alt="image" data-base62-sha1="w0awJZCEVOJyMDfGSzi6CqEfafU" width="690" height="302" data-dominant-color="889ACF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">813×356 5.53 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards,<br>
Srijeet</p>

---

## Post #2 by @Srijeet_Chatterjee (2022-01-24 12:47 UTC)

<p>The problem was really simple. But just in case someone faces similar issues, transforming the Obj file in the correct orientation using meshlab would solve the issue.</p>

---
