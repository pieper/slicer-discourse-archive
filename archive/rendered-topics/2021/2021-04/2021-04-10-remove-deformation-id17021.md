---
topic_id: 17021
title: "Remove Deformation"
date: 2021-04-10
url: https://discourse.slicer.org/t/17021
---

# Remove deformation

**Topic ID**: 17021
**Date**: 2021-04-10
**URL**: https://discourse.slicer.org/t/remove-deformation/17021

---

## Post #1 by @Marta_Fernandez (2021-04-10 15:11 UTC)

<p>Hello.<br>
I have a Skull with deformation in the area of the coronal Suture. How I can remove it, to make the parietals and frontal bone match<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a4b05e7bd09cf74fc8a3e8a1a6692e29ee13ef5.jpeg" data-download-href="/uploads/short-url/cSLHVyliG3uzUAprY9FEpy8uy7H.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a4b05e7bd09cf74fc8a3e8a1a6692e29ee13ef5.jpeg" alt="image" data-base62-sha1="cSLHVyliG3uzUAprY9FEpy8uy7H" width="690" height="284" data-dominant-color="C0BF4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">726×299 74.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/600c5bca9ada2f08405e009ae72a128d8ad9434b.png" alt="image" data-base62-sha1="dHGjxQpBWJCssPMqNZ1h4nujDbt" width="161" height="300"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52cbcc365cbff3bc6feb809db1e1cd1de6b28b2.jpeg" data-download-href="/uploads/short-url/yYUPqZWo3bB8zkE0uW6VqDYLuMO.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f52cbcc365cbff3bc6feb809db1e1cd1de6b28b2_2_690x313.jpeg" alt="image" data-base62-sha1="yYUPqZWo3bB8zkE0uW6VqDYLuMO" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f52cbcc365cbff3bc6feb809db1e1cd1de6b28b2_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52cbcc365cbff3bc6feb809db1e1cd1de6b28b2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52cbcc365cbff3bc6feb809db1e1cd1de6b28b2.jpeg 2x" data-dominant-color="BABB5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">898×408 99.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you in advance.</p>

---

## Post #2 by @tsehrhardt (2021-04-11 23:26 UTC)

<p>If you create a separate segment for the frontal and export both segments as 3d models, you can use Meshlab or Meshmixer to shift the frontal. Is this a CT or surface scan?</p>

---

## Post #3 by @muratmaga (2021-04-11 23:40 UTC)

<aside class="quote no-group" data-username="Marta_Fernandez" data-post="1" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marta_fernandez/48/10323_2.png" class="avatar"> Marta_Fernandez:</div>
<blockquote>
<p>I have a Skull with deformation in the area of the coronal Suture. How I can remove it, to make the parietals and frontal bone match</p>
</blockquote>
</aside>
<p>I am not sure how it will turn out, but at least you can try something like this fairly easily.</p>
<ol>
<li>Create a curve along the coronal suture (with fairly high number of points, for that you can use resample). Rename this curve original</li>
<li>Clone that curve, and move the points where you would like the coronal suture to be stretched. Rename this curve modified.</li>
<li>Use the Fiducial Registration wizard (available in SlicerIGT) to create a <strong>Warping</strong> transformation <strong>From</strong> original curve to <strong>To</strong> modified curve.</li>
<li>Apply this transformation to your model (you may want to clone the model before you do this, so that you can see the effect of the warp).</li>
<li>Keep adjusting the points on the Modified curve, until you achieve the results you are looking for.</li>
</ol>

---

## Post #4 by @Marta_Fernandez (2021-04-12 13:20 UTC)

<p>Hi. It is a surface scan.</p>

---

## Post #5 by @Marta_Fernandez (2021-04-13 13:30 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Fiducial Registration wizard</p>
</blockquote>
</aside>
<p>Thanks for the advice. But I can´t put the curve in the fiducial Registration Wizard to create a warping transformation.<br>
So how y can put the “original curve” and the “modified curve” in the <strong>For</strong> and <strong>To</strong> places??<br>
And the resample is not working also. I only can create the curve from the points tool</p>

---

## Post #6 by @tsehrhardt (2021-04-13 13:40 UTC)

<p>Did you scan the frontal separately and digitally attach because I can see displacement of the frontal at the right frontozygomatic suture?</p>

---

## Post #7 by @Marta_Fernandez (2021-04-13 13:55 UTC)

<p>I scan separately the frontal, the parietal and the temporal and later fuse them.<br>
Any advice or recommendations?</p>

---

## Post #8 by @muratmaga (2021-04-13 15:10 UTC)

