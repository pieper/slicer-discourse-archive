---
topic_id: 21880
title: "Selected Segment And Applied Effect History On Undo Redo"
date: 2022-02-09
url: https://discourse.slicer.org/t/21880
---

# Selected segment and applied effect history on undo/redo

**Topic ID**: 21880
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/selected-segment-and-applied-effect-history-on-undo-redo/21880

---

## Post #1 by @mau_igna_06 (2022-02-09 21:20 UTC)

<p>Hi Devs.</p>
<p>Our application has a fixed segmentation workflow comprised of several segmentation steps. Each step may create 1 or more segments, select it and execute 1 or more segmentEditorEffects.</p>
<p>The problem with the current undo/redo functionality is that it cannot save the selected segment history along with the segmentation state after the user executes a segmentation step. Also the segmentationHistory does not save the applied effect name.</p>
<p>I would like to access some how this information so I can set up my custom undo/redo logic according to our segmentation steps so it is easy to navigate for the user.</p>
<p>Maybe accessing this signals would be useful:<br>
<a href="https://github.com/Slicer/Slicer/blob/1178ed47833e8d921b36a17e0763828e56e9029b/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L466-L469" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/1178ed47833e8d921b36a17e0763828e56e9029b/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L466-L469</a></p>
<p>But the segmentEditorWidget.SegmentsTableView should be public I think.</p>
<p>Any ideas of how to solve this? Would Slicer core need to be updated for this use case? What would be the best way to do it?</p>

---

## Post #2 by @lassoan (2022-02-09 21:39 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="21880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>The problem with the current undo/redo functionality is that it cannot save the selected segment history along with the segmentation state after the user executes a segmentation step.</p>
</blockquote>
</aside>
<p>If the default segmentation states that are saved are ideal for your workflow then you can disable undo/redo in the segment editor and instantiate your own <code>vtkSegmentationHistory</code> class and save and restore states whenever you see fit.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="21880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Also the segmentationHistory does not save the applied effect name.</p>
</blockquote>
</aside>
<p>An optional “description” input argument could be added to vtkSegmentationHistory::SaveState(). Effects could put in that description what they are about to do, such as “Erode by 3mm”. That description could be shown in the undo/redo button tooltip. Pull request is welcome (i.e., you implement it and Slicer developers review and integrate).</p>
<aside class="quote no-group quote-modified" data-username="mau_igna_06" data-post="1" data-topic="21880">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Maybe accessing this signals would be useful:<br>
<a href="https://github.com/Slicer/Slicer/blob/1178ed47833e8d921b36a17e0763828e56e9029b/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L466-L469" class="inline-onebox">Slicer/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx at 1178ed47833e8d921b36a17e0763828e56e9029b · Slicer/Slicer · GitHub</a></p>
</blockquote>
</aside>
<p>The currently selected segment is available in the segment editor node. You can observe that node if you want to get notified about selection change.</p>

---

## Post #3 by @mau_igna_06 (2022-02-12 18:11 UTC)

<p>I was able to bypass the problem by using the info here: <a href="https://discourse.slicer.org/t/observe-modified-segment/7528/2" class="inline-onebox">Observe modified segment - #2 by lassoan</a> to create a log of executed effects (I could do that because we have segmentation steps that execute sequentially fixed segmentEditor effects or allow user-interactions like paint effect)<br>
And we decided to only give support to undo/redo the paint steps of our workflow.</p>
<p>However, there is a <a href="https://github.com/Slicer/Slicer/issues/6183">bug</a> on the segment editor that breaks our custom undo/redo logic.</p>

---

## Post #4 by @lassoan (2022-02-14 22:37 UTC)

<p>Thanks for reporting the issue, indeed some of the saved undo states were indeed unnecessary - requiring users to do extra undo/redo clicks. The problem is now <a href="https://github.com/Slicer/Slicer/commit/d547e8a34f9877574e1d7aadd64f4f7571591e47">fixed</a>.</p>

---
