# Hi, I have problems solving the "couldn't not load.....scalar volume" problem

**Topic ID**: 2840
**Date**: 2018-05-17
**URL**: https://discourse.slicer.org/t/hi-i-have-problems-solving-the-couldnt-not-load-scalar-volume-problem/2840

---

## Post #1 by @felipec_34 (2018-05-17 11:47 UTC)

<p>Operating system: windows 8.1<br>
Slicer version: 4.8.1<br>
Expected behavior: loading the dicom data<br>
Actual behavior: not loading</p>
<p>Please help me with this. I tried to change the dicom information with dicomcleaner but it didn’t work either</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecc174c6b24e6935e95a3170e91add5ef77dd6ae.png" data-download-href="/uploads/short-url/xMr9YCfmjjBDU8K6NkKdwUsB2iO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecc174c6b24e6935e95a3170e91add5ef77dd6ae_2_690x388.png" alt="image" data-base62-sha1="xMr9YCfmjjBDU8K6NkKdwUsB2iO" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecc174c6b24e6935e95a3170e91add5ef77dd6ae_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecc174c6b24e6935e95a3170e91add5ef77dd6ae_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecc174c6b24e6935e95a3170e91add5ef77dd6ae_2_1380x776.png 2x" data-dominant-color="E4E2DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Andinet_Enquobahrie (2018-05-17 13:21 UTC)

<p>You might want to try the SlicerDicomPatcher</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/lassoan/SlicerDicomPatcher">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/lassoan/SlicerDicomPatcher" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/4c6af18ff49b7503e12c90c5ecd7edfd54995bd37f8d8dc496806eacd08c2a30/lassoan/SlicerDicomPatcher" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/lassoan/SlicerDicomPatcher" target="_blank" rel="noopener nofollow ugc">GitHub - lassoan/SlicerDicomPatcher: Module for 3D Slicer that fixes most...</a></h3>

  <p>Module for 3D Slicer that fixes most common errors in DICOM files - GitHub - lassoan/SlicerDicomPatcher: Module for 3D Slicer that fixes most common errors in DICOM files</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2018-05-17 18:04 UTC)

<p>Series of “OT” (other) modality are typically not images and therefore they are not loadable.<br>
Can you load the “CT” series? If not then DICOM patcher module is a good starting point. If you cannot load the CT volume after patching then let us know.</p>

---

## Post #4 by @felipec_34 (2018-05-17 18:20 UTC)

<p>Hi thank you both for your help. I tried the patcher but i got this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/02de8d7a7d4148a925e4a2ed2c37830e648c341e.png" data-download-href="/uploads/short-url/pnLQMnuuV8TxMIsDqzHxdPn6H4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02de8d7a7d4148a925e4a2ed2c37830e648c341e_2_690x388.png" alt="image" data-base62-sha1="pnLQMnuuV8TxMIsDqzHxdPn6H4" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02de8d7a7d4148a925e4a2ed2c37830e648c341e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02de8d7a7d4148a925e4a2ed2c37830e648c341e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/02de8d7a7d4148a925e4a2ed2c37830e648c341e_2_1380x776.png 2x" data-dominant-color="737173"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 274 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @diegotrap (2019-05-03 10:51 UTC)

<p>We have had this problem with DICOM files stored inside directories with names that contain certain “rare” characters (I our case, directories in Spanish with words with accents).</p>
<p>We have changed all the directories to plain names without accents and we are able to avoid this and other Slicer errors (such as sudden closes when trying to save files).</p>

---

## Post #6 by @lassoan (2019-05-03 12:52 UTC)

<p>Please also use latest stable version (Slicer-4.10.1). The DICOM patcher has been made more robust, it does not abort processing if non-DICOM files are encountered.</p>

---

## Post #7 by @samjonas (2019-05-08 09:49 UTC)

<p>Me too had the same problem… thank You guys</p>

---

## Post #8 by @oscar.filevich (2019-07-10 22:10 UTC)

<p>This worked for me too (removing an “ó” from path). Thanks !! (although I also disabled the DWI module in the same trial) using v4.10.2</p>

---

## Post #9 by @Alejandro_Mesa (2020-04-01 20:43 UTC)

<p>This worked for me<br>
Gracias!</p>

---

## Post #10 by @lassoan (2020-04-01 21:34 UTC)

<p>For your information, recent Slicer Preview Releases can load DICOM images from arbitrary paths (even if they contain special characters).</p>

---

## Post #11 by @lassoan (2021-03-07 01:39 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/error-can-not-download-as-scalar-volume/16406/2">ERROR -can  not download …as scalar volume</a></p>

---

## Post #12 by @kaizhao (2022-10-28 23:11 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , just curious what does the <code>DicomPatcher</code> do exactly with the dicom files? I have a look at your code but didn’t get it.</p>
<p>I generated some <code>Ktrans </code>maps using my own codes and save the results to dicom. They cannot be openned by Slicer (but can be opened by Osirix).</p>
<p>Just wanted to know what does <code>DicomPatcher</code> do so that I can pre-process my maps before saving it.</p>
<p>Thanks!</p>

---
