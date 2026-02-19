---
topic_id: 15554
title: "Save Stl Segmentation To Image Format"
date: 2021-01-16
url: https://discourse.slicer.org/t/15554
---

# Save stl segmentation to image format

**Topic ID**: 15554
**Date**: 2021-01-16
**URL**: https://discourse.slicer.org/t/save-stl-segmentation-to-image-format/15554

---

## Post #1 by @Moran_Artzi (2021-01-16 14:23 UTC)

<p>HI<br>
I have stl file and CT file (on which the segmentation was perform)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4810871bd245a04df63d00d3653b43475a96395.jpeg" data-download-href="/uploads/short-url/ntgKW6f7ytMb1qMWRQXQXYk5Bf7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4810871bd245a04df63d00d3653b43475a96395_2_690x450.jpeg" alt="image" data-base62-sha1="ntgKW6f7ytMb1qMWRQXQXYk5Bf7" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a4810871bd245a04df63d00d3653b43475a96395_2_690x450.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4810871bd245a04df63d00d3653b43475a96395.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4810871bd245a04df63d00d3653b43475a96395.jpeg 2x" data-dominant-color="88898B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">779×509 89.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I convert and save my stl file into dicom / nifti or other image format at the same dimension as the orig CT image?</p>
<p>Thanks a lot<br>
Moran</p>

---

## Post #2 by @lassoan (2021-01-16 15:19 UTC)

<p>Yes, you can do all this conversions in Slicer:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">import surface mesh into segmentation</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#dicom-export">export segmentation to DICOM</a></li>
</ul>

---

## Post #3 by @Moran_Artzi (2021-01-16 16:03 UTC)

<p>Thanks for your reply<br>
Trying to do so<br>
I got dicom files with different dimensions</p>
<p>768X120X216 for the CT image file (449 dicom images) - correct dimensions</p>
<p>288X120X449 for the segmentation file (449 dicom images)</p>
<p>What did I do wrong?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a82fe099371914f5665bf93735dcbc3db26d48.png" alt="image.png" data-base62-sha1="v3tWUfF910wmmSm0cOiUYbA1ViM" width="562" height="383"></p>

---

## Post #4 by @lassoan (2021-01-16 16:07 UTC)

<p>Did you export RT structure set or DICOM segmentation object?</p>

---

## Post #5 by @Moran_Artzi (2021-01-16 16:12 UTC)

<p>I did the follow</p>
<p>Need to do differently?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8c4ba9b227cecf768afe9d80a7704a7f3cecd3.png" data-download-href="/uploads/short-url/flpFC2blHMAFpfN2tKw0GNUmzFF.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b8c4ba9b227cecf768afe9d80a7704a7f3cecd3_2_562x326.png" alt="image.png" data-base62-sha1="flpFC2blHMAFpfN2tKw0GNUmzFF" width="562" height="326" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b8c4ba9b227cecf768afe9d80a7704a7f3cecd3_2_562x326.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8c4ba9b227cecf768afe9d80a7704a7f3cecd3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8c4ba9b227cecf768afe9d80a7704a7f3cecd3.png 2x" data-dominant-color="EDF1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">780×452 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e942dfa9ae713fa1e705d429dd90f3b45f5049f.png" data-download-href="/uploads/short-url/8VB4K5WuCalDdqeirv9Aj4c3lqn.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e942dfa9ae713fa1e705d429dd90f3b45f5049f.png" alt="image.png" data-base62-sha1="8VB4K5WuCalDdqeirv9Aj4c3lqn" width="562" height="450" data-dominant-color="EEF1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">644×516 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2021-01-16 16:27 UTC)

<p>What format you would like to save the segmentation to (fake CT, segmentation object, RT structure set)? If you are not sure, can you tell a bit more about your complete workflow, about what is your overall goal?</p>

---

## Post #7 by @Moran_Artzi (2021-01-18 06:34 UTC)

