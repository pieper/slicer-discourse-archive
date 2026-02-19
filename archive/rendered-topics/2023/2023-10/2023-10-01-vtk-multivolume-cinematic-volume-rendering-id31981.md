---
topic_id: 31981
title: "Vtk Multivolume Cinematic Volume Rendering"
date: 2023-10-01
url: https://discourse.slicer.org/t/31981
---

# VTK multivolume/cinematic volume rendering

**Topic ID**: 31981
**Date**: 2023-10-01
**URL**: https://discourse.slicer.org/t/vtk-multivolume-cinematic-volume-rendering/31981

---

## Post #1 by @Deep_Learning (2023-10-01 14:16 UTC)

<p>Looking for advice.<br>
When starting with a 3D volume and a segmentation with 10 segments…</p>
<p>What are the options in using multivolume volume rendering?</p>
<p>I know that one option is to create 10 volumes using fill outside =0.<br>
That’s going to have memory limitations…</p>
<p>Any other current options?</p>

---

## Post #2 by @muratmaga (2023-10-01 16:50 UTC)

<p>What do you want to achieve?</p>

---

## Post #3 by @Deep_Learning (2023-10-01 21:56 UTC)

<p>Short answer: cinematic rendering of cardiac ct.<br>
As a first step, I would want to have ~20 structures volume rendered with different adjustable transfer functions.  I’ve tried this with two, works fine.</p>
<p>I already have them surface rendered in 3dslicer as a volume and segmentation.<br>
My understanding is that "cinematic rendering’s secret sauce is segmentation followed by multivolume rendering.</p>

---

## Post #4 by @lassoan (2023-10-01 23:43 UTC)

<p>Usually we don’t visualize segmentations using volume rendering. There are many reasons for this, but probably the most important is that soft tissues are not well suited for volume rendering because the texture is not directly useful for visualization. The texture just makes the image more messy, does not make things more recognizable.</p>
<p>Instead, typically structures are segmented and the homogeneous segmentation result is rendered in 3D:</p>
<ul>
<li>If you render opaque segments: surface rendering typically provides much nicer results than volume rendering (there are many shading options and rendering is very efficient).</li>
<li>If you render many segments semi-transparently: it does not matter what rendering you use, because the result is just so complex and hard to interpret that it is rarely useful.</li>
<li>If you render most segments opaque and one or few segments transparently: you can use surface rendering for the opaque segments and may consider volume rendering for the transparent segments. In most use cases, single volume rendering is sufficient, but in rare cases multi-volume rendering might be useful.</li>
</ul>
<p>Therefore, you probably don’t actually need to set up multi-volume rendering for dozens of volumes ever.</p>
<p>What cardiac structures would you like to render? For what purpose (patient communication, anatomy education, treatment planning, simulation, marketing material, …)? Can you show a few example renderings that you have so far?</p>

---

## Post #5 by @Deep_Learning (2023-10-02 15:36 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe396c52b896d218bf243f90689fccd7d8818969.jpeg" data-download-href="/uploads/short-url/AgYiYfVBwtOMwYy6iRtBvH1LLSx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe396c52b896d218bf243f90689fccd7d8818969_2_690x431.jpeg" alt="image" data-base62-sha1="AgYiYfVBwtOMwYy6iRtBvH1LLSx" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe396c52b896d218bf243f90689fccd7d8818969_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe396c52b896d218bf243f90689fccd7d8818969_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe396c52b896d218bf243f90689fccd7d8818969_2_1380x862.jpeg 2x" data-dominant-color="9F9BB0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I 100% agree with your comments… Why go from a quantitative segmentation to volume rendering…<br>
Big information loss.</p>
<p>Pause…</p>
<p>A) A more realistic render.<br>
B) Glutton for punishment…<br>
C) I explored commercial and non-commercial cinematic rendering.  What seems crucial is the segmentation.  For example, aorta, heart, coronary segmentation is crucial for good CR.  I was hoping for a CR with calcium and valves opaque and the rest of the heart translucent.</p>
<p>Restricting myself to the descending aorta and calcium.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d388eefb2b32fc4fc7ed22af9cb97b26ec8409.png" data-download-href="/uploads/short-url/heSvuhVmM43TvNIPDd2IEbspMQp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d388eefb2b32fc4fc7ed22af9cb97b26ec8409_2_690x441.png" alt="image" data-base62-sha1="heSvuhVmM43TvNIPDd2IEbspMQp" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d388eefb2b32fc4fc7ed22af9cb97b26ec8409_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d388eefb2b32fc4fc7ed22af9cb97b26ec8409_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d388eefb2b32fc4fc7ed22af9cb97b26ec8409_2_1380x882.png 2x" data-dominant-color="C6C0DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 496 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would you quickly explain the difference between VTK GPU raycasting and VTK multivolume?<br>
Also, does this setting affect shape rendering?</p>
<p>VTK GPU raycasting seems to work with multivolumes… But the opacity does not have the desired effect. As I rotate (180 degrees) the calcium projects right through the aorta.</p>

---

## Post #6 by @lassoan (2023-10-02 15:52 UTC)

<p>Volume rendering should work very well for blood pool/calcification segmentation. I don’t think it is necessary to use multivolume rendering for this, as calcium would be detected based on voxel value, so you can use the opacity and color transfer functions.</p>
<p>You can use surface rendering for myocardium and valves. You can make rendering more realistic (“cinematic”) by exporting segmentation to models, choose PBR rendering in Models module, and use features in the Lights module (in Sandbox exension).</p>

---

## Post #7 by @Deep_Learning (2023-10-02 19:14 UTC)

<p>If I want to use models in my merged sequence…<br>
I believe that the group of exported models is not a data node, but rather a folder of models.<br>
Is it possible to add the folder of models to a sequence.<br>
I use SetDataNodeAtValue(segmentationNode,n) for segmentations, but it does not work for the folder of models.</p>

---

## Post #8 by @lassoan (2023-10-02 20:02 UTC)

<p>You need to add each model to its own sequence. You can then add all sequences to the same sequence browser node.</p>

---

