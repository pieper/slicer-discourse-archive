---
topic_id: 4055
title: "Finding Corresponding Segments In Segmentations"
date: 2018-09-10
url: https://discourse.slicer.org/t/4055
---

# Finding corresponding segments in segmentations

**Topic ID**: 4055
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/finding-corresponding-segments-in-segmentations/4055

---

## Post #1 by @phcerdan (2018-09-10 20:23 UTC)

<p>Hi, I haven’t found a way to change the <code>segmentId</code> on a <code>SegmentationNode</code>.<br>
I can change the name of a segment, but not the ID.</p>
<pre><code class="lang-auto">segmentationNode.GetSegmentation().GetSegment('a_segment_id').SetName('segment_name')
</code></pre>
<p>Just wondering if I am missing some API, or it is just not possible.</p>
<p>Thanks!</p>

---

## Post #2 by @jamesobutler (2018-09-10 20:38 UTC)

<p>I know there are calls from the widget:</p>
<pre><code class="lang-python">a=slicer.modules.segmenteditor.widgetRepresentation().self().editor
a.setSegmentationNodeID("words")
# or
a.setCurrentSegmentId("words")</code></pre>

---

## Post #3 by @cpinter (2018-09-10 20:42 UTC)

<p>Why do you want to change the segment ID? Those are just identifiers that do not show up on the UI, they are just strings to uniquely identify the segments. The human readable identifier of the segments are their names. If you really want to, you can <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkSegmentation.h#L204">add a segment with an ID specified</a>.</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> As far as I understand he wants to set the ID for the segment, not the selected segment in Segment Editor.</p>

---

## Post #4 by @phcerdan (2018-09-10 21:01 UTC)

<p>My logic was using <code>segmentId</code> to compare segments (with same ID) between different subjects (each one represented with a SegmentationNode).</p>
<p>Creating a segmentation from a label map always give numerical segmentIds, usually  <code>1, 2, ...</code>. However, when getting a segmentation from a model, the segmentId is the name of the model…</p>
<p>I wanted to change the segmentId generated from the model to be <code>1</code>, for easy comparison with label maps.</p>
<p>But I can change my logic to use the segment name instead of ID, which makes more sense. Thanks!</p>

---

## Post #5 by @cpinter (2018-09-10 21:07 UTC)

<p>Segment name could work for sure, however if you want to find corresponding segments, then I’d suggest making use of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Terminologies">terminologies feature</a>.<br>
Once you select a terminology for a segment, it fills a <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkSegment.h#L52">tag</a> in the segment. You can then compare the values of these tags. The advantage of using terminologies is that it relies on a standard dictionary, which is unambiguous, and there is no room for human error when inputing the name for example.</p>

---

## Post #6 by @lassoan (2018-09-10 21:44 UTC)

<p>Changing segment ID of a segment that is already added to a segmentation node would cause many issues. When you create a segment but it is not yet added to the segmentation then you can still set the ID. However, for the described purpose teeminology seems to be a much better choice.</p>

---

## Post #7 by @phcerdan (2018-09-10 22:02 UTC)

<p>That sounds good! However, in my testing, it seems that not all the public members of vtkSegment are wrapped in python. Especially missing <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkSegment.h#L107" rel="nofollow noopener">GetTags</a> which uses a <code>std::map</code> as input.</p>
<pre><code class="lang-auto">slicer.mrmlScene.GetNodeByID('vtkMRMLSegmentationNode1').GetSegmentation().GetSegment('1')
</code></pre>
<p>Only <code>GetTag(std::string, std::string&amp;)</code> is available, and it has a string reference, so it might be usable with <code>s_ref = vtk.vtk.reference()</code> for the second argument.</p>
<p>I am going to use names meanwhile, hopefully, will be enough for my needs. Thanks for the input, I will update if I find something else.</p>

---

## Post #8 by @lassoan (2018-09-11 00:45 UTC)

<p>In Slicer you often find multiple interfaces for accessing the same features: some of them are more convenient to use from C++, while others are more accessible from Python.</p>
<p>Segment GetTag()/SetTag() is usable from Python, see for example <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorSurfaceCut/SegmentEditorSurfaceCutLib/SegmentEditorEffect.py">here</a>. You can find example of how to retrieve terminology for a segment <a href="https://github.com/Slicer/Slicer/blob/0f339cc1d8074c4ded2f3c3f54da8f2bdb3836c6/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentsTableView.cxx#L1245-L1315">here</a>.</p>

---

## Post #9 by @cpinter (2018-09-11 12:50 UTC)

<p>If you suggest specific python-accessible functions I can add them for you if this is the issue that prevents using terminologies.</p>

---
