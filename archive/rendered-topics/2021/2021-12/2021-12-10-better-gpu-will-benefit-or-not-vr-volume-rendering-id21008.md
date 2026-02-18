# Better GPU will benefit or not VR volume rendering

**Topic ID**: 21008
**Date**: 2021-12-10
**URL**: https://discourse.slicer.org/t/better-gpu-will-benefit-or-not-vr-volume-rendering/21008

---

## Post #1 by @davide445 (2021-12-10 16:31 UTC)

<p>Was testing today VR view using a Vive Cosmos headset, a GTX 1070 GPU, Ryzen 2600X CPU and 64GB RAM.<br>
Works but it’s not really fluid, a bit of nauseating shutters.<br>
Tried to change various setting but didn’t find better performance maintaining the same visual quality.<br>
Since the GPU was just 50% busy wanted to ask if with a more recent and powerful (was thing a RX 6800XT) will really improve things.</p>

---

## Post #2 by @lassoan (2021-12-10 16:41 UTC)

<p>You can tune volume rendering quality settings in SlicerVirtualReality module settings to ensure that volume rendering updates are fast enough (using any GPU) while the head is moving, of course at the cost temporarily lowering the image quality .</p>
<p>A significantly better GPU is expected to provide significantly better rendering speed for volume rendering, so if the dynamic quality adjustment does not give you satisfactory results then it may make sense to upgrade. In general I would recommend NVidia GeForce GPUs for volume rendering (NVidia for software compatibility and driver quality; and GeForce series for cost effectiveness and software compatibility).</p>

---

## Post #3 by @davide445 (2021-12-10 18:05 UTC)

<p>The fact my 1070 was not saturated was wondering me, or a faster GPU will be anyway get better results even if not saturated.<br>
Also I’m not using very big models, having total VRAM&gt;model size will allow better compatibility with AMD GPUs.<br>
I tend to prefer AMD hw for next rig due better price/performance (6900 XT at €1700 vs 3090 at €3700 here).</p>

---

## Post #4 by @lassoan (2021-12-10 18:53 UTC)

<aside class="quote no-group" data-username="davide445" data-post="3" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>Also I’m not using very big models,</p>
</blockquote>
</aside>
<p>Do you have performance issues with visualizing models or volumes?</p>
<p>If you visualize volumes, what is the volume size in voxels?</p>
<aside class="quote no-group" data-username="davide445" data-post="3" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>I tend to prefer AMD hw for next rig due better price/performance (6900 XT at €1700 vs 3090 at €3700 here).</p>
</blockquote>
</aside>
<p>With an AMD GPU there is a higher chance that you will run into problems, but it could be a good option if you are willing to take the risk and/or you are ready to do some low-level OpenGL debugging and contribute fixes to VTK.</p>

---

## Post #5 by @davide445 (2021-12-10 20:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you visualize volumes, what is the volume size in voxels?</p>
</blockquote>
</aside>
<p>I visualize volumes, testing on ircad 12, 512x512x260</p>
<p>Not able to debug OpenGL, reading the issues was having the impression AMD has problems in case of big volumes using a lot of VRAM or using Adaptive quality.</p>

---

## Post #6 by @lassoan (2021-12-10 20:10 UTC)

<p>It is not a small volume, so it is not surprising that a several-year-old GPU struggles to render it at full resolution in stereo at 60fps.</p>
<p>Most “large volume” rendering issues start at texture sizes above 512, so probably you would not run into them even if you use an AMD GPU.</p>

---

## Post #7 by @davide445 (2021-12-10 20:29 UTC)

<p>Not an expert but 16 bit grayscale is meaning 68MB image… Not that much to me. Wrong calculations probably.</p>

---

## Post #8 by @Hao_Li (2021-12-10 20:32 UTC)

<p>Buy 3090. I bought 6900XT and regret very hard =).<br>
I ran into data sets I can visualize with volume rendering on 1070, but not 6900XT <img src="https://emoji.discourse-cdn.com/twitter/dizzy_face.png?v=10" title=":dizzy_face:" class="emoji" alt=":dizzy_face:"> and some other data sets vice versa. 3090 opened them all.</p>

---

## Post #9 by @davide445 (2021-12-10 20:57 UTC)

<p>But there is some rule? Getting problems only with big files, or using Adaptive resolution, or simply not track able to any specific feature so is not predictable.</p>

---

## Post #10 by @Hao_Li (2021-12-10 21:33 UTC)

<p>I find it unpredictable.<br>
I have a file with size around 4Gb I cannot volume render at all with 6900XT, but works fine with 1070 or CPU. I also have a file at 11Gb, which I can volume render with 6900XT but it shows wrong stiched. The 11Gb file can not be volume rendered using 1070.<br>
Volume rendering 11Gb file, the speed is slow when using Adaptive resolution with 3090.</p>

---

## Post #11 by @muratmaga (2021-12-10 23:57 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="10" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>Volume rendering 11Gb file, the speed is slow when using Adaptive resolution with 3090.</p>
</blockquote>
</aside>
<p>If you have 3090, you really shouldn’t need to use Adaptive. Normal should give you better performance. Another thing to check is to see if you are really set to use the discrete GPU to for 3D rendering (In case your CPU has an internal GPU as well). In windows 10 this is handled by the Graphics Settings hardware-accelerated GPU scheduling. Make sure SlicerrealApp.exe is chosen to use the 3090.</p>

---

## Post #12 by @davide445 (2021-12-11 06:27 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="10" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>I have a file with size around 4Gb I cannot volume render at all with 6900XT</p>
</blockquote>
</aside>
<p>You mean 4GB on the file system, or in VRAM (how you check it?). As example I’m testing using also the <a href="https://www.ircad.fr/softwares/3Dircadb/3Dircadb1/3Dircadb1.12.zip" rel="noopener nofollow ugc">Ircadb 1.12</a> image if you have time to have a test on it.</p>

