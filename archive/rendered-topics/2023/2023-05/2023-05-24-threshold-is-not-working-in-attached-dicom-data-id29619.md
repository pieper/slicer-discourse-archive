---
topic_id: 29619
title: "Threshold Is Not Working In Attached Dicom Data"
date: 2023-05-24
url: https://discourse.slicer.org/t/29619
---

# Threshold is not working in attached DICOM data

**Topic ID**: 29619
**Date**: 2023-05-24
**URL**: https://discourse.slicer.org/t/threshold-is-not-working-in-attached-dicom-data/29619

---

## Post #1 by @Dwij_Mistry (2023-05-24 04:59 UTC)

<p>I was working with a patient’s data, and it loaded perfectly. However, when I attempted to perform a threshold operation, I noticed that it only applied to the top right corner.</p>
<p>you can download the DICOM data from : <a href="https://www.dropbox.com/s/ts69c4mirm89153/TD3_Maxilla%20mandible%20%26%20cervical%20vtb%20%281%29.zip?dl=0" rel="noopener nofollow ugc">https://www.dropbox.com/s/ts69c4mirm89153/TD3_Maxilla%20mandible%20%26%20cervical%20vtb%20%281%29.zip?dl=0</a></p>
<p>Here is the evidence in the slicer:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a15b58c698aa461a04afcf0a34c43e3e32dee25.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a15b58c698aa461a04afcf0a34c43e3e32dee25.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a15b58c698aa461a04afcf0a34c43e3e32dee25.mp4</a>
    </source></video>
  </div><p></p>
<p>Step1 selecting threshold range<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/967293b0adb2e05666858285cdf6a8990912b301.png" data-download-href="/uploads/short-url/lsV6edYd7TNEcWKlw7GyQCYvovn.png?dl=1" title="step 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/967293b0adb2e05666858285cdf6a8990912b301_2_690x322.png" alt="step 1" data-base62-sha1="lsV6edYd7TNEcWKlw7GyQCYvovn" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/967293b0adb2e05666858285cdf6a8990912b301_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/967293b0adb2e05666858285cdf6a8990912b301_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/967293b0adb2e05666858285cdf6a8990912b301_2_1380x644.png 2x" data-dominant-color="767E7F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step 1</span><span class="informations">1920×897 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Step2 after applying the threshold<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d1bdd1ef980e220b9f67ba43f64c95e73f33bd0.jpeg" data-download-href="/uploads/short-url/49vxKU9MA3JE3kN6DUwFHrc2gFi.jpeg?dl=1" title="step 2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1bdd1ef980e220b9f67ba43f64c95e73f33bd0_2_690x323.jpeg" alt="step 2" data-base62-sha1="49vxKU9MA3JE3kN6DUwFHrc2gFi" width="690" height="323" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1bdd1ef980e220b9f67ba43f64c95e73f33bd0_2_690x323.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1bdd1ef980e220b9f67ba43f64c95e73f33bd0_2_1035x484.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1bdd1ef980e220b9f67ba43f64c95e73f33bd0_2_1380x646.jpeg 2x" data-dominant-color="75767D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step 2</span><span class="informations">1920×900 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And here is the evidence in Mimics:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1f0319c2ae8bab71a5f26919e939d8c95990db1.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1f0319c2ae8bab71a5f26919e939d8c95990db1.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1f0319c2ae8bab71a5f26919e939d8c95990db1.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #2 by @pieper (2023-05-24 17:36 UTC)

<p>Probably you need to set the set the segmentation geometry to match the volume.  Pick the button with the box (above the white arrow in red circle) to get the dialog shown below.  Then pick the CT as the source geometry.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb7df4c6112f1b797810fffde93c7ee39818a546.png" alt="image" data-base62-sha1="xBg43eh2bJn9GQEfvKAZAtRA80m" width="680" height="368"></p>

---