## Post #9 by @cpinter (2023-10-03 08:34 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="5" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>Would you quickly explain the difference between VTK GPU raycasting and VTK multivolume?</p>
</blockquote>
</aside>
<p>As you also found, the regular GPU raycasting handles one volume at a time, and the order of rendering is always the same, so the depth information between the different rendered volumes is lost (one always appears “in front of” the other). Multi-volume rendering considers all the volumes at the same time when rendering, thus showing realistic depth even if the volumes overlap. The problem with multi-volume rendering is that its development in VTK stopped halfway, so besides some bugs (some of which have been worked around in the Slicer code to make it function), there are some important features missing, such as cropping. We re-added shading, but I believe it’s not perfect either yet.</p>
<p>A very interesting conversation! Do you plan to publish the results of your work later somewhere? I think many Slicer users are interested in approximating cinematic rendering using the platform.</p>

---

## Post #10 by @LucasGandel (2023-10-06 13:05 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> is bringing a good point regarding multivolume support in VTK. It is definitely missing many features that have been implemented for single volume rendering, such as the scattering shading model. We recently added support for mixing RGBA volumes with multivolume, so the development should not be considered stopped. However, it highlights the fact that even small feature like RGBA volume support are missing with vtkMultiVolume, probably because the two paths (single vs multivolume) are too decoupled. I am happy to discuss further this technical point if needed, or assist/review potential contributions.</p>

---

## Post #11 by @Deep_Learning (2023-10-07 13:16 UTC)

<p>Thank you for your reply.</p>
<p>After searching the forum… I always end up agreeing with Andras Lasso.<br>
With one exception.  (there should be support for *.seg.nii.gz).</p>
<p>CR is nice for twitter, patient education and exploration. I will explore model rendering further, but converting all my segmentations to models and controlling the rendering individually will take some coding.</p>
<p>I am by no means an expert in CR.<br>
If people are interesting in CR specifically in Slicer, I would check out paraview if technically inclined and volview if not.  There is a strong relationship between slicer, kitware vtk, paraview, etc. Paraview is excellent for data exdploration.  Paraview is most advanced.</p>
<p>Other options are Blender and Mevislab.</p>
<p>Mevislab has many awesome renderings on their webpage, but I am unable to find the example networks.  If anyone from Mevislab is reading this, please provide example networks for all renderings.</p>

---

## Post #12 by @lassoan (2023-10-09 13:45 UTC)

<p>Yesterday I created a <a href="https://github.com/Slicer/VTK/pull/43#issuecomment-1752104540">new module for generating a full-color RGBA volume</a>, by combining a segmentation and a scalar volume using some smart filtering and masking. Combined with a fix in the VTK RGBA volume renderer, I find that it creates beautiful renderings that hasn’t been possible before; and it surpasses many “cinematic renderings” in the coloring aspect.</p>
<p>For example, TotalSegmentator segmentation results on the CTLiver sample data set are rendered like this:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d21de7da88291c4dfd067825ed24c9fa7b4d139.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d21de7da88291c4dfd067825ed24c9fa7b4d139.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d21de7da88291c4dfd067825ed24c9fa7b4d139.mp4</a>
    </video>
  </div><p></p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Colorized, masked</th>
<th>Colorized, masked</th>
<th>Colorized, not masked</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e14101a69bebdba8dc7f6a543e199096964fc5c8.jpeg" data-download-href="/uploads/short-url/w8GHNSBc8rWxlKxYXGbmPNlPTzq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e14101a69bebdba8dc7f6a543e199096964fc5c8_2_498x499.jpeg" alt="image" data-base62-sha1="w8GHNSBc8rWxlKxYXGbmPNlPTzq" width="498" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e14101a69bebdba8dc7f6a543e199096964fc5c8_2_498x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e14101a69bebdba8dc7f6a543e199096964fc5c8_2_747x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e14101a69bebdba8dc7f6a543e199096964fc5c8.jpeg 2x" data-dominant-color="87747E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×970 83.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de245f380c811ad167e8c53d46b17b3b002385c.jpeg" data-download-href="/uploads/short-url/fG4PC1XLwzx0gf2lMrWyssA54Qs.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de245f380c811ad167e8c53d46b17b3b002385c_2_498x499.jpeg" alt="image" data-base62-sha1="fG4PC1XLwzx0gf2lMrWyssA54Qs" width="498" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de245f380c811ad167e8c53d46b17b3b002385c_2_498x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de245f380c811ad167e8c53d46b17b3b002385c_2_747x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de245f380c811ad167e8c53d46b17b3b002385c.jpeg 2x" data-dominant-color="89686D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">968×970 71.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d14a7afd546e05b88fcbee671324248afd2eca3.jpeg" data-download-href="/uploads/short-url/1RIsxpWlvGMUtPwoRRhhwu1JBjd.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d14a7afd546e05b88fcbee671324248afd2eca3_2_623x499.jpeg" alt="image" data-base62-sha1="1RIsxpWlvGMUtPwoRRhhwu1JBjd" width="623" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d14a7afd546e05b88fcbee671324248afd2eca3_2_623x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d14a7afd546e05b88fcbee671324248afd2eca3_2_934x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d14a7afd546e05b88fcbee671324248afd2eca3.jpeg 2x" data-dominant-color="918AA2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1210×970 73.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
</tr>
</tbody>
</table>
</div><p>Just for reference, surface rendering provides much less texture details - see below. However, what works well for surface rendering (and is not available for volume rendering) is screen-space ambient occlusion (making things that are behind other objects appear darker).</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Surface</th>
<th>Surface with screen-space ambient occlusion</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a3bd16b11993d8b89718109de62a1fb4d733bd6.jpeg" data-download-href="/uploads/short-url/61CddZLpOtfab5J5dj6sw3A5iIK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a3bd16b11993d8b89718109de62a1fb4d733bd6_2_623x499.jpeg" alt="image" data-base62-sha1="61CddZLpOtfab5J5dj6sw3A5iIK" width="623" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a3bd16b11993d8b89718109de62a1fb4d733bd6_2_623x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a3bd16b11993d8b89718109de62a1fb4d733bd6_2_934x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a3bd16b11993d8b89718109de62a1fb4d733bd6.jpeg 2x" data-dominant-color="986661"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1210×970 74.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5445cfbe7bb30c52f7490459c8d7334632d240fe.jpeg" data-download-href="/uploads/short-url/c1vG26AqjuDbgPDNt0io3bBq0O2.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5445cfbe7bb30c52f7490459c8d7334632d240fe_2_623x499.jpeg" alt="image" data-base62-sha1="c1vG26AqjuDbgPDNt0io3bBq0O2" width="623" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5445cfbe7bb30c52f7490459c8d7334632d240fe_2_623x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5445cfbe7bb30c52f7490459c8d7334632d240fe_2_934x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5445cfbe7bb30c52f7490459c8d7334632d240fe.jpeg 2x" data-dominant-color="9D6B62"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1210×970 62.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
</tr>
</tbody>
</table>
</div><p>I think this is the only thing that would be necessary to make stunning volume renderings in VTK. Screen-space ambient occlusion is also very fast, so it could be usable not only for rendering videos, but for real-time rendering for surgical guidance, virtual reality, etc.</p>
<p>I’ve tried the VTK’s scattering shading models, but they are slow, the results look very artificial and low-quality (almost as if there was no shading). It is not just my settings - all the <a href="https://www.kitware.com/volumetric-rendering-in-vtk-and-paraview-introducing-the-scattering-model-on-gpu/">showcased renderings in the Kitware blog</a> all look pretty bad to me. To me, it looks like some interesting effects applied on volume rendering, which make the rendering appear less realistic than basic volume rendering. Scattering also hangs on my laptop and hangs or crashes on my desktop (with RTX3060) after a short while when I’m trying to adjust parameters. Also, it does not seem to work at all for RGBA volumes.</p>
<p><a class="mention" href="/u/lucasgandel">@LucasGandel</a> Are there any better examples of VTK’s scattering shader where the resulting rendering look more realistic? Is there a chance that screen-space ambient occlusion will be made available for volume rendering? (the Z buffer generated by the volume renderer could be used for the occlusion computation)</p>

