# Syncronize 2d slices with 3d camera focal point position in Endoscopy module

**Topic ID**: 41719
**Date**: 2025-02-15
**URL**: https://discourse.slicer.org/t/syncronize-2d-slices-with-3d-camera-focal-point-position-in-endoscopy-module/41719

---

## Post #1 by @Jay39 (2025-02-15 23:06 UTC)

<p>Hi everyone, I’m a bronchoscopist exploring different software options to perform a virtual bronchoscopy and so long 3d slicer has been great. The only thing that I can’t find how to do is, make the 2d visor with the ct scan images to match the position of the 3d camera as it moves thorugh the curve of the flythrough. I can manually jump the slices moving the mouse cursor in the 3d scene while pressing SHIFT but only that. Is there a way to accomplish this, maybe with a python script?<br>
Thank you for your help and thanks too for this great software!</p>

---

## Post #2 by @pieper (2025-02-16 13:39 UTC)

<p>Thanks for the kind words <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>You could try the Volume Reslice Driver in the SlicerIGT extension:</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/SlicerIGT/SlicerIGT?tab=readme-ov-file#volume-reslice-driver">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerIGT?tab=readme-ov-file#volume-reslice-driver" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/735ec429f4b5b2759f6f2ac081530fd3/SlicerIGT/SlicerIGT?tab=readme-ov-file#volume-reslice-driver" class="thumbnail">

  <h3><a href="https://github.com/SlicerIGT/SlicerIGT?tab=readme-ov-file#volume-reslice-driver" target="_blank" rel="noopener">GitHub - SlicerIGT/SlicerIGT: Modules supporting image-guided interventions in...</a></h3>

    <p><span class="github-repo-description">Modules supporting image-guided interventions in 3D Slicer.</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeResliceDriver" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/VolumeResliceDriver</a></p>

---

## Post #3 by @Jay39 (2025-02-19 22:23 UTC)

<p>Thanks, it worked! Exactly what I wanted<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e04c0494ec979f5be78f2884dd9f374b731e1ed3.jpeg" data-download-href="/uploads/short-url/w0dOTPf4i3RDMhsAbikLLdFd4ZR.jpeg?dl=1" title="slicerVB" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e04c0494ec979f5be78f2884dd9f374b731e1ed3_2_690x373.jpeg" alt="slicerVB" data-base62-sha1="w0dOTPf4i3RDMhsAbikLLdFd4ZR" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e04c0494ec979f5be78f2884dd9f374b731e1ed3_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e04c0494ec979f5be78f2884dd9f374b731e1ed3_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/0/e04c0494ec979f5be78f2884dd9f374b731e1ed3_2_1380x746.jpeg 2x" data-dominant-color="A59896"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerVB</span><span class="informations">1916×1037 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
