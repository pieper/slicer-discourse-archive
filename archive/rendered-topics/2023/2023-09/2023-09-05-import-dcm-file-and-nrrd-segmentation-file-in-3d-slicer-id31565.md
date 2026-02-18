# Import dcm file and nrrd segmentation file in 3D slicer

**Topic ID**: 31565
**Date**: 2023-09-05
**URL**: https://discourse.slicer.org/t/import-dcm-file-and-nrrd-segmentation-file-in-3d-slicer/31565

---

## Post #1 by @Liang_Ma (2023-09-05 12:21 UTC)

<p>Hello, I have a dataset downloaded from TCIA.</p>
<p>Here for one patient id I have two folders:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/991cf870a2190ed0e06fb2ba3316693ac391ccc9.png" alt="image" data-base62-sha1="lQv7yFjlWERkdLq4YRZEyTNQpdL" width="379" height="141"><br>
The 1st named segmentation folder contains one dcm file and one nrrd file – which I suppose is the segmentation file.<br>
The 2nd folder contains 167 dcm files, which is the 3D series dicom data.</p>
<p>I would like to import both files in 3D slicer so I can check the segmentation visually. But I could not find how–can someone give a step-by-step instruction?</p>

---

## Post #2 by @ebrahim (2023-09-05 13:26 UTC)

<p>Here are step-by-step instructions: <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="inline-onebox" rel="noopener nofollow ugc">Data Loading and Saving — 3D Slicer documentation</a></p>
<p>Note that the steps for DICOM are different from the steps for everything else</p>

---

## Post #3 by @Liang_Ma (2023-09-06 11:02 UTC)

<p><a class="mention" href="/u/ebrahim">@ebrahim</a> Many thanks for the suggestion!</p>
<p>I am able to import dcm series files, then looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04cdf451292a253162545804bcf28db02773eb27.jpeg" data-download-href="/uploads/short-url/GvaewTcFZ6q9qVuzyaolsJ26zl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04cdf451292a253162545804bcf28db02773eb27_2_690x402.jpeg" alt="image" data-base62-sha1="GvaewTcFZ6q9qVuzyaolsJ26zl" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04cdf451292a253162545804bcf28db02773eb27_2_690x402.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04cdf451292a253162545804bcf28db02773eb27_2_1035x603.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04cdf451292a253162545804bcf28db02773eb27.jpeg 2x" data-dominant-color="545358"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1140×665 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then when I am loading the segmentation file from the single dcm file, click the Description area, there is only the “Volume” option there, and can not be assigned to “Segmentation”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e23fdf610f235a790a9590f0d242496dbcb190a2.png" data-download-href="/uploads/short-url/whuKMZNoNqU8fHhTFMTZl5NspVw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e23fdf610f235a790a9590f0d242496dbcb190a2_2_690x172.png" alt="image" data-base62-sha1="whuKMZNoNqU8fHhTFMTZl5NspVw" width="690" height="172" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e23fdf610f235a790a9590f0d242496dbcb190a2_2_690x172.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e23fdf610f235a790a9590f0d242496dbcb190a2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e23fdf610f235a790a9590f0d242496dbcb190a2.png 2x" data-dominant-color="313030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">943×236 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then finally I get only the segmentation shown as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80cd65eca480ed6ed424ee62cea7709df03805ff.png" data-download-href="/uploads/short-url/inrb8NjvUnfV4xNFNmUI7oHl54H.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80cd65eca480ed6ed424ee62cea7709df03805ff_2_689x417.png" alt="image" data-base62-sha1="inrb8NjvUnfV4xNFNmUI7oHl54H" width="689" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80cd65eca480ed6ed424ee62cea7709df03805ff_2_689x417.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/80cd65eca480ed6ed424ee62cea7709df03805ff_2_1033x625.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80cd65eca480ed6ed424ee62cea7709df03805ff.png 2x" data-dominant-color="38383D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1148×694 78.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I really want to do is to have segmentation to map on the dcm file visually, together… Can that be done?</p>

---

## Post #4 by @lassoan (2023-09-07 17:27 UTC)

<p>Please use the Slicer Stable Release (currently 5.4) and let us know if something still does not work as expected.</p>
<p>One issue can be that your segmentation seems to be stored as a fake CT image instead of proper DICOM Segmentation information object. You can still use it, but you may need to do some extra steps (convert the fake CT to labelmap and then convert that to a segmentation).</p>

---
