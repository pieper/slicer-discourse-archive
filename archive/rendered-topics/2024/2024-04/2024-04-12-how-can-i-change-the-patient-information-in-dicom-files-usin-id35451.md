# How can i change the patient information in DICOM files using 3D Slicer during import?

**Topic ID**: 35451
**Date**: 2024-04-12
**URL**: https://discourse.slicer.org/t/how-can-i-change-the-patient-information-in-dicom-files-using-3d-slicer-during-import/35451

---

## Post #1 by @Jake1 (2024-04-12 05:02 UTC)

<p>Operating system: win 10<br>
Slicer version: 5.6.1<br>
For research purposes, I would like to de-identify the CBCT files I have. Does anyone know how to do this?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d61b9b1261d241c0646d81e392b692bd28af049.png" alt="7" data-base62-sha1="4bVdMmILDu5btSNwZqAXhCLfFd7" width="628" height="284"><br>
Sincere thanks!</p>

---

## Post #2 by @pieper (2024-04-12 12:23 UTC)

<p>Slicer doesn’t have that feature built in exactly.  You could load the data and then re-export to dicom with different metadata.</p>
<p>If you are looking to remove patient identifiers you can search the internet and find lots of tools for that, I’m not sure which would best suit your needs.</p>
<p>If you want background on the topic this paper is very thorough:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://arxiv.org/abs/2303.10473">
  <header class="source">
      <img src="https://arxiv.org/static/browse/0.3.4/images/icons/favicon-32x32.png" class="site-icon" width="32" height="32">

      <a href="https://arxiv.org/abs/2303.10473" target="_blank" rel="noopener">arXiv.org</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/402;"><img src="https://static.arxiv.org/icons/twitter/arxiv-logo-twitter-square.png" class="thumbnail" width="500" height="500"></div>

<h3><a href="https://arxiv.org/abs/2303.10473" target="_blank" rel="noopener">Report of the Medical Image De-Identification (MIDI) Task Group -- Best...</a></h3>

  <p>This report addresses the technical aspects of de-identification of medical images of human subjects and biospecimens, such that re-identification risk of ethical, moral, and legal concern is sufficiently reduced to allow unrestricted public sharing...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Jake1 (2024-04-17 15:30 UTC)

<p>Thank you very much for your advice！I will go and learn more about the field.</p>

---

## Post #4 by @lassoan (2024-04-17 17:37 UTC)

<p>Note that if you don’t need any metadata from the data set, just the image data, then an effective way to anonymize is to save the image in .nrrd format.</p>
<p>There may be burnt-in annotations (especially in secondary captures and various reports) and you may need to blur the face, etc. So, depending on your images and your study protocol you might need to modify the image content as well, to make the images harder to reidentify.</p>

---
