---
topic_id: 21317
title: "Volumertric Painting Is Possible Or Not"
date: 2022-01-03
url: https://discourse.slicer.org/t/21317
---

# Volumertric painting is possible or not

**Topic ID**: 21317
**Date**: 2022-01-03
**URL**: https://discourse.slicer.org/t/volumertric-painting-is-possible-or-not/21317

---

## Post #1 by @davide445 (2022-01-03 11:24 UTC)

<p>For a project was looking a way to add anatomic structures details (i.e. tissue histology) directly starting from a CT/MR, to be used for education, analysis and simulation using realtime 3d rendering.</p>
<p>In 3d Slicer you can segment your data to extract the different elements, and export them in various formats that can be used for realtime rendering.<br>
I have seen beautiful CR examples such as this one<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/518a44785b6c7a9e086a708bcd518635a99db12e.jpeg" data-download-href="/uploads/short-url/bDkUwRQGKSRWRWrhnkoQNldezDM.jpeg?dl=1" title="" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/518a44785b6c7a9e086a708bcd518635a99db12e_2_440x500.jpeg" alt="" data-base62-sha1="bDkUwRQGKSRWRWrhnkoQNldezDM" role="presentation" width="440" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/518a44785b6c7a9e086a708bcd518635a99db12e_2_440x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/518a44785b6c7a9e086a708bcd518635a99db12e_2_660x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/518a44785b6c7a9e086a708bcd518635a99db12e.jpeg 2x" data-dominant-color="614238"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">661×750 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
that I suspect it’s “just” using the traditional PBR pipeline using surface materials.<br>
Meaning if you cut the model you didn’t find any detail inside.</p>
<p>So far to add volumetric details you can sculpt them as a volume using tools such as Freeform and next provide the volume itself some color. It’s a long process.</p>
<p>A better way will be using some color 3D brushes to paint directly in 3d and export 3D volumetric images.<br>
But searching on I didn’t find any approach like that, for sure might be not so efficient in term of data sizes (volume model + volume textures).</p>
<p>Wanted to ask if someone has better information than me on this topic, to understand if it’s just a bad night idea, or there is some value in it.</p>

---

## Post #2 by @muratmaga (2022-01-03 15:03 UTC)

<aside class="quote no-group" data-username="davide445" data-post="1" data-topic="21317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>A better way will be using some color 3D brushes to paint directly in 3d and export 3D volumetric images.</p>
</blockquote>
</aside>
<p>Segmentation in Slicer is always 3D and volumetric. So instead of exporting your segmentation as models, you can use the MaskVolume feature to export them separate volumes, and then use the volume rendering to assign different transfer functions to each of these volumes. So that’s already doable easily.</p>
<p>Where it gets difficult is the multi-volume rendering in Slicer is not fully implemented (as far as I know). Depending on the view/angle, you will have rendering artifacts and such, but I think the more users request and demand it, more attention it will get.</p>

---

## Post #3 by @davide445 (2022-01-03 15:27 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="21317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Segmentation in Slicer is always 3D and volumetric</p>
</blockquote>
</aside>
<p>Of course. But what about if I want to fill the volume with a tissue (just as example)? Not a single color, but a texture depicting colored details.</p>

---

## Post #4 by @lassoan (2022-01-03 15:41 UTC)

