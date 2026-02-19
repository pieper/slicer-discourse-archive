---
topic_id: 13657
title: "Export Deformation Field As Dicom"
date: 2020-09-23
url: https://discourse.slicer.org/t/13657
---

# Export Deformation Field as Dicom

**Topic ID**: 13657
**Date**: 2020-09-23
**URL**: https://discourse.slicer.org/t/export-deformation-field-as-dicom/13657

---

## Post #1 by @iTheoch (2020-09-23 12:56 UTC)

<p>Dear all,</p>
<p>I am looking if 3D Slicer is capable of exporting Deformable Registration Objects as DICOM. Of course my first priority was to search your forum and see if anyone else had a similar request. Indeed I found a couple related issues (links below)</p><aside class="quote quote-modified" data-post="23" data-topic="368">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-of-registration-dicom-files/368/23">Import of registration DICOM files</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
Thanks for your reply. I have downloaded the most recently nightly Slicer (Slicer 4.11.0-2019-05-19) but I still can’t export the deformable transform (done in “General Registration (BRAINS)” module)? I have succeeded in exporting linear transform and got the SRO (.dcm) which I could import to mim software as REG. Is there any wrong with my Slicer version? Your help is highly appreciated. 
Crayon 
[01] [02]
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="1" data-topic="7997">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/export-deformable-transform-to-dicom/7997">Export deformable transform to DICOM</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for the clarification. 
I have succeeded in installing the extensions using yesterday’s preview release version. But I still have two other questions. 


I want to export deformable transform, but when I install “SlicerRT” extension, “DICOM Registration Export” module didn’t show up. I have followed this <a href="https://discourse.slicer.org/t/import-of-registration-dicom-files/368/22">thread</a> but don’t know how to use that? Could you give some advice? 


I was a bit confused about the warning(?) in Python Interactor (shown below). I have installed “SlicerRT” extension a…
  </blockquote>
</aside>
<p>
Following your suggestions on these threads I have downloaded the latest nightly build at that moment 4.11.0-2020-09-21 r29383 / c299952. Though I cannot find the proper way of using the DICOM Spatial Registration Object Import Export plugin. I have tried SAVE scene option and selected only the Deformation Grid but in the File format combo box I can’t see any DICOM option. Also some options are giving me error on saving (like MHA. MHD) while saving as h5 or txt works.<br>
Also tried right click on scene → Dicom Export but again there when REG object is selected there are no Dicom Tags visible.<br>
Am I doing something completely wrong here or the functionality is still not implemented?</p>
<p>Thank you for your patience, excellent work and assistance.<br>
Kind regards<br>
Yiannis</p>

---

## Post #2 by @cpinter (2020-09-23 13:11 UTC)

<p>It sounds like you don’t have your registration transform under a patient and study. You either need to drag&amp;drop it under an existing study (if your input came from DICOM you have it), or you need to create a new one. You need to do both in the Data module. To create a new patient right-click the empty space and choose Create new subject, and then Create new study under the new patient. Then when the transform is under a study, right-click the study and choose Export to DICOM. Make sure the REG plugin is selected on the bottom left. You can set DICOM tags in this window.</p>

---

## Post #3 by @iTheoch (2020-09-24 10:15 UTC)

<p>Dear cpinter,</p>
<p>Thanks for the quick reply. I have created manually a new patient/study/series tree like this<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f229e9f5df55c0c103af236da027615b95215cf0.png" alt="image" data-base62-sha1="yyhlzDVRznAM1zbG0Msz8BhBkVa" width="396" height="99"></p>
<p>When selecting Export Dicom from the study I get the dialog below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a9ededb99609b665d40f08b97d8e9080aed045a.png" data-download-href="/uploads/short-url/m3PUmdZ2hD0BlQPFUOhh4DvZtSG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a9ededb99609b665d40f08b97d8e9080aed045a.png" alt="image" data-base62-sha1="m3PUmdZ2hD0BlQPFUOhh4DvZtSG" width="653" height="500" data-dominant-color="F0F2F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">660×505 18.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And when I focus on the Deformable Reg node I get no options to select.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0af3ecc8a7b34fe173b0c15f3a8976c758d3a8ef.png" data-download-href="/uploads/short-url/1yTnEnhl9WEgmd8G3MY2oUeAoZ9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0af3ecc8a7b34fe173b0c15f3a8976c758d3a8ef.png" alt="image" data-base62-sha1="1yTnEnhl9WEgmd8G3MY2oUeAoZ9" width="646" height="500" data-dominant-color="F6F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">662×512 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Do I need to install separately the REG plugin? I have installed SlicerRT and SlicerElastix extensions.</p>
<p>Thanks again for your help.</p>
<p>Kind regards<br>
Yiannis</p>

