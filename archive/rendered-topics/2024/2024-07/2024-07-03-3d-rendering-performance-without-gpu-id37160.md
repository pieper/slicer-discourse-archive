---
topic_id: 37160
title: "3D Rendering Performance Without Gpu"
date: 2024-07-03
url: https://discourse.slicer.org/t/37160
---

# 3D rendering performance without GPU

**Topic ID**: 37160
**Date**: 2024-07-03
**URL**: https://discourse.slicer.org/t/3d-rendering-performance-without-gpu/37160

---

## Post #1 by @muratmaga (2024-07-03 00:11 UTC)

<p>I have noticed that when the show 3D is enabled the rendering performance is extremely slow on system without GPU (e.g., CPU only nodes on JetStream).</p>
<p>I wouldn’t be too surprised if the volume rendering of the source volume of the same segmentation didn’t provide decent performance either, but it did. So when volume rendering (in the GPU rendering option, which should be using software rendering) is using about a dozen or more cores, but in the 3D rendering of the segmentation models the utilization is only 200%, meaning it is only using two cores.</p>
<p>Is this normal, is there a trick to make the segmentation rendering as perfomant as the volume rendering on CPU only systems?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @lassoan (2024-07-03 03:47 UTC)

<p>VTK’s CPU volume renderer has very low resource needs, because it was developed decades ago, when CPUs were really weak. It uses special computation tricks that makes rendering fast and memory-efficient. Since it does not use any GPU at all, it is just as fast on a computer with or without GPU.</p>
<p>Rendering of polydata does not use the CPU at all when you just rotate the view around (it may use the CPU a bit when there are more layers, depth sorting, etc.). If there is no graphics hardware then a software OpenGL implementation is used, which simulates a GPU in software, which of course is very inefficient.</p>
<p>If you find that only 1-2 CPU cores are used for surface rendering then you can experiment with options in your software renderer. Maybe threading in your mesa (or other software renderer) is turned off by default.</p>

---

## Post #3 by @muratmaga (2024-07-03 20:23 UTC)

<p>Thanks, I tried adjusting the threading settings on the OS (ubuntu) provided mesa, which had no effect.</p>
<p>I came across this thread from Kitware about OpenSWR being a lot more perfomant for CPU only systems (<a href="https://www.paraview.org/Wiki/ParaView/ParaView_And_Mesa_3D" class="inline-onebox">ParaView/ParaView And Mesa 3D - KitwarePublic</a>).</p>
<p>But it looks like it needs to be built from scratch…</p>

---

## Post #4 by @muratmaga (2024-10-01 06:56 UTC)

<p>Following on this: I managed to build the <a href="https://www.openswr.org/build-linux.html" rel="noopener nofollow ugc">openSWR</a> on a CPU only system (with 16 cores), and run some basic test. I have made large polydata model from MRHead (supersampled it by 0.5 with isotropic scaling).</p>
<p>When using the Ubuntu 22.04 provided mesa, full 3D view swinging performance of Slicer (latest preview version) was &lt;1 fps. It never utilized over 200% of CPUs (so two cores).</p>
<p>With the gallium SWR exposed, performance was about 10fps, utilizing 1400-1500% of the CPU (so 14-15 cores).</p>

---

## Post #5 by @lassoan (2024-10-01 12:04 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>, this is very useful information! Maybe SWR could be bundled with Slicer in standard factory builds (new VTK feature is to allow switching between different OpenGL implementation at runtime).</p>
<p>Could you share the model so that we can test it on other systems for comparison?</p>

---

## Post #6 by @muratmaga (2024-10-01 17:57 UTC)

<p><a href="https://js2.jetstream-cloud.org:8001/swift/v1/SampleData/Segment_1.ply" class="onebox" target="_blank" rel="noopener nofollow ugc">https://js2.jetstream-cloud.org:8001/swift/v1/SampleData/Segment_1.ply</a></p>

---

## Post #7 by @muratmaga (2024-10-02 15:39 UTC)

<p>One more data point: Volume rendering in a system without a GPU is more performant using GPU raycasting (and SWR driver) than using CPU raycasting. Seems to scale much efficiently.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="37160">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe SWR could be bundled with Slicer in standard factory builds (new VTK feature is to allow switching between different OpenGL implementation at runtime).</p>
</blockquote>
</aside>
<p>This would be great. I am not sure how applicable this would be mac and windows, but on Linux (where it is more likely to get deployed on cloud without GPUs) is going to make a difference.</p>

