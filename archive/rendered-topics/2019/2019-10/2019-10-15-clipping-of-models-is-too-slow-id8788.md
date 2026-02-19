---
topic_id: 8788
title: "Clipping Of Models Is Too Slow"
date: 2019-10-15
url: https://discourse.slicer.org/t/8788
---

# Clipping of models is too slow

**Topic ID**: 8788
**Date**: 2019-10-15
**URL**: https://discourse.slicer.org/t/clipping-of-models-is-too-slow/8788

---

## Post #1 by @Prashant_Pandey (2019-10-15 18:12 UTC)

<p>I’m also trying to clip models as a tracked tool is being moved around, by combining the models module and the volume reslice driver. However it seems that models cannot be clipped in real-time - I manage to get only 1 frame/second. I tried decimating the model, but I have to decimate by 99% to get anywhere near real-time (20/30 FPS) model clipping. Is there a solution to this?</p>

---

## Post #2 by @Prashant_Pandey (2019-10-15 22:35 UTC)

<p>Another issue I’ve come across with clipping modules from the models module is that if you have two different 3D views (‘View1’ and ‘View2’) each showing a different model, and you set both models to be clipped, the clipping parameters will be shared between the two models and views. I think this is a bug, as clipping parameters should be separated by models and views.</p>

---

## Post #3 by @lassoan (2019-10-15 22:53 UTC)

<p>We have implemented many navigation systems over the years and I don’t remember model clipping ever came up as a requirement. Could you write a bit more about your use case? How do you envision to utilize model clipping?</p>
<aside class="quote no-group" data-username="Prashant_Pandey" data-post="2" data-topic="8788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>if you have two different 3D views (‘View1’ and ‘View2’) each showing a different model, and you set both models to be clipped, the clipping parameters will be shared between the two models and views</p>
</blockquote>
</aside>
<p>This is the intended behavior.</p>
<p>You can always add an observer to a slice node and use it to clip your polydata with a filter. You can then choose what to cut and what to show in each view. If you don’t need straight cut then maybe you can find a filter that can clip faster.</p>
<p>How many points and cells are in your data set before and after decimation?</p>

---

## Post #4 by @Prashant_Pandey (2019-10-16 00:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We have implemented many navigation systems over the years and I don’t remember model clipping ever came up as a requirement. Could you write a bit more about your use case? How do you envision to utilize model clipping?</p>
</blockquote>
</aside>
<p>We want to use model clipping to visualize in 3D how the tool lines up with the preoperatively planned path for orthopaedic surgery. Here are two images showing the preop model with pre-op screw plans, and the same model clipped by two orthogonal planes defined by the tool tip.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66c6a1ad97633710f1018fe3b049d3157821fab1.jpeg" data-download-href="/uploads/short-url/eFcgCGPWpF2VocVzrJaBFXTC209.jpeg?dl=1" title="clippingdemo" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66c6a1ad97633710f1018fe3b049d3157821fab1_2_690x405.jpeg" alt="clippingdemo" data-base62-sha1="eFcgCGPWpF2VocVzrJaBFXTC209" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66c6a1ad97633710f1018fe3b049d3157821fab1_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66c6a1ad97633710f1018fe3b049d3157821fab1_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66c6a1ad97633710f1018fe3b049d3157821fab1.jpeg 2x" data-dominant-color="9E9ABA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clippingdemo</span><span class="informations">1287×756 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba1edc996b0d1157cc4c04203bb51fa93891d1f6.jpeg" data-download-href="/uploads/short-url/qyuVGylesLY6MmvEnmG0kgB8Qp8.jpeg?dl=1" title="clippingdemo2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1edc996b0d1157cc4c04203bb51fa93891d1f6_2_690x406.jpeg" alt="clippingdemo2" data-base62-sha1="qyuVGylesLY6MmvEnmG0kgB8Qp8" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1edc996b0d1157cc4c04203bb51fa93891d1f6_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1edc996b0d1157cc4c04203bb51fa93891d1f6_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba1edc996b0d1157cc4c04203bb51fa93891d1f6.jpeg 2x" data-dominant-color="9B9AC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clippingdemo2</span><span class="informations">1284×757 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is to aid the volume reslice views which only show 2D visualizations of the tool relative to the patient.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is the intended behavior.</p>
</blockquote>
</aside>
<p>Could you explain why this is the intended behaviour? I would expect different models and views to have independent properties, especially as other model and view properties are not shared (lighting, surface/point rendering, etc.)</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can always add an observer to a slice node and use it to clip your polydata with a filter. You can then choose what to cut and what to show in each view. If you don’t need straight cut then maybe you can find a filter that can clip faster.</p>
</blockquote>
</aside>
<p>I’m not sure what you mean by cutting/clipping with a filter? Do you have any examples? We would like cuts defined by the tracked tool’s planes.</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How many points and cells are in your data set before and after decimation?</p>
</blockquote>
</aside>
<p>Before decimation: ~1 million points and 2 million cells.<br>
After decimation: 55,000 points and 20,000 cells but the anatomic detail is not sufficient</p>

