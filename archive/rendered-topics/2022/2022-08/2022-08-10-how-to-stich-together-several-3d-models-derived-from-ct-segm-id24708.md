# How to stich together several 3D models derived from CT segmentation? 

**Topic ID**: 24708
**Date**: 2022-08-10
**URL**: https://discourse.slicer.org/t/how-to-stich-together-several-3d-models-derived-from-ct-segmentation/24708

---

## Post #1 by @Nicole_Torres-Tamayo (2022-08-10 09:41 UTC)

<p>Hi there,</p>
<p>I am using 3D slicer to segment some micro-CTs that I have collected for my post-doc research. These micro-CTs are very very heavy because of their high resolution. They are composed 2000-3000 slices in DICOM extension, so when I upload the full stack into 3D slicer, the laptop is not able to segment the full model and crashes after an error message in Slicer, saying that it is running out of memory.</p>
<p>To deal with this problem, I decided to divided the &gt;2000 slice stack intro 4 parts and segment the 4 models separately. This way, when I have the four 3D models and I upload them in a different software, they should be in the original coordinate system (that is, and I can export a final merged 3D model and finally obtain the full anatomical structure). However, when I do this, after segmenting the 4 models in slicer exporting them in .stl format and importing them into whatever other softeware, the models are overlapped, not in the original coordinate system, so I need to align them manually. Please, see screenshot (1st screenshot, how they are, second screenshot, how they should be).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d486aab71c0b76540f141aec80f5843a4bffd289.jpeg" data-download-href="/uploads/short-url/uk5KgbafNfo38UIZL0zMyx8jIU1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d486aab71c0b76540f141aec80f5843a4bffd289.jpeg" alt="image" data-base62-sha1="uk5KgbafNfo38UIZL0zMyx8jIU1" width="575" height="500" data-dominant-color="A0AAA7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">596×518 40.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d70f3c45edb7f9cf5cf6ead51ca9b726ee0c31c.jpeg" data-download-href="/uploads/short-url/8Lx7Jm1O2l6QUA3aylpqeWACEBS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d70f3c45edb7f9cf5cf6ead51ca9b726ee0c31c_2_478x499.jpeg" alt="image" data-base62-sha1="8Lx7Jm1O2l6QUA3aylpqeWACEBS" width="478" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d70f3c45edb7f9cf5cf6ead51ca9b726ee0c31c_2_478x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d70f3c45edb7f9cf5cf6ead51ca9b726ee0c31c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d70f3c45edb7f9cf5cf6ead51ca9b726ee0c31c.jpeg 2x" data-dominant-color="95A59F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">549×574 64.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there any option while exporting from 3D slicer that keeps each 3D model in the original coordinate system and that I may be overlooking in this process?</p>
<p>Thank you very much for your help.</p>
<p>Nicole</p>

---

## Post #2 by @lassoan (2022-08-10 09:46 UTC)

<p>Slicer keeps the models in the original coordinate system. Are the STL files aligned correctly when you load them into Slicer?</p>

---
