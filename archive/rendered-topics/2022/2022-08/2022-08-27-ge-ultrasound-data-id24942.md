# GE ultrasound data

**Topic ID**: 24942
**Date**: 2022-08-27
**URL**: https://discourse.slicer.org/t/ge-ultrasound-data/24942

---

## Post #1 by @whu (2022-08-27 07:50 UTC)

<p>Dear all,</p>
<p>There has patch method for loading philips US data.</p>
<p>How about the Normal format DICOM data of the GE ？</p>
<p>When load the GE US data, System error:</p>
<p>Warning in DICOM plugin Image sequence when examining loadable 0001: US [0008]: Image spacing may need to be calibrated for accurate size measurements.</p>
<p>Finally it can show the result ,but can not use other module.</p>

---

## Post #2 by @lassoan (2022-08-27 22:57 UTC)

<p>Ultrasound images are usually saved into DICOM as a screen capture. This screen capture contains RGB color images, while most modules expect simple scalar images. You can use <code>Vector to Scalar Volume</code> to convert the RGB color image to a scalar image that can be used by all modules.</p>

---

## Post #3 by @whu (2022-09-13 08:34 UTC)

<p>When adding DICOM data(GE Ultrasound data),The warning is like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127742266115f62f9b23f3cb095a072c85c78087.png" data-download-href="/uploads/short-url/2Dm6tlgCUtPlE9NI1lsXa3n84Qf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/127742266115f62f9b23f3cb095a072c85c78087.png" alt="image" data-base62-sha1="2Dm6tlgCUtPlE9NI1lsXa3n84Qf" width="690" height="324" data-dominant-color="E5EBF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">982×462 31.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to use this data in the SlicerHeart module.<br>
Is this kind of problem serious？</p>

---

## Post #4 by @lassoan (2022-09-13 11:21 UTC)

<p>This suggests that the series is not a 3D image or the 3D information is stored in private fields. See more information here: <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md#ge" class="inline-onebox">SlicerHeart/ImageImportExport.md at master · SlicerHeart/SlicerHeart · GitHub</a></p>

---

## Post #5 by @whu (2022-09-14 14:09 UTC)

<p>I found the Image3dAPI on github</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/MedicalUltrasound/Image3dAPI">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/MedicalUltrasound/Image3dAPI" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/0994fce44a404b40cc7580dc9bb8ea0d9c670d6dee83f5a7c64ad43475b8108a/MedicalUltrasound/Image3dAPI" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/MedicalUltrasound/Image3dAPI" target="_blank" rel="noopener nofollow ugc">GitHub - MedicalUltrasound/Image3dAPI: Interface for loading 3D ultrasound data</a></h3>

  <p>Interface for loading 3D ultrasound data. Contribute to MedicalUltrasound/Image3dAPI development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Is this what the exact one for GE US data ?<br>
thanks.</p>

---

## Post #6 by @lassoan (2022-09-14 18:41 UTC)

<p>The repository you have found is only the API specification and examples. You need to get the Image3dAPI loader for GE images (Image3dLoaderGe.dll) as described on the page that I linked above.</p>

---

## Post #7 by @whu (2022-09-19 06:34 UTC)

<p>It seemed that this is not open for China. So trouble… no…</p>

---

## Post #8 by @lassoan (2022-09-19 07:53 UTC)

<p>Contact GE people. Maybe <a href="https://twitter.com/eigilsa/status/1288163425244385280">Eigil Samset</a> can help you.</p>

---