---

## Post #4 by @cpinter (2020-09-24 10:26 UTC)

<p>If the transforms are directly under the study then what happens?</p>
<p>The REG plugin is in SlicerRT.</p>

---

## Post #5 by @iTheoch (2020-09-24 10:43 UTC)

<p>Similar behavior<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c65c749dfaa3bd8b6f913300eab367b82655c73e.png" data-download-href="/uploads/short-url/siMCHvb3blceZ5fJS4YYPLVLb8G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c65c749dfaa3bd8b6f913300eab367b82655c73e.png" alt="image" data-base62-sha1="siMCHvb3blceZ5fJS4YYPLVLb8G" width="646" height="500" data-dominant-color="F2F4F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">662×512 18.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For some reason also I cannot drag and drop in the data tree control. When I click and drag is starting selecting other nodes also. (something different from my initial problem but thought to report it).</p>
<p>the tree that you see above is how is loaded by slicer and by default as I can see the REG is under the study and not the series. But again I don’t get the option to export.</p>
<p>Thanks</p>
<p>update: The drag and drop is now back and running. not sure what was wrong.</p>

---

## Post #6 by @cpinter (2020-09-24 10:58 UTC)

<blockquote>
<p>For some reason also I cannot drag and drop in the data tree control. When I click and drag is starting selecting other nodes also.</p>
</blockquote>
<p>You can drag&amp;drop in the Data module, and not in other views (<a class="mention" href="/u/lassoan">@lassoan</a> the same is happening in the DICOM module, and it’s quite annoying. We should do something with this, maybe just enable single selection, otherwise it seems like a bug that drag&amp;drop is not enabled in those views. What do you think?)</p>
<p>Is there any error in your log? For example “Failed to find moving and/or fixed image for transform…”. Because the transform can only be exported to DICOM if it was created by one of Slicer’s registration modules and the proper references set.</p>
<p>Btw here’s a tutorial about DICOM SROs:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_DICOMRegistrationObject.pptx">
  <header class="source">

      <a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_DICOMRegistrationObject.pptx" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_DICOMRegistrationObject.pptx" target="_blank" rel="noopener">SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_DICOMRegistrationObject.pptx</a></h4>


  This file is binary. <a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_DICOMRegistrationObject.pptx" target="_blank" rel="noopener">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2020-09-24 11:17 UTC)

<p>I remember I was surprised by disabled drag-and-drop, too. Could we just enable drag-and-drop in the subject hierarchy tree widget by default?</p>

---

## Post #8 by @iTheoch (2020-09-24 11:25 UTC)

<p>Thanks for the tutorial, I will study it.<br>
You are absolutely right on the reason of not exporting. I indeed have a “Failed to find moving…” error. And indeed also I am loading a DVF file from Varian Ethos manufacturer. So I assume that importing a DVF from another vendor means that I cannot export again? Is export only available for Slicer created fields?</p>
<p>Thanks again,<br>
Yiannis</p>

---

## Post #9 by @lassoan (2020-09-24 11:38 UTC)

<p>We could probably automatically guess the two images from the scene (if there are multiple candidate image pairs then we could choose the first). Maybe we could also add the series instance uids of the fixed and moving image it to the list of editable DICOM fields in export dialog (just in case someone wants to select.a different one)? Or, could we add node reference selector in the DICOM export info window? <a class="mention" href="/u/cpinter">@cpinter</a> what do you think?</p>

---

## Post #10 by @cpinter (2020-09-24 12:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could we just enable drag-and-drop in the subject hierarchy tree widget by default?</p>
</blockquote>
</aside>
<p>Yes probably that would be a good idea too</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Or, could we add node reference selector in the DICOM export info window?</p>
</blockquote>
</aside>
<p>While reading the first part of your comment this was the idea that popped up in my head. Maybe we should allow series to define the necessary node references and expose them in the export dialog.</p>
<p>Another thing that many people miss is exporting from under a patient/study. There are many things to do in the DICOM export dialog. There may be a project in terms of which we can do some of these in a few months. I’ll ask.</p>
<p>For the specific issue of <a class="mention" href="/u/itheoch">@iTheoch</a>, what I’d suggest so that progress can be made is to set the node references manually. <a class="mention" href="/u/lassoan">@lassoan</a> there is a module exposing node references in one of the developer extensions right?<br>
The two references that need to be set are</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.vtkMRMLTransformNode.GetMovingNodeReferenceRole()
'spatialRegistrationMoving'
&gt;&gt;&gt; slicer.vtkMRMLTransformNode.GetFixedNodeReferenceRole()
'spatialRegistrationFixed'
</code></pre>

---

