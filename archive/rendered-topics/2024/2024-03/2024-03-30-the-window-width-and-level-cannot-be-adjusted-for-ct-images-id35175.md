# The window width and level cannot be adjusted for CT images

**Topic ID**: 35175
**Date**: 2024-03-30
**URL**: https://discourse.slicer.org/t/the-window-width-and-level-cannot-be-adjusted-for-ct-images/35175

---

## Post #1 by @XX_Chen (2024-03-30 04:14 UTC)

<p>Hello,</p>
<p>I recently loaded an abdominal CT image in nii.gz format, but unfortunately, the image cannot be adjusted for window/level, neither manually nor automatically. These CT images are from a public dataset, and I have uploaded one of them to Google Drive for everyone to view.Thank you for your help!</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1oPD0pqaV2zDG4b9SzxPB_DWEaqRreLsg/view?usp=drive_link">
  <header class="source">

      <a href="https://drive.google.com/file/d/1oPD0pqaV2zDG4b9SzxPB_DWEaqRreLsg/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1oPD0pqaV2zDG4b9SzxPB_DWEaqRreLsg/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1oPD0pqaV2zDG4b9SzxPB_DWEaqRreLsg/view?usp=drive_link" target="_blank" rel="noopener nofollow ugc">Adrenal_Ki67_Seg_001_0000.nii.gz</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @muratmaga (2024-03-30 04:48 UTC)

<p>Seems to work fine for me:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac59527c45eb8c9a414b8f487141f90dbf8a3f6a.png" data-download-href="/uploads/short-url/oAFuNXihWvI6GrVqdO6pn2Xsuts.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac59527c45eb8c9a414b8f487141f90dbf8a3f6a_2_532x499.png" alt="image" data-base62-sha1="oAFuNXihWvI6GrVqdO6pn2Xsuts" width="532" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac59527c45eb8c9a414b8f487141f90dbf8a3f6a_2_532x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac59527c45eb8c9a414b8f487141f90dbf8a3f6a_2_798x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac59527c45eb8c9a414b8f487141f90dbf8a3f6a_2_1064x998.png 2x" data-dominant-color="9B9996"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1846×1732 493 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01562631165850d7ac724caa61a2aea8c594a065.png" data-download-href="/uploads/short-url/bP3b0Cx1OBhEsWpaUGft1yJQWN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01562631165850d7ac724caa61a2aea8c594a065_2_548x500.png" alt="image" data-base62-sha1="bP3b0Cx1OBhEsWpaUGft1yJQWN" width="548" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01562631165850d7ac724caa61a2aea8c594a065_2_548x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01562631165850d7ac724caa61a2aea8c594a065_2_822x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01562631165850d7ac724caa61a2aea8c594a065_2_1096x1000.png 2x" data-dominant-color="969592"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1866×1700 442 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I drag and dropped it into the Slicer, Slicer read it as a label map due to the. Make sure it is not loaded as labelmap (I think it is due to the _Seg prefix in the filename). Otherwise, it works fine.</p>

---

## Post #3 by @XX_Chen (2024-03-30 05:28 UTC)

<p>Thank you Prof. Maga! I followed your advice and removed ‘Seg’ in the file name, and everything went back to normal!</p>

---
