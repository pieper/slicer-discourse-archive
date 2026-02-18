# Volume rendering issues with high-resolution data in 4.9 nightlies continues with new hardware

**Topic ID**: 4051
**Date**: 2018-09-10
**URL**: https://discourse.slicer.org/t/volume-rendering-issues-with-high-resolution-data-in-4-9-nightlies-continues-with-new-hardware/4051

---

## Post #1 by @muratmaga (2018-09-10 18:32 UTC)

<p>I recently upgraded my desktop GPU from old Geforce Titan to 1080TI due to the feedback I am getting new VTK requiring newer hardware.</p>
<p>My datasets, which work perfectly with 4.8.1, crashes the GPU volume rendering in nigthlies with identical settings VP. This is on Windows 7, with a recent Nvidia driver 398.11 (from June). It is a fairly standard setup.</p>
<p>I am happy to provide datasets and setting to provide better trouble shooting. Just indicate me what’s necessary. This is really a big obstacle for my lab and our user basis and we really cannot move on from stable version, and yet we need the features introduced to segment editor after the release of 4.8.1</p>

---

## Post #2 by @muratmaga (2018-09-10 19:21 UTC)

<p>Here is the link to a large dataset and the VP I use:<br>
<a href="https://seattlechildrens1.box.com/v/VR-test-data" class="onebox" target="_blank" rel="nofollow noopener">https://seattlechildrens1.box.com/v/VR-test-data</a></p>

---

## Post #3 by @lassoan (2018-09-10 20:21 UTC)

<p>I could reproduce the error. Volume rendering works and the performance is reasonable, but as I zoom in and rotate around after a couple of seconds the application hangs. Windows error log indicates that the video card driver crashed (faulting module: C:\WINDOWS\SYSTEM32\nvoglv64.DLL).</p>
<p>In VTK OpenGL rendering backend (that was used in Slicer-4.8.x) you could specify GPU memory size and the renderer automatically downsampled the input volume to fit there. As far as I know, this features has not been implemented yet in the new VTK OpenGL2 rendering backend. Most likely this is the root cause of TDR errors (graphics card driver timeouts) and this application hang. It might be also some trivial bug, due to unusual properties of your data set (float voxel typ, very small voxel size, etc.), which might be easy to fix.</p>
<p>Now that basic rendering issues around clipped volume are getting resolved, it may be a good time to work on rendering of large volumes.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> What is the best course of action? Can somebody at kitware have a look at rendering this data set with a small VTK application to see if they can reproduce the error? Should we enter an issue into VTK bugtracker?</p>

---

## Post #4 by @lassoan (2018-09-10 20:35 UTC)

<p>FYI, converting your volume to have “unsigned char” voxels fixes the GPU volume rendering issues. Rendering may work because of smaller memory footprint of the image (voxel can be represented on 1 byte instead of 4 bytes) or there may be an error in GPU rendering of volumes with float voxels.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> It would be nice if you could test volume rendering of large images that have char or int voxels (not float or double).</p>

---

## Post #5 by @cpinter (2018-09-10 20:43 UTC)

<p>For reference, here’s a discussion about memory size for OpenGL2 mappers:<br>
<a href="http://vtk.1045678.n5.nabble.com/vtkGPUInfoList-does-not-work-with-OpenGL2-td5747672.html" class="onebox" target="_blank">http://vtk.1045678.n5.nabble.com/vtkGPUInfoList-does-not-work-with-OpenGL2-td5747672.html</a></p>

---

## Post #6 by @muratmaga (2018-09-10 20:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
I tried converting to uchar and, yes, it did not crashed. Thanks for the tip.<br>
I actually got a better interactivity, when I switched from Adaptive to Normal at the Quality setting. Selecting Maximum caused an immediate crash.</p>
<p>Can I also suggest expanding the GPU memory value range a bit more? 1080TI has 11GB RAM, I can either choose 8GB, which is less than what is capable or 12GB which is more.</p>

---

## Post #7 by @pieper (2018-09-10 20:49 UTC)

<p>FWIW this volume renders nicely with the nightly from 2018-08-28 on a mac with  AMD FirePro D700 6144 MB.</p>

