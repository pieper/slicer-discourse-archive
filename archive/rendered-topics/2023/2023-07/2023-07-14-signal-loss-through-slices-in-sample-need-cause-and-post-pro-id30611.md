# Signal loss through slices in sample. Need Cause and Post-Processing suggestions

**Topic ID**: 30611
**Date**: 2023-07-14
**URL**: https://discourse.slicer.org/t/signal-loss-through-slices-in-sample-need-cause-and-post-processing-suggestions/30611

---

## Post #1 by @nasibov_98 (2023-07-14 16:36 UTC)

<p>Hi, I am working on a project to segment tumours and livers automatically in FLASH axial images of mouse livers. There is progressive signal loss as I approach the bottom-most slices in a 45 slice image.</p>
<p>I have attached a figure with slices from a single MRI scan and image acquisition parameters in case it comes in handy.</p>
<ol>
<li>
<p>Can you please help me Identify the phenomenon that is causing this signal loss? E.g. Is it Magnetic Field Inhomogeneity? Crosstalk? Is it the positioning of the coil around the mouse abdomen?</p>
</li>
<li>
<p>Do you have any suggestions on post-processing to correct for this?</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b5423a02905497438b027ce4af1c3e8b51fe00f.png" data-download-href="/uploads/short-url/8sQr9YXNVXZOMv3ecpTucIeYqd1.png?dl=1" title="Acquisition Parameters" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b5423a02905497438b027ce4af1c3e8b51fe00f_2_690x281.png" alt="Acquisition Parameters" data-base62-sha1="8sQr9YXNVXZOMv3ecpTucIeYqd1" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b5423a02905497438b027ce4af1c3e8b51fe00f_2_690x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b5423a02905497438b027ce4af1c3e8b51fe00f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b5423a02905497438b027ce4af1c3e8b51fe00f.png 2x" data-dominant-color="EDECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Acquisition Parameters</span><span class="informations">744×303 41.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddfbb590cd6291c2dad66cdc5f5b4750d36d197a.jpeg" alt="Signal Loss" data-base62-sha1="vFKNWsrZKUniBoAflCJpMbBGpgm" width="612" height="396"></p>
<p>If I can know the cause, I can do the research to come up with an image processing solution. Your help is greatly appreciated!</p>
<p>Cheers,</p>
<p>Ulvi</p>
<p>Operating system: MAC OS<br>
Slicer version: 5.2.2</p>

---

## Post #2 by @lassoan (2023-07-14 17:36 UTC)

<p>It seems that your images require bias field correction. You can use <code>N4 ITK MRI Bias correction</code> module for that.</p>

---

## Post #3 by @nasibov_98 (2023-07-17 15:43 UTC)

<p>Thank you for your response. Bias Field Correction seems to be a rabbit hole of research in itself. I tried to learn the mathematics of how it works, but it is beyond me at this stage. I worked through different parameter sets through pure trial and error, and was only able to improve the images ever so slightly, I think there is significant signal loss after slice 30 because the lower abdomen is out of the coil used to image. Thank you for your help and for your contribution to the Slicer 3D toolkit!</p>
<p>Cheers,</p>
<p>Ulvi</p>

---
