#  questions about the use of radiomics module

**Topic ID**: 7916
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/questions-about-the-use-of-radiomics-module/7916

---

## Post #1 by @zhangyf2 (2019-08-07 13:24 UTC)

<p>Hello, I am a researcher from China and have some questions about the use of radiomics module.</p>
<p>I want to implement RADIOMICS analysis on enhanced ultrasound images.</p>
<p>I have exported the.dcm file and split the ROI, and the data list is shown in the figure below.</p>
<p>But in radiomics module, input cannot be clicked and segmentation cannot be selected.</p>
<p>What should I do?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed430652a1afb99ccc27b26ff6bef3591e00079c.jpeg" data-download-href="/uploads/short-url/xQUL8oX5XpdheDI49Bs7uFspEFS.jpeg?dl=1" title="question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed430652a1afb99ccc27b26ff6bef3591e00079c_2_303x500.jpeg" alt="question" data-base62-sha1="xQUL8oX5XpdheDI49Bs7uFspEFS" width="303" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed430652a1afb99ccc27b26ff6bef3591e00079c_2_303x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed430652a1afb99ccc27b26ff6bef3591e00079c_2_454x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/ed430652a1afb99ccc27b26ff6bef3591e00079c_2_606x1000.jpeg 2x" data-dominant-color="BEC8C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question</span><span class="informations">800×1316 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
P.S.  I don’t understand why the color of the loaded image is very strange.</p>

---

## Post #2 by @pieper (2019-08-07 13:40 UTC)

<p>The ultrasound may be a secondary capture dicom, so loaded as a vector (color) volume.  You can check this in the Volumes module.  If so, you can use the Vector to Scalar Volume module to convert and then it should be selectable for radiomics.</p>

---

## Post #3 by @zhangyf2 (2019-08-17 15:10 UTC)

<p>Thank you for solving my problem! This BBS is awesome</p>

---
