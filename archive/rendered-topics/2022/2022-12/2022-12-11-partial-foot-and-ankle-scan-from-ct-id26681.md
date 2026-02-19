---
topic_id: 26681
title: "Partial Foot And Ankle Scan From Ct"
date: 2022-12-11
url: https://discourse.slicer.org/t/26681
---

# Partial Foot and Ankle scan from CT

**Topic ID**: 26681
**Date**: 2022-12-11
**URL**: https://discourse.slicer.org/t/partial-foot-and-ankle-scan-from-ct/26681

---

## Post #1 by @cepehde (2022-12-11 06:57 UTC)

<p>Operating system:  Windows 10 Pro<br>
Slicer version: 5.0.3<br>
Expected behavior:  Full View of Foot and Ankle<br>
Actual behavior:  Small Partial view of Foot and Ankle</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01fc25a42fc85bff504fe8c73207156c229f280a.jpeg" data-download-href="/uploads/short-url/hyHoOJsSbMWfPms7fnZc6Hfx2i.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01fc25a42fc85bff504fe8c73207156c229f280a_2_690x388.jpeg" alt="image" data-base62-sha1="hyHoOJsSbMWfPms7fnZc6Hfx2i" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01fc25a42fc85bff504fe8c73207156c229f280a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01fc25a42fc85bff504fe8c73207156c229f280a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01fc25a42fc85bff504fe8c73207156c229f280a_2_1380x776.jpeg 2x" data-dominant-color="7E7E85"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1082 83.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86e25518c4639a7a44d18ce29757dfef2304a19f.jpeg" data-download-href="/uploads/short-url/jfeTybBkI3wTupnWWOXbatxfbD9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86e25518c4639a7a44d18ce29757dfef2304a19f_2_690x316.jpeg" alt="image" data-base62-sha1="jfeTybBkI3wTupnWWOXbatxfbD9" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86e25518c4639a7a44d18ce29757dfef2304a19f_2_690x316.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86e25518c4639a7a44d18ce29757dfef2304a19f_2_1035x474.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86e25518c4639a7a44d18ce29757dfef2304a19f_2_1380x632.jpeg 2x" data-dominant-color="F1F4F6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1685×774 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have a Foot and Ankle CT scan that only loads a small, partial portion.  I though it was because my disc had compressed DICOM files.   I obtained a copy of uncompressed DICOM files but with the same result.</p>
<p>I have received multiple scans from the radiology department at my hospital without issues.</p>
<p>I am hoping I have messed up a setting in this particular case, but I cannot figure out what or why this scan is this way.</p>
<p>Collin</p>

---

## Post #2 by @pieper (2022-12-11 14:43 UTC)

<p>Try the suggestions here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---

## Post #3 by @lassoan (2022-12-12 18:11 UTC)

<p>It seems that only a few dozens files are imported. Make sure you drag-and-drop the entire folder that may contain DICOM files into the Slicer application window and wait for the DICOM import step to complete.</p>

---

## Post #4 by @cepehde (2022-12-13 04:36 UTC)

<p>Thank you for the information. I was able to use the DICOM Patcher Module and it worked and fixed the issue.</p>
<p>Thanks again for the advice.</p>
<p>Collin</p>

---
