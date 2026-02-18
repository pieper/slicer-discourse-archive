# Pyradiomics feature extraction for bin-width 255

**Topic ID**: 20347
**Date**: 2021-10-25
**URL**: https://discourse.slicer.org/t/pyradiomics-feature-extraction-for-bin-width-255/20347

---

## Post #1 by @Sovan_Mukherjee (2021-10-25 23:01 UTC)

<p>Hi,</p>
<p>I was extracting radiomics features from a CT dataset using PyRadiomics at various bin-widths for a comparison study (25, 32, 255 etc).</p>
<p>I was comparing individual gray level features between bin-width 25 and 255. My CT images are normalized to intensity levels (0 to 255). So, for bin-width 255, I just have 1 gray level.</p>
<p>While comparing GLCM between bin-width 25 and 255 , I noticed that GLCM for bin-width 255 is almost non-existing which makes sense since I have only one gray level. However, while comparing GLRLM between bin-width 25 and 255, I see a similar pattern between bin-width 25 and 255. I have attached three slides describing what is happening.</p>
<p>My question is for bin-width 255, both GLCM and GLRLM should behave in a similar way since we are dealing with only one gray level. But why, GLRLM feature pattern at bin-width 255 are similar to bin-width 25?</p>
<p>Could you please help me figure it out?</p>
<p><strong>Version (please complete the following information):</strong></p>
<ul>
<li>OS: [iOS]</li>
<li>Python version: [3.8.1]</li>
<li>PyRadiomics version [v3.0.1.post3+g0c53d1d]</li>
</ul>
<p>Thank you,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fd46d6174c66ff84ecaa86aac862fed90cf89d0.png" data-download-href="/uploads/short-url/6P7yZGxdWnskULgtJV6sj5Vws2Q.png?dl=1" title="Slide1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fd46d6174c66ff84ecaa86aac862fed90cf89d0_2_690x388.png" alt="Slide1" data-base62-sha1="6P7yZGxdWnskULgtJV6sj5Vws2Q" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2fd46d6174c66ff84ecaa86aac862fed90cf89d0_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fd46d6174c66ff84ecaa86aac862fed90cf89d0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2fd46d6174c66ff84ecaa86aac862fed90cf89d0.png 2x" data-dominant-color="F6F6F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slide1</span><span class="informations">720×405 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c526774c367941e2efddd872fda5ed16ab539a55.png" data-download-href="/uploads/short-url/s84tqOvCqlooqVDp7jql9EwadQp.png?dl=1" title="Slide2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c526774c367941e2efddd872fda5ed16ab539a55_2_690x388.png" alt="Slide2" data-base62-sha1="s84tqOvCqlooqVDp7jql9EwadQp" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c526774c367941e2efddd872fda5ed16ab539a55_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c526774c367941e2efddd872fda5ed16ab539a55.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c526774c367941e2efddd872fda5ed16ab539a55.png 2x" data-dominant-color="F8F7F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slide2</span><span class="informations">720×405 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6ab87fa6127283d68eb8c8d54fb43613b07ff3.png" data-download-href="/uploads/short-url/ibbhMpu7Xu3b8MKnofwkrldfL35.png?dl=1" title="Slide3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f6ab87fa6127283d68eb8c8d54fb43613b07ff3_2_690x388.png" alt="Slide3" data-base62-sha1="ibbhMpu7Xu3b8MKnofwkrldfL35" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f6ab87fa6127283d68eb8c8d54fb43613b07ff3_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6ab87fa6127283d68eb8c8d54fb43613b07ff3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f6ab87fa6127283d68eb8c8d54fb43613b07ff3.png 2x" data-dominant-color="F3F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slide3</span><span class="informations">720×405 26.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
