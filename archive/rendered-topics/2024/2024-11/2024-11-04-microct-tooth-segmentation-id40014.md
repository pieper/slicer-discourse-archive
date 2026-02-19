---
topic_id: 40014
title: "Microct Tooth Segmentation"
date: 2024-11-04
url: https://discourse.slicer.org/t/40014
---

# MicroCT tooth segmentation

**Topic ID**: 40014
**Date**: 2024-11-04
**URL**: https://discourse.slicer.org/t/microct-tooth-segmentation/40014

---

## Post #1 by @r_dientes (2024-11-04 13:28 UTC)

<p>Hello!<br>
I’m starting to segment microCT images and I wanted to segment separately<br>
enamel, dentin and pulp canal.<br>
My doubt arises from my still little experience and that I have Micro-CT images that are quite heavy for my computer. For this reason, I need to lower the quality of the images but then be able to distinguish the structures well to be able to segment. Any recommendations? I leave you a screenshot of my work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0.jpeg" data-download-href="/uploads/short-url/h5IlKdhm0yDsO8WtXJCCy6Mpeb6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0_2_690x366.jpeg" alt="image" data-base62-sha1="h5IlKdhm0yDsO8WtXJCCy6Mpeb6" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77ca59772122485f6e54524349c0a6a7c42c1ee0_2_1380x732.jpeg 2x" data-dominant-color="8F8F94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1020 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-11-04 18:39 UTC)

<p>Looks like you successfully imported your imagestack. To downsample you have couple different options:</p>
<ol>
<li>
<p>You can use the cropVolume of Slicer to reduce it to a size managable by your computer. Looks like your images are 13.2 microns. Perhaps you can try scaling factor of 1.52, which would give you approximately 20 micron resolution while reducing the data size 3.5 times. You can experiment with the scaling factor to find a resolution that still keeps the detail you want to see, but not data is not too large for your computer.</p>
</li>
<li>
<p>Another option is to use ImageStacks module of SlicerMorph extension. It does have the option of reducing the data at the time of import. However, it is not as flexible as the CropVolume reduction factor will be either 2 (half quality) or 4 (preview quality).</p>
</li>
</ol>
<p>So unless you hit a memory issue, i would suggest you use the first option.</p>

---