---

## Post #13 by @chir.set (2021-12-11 08:11 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="10" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>I have a file with size around 4Gb I cannot volume render at all with 6900XT</p>
</blockquote>
</aside>
<p>Do you mean volume rendering without virtual reality?<br>
Is it possible to post an anonymized copy of this volume ? I’m eager to test it with my 6700XT without virtual reality.</p>

---

## Post #14 by @Hao_Li (2021-12-11 08:21 UTC)

<p>I’ll check on Monday on the Ircadb file. The file size is 4Gb, I don’t know VRAM.</p>

---

## Post #15 by @Hao_Li (2021-12-11 08:34 UTC)

<p>Hi! Yes, I’m volume rendering without virtual reality. 6900XT is not very predictable in my hands, I’m not handy at all though. The specific data belongs to other people, I’ll try to find similar data which belongs to me and send to you.</p>

---

## Post #16 by @davide445 (2021-12-11 09:48 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="14" data-topic="21008" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>I’ll check on Monday on the Ircadb file. The file size is 4Gb, I don’t know VRAM.</p>
</blockquote>
</aside>
<p>Thanks. Btw you are on Windows or Linux.</p>

---

## Post #17 by @Hao_Li (2021-12-11 09:52 UTC)

<p>I’m on windows 10. Maybe windows operative system comes into play as well…</p>

---

## Post #18 by @davide445 (2021-12-12 02:01 UTC)

