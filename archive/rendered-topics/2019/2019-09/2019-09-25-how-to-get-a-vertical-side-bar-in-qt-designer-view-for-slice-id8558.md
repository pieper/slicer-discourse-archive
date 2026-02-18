# How to get a vertical side bar in QT designer view for Slicer

**Topic ID**: 8558
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/how-to-get-a-vertical-side-bar-in-qt-designer-view-for-slicer/8558

---

## Post #1 by @Saima (2019-09-25 10:15 UTC)

<p>How to get the vertical scroll bar in the designers view for slicer.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @lassoan (2019-09-26 01:01 UTC)

<p>Scroll bar is added automatically in the scripted module GUI widget area. You can also enable it for certain widgets (e.g., tables, lists). You may also add a QScrollArea to your GUI. These are all purely Qt features, so you can google for more details and examples.</p>

---

## Post #3 by @Saima (2019-09-28 07:45 UTC)

<p>Hi andras,<br>
I need to add widgets like from segmenteditor I need to add scissors and maskvolume. Is it posssible to add it in your own scripted modules.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @lassoan (2019-09-28 12:25 UTC)

<p>Yes, you can add Segment Editor widget to your module GUI and configure which effects and parts of the widget you want to show. See the Segment Editor module source code for an example.</p>

---

## Post #5 by @Saima (2019-10-04 02:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="8558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>get you want to show. See the Segment Editor module source code for an example.</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I followed what you said. I added the following in the scripted module</p>
<p>self.ui.sEditor.setMRMLScene(slicer.mrmlScene)</p>
<pre><code>segmentEditorSingletonTag = "SegmentEditor"
segmentEditorNode = slicer.mrmlScene.GetSingletonNode(segmentEditorSingletonTag, "vtkMRMLSegmentEditorNode")
if segmentEditorNode is None:
  segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
  segmentEditorNode.SetSingletonTag(segmentEditorSingletonTag)
  segmentEditorNode = slicer.mrmlScene.AddNode(segmentEditorNode)

self.parameterSetNode = segmentEditorNode
self.ui.sEditor.setMRMLSegmentEditorNode(self.parameterSetNode)
</code></pre>
<p>How can I only add the effects I need. Also how can I get the results of segment editor. Example how can I see the segmented volume in other volume inputs of other module</p>
<p>Regards.<br>
Saima Safdar</p>

---

## Post #6 by @lassoan (2019-10-04 04:39 UTC)

<aside class="quote no-group" data-username="Saima" data-post="5" data-topic="8558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>How can I only add the effects I need.</p>
</blockquote>
</aside>
<p>You can use <a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#ac28caab505058e98b850f73044c82ee8">setEffectNameOrder</a> and <a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a7af0c74206f9045a071743d5724ff3a9">setUnorderedEffectsVisible</a> methods of the segment editor widget.</p>
<aside class="quote no-group" data-username="Saima" data-post="5" data-topic="8558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>how can I see the segmented volume in other volume inputs of other module</p>
</blockquote>
</aside>
<p>You can use masterVolumeNode/setMasterVolumeNode and segmentationNode/setSegmentationNode methods of the segment editor widget.</p>

---
