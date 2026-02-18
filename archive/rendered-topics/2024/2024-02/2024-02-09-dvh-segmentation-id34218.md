# DVH segmentation

**Topic ID**: 34218
**Date**: 2024-02-09
**URL**: https://discourse.slicer.org/t/dvh-segmentation/34218

---

## Post #1 by @Mouadh_Ben_Nasr (2024-02-09 02:15 UTC)

<p>Hey everyone,<br>
I am conducting a study about selective intraarterial radiation therapy (SIRT) in HCC.<br>
I used Simplicity software (Boston) for segmenting Liver, tumor, perfused volume and normal liver tissue. The isodose curves were created, and the only exportable form is .CSV files.<br>
Is it possible to make the imported dose curves from the DHV .CSV files in 3D sliver, and register them on the already segmented liver and tumor label maps?<br>
Thanks for your help</p>

---

## Post #2 by @lassoan (2024-02-09 02:16 UTC)

<p>You can compute and compare dose volume histograms in Slicer, using SlicerRT extension.</p>

---

## Post #3 by @Mouadh_Ben_Nasr (2024-02-09 08:10 UTC)

<p>I imported the segmentation. But, when importing DHV .csv files, I can’t make further steps.<br>
Here is an exemple<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48b5b67dd96116865b70a3c1e6698a7aa62655fb.jpeg" data-download-href="/uploads/short-url/andH8WpRd7cTnJaxtYu59dMSayD.jpeg?dl=1" title="IMG_9154" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48b5b67dd96116865b70a3c1e6698a7aa62655fb_2_690x362.jpeg" alt="IMG_9154" data-base62-sha1="andH8WpRd7cTnJaxtYu59dMSayD" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48b5b67dd96116865b70a3c1e6698a7aa62655fb_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48b5b67dd96116865b70a3c1e6698a7aa62655fb_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48b5b67dd96116865b70a3c1e6698a7aa62655fb_2_1380x724.jpeg 2x" data-dominant-color="B7BAB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_9154</span><span class="informations">3855×2026 2.13 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thanks for helping me</p>

---

## Post #4 by @lassoan (2024-02-09 10:58 UTC)

<p>I was assuming that you meant DVH (dose volume histogram) and DHV was just a typo, but you keep consistently using the DHV acronym. Could you explain what you mean by DHV?</p>

---

## Post #5 by @Mouadh_Ben_Nasr (2024-02-09 11:00 UTC)

<p>Indeed, I meant the dose volume histogram (DVH).<br>
The only exportable data form is csv file on Simplicity (Boston Scientific), or graph form.</p>

---

## Post #6 by @lassoan (2024-02-10 17:05 UTC)

<p>DVH computation is fairly straightforward. You don’t need to import it from an external software but you can directly compute it in Slicer.</p>

---

## Post #7 by @Mouadh_Ben_Nasr (2024-02-10 17:06 UTC)

<p>Does it work with Yottrium 90 PET/CT or PET/MRI exams?</p>

---

## Post #8 by @lassoan (2024-02-10 17:10 UTC)

<p>Yes, it does not matter what imaging modality you used for creating your segmentation (structure sets) - CT, CBCT, MRI, 3D ultrasound, etc.; and any 3D dose map can be used as input.</p>

---

## Post #9 by @Mouadh_Ben_Nasr (2024-02-10 19:33 UTC)

<p>Which is the appropriate form to export these doses from Simplicity 90Y software (Boston scientific)?</p>

---

## Post #10 by @lassoan (2024-02-11 11:48 UTC)

<p>Probably the best is to export it as DICOM (RTDOSE) file, because that contains all necessary metadata to interpret the voxel values.</p>

---