<p>Discovered this opened issue on VTK</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/-/issues/17969">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/favicon.ico" class="site-icon" width="16" height="21">

      <a href="https://gitlab.kitware.com/vtk/vtk/-/issues/17969" target="_blank" rel="noopener nofollow ugc">GitLab</a>
  </header>

  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar" width="146" height="146">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/-/issues/17969" target="_blank" rel="noopener nofollow ugc">Volume rendering issue with volumes bigger 4GB using AMD GPU (#17969) · Issues...</a></h3>

  <p>I just found a strange behavoir when was using a Radeon VII to render a bigger volume (volume bigger 4GB). It seems the volume is cutted into segments...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
No assignee after one year, just a pity 20% of the market is ignored (considering i.e. all the Apple have AMD GPU).<br>
Also seems AMD subpar OpenGL support (and essentially switching their effort on Vulkan) play a role, not good for VTK due a migration to Vulkan seems not to be happening fast</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://discourse.vtk.org/t/vulkan-development/3307/23">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/vulkan-development/3307/23" target="_blank" rel="noopener nofollow ugc" title="12:33PM - 17 August 2021">VTK – 17 Aug 21</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<h3><a href="https://discourse.vtk.org/t/vulkan-development/3307/23" target="_blank" rel="noopener nofollow ugc">Vulkan Development</a></h3>

  <p>As an FYI, we just got a user report that a Mac running Big Sur (Mac OS 11.4) on the Apple M1 core does not have OpenGL installed. What is the priority for getting VTK working on new Macs?</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Was reading a post where AMD states his Windows OpenGL drivers are “workstation” drivers, so will be curios to know if there is someone able to test on AMD workstation GPU to check if the problems are still there.<br>
Anyway interersted to know if we can track down the limitations on AMD GPUs to lower than 4GB files.</p>

---

## Post #19 by @Hao_Li (2021-12-13 08:51 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="14" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>Ircadb file</p>
</blockquote>
</aside>
<p>Hi! I have tried the Ircadb files. Patient CT and VTKs. I used 6900XT, it runs very smoothly. I used normal, adaptive and maximum methods, all three ran smoothly. I tried same files in 3090, there is no difference.</p>

---

## Post #20 by @davide445 (2021-12-13 15:44 UTC)

<p>Will be possible for you to test on this file</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/c818812292a259d64e948800322b982720211213153930/95ef7c">
  <header class="source">
      <img src="https://prod-cdn.wetransfer.net/packs/media/images/favicon-a34a7465.ico" class="site-icon" width="64" height="64">

      <a href="https://wetransfer.com/downloads/c818812292a259d64e948800322b982720211213153930/95ef7c" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://prod-cdn.wetransfer.net/packs/media/images/wt-facebook-9db47080.png" class="thumbnail onebox-avatar" width="200" height="200">

<h3><a href="https://wetransfer.com/downloads/c818812292a259d64e948800322b982720211213153930/95ef7c" target="_blank" rel="noopener nofollow ugc">eyeglobe-overview.rar</a></h3>

  <p>1 file sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
This time a 1004x1024x1018 volume, 2GB size.</p>

---

## Post #21 by @chir.set (2021-12-14 08:29 UTC)

<p>That’s all I can get in Volume Rendering with your eyeglobe data using a 6700XT on Linux.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d0a8913247a913f07116882dfd69c80fcfbecb7.png" data-download-href="/uploads/short-url/k7HTw1orEgJoOIoyUMEMz26Zb6v.png?dl=1" title="unusable" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0a8913247a913f07116882dfd69c80fcfbecb7_2_480x500.png" alt="unusable" data-base62-sha1="k7HTw1orEgJoOIoyUMEMz26Zb6v" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d0a8913247a913f07116882dfd69c80fcfbecb7_2_480x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d0a8913247a913f07116882dfd69c80fcfbecb7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d0a8913247a913f07116882dfd69c80fcfbecb7.png 2x" data-dominant-color="5E5D5B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">unusable</span><span class="informations">605×630 177 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Unusable.</p>

---

## Post #22 by @chir.set (2021-12-14 09:58 UTC)

<p>This is after rescaling the intensity range from 0 to 5000.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ad9f370e7f7f0a1b3ad40767c7b6520ed46f1a8.jpeg" data-download-href="/uploads/short-url/6750IcbVIBliwU1FGBElXNqvpPy.jpeg?dl=1" title="better" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ad9f370e7f7f0a1b3ad40767c7b6520ed46f1a8.jpeg" alt="better" data-base62-sha1="6750IcbVIBliwU1FGBElXNqvpPy" width="580" height="500" data-dominant-color="594834"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">better</span><span class="informations">726×625 69.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #23 by @Hao_Li (2021-12-14 12:36 UTC)

<p>I managed to replace 6900XT today with 3090 … Volume rendering the eye, 3090 appears to be stable at normal quality. Using adaptive quality, 3090 works at about 80-90% when rotating non-stop in 3D view, a little laggy when making sudden rotations. At maximum quality, slicer just closes. In windows.</p>

---

## Post #24 by @lassoan (2021-12-14 13:39 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="23" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>At maximum quality, slicer just closes. In windows</p>
</blockquote>
</aside>
<p>Windows stops applications that use the GPU for too long, exceeding the <a href="https://discourse.slicer.org/t/volume-rendering-causes-application-crash/3783/4">TDR delay</a>. You can increase TDR delay to avoid this, but it would be great if you could test if <a href="https://discourse.slicer.org/t/stitching-artifact-with-volume-rendering-large-volumes-feb-17-2021-nightly/16390/16">setting volume partitions</a> solves this issue, too.</p>
<aside class="quote no-group" data-username="Hao_Li" data-post="23" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>Using adaptive quality, 3090 works at about 80-90% when rotating non-stop in 3D view, a little laggy when making sudden rotations.</p>
</blockquote>
</aside>
<p>At “adaptive” quality setting the renderer measures rendering time and adjusts rendering quality (number of rays, sampling distances, etc.) for the next rendering request to achieve the requested frame rate. This mechanism works very well for CPUs because the computation is very predictable. However, rendering time on GPU can be highly nonlinear and the GPU may perform complex internal optimizations, too, therefore the prediction is often very inaccurate, especially for large volumes. As a result, “adaptive” setting may not work as intended for GPU volume rendering.</p>

---

## Post #25 by @chir.set (2021-12-14 19:27 UTC)

<aside class="quote no-group" data-username="davide445" data-post="20" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>Will be possible for you to test on this file</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="chir.set" data-post="21" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Volume Rendering with your eyeglobe data using a 6700XT on Linux.</p>
</blockquote>
</aside>
<p>Volume rendering with the eyeglobe dataset works equally well with a 5500XT on Linux, with or without intensity resampling.</p>
<p>It’s worthwhile mentioning that it’s good also on my laptop having an AMD Ryzen 5 2500U with integrated Radeon Vega Mobile Gfx video chip, and only 1 GB <em>shared</em> VRAM, using Linux of course.</p>
<p>It seems that if results are near random with a 6900XT on Windows, it would be the video driver’s performance to be questioned. This is quite surprising because AMD gives optimized drivers for Windows first.</p>
<p>All this to say that the Radeon cards are good, with good drivers.</p>

---

## Post #26 by @davide445 (2021-12-14 19:53 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="25" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>It seems that if results are near random with a 6900XT on Windows, it would be the video driver’s performance to be questioned. This is quite surprising because AMD gives optimized drivers for Windows first.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/hao_li">@Hao_Li</a> will be possible for you to check on the 6900 XT</p>

---

## Post #27 by @Hao_Li (2021-12-16 08:30 UTC)

<p>Hi!<br>
I tried the <a href="https://discourse.slicer.org/t/stitching-artifact-with-volume-rendering-large-volumes-feb-17-2021-nightly/16390/16">setting volume partitions</a> method on 3090 opening the eyeglobe data and used 2, 2, 2 and 4, 4, 4. They both negatively affected volume rendering speed. Most obvious was under normal method, it became very laggy. No difference was observed with 222/444 under maximum quality, every rotation movement took about 5-10 seconds, if the movement was too fast, windows will close slicer. I did not dare to test change TDR delay, as I’m not very handy with computers, it felt dangerous…</p>

---

## Post #28 by @Hao_Li (2021-12-16 09:15 UTC)

<p>Hi Davide!</p>
<p>I’m happy to test the data for you. Do you have some more files you want tested on 6900XT? I have switched over to work with 3090 now. I’m not very handy with computers so it’s a big project for me to change graphic cards <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=10" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"> If you have more files, I can try them at same time.</p>

---

## Post #29 by @Hao_Li (2021-12-16 13:22 UTC)

<p><a class="mention" href="/u/davide445">@davide445</a><br>
Just freshly tested volume rendering of the eye on 6900XT. Ran smoothly under normal quality. Laggy at adaptive quality. At maximum quality, it is very slow, around 5 seconds for each rotation movement. All similar to 3090. I’ll keep the card today and tomorrow, let me know if you want more data tested.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9381ca1e91a7def1e31c249315f9affca2a91fb.jpeg" data-download-href="/uploads/short-url/o8YUw7aAeEIyaLjoye10OShrYBt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9381ca1e91a7def1e31c249315f9affca2a91fb_2_690x388.jpeg" alt="image" data-base62-sha1="o8YUw7aAeEIyaLjoye10OShrYBt" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9381ca1e91a7def1e31c249315f9affca2a91fb_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9381ca1e91a7def1e31c249315f9affca2a91fb_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a9381ca1e91a7def1e31c249315f9affca2a91fb_2_1380x776.jpeg 2x" data-dominant-color="ADA5B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #30 by @davide445 (2021-12-16 20:38 UTC)

<p><a class="mention" href="/u/hao_li">@Hao_Li</a> <a class="mention" href="/u/chir.set">@chir.set</a> there are two final tests to me worth doing</p>
<ul>
<li>testing with resolution 2047 and 2049 (so just below and just above 2048)</li>
<li>test same resolution on Linux and not Windows</li>
</ul>
<p>I didn’t find scans just above the 2048 limit, will be possibile to upscale this eye, or downscale an higher res one?</p>
<p>The reason for this test is looking good at the <a href="https://opengl.gpuinfo.org/listreports?sortby=date_desc" rel="noopener nofollow ugc">OpenGL Reports DB</a> I noticed the same AMD GPU (almost all the one I checked) have GL_MAX_3D_TEXTURE_SIZE = 2048 under Windows and 8192 under Linux.<br>
Also all Nvidia GPU has the same parameter as 16384 regardless if Windows or Linux.</p>
<p>I found a few cases where this is not true, but if so seems AMD GPU Windows drivers are reporting the wrong value. I didn’t understand if the GPU hw architecture define this value, so there is maybe another “true” and max possible value, but seems to me worth a test (if possible).</p>

---

## Post #31 by @Hao_Li (2021-12-16 21:31 UTC)

<p><a class="mention" href="/u/davide445">@davide445</a> I’m happy to test on Windows. Just send a file <img src="https://emoji.discourse-cdn.com/twitter/cowboy_hat_face.png?v=10" title=":cowboy_hat_face:" class="emoji" alt=":cowboy_hat_face:"></p>

---

## Post #32 by @chir.set (2021-12-17 07:33 UTC)

<aside class="quote no-group" data-username="davide445" data-post="30" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<ul>
<li>testing with resolution 2047 and 2049 (so just below and just above 2048)</li>
<li>test same resolution on Linux and not Windows</li>
</ul>
</blockquote>
</aside>
<p>I’l be happy to test with my 6700XT on Linux. I don’t have any datasets with such high resolution.</p>
<aside class="quote no-group" data-username="davide445" data-post="30" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>all Nvidia GPU has the same parameter as 16384 regardless if Windows or Linux.</p>
</blockquote>
</aside>
<p>This <a href="https://discourse.slicer.org/t/gpu-based-volume-rendering-fails-if-one-dimension-is-more-than-2000px/6546/8">post</a> suggests that not all software report GL_MAX_3D_TEXTURE_SIZE reliably.</p>

---

## Post #33 by @Hao_Li (2021-12-17 09:45 UTC)

<p><a class="mention" href="/u/davide445">@davide445</a><br>
I realized I have alot of scans above 2048 and I think I can confirm your concerns.<br>
I have tested the following scans on windows with 6900XT</p>
<p>2367x1784x942 = 7G No<br>
1950x1830x1600 = 11G Wrong stitching<br>
885x1300x1230 = 5G Yes<br>
2125x2510x938 = 10G No<br>
1937x1829x951 = 6,5G Wrong stitching<br>
2836x1948x2664 = 14G No<br>
1928x1927x937 = 6,8G Wrong stitching<br>
2098x1919x936 = 7G No<br>
1268x1454x1064 = 3G yes<br>
2572x1837x951 = 8G no</p>
<p>After testing, I believe scans with any dimension above 2048 (2098 smallest of my scans) can not be volume rendered disregard total scan file size.</p>
<p>Out of curiousity I tested on 3090 as well the followings.<br>
2097x 2134x 1850 , 16G<br>
2292x2207x2238, 46G<br>
3784x3784x2085, 58G<br>
They all could be volume rendered properly on 3090 in windows, I didn’t have larger scans to test the limit.</p>

---

## Post #34 by @davide445 (2021-12-17 09:53 UTC)

<p><a class="mention" href="/u/hao_li">@Hao_Li</a> thanks a lot. Might I ask if you can share your 2098 file so <a class="mention" href="/u/chir.set">@chir.set</a> can test it on Linux.<br>
Also if you will be able to downsample a not rendering image to lower resolution (i.e. using Resample Scalar Volume module) we can cross check.</p>

---

## Post #35 by @chir.set (2021-12-17 09:54 UTC)

<aside class="quote no-group" data-username="davide445" data-post="34" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>if you can share your 2098 file so <a class="mention" href="/u/chir.set">@chir.set</a> can test it on Linux.</p>
</blockquote>
</aside>
<p>Yep, I was about to request the 3784x3784x2085, 58G series too. All duly anonymized of course.</p>

---

## Post #36 by @Hao_Li (2021-12-17 10:01 UTC)

<p>Hi, I’m sorry I cannot share the scans, they don’t belong to me …</p>

---

## Post #37 by @Hao_Li (2021-12-17 10:16 UTC)

<p>I used Resample Scalar Volume, Spacing 0,0,0 and interpolation linear.<br>
Volume size resulted same from 2572x1837x951 to 2572x1837x951<br>
And the volume was not able to be rendered, empty square.</p>

---

## Post #38 by @davide445 (2021-12-17 11:37 UTC)

<p><a class="mention" href="/u/hao_li">@Hao_Li</a> <a class="mention" href="/u/chir.set">@chir.set</a> can you try on the ircadb1.12 to use the Crop Volume feature with this parameters and try if the result can be rendered<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df234939bedce52c8f10c04be7136dc0ad943a0.png" alt="image" data-base62-sha1="dp5kirGSUciLEkt7S0LQeXihcYM" width="609" height="436"><br>
The resulting volume need to have more than 2048 slice<br>
Edit: sorry use 0.24 spacing scale , not 0.26 as in the image</p>

---

## Post #39 by @Hao_Li (2021-12-17 12:14 UTC)

<p>Hi! I got this on 6900XT. Can not volume render.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c094fd382ce2fb4b4dfcf63fd5be4c626bcefd39.png" data-download-href="/uploads/short-url/rtESGJ6nouBCnZjSwwZtJWFnCCl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c094fd382ce2fb4b4dfcf63fd5be4c626bcefd39_2_690x388.png" alt="image" data-base62-sha1="rtESGJ6nouBCnZjSwwZtJWFnCCl" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c094fd382ce2fb4b4dfcf63fd5be4c626bcefd39_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c094fd382ce2fb4b4dfcf63fd5be4c626bcefd39_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c094fd382ce2fb4b4dfcf63fd5be4c626bcefd39_2_1380x776.png 2x" data-dominant-color="A0A2B5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3840×2160 285 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #40 by @chir.set (2021-12-17 14:15 UTC)

<aside class="quote no-group" data-username="davide445" data-post="38" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>use the Crop Volume feature with this parameters and try if the result can be rendered</p>
</blockquote>
</aside>
<p>I don’t fully understand your requirements :</p>
<ul>
<li>what is the original volume ?</li>
</ul>
<p>I tested with the eyeglobe and another 512x512x2147 slices volume with ‘Spacing scale’ &lt; 0.24, Volume rendering always works on Linux. In both cases, though the ''Crop volume module shows high dimension values, the ‘Volumes’ module always show the source dimensions for the cropped volumes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3ed25732a40105cdd16d2fba2e29ba9978ff32a.png" data-download-href="/uploads/short-url/pFHy9eKvd4rYHEYFBeZAxv8FcCK.png?dl=1" title="crop_0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3ed25732a40105cdd16d2fba2e29ba9978ff32a_2_467x499.png" alt="crop_0" data-base62-sha1="pFHy9eKvd4rYHEYFBeZAxv8FcCK" width="467" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b3ed25732a40105cdd16d2fba2e29ba9978ff32a_2_467x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3ed25732a40105cdd16d2fba2e29ba9978ff32a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3ed25732a40105cdd16d2fba2e29ba9978ff32a.png 2x" data-dominant-color="373737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">crop_0</span><span class="informations">664×710 54.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aae447fc54ea59d1266abb1c4b83707e8cb7a553.png" data-download-href="/uploads/short-url/onMg87Uyrvar0zmDlkiJeiG4prB.png?dl=1" title="crop_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aae447fc54ea59d1266abb1c4b83707e8cb7a553_2_467x499.png" alt="crop_1" data-base62-sha1="onMg87Uyrvar0zmDlkiJeiG4prB" width="467" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aae447fc54ea59d1266abb1c4b83707e8cb7a553_2_467x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aae447fc54ea59d1266abb1c4b83707e8cb7a553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aae447fc54ea59d1266abb1c4b83707e8cb7a553.png 2x" data-dominant-color="373737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">crop_1</span><span class="informations">664×710 52.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #41 by @chir.set (2021-12-17 14:20 UTC)

<aside class="quote no-group" data-username="davide445" data-post="38" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>can you try on the ircadb1.12</p>
</blockquote>
</aside>
<p>What is this strange file ?</p>

---

## Post #43 by @davide445 (2021-12-18 19:52 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="41" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>What is this strange file ?</p>
</blockquote>
</aside>
<p>I probably misunderstood your question. The zip contains dicom volumes from a public anonimized dataset used for research.<br>
Just choosen something anyone can use for testing.</p>

---

## Post #44 by @davide445 (2021-12-19 11:25 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="33" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>I have tested the following scans on windows with 6900XT</p>
<p>2367x1784x942 = 7G No<br>
1950x1830x1600 = 11G Wrong stitching<br>
885x1300x1230 = 5G Yes<br>
2125x2510x938 = 10G No<br>
1937x1829x951 = 6,5G Wrong stitching<br>
2836x1948x2664 = 14G No<br>
1928x1927x937 = 6,8G Wrong stitching<br>
2098x1919x936 = 7G No<br>
1268x1454x1064 = 3G yes<br>
2572x1837x951 = 8G no</p>
</blockquote>
</aside>
<p>Might I ask you if will be possible to use volume crop changing the spacing scale of your 1268x1454x1064 volume to 0.9, and test this way on the 6900 XT.<br>
This since seems apart the GL_MAX_3D_TEXTURE_SIZE = 2048 topic might be some wrong shared memory management.<br>
Looking at your numbers and seeing the GPU memory usage on my side I got the idea to verify why in some cases you have problems even if the texture resolution is below 2048, and created this table</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Res</th>
<th>Hao_Li disk</th>
<th>Hao_Li results</th>
<th>VRAM needed (GByte)</th>
</tr>
</thead>
<tbody>
<tr>
<td>2367x1784x942</td>
<td>7G</td>
<td>No</td>
<td>29.6</td>
</tr>
<tr>
<td>1950x1830x1600</td>
<td>11G</td>
<td>Wrong stitching</td>
<td>42.5</td>
</tr>
<tr>
<td>885x1300x1230</td>
<td>5G</td>
<td>Yes</td>
<td>10.5</td>
</tr>
<tr>
<td>2125x2510x938</td>
<td>10G</td>
<td>No</td>
<td>37.3</td>
</tr>
<tr>
<td>1937x1829x951</td>
<td>6.5G</td>
<td>Wrong stitching</td>
<td>25.0</td>
</tr>
<tr>
<td>2836x1948x2664</td>
<td>14G</td>
<td>No</td>
<td>109.7</td>
</tr>
<tr>
<td>1928x1927x937</td>
<td>6.8G</td>
<td>Wrong stitching</td>
<td>25.9</td>
</tr>
<tr>
<td>2098x1919x936</td>
<td>7G</td>
<td>No</td>
<td>28.1</td>
</tr>
<tr>
<td>1268x1454x1064</td>
<td>3G</td>
<td>Yes</td>
<td>14.6</td>
</tr>
<tr>
<td>2572x1837x951</td>
<td>8G</td>
<td>No</td>
<td>33.5</td>
</tr>
</tbody>
</table>
</div><p>Where the VRAM needed is calculated considering 16bit (2 byte) resolution at every index, so 8 byte per voxel.<br>
Appear to me you got problems not only if the slice number is more than 2048, but also if the needed VRAM is greather than your GPU VRAM, 16GB in your case.<br>
When both the conditions are met (no more than 2048 slices and no more than 16GB VRAM required) you have no problems (two cases).<br>
So upscaling 10% that volume create a new one requiring more than 16GB and if my hypotesys is true you will need to start having problems even if the slice are less than 2048.</p>

---

## Post #45 by @davide445 (2021-12-19 11:44 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="40" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I don’t fully understand your requirements :</p>
<ul>
<li>what is the original volume ?</li>
</ul>
<p>I tested with the eyeglobe and another 512x512x2147 slices volume with ‘Spacing scale’ &lt; 0.24, Volume rendering always works on Linux. In both cases, though the ''Crop volume module shows high dimension values, the ‘Volumes’ module always show the source dimensions for the cropped volumes.</p>
</blockquote>
</aside>
<p>Sorry never answered this question. “original volume” it’s just the name appears on my side as the ircabd1.12 data (the PATIENT_DICOM folder) is loaded, nothing else.<br>
About your test being already more than 2048 slices it’s interesting works.<br>
But wanted to ask if you was actually visualizing the 3d of the first upscaled volume (and not maybe the original one): 6400x6400x26837 will need something about 8 TB VRAM!<br>
Might I ask how much RAM has your PC.</p>

---

## Post #46 by @chir.set (2021-12-19 13:10 UTC)

<aside class="quote no-group" data-username="davide445" data-post="45" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>the PATIENT_DICOM folder</p>
</blockquote>
</aside>
<p>OK, I’ll test with that on my work machine tomorrow.</p>
<aside class="quote no-group" data-username="davide445" data-post="45" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>Might I ask how much RAM has your PC</p>
</blockquote>
</aside>
<p>I’m running with 64 GB of RAM and 12 GB of VRAM on the 6700XT.</p>
<aside class="quote no-group" data-username="davide445" data-post="45" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>if you was actually visualizing the 3d of the first upscaled volume</p>
</blockquote>
</aside>
<p>I visualized on both volumes, original and cropped, with Volume Rendering cache emptied. I don’t think that the cropped volumes have so many real slices. The Volumes module does not report that magnitude of Z dimension in the cropped volumes, but the original one. Moreover, if I export a cropped volume as a DICOM series, it has the same number of files as the Z dimension of the original volume. I don’t how we should understand the ‘Spacing scale’ parameter of Crop Volume.</p>

---

## Post #47 by @lassoan (2021-12-19 14:46 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="46" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>The Volumes module does not report that magnitude of Z dimension in the cropped volumes, but the original one</p>
</blockquote>
</aside>
<p>If you find that the actual volume size is not the same as what Volumes module displays then it is a bug. Check again that you selected the correct volume node etc. and if you confirm that the reported size is wrong then please provide a list of steps to reproduce.</p>
<aside class="quote no-group" data-username="chir.set" data-post="46" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>don’t how we should understand the ‘Spacing scale’ parameter of Crop Volume</p>
</blockquote>
</aside>
<p>Output volume spacing = input volume spacing * spacing scale</p>

---

## Post #48 by @chir.set (2021-12-19 16:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="47" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Check again that you selected the correct volume node etc.</p>
</blockquote>
</aside>
<p>It seems there’s a bug.</p>
<p><em>Try 1</em></p>
<ul>
<li>Start Slicer</li>
<li>Load CTA-cardio</li>
<li>Go to Crop Volume</li>
<li>Generate the ROI with the ‘Fix’ button</li>
<li>Hide the ROI</li>
<li>Set Spacing Scale to 0.1</li>
<li>Apply</li>
</ul>
<p>It completes quickly with the result below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64074aa6b5955a018d2509865f853b176d318145.png" data-download-href="/uploads/short-url/egTmTm4clSQ7lXuArmJV8luKRtr.png?dl=1" title="crop_volume_01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64074aa6b5955a018d2509865f853b176d318145_2_603x500.png" alt="crop_volume_01" data-base62-sha1="egTmTm4clSQ7lXuArmJV8luKRtr" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64074aa6b5955a018d2509865f853b176d318145_2_603x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64074aa6b5955a018d2509865f853b176d318145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64074aa6b5955a018d2509865f853b176d318145.png 2x" data-dominant-color="363636"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">crop_volume_01</span><span class="informations">757×627 58.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In Volumes module, the cropped volume is similar as the original.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/401b8b5eae987be625fef519fee220ed83adc590.png" data-download-href="/uploads/short-url/997zrMeFGi03ssaUNAMroxPvtqU.png?dl=1" title="volume_01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/401b8b5eae987be625fef519fee220ed83adc590_2_690x217.png" alt="volume_01" data-base62-sha1="997zrMeFGi03ssaUNAMroxPvtqU" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/401b8b5eae987be625fef519fee220ed83adc590_2_690x217.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/401b8b5eae987be625fef519fee220ed83adc590.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/401b8b5eae987be625fef519fee220ed83adc590.png 2x" data-dominant-color="373738"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume_01</span><span class="informations">792×250 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><em>Try 2</em></p>
<ul>
<li>Do as above</li>
<li>But with Spacing Scale to 0.9</li>
</ul>
<p>It takes some time to complete, and the Volumes module shows a cropped volume different from the original.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/974b9abe54f0d84857e504e3c5003977c5e81334.png" data-download-href="/uploads/short-url/lAq4WZ2YAgCYUdmm3aspnvGFrNO.png?dl=1" title="volume_09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/974b9abe54f0d84857e504e3c5003977c5e81334_2_690x210.png" alt="volume_09" data-base62-sha1="lAq4WZ2YAgCYUdmm3aspnvGFrNO" width="690" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/974b9abe54f0d84857e504e3c5003977c5e81334_2_690x210.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/974b9abe54f0d84857e504e3c5003977c5e81334.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/974b9abe54f0d84857e504e3c5003977c5e81334.png 2x" data-dominant-color="363636"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume_09</span><span class="informations">789×241 29.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Afterwards, in the same session, it we set Spacing Scale to 0.1, it blows up my laptop.</p>
<p>There’s a problem if first Spacing Scale is too low.</p>

---

## Post #49 by @rbumm (2021-12-19 18:53 UTC)

<p>Can confirm that <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #50 by @lassoan (2021-12-19 19:04 UTC)

<p>Spacing scale of 0.1 is expected to “blow up” most computers, as it means making the volume size 1000x larger! Windows would probably just terminate the offending application but on Linux your computer may need a hard reset.</p>
<p>We could maybe display a warning when somebody attempts to do such an extreme operation, because a scaling value of 0.1 may look innocent if you don’t think about what it does and you don’t look at the output volume size.</p>

---

## Post #51 by @chir.set (2021-12-19 19:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="50" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if you don’t think about what it does</p>
</blockquote>
</aside>
<p>Yes, that was my case.</p>
<p>However, if we start at 0.1, it completes without rescaling anything. This may need a fix too. The warning is welcome. But if it does not rescale despite the warning, it’s misleading.</p>

---

## Post #52 by @chir.set (2021-12-20 08:05 UTC)

<aside class="quote no-group" data-username="davide445" data-post="38" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>can you try on the ircadb1.12 to use the Crop Volume feature with this parameters and try if the result can be rendered</p>
</blockquote>
</aside>
<p>With Spacing Scale at 0.24 using your reference dataset, the resulting volume is 2133 x 2133 x 1083, so &gt; 2048 in 2 dimensions.</p>
<p>Volume rendering with this resampled volume works, and is very fluid at normal speed.<br>
Using adaptative, it’s a little laggy, but yet good at default 8 fps.<br>
At maximum speed, it’s of course minimum interaction speed, 2 - 3 seconds between rotations.</p>

---

## Post #53 by @davide445 (2021-12-20 08:09 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="52" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>With Spacing Scale at 0.24 using your reference dataset, the resulting volume is 2133 x 2133 x 1083, so &gt; 2048 in 2 dimensions.</p>
</blockquote>
</aside>
<p>Also at that resolution will exceed the VRAM of your GPU, so that we got also this check that using shared memory works in Linux.</p>

---

## Post #54 by @chir.set (2021-12-20 08:41 UTC)

<aside class="quote no-group" data-username="davide445" data-post="53" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>Also at that resolution will exceed the VRAM of your GPU</p>
</blockquote>
</aside>
<p>I checked that, it used between 1.7 to 2.2 GB of VRAM. Or it’s badly reported by <a href="https://gitlab.com/corectrl/corectrl" rel="noopener nofollow ugc">CoreCtrl</a>.</p>

---

## Post #55 by @davide445 (2021-12-20 08:54 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="54" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I checked that, it used between 1.7 to 2.2 GB of VRAM. Or it’s badly reported by <a href="https://gitlab.com/corectrl/corectrl" rel="noopener nofollow ugc">CoreCtrl</a>.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/hao_li">@Hao_Li</a> we need your crosscheck on Windows if possibile as from this post</p><aside class="quote quote-modified" data-post="44" data-topic="21008">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/better-gpu-will-benefit-or-not-vr-volume-rendering/21008/44">Better GPU will benefit or not VR volume rendering</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Might I ask you if will be possible to use volume crop changing the spacing scale of your 1268x1454x1064 volume to 0.9, and test this way on the 6900 XT. 
This since seems apart the GL_MAX_3D_TEXTURE_SIZE = 2048 topic might be some wrong shared memory management. 
Looking at your numbers and seeing the GPU memory usage on my side I got the idea to verify why in some cases you have problems even if the texture resolution is below 2048, and created this table 




Res
Hao_Li disk
Hao_Li results
V…
  </blockquote>
</aside>


---

## Post #56 by @chir.set (2021-12-20 08:58 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="52" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>With Spacing Scale at 0.24 using your reference dataset, the resulting volume is 2133 x 2133 x 1083</p>
</blockquote>
</aside>
<p>One last note.</p>
<p>With Spacing Scale at 0.18 using your reference dataset, the resulting volume is 2844 x 2844 x 1444, and Volume Rendering no longer works at any interactive speed.</p>

---

## Post #57 by @davide445 (2021-12-20 09:48 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="56" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>With Spacing Scale at 0.18 using your reference dataset, the resulting volume is 2844 x 2844 x 1444, and Volume Rendering no longer works at any interactive speed.</p>
</blockquote>
</aside>
<p>Used VRAM using your monitor system?</p>

---

## Post #58 by @chir.set (2021-12-20 10:25 UTC)

<aside class="quote no-group" data-username="davide445" data-post="57" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide445/48/13460_2.png" class="avatar"> davide445:</div>
<blockquote>
<p>Used VRAM using your monitor system?</p>
</blockquote>
</aside>
<p>1.2 GB, i.e., nothing from Volume Rendering.</p>

---

## Post #59 by @Hao_Li (2021-12-20 12:18 UTC)

<p>Hi! I’m on vacation, will test in a week.</p>

---

## Post #60 by @Hao_Li (2021-12-27 09:52 UTC)

<p><a class="mention" href="/u/davide445">@davide445</a><br>
Hi! I’ve just checked.<br>
1268x1454x1064 Original<br>
I cropped using 0.9 spacing scale, and the new volume became 1408x1615x1182. The result was viewable but ended in wrong stitching. Wonder if it confirms your thoughts. Let me know if you need anything else tested, I’ll switch back to 3090 when we finish.</p>

---

## Post #61 by @davide445 (2021-12-27 12:45 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="60" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>I cropped using 0.9 spacing scale, and the new volume became 1408x1615x1182</p>
</blockquote>
</aside>
<p>Please try to decrease the spacing scale until one of the dimensions exceed 2048, this will need to result in no rendering (if the idea is true)</p>

---

## Post #62 by @Hao_Li (2021-12-27 13:54 UTC)

<p>Hi!<br>
I’ve tried now cropping using spacing 0.7 and it became 1811x2077x1520, and the result was not viewable, nothing happens.</p>
<p>I came across another odd thing for 6900xt windows in slicer, found it while I was having fun cropping. If you open data set A which can not be rendered, such like the one I used (1811x2077x1520). Then drag data set B which CAN be rendered into same slicer window ;D, volume render both data sets and you’ll see two Bs.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f80e07d6cb4dbddb6a610292b743d3015446a01e.jpeg" data-download-href="/uploads/short-url/zootkKdbM9vtTZLY6UHkv7TP6ua.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f80e07d6cb4dbddb6a610292b743d3015446a01e_2_690x388.jpeg" alt="image" data-base62-sha1="zootkKdbM9vtTZLY6UHkv7TP6ua" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f80e07d6cb4dbddb6a610292b743d3015446a01e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f80e07d6cb4dbddb6a610292b743d3015446a01e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f80e07d6cb4dbddb6a610292b743d3015446a01e_2_1380x776.jpeg 2x" data-dominant-color="B2B3CB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Another interesting thing, here the scale is even changed.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70ee9ca9b4348fad3aaf873063f4f78c33606b7e.jpeg" data-download-href="/uploads/short-url/g72HqALyOjTVgLTBRLTFBg4GCOq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70ee9ca9b4348fad3aaf873063f4f78c33606b7e_2_690x388.jpeg" alt="image" data-base62-sha1="g72HqALyOjTVgLTBRLTFBg4GCOq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70ee9ca9b4348fad3aaf873063f4f78c33606b7e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70ee9ca9b4348fad3aaf873063f4f78c33606b7e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70ee9ca9b4348fad3aaf873063f4f78c33606b7e_2_1380x776.jpeg 2x" data-dominant-color="B2B3C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried A (not viewable) + B (viewable) + C (viewable) as well, resulted in even more unpredictable results. A + B + C (all viewable) acted normally.</p>

---

## Post #63 by @davide445 (2021-12-27 14:11 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="62" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>I’ve tried now cropping using spacing 0.7 and it became 1811x2077x1520, and the result was not viewable, nothing happens.</p>
</blockquote>
</aside>
<p>Thanks for this, on my side I didn’t have any more test to do.<br>
Interesting what you discovered.</p>

---

## Post #64 by @lassoan (2021-12-27 21:04 UTC)

<aside class="quote no-group" data-username="Hao_Li" data-post="62" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hao_li/48/3420_2.png" class="avatar"> Hao_Li:</div>
<blockquote>
<p>I came across another odd thing for 6900xt windows in slicer, found it while I was having fun cropping. If you open data set A which can not be rendered, such like the one I used (1811x2077x1520)</p>
</blockquote>
</aside>
<p>Try with the latest Slicer Preview Release, too. It has many fixes compared to the latest Slicer Stable Release, some of them related to rendering of multiple volumes.</p>

---

## Post #65 by @davide445 (2021-12-28 17:15 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="64" data-topic="21008">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Try with the latest Slicer Preview Release, too. It has many fixes compared to the latest Slicer Stable Release, some of them related to rendering of multiple volumes.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/hao_li">@Hao_Li</a> would you so kind to try on the preview release (can download on <a href="https://download.slicer.org/bitstream/61c43f01342a877cb3ef389b" rel="noopener nofollow ugc">this</a> link) doing the same test as before with spacing 0.7.<br>
Also my I ask apart the GPU what other hardware you are working on (CPU, motherboard, RAM).</p>

---

## Post #66 by @Hao_Li (2021-12-29 09:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Hi! I already managed changing back to 3090 …</p>
<p>On 3090, I don’t have any problem with multi volume rendering on 4.11.20210226. Oddities I came across on 6900xt didn’t appear.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/323f85ecb1804345f3678140fc69ab38f7a1405d.jpeg" data-download-href="/uploads/short-url/7avYdoVTjScxr8M2IP72fBaTV5X.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/323f85ecb1804345f3678140fc69ab38f7a1405d_2_690x388.jpeg" alt="image" data-base62-sha1="7avYdoVTjScxr8M2IP72fBaTV5X" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/323f85ecb1804345f3678140fc69ab38f7a1405d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/323f85ecb1804345f3678140fc69ab38f7a1405d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/323f85ecb1804345f3678140fc69ab38f7a1405d_2_1380x776.jpeg 2x" data-dominant-color="B9BAC8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><a class="mention" href="/u/davide445">@davide445</a><br>
The components of my computer are ASUS ROG Crosshair VIII Formula, AMD Ryzen 9 5900X, Samsung 980 PRO and CORSAIR Vengeance LPX - DDR4 - 4 x 32 GB.<br>
The other computer is ASUS ROG MAXIMUS XII FORMULA, Intel Core i9 10900K, Samsung 980 PRO and CORSAIR Vengeance LPX - DDR4 - 4 x 32 GB.</p>
<p>I’m having 3090 on both now … and they both can render<br>
0.7 spacing crop resulted 1811x2077x1520.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f99e9d0190e3379de276793772c8f838dc6f2bd2.jpeg" data-download-href="/uploads/short-url/zCeIunBile3Dz6bCrHAd1HR7zfI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f99e9d0190e3379de276793772c8f838dc6f2bd2_2_690x388.jpeg" alt="image" data-base62-sha1="zCeIunBile3Dz6bCrHAd1HR7zfI" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f99e9d0190e3379de276793772c8f838dc6f2bd2_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f99e9d0190e3379de276793772c8f838dc6f2bd2_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f99e9d0190e3379de276793772c8f838dc6f2bd2_2_1380x776.jpeg 2x" data-dominant-color="A4A5B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
