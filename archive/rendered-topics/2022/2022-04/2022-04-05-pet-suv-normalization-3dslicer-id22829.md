---
topic_id: 22829
title: "Pet Suv Normalization 3Dslicer"
date: 2022-04-05
url: https://discourse.slicer.org/t/22829
---

# PET SUV normalization 3Dslicer

**Topic ID**: 22829
**Date**: 2022-04-05
**URL**: https://discourse.slicer.org/t/pet-suv-normalization-3dslicer/22829

---

## Post #1 by @Hanne1234 (2022-04-05 07:45 UTC)

<p>I want to normalize my PET images to the SUV using 3Dslicer. I installed the <em>PETDICOM</em> extension and followed the steps of this video: <a href="http://qiicr.org/tool/PETDICOM/" class="inline-onebox" rel="noopener nofollow ugc">PETDICOM: PET normalization</a><br>
However, when I try to examine my PET data, there is no PET SUV Plugin outcome.<br>
See the screenshot below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2cf55e42d01fa45e2e5aa8db5f0862e5e371ca3.png" data-download-href="/uploads/short-url/yDZLfEs9Z29SZF0HQWbNUwoTdh9.png?dl=1" title="Screen Shot 2022-04-05 at 10.39.02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2cf55e42d01fa45e2e5aa8db5f0862e5e371ca3_2_690x300.png" alt="Screen Shot 2022-04-05 at 10.39.02" data-base62-sha1="yDZLfEs9Z29SZF0HQWbNUwoTdh9" width="690" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2cf55e42d01fa45e2e5aa8db5f0862e5e371ca3_2_690x300.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2cf55e42d01fa45e2e5aa8db5f0862e5e371ca3_2_1035x450.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2cf55e42d01fa45e2e5aa8db5f0862e5e371ca3_2_1380x600.png 2x" data-dominant-color="EEEEEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-04-05 at 10.39.02</span><span class="informations">2226×970 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What I am doing wrong?</p>
<p>Thank you in advance!</p>

---

## Post #2 by @pieper (2022-04-05 12:21 UTC)

<p>Not all scanners produce standard dicom files so the plugin may not have the information needed for processing.  Because there aren’t comprehensive open databases of data to test against, the tool was built to work with the data available.  You probably need to look at the source code and compare example data with the data you have (dicom headers) and adapt the code to get the needed parameters.  If you aren’t a programmer you can look to share a phantom scan and perhaps someone in the community can help you investigate.</p>

---
