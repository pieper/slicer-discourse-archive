---
topic_id: 9483
title: "3D Segment Interaction"
date: 2019-12-12
url: https://discourse.slicer.org/t/9483
---

# 3D Segment Interaction

**Topic ID**: 9483
**Date**: 2019-12-12
**URL**: https://discourse.slicer.org/t/3d-segment-interaction/9483

---

## Post #1 by @manjula (2019-12-12 21:54 UTC)

<p>Is there a interactive tool for us to move the segments ? Like in 3D software so we can move our segments independently with the mouse pointer ?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/365b3d3b53888e7e7d0e8db72a91f753cad18e13.gif" alt="segmentInteraction" data-base62-sha1="7KRggTvTCE6xYWn4rtGUnJ6cDOX" width="500" height="281"></p>
<p>to do this with the mouse without adjusting the sliders in the transform module ???</p>
<div class="youtube-onebox lazy-video-container" data-video-id="VzVjvnKuBAE" data-video-title="3D Slicer reconstruction of fragmented bones in virtual reality" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=VzVjvnKuBAE" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/VzVjvnKuBAE/maxresdefault.jpg" title="3D Slicer reconstruction of fragmented bones in virtual reality" width="" height="">
  </a>
</div>


---

## Post #2 by @pieper (2019-12-12 22:12 UTC)

<p>Yes, you can enable interaction at the transform level and it will apply to any model/segmentation/volume/etc inside that transform.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1524e1be0be84b64317a74ed35f896d1ce1c5ef8.png" alt="image" data-base62-sha1="3132PZL6ejBFSIwtEpAaNvpijCo" width="468" height="428"></p>

---

## Post #3 by @lassoan (2019-12-12 22:21 UTC)

<p>Have you actually tried to align arbitrarily transformed objects with such tools? It is painful.</p>
<p>In general, I would not recommend this kind of visual alignment, as it is an inaccurate and time-consuming iterative process if you use 2D display or 2D input device. In contrast, landmark registration is fast, accurate, and non-iterative. There are several landmark registration modules for Slicer, but the most versatile is “Fiducial registration wizard” module in SlicerIGT extension. For slight alignment of images, you can use “Landmark Registration” module.</p>

---

## Post #4 by @manjula (2019-12-12 22:29 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Dear <a class="mention" href="/u/pieper">@pieper</a> Transform tool allows the rotations but not forward/back/up/down movements interactively. (I mean with the mouse pointer). Yes it does allow to move  forward/back/up/down  with the sliders and rotate the segments with the mouse pointer. I am wondering is it possible to do  forward/back/up/down movements for surgical simulations with this ?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>  This is not for registrations of the segments. Our registration problem is now sorted with the CMF ROI registration option but the problem i described in the development segment still persist with that in our machine.  ( <a href="https://discourse.slicer.org/t/cmfreg-roi-registration-bug/9443" class="inline-onebox">CMFReg - ROI registration Bug</a> )</p>
<p>I want to segment the maxilla and move it in relation to the rest of the segments.<br>
Like this</p>
<div class="lazyYT" data-youtube-id="ZrSx5l8Nyfc" data-youtube-title="Dolphin Aquarium©; surgery video montage" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #5 by @lassoan (2019-12-12 22:42 UTC)

<p>You could create a transform tree to define translation axes and then use sliders to move pieces along those axes. You can put all the necessary sliders on a Python scripted module’s GUI, so you don’t need to switch between transforms and can have customized labels for the sliders.</p>
<p>It could be similar to RoomsEyeView module - <a class="mention" href="/u/cpinter">@cpinter</a> can you send a link to a demo video to show how you can move pieces of a model using Transforms?</p>

---

## Post #6 by @manjula (2019-12-12 22:46 UTC)

<p>Thank you so much i will try that and get back if i run in to problems. Meanwhile having  demo video would be super helpful if available.</p>

---

## Post #7 by @cpinter (2019-12-13 09:39 UTC)