---

## Post #13 by @LucasGandel (2023-10-09 16:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Awesome work! The texture details look great! Such representations should definitely be considered.</p>
<p>Although I agree that the computation time of the scattering model is problematic, one of the nice effect I like is the shadows/ambient occlusions it brings, which seems obvious to me on the screenshots of the article you referenced. The interesting point you bring is that this makes the final rendering looks less realistic than initially. I would love to discuss this further to understand what makes you think that. If you have concrete examples, please share.</p>
<p>Finally, I love the idea you propose regarding the use of SSAO for volume rendering to improve further the results you already have. Technically, writing the normals and positions as done for the <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/OpenGL2/vtkSSAOPass.cxx#L540" rel="noopener nofollow ugc">polydata mapper</a> could be enough. I’ll try to investigate further.</p>

---

## Post #14 by @muratmaga (2023-10-09 18:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Yesterday I created a <a href="https://github.com/Slicer/VTK/pull/43#issuecomment-1752104540">new module for generating a full-color RGBA volume </a>, by combining a segmentation and a scalar volume using some smart filtering and masking. Combined with a fix in the VTK RGBA volume renderer, I</p>
</blockquote>
</aside>
<p>FYI, looks like this didn’t make it into today’s preview build, neither in Linux nor in Windows. I am very excited to give it a try…</p>

---

## Post #15 by @muratmaga (2023-10-09 23:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> looks like CDASH is showing a configure error for the sandbox extension for the colorize volume module.</p>
<p><a href="https://slicer.cdash.org/build/3171192/configure" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/build/3171192/configure</a></p>

---

## Post #16 by @lassoan (2023-10-10 04:24 UTC)

<aside class="quote no-group" data-username="LucasGandel" data-post="13" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucasgandel/48/18202_2.png" class="avatar"> LucasGandel:</div>
<blockquote>
<p>The interesting point you bring is that this makes the final rendering looks less realistic than initially. I would love to discuss this further to understand what makes you think that</p>
</blockquote>
</aside>
<p>In <a href="https://www.kitware.com/volumetric-rendering-in-vtk-and-paraview-introducing-the-scattering-model-on-gpu/">this blog post</a> the issue may be that the plain volume rendering of the medical images are quite messy, not showing anything clearly or realistically. When the shadows are added then the images become even more complex and harder to interpret and some areas become overexposed/underexposed in certain regions. Maybe the issue is also that there was no particular purpose of the visualization and so random details of the volume got highlighted/suppressed.</p>
<p>The images in <a href="https://www.kitware.com/cinematic-volume-rendering">this blog entry</a> look OK with basic gradient shading but appears faded, washed out when the volumetric shading is used. In case of the hybrid mode, the image loses details.</p>
<p>I would like to play a bit more with these options, but Slicer and ParaView hangs or crashes when I play with the parameters. Also, I would be most interested trying RGBA rendering and that does not seems to work at all for RGBA.</p>
<aside class="quote no-group" data-username="LucasGandel" data-post="13" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucasgandel/48/18202_2.png" class="avatar"> LucasGandel:</div>
<blockquote>
<p>Technically, writing the normals and positions as done for the <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/OpenGL2/vtkSSAOPass.cxx#L540">polydata mapper</a> could be enough. I’ll try to investigate further.</p>
</blockquote>
</aside>
<p>This would be awesome.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>looks like this didn’t make it into today’s preview build</p>
</blockquote>
</aside>
<p>Thanks for testing. In addition to the module, a VTK fix that we worked on with <a class="mention" href="/u/pieper">@pieper</a> must be also integrated. We usually fix issues in VTK first and then cherry pick from there to Slicer, but we can make exceptions if it’s something urgent.</p>

---

## Post #17 by @LucasGandel (2023-10-10 11:58 UTC)

<p>Thanks a lot for the great feedback. I will forward it to the VTK experts in charge of volumetric rendering to open the discussion.</p>
<p>Adding support for RGBA volumes and improving the robustness in Slicer and Paraview are additional topics that can probably be handled without too much effort.</p>
<p>Regarding SSAO, a very simple example adding a volume and a SSAO pass result in OpenGL errors because of incorrect FBO bindings. This would have to be investigated further, but besides that the required information (normals and positions) is already available in the existing shader. A few days are probably needed to get a POC.</p>

