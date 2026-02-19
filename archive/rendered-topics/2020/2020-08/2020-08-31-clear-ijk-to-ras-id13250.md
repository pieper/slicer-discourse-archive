---
topic_id: 13250
title: "Clear Ijk To Ras"
date: 2020-08-31
url: https://discourse.slicer.org/t/13250
---

# Clear IJK to RAS

**Topic ID**: 13250
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/clear-ijk-to-ras/13250

---

## Post #1 by @joachim (2020-08-31 14:50 UTC)

<p>My DICOM image serie has a built in transformation, which can be seen in <em>Volume Information</em>:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9b480cada6e577850602a6e79cd1b2f388bbe5b.png" alt="Capture" data-base62-sha1="zCZCcPe8Nig8wyuOaCOmdjtMDPR" width="614" height="132"></p>
<p>(Or using ImageMagick: <code>magick identify -verbose file.dcm</code> shows a tag <code>dcm:ImageOrientation(Patient)</code> with this orientation).</p>
<p>How can I clear this orientation in the Slicer application? Because my segmentation becomes bad when the orientation of the image volume and the segmentation volume does not match. I don’t care about the orientation of the image volume. And I don’t care about the orientation in the DICOM files. I only want a plain segmentation using the pixels in the image volume.</p>

---

## Post #2 by @lassoan (2020-08-31 16:18 UTC)

<p>You should not ignore image orientation for many reasons. If you want to segment on slices that are parallel to image axes then click the oblique slice warning icon in the Segment Editor (next to the segmentation node selector). If the warning button is clicked, each slice view is automatically aligned to the closest segment axis.</p>
<p>                    <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/MisalignmentWarningButton.png" target="_blank" rel="nofollow ugc noopener" class="onebox">
            <img src="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/MisalignmentWarningButton.png" width="690" height="143">
          </a>

</p>

---

## Post #3 by @joachim (2020-09-01 13:47 UTC)

<p>OK, and if I press the button below, I see that the segmentation labelmap volume has the same orientation, so it should be aligned with the voxels of the image volume.</p>
<p>But if I click the slice warning icon, the hotlink between my two Views does not work anymore. Is that a bug or correct behaviour? (If I remember correctly, hotlink is implemented in <a href="https://github.com/Slicer/Slicer/blob/43300c7b9a3b27265c2bc736693cb881f05e3ea9/Libs/MRML/Logic/vtkMRMLSliceLinkLogic.cxx" rel="noopener nofollow ugc">vtkMRMLSliceLinkLogic.cxx</a>).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43893e7173a6aa656d4577519e29e58921518757.png" data-download-href="/uploads/short-url/9Ds27H26flCmvIjHInE401YiIn5.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43893e7173a6aa656d4577519e29e58921518757.png" alt="Capture" data-base62-sha1="9Ds27H26flCmvIjHInE401YiIn5" width="591" height="500" data-dominant-color="E9EDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">615×520 29.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> .</p>

---

## Post #4 by @lassoan (2020-09-01 22:53 UTC)

<p>Linking synchronizes views that have the same orientation. You can manually rotate any view to a volume axis by clicking the corresponding button in the slice view control widget.</p>

---

## Post #5 by @joachim (2020-09-11 20:36 UTC)

<p>If I remember correctly, clicking the slice warning icon only affects Views having a segmentation overlay. I created <a href="https://github.com/karamellpelle/SlicerRC/blob/998d8e881524aa1a302378be458e2e13cd2aa5f0/slicerrc.py" rel="nofollow noopener">my own layouts</a> to do manual segmentations easier. Here I synchronize (i.e. hotlinks) two Views so that one shows segmentation overlays and the other not (this makes it easier to see structures). Reformatting only one View probably breaks the hotlink. I suppose I can copy the reformatted orientation to the other View next time.</p>

---

## Post #6 by @lassoan (2020-09-11 20:51 UTC)

<p>You can also add one more display node to your segmentation (using Python scripting), which associates the segmentation with additional views, but makes the segments almost completely transparent, so that you can very clearly see your structures.</p>
<p>To make background images easier to see, you can also make segment outlines thinner and filling more transparent; and adjust window/level of the background image.</p>

---