<aside class="quote no-group" data-username="Marta_Fernandez" data-post="5" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marta_fernandez/48/10323_2.png" class="avatar"> Marta_Fernandez:</div>
<blockquote>
<p>But I can´t put the curve in the fiducial Registration Wizard to create a warping transformation.</p>
</blockquote>
</aside>
<p>You are right, it doesn’t seem to accept curve markups type. While you can copy and paste points from curve to a fiducial markups, I don’t think this will work well for you. Slicer is not really a mesh editing software and as such has limited capabilities to do fusion. You can put every individual bone under a transform and manually translate/rotate them. Or you can try the osteotomy planner:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.kitware.com//introducing-osteotomy-planner-a-3d-slicer-extension-module-to-simulate-bone-cutting-remodeling-and-repositioning/">
  <header class="source">
      <img src="https://www.kitware.com/main/wp-content/themes/kitwarean/assets/img/favicon/android-icon-192x192.png" class="site-icon" width="192" height="192">

      <a href="https://www.kitware.com//introducing-osteotomy-planner-a-3d-slicer-extension-module-to-simulate-bone-cutting-remodeling-and-repositioning/" target="_blank" rel="noopener">kitware.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:400/352;"><img src="https://www.kitware.com/main/wp-content/uploads/2018/05/OsteotomyPlannerFeat-e1525966609693.jpg" class="thumbnail" width="400" height="352"></div>

<h3><a href="https://www.kitware.com//introducing-osteotomy-planner-a-3d-slicer-extension-module-to-simulate-bone-cutting-remodeling-and-repositioning/" target="_blank" rel="noopener">Introducing Osteotomy Planner: A 3D Slicer extension module to simulate bone...</a></h3>

  <p>This blog describes the Osteotomy Planner extension module that was developed for osteotomy simulation. This module was presented at the SPIE Medical Imaging conference recently held in Houston, TX [1]. This extension is available in the 3D Slicer...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2021-04-18 05:32 UTC)

<p>Fiducial registration wizard (in SlicerIGT) should take care of this. 6-8 anatomical landmarks should align things well if there is only rigid misalignment (translation/rotation).</p>
<p>If you need warping transform then complete the rigid registration and harden the transform. Then place 10-20 markups fiducial points in the region that you want to warp and place about 10-20 additional landmarks distributed evenly in areas that you don’t want to warp. Use these as “from” points in Fiducial registration wizard module. Clone this markups fiducial list and choose the clone as “to” points. Hide the “from” points (to prevent them from moving) and adjust the “to” points to warp the mesh.</p>
<p>If you have open surfaces then you can merge them using “Merge models” module. If you have closed surfaces then you can merge them using “Combine models” module (provided by Sandbox extension).</p>

---

## Post #10 by @tsehrhardt (2021-04-23 12:16 UTC)

<p>Marta I sent you a direct message about how to make the adjustments to the separate pieces in Meshlab and Meshmixer. If I have enough time when scanning skulls for facial approximation, I scan the fragments separately and also tape them together (if they fit) to get at least one 360 scan to help with digitally fitting the fragments together.</p>

---

## Post #11 by @lassoan (2021-04-23 13:09 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="10" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>Marta I sent you a direct message about how to make the adjustments to the separate pieces in Meshlab and Meshmixer.</p>
</blockquote>
</aside>
<p>It is too bad you don’t find the workflow in Slicer convenient enough. Could we do something to improve?</p>

---

## Post #12 by @tsehrhardt (2021-04-23 13:41 UTC)

<p>I’ve just always used Meshlab for working with surface scans. I can use the alignment tool for fitting fragments or just grab the pieces and move them where I need them. I haven’t tried to do the same things in Slicer yet.</p>

---

## Post #13 by @lassoan (2021-04-23 14:56 UTC)

<p>For many years, we did not really add surface manipulation capabilities to 3D Slicer. However, some of our funded projects (in neuorimaging, cardiac modeling, etc.) increasingly work in the surface domain. Moreover, there are huge improvements in Slicer and VTK while almost no progress in some of the commonly used mesh editing tools (MeshMixer and MeshLab). Therefore it makes sense to expose more surface manipulation features in Slicer.</p>
<p>If you let us know what surface manipulation features you need (especially those that are often used along with imaging) then we can take that information into account when deciding what features to prioritize.</p>

---

## Post #14 by @muratmaga (2021-04-23 15:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you let us know what surface manipulation features you need (especially those that are often used along with imaging) then we can take that information into account when deciding what features to prioritize.</p>
</blockquote>
</aside>
<p>We don’t do surface scanning, but a lot of my colleagues working with large-ish things do. I think available tools for manipulating individuals tools (such as transforms and fiducial registration) are ok to manually align individual objects. What I think would entice the surface scanning crowd in biology to start using Slicer more, if there can be a way to register individual mesh segments (that were scanned individually) more automatically and then fuse them.</p>
<p>That, and being able to import/display textures more easily are the common requests we hear about.</p>

