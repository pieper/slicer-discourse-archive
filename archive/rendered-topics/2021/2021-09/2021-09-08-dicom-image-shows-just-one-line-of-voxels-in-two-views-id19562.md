---
topic_id: 19562
title: "Dicom Image Shows Just One Line Of Voxels In Two Views"
date: 2021-09-08
url: https://discourse.slicer.org/t/19562
---

# Dicom image shows just one line of voxels in two views

**Topic ID**: 19562
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/dicom-image-shows-just-one-line-of-voxels-in-two-views/19562

---

## Post #1 by @S_Arbabi (2021-09-08 10:19 UTC)

<p>Hi, I’m opening a DICOM series from a folder on disk, using the following piece of code:</p>
<pre><code class="lang-auto">    from DICOMLib import DICOMUtils
    with DICOMUtils.TemporaryDICOMDatabase() as db:
      DICOMUtils.importDicom(image_dicom_folder, db)
      patientUIDs = db.patients()
      for patientUID in patientUIDs:
        loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p>but it sometimes shows the image not as it is expected.<br>
I attach two pictures of it:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74cf6e459b3fb71605d7ea7e4b9c11cdd3e219f0.jpeg" data-download-href="/uploads/short-url/gFlNU32tDrsvJjTbQic5afwPFYY.jpeg?dl=1" title="slicer_readdcm" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74cf6e459b3fb71605d7ea7e4b9c11cdd3e219f0_2_639x500.jpeg" alt="slicer_readdcm" data-base62-sha1="gFlNU32tDrsvJjTbQic5afwPFYY" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74cf6e459b3fb71605d7ea7e4b9c11cdd3e219f0_2_639x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74cf6e459b3fb71605d7ea7e4b9c11cdd3e219f0_2_958x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/74cf6e459b3fb71605d7ea7e4b9c11cdd3e219f0_2_1278x1000.jpeg 2x" data-dominant-color="464543"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_readdcm</span><span class="informations">1319×1031 34.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dd42d089326157021923823f4d3e6b05738157c.jpeg" data-download-href="/uploads/short-url/4fSqKrN8PeDIBic3VK9nK8UU6DO.jpeg?dl=1" title="slicer_readdcm2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd42d089326157021923823f4d3e6b05738157c_2_690x490.jpeg" alt="slicer_readdcm2" data-base62-sha1="4fSqKrN8PeDIBic3VK9nK8UU6DO" width="690" height="490" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd42d089326157021923823f4d3e6b05738157c_2_690x490.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd42d089326157021923823f4d3e6b05738157c_2_1035x735.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dd42d089326157021923823f4d3e6b05738157c.jpeg 2x" data-dominant-color="454442"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_readdcm2</span><span class="informations">1317×936 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks for your advise in advance</p>

---

## Post #2 by @lassoan (2021-09-08 17:06 UTC)

<p>How many series are stored in the folder?<br>
How many series show up in the Data module?<br>
Which Slicer version are you using?<br>
Does loading work as expected if you use the DICOM module user interface?</p>

---

## Post #3 by @S_Arbabi (2021-09-08 17:33 UTC)

<p>one series was in the folder, that was working well on 4.11.20210226 but when I updated to 4.13, this showed this behavior. I downgraded to 4.11 and that works correctly.<br>
loading was working correctly when used DICOM module user interface.</p>

---

## Post #4 by @lassoan (2021-09-08 17:44 UTC)

<p>Does it work well with the very latest Slicer Preview Release?</p>
<p>Is the MRI loaded as a time sequence? (you can see that by going to MultiVolume explorer module or Sequence browser module)</p>

---

## Post #5 by @S_Arbabi (2021-09-08 18:08 UTC)

<p>When opened with DICOM module user interface, it shows like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae058d02a4da0fe39245f9d5a68e8ae1acce4b8d.jpeg" data-download-href="/uploads/short-url/oPsYi3kLX0ncVqJttCMUTi2wK97.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae058d02a4da0fe39245f9d5a68e8ae1acce4b8d_2_607x500.jpeg" alt="1" data-base62-sha1="oPsYi3kLX0ncVqJttCMUTi2wK97" width="607" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae058d02a4da0fe39245f9d5a68e8ae1acce4b8d_2_607x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae058d02a4da0fe39245f9d5a68e8ae1acce4b8d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae058d02a4da0fe39245f9d5a68e8ae1acce4b8d.jpeg 2x" data-dominant-color="F7F8F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">802×660 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
but when opened in code above, the same folder shows as the following:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d801cde1fe9a4b87ccedf2c4bc494f9f367e95.jpeg" data-download-href="/uploads/short-url/zEdGlRANWFlrrbqWa7scXaXNgMd.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9d801cde1fe9a4b87ccedf2c4bc494f9f367e95_2_690x474.jpeg" alt="2" data-base62-sha1="zEdGlRANWFlrrbqWa7scXaXNgMd" width="690" height="474" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f9d801cde1fe9a4b87ccedf2c4bc494f9f367e95_2_690x474.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d801cde1fe9a4b87ccedf2c4bc494f9f367e95.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d801cde1fe9a4b87ccedf2c4bc494f9f367e95.jpeg 2x" data-dominant-color="FBFBFB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">923×635 30.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
the “sequence” is showing like one line of voxels.</p>

---

## Post #6 by @lassoan (2021-09-08 18:10 UTC)

<p>Does it work well with the very latest Slicer Preview Release?</p>

---

## Post #7 by @S_Arbabi (2021-09-08 18:19 UTC)

<p>perfect, yes. It works with today’s build of preview release.<br>
Thanks Andras</p>
<p>Best,<br>
Saeed</p>

---

## Post #8 by @S_Arbabi (2021-09-09 06:19 UTC)

<p>one other kind of issue with loading DICOMs is like this image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3ec1006b56112e6964fe9dbd95aeb0bc9148b593.jpeg" data-download-href="/uploads/short-url/8X96EloLPgsGxz6i45LkzMFfw0X.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ec1006b56112e6964fe9dbd95aeb0bc9148b593_2_690x380.jpeg" alt="3" data-base62-sha1="8X96EloLPgsGxz6i45LkzMFfw0X" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ec1006b56112e6964fe9dbd95aeb0bc9148b593_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ec1006b56112e6964fe9dbd95aeb0bc9148b593_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3ec1006b56112e6964fe9dbd95aeb0bc9148b593_2_1380x760.jpeg 2x" data-dominant-color="81817F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1920×1060 90.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
in which a kind of just one slice of image is showing in one view and nothing in the two other views. the range slicer selectors are freezed and not changeable.</p>

---

## Post #9 by @lassoan (2021-09-10 03:39 UTC)

<p>It seems that each slice in the series contains a different instance number. This indicates that this is a time sequence. If it is not a time sequence then most likely the image got corrupted by incorrect anonymization. You may still be able to load it as a single volume if you enable “Advanced” option in DICOM module and choose an item that is not a sequence.</p>

---
