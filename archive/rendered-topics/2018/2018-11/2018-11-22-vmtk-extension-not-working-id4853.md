# VMTK extension not working?

**Topic ID**: 4853
**Date**: 2018-11-22
**URL**: https://discourse.slicer.org/t/vmtk-extension-not-working/4853

---

## Post #1 by @kantzoul (2018-11-22 21:12 UTC)

<p>Hi all,</p>
<p>So I am trying to extract the vessels from a Partial brain MRA scan however I am having a hard time understanding how to use it as I am not familiar with VMTK. I am able to generate a centerline and vesselness<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d300f9855d5a12f74f96587671a1a7469deb90a.jpeg" data-download-href="/uploads/short-url/fzV0T3amViok2hk2Ri49slRy2bU.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d300f9855d5a12f74f96587671a1a7469deb90a_2_690x471.jpeg" alt="PNG" data-base62-sha1="fzV0T3amViok2hk2Ri49slRy2bU" width="690" height="471" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d300f9855d5a12f74f96587671a1a7469deb90a_2_690x471.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d300f9855d5a12f74f96587671a1a7469deb90a_2_1035x706.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6d300f9855d5a12f74f96587671a1a7469deb90a_2_1380x942.jpeg 2x" data-dominant-color="4B4852"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1390×950 341 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>  filtering to generate the vesselness volume but when I go to use the level set segmentation I only get a piece of the vessels. I have attached a screenshot for you to see.</p>
<p>Kind regards</p>

---

## Post #2 by @lassoan (2018-11-23 03:50 UTC)

<p>Level set segmentation only extracts a single branch between two specified points. There may be other segmentation algorithms in VMTK that are not exposed in Slicer. Please ask VMTK developers about that and report back what they recommended. We may be able to expose additional VMTK features in Slicer.</p>

---

## Post #3 by @Nicholas.jacobson (2019-03-12 04:32 UTC)

<p>Has anyone found a good resource describing all the tools or an uptodate tutorial for VMTK? Everything I see it 8 years old or more.</p>

---
