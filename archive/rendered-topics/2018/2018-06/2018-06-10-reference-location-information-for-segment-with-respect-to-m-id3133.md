---
topic_id: 3133
title: "Reference Location Information For Segment With Respect To M"
date: 2018-06-10
url: https://discourse.slicer.org/t/3133
---

# Reference location information for segment with respect to master volume

**Topic ID**: 3133
**Date**: 2018-06-10
**URL**: https://discourse.slicer.org/t/reference-location-information-for-segment-with-respect-to-master-volume/3133

---

## Post #1 by @MRXCAT_CMR (2018-06-10 11:29 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.8.1 (r26813) built myself</p>
<p>I am currently working on some extension submodule to Segment Editor doing automatic segmentation of some organs. This involves handling multiple segments mostly working with numpy arrays. This is currently done as follows inside a SegmentEditor effect method:</p>
<pre><code># get master volume array
volumeNode = slicer.util.getNode('CT image')
npImage = slicer.util.arrayFromVolume(volumeNode)

# get mask array
segNode = slicer.util.getNode('Segmentation') # Get the segmentation node    
npMask = slicer.util.arrayFromSegment( segNode, 'Airways')
</code></pre>
<p>My question: The npMask array is smaller than the npImage array. Where can I get information about how they relate spatially?<br>
Or more precisely: where in npImage is the lower left corner of npMask located?</p>

---

## Post #2 by @lassoan (2018-06-10 14:02 UTC)

<p>Origin, spacing, axis directions, and extents of binary labelmap representation for each segment is stored in the vtkOrientedImage data object in the corresponding vtkSegment object. You can use <code>GetBinaryLabelmapRepresentation</code> convenience method in segmentation node to get this image directly, as it is done in the <a href="https://github.com/Slicer/Slicer/blob/f051e24c803ae0a067e04ea2b2a9a178040d7415/Base/Python/slicer/util.py#L829-L844"><code>slicer.util.arrayFromSegment</code></a> method.</p>
<p>Segment editor takes care of getting the master volume and resample to the segment’s geometry (so you don’t need to worry about matching voxels of the master volume and your segment; origin, spacing, and axis directions will be the same; only their extent may be different), updating voxels in of all segments by respecting masking settings, etc. Therefore, instead of trying to implement an effect from scratch, I would recommend to find the effect that is most similar to what you would like to do and modify/extend that. Most segment editor effects are implemented in Python, so there are plenty of examples. Source code:</p>
<ul>
<li>
<a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Segmentations/EditorEffects/Python">https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Segmentations/EditorEffects/Python</a> (source code of all built-in effects that are implemented in Python)</li>
<li>
<a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects">https://github.com/lassoan/SlicerSegmentEditorExtraEffects</a> (this also shows how to define additional custom effects in an extension that show up in the Segment Editor)</li>
</ul>

---
