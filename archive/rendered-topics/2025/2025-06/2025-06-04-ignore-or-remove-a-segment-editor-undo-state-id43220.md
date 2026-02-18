# Ignore or remove a Segment Editor undo state

**Topic ID**: 43220
**Date**: 2025-06-04
**URL**: https://discourse.slicer.org/t/ignore-or-remove-a-segment-editor-undo-state/43220

---

## Post #1 by @mh00 (2025-06-04 15:54 UTC)

<p>If I have a workflow like the following:</p>
<blockquote>
<p>Load CT and create a Segmentation<br>
Use Paint effect on red slice<br>
Use Paint effect on green slice<br>
Set a tag on the first segment of the segmentation node<br>
Use Paint effect on yellow slice</p>
</blockquote>
<p>In the application I’m working with, the “tag set” operation is done in the background and the user is not aware of it. I’d like for that “tag set” operation to not count as a state that can be undone. For example, if the user were to click the segment editor undo button three times, the three Paint effect changes would be undone. As opposed to the current functionality which would undo two of the three paint effect changes and the “tag set” change.</p>
<p>I’ve tried to do this by:</p>
<ol>
<li>Temporarily turning off undo/redo for the segment editor, setting the segment tag, and re-enabling undo/redo. Doing this with <code>qMRMLSegmentEditorWidget::setUndoEnabled</code> clears the undo history. It seems like undo/redo at the scene level has this type of functionality via <code>vtkMRMLScene::SetUndoOff</code> and <code>vtkMRMLScene::SetUndoOn</code> but I haven’t found anything similar for the segment editor.</li>
<li>Removing the last undo state from the stack, but I haven’t found where that’s exposed in the API.</li>
</ol>
<p>Am I missing a way to accomplish this behavior?</p>

---

## Post #2 by @mau_igna_06 (2025-06-04 18:54 UTC)

<p>I have also wanted in the past an alike feature for a project, my use-case was to compress 2 or more segmentation modifications into only one undo/redo step on the segmentation history chain</p>

---

## Post #3 by @cpinter (2025-06-06 12:14 UTC)

<p>I also bumped into this problem, especially the second one.</p>
<p>My opinion is that it would be quite simple to enable such non-standard operations, by opening the API of the SegmentationHistory, but it is hidden behind Pimpl classes.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> what do you think? Could we expose a few methods in the segment editor widget about the undo history?</p>

---

## Post #4 by @lassoan (2025-06-06 18:12 UTC)

<p>Probably the best would be to implement a <code>bool BlockSaveState(bool)</code> method in <code>vtkSegmentationHistory</code> (similar to <code>blockSignals</code> method in Qt), which could temporarily block all undo save requests. It would be probably quite simple to implement and the operation would be faster and use less memory than implementing methods to delete (merge) undo states.</p>

---
