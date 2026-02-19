---
topic_id: 14763
title: "How To Call The Islands Function Of The Segment Editor From"
date: 2020-11-25
url: https://discourse.slicer.org/t/14763
---

# How to call the "Islands" function of the Segment Editor from a python script with "Keep selected island"

**Topic ID**: 14763
**Date**: 2020-11-25
**URL**: https://discourse.slicer.org/t/how-to-call-the-islands-function-of-the-segment-editor-from-a-python-script-with-keep-selected-island/14763

---

## Post #1 by @rbumm (2020-11-25 09:13 UTC)

<p>Hi,</p>
<p>I am developing an semiautomated script for CT lung masking.<br>
After thresholding and cutting out segments of the trachea and left main bronchus (works), I normally  use the “Islands” function of the Segment Editor next with the parameter “Keep selected island”.</p>
<p>However, something like this</p>
<pre><code>    ...
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation","KEEP_SELECTED_ISLAND")
    effect.setParameter("MinimumSize","1000")
    effect.self().onApply()
    ...
</code></pre>
<p>does not work from my script.<br>
How can I pass coordinates / selected slice view / mouse click ?<br>
Would be glad if someone had an idea or a code snippet.</p>
<p>Thanks, best regards<br>
rudolf</p>

---

## Post #2 by @rbumm (2020-11-25 12:12 UTC)

<aside class="quote no-group quote-modified" data-username="rbumm" data-post="1" data-topic="14763">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<pre><code class="lang-auto">...

def rasToDisplay(self, r, a, s):
    displayCoords = [0, 0, 0, 1]

    # get the slice node
    lm = slicer.app.layoutManager()
    sliceWidget = lm.sliceWidget('Red')
    sliceLogic = sliceWidget.sliceLogic()
    sliceNode = sliceLogic.GetSliceNode()

    xyToRASMatrix = sliceNode.GetXYToRAS()
    rasToXyMatrix = vtk.vtkMatrix4x4()
    rasToXyMatrix.Invert(xyToRASMatrix, rasToXyMatrix)

    worldCoords = [r, a, s, 1.0]
    rasToXyMatrix.MultiplyPoint(worldCoords, displayCoords)

    return (int(displayCoords[0]), int(displayCoords[1]))

... 
def how_to_call_keep_selected_islands():
...
    lm = slicer.app.layoutManager()
    sliceWidget = lm.sliceWidget('Red')
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation","KEEP_SELECTED_ISLAND")
    slicer.util.clickAndDrag(sliceWidget, start=self.rasToDisplay(25.3, 5.8, sliceOffset), end=self.rasToDisplay(25.3, 5.8, sliceOffset), steps=1)
    ...
</code></pre>
</blockquote>
</aside>
<p>Found the solution myself.<br>
Enjoy.</p>

---

## Post #3 by @lassoan (2020-11-25 14:47 UTC)

<p>Thanks for sharing. You could make your code simpler and more robust by slightly changing the Islands effect so that it can take a 3D coordinate directly (not just an interaction event that you need to simulate via the GUI). The effect is a simple Python script, which you can freely modify locally (you could inject the 3D coordinate <a href="https://github.com/Slicer/Slicer/blob/c7937deffdfb347f1a8144c5781689ba4fe5b537/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorIslandsEffect.py#L308">here</a>). If the modification works well for you then you can send us a pull request so that we can integrate that change into Slicer core.</p>

---

## Post #4 by @jumbojing (2021-10-02 13:16 UTC)

<aside class="quote no-group quote-modified" data-username="rbumm" data-post="1" data-topic="14763">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<pre><code class="lang-auto">...

def rasToDisplay(self, r, a, s):
    displayCoords = [0, 0, 0, 1]

    # get the slice node
    lm = slicer.app.layoutManager()
    sliceWidget = lm.sliceWidget('Red')
    sliceLogic = sliceWidget.sliceLogic()
    sliceNode = sliceLogic.GetSliceNode()

    xyToRASMatrix = sliceNode.GetXYToRAS()
    rasToXyMatrix = vtk.vtkMatrix4x4()
    rasToXyMatrix.Invert(xyToRASMatrix, rasToXyMatrix)

    worldCoords = [r, a, s, 1.0]
    rasToXyMatrix.MultiplyPoint(worldCoords, displayCoords)

    return (int(displayCoords[0]), int(displayCoords[1]))

... 
def how_to_call_keep_selected_islands():
...
    lm = slicer.app.layoutManager()
    sliceWidget = lm.sliceWidget('Red')
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation","KEEP_SELECTED_ISLAND")
    slicer.util.clickAndDrag(sliceWidget, start=self.rasToDisplay(25.3, 5.8, sliceOffset), end=self.rasToDisplay(25.3, 5.8, sliceOffset), steps=1)
    ...
</code></pre>
</blockquote>
</aside>
<p><a class="mention" href="/u/rbumm">@rbumm</a> 我想知道这个代码只是在一个slice上选点,可是这个slice如何确定呢…我想说的是三维空间的第三个点怎么确定呢?</p>
<blockquote>
<p>I want to know that this code just selects a point on a slice, but how to determine this slice…What I want to konw is how to determine the third point in the three-dimensional space?</p>
</blockquote>

---

## Post #5 by @jumbojing (2021-10-02 13:28 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> 没有更简洁的方法,直接输入the 3D coordinate来获取island?</p>
<blockquote>
<p>There is no more concise way  that inject  the 3D coordinate to get the island…e.g. effiect.setparameter()</p>
</blockquote>

---