---

## Post #8 by @lassoan (2024-10-02 17:34 UTC)

<p>When you use SWR, does GPU volume renderer has any of the usual GPU hardware limitations, such as limited amount of GPU RAM, maximum texture size, …? Or if you use SWR then GPU volume renderer can work with volumes of practically unlimited size?</p>

---

## Post #9 by @muratmaga (2024-10-02 18:25 UTC)

<p>Yes, it did generate this error with a large volume:</p>
<pre><code class="lang-auto">
Switch to module:  "Data"
Switch to module:  "Volumes"
ctkRangeWidget::setSingleStep( 100 ) is outside valid bounds
Switch to module:  "VolumeRendering"
ERROR: OpenGL MAX_3D_TEXTURE_SIZE is 2048
Invalid texture dimensions [1948, 1948, 2952]
</code></pre>
<p>I wonder if 3D_TEXTURE_SIZE is a property than be adjusted at the build time, or change in the code. I simply followed the instructions on openSWR page.</p>

---

## Post #10 by @muratmaga (2024-10-02 18:27 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="9" data-topic="37160">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><code>OpenGL MAX_3D_TEXTURE_SIZE</code></p>
</blockquote>
</aside>
<p>Sounds it  should be possible to modify this if your building your own driver:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.paraview.org/t/paraview-5-11-0-egl-vs-mesa-invalid-texture-dimensions/13029/6">
  <header class="source">
      <img src="https://discourse.paraview.org/uploads/default/optimized/2X/8/8ca8a3bd08e322918d9c0958f548dec7d0e7cd8d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.paraview.org/t/paraview-5-11-0-egl-vs-mesa-invalid-texture-dimensions/13029/6" target="_blank" rel="noopener nofollow ugc" title="02:22PM - 23 October 2023">ParaView – 23 Oct 23</a>
  </header>

  <article class="onebox-body">
    <img src="https://discourse.paraview.org/uploads/default/original/2X/8/8ca8a3bd08e322918d9c0958f548dec7d0e7cd8d.png" class="thumbnail onebox-avatar" width="500" height="500">

<div class="title-wrapper">
  <h3><a href="https://discourse.paraview.org/t/paraview-5-11-0-egl-vs-mesa-invalid-texture-dimensions/13029/6" target="_blank" rel="noopener nofollow ugc">Paraview 5.11.0 EGL vs Mesa - "Invalid Texture Dimensions"</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #BF1E2E;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">ParaView Support</span>
        </span>
      </span>
  </div>
</div>

  <p>Looks like a limitation of the osmesa driver.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I search for 3D_MAX_TEXTURE in the source tree of mesa, and these are the hits:</p>
<pre><code class="lang-auto">./glext.h:84:#define GL_MAX_3D_TEXTURE_SIZE            0x8073
./glcorearb.h:447:#define GL_MAX_3D_TEXTURE_SIZE            0x8073
./gl.h:1483:#define GL_MAX_3D_TEXTURE_SIZE			0x8073
</code></pre>
<p>though not sure 0x8073 refers to. Doesn’t correspond to 2048 in hexadecimal.</p>

---

## Post #12 by @muratmaga (2024-10-03 04:36 UTC)

<p>Making some more progress: I think this is the place to change the limits on 3D texture dimensions <code>SWR_MAX_TEXTURE_3D_LEVELS</code>:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.freedesktop.org/mesa/mesa/-/blob/21.3/src/gallium/drivers/swr/swr_screen.cpp?ref_type=heads#L58">
  <header class="source">
      <img src="https://gitlab.freedesktop.org/uploads/-/system/appearance/favicon/1/fdo-favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://gitlab.freedesktop.org/mesa/mesa/-/blob/21.3/src/gallium/drivers/swr/swr_screen.cpp?ref_type=heads#L58" target="_blank" rel="noopener nofollow ugc">GitLab</a>
  </header>

  <article class="onebox-body">
    <img width="64" height="64" src="https://gitlab.freedesktop.org/uploads/-/system/project/avatar/176/gears.png" class="thumbnail onebox-avatar">