<p>Yes SlicerRT is (now) installed but does not seems to add saving options<br>
From <strong>Data</strong> modul &gt; <strong>NewStudy</strong> hierarchy i selected <strong>Export to Dicom</strong></p>
<p>This open the following GUI and enable me to save (sepeatly) my CT and my segmentation file (z4338682_Trachea_w[1]_s[0.6]_V1) into 2 dicom series however with different dimensions:</p>
<p>768X120X216 for the CT image file (449 dicom images) - correct dimensions<br>
288X120X449 for the segmentation file (449 dicom images)</p>
<p>Can You please assist me with this issue?</p>
<p>If you agree I can send you both files</p>
<p>Thanks a lot<br>
Moran</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b53c2ba5ccd6a9ba6e3818a7c7161230fa447ee.png" alt="image.png" data-base62-sha1="aKngx2ZpcZFkdEpqFT48ExFXNYa" width="193" height="202"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a19b0e8f558e07c5e47eb58047626f7eec139b63.png" data-download-href="/uploads/short-url/n3D4ZGEXEEp376kXVdVSDMcwX87.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a19b0e8f558e07c5e47eb58047626f7eec139b63_2_297x234.png" alt="image.png" data-base62-sha1="n3D4ZGEXEEp376kXVdVSDMcwX87" width="297" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a19b0e8f558e07c5e47eb58047626f7eec139b63_2_297x234.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a19b0e8f558e07c5e47eb58047626f7eec139b63_2_445x351.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a19b0e8f558e07c5e47eb58047626f7eec139b63_2_594x468.png 2x" data-dominant-color="F0F3F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">648×510 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8c4ba9b227cecf768afe9d80a7704a7f3cecd3.png" data-download-href="/uploads/short-url/flpFC2blHMAFpfN2tKw0GNUmzFF.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8c4ba9b227cecf768afe9d80a7704a7f3cecd3.png" alt="image.png" data-base62-sha1="flpFC2blHMAFpfN2tKw0GNUmzFF" width="690" height="399" data-dominant-color="EDF1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">780×452 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e942dfa9ae713fa1e705d429dd90f3b45f5049f.png" data-download-href="/uploads/short-url/8VB4K5WuCalDdqeirv9Aj4c3lqn.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e942dfa9ae713fa1e705d429dd90f3b45f5049f.png" alt="image.png" data-base62-sha1="8VB4K5WuCalDdqeirv9Aj4c3lqn" width="624" height="500" data-dominant-color="EEF1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">644×516 22.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @cpinter (2021-01-18 10:12 UTC)

<p>I think you should try to export the segmentation not the labelmap. It’s the object with the same name above the labelmap you have selected.</p>

---

## Post #9 by @Moran_Artzi (2021-01-18 10:44 UTC)

<p>Thanks for your reply I tried to export the segmentation<br>
[the labelmap does not have dicom identification]<br>
still - i get dicom files of the segmentation but with Coordinates that do not match the CT image</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/169c797e3a2fb06c5556ea45aa72948c9316987a.png" data-download-href="/uploads/short-url/3e1KtrNVXBfeznRf3qZU2BObOkO.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/169c797e3a2fb06c5556ea45aa72948c9316987a.png" alt="image.png" data-base62-sha1="3e1KtrNVXBfeznRf3qZU2BObOkO" width="472" height="371" data-dominant-color="EFF1F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">652×513 21 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a04f2dc003a886c0b47607bcf6bdc758aee0eb9c.png" alt="image.png" data-base62-sha1="mSa2a4qXN5G7pIngB0RKBJXaCVS" width="517" height="397"></p>

---

## Post #10 by @lassoan (2021-01-18 14:53 UTC)

<p><a class="mention" href="/u/moran_artzi">@Moran_Artzi</a> There are many ways of representing segmentations in DICOM. Slicer supports 3 of them. To avoid unnecessary work for you and us, we first need to understand what you would like to achieve.</p>
<p>What format you would like to save the segmentation to (fake CT, segmentation object, RT structure set)? If you are not sure, can you tell a bit more about your complete workflow, about what is your overall goal?</p>

---

## Post #11 by @Moran_Artzi (2021-01-18 15:12 UTC)

<p>Thanks for your reply<br>
my main goal is to save the segmentation file in image format (as dicom / nifti / analyze) with the same dimension as the orig CT image in order to utilize this data as training data for deep learning segmentation model</p>

---

## Post #12 by @lassoan (2021-01-18 16:20 UTC)

<p>DICOM excels as an archival and data exchange format and very bad for storing working copies of image volume, as it is just way too inefficient and complicated for that purpose. Nifti is a neuroimaging file format. If you work with brain images then you can use that. In all other cases, I would recommend the simple and general-purpose nrrd file format.</p>
<p>Latest Slicer Stable Release will create the segmentation by default with the same geometry as the first selected master volume, but if that is not what you need then you need to select a reference volume when you <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume">export to labelmap volume</a>.</p>
<p>In Latest Slicer Preview Release it is even simpler: you can set reference volume and all other options in <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">Export to files</a>.</p>

---

## Post #13 by @Moran_Artzi (2021-01-18 17:28 UTC)

<p>Thanks a lot<br>
it worked !</p>

---