## Post #11 by @lassoan (2020-09-24 12:58 UTC)

<aside class="quote no-group quote-modified" data-username="cpinter" data-post="10" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could we just enable drag-and-drop in the subject hierarchy tree widget by default?</p>
</blockquote>
</aside>
<p>Yes probably that would be a good idea too</p>
</blockquote>
</aside>
<p>OK. I’ll try this and see if it works as expected or there are side effects that we haven’t thought about.</p>
<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>There are many things to do in the DICOM export dialog. There may be a project in terms of which we can do some of these in a few months. I’ll ask.</p>
</blockquote>
</aside>
<p>Sounds good. It would be nice to have node selectors and enumerated values. Maybe we could reuse parts of the CLI module widget factory.</p>
<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>For the specific issue of <a class="mention" href="/u/itheoch">@iTheoch</a>, what I’d suggest so that progress can be made is to set the node references manually</p>
</blockquote>
</aside>
<p>Agreed.</p>
<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>there is a module exposing node references in one of the developer extensions right?</p>
</blockquote>
</aside>
<p>Yes, “Node info” module in DebuggingTools extension can show node references (you cannot change them, but if the need to add/remove/modify node references comes up frequently enough then it should be easy to implement this).</p>

---

## Post #12 by @cpinter (2020-09-24 13:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>OK. I’ll try this and see if it works as expected or there are side effects that we haven’t thought about.</p>
</blockquote>
</aside>
<p>I’m about to push a PR. Do you have anyhing particular in mind that I should test?</p>

---

## Post #13 by @lassoan (2020-09-24 13:21 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="12" data-topic="13657">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I’m about to push a PR. Do you have anyhing particular in mind that I should test?</p>
</blockquote>
</aside>
<p>Nothing specific, just test drag-and-drop in DICOM module widget (I don’t expect any issues, as its role is essentially the same as in Data module), DICOM export dialog (probably we want to disable drag&amp;drop there), and run the automatic tests. Models and Markups module widgets already have drag&amp;drop enabled, so we don’t need to test there.</p>

---

## Post #14 by @iTheoch (2020-09-24 14:25 UTC)

<p>Hi both,<br>
Thank you for looking at the issue. Is there anything I can do as it is now to apply the workaround or should I wait for some future nightly release version?</p>
<p>Regards<br>
Yiannis</p>

---

## Post #15 by @cpinter (2020-09-24 19:28 UTC)

<p>I added drag&amp;drop to the data tree, see the pull request <a href="https://github.com/Slicer/Slicer/pull/5201">https://github.com/Slicer/Slicer/pull/5201</a></p>
<p><a class="mention" href="/u/itheoch">@iTheoch</a> If you want, you can do everything from Python right now, but as <a class="mention" href="/u/lassoan">@lassoan</a> said we can help you do this from the UI after adding a small feature.</p>

---

## Post #16 by @iTheoch (2020-09-25 08:34 UTC)

<p>Hi both.<br>
Thank you for your assistance and effort. I will check Python to see if I can work around the issue and will be looking forward for a future version.</p>
<p>Kind regards<br>
Yiannis</p>

---

## Post #17 by @cpinter (2020-09-25 09:06 UTC)

<p>Please note that you will need to have two volumes: both the fixed and the moving.</p>
<p>In order to set the references:</p>
<pre><code class="lang-auto">transformNode = getNode('TransformName') # Double-click node in Data module and copy-paste name
fixedVolumeNode = getNode('FixedVolumeName')
transformNode.SetNodeReferenceID(slicer.vtkMRMLTransformNode.GetFixedNodeReferenceRole(), fixedVolumeNode.GetID())
movingVolumeNode = getNode('MovingVolumeName')
transformNode.SetNodeReferenceID(slicer.vtkMRMLTransformNode.GetMovingNodeReferenceRole(), movingVolumeNode.GetID())
</code></pre>
<p>This should do it</p>

---

## Post #18 by @marianaslicer (2021-07-14 10:20 UTC)

<p>Hi everyone,</p>
<p>I exported my DVFs to DICOM as reported in this topic, but I noticed that they have about 400 MB size. Is there any to make DVFs more lightweight? E.g. downsample the data before saving?</p>

---

## Post #19 by @lassoan (2021-07-14 20:32 UTC)

<p>Dense displacement fields are usually this big, it should not cause issues.</p>
<p>You can resample transform using Transforms module → Convert, by specifying a downsampled volume as reference.</p>
<p>However, if you need lower resolution displacement field then probably you can get much better results if you use bspline transform. Bspline transform is the same as grid transform except it uses bspline interpolation instead of trilinear interpolation, therefore a smooth displacement field can be described with several magnitudes less control points.</p>

---
