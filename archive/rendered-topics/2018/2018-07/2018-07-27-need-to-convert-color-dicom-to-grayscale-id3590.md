# Need to convert color dicom to grayscale

**Topic ID**: 3590
**Date**: 2018-07-27
**URL**: https://discourse.slicer.org/t/need-to-convert-color-dicom-to-grayscale/3590

---

## Post #1 by @travesty82 (2018-07-27 02:04 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.8.1<br>
Expected behavior: Convert to grayscale<br>
Actual behavior: Cannot load as a scalar volume</p>
<p>I have PET images that I want to get the SUV values from certain ROIs. However, I cannot load the DICOMs in because they are RGB instead of grayscale. Is there a way to convert this to grayscale? So far I see the “Vector to Scalar Volume” module, but this appears to be for images (.jpg, .png, etc).</p>
<p>I converted my PET to grayscale in MATLAB but I am not confident in the transfer back to Slicer. Is there an easier in-house method for the DICOM files?</p>

---

## Post #2 by @pieper (2018-07-27 14:34 UTC)

<p>How did you end up with RGB PET images?  I suspect they might be secondary captures or other be non-original data and you may not be able to get SUV values out, at least not with the standard tools.</p>
<p>There’s a lot of detail about the kind of PET DICOM Slicer expects, for example in this paper:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://peerj.com/articles/2057/">
  <header class="source">
      <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e91a9ae40359a983bd5440f20d00e51405ba4c9a.png" class="site-icon" data-dominant-color="1AAFFC" width="192" height="192">

      <a href="https://peerj.com/articles/2057/" target="_blank" rel="noopener">PeerJ</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:380/500;"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2a44351bdbe7296acb9b35af12abe6366991601e_2_380x500.jpg" class="thumbnail" data-dominant-color="91839F" width="380" height="500"></div>

<h3><a href="https://peerj.com/articles/2057/" target="_blank" rel="noopener">DICOM for quantitative imaging biomarker development: a standards based...</a></h3>

  <p>Background. Imaging biomarkers hold tremendous promise for precision medicine clinical applications. Development of such biomarkers relies heavily on image post-processing tools for automated image quantitation. Their deployment in the context of...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @fedorov (2018-07-27 14:47 UTC)

<p>Chances are, your DICOM files are secondary captures, and this probably means you won’t be able to use them for quantitation.</p>
<p>It would be difficult to know more without looking at the data.</p>
<p>If you share the data, remember that it is your responsibility to ensure it does not contain patient identifiable information and you are in compliance with the applicable patient privacy rules.</p>

---

## Post #4 by @travesty82 (2018-07-27 15:34 UTC)

<p>Thank you. I will ask the radiologist about this. If this is the case, hopefully I can get the original data.</p>

---

## Post #5 by @travesty82 (2018-07-27 15:36 UTC)

<p>Thank you. I will investigate. I would like to share for more clarity, and will anonymize the DICOMs if I share them.</p>

---
