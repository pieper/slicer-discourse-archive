---
topic_id: 13317
title: "Ia Femesh Extension For Abaqus"
date: 2020-09-03
url: https://discourse.slicer.org/t/13317
---

# IA-FEMesh extension for Abaqus

**Topic ID**: 13317
**Date**: 2020-09-03
**URL**: https://discourse.slicer.org/t/ia-femesh-extension-for-abaqus/13317

---

## Post #1 by @nithin (2020-09-03 12:35 UTC)

<p>Dear all,</p>
<p>I am trying to apply material mapping to the vertebral model and analyze in Abaqus. I exported image data and surface model (.stl) from the 3D slicer, but when the same are imported IA-FEMesh, there is no overlap, so cannot apply the image intensity based properties.</p>
<p>Can you please help me to resolve this issue.</p>
<p>I found out that IA-FEMesh is discontinued  for versions 4.x, Is it possible to link the IA-FEMesh to 3D slicer older versions?</p>

---

## Post #2 by @lassoan (2020-09-03 12:37 UTC)

<p>You can generate volumetric meshes for FEA using Segment Mesher module (provided by Segment Editor extension). Let us know how it works for you.</p>

---

## Post #3 by @pieper (2020-09-03 12:42 UTC)

<p>IA-FEMesh is not currently funded, so it’s likely to be ported to new versions of Slicer.  But it’s open source in case anyone wants to try.  I believe some of the features it exposed are not available in other packages.</p>
<p>Regarding the positioning issue, earlier versions of Slicer used the RAS convention but newer versions save in LPS by default.  Toggling to RAS on export might fix your issue.</p>

---

## Post #4 by @lassoan (2020-09-03 13:33 UTC)

<p>As far as I know, SegmentMesher development is funded and some new meshing algorithm integration and other features are planned. If you describe what you need then we should be able to tell if it’s already available, comes soon, or not planned yet.</p>

---

## Post #5 by @nithin (2020-09-03 14:13 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , <a class="mention" href="/u/pieper">@pieper</a> thanks for the replay,</p>
<p>My aim is to model spine from ct images and analyze it under different loading conditions in finite element software Abaqus.<br>
I also need to apply image-intensity specific properties to the mesh.</p>

---

## Post #6 by @lassoan (2020-09-03 14:46 UTC)

<p>That should already work. After you create the volumetric mesh with “Segment mesher” module, you can assign CT intensity to each mesh point by using “Probe volume with data” module.</p>

---

