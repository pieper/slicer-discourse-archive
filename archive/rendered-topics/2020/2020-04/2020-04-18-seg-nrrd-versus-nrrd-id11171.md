---
topic_id: 11171
title: "Seg Nrrd Versus Nrrd"
date: 2020-04-18
url: https://discourse.slicer.org/t/11171
---

# .seg.nrrd versus .nrrd

**Topic ID**: 11171
**Date**: 2020-04-18
**URL**: https://discourse.slicer.org/t/seg-nrrd-versus-nrrd/11171

---

## Post #1 by @codecrazer (2020-04-18 02:33 UTC)

<p>What is the difference between file ended with .nrrd versus .seg.nrrd<br>
I found when I load the .seg.nrrd file into 3D slicer, it was recognized as segmentation; but in the case of .nrrd file, i need to choose by myself.<br>
Are the information stored in both format the same, only adding segmentation attribute in the .seg.nrrd file? Thanks for your help!</p>

---

## Post #2 by @lassoan (2020-04-18 02:39 UTC)

<p>When a segmentation is saved into .nrrd image format, a couple of <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details">additional metadata fields are saved</a> (segment names, colors, terminology, etc.). We still keep the .nrrd file extension so that any nrrd-compatible software can recognize it.</p>
<p>The composite .seg.nrrd file extension just gives a hint for Slicer to load the file as “Segmentation”. If you save the segmentation as .nrrd then it is loaded as “Volume” by default and you need to manually select Description-&gt;Segmentation in “Add data” dialog to load it as “Segmentation”.</p>

---

## Post #4 by @codecrazer (2020-04-18 14:41 UTC)

<p>Are the segmentation area in both file the same? Thanks for your help!</p>

---

## Post #5 by @lassoan (2020-04-18 14:44 UTC)

<p>In Slicer-4.10, segmentations were always saved as 4D volumes and automatically cropped to the minimum necessary extent. In Slicer-4.11 segmentation is saved the same way as an exported 3D labelmap (only 3D volume if no overlap between segments, not cropped to minimum size).</p>

---

## Post #6 by @codecrazer (2020-04-18 15:09 UTC)

<p>Thanks for your reply!!! According what you reply, can I state that in slicer 4.10, no matter I store the segmentation in need or seg.nrrd, the segmentation area will be the same area in both format.? Does this result also apply to slicer 4.11?  I am really grateful for your answer, thanks a lot???</p>

---

## Post #7 by @lassoan (2020-04-18 15:27 UTC)

<p>If you save the segmentation directly (not by exporting to labelmap node and saving the labelmap) then it does not matter if you choose .seg.nrrd or just .nrrd file extension. Dimensionality and extent depends on Slicer version (Slicer-4.10 is 4D data with reduced extent; Slicer-4.11 is usually 3D and by default not reduced extent).</p>

---

## Post #8 by @codecrazer (2020-04-19 13:32 UTC)

<p>Just for confirmation, sorry for keep asking question.<br>
Does save the segmentation directly means this screen?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/023a556eddfaf8c05a9658b88ab85909f62945ab.png" data-download-href="/uploads/short-url/jHVVHyHNOxrCExuAOJfqeYZYDN.png?dl=1" title="seg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/023a556eddfaf8c05a9658b88ab85909f62945ab_2_690x361.png" alt="seg" data-base62-sha1="jHVVHyHNOxrCExuAOJfqeYZYDN" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/023a556eddfaf8c05a9658b88ab85909f62945ab_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/023a556eddfaf8c05a9658b88ab85909f62945ab.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/023a556eddfaf8c05a9658b88ab85909f62945ab.png 2x" data-dominant-color="DBDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">seg</span><span class="informations">864×453 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Do these two file format, .nrrd or seg.nrrd. , both contains the same segmentation area?</p>
<p>Really thanks for your help!!!</p>

---

## Post #9 by @lassoan (2020-04-19 14:39 UTC)

<p>Your file extension choice in this save data window only affects the segmentation file’s extension. The content is exactly the same.</p>

---

## Post #10 by @yongfenggu985 (2024-10-26 14:35 UTC)

<p>So how to convert .seg.nrrd exported by slicer 4.10 to nrrd and restore the original size</p>

---

## Post #11 by @lassoan (2024-10-27 16:53 UTC)

<p>You can click the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options">Specify Geometry button</a> in Segment Editor and then select a volume that you want to match the geometry of.</p>

---