---

## Post #15 by @lassoan (2021-04-23 15:20 UTC)

<p>Displaying RGB color when loading PLY textures should have improved usability already. Loading textures from separate image files would be quite easy to implement, too.</p>
<p>There have been modules developed for automatic bone segment registration, but the developers have moved on. You would need funding or research groups that are interested in making their automatic alignment tools available for Slicer.</p>
<p>For manual alignment, virtual reality works amazingly well. It is very similar to holding the physical pieces and putting them together with your hand, but it is actually easier, because the pieces stay in mid-air where you left them, so you don’t need glue. You can also rotate and zoom the world around very easily, so you are not limited by your physical eyesight or steadiness of your hand. If anyone needs to frequently put together models from multiple pieces, investing $1000 into a virtual reality setup is absolutely worth it (you also need to get a desktop computer or a gaming laptop, because most laptops do not support virtual reality). You can show the current 3D view in virtual reality in Slicer by a single button click.</p>

---

## Post #16 by @muratmaga (2021-04-23 15:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Displaying RGB color when loading PLY textures should have improved usability already. Loading textures from separate image files would be quite easy to implement, too.</p>
</blockquote>
</aside>
<p>I agree, I haven’t had a chance to test this yet. Looking forward to.</p>
<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For manual alignment, virtual reality works amazingly well.</p>
</blockquote>
</aside>
<p>Do you have a demo/tutorial of it somewhere? I tried the Oculus VR with slicer, but wasn’t able to do much beyond being able to slice through MRHead via head gestures and using controllers to manipulate things in space. It was my first time with VR, so perhaps that’s part of it.</p>

---

## Post #17 by @lassoan (2021-04-23 15:42 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="16" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For manual alignment, virtual reality works amazingly well.</p>
</blockquote>
</aside>
<p>Do you have a demo/tutorial of it somewhere?</p>
</blockquote>
</aside>
<p>This is the closest demo video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="VzVjvnKuBAE" data-video-title="3D Slicer reconstruction of fragmented bones in virtual reality" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=VzVjvnKuBAE" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/VzVjvnKuBAE/maxresdefault.jpg" title="3D Slicer reconstruction of fragmented bones in virtual reality" width="" height="">
  </a>
</div>

<aside class="quote no-group" data-username="muratmaga" data-post="16" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I tried the Oculus VR with slicer, but wasn’t able to do much beyond being able to slice through MRHead via head gestures and using controllers to manipulate things in space.</p>
</blockquote>
</aside>
<p>Lots of Slicer features are available, it is just not obvious to the users, because there is no module to conveniently set up the scene for various use cases. For now, you need to set up manually based on the instructions <a href="https://github.com/KitwareMedical/SlicerVirtualReality#transform-objects">here</a>. I think <a class="mention" href="/u/cpinter">@cpinter</a> got a grant recently that will address this shortcoming.</p>

---

## Post #18 by @tsehrhardt (2021-04-27 14:24 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="17021">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you let us know what surface manipulation features you need (especially those that are often used along with imaging) then we can take that information into account when deciding what features to prioritize.</p>
</blockquote>
</aside>
<p>I use Meshlab to make final meshes from my surface scans–deleting unwanted parts via surface painting or drawing boxes, aligning scans or parts, flip normals, Poisson surface reconstruction for a watertight mesh, decimation, smoothing, adding color/shading. I can quickly toggle vertex colors or textures on/off and transfer them between meshes.  I also apply Ambient Occlusion shading for pathological CT/microCT specimens to highlight the surface details and use the same function to remove internal surfaces if needed.</p>
<p>Even compared to Meshmixer, the manual alignment in Meshlab is easier for me–I can select a single axis to translate/rotate or just click on the model and move it (I usually need this to align separate pieces or 2 surfaces of a flat object). The ICP alignment using 4 or more points is quick and sometimes works for articulating matching edges on fragments or sutures.</p>
<p>I have my workflows down for Meshlab, so it’s just a matter of sitting down with Slicer to see if I can do the same things. For the microCT models, I have started using the Surface Toolbox more than Meshlab to decimate. And I really use a combination of Slicer, Meshlab, and Meshmixer for surface scans and CT/microCT models, depending on what I need!</p>
<p>I have recently started working with post-autopsy CT scans so the areas of interest are not in the correct places. I know I can use Split Volumes in the Segment Editor to create separate volumes for each segment but can I then move these to the correct anatomical positions and then create a new CT volume? I can move the exported models in Meshlab, but then the CT volume doesn’t match. I don’t know at this point if I need the CT volume to match the 3D models, but for these cases it would be nice to have the full workflow in Slicer.</p>

---
