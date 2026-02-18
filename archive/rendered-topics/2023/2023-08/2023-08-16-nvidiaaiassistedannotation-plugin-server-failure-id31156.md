# NvidiaAIAssistedAnnotation plugin server failure

**Topic ID**: 31156
**Date**: 2023-08-16
**URL**: https://discourse.slicer.org/t/nvidiaaiassistedannotation-plugin-server-failure/31156

---

## Post #1 by @Vineet_Saravanan (2023-08-16 00:06 UTC)

<p>Hello, I was trying to use the NvidiaAIAssistedAnnotation plugin to segment brain arteries, but I got this following error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce949a5b85ff1aa6501fe5159d4699c535c55d33.png" data-download-href="/uploads/short-url/ttuJPO36qYjxX9HzZaxuSVqRuuv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce949a5b85ff1aa6501fe5159d4699c535c55d33_2_690x165.png" alt="image" data-base62-sha1="ttuJPO36qYjxX9HzZaxuSVqRuuv" width="690" height="165" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce949a5b85ff1aa6501fe5159d4699c535c55d33_2_690x165.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce949a5b85ff1aa6501fe5159d4699c535c55d33.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce949a5b85ff1aa6501fe5159d4699c535c55d33.png 2x" data-dominant-color="EAE8E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1018×244 22.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried searching online, but I could not find a valid server link for the server. I read online that the plugin is no longer being developed, so could that be the reason it is down? Additionally, if it is down, is there any other ai assisted tools that I could use to extract the arteries from a brain MRA scan?</p>

---

## Post #2 by @rbumm (2023-08-16 05:20 UTC)

<p>The program and the servers are no longer maintained by NVIDIA. Please use alternate tools like MONAILabel.</p>

---

## Post #3 by @Vineet_Saravanan (2023-08-16 18:13 UTC)

<p>Hello. I tried MONAILabel, but I am getting the same error with the server as seen here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdffdbcd67b0d777bf837c324df2745e7c12fa29.png" data-download-href="/uploads/short-url/tom3t9pdESJNyTmmkCJz0znJQtH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdffdbcd67b0d777bf837c324df2745e7c12fa29_2_615x500.png" alt="image" data-base62-sha1="tom3t9pdESJNyTmmkCJz0znJQtH" width="615" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdffdbcd67b0d777bf837c324df2745e7c12fa29_2_615x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdffdbcd67b0d777bf837c324df2745e7c12fa29_2_922x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cdffdbcd67b0d777bf837c324df2745e7c12fa29_2_1230x1000.png 2x" data-dominant-color="E2E1EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2008×1632 246 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @rbumm (2023-08-17 05:22 UTC)

<p>You should set up your own MONAILabel Server on the same computer or connect to a distant one you know it is running.</p>
<p><a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html" rel="noopener nofollow ugc">See here</a> or find a full description on MONAILabels Github.</p>

---
