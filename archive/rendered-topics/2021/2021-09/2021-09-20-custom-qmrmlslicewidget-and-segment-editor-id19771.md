---
topic_id: 19771
title: "Custom Qmrmlslicewidget And Segment Editor"
date: 2021-09-20
url: https://discourse.slicer.org/t/19771
---

# Custom qMRMLSliceWidget and segment editor

**Topic ID**: 19771
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/custom-qmrmlslicewidget-and-segment-editor/19771

---

## Post #1 by @giovform (2021-09-20 20:43 UTC)

<p>Hello, this code from the script repository creates a slice view widget in a separate window:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout</a></p>
<p>Then I selected a background volume in this new view and went to the segment editor module, but couldn’t use the effects (for the Paint effect for example, the brush cursor does not appear over this new slice view). What is missing to make it work?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26a777612f9e06687075e796833fcf489d9b662e.png" data-download-href="/uploads/short-url/5vWWcQOXk0qMpPIUgEZpf7MPKDY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26a777612f9e06687075e796833fcf489d9b662e_2_627x500.png" alt="image" data-base62-sha1="5vWWcQOXk0qMpPIUgEZpf7MPKDY" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26a777612f9e06687075e796833fcf489d9b662e_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26a777612f9e06687075e796833fcf489d9b662e_2_940x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26a777612f9e06687075e796833fcf489d9b662e.png 2x" data-dominant-color="707272"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1053×839 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-09-21 17:40 UTC)

<p>The Segment Editor gets the list of views from the layout manager. Any additional views are ignored.</p>
<p>To change this, you would first need to create a method in the Segment Editor widget that provides a list of views (this method could use the layout manager by default but could take some extra custom view nodes). Then you would need to update the widget (and a couple of effects that needs a view list) to use this method instead of asking the list of views from the layout manager.</p>

---

## Post #3 by @giovform (2021-09-21 18:03 UTC)

<p>Thanks for your response, <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>But from what I’ve read on the qMRMLSegmentEditorWidget code, it uses the layout manager, as you described, to list the slice view names as in <a href="https://github.com/Slicer/Slicer/blob/5a44b5e47650ea7b954dbfa52bb28da10cd19a32/Modules/Loadable/Segmentations/Widgets/qMRMLSegmentEditorWidget.cxx#L3716" rel="noopener nofollow ugc">here</a>.</p>
<p>If I use the layout manager to list the sliceview names, I get my custom slicewidget listed on the python console:</p>
<blockquote>
<p>slicer.app.layoutManager().sliceViewNames()<br>
(‘TestSlice1’, ‘Red’, ‘Yellow’, ‘Green’)</p>
</blockquote>
<p>The first one is not considered somehow by the cpp code?</p>
<p>The segmentation is displayed on the custom slicewidget just fine, the effects are not.</p>
<p>Also, I’ve noticed another issue with the adjust window/level tool, the functionality works but the mouse pointer does not change when using it at the custom slicewidget.</p>

---

## Post #4 by @lassoan (2021-09-21 20:42 UTC)

<p>You are right, the layout manager returns all view names, not just those that it owns, so that should not prevent segmentation interactions. It seems that the render window interactor that the Segment Editor widget adds observers to, is not the one that actually receives the events. I did a little debugging but it was not obvious what is the root cause of this.</p>

---

## Post #5 by @giovform (2021-09-21 23:43 UTC)

<p>Any near future investigations on this issue, or thoughts on how we could bypass this problem? Sorry for asking this, but it is something we really need in an important module that we are developing.</p>
<p>Thanks again Andras,</p>
<p>Giovanni</p>

---

## Post #6 by @jamesobutler (2021-09-21 23:57 UTC)

<p>Can you explain how you are using this extra slice viewer and why you decided to create a new one instead of using an existing layout view?</p>

---

## Post #7 by @giovform (2021-09-22 00:04 UTC)

<p>Hi James, the user of our module can add slice views via interface (as many as he wants, with interface space limitations, of course), to compare many similar volumes side by side.</p>
<p>This module also allows segmentation (the user has to select the “active” volume that he wants to segment, and we set up the necessary segmentation node and master volume on the Segment Editor widget that is embeded in our module).</p>

---

## Post #8 by @jamesobutler (2021-09-22 00:10 UTC)

