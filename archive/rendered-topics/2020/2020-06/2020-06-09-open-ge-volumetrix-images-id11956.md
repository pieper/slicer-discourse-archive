---
topic_id: 11956
title: "Open Ge Volumetrix Images"
date: 2020-06-09
url: https://discourse.slicer.org/t/11956
---

# Open GE Volumetrix images

**Topic ID**: 11956
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/open-ge-volumetrix-images/11956

---

## Post #1 by @Alex_Vergara (2020-06-09 14:34 UTC)

<p>Hello</p>
<p>I have some GE Volumetrix images I need to open. They are basically one dicom file containing multiple volumes inside. In my case one NM study (single dcm file) containing inside (2 NM FOV with AC correction + 2 Mu map + 2 NM FOV without AC correction). The camera is a GE Discovery 670 and exports this way. The files itself can be opened by Hermes workstation which separates each volume correctly. However Slicer opens just the first of the volumes (that can be randomly anyone).</p>
<p>In Hermes they look like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c4498d7644db9d808ea2d7c09a4937007c17087.png" alt="image" data-base62-sha1="aSHfSW8fBF6zU6pnrCzFLFiPwqj" width="634" height="223"></p>
<p>Is this a bug? Is there a way to force the reading of these images?<br>
Cheers</p>

---

## Post #2 by @pieper (2020-06-09 16:02 UTC)

<p>I’m not sure I’d call this a bug in slicer, but this is probably not a kind of data anybody has really worked on before.</p>
<p>Probably the best approach is to use pydicom to access data data and put it into a form that’s compatible with what you want to accomplish.  If you end up wanting to process a lot of similar files you could create a custom DICOMPlugin to handle reading (and optionally writing) of that kind of data and contribute it as an extension along with some sample datasets for testing.</p>

---

## Post #3 by @lassoan (2020-06-09 16:20 UTC)

<p>The volumes may be loaded as multivolume/volume sequence. Could you post a screenshot of the DICOM browser’s advanced section after you clicked “Examine”?</p>

---

## Post #4 by @Alex_Vergara (2020-06-10 18:26 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d234615c5d2b4e52eb5100ff2c1d833c5b5d0987.png" data-download-href="/uploads/short-url/tZyuzuewFkPkKxt6xsZQUkD4wxV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d234615c5d2b4e52eb5100ff2c1d833c5b5d0987_2_690x266.png" alt="image" data-base62-sha1="tZyuzuewFkPkKxt6xsZQUkD4wxV" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d234615c5d2b4e52eb5100ff2c1d833c5b5d0987_2_690x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d234615c5d2b4e52eb5100ff2c1d833c5b5d0987_2_1035x399.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d234615c5d2b4e52eb5100ff2c1d833c5b5d0987_2_1380x532.png 2x" data-dominant-color="F1F4F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2400×928 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83ac7a30782439b2a7be47983567b32070dfe2b9.png" data-download-href="/uploads/short-url/iMQ4VLD0Fgd5ODm4H0XzxBP9y4N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83ac7a30782439b2a7be47983567b32070dfe2b9_2_690x141.png" alt="image" data-base62-sha1="iMQ4VLD0Fgd5ODm4H0XzxBP9y4N" width="690" height="141" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83ac7a30782439b2a7be47983567b32070dfe2b9_2_690x141.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83ac7a30782439b2a7be47983567b32070dfe2b9_2_1035x211.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83ac7a30782439b2a7be47983567b32070dfe2b9_2_1380x282.png 2x" data-dominant-color="D0DEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1770×362 36.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2020-06-10 18:45 UTC)

<p>If you provide a sample data set then we can have a look if there is a simple loading rule that we can add to the DICOM importer.</p>
<p>If it uses private tags or unusual way of storing images then you may need to add a custom importer (just a small Python script that interprets the fields and put the results into MRML nodes) or ask the vendor to provide simpler DICOM export options.</p>

---
