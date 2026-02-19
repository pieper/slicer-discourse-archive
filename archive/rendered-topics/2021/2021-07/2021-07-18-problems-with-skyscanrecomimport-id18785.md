---
topic_id: 18785
title: "Problems With Skyscanrecomimport"
date: 2021-07-18
url: https://discourse.slicer.org/t/18785
---

# Problems with SkyscanRecomimport

**Topic ID**: 18785
**Date**: 2021-07-18
**URL**: https://discourse.slicer.org/t/problems-with-skyscanrecomimport/18785

---

## Post #1 by @hourglassnam (2021-07-18 11:14 UTC)

<p>Dear all,<br>
I am trying to reconstruct the CT images, but it is not working.<br>
I used Skyscan 1272 to achieve the CT data and they are in tiff format.<br>
When I plugged in the tiff data into Volume Rendering or Image Stack, only the Axial data showed up properly, but rest of the reconstructed images were not what it should be.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d394241a810989d89b60856585b0fca9954b358c.jpeg" data-download-href="/uploads/short-url/ubI8usz8FCQGlm4LUubrVzrZnVW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d394241a810989d89b60856585b0fca9954b358c_2_690x420.jpeg" alt="image" data-base62-sha1="ubI8usz8FCQGlm4LUubrVzrZnVW" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d394241a810989d89b60856585b0fca9954b358c_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d394241a810989d89b60856585b0fca9954b358c_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d394241a810989d89b60856585b0fca9954b358c_2_1380x840.jpeg 2x" data-dominant-color="47474D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2876×1752 453 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So the next thing I tried was using the log data.<br>
However, this also did work, showing the error messages such as below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcb7571cf461e53b62113fc3cbe8aae61ed971b8.png" data-download-href="/uploads/short-url/qVszhZ1izNq3DvHAAEjP4OkZZK8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcb7571cf461e53b62113fc3cbe8aae61ed971b8_2_690x416.png" alt="image" data-base62-sha1="qVszhZ1izNq3DvHAAEjP4OkZZK8" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcb7571cf461e53b62113fc3cbe8aae61ed971b8_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcb7571cf461e53b62113fc3cbe8aae61ed971b8_2_1035x624.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcb7571cf461e53b62113fc3cbe8aae61ed971b8_2_1380x832.png 2x" data-dominant-color="2B2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1514×914 67.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any advice will be much appreciated.</p>

---

## Post #2 by @lassoan (2021-07-18 11:23 UTC)

<p>You have loaded a sinogram - a series of projection images. You need to use a toolkit such as <a href="http://www.openrtk.org/">RTK</a> to create a 3D volume from it.</p>
<p>If you want to implement your complete workflow in Slicer then you can implement a Python script or module that launches RTK from Slicer.</p>

---

## Post #3 by @muratmaga (2021-07-18 17:12 UTC)

<p>Tutorial for SkyscanReconImport is here:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport" target="_blank" rel="noopener nofollow ugc">SlicerMorph/Tutorials</a></h3>

  <p><a href="https://github.com/SlicerMorph/Tutorials/tree/main/SkyscanReconImport" target="_blank" rel="noopener nofollow ugc">main/SkyscanReconImport</a></p>

  <p><span class="label1">SlicerMorph module tutorials. Contribute to SlicerMorph/Tutorials development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You have to provide a the <strong>_rec.log</strong>  file as the input. From the screenshot above either you are not passing the correct log file, or the file doesn’t have the fields our module expects.</p>
<p>Did you reconstruct these shadow image (sinograms) with the Nrecon and obtain the cross-sectional slices? That’s what SkyscanReconImport works with. If you did and still have issues, please send us a copy of the log file along with a few of the reconstructed slices…</p>
<p>Thanks,</p>

---

## Post #4 by @hourglassnam (2021-07-23 05:19 UTC)

<p>Thank you guys all for your help!<br>
Sadly, I couldn’t figure out how to use the RTK but I was able to ask the operator for the reconstructed file of the CT images!<br>
After receiving new file, I realized why the SkyscanReconImport did not worked!<br>
I been using _.log file instead of the _rec.log file!<br>
Now my problems are solved.<br>
Once again, thanks to you guys and I wish you have a great day!</p>

---