<h3><a href="https://gitlab.freedesktop.org/mesa/mesa/-/blob/21.3/src/gallium/drivers/swr/swr_screen.cpp?ref_type=heads#L58" target="_blank" rel="noopener nofollow ugc">src/gallium/drivers/swr/swr_screen.cpp · 21.3 · Mesa / mesa · GitLab</a></h3>

  <p>Mesa 3D graphics library</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I changed the value from 12 to 14, assuming it would provide 8K textures size.</p>
<p>This worked up to a point. I can resample the MRhead to 2560x2560x130 (4.7GB) and it does render. At which point the rendering speed is acceptable (i get around 3fps) and much better than CpuRaycasting, which I can’t even move interactively, and also GPU rendering quality is better.</p>
<p>GPU Raycasting:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ceca644e19ec034cf6bd9ed34a29041a61e9e61.jpeg" data-download-href="/uploads/short-url/modvhBL7DDuxUd95sGHXn0X7PAB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ceca644e19ec034cf6bd9ed34a29041a61e9e61_2_690x396.jpeg" alt="image" data-base62-sha1="modvhBL7DDuxUd95sGHXn0X7PAB" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ceca644e19ec034cf6bd9ed34a29041a61e9e61_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ceca644e19ec034cf6bd9ed34a29041a61e9e61_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9ceca644e19ec034cf6bd9ed34a29041a61e9e61_2_1380x792.jpeg 2x" data-dominant-color="B4B1B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1693×973 89.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>CPU Raycasting:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47320037c3a7f3f95c49611f4df186d414d95a3b.jpeg" data-download-href="/uploads/short-url/a9P1EKIeUewxmdnm2IljPvHGEEH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47320037c3a7f3f95c49611f4df186d414d95a3b_2_690x348.jpeg" alt="image" data-base62-sha1="a9P1EKIeUewxmdnm2IljPvHGEEH" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47320037c3a7f3f95c49611f4df186d414d95a3b_2_690x348.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47320037c3a7f3f95c49611f4df186d414d95a3b_2_1035x522.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/47320037c3a7f3f95c49611f4df186d414d95a3b_2_1380x696.jpeg 2x" data-dominant-color="BAB4B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1697×858 77.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, when I go to 2560x2560x270 (~3.8GB) in MRHead, Slicer crashes without an error. This seems related to texture memory limit, more than the dimension, since it works fine when I keep the volume dimensions the same but cast the data type as unsigned char instead of short.</p>
<p>There is also this <code>SWR_MAX_TEXTURE_SIZE </code> setting which seems relevant:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.freedesktop.org/mesa/mesa/-/blob/21.3/src/gallium/drivers/swr/swr_screen.cpp?ref_type=heads#L54">
  <header class="source">
      <img src="https://gitlab.freedesktop.org/uploads/-/system/appearance/favicon/1/fdo-favicon.ico" class="site-icon" width="16" height="16">

      <a href="https://gitlab.freedesktop.org/mesa/mesa/-/blob/21.3/src/gallium/drivers/swr/swr_screen.cpp?ref_type=heads#L54" target="_blank" rel="noopener nofollow ugc">GitLab</a>
  </header>

  <article class="onebox-body">
    <img width="64" height="64" src="https://gitlab.freedesktop.org/uploads/-/system/project/avatar/176/gears.png" class="thumbnail onebox-avatar">

<h3><a href="https://gitlab.freedesktop.org/mesa/mesa/-/blob/21.3/src/gallium/drivers/swr/swr_screen.cpp?ref_type=heads#L54" target="_blank" rel="noopener nofollow ugc">src/gallium/drivers/swr/swr_screen.cpp · 21.3 · Mesa / mesa · GitLab</a></h3>

  <p>Mesa 3D graphics library</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I tried modifying it to be 4096^3, but it still doesn’t seem to make a difference.</p>
<p>This is as far as I can troubleshoot. Someone who know openGL and C++ needs to dig deeper.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #13 by @pieper (2024-10-03 05:08 UTC)

<p>The comment in the code you linked earlier mentions a limit on total size related to the use of signed int and 32 bit offsets (and that the special CPU instructions have a limit) so you may be hitting a wall with this approach.</p>

---
