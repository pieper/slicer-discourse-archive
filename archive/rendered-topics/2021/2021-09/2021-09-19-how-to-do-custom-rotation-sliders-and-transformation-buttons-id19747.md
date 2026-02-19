---
topic_id: 19747
title: "How To Do Custom Rotation Sliders And Transformation Buttons"
date: 2021-09-19
url: https://discourse.slicer.org/t/19747
---

# How to do custom rotation sliders and transformation buttons with python?

**Topic ID**: 19747
**Date**: 2021-09-19
**URL**: https://discourse.slicer.org/t/how-to-do-custom-rotation-sliders-and-transformation-buttons-with-python/19747

---

## Post #1 by @jmhuie (2021-09-19 15:25 UTC)

<p>Hi all,</p>
<p>I am currently working on a scripted module that requires a user to rotate segments beforehand (currently done in the transforms module). To improve user accessibility, I would like to implement 1 or 2 feature into my module directly. The first option is to create custom transformation sliders that will rotate a segment around its centroid. There is a nice guide for how to initialize rotation around a point <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" rel="noopener nofollow ugc">here</a>. However, I don’t think I can reasonable expect users to set this up themselves and would like to have custom rotation sliders in my module’s GUI that’ll do this. However, I cannot find much documentation on how I would actually implement this. The Room’s Eye View module in SlicerRT does essentially what I want (and way more) but I cannot decipher the source code.</p>
<p>I understand that transformation chains can be complicated so the alternative feature I’d like to add is a button that can access the transforms “interaction in 3D view” feature and toggle it on and off. The only difference I’d want to make is have it initialize the bounds based on a specific node and not all of the nodes for which the transformation is applied (e.g., initialize based on the segment but not the volume node). When initialized based on a segmentation node with a single segment, the interactive 3D box effectively allows the user to rotate the segment around its centroid.</p>
<p>So, I am wondering if there are any resources or python scripted examples with something similar that will point me in the right direction? I would greatly appreciate any help.</p>
<p>Thanks,<br>
Jonathan</p>

---

## Post #2 by @rbumm (2021-09-19 16:13 UTC)

<p>This topic may serve as a good starting point:</p><aside class="quote" data-post="9" data-topic="9398">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rotation-around-specific-point/9398/9">Rotation around specific point</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Pay attention to which transform you apply to the model and which one you are adjusting with sliders (they are not same). 
Also check for any error messages in the console. 
If you need more specific help, share a screen capture video of what you do, or save the scene as a bundle (mrb) file and share that.
  </blockquote>
</aside>
<p>
There is an interesting script and video at the end.</p>

---

## Post #3 by @jmhuie (2021-09-19 18:09 UTC)

<p>Thanks <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>I had not see this video but unfortunately, it only demonstrates the code use to rotate around a point. I am stuck trying to create sliders that will do this automatically.</p>
<p>I did however, manage to implement the second feature I had outlined by following these <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" rel="noopener nofollow ugc">instructions</a> to call the widget from the transforms node. Maybe that’ll also help me figure out how the sliders work.</p>

---

## Post #4 by @rbumm (2021-09-19 19:19 UTC)

<p>You may want to look at the 3D Slicer script repository,<br>
maybe <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" rel="noopener nofollow ugc">this snippet</a> helps …</p>

---

## Post #5 by @chir.set (2021-09-19 19:19 UTC)

<aside class="quote no-group" data-username="jmhuie" data-post="3" data-topic="19747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jmhuie/48/7086_2.png" class="avatar"> jmhuie:</div>
<blockquote>
<p>create sliders that will do this automatically</p>
</blockquote>
</aside>
<p>Would <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/e73746cbd9489508be36ca028281b1db1905d92d/CrossSectionAnalysis/CrossSectionAnalysis.py#L136" rel="noopener nofollow ugc">this</a> be of help to you ?</p>
<p>Unless I misunderstood your requirement, this example connects a slider bar to a function, and forwards the cursor’s position to said function.</p>

---

## Post #6 by @jmhuie (2021-09-19 19:45 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="4" data-topic="19747" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>You may want to look at the 3D Slicer script repository,<br>
maybe <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" rel="noopener nofollow ugc">this snippet </a> helps …</p>
</blockquote>
</aside>
<p>Thanks you for your suggestion! However, I don’t think I have been clear with my problem. The issue I’m having is making custom GUI sliders that will apply a rotation to a segment. I understand how the transformation around a point works and it works great when I use the python console and transforms module. However, I am basically trying to make copies of those transforms rotation sliders in my own module that can rotate a segment around its centroid. This is to make it so the user does not need to keep going back and forth between my module and the transforms module or deal with using python to initialize the rotation around a point.</p>
<aside class="quote no-group" data-username="chir.set" data-post="5" data-topic="19747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Would <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/e73746cbd9489508be36ca028281b1db1905d92d/CrossSectionAnalysis/CrossSectionAnalysis.py#L136" rel="noopener nofollow ugc">this </a> be of help to you ?</p>
<p>Unless I misunderstood your requirement, this example connects a slider bar to a function, and forwards the cursor’s position to said function.</p>
</blockquote>
</aside>
<p>This is definitely helpful! Now I just have to figure out how to actually execute the function that I want to link up with the slider</p>

---

## Post #7 by @jmhuie (2021-09-20 17:01 UTC)

<aside class="quote no-group" data-username="jmhuie" data-post="3" data-topic="19747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jmhuie/48/7086_2.png" class="avatar"> jmhuie:</div>
<blockquote>
<p>I did however, manage to implement the second feature I had outlined by following these <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" rel="noopener nofollow ugc">instructions</a> to call the widget from the transforms node. Maybe that’ll also help me figure out how the sliders work.</p>
</blockquote>
</aside>
<p>I figured out how to add the sliders I wanted using the qMRMLTransformSliders widget. Here is the documentation. <a href="http://apidocs.slicer.org/v4.10/classqMRMLTransformSliders.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: qMRMLTransformSliders Class Reference</a></p>

---
