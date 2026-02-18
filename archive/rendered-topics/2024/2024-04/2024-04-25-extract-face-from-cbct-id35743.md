# Extract face from CBCT

**Topic ID**: 35743
**Date**: 2024-04-25
**URL**: https://discourse.slicer.org/t/extract-face-from-cbct/35743

---

## Post #1 by @qaz8788817 (2024-04-25 08:42 UTC)

<p>Hi, <a class="mention" href="/u/slicer360">@Slicer360</a> . I want to extract face using 3D slicer. I am a beginner. Can you advise me how to extract the face like yours (Figure 3)?<br>
Here is my side face.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6af024767fd5e1377eaf96d4b419b37977faf5e0.png" alt="image" data-base62-sha1="fg176K9Pqnt6DoHkFIV4D0O8IDu" width="334" height="391"></p>
<p>Thank you.</p>

---

## Post #2 by @qaz8788817 (2024-04-29 03:08 UTC)

<p>Hi, there. I try to segment skin surface of CT image, like this:<br>
Figure 1. An example of facial mesh<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcd3bb8e8f56c6172b08854e0f6853089eadb8cd.png" alt="image" data-base62-sha1="vvwG4wy10J6q3nLr8SYnGpCNS9f" width="318" height="397"><br>
Figure 2. Side face<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1eb27400fac426e596a07cd2ce686722b179e55f.png" alt="image" data-base62-sha1="4nyEO85jYTTJDaMuaPTCbcwpL0H" width="316" height="418"><br>
and here is my segment:<br>
Figure 3. My current segment<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e350cd6e73a844e20400a247beb757fae9fcebb6.jpeg" data-download-href="/uploads/short-url/wqVvgrCCKaLWP9nJZf87bPXtqzI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e350cd6e73a844e20400a247beb757fae9fcebb6_2_319x500.jpeg" alt="image" data-base62-sha1="wqVvgrCCKaLWP9nJZf87bPXtqzI" width="319" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e350cd6e73a844e20400a247beb757fae9fcebb6_2_319x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e350cd6e73a844e20400a247beb757fae9fcebb6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e350cd6e73a844e20400a247beb757fae9fcebb6.jpeg 2x" data-dominant-color="A69B99"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">400×626 79.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there any quick and simple way to generate a smooth face model?</p>
<p>Thanks.</p>

---

## Post #3 by @Mohamed_Hamdy (2024-05-12 09:55 UTC)

<p>Can you please let me know to segment the facial skin, if there are any automated tools for that?</p>

---

## Post #4 by @lassoan (2024-05-12 11:20 UTC)

<p>You can export the segmentation to a model, use Markups module to draw a closed curve around the face, and then remove everything outside the curve using Dynamic Modeler module.</p>

---