---

## Post #5 by @lassoan (2019-10-16 05:03 UTC)

<p>It seems that your use case is not a good match for what model clipping offers. However, Slicer is so flexible that there are always many alternative options. You can only clip a 1M point model efficiently at the end of the rendering pipeline, in the mapper. So, instead of using model clipping, you can go one level lower: get the polydata mapper from the displayable manager and then add a clipping plane manually:</p>
<pre><code class="lang-python">
modelNode = getNode('SpinePhantom2Model')
threeDWidgetIndex = 0

# Get model displayable manager
threeDViewWidget = slicer.app.layoutManager().threeDWidget(threeDWidgetIndex)
managers = vtk.vtkCollection()
threeDViewWidget.getDisplayableManagers(managers)
for i in range(managers.GetNumberOfItems()):
  obj = managers.GetItemAsObject(i)
  if obj.IsA('vtkMRMLModelDisplayableManager'):
    modelDisplayableManager = obj
    break

# Get polydata mapper for the model node
modelMapper = modelDisplayableManager.GetActorByID(modelNode.GetDisplayNode().GetID()).GetMapper()

# Add a clipping plane
clippingPlane = vtk.vtkPlane()
modelMapper.AddClippingPlane(clippingPlane)

# Set clipping plane position
clippingPlane.SetOrigin(30,30,30)
clippingPlane.SetNormal(0,0,1)
threeDViewWidget.threeDView().scheduleRender()

# Move clipping plane to a different position
clippingPlane.SetOrigin(30,30,80)
threeDViewWidget.threeDView().scheduleRender()
</code></pre>

---

## Post #6 by @Prashant_Pandey (2019-10-17 04:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="8788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code># Set clipping plane position clippingPlane.SetOrigin(30,30,30) clippingPlane.SetNormal(0,0,1)</code></p>
</blockquote>
</aside>
<p>I tried the above snippet and it can clip the example model in a static way, but how would I change the quoted lines above so that clipping is done dynamically based on my red and yellow slice planes (which are being computed using the volume reslice driver)?</p>

---

## Post #7 by @lassoan (2019-10-17 04:43 UTC)

<p>You can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_transform_is_modified" rel="nofollow noopener">add an observer to the tool’s transform node</a> and update the clipping plane position and orientation whenever the transform is modified.</p>

---

## Post #8 by @Prashant_Pandey (2019-10-17 05:56 UTC)