<p>I see. So you are trying to implement <a href="https://github.com/Slicer/Slicer/issues/2384" class="inline-onebox" rel="noopener nofollow ugc">arbitrary screen layout grids · Issue #2384 · Slicer/Slicer · GitHub</a> regarding the ability to set up a dynamic layout view based on user selections. Where the user can define their own custom layout of viewers rather than picking from a predefined list.</p>
<aside class="quote no-group" data-username="giovform" data-post="7" data-topic="19771">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>(as many as he wants, with interface space limitations, of course)</p>
</blockquote>
</aside>
<p>Could you instead define a certain number of slice viewers to define a hard constraint? You would register specific layouts of slice viewers instead of trying to dynamically create new ones. I suggest this based on the uncharted territory of manually creating slice views and having all the functionality of segment editor and cursor icon and stuff work appropriately. Creating new slice views has probably only been supported in a basic sense of viewing volume nodes, but not much more.</p>

---

## Post #9 by @lassoan (2021-09-22 00:16 UTC)

<p>I agree. Generating the XML view descriptions on-the-fly is simpler to implement and maintain and more robust than adding views outside the view layout.</p>
<p>If you want to go with creating views outside the view layout then you need to debug the view creation and figure out why the mouse event observations are added to the wrong render window interactor object.</p>

---

## Post #10 by @jamesobutler (2021-09-22 00:18 UTC)

<p>Here is how you can define a new layout and register it as a layout to choose.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-view-layout</a></p>

---

## Post #11 by @giovform (2021-09-30 22:48 UTC)

<p>Hello, sorry for the delayed response. I managed to develop what we needed using layouts, but in the end it is still much more convenient (for this case) to be able to play around with the slice widgets freely, as if they were just another widget.</p>
<p>I think that maybe the example in the script repository, referenced in the beginning of this topic, should have a warning about the lack of segmentation interaction with these custom slice views, to save some time if anyone starts to develop something with them and end up in a dead end like I did.</p>
<p>Thanks for your time to help solve this issue.</p>
<p>Giovanni</p>

---

## Post #12 by @giovform (2021-10-01 00:16 UTC)

<p>One thing that I forgot to mention. Disabling these interactor style actions for a slice view, renders the Data Probe inoperative (not displaying the intensities when the mouse is over the slice view).</p>
<pre><code>    sliceViewInteractorStyle = sliceWidget.sliceView().sliceViewInteractorStyle()
    sliceViewInteractorStyle.SetActionEnabled(sliceViewInteractorStyle.Translate, False)
    sliceViewInteractorStyle.SetActionEnabled(sliceViewInteractorStyle.Zoom, False)
    sliceViewInteractorStyle.SetActionEnabled(sliceViewInteractorStyle.Rotate, False)
</code></pre>
<p>We need to not allow the user to do these actions (the view is configured automatically).</p>

---

## Post #13 by @lassoan (2021-10-01 01:48 UTC)

<aside class="quote no-group" data-username="giovform" data-post="12" data-topic="19771">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>One thing that I forgot to mention. Disabling these interactor style actions for a slice view, renders the Data Probe inoperative (not displaying the intensities when the mouse is over the slice view).</p>
</blockquote>
</aside>
<p>This has been fixed quite long time ago (several months, maybe a year ago).</p>

---

## Post #14 by @giovform (2021-10-01 01:50 UTC)

<p>We are using the Slicer from 2021-09-13</p>

---

## Post #15 by @lassoan (2021-10-01 01:51 UTC)

<p>Try this code in recent official Slicer release and let us know if you don’t see the Data Probe updating:</p>
<pre><code class="lang-python">sliceViewInteractorStyle = slicer.app.layoutManager().sliceWidget("Red").sliceView().sliceViewInteractorStyle()
sliceViewInteractorStyle.SetActionEnabled(sliceViewInteractorStyle.Translate, False)
sliceViewInteractorStyle.SetActionEnabled(sliceViewInteractorStyle.Zoom, False)
sliceViewInteractorStyle.SetActionEnabled(sliceViewInteractorStyle.Rotate, False)
</code></pre>

---

## Post #16 by @giovform (2021-10-01 02:22 UTC)

<p>Uh oh. I was very mistaken about the version we used. The date is from a compiled version of ours, not from the Slicer released date. The Slicer used was from 30/09/2020 revision 29402, exactly a year ago.</p>
<p>I tested your sample code in both the Latest Stable Release (revision 29738) and Latest Preview Release (revision 30272).</p>
<p>The bug is present on the Latest Stable and is fixed in the Latest Preview. We will update our compiled version, since the problem is fixed. Thanks Andras.</p>

---
