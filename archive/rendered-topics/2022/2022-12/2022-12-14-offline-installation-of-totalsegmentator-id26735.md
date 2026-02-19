---
topic_id: 26735
title: "Offline Installation Of Totalsegmentator"
date: 2022-12-14
url: https://discourse.slicer.org/t/26735
---

# Offline installation of TotalSegmentator

**Topic ID**: 26735
**Date**: 2022-12-14
**URL**: https://discourse.slicer.org/t/offline-installation-of-totalsegmentator/26735

---

## Post #1 by @Augusto (2022-12-14 17:33 UTC)

<p>Hello,</p>
<p>I have a computer with 3D Slicer, but has no internet connection, therefore to install extensions i have to download them from another computer and passed the folder to the one having 3D Slicer installed.<br>
I saw TotalSegmentator was not yet available in the extensions catalog (<a href="https://extensions.slicer.org/catalog/All/30822/win" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a>).<br>
Is there a way to download it ?</p>
<p>Thanks</p>

---

## Post #2 by @rbumm (2022-12-14 18:56 UTC)

<p>This is difficult because TotalSegmentator (the nnU-Net segmentation tool by Jakob Wasserthal and coworkers) gets pip-installed into Slicer´s Python directory during the first run via the extension.<br>
What probably works (not tested) Is to completely install 3D Slicer stable version as well as the TotalSegmentator extension as well as PyTorch on your computer with Internet, and finally run TotalSegmentator and check the results. Then move the complete Slicer directory to your other computer without the Internet.  Please bear in mind that the size of the directory will be several GB.</p>

---

## Post #3 by @lassoan (2022-12-14 19:25 UTC)

<p>You can get the correct link for the extension catalog from the Extensions Manager:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40b64a8caab91f4e9b23bc4ebcdb152012fa0121.png" data-download-href="/uploads/short-url/9et78ULILIJEueWYGAQBaVvOf2F.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40b64a8caab91f4e9b23bc4ebcdb152012fa0121_2_690x118.png" alt="image" data-base62-sha1="9et78ULILIJEueWYGAQBaVvOf2F" width="690" height="118" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40b64a8caab91f4e9b23bc4ebcdb152012fa0121_2_690x118.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40b64a8caab91f4e9b23bc4ebcdb152012fa0121_2_1035x177.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40b64a8caab91f4e9b23bc4ebcdb152012fa0121_2_1380x236.png 2x" data-dominant-color="424547"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2186×376 57.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For Slicer-5.2.1 it is: <a href="https://extensions.slicer.org/catalog/All/31317/win">https://extensions.slicer.org/catalog/All/31317/win</a></p>
<p>However, as <a class="mention" href="/u/rbumm">@rbumm</a> explained above, TotalSegmentator downloads additional Python packages and models. All Slicer installation trees are fully portable, so if you can copy the <code>%localappdata%/NA-MIC/Slicer 5.2.1</code> folder to the offline computer that will contain all Slicer extension and Python packages. In addition to that you also need to copy the downloaded model weights cached in <code>%userprofile%\.totalsegmentator</code></p>

---

## Post #4 by @Augusto (2022-12-14 19:47 UTC)

<p>Ok, thank you for the help!</p>

---

## Post #5 by @Augusto (2022-12-14 19:48 UTC)

<p>I will try and do that</p>
<p>Thank you!</p>

---