<p>Thanks!<br>
I’m new to using observers. How do I pass more arguments to the AddObserver function - for example adapting your above snippet I want :</p>
<pre><code>def onTransformNodeModified(transformNode, unusedArg2=None, unusedArg3=None):
	transformMatrix = vtk.vtkMatrix4x4()
	transformNode.GetMatrixTransformToWorld(transformMatrix)
	clippingPlane.SetTransform([transformMatrix.GetElement(0,0), transformMatrix.GetElement(0,1), transformMatrix.GetElement(0,2),transformMatrix.GetElement(0,3),
		transformMatrix.GetElement(1,0), transformMatrix.GetElement(1,1),transformMatrix.GetElement(1,2),transformMatrix.GetElement(1,3),
		transformMatrix.GetElement(2,0), transformMatrix.GetElement(2,1),transformMatrix.GetElement(2,2),transformMatrix.GetElement(2,3),
		transformMatrix.GetElement(3,0), transformMatrix.GetElement(3,1),transformMatrix.GetElement(3,2),transformMatrix.GetElement(3,3)])
	threeDViewWidget.threeDView().scheduleRender() 	


tNode = slicer.mrmlScene.GetNodeByID('vtkMRMLLinearTransformNode4')
tNode.AddObserver(slicer.vtkMRMLTransformNode.TransformModifiedEvent, onTransformNodeModified)
</code></pre>
<p>When I try this and change the transform, the model remains unclipped.</p>

---

## Post #9 by @lassoan (2019-10-17 11:16 UTC)

<p>I don’t think <code>SetTransform</code> is taken into account when using the plane to define a clipping plane in the mapper. Instead, set the origin (from the 4th column of the transform) and normal (3rd column) as I showed in my example above.</p>

---

## Post #10 by @Prashant_Pandey (2019-10-17 20:15 UTC)

<p>Thanks, that worked great!</p>
<p>So now I’m trying to extend this by having two 3D viewers side-by-side, where the same model is in both viewers but is being clipped by different planes in each viewer. Is this possible? I tried changing the 'threeDWidgetIndex from 0 to 1 or 2 but this either crashes Slicer or does not appear to do anything.</p>

---

## Post #11 by @lassoan (2019-10-17 20:47 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="10" data-topic="8788">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>I tried changing the 'threeDWidgetIndex from 0 to 1 or 2</p>
</blockquote>
</aside>
<p>You can ask the number of threeDWidgets from the layout manager. If you try to get an index that goes beyond that number-1 then you’ll make Slicer crash. If you ask for a valid index then it should work well.</p>

---

## Post #12 by @Prashant_Pandey (2019-10-17 22:11 UTC)

<p>Thanks, it’s working perfectly now! See: <a href="https://drive.google.com/open?id=1dpjrrUuoFvtAltOaN_RfPkhyqnYpleU6" rel="nofollow noopener">https://drive.google.com/open?id=1dpjrrUuoFvtAltOaN_RfPkhyqnYpleU6</a></p>
<p>Just wondering if it’s possible to clip volumes with a clipping plane too (as opposed to a ROI annotation)? We have a powerful GPU machine and Slicer renders medical volumes very nicely so it would be nice to be able to use that in the same way.</p>

---

## Post #13 by @lassoan (2019-10-17 23:25 UTC)

<p>Volume rendering displayable manager already uses the mapper’s clipping plane for clipping. You can simply apply the tool transform to the clipping ROI node.</p>

---

## Post #14 by @Prashant_Pandey (2019-10-18 21:37 UTC)

<p>If I understand, for volume rendering it’s a ROI not a plane? Can I apply a plane instead?<br>
I tried transforming the ROI with the tool transform, and manually adjusting the extents of the ROI to make it like a plane, but that isn’t ideal.</p>

---

## Post #15 by @lassoan (2019-10-28 21:15 UTC)

<p>If you just want to clip with a single plane then move the other clipping planes very far (this is what we usually do).</p>
<p>You can manipulate the mapper at lower level at replace the clipping plane set with a single plane but then you will fight with the volume rendering displayable manager (time to time the displayable manager will reset the clipping plane set that is stored in MRML).</p>

---
