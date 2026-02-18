# Segmentation MRML node function names/arguments changed

**Topic ID**: 8776
**Date**: 2019-10-14
**URL**: https://discourse.slicer.org/t/segmentation-mrml-node-function-names-arguments-changed/8776

---

## Post #1 by @ungi (2019-10-14 18:42 UTC)

<p>This example doesn’t work anymore:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_representation_of_a_segment" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_representation_of_a_segment</a></p>
<p>What is the recommended new way to get the segmentation labelmaps?<br>
Just change GetBinaryLabelmapRepresentation to GetBinaryLabelmapInternalRepresentation?</p>

---

## Post #2 by @lassoan (2019-10-14 18:58 UTC)

<p>Probably you want to use <code>GetBinaryLabelmapRepresentation</code>, which returns a binary labelmap that only has non-zero voxels in the requested segment’s region.</p>
<p><code>GetBinaryLabelmapInternalRepresentation</code> is for advanced use cases (mainly for internal use by editor effects). It returns the internal labelmap that is potentially shared by multiple segments (so that you need to threshold it with the segment’s label value to get the segment’s binary labelmap).</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> will write a forum post about the new features of Editor that made this API change necessary, and update the migration guide with instructions.</p>

---

## Post #3 by @ungi (2019-10-14 20:12 UTC)

<p>What I am doing is clear the segmentation canvas. (Getting the labelmap, setting all pixels to zero, then setting it back in the segmentation node.)<br>
If the new API will include a function to clear the segmentation, then I will use that.<br>
Of course, the example script will need to be fixed regardless.</p>

---

## Post #4 by @lassoan (2019-10-14 22:07 UTC)

<p>The simplest way to clear a segment is to call <a href="https://apidocs.slicer.org/master/classvtkSegmentation.html#a73a66c23a2f2df7b465d5cd80b71373a" rel="nofollow noopener">vtkSegmentation::ClearSegment</a>.</p>

---
