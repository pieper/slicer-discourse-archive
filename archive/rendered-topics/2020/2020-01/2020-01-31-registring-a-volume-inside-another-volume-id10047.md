---
topic_id: 10047
title: "Registring A Volume Inside Another Volume"
date: 2020-01-31
url: https://discourse.slicer.org/t/10047
---

# Registring a volume inside another volume

**Topic ID**: 10047
**Date**: 2020-01-31
**URL**: https://discourse.slicer.org/t/registring-a-volume-inside-another-volume/10047

---

## Post #1 by @muntahi398 (2020-01-31 11:27 UTC)

<p>Dear All,<br>
I am trying to  register a volume inside another bigger volume, where I know that it should have only translation in  Y axis and rotation  only to match.<br>
Here is the screeenshot…<br>
<a href="/uploads/short-url/wNFLDfis8B4ILB3srp50J3YPtIQ.jpeg">register_volume.PNG|690x397</a></p>
<p>Volumes  I am trying to register is uploaded here. (I had to rescal original data to look similar as an image)</p>
<p><a href="https://drive.google.com/open?id=1iGdQmh-ZAt5W_PE6gtle6kspG-S2iNfb" class="inline-onebox" rel="noopener nofollow ugc">registration - Google Drive</a>!</p>
<p>What would be the easy and best way to register this volume ?</p>

---

## Post #2 by @timeanddoctor (2020-01-31 12:03 UTC)

<p>Are there markers in this volumes? If yes, you can perform the fiducial registration to repostion them</p>
<ol>
<li>creat two point lists use the markups(F-1;F-2), each list contain at lest 3 points</li>
<li>swith to the fiducial registration module and apply the transform matrix</li>
</ol>
<p>.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdd81cd248782b0dbe80994a4ce47163f1c3791e.png" data-download-href="/uploads/short-url/AdBOMC9uqxXF7Wg93dLB2WcqOjc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdd81cd248782b0dbe80994a4ce47163f1c3791e_2_611x500.png" alt="image" data-base62-sha1="AdBOMC9uqxXF7Wg93dLB2WcqOjc" width="611" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdd81cd248782b0dbe80994a4ce47163f1c3791e_2_611x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fdd81cd248782b0dbe80994a4ce47163f1c3791e_2_916x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdd81cd248782b0dbe80994a4ce47163f1c3791e.png 2x" data-dominant-color="CDC8BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1029×841 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
