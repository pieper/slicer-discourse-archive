# Anatomy of Aorta and Pulmonary arteries

**Topic ID**: 40564
**Date**: 2024-12-08
**URL**: https://discourse.slicer.org/t/anatomy-of-aorta-and-pulmonary-arteries/40564

---

## Post #1 by @OmerAfsin (2024-12-08 13:05 UTC)

<p>Hello everyone.<br>
I’m new here and this is my first post in community. If there is something you find wrong in this post, I can remove it if you contact me.</p>
<p>I am working on a project about the automatic segmentation of great arteries from CT images. I study engineering so that my anatomy background is not very good. I started to use a 3D slicer to segment aort and pulmonary arteries, but anatomy and selecting appropriate segmentation tools are hard for me. Can you suggest sources for these issues?</p>
<p>In addition, I want to ask another thing. I exported the segmentation of a dicom slice in NRRD format as a labelmap and read the NRRD file in Python. When I visualized this, I noticed that it was rotated compared to the segmentation I made in 3D slicer. Is that because of the fact that the Dicom and NRRD file keeps the axis records in different orders?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26a06a7533663cbdd26c4c95263139d295d59b77.png" data-download-href="/uploads/short-url/5vHPF1nEhMZSccgjPardZ4preOH.png?dl=1" title="Ekran görüntüsü 2024-12-05 005552" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26a06a7533663cbdd26c4c95263139d295d59b77_2_690x466.png" alt="Ekran görüntüsü 2024-12-05 005552" data-base62-sha1="5vHPF1nEhMZSccgjPardZ4preOH" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26a06a7533663cbdd26c4c95263139d295d59b77_2_690x466.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26a06a7533663cbdd26c4c95263139d295d59b77.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26a06a7533663cbdd26c4c95263139d295d59b77.png 2x" data-dominant-color="9C9C9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2024-12-05 005552</span><span class="informations">813×550 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-12-08 13:12 UTC)

<p>You can segment message vessels automatically using MONAIAuto3DSeg, TotalSegmentator, LungCTAnalyzer extension.</p>
<p>If a software displays an image incorrectly then you can report the error to its developers. If they don’t respond then you can try to fix the issue yourself or use a different software.</p>

---

## Post #3 by @OmerAfsin (2024-12-08 17:25 UTC)

<p>First of all, thank you for answering. I tried the 3 extensions you mentioned.</p>
<p>MonaIauto3dseg and Totalsegmentator returned very good segmentations than I expected.</p>
<p>The aorta has a understandable anatomy, but <strong>Pulmonary Arteries</strong> is a bit difficult. I couldn’t find a simplified source to define its anatomy. If you have a source about this, can you share it with me?</p>
<p>Before I see your answer, I tried to do it myself and I shared the result I made. With this, I plan to train a 3D U-Net model, and I will give the segmentation of 20 such volumes to the model by matching these slices with the corresponding labelmap, respectively. I really appreciate if you comment.</p>
<p>About Nrrd, I just asked because I was wondered, my goal was not to complain.</p>
<p>Thanks for sharing your time.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/703ab82599315bc94c5cc1a64b51b1fb34c65a1f.png" data-download-href="/uploads/short-url/g0Phv0Jea0tgmng10yTxONrBTfV.png?dl=1" title="segmentation1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/703ab82599315bc94c5cc1a64b51b1fb34c65a1f_2_370x499.png" alt="segmentation1" data-base62-sha1="g0Phv0Jea0tgmng10yTxONrBTfV" width="370" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/703ab82599315bc94c5cc1a64b51b1fb34c65a1f_2_370x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/703ab82599315bc94c5cc1a64b51b1fb34c65a1f_2_555x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/703ab82599315bc94c5cc1a64b51b1fb34c65a1f.png 2x" data-dominant-color="8E97BB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation1</span><span class="informations">570×769 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
