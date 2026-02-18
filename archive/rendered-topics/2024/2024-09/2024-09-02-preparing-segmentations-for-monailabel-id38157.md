# Preparing Segmentations for MonaiLabel

**Topic ID**: 38157
**Date**: 2024-09-02
**URL**: https://discourse.slicer.org/t/preparing-segmentations-for-monailabel/38157

---

## Post #1 by @evaherbst (2024-09-02 14:26 UTC)

<p>Hi all,</p>
<p>I have read several posts about the topic of label values and wanted to double check about the best approach.<br>
We have segmentations of shoulder bones but have not ensured label value consistency, so we need to fix this before using MonaiLabel.</p>
<p>I see one option is to export labels using slicerio and this code from <a class="mention" href="/u/lassoan">@lassoan</a> : <a href="https://discourse.slicer.org/t/how-to-change-the-label-value-of-binary-labelmap-volume/12511/9" class="inline-onebox">How to change the label value of binary labelmap volume? - #9 by lassoan</a></p>
<p>It looks like the other option is to create a color table as <a href="https://discourse.slicer.org/t/segment-ids-when-imported-from-label-map/12502">described here</a></p>
<p>Do I understand correctly that the color table can be used to to assign label values on export (if having an existing scene where I wish to change the label values?) using <a href="https://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#ace576efb43c16ee0478bf077b3324cff" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkSlicerSegmentationsModuleLogic Class Reference</a></p>
<p>And the color table can also be used to load existing segmentations into a scene (by selecting it on import) and it will match the segment name to the segment value specified in the table (so if I load a segmentation with a segment called “right scapula”, the color table will be used to assign the correct ID)?</p>
<p>I assume the color table is preferable to the first option since it can then also be used to make new segmentations and assign the correct segment value?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2024-09-02 15:38 UTC)

<p>To convert between .seg.nrrd files and labelmap images that use hardcoded label values:</p>
<ul>
<li>In Slicer: you can use a color table when importing/exporting segmentations</li>
<li>Outside Slicer: you can use slicerio Python package</li>
</ul>

---

## Post #3 by @evaherbst (2024-09-02 15:56 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for the quick reply.</p>
<p>Is there a difference between using .seg.nrrd or .nrrd for inputs in MonaiLabel? Do they both work?</p>
<p>As far as I can tell seg.nrrd has more info such as colors etc, ie the color table would not need to be loaded again into a new file once I have my updated seg.nrrds with the updated values?</p>
<p>Or will the colormap export for assigning new label values only work with .nrrd and not seg.nrrd?</p>
<p>Thank you,<br>
Eva</p>

---

## Post #4 by @lassoan (2024-09-02 16:06 UTC)

<p>MONAILabel can read both .nrrd and .seg.nrrd files, because .seg.nrrd files are just standard .nrrd files with some extra metadata.</p>
<p>Ideally, AI training frameworks should not rely on hardcoded label values but they would get the label value for each segment based on metadata in the .seg.nrrd file. I don’t think MONAILabel currently does this, so you can pre-process your seg.nrrd files using slicerio before using them in MONAILabel.</p>
<p>When you load a plain .nrrd file then you can use a color table to create a segmentation with correct colors and segment names. I’m working on updating color tables in Slicer to allow setting segment terminology as well (terminology codes are more robust and cleaner way to specify segment content than some arbitrary chosen names).</p>

---
