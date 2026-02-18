# Applying N4 bias field correction on TCIA breast DCE-MRI images

**Topic ID**: 28575
**Date**: 2023-03-25
**URL**: https://discourse.slicer.org/t/applying-n4-bias-field-correction-on-tcia-breast-dce-mri-images/28575

---

## Post #1 by @LIE_CAI (2023-03-25 21:01 UTC)

<p>Hi everyone,</p>
<p>I’m trying to do the N4 correction from open-source breast cancer MRI images: <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=22513764#2251376410ab7881a92645bc86da6aa79b0947f9" class="inline-onebox" rel="noopener nofollow ugc">Single site breast DCE-MRI data and segmentations from patients undergoing neoadjuvant chemotherapy (Breast-MRI-NACT-Pilot) - The Cancer Imaging Archive (TCIA) Public Access - Cancer Imaging Archive Wiki</a></p>
<p>These images only show one side of the breast, when I want to do N4 on it by 3D-slicer, I can’t select the volume as input volume in Filtering &gt; N4ITK MRI Bias Correction.<br>
Then I transferred this series of DICOM images into NRRD format, and re-open it but I still couldn’t select it as input volume.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2e493a9c227162968436dfd73c9ec17082ca924.png" data-download-href="/uploads/short-url/pwyIdU6ZDRc85vT5uBPjZFK2oGE.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2e493a9c227162968436dfd73c9ec17082ca924_2_690x283.png" alt="2" data-base62-sha1="pwyIdU6ZDRc85vT5uBPjZFK2oGE" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2e493a9c227162968436dfd73c9ec17082ca924_2_690x283.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2e493a9c227162968436dfd73c9ec17082ca924_2_1035x424.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2e493a9c227162968436dfd73c9ec17082ca924.png 2x" data-dominant-color="898887"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1144×470 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Then I tried to do it in python, but with the error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c7b1d94e03778ca9e3012686b69055126009916.png" data-download-href="/uploads/short-url/8D2qau5BB2ATmyYLkOKKW86pnQa.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c7b1d94e03778ca9e3012686b69055126009916.png" alt="3" data-base62-sha1="8D2qau5BB2ATmyYLkOKKW86pnQa" width="690" height="249" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1417×513 27.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can anyone know how to solve this problem? You can download images from the above links and the “Sagittal-IR_3DFGRE” series was what I used.</p>

---

## Post #2 by @lassoan (2023-03-26 04:14 UTC)

<p>This breast TCIA data set is always very problematic. The main complication is that most images are time sequences.</p>
<p>Most modules will not allow you to select a time sequence as input. If you load the data as “Volume sequence” (using “Advanced” option in the DICOM module) then the current timepoint will show up as a simple scalar volume and so you can run bias correction on it.</p>

---
