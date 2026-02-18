# Diffusion MRI brain extraction

**Topic ID**: 7736
**Date**: 2019-07-24
**URL**: https://discourse.slicer.org/t/diffusion-mri-brain-extraction/7736

---

## Post #1 by @rmukh (2019-07-24 01:56 UTC)

<p>I found two bugs on the brain mask extraction utility (Diffusion Brain Masking) from diffusion images.</p>
<ol>
<li>
<p>It creates a mask which is just a plain square. I think it is the problem with the option ‘Remove islands in Brain Mask’</p>
</li>
<li>
<p>If I disable this option, then inverted mask generated.</p>
</li>
</ol>
<p>Please, find images attached.<br>
Stable release 4.10 works fine.</p>
<p>Package: Slicer-4.11.0-2019-07-22-linux-amd64<br>
OS: Ubuntu 18.04.2 LTS</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72cf59b907be3aca169323c1e777ae29e4e45763.png" data-download-href="/uploads/short-url/gnEG2aMbo2bSSWqTRC2usKeKf1V.png?dl=1" title="Screenshot%20from%202019-07-23%2015-13-00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72cf59b907be3aca169323c1e777ae29e4e45763_2_690x343.png" alt="Screenshot%20from%202019-07-23%2015-13-00" data-base62-sha1="gnEG2aMbo2bSSWqTRC2usKeKf1V" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72cf59b907be3aca169323c1e777ae29e4e45763_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72cf59b907be3aca169323c1e777ae29e4e45763_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72cf59b907be3aca169323c1e777ae29e4e45763_2_1380x686.png 2x" data-dominant-color="7791B3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-07-23%2015-13-00</span><span class="informations">1920×956 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ljod (2019-08-01 15:43 UTC)

<p>THanks. Yes this is due to a bug in ITK 5. I have not yet had time to push the information upstream somehow. There is a workaround in the nightly but it fails if the background is larger than the brain volume. This is helpful if you can share your dataset at a later time for testing.</p>

---
