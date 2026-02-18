# CT Perfusion coregistration with DWI

**Topic ID**: 7312
**Date**: 2019-06-26
**URL**: https://discourse.slicer.org/t/ct-perfusion-coregistration-with-dwi/7312

---

## Post #1 by @Sibi_Thirunavukarasu (2019-06-26 11:51 UTC)

<p>Hi I am trying to prepare ground truth for a CT Perfusion based stroke study. First I am trying to coregister CTP source images with the DWI and then I have to perform segmentation of dwi images.<br>
I am a physician by training and I am just learning to work on slicer for the past few weeks.<br>
I tried to register mri using elastix module. but I am not able to find the CTP images in the module.<br>
CTP source images are multivolume, do I have to separate a single volume before proceeeding with registration using elastix module?</p>

---

## Post #2 by @lassoan (2019-06-27 05:30 UTC)

<p>Sequence registration (that can freeze the heart motion of CTP images so that you can see the perfusion more clearly) requires volume sequence input.</p>
<p>You need to load your image series as Volume sequence: In Advanced settings in DICOM module choose volume sequence loadable in the table. If you load from nrrd, choose “volume sequence” in Description column.</p>

---

## Post #3 by @Sibi_Thirunavukarasu (2019-07-02 18:11 UTC)

<p>Thanks Dr. Lasso,</p>
<p>I am also getting this error<br>
Error: type object ‘MRMLCorePython.vtkMRMLTransformNode’ has no attribute ‘GetMovingNodeReferenceRole’<br>
When I am performing registration using elastix module.</p>
<p>Regards</p>
<p>Sibi</p>

---

## Post #4 by @lassoan (2019-07-02 19:10 UTC)

<aside class="quote no-group" data-username="Sibi_Thirunavukarasu" data-post="3" data-topic="7312">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sibi_thirunavukarasu/48/3962_2.png" class="avatar"> Sibi_Thirunavukarasu:</div>
<blockquote>
<p>I am also getting this error<br>
Error: type object ‘MRMLCorePython.vtkMRMLTransformNode’ has no attribute ‘GetMovingNodeReferenceRole’</p>
</blockquote>
</aside>
<p>This error has been fixed. If you <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Updating_installed_extensions">update SlicerElastix extension</a> then the problem should go away.</p>

---

## Post #5 by @Sibi_Thirunavukarasu (2019-07-04 18:03 UTC)

<p>Thank you very much. Now it works fine<br>
best regards<br>
Sibi</p>

---
