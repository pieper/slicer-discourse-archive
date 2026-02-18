# Radiomics developing a blank table?

**Topic ID**: 16618
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/radiomics-developing-a-blank-table/16618

---

## Post #1 by @jmunchel (2021-03-18 14:51 UTC)

<p>Operating system: MacOS 10.15.7<br>
Slicer version: 4.11.20200930 r29402<br>
Expected behavior: Radiomics will use a PET scan as an input image volume and a lung segmentation as the input region to present descriptive statistics of the SUV values in a table.<br>
Actual behavior: Table is blank</p>
<p>I’ve done this exact same process 8 prior times and it has always worked fine. Not sure why the table is blank now?</p>
<p>Not sure if this is helpful:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9ad4cb12f2c0b4d2d2f5e57b2dc1a4b7d875da68.png" data-download-href="/uploads/short-url/m5Hr9iccluYmlWrc9SbYsxkydle.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ad4cb12f2c0b4d2d2f5e57b2dc1a4b7d875da68_2_690x222.png" alt="image" data-base62-sha1="m5Hr9iccluYmlWrc9SbYsxkydle" width="690" height="222" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ad4cb12f2c0b4d2d2f5e57b2dc1a4b7d875da68_2_690x222.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ad4cb12f2c0b4d2d2f5e57b2dc1a4b7d875da68_2_1035x333.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ad4cb12f2c0b4d2d2f5e57b2dc1a4b7d875da68_2_1380x444.png 2x" data-dominant-color="F0F0F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3584×1158 376 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-03-18 18:17 UTC)

<p>Can you clarify if it’s one particular dataset that isn’t working or is it a new version of SlicerRadiomics that isn’t working on any dataset?</p>

---

## Post #3 by @jmunchel (2021-03-18 19:45 UTC)

<p>It seems to just be this one dataset.</p>

---

## Post #4 by @pieper (2021-03-18 21:32 UTC)

<p>If you can share the (anonymized) dataset that fails probably someone can have a look.  Or you could run the radiomics extraction process in python from the command line to see what happens.</p>

---
