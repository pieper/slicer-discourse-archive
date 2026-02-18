# How to change segmentID of existing segmentations

**Topic ID**: 11254
**Date**: 2020-04-22
**URL**: https://discourse.slicer.org/t/how-to-change-segmentid-of-existing-segmentations/11254

---

## Post #1 by @Vincent_C (2020-04-22 19:07 UTC)

<p>Hi all,</p>
<p>How can I change the segmentIDs/tags of existing segmentations? Currently, saving a colour table results in these default values (in bold) but I would like to set my own tags for the existing segmentations that I have.</p>
<p><strong>0</strong> Background 0 0 0 0<br>
<strong>1</strong> Muscle 255 0 0 255<br>
<strong>2</strong> SAT 0 255 255 255<br>
<strong>3</strong> VAT 255 255 0 255<br>
<strong>4</strong> Bone 0 0 255 255</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-04-22 20:31 UTC)

<p>What do you mean by tag? Labelmap voxel value? Segment name? In user interface or using Python scripting?</p>
<p>Note that a segmentation can contain overlapping segments and multiple segments can use the same label value (e.g., if you imported them from multiple labelmaps). The overly simplistic approach that many other software does (that can only represent a segmentation as a 3D labelmap volume) may not be directly transferable but we should be able to achieve what you need.</p>
<p>Can you describe your overall goal? What is the clinical problem you are trying to solve and what is your current plan to achieve that?</p>

---

## Post #3 by @Vincent_C (2020-04-22 21:10 UTC)

<p>Hi Andras,</p>
<p>Sorry - yes, i meant Labelmap voxel value.</p>
<p>My overall goal is to segment muscle, fat and bone in whole-body CT scans. My lab has already pre-defined the Labelmap voxel values for each segment component to keep things consistent. I would like to change the current Labelmap voxel values to the ones set by my lab both for existing segmentations and for future segmentations.</p>
<p>It would be great to know how to change that in both the UI and through Python scripting.</p>
<p>Thanks</p>

---

## Post #4 by @Vincent_C (2020-04-24 06:14 UTC)

<p>Please let me know if there is a solution to achieve this!</p>
<p>Thanks</p>

---

## Post #5 by @lassoan (2020-04-24 13:27 UTC)

<p>If you start from an empty <a href="https://discourse.slicer.org/t/segment-editor-color-name-template/10982/5">segmentation template</a> then you can set the label values once and those are preserved (if you don’t delete the segment or copy the segment into another segmentation that already uses that label value).</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Do we a helper function in segmentation MRML or logic classes to change associated label value in a segment? (if we keep getting these requests then we may need to expose label and layer value assignment on the GUI and add a flag to allow locking of label&amp;layer for a segment).</p>

---

## Post #6 by @Sunderlandkyl (2020-04-24 13:39 UTC)

<p>There aren’t any helper functions for changing label values or layers currently.</p>

---

## Post #7 by @lassoan (2020-04-24 14:27 UTC)

<p>I’ve added a features request for allowing customization of label values: <a href="https://github.com/Slicer/Slicer/issues/4886">https://github.com/Slicer/Slicer/issues/4886</a>. Probably we’ll get to it within a few months.</p>
<p>Until then you can use the template approach and/or export segmentation to a labelmap volume node and change label values as needed like this:</p>
<pre><code class="lang-python">labelmapVolumeName = 'Segmentation-label'
originalLabelValue = 1
newLabelValue = 5

labelmapVolumeNode = slicer.uitil.getNode(labelmapVolumeName)
labelmapArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
labelmapArray[ labelmapArray==originalLabelValue ] = newLabelValue
labelmapArray = slicer.util.arrayFromVolumeModified(labelmapVolumeNode)
</code></pre>

---
