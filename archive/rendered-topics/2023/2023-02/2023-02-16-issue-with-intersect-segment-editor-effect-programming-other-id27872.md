---
topic_id: 27872
title: "Issue With Intersect Segment Editor Effect Programming Other"
date: 2023-02-16
url: https://discourse.slicer.org/t/27872
---

# Issue with "INTERSECT" segment editor effect programming (others are fine)

**Topic ID**: 27872
**Date**: 2023-02-16
**URL**: https://discourse.slicer.org/t/issue-with-intersect-segment-editor-effect-programming-others-are-fine/27872

---

## Post #1 by @nrex45 (2023-02-16 17:29 UTC)

<p>Hello All,</p>
<p>I’ve been working witht the segmentEditor Widget based on the code examples on the dev site and have been referencing the info here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#effect-parameters" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a></p>
<p>But for whatever reason I cannot get the “INTERSECT” option to work. I am able to get every other option (COPY, UNION, SUBTRACT, INVERT, CLEAR, FILL) to work properly, but when I choose INTERSECT it simply returns the first segment I pass, and not the overlap between the two.</p>
<p>My code can be found below… Has anybody been able to get INTERSECT to work properly?</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    
    segmentEditorWidget.setSegmentationNode(segmentationNodeNew)
    segmentEditorWidget.setActiveEffectByName("Logical operators")
    
    effect = segmentEditorWidget.activeEffect()
    effect.self().scriptedEffect.setParameter("Operation","UNION")
    selectedSegmentID = effect.self().scriptedEffect.parameterSetNode().GetSelectedSegmentID()
    effect.self().scriptedEffect.setParameter("BypassMasking", 1)
    effect.self().scriptedEffect.setParameter("ModifierSegmentID",segmentationNodeNew.GetSegmentation().GetNthSegmentID(1))
    effect.self().onApply()
</code></pre>

---

## Post #2 by @lassoan (2023-02-16 19:26 UTC)

<p>This code snippet works well for me on Slicer-5.2.1:</p>
<pre><code class="lang-python">segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorWidget.setActiveEffectByName("Logical operators")
effect = segmentEditorWidget.activeEffect()
effect.self().scriptedEffect.setParameter("Operation","INTERSECT")
effect.self().scriptedEffect.setParameter("BypassMasking", "1")
effect.self().scriptedEffect.setParameter("ModifierSegmentID","Segment_2")
effect.self().onApply()
</code></pre>

---

## Post #3 by @lassoan (2023-02-19 00:20 UTC)

<p>A post was split to a new topic: <a href="/t/processing-slows-down-after-many-iterations/27910">Processing slows down after many iterations</a></p>

---
