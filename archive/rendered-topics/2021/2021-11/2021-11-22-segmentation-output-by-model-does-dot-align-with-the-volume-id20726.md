# segmentation output by model does dot align with the volume when loaded into Slicer 

**Topic ID**: 20726
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/segmentation-output-by-model-does-dot-align-with-the-volume-when-loaded-into-slicer/20726

---

## Post #1 by @function2 (2021-11-22 14:46 UTC)

<p>Hello, the 3D Slicer Community,</p>
<p>Sorry if this question has been asked many times. I’ve trained a segmentation model for some brain tumor, and I want to review the results in Slicer. When I load them into the Slicer, the segmentation does not overlay at the correct position (see the screenshot of the scene in Slicer and a plot I create with matplotlib, I’m assured that the volume and the output segmentation have the same shape, and the segmentation output by the model for this case is almost correct)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/065dae77225b7c7ee043e3a127e9a7019c680007.jpeg" data-download-href="/uploads/short-url/UjzK9o2W7zfppSsudZ4CGpSPcP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/065dae77225b7c7ee043e3a127e9a7019c680007_2_689x296.jpeg" alt="image" data-base62-sha1="UjzK9o2W7zfppSsudZ4CGpSPcP" width="689" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/065dae77225b7c7ee043e3a127e9a7019c680007_2_689x296.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/065dae77225b7c7ee043e3a127e9a7019c680007_2_1033x444.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/065dae77225b7c7ee043e3a127e9a7019c680007_2_1378x592.jpeg 2x" data-dominant-color="656564"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2392×1029 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-11-22 18:48 UTC)

<p>Some tools discard image geometry (origin, spacing, axis directions). If you visualize image data using tools that ignore this information (such as Matplotlib) then you may not even realize that you have a problem. You need to use a tool like Slicer to realize that there is a misalignment. If you lose the image geometry during your processing workflow then make sure you restore it in the image header before loading it into Slicer.</p>

---
