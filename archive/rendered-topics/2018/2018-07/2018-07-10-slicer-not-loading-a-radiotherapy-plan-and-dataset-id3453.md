---
topic_id: 3453
title: "Slicer Not Loading A Radiotherapy Plan And Dataset"
date: 2018-07-10
url: https://discourse.slicer.org/t/3453
---

# Slicer not loading a radiotherapy plan and dataset

**Topic ID**: 3453
**Date**: 2018-07-10
**URL**: https://discourse.slicer.org/t/slicer-not-loading-a-radiotherapy-plan-and-dataset/3453

---

## Post #1 by @Lowey (2018-07-10 21:35 UTC)

<p>Operating system: Windows 7</p>
<p>Slicer version: 4.8.1</p>
<p>Expected behavior: To be able to examine and load a radiotherapy dataset without errors</p>
<p>Actual behavior: I receive the following errors when trying to ‘examine’ my data:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63e565ad20f673734f0c9023d1064ca73fd1f2f7.png" alt="Error1" data-base62-sha1="efIKxSXpcOjtkuIWKZRQQKQo6ph" width="241" height="115"></p>
<p>and then when I ‘load’ the data I get the following error,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98a42581550fc6974c584e903e8537bf528e960.png" data-download-href="/uploads/short-url/qtmy9HeELiaR3UFjpJQlQpsQYZG.png?dl=1" title="Error3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b98a42581550fc6974c584e903e8537bf528e960_2_479x500.png" alt="Error3" data-base62-sha1="qtmy9HeELiaR3UFjpJQlQpsQYZG" width="479" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b98a42581550fc6974c584e903e8537bf528e960_2_479x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98a42581550fc6974c584e903e8537bf528e960.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98a42581550fc6974c584e903e8537bf528e960.png 2x" data-dominant-color="EAECEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error3</span><span class="informations">481×502 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be greatly appreciated. I have run this dataset on my personal computer with no issues. So, I expect there may be some issue with the hospital network on the computer I am trying to run this on</p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2018-07-11 00:09 UTC)

<p>Check out tips on <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#When_I_click_on_.22Load_selection_to_slicer.22_I_get_an_error_message_.22Could_not_load_..._as_a_scalar_volume.22">DICOM FAQ page</a>. If you cannot resolve the issue then the best would be to share a phantom or anonymized dataset with us.</p>

---

## Post #3 by @Lowey (2018-07-11 01:18 UTC)

<p>My DICOM dataset is not the issue I’m fairly sure. This is because I have Slicer installed on a personal laptop and can load the exact same dataset with no issues.</p>
<p>However on my hospital computer I run into the issues posted above. I have attempted the tips on the DICOM FAQ page with no success.</p>
<p>I have attached the error messages I receive in the python console when simply starting Slicer,<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0e076d6209d9cc620b3ba7b28daf2363544de08.png" data-download-href="/uploads/short-url/ymTvkaU3mMmX3bTZoOUW9zYdyOI.png?dl=1" title="Error4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0e076d6209d9cc620b3ba7b28daf2363544de08_2_690x232.png" alt="Error4" data-base62-sha1="ymTvkaU3mMmX3bTZoOUW9zYdyOI" width="690" height="232" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0e076d6209d9cc620b3ba7b28daf2363544de08_2_690x232.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0e076d6209d9cc620b3ba7b28daf2363544de08_2_1035x348.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f0e076d6209d9cc620b3ba7b28daf2363544de08_2_1380x464.png 2x" data-dominant-color="D7D6D9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error4</span><span class="informations">3200×1080 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2018-07-11 01:31 UTC)

<p>It seems that SlicerRT extension installation is corrupted. Please try to uninstall SlicerRT and reinstall.</p>

---

## Post #5 by @Lowey (2018-07-11 01:38 UTC)

<p>Hi Andras,</p>
<p>Thanks for your speedy reply. I just attempted an uninstall and reinstall of Slicer 3.8.1 and then an install of SlicerRT but I still get the same error messages upon starting Slicer,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22380013e274399d4ed721afc67de9e610182475.png" data-download-href="/uploads/short-url/4SIdgY7cvy1NTxEF3dEpPhERTrn.png?dl=1" title="Error5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22380013e274399d4ed721afc67de9e610182475_2_503x500.png" alt="Error5" data-base62-sha1="4SIdgY7cvy1NTxEF3dEpPhERTrn" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22380013e274399d4ed721afc67de9e610182475_2_503x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22380013e274399d4ed721afc67de9e610182475_2_754x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22380013e274399d4ed721afc67de9e610182475_2_1006x1000.png 2x" data-dominant-color="C6C3C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error5</span><span class="informations">1085×1078 86.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Lowey (2018-07-11 02:04 UTC)

<p>Hi Andras,</p>
<p>OK I have fixed my problem, although I have no idea why it was an issue. For some reason Slicer wasn’t reading the SlicerRT extension’s qt-loadable-modules in the ‘Additional module path’</p>
<p>So, I copied those files and placed them in the ‘Slicer/lib/Slicer-4.8/qt-loadable-modules’ path</p>
<p>And now it seems to work fine</p>
<p>Thank you, as always!!</p>

---