---

## Post #18 by @lassoan (2023-10-10 16:38 UTC)

<aside class="quote no-group" data-username="LucasGandel" data-post="17" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucasgandel/48/18202_2.png" class="avatar"> LucasGandel:</div>
<blockquote>
<p>Regarding SSAO, a very simple example adding a volume and a SSAO pass result in OpenGL errors because of incorrect FBO bindings. This would have to be investigated further, but besides that the required information (normals and positions) is already available in the existing shader. A few days are probably needed to get a POC.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lucasgandel">@LucasGandel</a> is this something that you or someone from Kitware would look into in the near future?</p>
<p><a class="mention" href="/u/drouin-simon">@drouin-simon</a> Do you think one of your students could explore this? It seems that it may not be a lot of work and could have a huge impact (fast volume rendering with much improved depth perception).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>looks like this didn’t make it into today’s preview build, neither in Linux nor in Windows. I am very excited to give it a try</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I’ll try to get all the necessary pieces merged today so that you can start playing with it from tomorrow.</p>

---

## Post #19 by @LucasGandel (2023-10-11 05:15 UTC)

<blockquote>
<p><a class="mention" href="/u/lucasgandel">@LucasGandel</a> is this something that you or someone from Kitware would look into in the near future?</p>
</blockquote>
<p>I don’t think I’ll manage to find funding/time for this in the near future unfortunately, but I’m happy to answer technical questions. I agree it is worth giving it a try as the effort seems reasonable and it might just work.<br>
The bigger part is probably to solve the current FBO binding issue while adding multiple render target support to the GPU volume mapper. Then writing the position and normal when the <a href="https://gitlab.kitware.com/vtk/vtk/-/blob/master/Rendering/VolumeOpenGL2/vtkVolumeShaderComposer.h?ref_type=heads" rel="noopener nofollow ugc">opacity threshold is reached</a> is probably a good start.</p>

---

