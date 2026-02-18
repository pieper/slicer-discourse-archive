# Images went wrong after RT export

**Topic ID**: 3054
**Date**: 2018-06-03
**URL**: https://discourse.slicer.org/t/images-went-wrong-after-rt-export/3054

---

## Post #1 by @mpsdw (2018-06-03 09:21 UTC)

<p>Operating system:windows<br>
Slicer version:4.3.1</p>
<p>Dear all：<br>
I have constructed  some  segments in T1+contrast images，and PET images were selected as master volume when I exported this structure in RT-export, but after that, PET images become terrible！！I dont know what’s going wrong，Does any body can help me？</p>
<p>Thanks<br>
Chentao<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb6df2aa39c9565de26b49e3bb811d4c40948abc.jpeg" data-download-href="/uploads/short-url/xAHLBG0vUJrZEfu2WblDmpmwg0Y.jpg?dl=1" title="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180603150450" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb6df2aa39c9565de26b49e3bb811d4c40948abc_2_690x497.jpg" alt="%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180603150450" data-base62-sha1="xAHLBG0vUJrZEfu2WblDmpmwg0Y" width="690" height="497" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb6df2aa39c9565de26b49e3bb811d4c40948abc_2_690x497.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb6df2aa39c9565de26b49e3bb811d4c40948abc_2_1035x745.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb6df2aa39c9565de26b49e3bb811d4c40948abc.jpeg 2x" data-dominant-color="83848E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20180603150450</span><span class="informations">1208×871 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-06-03 11:31 UTC)

<p>Please try with latest stable version of Slicer. If you still have issues, then post a screenshot that shows the PET image when it still looks good.</p>

---

## Post #3 by @mpsdw (2018-06-03 12:43 UTC)

<p>Thanks for your reply，but does the SlicerRT extension still works on slicer 4.8.1？ Because it seems some features like [DICOM-RT export] cannot be found in the [All Modules] list. So I don’t know how to conduct the same operation in the latest stable version. Can you teach me how to do or where I can get a manual about this？ Thank you</p>

---

## Post #4 by @lassoan (2018-06-03 21:22 UTC)

<p>Yes, SlicerRT works well on both latest stable (4.8.1) and latest nightly (4.9.x) versions. See DICOM module documentation about how to export data: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a></p>

---

## Post #5 by @mpsdw (2018-06-04 09:03 UTC)

<p>Hello，doctor lassoan，sorry to disturb again，I have tried many times according to the DICOM module documentation, conducting segamentation on MR images, making model, and draging the model to the structure of PET，then exporting the study，now PET images can be exported correctly，but why the 【rtss.dcm】 file does not appear. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc377773aa8d22fb5365edb96a3da76b9fad9772.jpeg" data-download-href="/uploads/short-url/zZd9S1cfauzMCuwF97b7a62yPm2.jpg?dl=1" title="export%20to%20dicom" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc377773aa8d22fb5365edb96a3da76b9fad9772_2_690x146.jpg" alt="export%20to%20dicom" data-base62-sha1="zZd9S1cfauzMCuwF97b7a62yPm2" width="690" height="146" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc377773aa8d22fb5365edb96a3da76b9fad9772_2_690x146.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc377773aa8d22fb5365edb96a3da76b9fad9772.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc377773aa8d22fb5365edb96a3da76b9fad9772.jpeg 2x" data-dominant-color="FBF3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">export%20to%20dicom</span><span class="informations">744×158 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2018-06-04 11:28 UTC)

<p>Structure set (RTSS) can be exported only from segmentation node. If you have your data in a model node then you need to import that into a segmentation node (using Segmentations module).</p>

---

## Post #7 by @mpsdw (2018-06-04 11:53 UTC)

<p>Yeah !! It really works ! The problem has been solved finally , and images looked great !  Really thanks for your help !</p>

---
