---
topic_id: 30456
title: "Vmtk Surface Clipping Contribution"
date: 2023-07-07
url: https://discourse.slicer.org/t/30456
---

# Vmtk surface clipping contribution

**Topic ID**: 30456
**Date**: 2023-07-07
**URL**: https://discourse.slicer.org/t/vmtk-surface-clipping-contribution/30456

---

## Post #1 by @DavidM (2023-07-07 19:36 UTC)

<p>I have developed a vmtk module that truncates/clips a vessel at user specified markup points (see image). This is a task that is commonly required for CFD software. I am wondering whether there is interest in contributing this to (I don’t think any of the current modules do this) the vmtk extension? If so it may be worth discussing some design considerations before submission.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20b955697a472dbef0ca63d31daea71bb262cce8.png" data-download-href="/uploads/short-url/4FulYSMOYCqHcrlL97XB83TNfHW.png?dl=1" title="clip_example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20b955697a472dbef0ca63d31daea71bb262cce8_2_690x400.png" alt="clip_example" data-base62-sha1="4FulYSMOYCqHcrlL97XB83TNfHW" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20b955697a472dbef0ca63d31daea71bb262cce8_2_690x400.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20b955697a472dbef0ca63d31daea71bb262cce8_2_1035x600.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/0/20b955697a472dbef0ca63d31daea71bb262cce8_2_1380x800.png 2x" data-dominant-color="D9DCE8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">clip_example</span><span class="informations">1932×1120 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @DavidM (2024-02-28 18:59 UTC)

<p>I just want to follow-up on this. Should I submit a pull request on github? I was not able to add this to the vmtk extension on my own computer. Not sure if it needs to be done from compilation.</p>

---

## Post #3 by @chir.set (2024-02-28 21:58 UTC)

<aside class="quote no-group" data-username="DavidM" data-post="1" data-topic="30456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/71e660/48.png" class="avatar"> DavidM:</div>
<blockquote>
<p>truncates/clips a vessel at user specified markup points</p>
</blockquote>
</aside>
<p>Have you considered ‘Dynamic modeler’ module? It is integrated in Slicer and can cut models in many ways.</p>

---

## Post #4 by @DavidM (2024-03-01 18:12 UTC)

<p>Thanks for highlighting this module. It looks to be quite powerful module but after trying I did not find it easy to clip a vessel normal to a centerline (and add flow extensions) as generally needed for CFD simulations. VMTK has a lot of functionality for this specific purpose.</p>

---

## Post #5 by @chir.set (2024-03-01 20:19 UTC)

<aside class="quote no-group" data-username="DavidM" data-post="4" data-topic="30456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/71e660/48.png" class="avatar"> DavidM:</div>
<blockquote>
<p>clip a vessel normal to a centerline</p>
</blockquote>
</aside>
<p>Ok, I see 3 options then.</p>
<ol>
<li>
<p>Find the closest point (p1) on the centerline to a fiducial point; get the closest centerline point to p1 (p2); this enables you to get a direction vector (v1); create a markups plane; position its first point at p1; set its normal as v1; use ‘Dynamic Modeler’ to cut your surface.</p>
</li>
<li>
<p>For a single tube (no bifurcations), set as many endpoints (fiducial) as needed where you want to chop the tube; create a centerline with ‘Extract centerline’ module; use ‘Branch clipper’ module to split the input tube.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2b76f5dcb99e5088da5caf7d193792a68cd0e95.png" data-download-href="/uploads/short-url/ndsmbVp5kFULI2O2J3ICoSt6oOV.png?dl=1" title="chopped" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2b76f5dcb99e5088da5caf7d193792a68cd0e95_2_139x500.png" alt="chopped" data-base62-sha1="ndsmbVp5kFULI2O2J3ICoSt6oOV" width="139" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2b76f5dcb99e5088da5caf7d193792a68cd0e95_2_139x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2b76f5dcb99e5088da5caf7d193792a68cd0e95_2_208x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2b76f5dcb99e5088da5caf7d193792a68cd0e95.png 2x" data-dominant-color="30352D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">chopped</span><span class="informations">239×858 57.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Clip your surface at a lower level; you can get inspiration <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/b16b9f79a6f6449d31d37b2d260b4d38e83010cf/StenosisMeasurement3D/Logic/vtkSlicerStenosisMeasurement3DLogic.cxx#L91" rel="noopener nofollow ugc">here</a>.</li>
</ol>

---

## Post #6 by @DavidM (2024-03-05 15:38 UTC)

<p>Thanks for demonstrating this and sharing the example. I think there was a little misunderstanding as I have already create an extension to perform this task. I have uploaded to github here - <a href="https://github.com/dmolony3/ClipVessel" class="inline-onebox" rel="noopener nofollow ugc">GitHub - dmolony3/ClipVessel: 3D Slicer extension for clipping or truncating 3D arteries</a>.</p>
<p>I’m trying to see if there is interest in contributing this repository to the current vmtk extension and if so how to go about integrating</p>

---

## Post #7 by @chir.set (2024-03-08 20:39 UTC)