## Post #20 by @muratmaga (2023-10-11 15:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I’ll try to get all the necessary pieces merged today so that you can start playing with it from tomorrow.</p>
</blockquote>
</aside>
<p>I just tried and got this error message with these settings:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f231449950652facaadc90df59d2a0e8babee625.png" data-download-href="/uploads/short-url/yyx6rGhEGIo7PQEuaGAsWibXIKV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f231449950652facaadc90df59d2a0e8babee625_2_690x370.png" alt="image" data-base62-sha1="yyx6rGhEGIo7PQEuaGAsWibXIKV" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f231449950652facaadc90df59d2a0e8babee625_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f231449950652facaadc90df59d2a0e8babee625_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f231449950652facaadc90df59d2a0e8babee625_2_1380x740.png 2x" data-dominant-color="8C8C90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2314×1244 429 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am using data from <a href="https://github.com/muratmaga/mouse_CT_atlas" class="inline-onebox">GitHub - muratmaga/mouse_CT_atlas: Analytical pipeline for skull shape analysis in adult mice</a> (the contents of template folder).</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Users/amaga/Desktop/SlicerPreview.app/Contents/bin/Python/slicer/util.py", line 3146, in tryWithErrorDisplay
    yield
  File "/Users/amaga/Desktop/SlicerPreview.app/Contents/Extensions-32228/Sandbox/lib/Slicer-5.5/qt-scripted-modules/ColorizeVolume.py", line 229, in onApplyButton
    self.logic.process(
  File "/Users/amaga/Desktop/SlicerPreview.app/Contents/Extensions-32228/Sandbox/lib/Slicer-5.5/qt-scripted-modules/ColorizeVolume.py", line 348, in process
    dilate.SetKernelSize(dilationKernelSize, dilationKernelSize, dilationKernelSize)
NameError: name 'dilationKernelSize' is not defined
</code></pre>

---

## Post #21 by @pieper (2023-10-11 16:47 UTC)

<p>Looks like that variable didn’t get set.  Probably it needs to be exposed in the UI.  For now you can just comment out this line (put <code>#</code> at the front) in /Users/amaga/Desktop/SlicerPreview.app/Contents/Extensions-32228/Sandbox/lib/Slicer-5.5/qt-scripted-modules/ColorizeVolume.py", line 348. or set the variable manually.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/master/ColorizeVolume/ColorizeVolume.py#L348">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ColorizeVolume/ColorizeVolume.py#L348" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/master/ColorizeVolume/ColorizeVolume.py#L348" target="_blank" rel="noopener">PerkLab/SlicerSandbox/blob/master/ColorizeVolume/ColorizeVolume.py#L348</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="338" style="counter-reset: li-counter 337 ;">
          <li>    segment = segmentationNode.GetSegmentation().GetSegment(segmentId)</li>
          <li>    color = segment.GetColor()</li>
          <li>    opacity = segmentationNode.GetDisplayNode().GetSegmentOpacity3D(segmentId)</li>
          <li>    colorTableNode.SetColor(segmentIndex + 1, *color, opacity)</li>
          <li></li>
          <li># Dilate labelmap to avoid edge artifacts</li>
          <li>slicer.util.showStatusMessage(f"Dilating segments...")</li>
          <li>slicer.app.processEvents()</li>
          <li>dilate = vtk.vtkImageMedian3D()</li>
          <li>dilate.SetInputData(labelmapVolumeNode.GetImageData())</li>
          <li class="selected">dilate.SetKernelSize(dilationKernelSize, dilationKernelSize, dilationKernelSize)</li>
          <li>dilate.SetIgnoreBackground(False)  # ignoring background turns makes median filter dilate label values</li>
          <li>dilate.SetBackgroundValue(0)</li>
          <li>dilate.Update()</li>
          <li>labelImage = dilate.GetOutput()</li>
          <li></li>
          <li>slicer.util.showStatusMessage(f"Generating colorized volume...")</li>
          <li>slicer.app.processEvents()</li>
          <li></li>
          <li>mapToRGB = vtk.vtkImageMapToColors()</li>
          <li>mapToRGB.ReleaseDataFlagOn()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #22 by @muratmaga (2023-10-11 17:02 UTC)

<p>OMG! This is a game changer for us.</p>
<p>We just now a way to adjust TF per segment basis somehow… And regular shadows/lights work great, just need the ambient shadows as <a class="mention" href="/u/lassoan">@lassoan</a> mentioned.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c5a532f77905930b10be6ff74d8539992e8f41f.jpeg" data-download-href="/uploads/short-url/fsx5oPUeuKWjMlnEJT2FAT5MqlN.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5a532f77905930b10be6ff74d8539992e8f41f_2_690x439.jpeg" alt="image" data-base62-sha1="fsx5oPUeuKWjMlnEJT2FAT5MqlN" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5a532f77905930b10be6ff74d8539992e8f41f_2_690x439.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5a532f77905930b10be6ff74d8539992e8f41f_2_1035x658.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/c/6c5a532f77905930b10be6ff74d8539992e8f41f_2_1380x878.jpeg 2x" data-dominant-color="34392C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1710×1090 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @pieper (2023-10-11 17:06 UTC)

<p>gorgeous image!  Keep 'em coming.</p>

---

## Post #24 by @lassoan (2023-10-11 17:11 UTC)

<p>I’m making some changes/fixes. You’ll get even better results! Just need an hour or so.</p>

---

## Post #25 by @lassoan (2023-10-11 22:37 UTC)

<p>It’s all ready. You can update manually from github or download the Slicer Preview Release tomorrow to get the updated version.</p>
<p>Example renderings:</p>
<p>Default rendering:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6ab346a328e725ba3fe8b4f1b95f5c1d186cc27.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6ab346a328e725ba3fe8b4f1b95f5c1d186cc27.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6ab346a328e725ba3fe8b4f1b95f5c1d186cc27.mp4</a>
    </video>
  </div><p></p>
<p>Using gradient opacity:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a318ef6ec27092d0732ca3ef376bc9096c23534.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a318ef6ec27092d0732ca3ef376bc9096c23534.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a318ef6ec27092d0732ca3ef376bc9096c23534.mp4</a>
    </video>
  </div><p></p>

---

## Post #27 by @muratmaga (2023-10-11 23:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It’s all ready. You can update manually from github or download the Slicer Preview Release tomorrow to get the updated version.</p>
</blockquote>
</aside>
<p>I am now working home with remote connection to lab server, and while it works with CPU rendering, I am getting bad memory allocation with GPU rendering.</p>
<p>This is probably an issue with virtualGL. However, when I invoke slicer without vgl, I still get the error with GPU rendering (which should use the software renderer).  Tomorrow, when I back I will try with windows and report back.</p>
<p>`<br>
"Slicer has caught an application error, please save your work and restart.</p>
<p>The application has run out of memory. Increasing swap size in system settings or adding more RAM may fix this issue. f you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org">https://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: std::bad_alloc"<br>
`</p>

---

## Post #28 by @lassoan (2023-10-11 23:21 UTC)

<p>You can crop&amp;resample the volume if you run out of memory. Or, as suggested, increase the swap size.</p>
<p>We use a couple of temporary buffers during computation that we release when the processing is completed. We can tune the code a bit to delete the buffers immediately when they are no longer needed. Let me know what line fails (you can run the module in a debugger or add logs to get the location).</p>

---

## Post #29 by @muratmaga (2023-10-11 23:51 UTC)

<p>I dont think out of memory is real (it is working off a gpu with 48gb and all iof which is available) and system has hundreds of gigs available.</p>

---

## Post #30 by @lassoan (2023-10-12 01:01 UTC)

<p>GPU RAM should be fine. "The application has run out of memory…“ popup means that a memory allocation failed due to not enough CPU RAM / swap size configured in the OS. To confirm that you run out of memory, please crop&amp;resample the input image. You can also send me the image and I can test it for you.</p>

---

## Post #31 by @muratmaga (2023-10-12 01:40 UTC)

<p>It doesn’t run out of memory during other datasets (that are much bigger). But anyways, if you like to try on your own I am using the files starting with 35_mic</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/muratmaga/mouse_CT_atlas/tree/master/data/templates">
  <header class="source">

      <a href="https://github.com/muratmaga/mouse_CT_atlas/tree/master/data/templates" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/muratmaga/mouse_CT_atlas/tree/master/data/templates" target="_blank" rel="noopener nofollow ugc"></a></h3>

  <p><a href="https://github.com/muratmaga/mouse_CT_atlas/tree/master/data/templates" target="_blank" rel="noopener nofollow ugc">//github.com/muratmaga/mouse_CT_atlas/tree/master/data/templates</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #32 by @lassoan (2023-10-12 02:21 UTC)

<p>I don’t see any problems with this mouse template on my computer. It is quite small, loads and renders quickly:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ce4368d60da5c96be446bbaa63005e68c0e14b.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ce4368d60da5c96be446bbaa63005e68c0e14b.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ce4368d60da5c96be446bbaa63005e68c0e14b.mp4</a>
    </video>
  </div><p></p>

---

## Post #33 by @muratmaga (2023-10-12 02:30 UTC)

<p>Yes, it works fine on my Mac too (that’s why I think it has smoething to do with remote connection or the virtualgl). Curious that your exported color volume doesn’t also show the brain endocast. When i redid a second time, that’s when it became visible…</p>

---

## Post #34 by @lassoan (2023-10-12 03:00 UTC)

<p>The endocast is air, and even if you color the region by the segmentation, it will still remain empty and will not show up (the boundary may be somewhat visible due to the edge smoothing). To display the endocast you can use “Mask volume” effect to virtually fill it with water or some other material.</p>

---

## Post #35 by @Deep_Learning (2023-10-12 15:39 UTC)

<p>Unreal…  I am having better/awesome experience with windows.  Ubuntu, I am getting the alloc error.</p>

---

## Post #36 by @muratmaga (2023-10-12 15:51 UTC)

<p>Yes, I think the out of memory error with vtkGPURaycasting is real. I am getting it even with mrhead simply when I am using GPURaycasting on vanialla data (no colorization or anything (with or without vgl).</p>
<p>Probably better to post this on the GH issues though.</p>

---

## Post #37 by @muratmaga (2023-10-13 04:43 UTC)

<p>I opened a bug report on Slicer repo, because I can reproduce the behavior without installing any extension. See</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/7281">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/7281" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/7281" target="_blank" rel="noopener nofollow ugc">Latest Preview in Linux crashes with GPU rendering </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2023-10-13" data-time="04:42:13" data-timezone="UTC">04:42AM - 13 Oct 23 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/muratmaga" target="_blank" rel="noopener nofollow ugc">
          <img alt="muratmaga" src="https://avatars.githubusercontent.com/u/21285140?v=4" class="onebox-avatar-inline" width="20" height="20">
          muratmaga
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          type:bug
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">1. Download and install the latest preview (I used r32228) for Linux (testing wi<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">th Ubuntu 20 and 22, both on cloud and locally). 
2. obtain MRHead and try to volume rendering with gpu rendering. 

Consistently crashes with bad allocation error. See screenshot above. Doesn't reproduce on windows or mac. 



&lt;img width="1225" alt="image" src="https://github.com/Slicer/Slicer/assets/21285140/daf51f74-60e2-4dea-9aa2-3bc1e579ab7e"&gt;

@lassoan @pieper</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #38 by @Deep_Learning (2023-10-13 12:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bab454a7dfe038e1d9f0fbda1bf8746e065678c5.png" data-download-href="/uploads/short-url/qDFaiWjt2xWr0BEpzAT8CF0d9f7.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bab454a7dfe038e1d9f0fbda1bf8746e065678c5_2_589x500.png" alt="Capture" data-base62-sha1="qDFaiWjt2xWr0BEpzAT8CF0d9f7" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bab454a7dfe038e1d9f0fbda1bf8746e065678c5_2_589x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bab454a7dfe038e1d9f0fbda1bf8746e065678c5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bab454a7dfe038e1d9f0fbda1bf8746e065678c5.png 2x" data-dominant-color="ABA8D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">697×591 346 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any tips on how to iterate over volume and segmentation sequences to create a true volume colored sequence?</p>
<p>I’m not easily impressed, but being able to do this myself with 100% open source software…</p>

---

## Post #39 by @lassoan (2023-10-13 13:50 UTC)

<p>This looks really, really nice!</p>
<p>To make it a sequence, add the colorized volume to the sequence:</p>
<ul>
<li>in Sequences module, click the green <code>+</code> icon to add a new sequence</li>
<li>in the table below set the colorized volume as <code>Proxy node</code></li>
<li>enable <code>Save changes</code></li>
</ul>
<p>After this, you can generate the colorized volume sequence by iterating through the time points of the sequence (manually, using the sequence toolbar) and click <code>Apply</code> for each. Since the colorized volume is assigned to a sequence and you enabled saving, the a new colorized volume is stored for each time point.</p>
<p>You can create an animation video by using Screen Capture module with “sequence” animation mode.</p>
<p>It would be great if you could post the resulting video here.</p>

---

## Post #40 by @Deep_Learning (2023-10-13 14:33 UTC)

<p>I’m sorry, I was not specific enough.</p>
<p>I start with a segmentation sequence and a volume sequence. 20 segmentations and 20 volumes.<br>
Saved as an .mrb.  It’s awesome… drag and drop.</p>
<p>When using Colorize Volume, I have Input volume = Volume Sequence and Input segmentation =Segmentation sequence.  The result is a single colorized volume selected from the sequence browser.  I’m not sure how that exactly happens.</p>
<p>I see two paths:</p>
<ol>
<li>A separate python script to  iterate over n=20 segs and vols.  But my guess is that this would necessitate the creation of the Colorize Volume Widget, setting all options,  …20 times…</li>
<li>Hacking the “Colorize Volume Extension” to “Colorize Volume Sequence Extension”.  The options in the ui would be set once and used.  Create a new sequence and fill it.</li>
</ol>
<p>I think that option <span class="hashtag-raw">#2</span> is the best… just wanted to confirm…it’s a lot of trial and error.  I am now familar with scripting a shape rendered sequence, but this is my first volume render…</p>
<p>Really nice extension!!! Thank you!!!</p>

---

## Post #41 by @lassoan (2023-10-13 15:00 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="40" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>I start with a segmentation sequence and a volume sequence. 20 segmentations and 20 volumes.<br>
Saved as an .mrb. It’s awesome… drag and drop.</p>
</blockquote>
</aside>
<p>After this, use Colorize volume on one time point and then add the created colorized volume to the sequence as I described in my previous post.</p>
<p>If it is acceptable to do two keypresses per time point (Ctrl + Shift + Right-arrow to go to the next frame and Space key to Apply colorization) then there is no need for any programming. If you do this regularly then you can write a tiny Python script that automates these two actions (3-4 lines of code).</p>
<p>If it is commonly needed by other users, too, then we can add an <code>Apply to all time points</code> option to the Colorize volume module that automates these few steps (adding the colorized volume to a sequence + apply colorization for all time points, not just the current one).</p>

---

## Post #42 by @Deep_Learning (2023-10-15 19:12 UTC)

<p>I think that I am done for the week…</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/439dcdb5ea3473c7fe9a43318b4487af735e9cb7.mp4">
  </div><p></p>

---

## Post #43 by @lassoan (2023-10-15 19:54 UTC)

<p>Thanks for sharing, this looks pretty amazing!</p>

---

## Post #44 by @jcfr (2023-10-17 19:55 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="37" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I opened a bug report on Slicer repo, because I can reproduce the behavior without installing any extension. See <a href="https://github.com/Slicer/Slicer/issues/7281">Slicer#7281</a></p>
</blockquote>
</aside>
<p>A fix has been implemented in the following pull request and will be integrated shortly. See <a href="https://github.com/Slicer/VTK/pull/45">https://github.com/Slicer/VTK/pull/45</a></p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a> For convenience, you may download the library <code>libvtkOpenGL-9.2.so.9.2</code> from <a href="https://drive.google.com/drive/u/0/folders/1jA8q49-CVKlb0x50rJh4zwsS31JieRac">this folder</a> and replace the one found in the install folder associated with <code>Slicer-5.5.0-2023-10-16-linux-amd64</code>.</p>
<p>This should allow to easily confirm everything work as excepted.</p>

---

## Post #45 by @jcfr (2023-10-17 21:08 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>
<p>And here is the corresponding Slicer fix ready for review. See <a href="https://github.com/Slicer/Slicer/pull/7286">https://github.com/Slicer/Slicer/pull/7286</a></p>

---

## Post #46 by @muratmaga (2023-10-18 15:00 UTC)

<p>Can confirm the preview build is now functional for volume rendering in linux. Thanks everyone.</p>

---

## Post #47 by @Deep_Learning (2023-10-18 15:42 UTC)

<p>Also can confirm that it is now working. regex lol…</p>
<p>Is there a good reason why the first and last points in the volume rendering opacity transfer curves can only be dragged right left and not up down?</p>

---

## Post #48 by @muratmaga (2023-10-18 15:50 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="47" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>why the first and last points i</p>
</blockquote>
</aside>
<p>You can i think, but through the interface it is clunky. use the opacity button and either type in the value or use the up/down arrows.</p>

---

## Post #49 by @Deep_Learning (2023-10-18 15:54 UTC)

<p>Yes you can select the last point and then change its value using the spinner.  I always want to change the last value to 1.   Wondering if this on purpose.  Paraview has a similar interface and I believe that the first and last values can be moved up and down with the mouse.</p>

---

## Post #50 by @mhalle (2023-10-18 16:19 UTC)

<p>Lovely renderings.</p>
<p>A few things come to mind. The nice thing about this kind of technique is that there’s a cleaner break between medical data (the CT data) and graphical primitives (colored regions and volumetric detail) than in strict volume rendering.</p>
<p>In volume rendering, graphics and segmentation are all kind of smushed together. When we have good segmentation algorithms, we should use them instead of counting on the soft thresholding of scalars and gradients that volume rendering provide.</p>
<p>This technique allows us to push volumetric-like graphical properties into segmented scenes.  And it looks great.</p>
<p>Some possible extensions:</p>
<ul>
<li>
<p>instead of using CT, any scalar volume could be used. This could, for instance, but a synthetic volume computed from anything (like from multi-channel MR corrected for field inhomogeneities)</p>
</li>
<li>
<p>surface detail such as texture on bone might be able to be captured back into normal maps or bump maps for the surface segmentation.</p>
</li>
<li>
<p>It would be interesting to have a rendering model with a final 3D representation that was simpler than a full-blown volume rendering model that could be recolored but still look lovely. 3D point clouds and Gaussian splatting come to mind, with the colorizing of the points deferred until final 3D to 2D rendering.</p>
</li>
</ul>

---

## Post #51 by @Deep_Learning (2023-10-25 20:32 UTC)

<p>A few questions:</p>
<p>— When using Lights. How does one reset?<br>
— I’m having some trouble reproducing Colorize Volume runs.  If I edit a segmentation or change the visible segments,the sliders “change”.  After more than one run, the necessary threshold value becomes very small (~1%).  Especially when there are more than one Colorized Volumes.</p>
<p>I think that this is an issue with repeatedly  colorizing to the same volume.  My work around is to colorize to a new volume and the sliders are reset.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e83181127c2fa1695c3f27c1ca1c5eba80a8a79.png" alt="image" data-base62-sha1="du5Kupyokzp4WpjrcHs84cNJdS9" width="680" height="424"></p>

---

## Post #52 by @lassoan (2023-10-26 01:19 UTC)

<aside class="quote no-group" data-username="mhalle" data-post="50" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>instead of using CT, any scalar volume could be used</p>
</blockquote>
</aside>
<p>We can use any imaging modality, as the background opacity is automatically reduced (you can choose by how much). It would be nice if someone could post rendering of some segmented MRIs.</p>
<aside class="quote no-group" data-username="mhalle" data-post="50" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>surface detail such as texture on bone might be able to be captured back into normal maps or bump maps for the surface segmentation</p>
</blockquote>
</aside>
<p>I agree, this could be a nice improvement on the state of the art surface rendering using fake textures (designers download some textures and normal/bump maps and apply it on the models to make them look more “realistic”).</p>
<p>Volume rendering is still better in that you can see through thick semi-transparent objects, but I admit that usually it is not necessary to see very deeply inside or through objects.</p>
<p>Somewhat related work is that we can now use the depth buffer to improve lighting in volume rendering - see <a href="https://discourse.slicer.org/t/screen-space-ambient-occlusion-for-volume-rendering/32323/26" class="inline-onebox">Screen-space ambient occlusion for volume rendering - #26 by lassoan</a>. This depth information could be captured in a bump map.</p>
<aside class="quote no-group" data-username="mhalle" data-post="50" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>It would be interesting to have a rendering model with a final 3D representation that was simpler than a full-blown volume rendering model that could be recolored but still look lovely. 3D point clouds and Gaussian splatting come to mind, with the colorizing of the points deferred until final 3D to 2D rendering.</p>
</blockquote>
</aside>
<p>Interesting. Are point clouds or Gaussian splatting faster or simpler to do on current GPU hardware than raycasting?</p>
<aside class="quote no-group" data-username="Deep_Learning" data-post="51" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>When using Lights. How does one reset?</p>
</blockquote>
</aside>
<p>Click <code>Default</code> for lighting, disable ambient shadows, and click <code>None</code> for image-based lighting. That said, there might be some things that we don’t reset exactly - that’s why Lights module is still in the sandbox. We’ll move features into Slicer core as we understand what features are useful enough and what is the best way to use them.</p>
<aside class="quote no-group quote-modified" data-username="Deep_Learning" data-post="51" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>If I edit a segmentation or change the visible segments,the sliders “change”<br>
…<br>
I think that this is an issue with repeatedly colorizing to the same volume. My work around is to colorize to a new volume and the sliders are reset.</p>
</blockquote>
</aside>
<p>If you mean that you choose a different volume for output than your input volume then that is not a workaround but that is how the module is intended to be used. If you use a different input and output volume and you still see some drift then take a screen capture video (or take a screenshot and describe every click you make).</p>
<p>Your coronary rendering looks very nice!</p>

---

## Post #53 by @lassoan (2023-10-26 01:22 UTC)

<p>To everyone who is following this topic but may have missed the other topic about ambient shadows: check it out <a href="https://discourse.slicer.org/t/screen-space-ambient-occlusion-for-volume-rendering/32323/26">here</a>.</p>
<p>                    <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33eede8d3e6d6f913adf32a7698b598e4aa7a7f.jpeg" target="_blank" rel="noopener" class="onebox">
            <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f33eede8d3e6d6f913adf32a7698b598e4aa7a7f.jpeg" width="690" height="277">
          </a>

</p>
<p>It should be available in the Slicer Preview Release soon (hopefully within a couple of days).</p>

---

## Post #54 by @Deep_Learning (2023-10-26 13:49 UTC)

<p>When I go into Lights and select View1.<br>
There is an immediate change.<br>
As you say, this is Default, …</p>
<p>Is there a way to get back to the state before I activated the Lights Module?  Not sure if that is the intended behavior?</p>
<p>Alsi, I’m not sure if one needs to turn off the “Sand Box Light” or “Default” is not the ““Default””.</p>

---

## Post #55 by @lassoan (2023-10-27 19:19 UTC)

<p>Modules in Sandbox extension are experimental, for making features available for early testing before the final feature is developed and integrated into Slicer core. When we implement lighting editing feature in Slicer core then we’ll always explicitly set the lights and provide saving/restoring of light configurations. However, we will not implement these in the Sandbox.</p>
<p>The changes in lights are not persistent, so if you want to reset to the VTK default then you can save the scene, restart Slicer, and load the scene. If you frequently want to go back to the default VTK lighting then you can check in VTK where the default light is placed and add lighting preset button corresponding to that. I guess it is just a single head light. You should be able to find it in the VTK source code or ask on the VTK forum.</p>

---

## Post #56 by @mau_igna_06 (2024-09-02 19:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="52" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I agree, this could be a nice improvement on the state of the art surface rendering using fake textures (designers download some textures and normal/bump maps and apply it on the models to make them look more “realistic”).</p>
</blockquote>
</aside>
<p>Is it possible to apply normal maps to 3D models? I’d like to use it for bone models to make them look more realistic</p>
<p>I’ve seen this method (<a href="https://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#ae02934ab1458a6162afe23cd33e00fe0" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkMRMLDisplayNode Class Reference</a>) exists but probably is for color textures not normal textures</p>

---

## Post #57 by @lassoan (2024-09-02 20:18 UTC)

<p>You can access the VTK actors and set normal texture (and base color texture, ORM texture, anisotropy texture, emissive texture, coat normal texture, etc.). If you find it useful then you could add a pull request that exposes additional textures via the MRML node API.</p>

---

## Post #58 by @mau_igna_06 (2024-09-03 17:39 UTC)

<p>I’d like to achieve something like this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="icGJeQ2H7FU" data-video-title="VTK Custom Shader - phong+normalmap" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=icGJeQ2H7FU" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/icGJeQ2H7FU/maxresdefault.jpg" title="VTK Custom Shader - phong+normalmap" width="690" height="388">
  </a>
</div>

<p>This did not work for me:</p>
<pre><code class="lang-auto">modelNode = slicer.util.getNode("tibia")

threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
modelDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName("vtkMRMLModelDisplayableManager")
actor=modelDisplayableManager.GetActorByID(modelNode.GetDisplayNode().GetID())
property=actor.GetProperty()
property.SetInterpolationToPBR()
property.SetMetallic(0.5)
property.SetRoughness(0.5)
property.SetColor(0.5,0.5,0.9)

import os
normalMapPath = os.path.join(downloadPath,'normalMap.png')
normalTexReader = vtk.vtkPNGReader()
normalTexReader.SetFileName(normalMapPath)

normalTex = vtk.vtkTexture()
normalTex.InterpolateOn()
normalTex.SetInputConnection(normalTexReader.GetOutputPort())
normalTex.Update()

property.SetNormalTexture(normalTex);

slicer.util.forceRenderAllViews()
</code></pre>

---

## Post #59 by @lassoan (2024-09-03 18:04 UTC)

<p>You need to enable image-based lighting and maybe set up some more complex light set than the default single light.</p>
<p>Also make sure to add texture coordinates. You can start from a VTK example to make sure you don’t miss anything important.</p>

---

## Post #60 by @mau_igna_06 (2024-09-03 22:00 UTC)

<p>As far as I understood with my search today, I’ll never be able to use normal map textures since the PolyDatas I use are not parametric surfaces and I cannot calculate the uv coordinates.</p>
<p>I got another way to create a tiled like paint effect on the surface using pointScalars. See below</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0e7e739501ec9d51a58e2c8a4677cff7c1b5dba.jpeg" data-download-href="/uploads/short-url/peYSSwGjP2odHnlfARbmnYVIhgC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0e7e739501ec9d51a58e2c8a4677cff7c1b5dba_2_690x272.jpeg" alt="image" data-base62-sha1="peYSSwGjP2odHnlfARbmnYVIhgC" width="690" height="272" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0e7e739501ec9d51a58e2c8a4677cff7c1b5dba_2_690x272.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0e7e739501ec9d51a58e2c8a4677cff7c1b5dba_2_1035x408.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b0e7e739501ec9d51a58e2c8a4677cff7c1b5dba_2_1380x544.jpeg 2x" data-dominant-color="A3A4C7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1716×678 82.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For bones it may be useful enough? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I’m not sure it looks good or not</p>

---

## Post #61 by @lassoan (2024-09-03 22:11 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="60" data-topic="31981">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>never be able to use normal map textures since the PolyDatas I use are not parametric surfaces</p>
</blockquote>
</aside>
<p>VTK has several filters that automatically compute texture coordinates for any polydata. For long bones <a href="https://vtk.org/doc/nightly/html/classvtkTextureMapToCylinder.html">cylindrical mapping</a> should work well.</p>

---