<p>From the cloud-like appearance of minor vessels you can tell that the image above is rendered using volume raycasting or path tracing. There is no surface extraction or segmentation and the same material is used for the entire volume: there is just a color map that makes lower intensity voxels darker red and higher intensity voxels brighter yellow; bones and vessels appear exactly the same, with the same red haze at the boundary due to partial volume effect.</p>
<p>I think the rendering is impressive partly because the image resolution is higher than average and because of the material/lighting model maybe a slightly more sophisticated than just a basic ambient/diffuse/specular reflective model: there seems to be some soft shadows created by screen space ambient occlusion or path tracing.</p>
<p>This is what you can get with a simple volume raycasting in Slicer on slightly lower resolution images:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e17130e9b89c0ca802b584609e63a0828ae69eb3.jpeg" data-download-href="/uploads/short-url/walWntLPYXm7dcja5idJxPx6mgX.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e17130e9b89c0ca802b584609e63a0828ae69eb3_2_690x418.jpeg" alt="image" data-base62-sha1="walWntLPYXm7dcja5idJxPx6mgX" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e17130e9b89c0ca802b584609e63a0828ae69eb3_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e17130e9b89c0ca802b584609e63a0828ae69eb3_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e17130e9b89c0ca802b584609e63a0828ae69eb3_2_1380x836.jpeg 2x" data-dominant-color="7E6E6A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1165 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7dad4f1aa3f6b53d9783c8df10126bf7980a9056.jpeg" data-download-href="/uploads/short-url/hVMZN22TJDcyhfJxUYzs92xmtam.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dad4f1aa3f6b53d9783c8df10126bf7980a9056_2_690x418.jpeg" alt="image" data-base62-sha1="hVMZN22TJDcyhfJxUYzs92xmtam" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dad4f1aa3f6b53d9783c8df10126bf7980a9056_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dad4f1aa3f6b53d9783c8df10126bf7980a9056_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7dad4f1aa3f6b53d9783c8df10126bf7980a9056_2_1380x836.jpeg 2x" data-dominant-color="7C6E6A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1165 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="davide445" data-post="3" data-topic="21317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>what about if I want to fill the volume with a tissue</p>
</blockquote>
</aside>
<p>Volume rendering already displays a “filled” 3D volumetric texture. If you can see this in all the semi-transparent regions or if you cut into it using the crop region.</p>

---

## Post #5 by @davide445 (2022-01-04 11:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> clear enough. In this way you can anyway color the volume only based on a single property the density.<br>
My idea was if there is any standard where I will be able to load painted 3d images, with much more details such as from the longitudinal and cross section of muscle</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://histologyguide.com/slideview/MH-055a-skeletal-muscle/04-slide-1.html?x=6990&amp;y=35509&amp;z=100.0">
  <header class="source">
      <img src="https://histologyguide.com/assets/imgs/favicon.ico" class="site-icon" width="48" height="48">

      <a href="https://histologyguide.com/slideview/MH-055a-skeletal-muscle/04-slide-1.html?x=6990&amp;y=35509&amp;z=100.0" target="_blank" rel="noopener nofollow ugc">histologyguide.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://histologyguide.com/slideview/MH-055a-skeletal-muscle/04-slide-1.html?x=6990&amp;y=35509&amp;z=100.0" target="_blank" rel="noopener nofollow ugc">Skeletal Muscle | Muscle Tissue</a></h3>

  <p>Histology of sarcomeres (A band, I band, H band, and Z band) in skeletal muscle.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2022-01-04 14:36 UTC)

<p>You can volume render an RGB or RGBA volume as well. In this case the provided color and opacity values are used (they are not computed from a single scalar with transfer functions).</p>
<aside class="quote quote-modified" data-post="1" data-topic="19732">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/color-rgb-volume-rendering/19732">Color (RGB) volume rendering</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    In recent Slicer Preview Releases, color volume rendering has been made much easier to access. While previously an alpha channel had to be created manually for rendering color RGB volumes, now the alpha channel is created automatically (from the luminance of the image). 
To render an RGB volume, just load the image stack and drag-and-drop the volume from the Data module to a 3D view (or use Volume Rendering module). When a color volume is loaded then “Scalar Color Mapping” section is not display…
  </blockquote>
</aside>


---

## Post #7 by @davide445 (2022-01-05 08:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> interesting. But if have an idea if there is any tool enabling to actually paint a volume RGB image. Just as example this idea</p><div class="youtube-onebox lazy-video-container" data-video-id="HUW49IKs1kE" data-video-title="Bird Gamayun - Virtual reality painting (Tilt Brush)" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=HUW49IKs1kE" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/HUW49IKs1kE/maxresdefault.jpg" title="Bird Gamayun - Virtual reality painting (Tilt Brush)" width="" height="">
  </a>
</div>
<p>
As far as I know i.e. Freeform it’s not able to paint volume RGB.</p>

---

## Post #8 by @lassoan (2022-03-13 04:53 UTC)

<p>Painting/sculpting segmentations in virtual reality sound like extremely tedious to me (even just holding out your arms for a few minutes takes quite a bit of effort). However, quick review (with grab to move, pinch to zoom) and touch-up (smoothing, filling holes, removing excess) may be useful and we plan to add these features.</p>

---
