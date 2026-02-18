# Plastimatch DRR Generation Export

**Topic ID**: 28455
**Date**: 2023-03-19
**URL**: https://discourse.slicer.org/t/plastimatch-drr-generation-export/28455

---

## Post #1 by @crissina0905 (2023-03-19 18:27 UTC)

<p>Hi everyone,</p>
<p>I am trying to generate 2D digitally reconstructed radiographs from 3D CT scans of the abdomen using the ‘Plastimatch DRR generation’ module. When the DRR renders in the software it looks like the image below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1c4b024fff7129e20852a47e54aafee830eafbf.jpeg" data-download-href="/uploads/short-url/rE9ylHe1xTV8D8q2UwVwEecOGHZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c4b024fff7129e20852a47e54aafee830eafbf_2_690x420.jpeg" alt="image" data-base62-sha1="rE9ylHe1xTV8D8q2UwVwEecOGHZ" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c4b024fff7129e20852a47e54aafee830eafbf_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c4b024fff7129e20852a47e54aafee830eafbf_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1c4b024fff7129e20852a47e54aafee830eafbf_2_1380x840.jpeg 2x" data-dominant-color="888B90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1171 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, when I export it, everything appears white:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffec5d85b0f910433ca69d2e623c4d38a9db034f.jpeg" data-download-href="/uploads/short-url/Aw0afwGRjhyqaWm1oMRt8vKBHhJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffec5d85b0f910433ca69d2e623c4d38a9db034f_2_546x500.jpeg" alt="image" data-base62-sha1="Aw0afwGRjhyqaWm1oMRt8vKBHhJ" width="546" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffec5d85b0f910433ca69d2e623c4d38a9db034f_2_546x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffec5d85b0f910433ca69d2e623c4d38a9db034f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffec5d85b0f910433ca69d2e623c4d38a9db034f.jpeg 2x" data-dominant-color="616060"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">640×586 27.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Does anybody know how I can fix this? Also, in the top right panel in the first image, the projection and the CT image do not have the same orientation, why is that?</p>
<p>FInally, I would be very grateful if I can have some guidance on how to select the SAD, SID and isocenter values.</p>
<p>Thanks for your help!</p>
<p>Cristina</p>

---

## Post #2 by @lassoan (2023-03-19 19:46 UTC)

<p>The images in your screenshots look good. You probably want to adjust the window/level in your viewer to avoid the too bright appearance.</p>

---

## Post #3 by @Mik (2023-03-20 08:26 UTC)

<aside class="quote no-group" data-username="crissina0905" data-post="1" data-topic="28455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/71e660/48.png" class="avatar"> crissina0905:</div>
<blockquote>
<p>Also, in the top right panel in the first image, the projection and the CT image do not have the same orientation, why is that?</p>
</blockquote>
</aside>
<p>The DRR module expects that CT volume has as a standard DICOM orientation. You can change the volume orientation in <code>Transforms</code> module.</p>
<aside class="quote no-group" data-username="crissina0905" data-post="1" data-topic="28455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/71e660/48.png" class="avatar"> crissina0905:</div>
<blockquote>
<p>FInally, I would be very grateful if I can have some guidance on how to select the SAD, SID and isocenter values.</p>
</blockquote>
</aside>
<p>I would recommend to use <code>External Beam Planning</code>, <code>Beams</code>, <code>DRR Image Computation</code> modules in the <code>Radiotherapy</code> subsection.</p>
<ul>
<li>External Beam Planning - create a dummy plan and setup isocenter point or segmentation node for the particular ROI;</li>
<li>Beams - setup RTBeam node parameters;</li>
<li>DRR Image Computation - module to compute DRR image with better UI, that module uses the <code>DRR generation</code> modules as a basis.</li>
</ul>

---

## Post #4 by @gcsharp (2023-03-20 15:22 UTC)

<p>The SAD and SID depend on the equipment, so you will need to check the user manual.  In RT, typical values would be SAD 100 cm and SID 150 cm.</p>

---