<p>There is no tutorial video showing how to create an adequate transform chain to achieve a specific movement path of objects. There is a demo video, but it only shows how to use the module that uses the transform chain:<br>
<a href="https://1drv.ms/v/s!Ao_a-dPPX98Zg5FhNPEUvyRq4uXAKw" class="onebox" target="_blank">https://1drv.ms/v/s!Ao_a-dPPX98Zg5FhNPEUvyRq4uXAKw</a></p>
<p>To use the module:</p>
<ol>
<li>Install the SlicerRT exension</li>
<li>Go to the Room’s Eye View module</li>
<li>Click Load treatment machine models</li>
</ol>
<p>Unfortunately this also won’t bring you much closer to seeing the actual transform chain, because the transforms are hidden so that they don’t clog the Data module.</p>
<p>To show the nodes you’ll need to paste this in the python interactor:</p>
<pre><code>transformNodes = getNodes('vtkMRMLLinearTransformNode*')
for node in list(transformNodes.values()):
  node.SetHideFromEditors(False)
</code></pre>
<p>The most complex movement belongs to the imaging panel. It had to be driven from code. To see how that movement is created, refer to the source:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/RoomsEyeView/Logic/vtkSlicerRoomsEyeViewModuleLogic.cxx#L993" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/RoomsEyeView/Logic/vtkSlicerRoomsEyeViewModuleLogic.cxx#L993" target="_blank">SlicerRt/SlicerRT/blob/master/RoomsEyeView/Logic/vtkSlicerRoomsEyeViewModuleLogic.cxx#L993</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="983" style="counter-reset: li-counter 982 ;">
<li>
</li>
<li>  vtkMRMLLinearTransformNode* gantryToFixedReferenceTransformNode =
</li>
<li>    this-&gt;IECLogic-&gt;GetTransformNodeBetween(vtkSlicerIECTransformLogic::Gantry, vtkSlicerIECTransformLogic::FixedReference);
</li>
<li>
</li>
<li>  vtkNew&lt;vtkTransform&gt; gantryToFixedReferenceTransform;
</li>
<li>  gantryToFixedReferenceTransform-&gt;RotateY(parameterNode-&gt;GetGantryRotationAngle());
</li>
<li>  gantryToFixedReferenceTransformNode-&gt;SetAndObserveTransformToParent(gantryToFixedReferenceTransform);
</li>
<li>}
</li>
<li>
</li>
<li>//-----------------------------------------------------------------------------
</li>
<li class="selected">void vtkSlicerRoomsEyeViewModuleLogic::UpdateLeftImagingPanelToGantryTransform(vtkMRMLRoomsEyeViewNode* parameterNode)
</li>
<li>{
</li>
<li>  if (!parameterNode)
</li>
<li>  {
</li>
<li>    vtkErrorMacro("UpdateLeftImagingPanelToGantryTransform: Invalid parameter set node");
</li>
<li>    return;
</li>
<li>  }
</li>
<li>  vtkMRMLModelNode* leftImagingPanelModel = vtkMRMLModelNode::SafeDownCast(this-&gt;GetMRMLScene()-&gt;GetFirstNodeByName(IMAGINGPANELLEFT_MODEL_NAME));
</li>
<li>  if (!leftImagingPanelModel)
</li>
<li>  {
</li>
<li>    vtkDebugMacro("UpdateLeftImagingPanelToGantryTransform: Optional imaging panel left model not found");
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #8 by @manjula (2019-12-13 11:05 UTC)

<p>Thanks. It is not exactly how i want to do it but this will become useful to me too. What I really wanted to do was to manipulate the segment/s like here,</p>
<div class="lazyYT" data-youtube-id="VzVjvnKuBAE" data-youtube-title="3D Slicer reconstruction of fragmented bones in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>but not using the Navigation instruments but by using the mouse pointer like in a 3D modelling program.</p>
<p>But his information was super useful for me  as well.</p>

---
