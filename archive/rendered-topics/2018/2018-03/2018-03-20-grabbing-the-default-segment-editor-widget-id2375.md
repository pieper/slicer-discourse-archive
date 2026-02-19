---
topic_id: 2375
title: "Grabbing The Default Segment Editor Widget"
date: 2018-03-20
url: https://discourse.slicer.org/t/2375
---

# Grabbing the default segment editor widget

**Topic ID**: 2375
**Date**: 2018-03-20
**URL**: https://discourse.slicer.org/t/grabbing-the-default-segment-editor-widget/2375

---

## Post #1 by @drusmanbashir (2018-03-20 13:32 UTC)

<p>Hi,<br>
Is there any way to access the active segment editor widget, for example to see the master volume / segmentation active currently?</p>
<p>Thanks<br>
Usman.</p>

---

## Post #2 by @lassoan (2018-03-20 13:56 UTC)

<p>Yes, you can access these information, but not through digging in the GUI, but elegantly getting information from the MRML node. For example, if you are interested in the segment editor widget of the Segment Editor module:</p>
<pre><code>segmentEditorNode = slicer.mrmlScene.GetSingletonNode("SegmentEditor", "vtkMRMLSegmentEditorNode")
segmentEditorNode.GetMasterVolumeNode()
</code></pre>
<p>Note that you can place a segment editor widget in your own module’s GUI. That segment editor widget will not use the singleton node above, but you create a separate vtkMRMLSegmentEditorNode for that. See the examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #3 by @drusmanbashir (2018-03-20 13:57 UTC)

<p>Thanks for the prompt reply.</p>

---

## Post #4 by @kayarre (2018-10-23 21:25 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="2" data-topic="2375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>egmentEditorNode = slicer.mrmlScene.GetSingletonNode(“SegmentEditor”, “vtkMRMLSegmentEditorNode”)</p>
</blockquote>
</aside>
<p>can something similar be done to access the instance of  slicer.qMRMLSegmentSelectorWidget()?</p>

---
