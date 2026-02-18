# Landmarking Surface Model - File Formats

**Topic ID**: 15722
**Date**: 2021-01-28
**URL**: https://discourse.slicer.org/t/landmarking-surface-model-file-formats/15722

---

## Post #1 by @EGlynne (2021-01-28 18:43 UTC)

<p>I am currently using photogrammetry methods to create a model in Meshroom. I then take that model and clean it in MeshLab, where I then export it as an stl file and bring that into 3DSlicer to try and landmark.</p>
<ol>
<li>I first have placed all my fiducial markups (fixed landmark). I then try to add an open curve markup to the mouth of the individual. I run into two questions here, first, when I go to resample the curve, if I constrain points to the surface of my model, it creates an odd shape.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a94f67cf7a4cba776a9325e534ed6103b25f2b64.png" alt="Curve" data-base62-sha1="o9MOIupmQygCREVtQbb4f2KsChK" width="130" height="146"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3986323fe4148d51830f4bf99e335f59323d1280.png" alt="Resample_curve" data-base62-sha1="8cSJgfRyERH5uNtvngLOa4mO9Dq" width="261" height="156"><br>
To me this tells me that for some reason the mesh I have created extends beyond the visual surface, but I am not sure. Any insight into this may be helpful, as I am not sure if this is something that I can resolve in the model creation step (MeshRoom) or model cleaning step (MeshLab / Slicer).</p>
<p>The second question this brings me to, is if I could use my prior fiducial points as the landmarks for the curve I want. Right now, I would have redundant data in my fixed landmarks with my curved landmarks, outside of the semi-placed landmarks which define the curve. Perhaps more simply asked, could I use my fiducial landmarks, Red 14-Red 2- Red 13, as the markers or indicators for my curve - set in blue in the above images?</p>
<ol start="2">
<li>In all of this, I would like to also set surface patches on the dorsal region of the skull. I tried doing this in the <em>CreateSemiLMPatches</em> module per listed in our workshop, but I find that the patches keep cutting through the model. Is there a way for me to constrain this to the mesh surface?</li>
</ol>

---

## Post #2 by @pieper (2021-01-28 18:48 UTC)

<p>The images got messed up somehow - can you try re-posting them?</p>

---

## Post #3 by @EGlynne (2021-01-28 18:55 UTC)

<p>Thank you! I edited the images, please let me know if this still does not work.</p>

---

## Post #4 by @muratmaga (2021-01-28 19:20 UTC)

<aside class="quote no-group" data-username="EGlynne" data-post="1" data-topic="15722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eglynne/48/6044_2.png" class="avatar"> EGlynne:</div>
<blockquote>
<p>I first have placed all my fiducial markups (fixed landmark). I then try to add an open curve markup to the mouth of the individual. I run into two questions here, first, when I go to resample the curve, if I constrain points to the surface of my model, it creates an odd shape.</p>
</blockquote>
</aside>
<p>Most people use Slicer for volumetric data. Meshes generated from volumetric scans have two surfaces (an internal and external surface). We implemented a projection option to make sure that we are finding the external surface to move the points on. This is irrelevant for surfaces that are derived from stereophotogrammetry. If you expand the Advanced section in Resample Curve option, you should be able to turn that off (or minimize it), and points will be on the surface like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f323c428cdd3fe8c70ff28b357ec3bd2d10473d8.jpeg" alt="image" data-base62-sha1="yGUEyyytlB8d6opy2wl3wBY7CVa" width="667" height="470"></p>
<p>I suspect same problem is happening for the <code>PseudoLMGenerator</code> module, which also has a similarly named setting ‘Maximum projection factor’. Try setting it to zero (or low).</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> perhaps we might consider a toggle switch for surface vs volumetric meshes?</p>
<p>But more importantly, I think the scale of your input data is wrong. There has been long discussion why <a href="https://discourse.slicer.org/t/beware-of-the-stl-file-format/7642/7">STL is a poor format choice</a> on the forum.  As I measured, the skull is reported to be 0.1mm long. I suspect that’s not the case. If you can, try exporting the data from your original software in a format that will preserve the scale correctly, such as PLY.</p>
<aside class="quote no-group" data-username="EGlynne" data-post="1" data-topic="15722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/eglynne/48/6044_2.png" class="avatar"> EGlynne:</div>
<blockquote>
<p>if I could use my prior fiducial points as the landmarks for the curve I want.</p>
</blockquote>
</aside>
<p>Yes, you can. Create blank curves node (red higlight), then copy and paste your existing anatomical fiducials (blue highlight).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f32138742d7d81230578c76ecb05447e35f28c.png" data-download-href="/uploads/short-url/x5VckbgAoNPusIGjxWktWaUq6kI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f32138742d7d81230578c76ecb05447e35f28c_2_422x500.png" alt="image" data-base62-sha1="x5VckbgAoNPusIGjxWktWaUq6kI" width="422" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f32138742d7d81230578c76ecb05447e35f28c_2_422x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e7f32138742d7d81230578c76ecb05447e35f28c_2_633x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f32138742d7d81230578c76ecb05447e35f28c.png 2x" data-dominant-color="3A454F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">729×862 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
