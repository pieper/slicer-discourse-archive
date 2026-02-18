# How to rename segments in a segmentation node?

**Topic ID**: 16575
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/how-to-rename-segments-in-a-segmentation-node/16575

---

## Post #1 by @akshay_pillai (2021-03-16 14:47 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.11<br>
How can I change the names of segments in a segmentation. I can do this manually in the GUI but I want to know if there is any way to do this programmatically. I can’t see any mrml node ids for each individual segment.</p>

---

## Post #2 by @Sunderlandkyl (2021-03-16 15:42 UTC)

<p>There are no nodes for individual segments. The segmentation node has a vtkSegmentation object which holds all of the segments.</p>
<p>You can get a segmentation from the segmentation node, and change the name like this:</p>
<pre><code class="lang-auto">segmentation = segmentationNode.GetSegmentation()
segment = segmentation.GetNthSegment(0)
segment.SetName("NewName")
</code></pre>
<p>vtkSegmentation doc: <a href="https://apidocs.slicer.org/master/classvtkSegmentation.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkSegmentation Class Reference</a><br>
vtkSegment doc: <a href="https://apidocs.slicer.org/master/classvtkSegment.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkSegment Class Reference</a></p>

---

## Post #4 by @akshay_pillai (2021-03-19 13:44 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Hey, thanks. Could you also tell me if there is a way to setname for vtkSegmentation and not just vtkSegment?</p>

---

## Post #5 by @Sunderlandkyl (2021-03-19 15:29 UTC)

<p>If you are trying to change the name of the entire segmentation node, you can use:</p>
<pre><code class="lang-auto">segmentationNode.SetName("NewName")
</code></pre>

---

## Post #6 by @akshay_pillai (2021-03-19 15:33 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> thanks again. Sorry for asking again and again but Similarly, if I have other types of nodes like markupcurvesnode but not one but multiple and want to change there names , how would I access each to set names?</p>

---

## Post #7 by @Sunderlandkyl (2021-03-19 15:35 UTC)

<p>The name of every node can be changed with the SetName method.</p>

---