---

## Post #8 by @cpinter (2018-09-10 20:54 UTC)

<p>The GPU memory combobox allows entering custom values. However, as <a class="mention" href="/u/lassoan">@lassoan</a> says and I also discovered before (see VTK thread), it has no effect in the new rendering backend, so it needs to be added in VTK for this to work.</p>

---

## Post #9 by @lassoan (2018-09-11 01:45 UTC)

<p>It seems there may be a bug in the VTK renderer, as I experience some strange behavior on a laptop with integrated Intel GPU.</p>
<ul>
<li>Original float image: volume appears but when I try to zoom in, the applications hangs within a few seconds.</li>
<li>Volume appears (in small size), can be rotated, speed is reasonable,  but when I try to zoom in, rendering of the application main window (all widgets and viewports) stops. The application still runs, because I can click on the ‘X’ button in the top-right corner and the exit confirmation popup appears, but nothing in the main window gets rendered anymore.</li>
<li>If I rescale and cast the image to unsigned char and increase the image spacing by a factor of 10 (from 0.018mm to 0.18mm) then rendering is robust, surprisingly fast (8-10fps), even on this really underpowered integrated Intel HD Graphics 620 GPU.</li>
</ul>

---

## Post #10 by @lassoan (2018-09-11 11:53 UTC)

<p>I’ve rescaled and casted the sample volume above to unsigned char then resampled to make it 8x larger (1440x2592x1120). This large volume could be rendered without any problems on a very basic integrated GPU (Intel HD Graphics 620 GPU), at about 4-5 fps.</p>
<p>So, it seems that <strong>volume rendering of floating-point volumes is broken on NVidia and Intel GPUs</strong>. Volume rendering works with integer types, regardless of volume size. It also seems to work with AMD GPUs.</p>

---

## Post #11 by @pieper (2018-09-11 12:18 UTC)

<p>It sounds like a rounding error - different cards can offer different floating point precision and range for the same variable declaration.  Probably some extra code to query or test the actual floating point type is needed.</p>

---

## Post #12 by @chir.set (2018-09-11 13:39 UTC)

<p>Just a not about AMD GPUs, in case it’s useful.</p>
<p>Tried the volume of the OP on an RX480 AMD GPU with 8 GB dedicated memory  on Linux :</p>
<p>Original volume : no volume rendering<br>
Cast to integer : much data loss, but VR works<br>
Cast to unsigned char : much data loss, but VR works</p>

---

## Post #13 by @lassoan (2018-09-11 14:06 UTC)

<p>Thanks for testing.</p>
<aside class="quote no-group" data-username="chir.set" data-post="12" data-topic="4051">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>much data loss</p>
</blockquote>
</aside>
<p>There is no perceivable “data loss”. What you see is due to difference in range of different scalar types.</p>
<p>Before you cast the image, you must rescale intensity levels to match the range of the scalar type you will convert to. For example, use Simple Filters module’s IntensityWindowingImageFilter with Window min = 0, max = 50; Output min = 0, max = 255 before casting float values to unsigned char.</p>
<p>This is rendered from unsigned char voxels after rescaling and casting:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71b8ea6ff9cb75586f21deb68591d410eff487b5.jpeg" data-download-href="/uploads/short-url/ge28kwTrc85OB5KlRJYYzJWsZoh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71b8ea6ff9cb75586f21deb68591d410eff487b5_2_522x500.jpeg" alt="image" data-base62-sha1="ge28kwTrc85OB5KlRJYYzJWsZoh" width="522" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/71b8ea6ff9cb75586f21deb68591d410eff487b5_2_522x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71b8ea6ff9cb75586f21deb68591d410eff487b5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71b8ea6ff9cb75586f21deb68591d410eff487b5.jpeg 2x" data-dominant-color="A3979F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×614 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @chir.set (2018-09-11 14:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="4051">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Before you cast the image, you must rescale intensity levels</p>
</blockquote>
</aside>
<p>Yep, following your instructions, I have the same VR results after rescaling and casting to unsigned char on the RX480.</p>

---
