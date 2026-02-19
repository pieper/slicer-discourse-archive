---
topic_id: 1222
title: "Side By Side Separate Segmentation Editing"
date: 2017-10-13
url: https://discourse.slicer.org/t/1222
---

# Side-by-side separate segmentation editing

**Topic ID**: 1222
**Date**: 2017-10-13
**URL**: https://discourse.slicer.org/t/side-by-side-separate-segmentation-editing/1222

---

## Post #1 by @mschumaker (2017-10-13 22:03 UTC)

<p>Thanks very much for previous assistance.<br>
I’m trying to create side-by-side views of different volumes (same patient, different MR acquisition sequences), with different segmentations active in each view. I have created two segmentation nodes, and I’m using the Segment Editor module.</p>
<pre><code>  self.theSegmentEditorBase = slicer.modules.segmenteditor.widgetRepresentation()
  self.theSegmentEditorWidget = self.theSegmentEditorBase.self()
</code></pre>
<p>The problem I run into is that, I think to change which volume I’m segmenting, I have to change the Segment Editor master volume:</p>
<pre><code>  self.theSegmentEditorWidget.editor.setMasterVolumeNode(self.SSFPVolumeNode)
</code></pre>
<p>When I do this, the displayed volume in both slice views changes to the master volume, and resets the displayed slice to the middle of the range. Also, the segmentation that I’m editing and the mouse cursor appear in both slice views, even when I get them to show different volumes.<br>
I tried</p>
<pre><code>        sliceComposite.SetDoPropagateVolumeSelection(False)
</code></pre>
<p>for each of the slice views, but it doesn’t seem to have an effect in this case.<br>
Is there a way to accomplish what I’m trying to do?<br>
Thanks.</p>

---

## Post #2 by @lassoan (2017-10-15 01:13 UTC)

<p>I’ve added two features (available in tomorrow’s build) that will allow parallel editing:</p>
<ol>
<li>
<p>Automatic display of master node can be now disabled</p>
</li>
<li>
<p>Editing of Segmentation nodes is restricted to those views where segmentation node is displayed in.</p>
</li>
</ol>
<p>See details here:</p>
<p><a href="https://github.com/Slicer/Slicer/commit/f039680b594552ebb7a37952771fcd7a7a1e4c0b" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/f039680b594552ebb7a37952771fcd7a7a1e4c0b</a></p>
<p>You may also want to decouple slice browsing between two sets of views (when you move slice views by Shift+MouseMove). To achieve that, make sure the two sets of views use a different <a href="http://apidocs.slicer.org/master/classvtkMRMLAbstractViewNode.html#a896bad470fb25f642165eb6305eee4fc">view group</a>.</p>

---

## Post #3 by @mschumaker (2017-10-16 14:15 UTC)

<p>Thank you very much, I’ve downloaded the newest build, and I’ll try this out.<br>
Regarding decoupling slice browsing, I’m actually linking the two slice views so that the slices shown are in the same axis and same position. With linking on, that’s working as I need it to.<br>
Thanks again.</p>

---

## Post #4 by @mschumaker (2017-10-16 20:58 UTC)

<p>I’ve implemented the change, and it’s working well. The only thing I noticed is that the available Undo actions resets every time the segmentation node and master volume change. Is this the expected behaviour?</p>

---

## Post #5 by @lassoan (2017-10-16 21:17 UTC)

<p>Yes, it is expected. History is stored in the Segment Editor node. You can have two Segment Editor widgets in your module GUI to avoid the need of changing the segmentation node and just hide the one that you don’t use.</p>

---

## Post #6 by @mschumaker (2018-01-26 20:09 UTC)

<p>I’ve started trying to set up two segment editors, though I noticed that there is a singleton tag associated with vtkMRMLSegmentEditorNode in <a href="http://SegmentEditor.py" rel="nofollow noopener">SegmentEditor.py</a>. I’ve tried a couple of ways to define two editors, but without success. How can I create two functioning segment editors?</p>

---

## Post #7 by @lassoan (2018-01-26 20:39 UTC)

<p>We haven’t considered having two segment editor active at the same time when we designed it, but it may be possible to set up.</p>
<p>Segment editor node does not have to be singleton, you can have more such nodes in the scene, just make sure you set the correct one in each segment editor widget.</p>
<p>Each widget will manage those views where the associated segmentation node is displayed in. So, you’ll have to make sure that you set up view node IDs for each segmentation node accordingly.</p>
<p>Can you tell us a bit about your workflow? Why do you find it useful to have two active segment editors?</p>

---

## Post #8 by @mschumaker (2018-01-26 20:58 UTC)

<p>Here’s a screenshot of what I have so far. It’s side-by-side MR image sets for the same patient’s leg. There is a common set of controls. I’m trying to get the Undo/Redo buttons working.<br>
Right now, the segment editor’s active segmentation and master volume automatically change when the mouse moves from the Red to the Yellow view. When we were discussing this a few months ago, you said that every time the segmentation is changed in the editor, the undo history is forgotten, and suggested I could keep the undo history for both segmentations if I didn’t have to keep switching the active segmentation in the same editor.<br>
Ultimately what I want is to be able to click “Undo” and have the previous change be undone, whichever one of the segmentations was last changed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/000559e407803971945063c339974e63a718ac0d.jpeg" data-download-href="/uploads/short-url/bsOwdqgbhlnUPCH9wSA20FVI9.jpg?dl=1" title="Both-ROI-selected" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/000559e407803971945063c339974e63a718ac0d_2_690x307.jpg" alt="Both-ROI-selected" data-base62-sha1="bsOwdqgbhlnUPCH9wSA20FVI9" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/000559e407803971945063c339974e63a718ac0d_2_690x307.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/000559e407803971945063c339974e63a718ac0d_2_1035x460.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/000559e407803971945063c339974e63a718ac0d_2_1380x614.jpg 2x" data-dominant-color="7A7978"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Both-ROI-selected</span><span class="informations">1920×855 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @lassoan (2018-01-26 22:18 UTC)

<p>Why do you need to switch between two segmentation nodes? Would it be possible to keep all segments that you would like to edit in one segmentation?</p>

---

## Post #10 by @mschumaker (2018-01-26 22:39 UTC)

<p>I don’t think I can, from my understanding. The image sets have different dimensions, so I can’t use the same master volume node or reference image geometry.</p>

---

## Post #11 by @lassoan (2018-01-26 23:27 UTC)

<p>You don’t need exactly matching geometry. You can choose a resolution in the segmentation’s internal labelmap that is sufficient for both volumes.</p>

---

## Post #12 by @mschumaker (2018-01-29 16:14 UTC)

<p>That’s a good suggestion, but I don’t think it will work for my application. I’m interested in the specific voxel values that correspond to the label maps.<br>
I’ll shelve this task for now, and revisit it later. Perhaps I can request a feature of retaining undo histories for multiple Segmentations in the same segment editor?</p>

---

## Post #13 by @lassoan (2018-01-29 21:20 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="12" data-topic="1222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>Perhaps I can request a feature of retaining undo histories for multiple Segmentations</p>
</blockquote>
</aside>
<p>Unless we have strong use cases, it is unlikely that we’ll implement maintaining history for multiple Segmentations (due to additional complexity of implementation and potentially increased memory need). If you really want to have such a feature then maybe we could add the necessary API to allow external implementation (for example, emit save state signals that you can use to maintain your own segmentation history objects).</p>

---

## Post #14 by @mschumaker (2018-01-30 15:16 UTC)

<p>That sounds good, thanks. I appreciate it.</p>

---