<p>I had a look at your module with much interest, it does what it says in most situations.</p>
<p>But <a href="https://disk.yandex.com/d/i9dJuRA_IwhEyw" rel="noopener nofollow ugc">this segmentation</a>  is stumbling.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a04f7a0bb6b34e1fee491f7dfbebac68a29dccb0.gif" alt="ClipVessel" data-base62-sha1="mSaFKzb7LENGJY72dzmm917tBeg" width="225" height="500" class="animated"></p>
<p>The picture shows that the clipping may be weird and result in unexpected flow extension. As we play with the parameters and point locations, it would sometimes suddenly give expected results. You may download the sample MRB file and place endpoints and clippoints at arbitrary locations to check on your own.</p>
<p>I suspect it’s because the tubes are almost parallel. May be there’s some optimisation to do. Or declare a well defined limitation.</p>
<p>As for merging it in SlicerVMTK as a contribution, this decision belongs to Slicer core developers. I would recommend requesting a review by <a class="mention" href="/u/lassoan">@lassoan</a> in particular.</p>
<p>Regards.</p>

---

## Post #8 by @DavidM (2024-03-08 21:13 UTC)

<p>Thanks for doing some testing of the module, I did try your geometry and I could not replicate, though I’m sure it can behave unexpectedly in cases. In particular, as you mention, vessels running parallel close to each other could be problematic. Are you able to share the markup points that produce the output above with me?</p>

---

## Post #9 by @chir.set (2024-03-08 21:41 UTC)

<aside class="quote no-group" data-username="DavidM" data-post="8" data-topic="30456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/71e660/48.png" class="avatar"> DavidM:</div>
<blockquote>
<p>Are you able to share the markup points that produce the output above with me?</p>
</blockquote>
</aside>
<p><a href="https://disk.yandex.com/d/MmN_0MhtEQp0ig" rel="noopener nofollow ugc">Here</a> is a complete scene file.</p>

---

## Post #10 by @chir.set (2024-03-08 21:59 UTC)

<aside class="quote no-group" data-username="DavidM" data-post="8" data-topic="30456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/71e660/48.png" class="avatar"> DavidM:</div>
<blockquote>
<p>Are you able to share the markup points that produce the output above with me?</p>
</blockquote>
</aside>
<p>I think that surrounding vessels that do not have a centerline, I.e, not studied, must be removed by the user before performing the clipping. May be it should be clearly stated in the documentation.</p>

---

## Post #11 by @lassoan (2024-03-09 02:29 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="7" data-topic="30456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>As for merging it in SlicerVMTK as a contribution, this decision belongs to Slicer core developers. I would recommend requesting a review by <a class="mention" href="/u/lassoan">@lassoan</a> in particular.</p>
</blockquote>
</aside>
<p>Adding the module to the SlicerVMTK extension sounds like a great idea.</p>

---

## Post #12 by @chir.set (2024-03-09 07:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="30456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Adding the module to the SlicerVMTK extension sounds like a great idea.</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> Welcoming more contributors is always a good idea.</p>

---

## Post #13 by @DavidM (2024-03-13 15:05 UTC)

<p>Yes, this seems to be the issue. I was able to generate the correct output for your provided markup points by removing unconnected regions. However, this does not work in all cases where branches do not have centerlines. I have made an edit to the documentation that all branches/vessels should contain a centerline. Again, thanks for testing.</p>

---

## Post #14 by @DavidM (2024-03-13 15:11 UTC)

<p>Great. Can you provide some guidance on how to add it to the current extension. I know I need to make a pull request and I think I need to edit the CMakeLists.txt file. Are there other changes that need to be made?</p>

---

## Post #15 by @chir.set (2024-03-13 17:51 UTC)

<aside class="quote no-group" data-username="DavidM" data-post="14" data-topic="30456">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/71e660/48.png" class="avatar"> DavidM:</div>
<blockquote>
<p>Can you provide some guidance on how to add it to the current extension.</p>
</blockquote>
</aside>
<p>These steps should complete the contribution submission.</p>
<p>Fork the SlicerVMTK repository on github in your own repository.<br>
Clone the forked repository.</p>
<p>Create a branch in your cloned repository (on your machine) (creating a branch is not compulsory).<br>
Add the ClipVessel directory at its root (the one containing ClipVessel.py).<br>
Insert an ‘add_subdirectory(ClipVessel)’ instruction in SlicerVMTK’s root CMakeLists.txt file.<br>
Move the documentation to the Docs directory and update accordingly.<br>
Add an entry in the README.md file in SlicerVMTK’s root to point to your module.</p>
<p>Push to your forked repository (master or your created branch) .<br>
Create the pull request.</p>

---

## Post #16 by @DavidM (2024-03-15 14:32 UTC)

<p>Thanks, will go ahead and do this.</p>

---

## Post #17 by @gpu (2024-06-07 09:01 UTC)

<p>Thanks for awesome work!<br>
just take a look at your code, there are some questions, hope you can help:</p>
<ol>
<li>
<p>you SetClipFunction with a hemi-sphere which the clipFunctionSphere.SetRadius(2 * radius_from_centerline), why multiple with 2? wouldn’t the 2 * R clip the other branch while the branches are close whose distance inside 2 * R.</p>
</li>
<li>
<p>VMTK is able to split every single branch to a single mesh, which then can be clip by a single Plane, as vtkClipPolyData does Clip on every Mesh, then it’s able to ONLY clip the clicked branch while keeping all the other branches not clipped. WHY did you do clip after VMTK branch clipper ?</p>
</li>
<li>
<p>DOES branchClipper in set_clipper did split each branch to a single mesh? as the Branch clipper in VMTK extention in 3D Slicer? if so, that will make sense to ONLY clip the picked branch. BUT why not do Branch clipper as Pre-processing?<br>
AND if so, clip with Plane is enough &amp; no need to clip with semi-sphere, right?</p>
</li>
<li>
<p>where to download this Extention for 3D Slicer?</p>
</li>
</ol>
<p>Thanks!</p>

---
