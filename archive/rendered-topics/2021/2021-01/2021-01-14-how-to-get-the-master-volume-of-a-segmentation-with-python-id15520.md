---
topic_id: 15520
title: "How To Get The Master Volume Of A Segmentation With Python"
date: 2021-01-14
url: https://discourse.slicer.org/t/15520
---

# How to get the master volume of a segmentation with Python

**Topic ID**: 15520
**Date**: 2021-01-14
**URL**: https://discourse.slicer.org/t/how-to-get-the-master-volume-of-a-segmentation-with-python/15520

---

## Post #1 by @samuelholly (2021-01-14 07:57 UTC)

<p>Dear Slicer communnity,</p>
<p>sorry if this was already asked before. I would like to ask how can I get the master volume node from of a segmentation in the Python interactor.</p>
<p>Thank you very much in advance.</p>
<p>Samuel</p>

---

## Post #2 by @samuelholly (2021-01-14 13:23 UTC)

<p>EDIT: I figured out. I used the following code:</p>
<pre><code>segment_editor_node = getNode('SegmentEditor')
</code></pre>
<p>followed by</p>
<pre><code>refvol = segment_editor_node.GetMasterVolumeNode()
</code></pre>
<p>Is this the proper to way to do it?</p>

---

## Post #3 by @cpinter (2021-01-15 10:46 UTC)

<p>It can be if in your use case you only have one segmentation, however it can get you the wrong result if you are editing another segmentation than which you want to get the master volume of.</p>
<p>This is the way to get the volume which gave the geometry of the segmentation: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SubjectHierarchyPlugins/SegmentStatisticsSubjectHierarchyPlugin.py#L93" class="inline-onebox">Slicer/SegmentStatisticsSubjectHierarchyPlugin.py at master · Slicer/Slicer · GitHub</a></p>

---
