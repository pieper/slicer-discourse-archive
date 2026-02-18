# Custom Segment Editor effect - Undo action

**Topic ID**: 22115
**Date**: 2022-02-22
**URL**: https://discourse.slicer.org/t/custom-segment-editor-effect-undo-action/22115

---

## Post #1 by @giovform (2022-02-22 15:32 UTC)

<p>I am writing a custom segment editor effect in python. I would like to perform some actions when a user clicks the Undo button under the current effect. How could it be done?</p>
<p>Thanks!</p>

---

## Post #2 by @rbumm (2022-02-22 18:25 UTC)

<p>Probably like:</p>
<pre><code class="lang-auto">segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
# do stuff ... but it was wrong
segmentEditorWidget.undo()</code></pre>

---

## Post #3 by @giovform (2022-02-22 20:29 UTC)

<p>No, this is not the intent. I want to perform actions when the user clicks the Undo button.</p>

---

## Post #4 by @rbumm (2022-02-22 20:49 UTC)

<p>Is it the Undo button of the SegmentEditorWidget or your own Undo button ?</p>

---

## Post #5 by @giovform (2022-02-22 20:51 UTC)

<p>From the SegmentEditorWidget</p>

---

## Post #6 by @rbumm (2022-02-22 21:08 UTC)

<p>The action is taking place <a href="https://github.com/Slicer/Slicer/blob/1178ed47833e8d921b36a17e0763828e56e9029b/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx">here</a> line 3148</p>

---

## Post #7 by @rbumm (2022-02-22 21:20 UTC)

<p>There is possibly an undo event that one could trap/handle but this is beyond my scope. Maybe <a class="mention" href="/u/lassoan">@lassoan</a> could comment</p>

---

## Post #8 by @lassoan (2022-02-22 22:02 UTC)

<blockquote>
<p>I want to perform actions when the user clicks the Undo button.</p>
</blockquote>
<p>There is no VTK event invoked or Qt signal emitted if the user clicks Undo/Redo, because Undo/Redo is just one of many reasons a segmentation node can change. Your custom effect should behave correctly regardless of what caused that change.</p>
<p>If you describe your use case in more detail then we can help finding the most appropriate objects and events to observe.</p>

---
