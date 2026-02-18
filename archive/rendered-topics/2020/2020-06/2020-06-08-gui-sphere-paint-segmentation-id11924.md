# GUI sphere paint segmentation

**Topic ID**: 11924
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/gui-sphere-paint-segmentation/11924

---

## Post #1 by @szhang (2020-06-08 11:20 UTC)

<p>It probably has been asked before, but in case I missed any latest development.<br>
If I want to include in my module a GUI component for segmentation (e.g. via sphere paint) as easy as creating a fiducial markup like qSlicerSimpleMarkupsWidget, is it possible?<br>
Thanks a lot in advance!</p>

---

## Post #2 by @lassoan (2020-06-08 14:18 UTC)

<p>There are several very simple options.</p>
<ol>
<li>You can create a model node from markups as shown in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">this example</a> and add it to a segmentation as shown in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_histogram_of_a_segmented_region">other example</a>.</li>
<li>You can find many examples <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">here</a> that shows how to use Segment Editor without showing a widget.</li>
<li>
<a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentEditor/SegmentEditor.py">Segment Editor module</a> is an example of how to embed a segment widget into any scripted module.</li>
</ol>

---
