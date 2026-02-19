---
topic_id: 4638
title: "Error Trying To Set Background Volume To A Slice Node In Sli"
date: 2018-11-05
url: https://discourse.slicer.org/t/4638
---

# Error Trying to Set Background Volume to a Slice Node in Slicelet

**Topic ID**: 4638
**Date**: 2018-11-05
**URL**: https://discourse.slicer.org/t/error-trying-to-set-background-volume-to-a-slice-node-in-slicelet/4638

---

## Post #1 by @bsmarine (2018-11-05 15:10 UTC)

<p>Operating system: MacOS 10.13.4<br>
Slicer version: 4.9.0 nightly 2018-8-10<br>
Expected behavior: Ability to set a composite node of a sliceNode to a particular background volume<br>
Actual behavior: ‘NoneType’ object has no attribute ‘GetSliceCompositeNode’</p>
<p>Hi all,</p>
<p>I’m trying to set a SliceNode to a particular background volume within a Slicelet when a button is clicked. Everything works well when button is clicked (volumes load, sliceNode default views are all set to ‘Axial’) except being able to set a SliceNode to a particular background volume. Is it possible that slicer.app.applicationLogic() isnt loading properly?</p>
<p>Vol_list is a list of volume nodes.</p>
<pre><code>sliceNodes = slicer.util.getNodesByClass('vtkMRMLSliceNode')		
for i,sliceNode in enumerate(sliceNodes):
				sliceNode.SetOrientation("Axial")
for i,sliceNode in enumerate(sliceNodes):
				  applicationLogic = slicer.app.applicationLogic()
				  sliceLogic = applicationLogic.GetSliceLogic(sliceNode)
				  sliceLogic.GetSliceCompositeNode().SetBackgroundVolumeID(vol_list[i].GetID())
</code></pre>
<p><code>'NoneType' object has no attribute 'GetSliceCompositeNode'</code></p>
<p>Thanks for any advice or thoughts!</p>
<p>Best,</p>
<p>Brett</p>

---

## Post #2 by @lassoan (2018-11-05 16:41 UTC)

<p>You can find example code for this and many similar tasks in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Iterate_over_current_visible_slice_views.2C_and_set_foreground_and_background_images">script repository</a>.</p>

---

## Post #3 by @bsmarine (2018-11-05 17:02 UTC)

<p>Hi Andras, these are the examples I’ve already been using as a guide… is the code I’ve written above incorrect?</p>

---

## Post #4 by @lassoan (2018-11-05 17:18 UTC)

<p>Please have a look at the current example in the script repository that uses <code>slicer.util.setSliceViewerLayers</code>.</p>
<p>The error indicates that no slice logic is found for a particular slice node. Maybe you are trying to access a slice node that is not used in any view. It is safer to iterate through slice nodes that are used in the current layout as it is done in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_slice_views_in_3D_window">this example</a>. This might also happen if you have created new slice nodes immediately before and associated slice logics are not ready yet (to solve this, you can call your method via a singleshot timer to make sure all scene updates are completed before your code runs).</p>

---

## Post #5 by @bsmarine (2018-11-06 01:59 UTC)

<p>Andras, thanks for the suggestions!</p>
<p>I could be wrong but seemed to run into issues whenever I called slicer.app.layoutManager() or slicer.app.applicationLogic(). They always turn up empty. But when I called these methods within the Python interacter in Slicer they would work fine. I didn’t investigate further using a singleshot timer… maybe that would have helped.</p>
<p>The alternate approach looping through nodes as you mentioned did the trick. Neglected to mention that the aim was to load a different unique image for each viewer which is a familiar layout for radiologists reading MR studies.</p>
<pre><code>vol_list = [list of different volumes already loaded into slicer]
viewNodes = slicer.mrmlScene.GetNodesByClass('vtkMRMLSliceCompositeNode')
for i,viewNode in enumerate(viewNodes):
	viewNode.SetBackgroundVolumeID(vol_list[i].GetID())
</code></pre>
<p>Thanks again for your assistance.</p>
<p>-Brett</p>

---

## Post #6 by @lassoan (2018-11-06 02:18 UTC)

<p>How do you start Slicer?</p>

---

## Post #7 by @bsmarine (2018-11-06 03:10 UTC)

<p>/Applications/Slicer.app/Contents/MacOS/Slicer --no-main-window --python-script seg_widget.py --raw ./RSTestData/Raw/ --ann ./RSTestData/Annotations --assignment ./RSTestData/assignment</p>

---

## Post #8 by @lassoan (2018-11-06 03:12 UTC)

<aside class="quote no-group quote-modified" data-username="bsmarine" data-post="7" data-topic="4638">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bsmarine/48/3898_2.png" class="avatar"> bsmarine:</div>
<blockquote>
<p>–no-main-window</p>
</blockquote>
</aside>
<p>This means there is no main window. No layout manager. No slice views.</p>

---
