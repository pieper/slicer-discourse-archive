# How to convert volume to segmentation?

**Topic ID**: 1081
**Date**: 2017-09-18
**URL**: https://discourse.slicer.org/t/how-to-convert-volume-to-segmentation/1081

---

## Post #1 by @pwang (2017-09-18 15:29 UTC)

<p>Operating system: Win7<br>
Slicer version: 4.7.0<br>
The original segmentation needs to be registered by deformable image registration (DIR) vector field generated from CT1 to CT2 DIR. My solution is: 1. convert segmentation to volume, 2. perform the DIR from CT1 to CT2, 3. deform seg volume using the vector field from step 2. However, the volume is considered to be one object, which doesn’t have the seg info, such as heart, liver, etc. Is there a way to conver the volume back to segmentation and keep the seg info? Thanks a lot.</p>

---

## Post #2 by @lassoan (2017-09-19 00:59 UTC)

<p>Import the labelmap volume to segmentation using Segmentations module.</p>

---

## Post #3 by @pwang (2017-09-19 17:06 UTC)

<p>Thank you for your reply, Lassoan. But is there a more detail instruction on how to import the lablemap volume? I clicked the Import button, but nothing happened. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0374ab0c93ac8f3c611577e64da5b419b643a210.png" data-download-href="/uploads/short-url/uzolTvFmQFxXx5b5Fu9bNg35AY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0374ab0c93ac8f3c611577e64da5b419b643a210.png" alt="image" data-base62-sha1="uzolTvFmQFxXx5b5Fu9bNg35AY" width="690" height="390" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">886×502 11.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>. However, it doesn’t say how to select the node in the right square. Operation system: Win7. Version: 4.7.0. Thank you very much.</p>

---

## Post #4 by @lassoan (2017-09-19 17:24 UTC)

<p>You can only import labelmap volumes. You have two options for having your volume interpreted as labelmap:</p>
<ul>
<li>Option A: Load your volume as a labelmap: in the <code>Add data</code> dialog click on <code>Show options</code> and check “LabelMap”.</li>
<li>Option B: Convert your grayscale volume to labelmap in the <code>Volumes</code> module, <code>Volume information</code> section, <code>Convert to label map</code> row.</li>
</ul>

---

## Post #5 by @cpinter (2017-09-19 17:33 UTC)

<p>It seems to me you don’t have a segmentation node selected. Create one first on the very top. Then you can import the labelmap. You also didn’t select the labelmap; for that, see Andras’ comment just above.</p>

---

## Post #6 by @pwang (2017-09-20 16:11 UTC)

<p>Thank you’ll for the quick reply. I have tried your suggested methods. They successfully convert the volume into segmentation. However the segmentation won’t be exported out. At first, I just exported the segmentation to dicom, there is the following error message. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcf0a047d5ac87d42308a5ac6cc654d95e3f599b.png" alt="image" data-base62-sha1="qXriOzeq49ltuHAsNtVekA9nmor" width="624" height="479">. But only CT set is exported and segmentation is not. Please help! Thank you.</p>

---

## Post #7 by @cpinter (2017-09-20 17:02 UTC)

<ol>
<li>A Subject needs to be created top-level, not a folder</li>
<li>A Study needs to be in the subject, not a folder</li>
<li>The CT and the segmentation need to be at the same level under the study</li>
</ol>

---

## Post #8 by @cpinter (2017-09-20 17:03 UTC)

<p>You may also want to consider filling out the DICOM tags on the right side: PatientID, PatientName, StudyDescription, etc.</p>

---

## Post #9 by @pwang (2017-09-20 21:19 UTC)

<p>Thank you so much. It solved my problem! Much appreciated!</p>

---

## Post #10 by @11114 (2019-03-10 06:45 UTC)

<p>Hi！  How can I segment the corresponding CT image by ROI?</p>

---

## Post #11 by @dp1991 (2019-03-10 13:10 UTC)

<p>Hi</p>
<p>All Module— &gt; Simple Filter ---- &gt; Crop Image Filter<br>
and then set parameters</p>

---