## Post #7 by @nithin (2020-09-04 02:05 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, thanks for the replay,</p>
<p>I tried to change change from LPS to RAS, but i didn’t find any option.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b144fb9435cd6e9be6bf7c02f23201b6e476fff.jpeg" data-download-href="/uploads/short-url/1A0LGMdHcUXJwC4J9gpexI2JLwb.jpeg?dl=1" title="save_slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b144fb9435cd6e9be6bf7c02f23201b6e476fff_2_689x160.jpeg" alt="save_slicer" data-base62-sha1="1A0LGMdHcUXJwC4J9gpexI2JLwb" width="689" height="160" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b144fb9435cd6e9be6bf7c02f23201b6e476fff_2_689x160.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0b144fb9435cd6e9be6bf7c02f23201b6e476fff_2_1033x240.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b144fb9435cd6e9be6bf7c02f23201b6e476fff.jpeg 2x" data-dominant-color="F2F2F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">save_slicer</span><span class="informations">1293×301 57.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @nithin (2020-09-04 02:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, thanks for the replay,<br>
i will try to use Segment mesher and update you, if it works.</p>
<p>Thanks</p>

---

## Post #9 by @lassoan (2020-09-04 02:45 UTC)

<aside class="quote no-group" data-username="nithin" data-post="7" data-topic="13317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/919ad9/48.png" class="avatar"> nithin:</div>
<blockquote>
<p>I tried to change change from LPS to RAS, but i didn’t find any option.</p>
</blockquote>
</aside>
<p>LPS/RAS coordinate system selection is available in recent Slicer-4.11 versions.</p>

---

## Post #10 by @nithin (2020-09-04 02:59 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, thansk for the replay.</p>
<p>I installed 4.11 version and tried, but i didn’t find the coordinate system option<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/253032f93942597173e1a440d9b9ad0c656f8efb.jpeg" data-download-href="/uploads/short-url/5iYVOFcrLTRqvA9XgxLfjddSsQP.jpeg?dl=1" title="save_slicer_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/253032f93942597173e1a440d9b9ad0c656f8efb_2_690x416.jpeg" alt="save_slicer_2" data-base62-sha1="5iYVOFcrLTRqvA9XgxLfjddSsQP" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/253032f93942597173e1a440d9b9ad0c656f8efb_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/253032f93942597173e1a440d9b9ad0c656f8efb_2_1035x624.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/253032f93942597173e1a440d9b9ad0c656f8efb_2_1380x832.jpeg 2x" data-dominant-color="CDCCD1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">save_slicer_2</span><span class="informations">1919×1159 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @nithin (2020-09-04 03:24 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, thanks for your replay.</p>
<p>I tried segment mesher option and able to generate volume meshing and applied probe volume with data option, is there any way to export the model to abaqus format .inp</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8038271091de0a33452674c1f092e7f6a497a113.jpeg" data-download-href="/uploads/short-url/iihqctBDtYqWAEOa4OoKtX31Deb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8038271091de0a33452674c1f092e7f6a497a113_2_690x412.jpeg" alt="image" data-base62-sha1="iihqctBDtYqWAEOa4OoKtX31Deb" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8038271091de0a33452674c1f092e7f6a497a113_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8038271091de0a33452674c1f092e7f6a497a113_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8038271091de0a33452674c1f092e7f6a497a113_2_1380x824.jpeg 2x" data-dominant-color="8E8D92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1148 453 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks &amp; Regards,</p>

---

## Post #12 by @lassoan (2020-09-04 04:29 UTC)

<p>There are many mesh formats and many mesh converter tools. I don’t know how you can get from vtu/vtk to inp, but it should be possible, maybe in a few steps. Let us know if you find a working combination.</p>
<blockquote>
<p>I installed 4.11 version and tried, but i didn’t find the coordinate system option</p>
</blockquote>
<p>I see, when you load the image then you can specify coordinate system; saving is always LPS by default and cannot be changed it on the GUI, but you can change it in the Python console:</p>
<pre data-code-wrap="ptyhon"><code class="lang-ptyhon">sn = getNode('MyNodeName').GetStorageNode()
sn.SetCoordinateSystem(sn.CoordinateSystemRAS)
</code></pre>

---

## Post #13 by @Michael_Hogg (2020-09-07 10:05 UTC)

<p>I have been using Abaqus for many years to do what you are trying to do, but mainly for knees and hips. I wrote my own package to do this, <a href="https://github.com/mhogg/bonemapy" rel="nofollow noopener">https://github.com/mhogg/bonemapy</a>. It extracts the HU units from the CT scans for all integration points of each element. I don’t really support it these days, but the code is there if you want to have a look. With my background in this area, I would be surprised if you could output an Abaqus .inp file from Slicer. I am not sure about IA-FEmesh.</p>
<p>Not sure you understand what is involved in getting a model like this to run in Abaqus, but you should note that from the CT scans you only get the HU values. You will still need to convert these values to apparent bone density, and then to elastic modulus. There are a few equations around to do this, for example Carter &amp; Hayes.</p>
<p>Also note that there are a few ways you could set up your bone material properties in Abaqus. One is to create a custom material together with user subroutine USDFLD. This method applies elastic modulus to each integration point (this is how my plugin works). Another way would be to calculate the elastic modulus at the centroid of all elements, bin the data, then create an element set and material for each bin.</p>
<p>Good luck,<br>
Michael</p>

---

## Post #14 by @lassoan (2020-09-07 20:25 UTC)

<aside class="quote no-group" data-username="Michael_Hogg" data-post="13" data-topic="13317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michael_hogg/48/5562_2.png" class="avatar"> Michael_Hogg:</div>
<blockquote>
<p>Another way would be to calculate the elastic modulus at the centroid of all elements, bin the data, then create an element set and material for each bin.</p>
</blockquote>
</aside>
<p>This is what you can do directly with Segment Editor and Segment mesher modules: define a number of distinct materials (not just based on HU but location, spatial proximity, etc) and create a multi-material mesh. Then in the simulation software you assign model and properties to each material, set boundary conditions, etc.</p>
<p>I’m not sure if Abaqus can read multimaterial meshes from VTK unstructured grid file format, but FeBIO Studio can. You may give it a try, if you consider other solvers besides Abaqus.</p>

---

## Post #15 by @gsolit (2023-09-01 21:13 UTC)

<p>Is there a guide or tutorial that could be shared?<br>
thanks</p>

---
