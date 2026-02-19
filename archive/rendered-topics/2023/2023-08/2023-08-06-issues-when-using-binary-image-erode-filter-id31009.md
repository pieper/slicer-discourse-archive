---
topic_id: 31009
title: "Issues When Using Binary Image Erode Filter"
date: 2023-08-06
url: https://discourse.slicer.org/t/31009
---

# Issues when using Binary Image Erode Filter

**Topic ID**: 31009
**Date**: 2023-08-06
**URL**: https://discourse.slicer.org/t/issues-when-using-binary-image-erode-filter/31009

---

## Post #1 by @Annabel_W (2023-08-06 10:58 UTC)

<p>Hi There,</p>
<p>I am working on a project that will allow me to automate the localization of intracranial electrodes using Pre and Post Surgical CTs and a Pre Surgical MRI on 3D Slicer.</p>
<p>I am Currently trying to remove the outer inch of the patients head to remove the skull allow the end of the electrodes to be exposed using the binary erode image filter.</p>
<p>I have attempted using three filters, ‘BinaryErodeImageFilter’, ‘ErodeObjectMorphologyImageFilter’ and BinaryMorpologicalOpeningImageFilter’.</p>
<p>These seemed to have no effect on my CT scans or Binarized Label-Maps.</p>
<p>Please could you let me know how I can complete this task.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f44dc1a801254e59dd0f24c568896cf30744399.png" data-download-href="/uploads/short-url/mIXrQIwE91l1s8ykKb3N3glE94J.png?dl=1" title="Screenshot 2023-08-06 103715" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f44dc1a801254e59dd0f24c568896cf30744399_2_690x324.png" alt="Screenshot 2023-08-06 103715" data-base62-sha1="mIXrQIwE91l1s8ykKb3N3glE94J" width="690" height="324" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f44dc1a801254e59dd0f24c568896cf30744399_2_690x324.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f44dc1a801254e59dd0f24c568896cf30744399_2_1035x486.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f44dc1a801254e59dd0f24c568896cf30744399.png 2x" data-dominant-color="4E4E54"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-06 103715</span><span class="informations">1345×633 209 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Kind Regards<br>
Annabel</p>

---

## Post #2 by @pieper (2023-08-06 18:23 UTC)

<p>You can convert the labelmaps to segmentations (use the right click menu in the Data module) and then in the Segment Editor you can use the Margin effect.</p>

---
