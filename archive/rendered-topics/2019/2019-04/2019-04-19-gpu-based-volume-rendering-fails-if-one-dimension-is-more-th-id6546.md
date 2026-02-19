---
topic_id: 6546
title: "Gpu Based Volume Rendering Fails If One Dimension Is More Th"
date: 2019-04-19
url: https://discourse.slicer.org/t/6546
---

# GPU based volume rendering fails if one dimension is more than 2000px

**Topic ID**: 6546
**Date**: 2019-04-19
**URL**: https://discourse.slicer.org/t/gpu-based-volume-rendering-fails-if-one-dimension-is-more-than-2000px/6546

---

## Post #1 by @muratmaga (2019-04-19 18:22 UTC)

<p>I can consistently reproduce this on Linux and Windows on various versions of Slicer.</p>
<p>On Linux I can capture the error (not through Slicer, but from the log of the virtualGL) something to do with opengl_max_texture limitation. On windows there is no error produced (as far as I can tell), simply a blank rectangle in volume rendering window.</p>
<p>behavior is consistent with multiple graphics card including 1080TI with 11GB of RAM and the latest driver from Nvidia (425 series).</p>
<p>data from research microCT often exceeds 2K in one dimension and given that we are GPUs with 16GB of ram, Slicer really need to work with this kind of high-resolution data.</p>

---

## Post #2 by @muratmaga (2019-04-19 18:49 UTC)

<p>As a note this specifically happens on unsigned integer datasets. To reproduce, download MRHEad.NRRD, User ResampleScalarImage 1, 0.1, 1.3, and see it render correct in Volume Rendering.</p>
<p>Then use CastScalarVolume to cast it as unsigned integer, and then see it no longer renders, but a empty volume.</p>

---

## Post #3 by @muratmaga (2019-04-22 19:29 UTC)

<p>This is the only error message I can generate using Slicer 4.11 on centos with Nvidia Geforce 980Ti with drivers 410.78. On windows it simply doesn’t render without giving any error message.</p>
<p>If it helps, datasets, which are resampled MRHead.nrrd files are here:<br>
<a href="https://seattlechildrens1.box.com/v/sampleLargeVRData" class="onebox" target="_blank" rel="noopener">https://seattlechildrens1.box.com/v/sampleLargeVRData</a></p>
<blockquote>
<p>[root@magalab-head bin]# /home/apps/Slicer-4.11.0-2019-04-16-linux-amd64/Slicer<br>
Switch to module:  “Welcome”<br>
Loaded volume from file: /mnt/ramdisk/large_test_volumes/large_short.nrrd. Dimensions: 2560x2560x676. Number of components: 1. Pixel type: short.<br>
“Volume” Reader has successfully read the file “/mnt/ramdisk/large_test_volumes/large_short.nrrd” “[36.21s]”<br>
Switch to module:  “VolumeRendering”<br>
ERROR: OpenGL MAX_3D_TEXTURE_SIZE is 2048<br>
Invalid texture dimensions [2560, 2560, 676]</p>
</blockquote>

---

## Post #4 by @lassoan (2019-04-22 19:46 UTC)

<p>This makes sense. There are often such GPU hardware/driver limitations.</p>
<p>Normally you would crop/resample the volume to a sensible size: if you need to see small details then crop to the region of interest, if you need to see the entire volume then you don’t lose any visible details by resampling the volume.</p>
<p>If multi-volume rendering implementation would be completed in VTK (it’s very close, only <a href="https://discourse.vtk.org/t/multivolume-shading-is-not-working/771" rel="nofollow noopener">shading is missing</a>) then we could split up the volume into a couple of pieces and render them using multi-volume rendering.</p>

---

## Post #5 by @muratmaga (2019-04-22 20:08 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. I think there are couple issues that I would like to address:</p>
<ol>
<li>
<p>One is the users’ perspective, if it doesn’t display the volume due to a limitation, it should give out an error message (or may be to suggest to switching to CPU based rendering which works fine, but slow). Otherwise, there is really nothing to go with.</p>
</li>
<li>
<p>Would it be possible to know for sure where the limitation is coming from (HW/driver both, VTK)? In my field, 3-4GB datasets are common, and people do like to look at full detail at full size (e.g., an elongated small fish microCT would have a volume such as 1024x1024x3000 slices). If you resample you would loose the details in the small/thin bones, if you crop it, you would loose the ability to look at the whole thing together.</p>
</li>
</ol>
<p>So I am trying to understand what should be recommendation? I thought 1080TI would be recent enough and have enough VRAM (11GB) to contain the full-resolution dataset. Quadros offer a lot of VRAM, but can’t seem to find any information about MAX_3D_TEXTURE_SIZE specs of graphic cards.</p>

---

## Post #6 by @lassoan (2019-04-22 21:31 UTC)

<p>Limitations of GPU hardware/driver should not be an issue in theory, since large volumes can be tiled so that each part can fit into maximum total size and per-axis dimension. If total size limit is reached then volumes can be automatically resampled (this was implemented in the old GPU volume renderer but not in the current one).</p>
<p>Ideally, these features could be implemented transparently at VTK level, but may be implemented at application level, too.</p>
<p>I would not count on waiting on future GPUs that have higher limits. 1. We cannot control when will it happen. It may take years. 2. Rendering large volumes in one block may lead to other errors, such as non-responsiveness of the renderer (and the operating system terminating the application due to TDR timeout).</p>

---

## Post #7 by @pieper (2019-04-22 21:33 UTC)

<p>Hi <a class="mention" href="/u/muratmaga">@muratmaga</a> -</p>
<p>I’ve been poking around at this but don’t have much to report back - I agree with you that we need a much better error messages, but for that we might need to update VTK’s reporting of the error.  Then too any further fixes would be at the VTK level as <a class="mention" href="/u/lassoan">@lassoan</a> says.</p>
<p>I believe the limitation is in the hardware (or drivers).  You should be able to check using <a href="https://webglreport.com/?v=2" rel="nofollow noopener">this link</a> and check the value of MAX_3D_TEXTURE_SIZE in the Textures box.  It should be the same for VTK as webgl.  I get very different values for different cards (2048 for a software OpenGL, 8192 for a nvidia 1080 on windows, and 16384 for a AMD on a mac pro).  I haven’t yet tested how they do on the big volumes yet.</p>

---

## Post #8 by @muratmaga (2019-04-23 18:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
We had a chat with <a class="mention" href="/u/pieper">@pieper</a> today and done some test. There seems to be a disconnect between what our test hardware is capable (Geforce 1080TI) as reported by OpenGL Hardware Capabilitiy viewer (<a href="https://opengl.gpuinfo.org/download.php" class="inline-onebox">OpenGL Hardware Database by Sascha Willems</a>) and what is reported by VTK/Slicer (and also the WebGL report link that <a class="mention" href="/u/pieper">@pieper</a> provided). According to the OpenGL Hardware Capability Viewer<br>
GL_MAX_3D_TEXTURE_SIZE is 16K for 1080TI, as oppose to 2K reported by VTK. Screen shots and the full report is below. I don’t know what to make of this, all I can say same issues persist in the latest Paraview as well.</p>
<p>You can query all reported 1080TI at<br>
<a href="https://opengl.gpuinfo.org/listreports" class="onebox" target="_blank" rel="noopener">https://opengl.gpuinfo.org/listreports</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3bc2e345b03cd489a78488f286ffe28950478e5.png" data-download-href="/uploads/short-url/nmt09FAZCAySQqqk85TALCKE4C1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3bc2e345b03cd489a78488f286ffe28950478e5_2_496x499.png" alt="image" data-base62-sha1="nmt09FAZCAySQqqk85TALCKE4C1" width="496" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/3/a3bc2e345b03cd489a78488f286ffe28950478e5_2_496x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3bc2e345b03cd489a78488f286ffe28950478e5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a3bc2e345b03cd489a78488f286ffe28950478e5.png 2x" data-dominant-color="CACDCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">657×661 41.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a0752d5ea00c1091340c764c61a664705f9b8d7.png" data-download-href="/uploads/short-url/hpvWpnhKXHrWpBaGk4NHHVeVmCj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a0752d5ea00c1091340c764c61a664705f9b8d7.png" alt="image" data-base62-sha1="hpvWpnhKXHrWpBaGk4NHHVeVmCj" width="497" height="500" data-dominant-color="B1B0A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">599×602 41.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Chris_Rorden (2019-04-23 18:55 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>  - it is necessary that no dimension exceeds MAX_3D_TEXTURE_SIZE. However, this is not sufficient to ensure that the texture can be loaded. Many cards can load up to MAX_3D_TEXTURE_SIZE in one dimension only if the other dimensions have much lower resolution. In other words, you can not assume that you can load a volume of MAX_3D_TEXTURE_SIZE^3.</p>
<p>The correct solution is to test glTexImage3D(<a href="https://stackoverflow.com/questions/26410799/portably-and-correctly-getting-maximum-1d-2d-3d-cube-texture-resolution-in-openg" rel="nofollow noopener">GL_PROXY_TEXTURE_3D</a>…) before you call glTexImage3D(GL_TEXTURE_3D…).</p>

---

## Post #10 by @muratmaga (2019-04-23 19:34 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a><br>
We are definitely not trying to load 16K^3 datasets. MOst of our datasets are around 3-5 gigavoxels. This particular one is 2560x2560x676.</p>
<p>Issue might be relating to VTK reporting the MAX_3D_TEXTURE as erroneously as 2K, as shown in the error message:</p>
<blockquote>
<p>ERROR: OpenGL MAX_3D_TEXTURE_SIZE is 2048<br>
Invalid texture dimensions [2560, 2560, 676]</p>
</blockquote>
<p>This error is consistent for same dataset rendered with GPU rendering both under Slicer and Paraview (5.6.0).</p>

---

## Post #11 by @pieper (2019-04-23 21:46 UTC)

<p>Yes, since this is in both Slicer and ParaView this is something at the VTK level.</p>
<p>I may not have time for a couple weeks, but I think the right thing to do is try creating a VTK test that replicates the issue so that it can be debugged in isolation and easily replicated on various hardware and driver scenarios.</p>

---

## Post #12 by @muratmaga (2019-04-24 23:52 UTC)

<p>Well one test with a Quadro P4000, which is also reported to have 16K max_3d_texture_size, resulted in efficient rendering of the same volume with GPU in a Slicer nightly. Performance is decent enough for such large volume (2560x2560x676).</p>
<p>So we are trying to understand why right value for this setting is not detected for 1080TI. Any input/suggestion would be highly appreciated.</p>

---

## Post #13 by @muratmaga (2019-04-26 21:40 UTC)

<p>Finally managed to build Slicer locally. This is the error message from the latest (4-24) on Windows 7, with 1080TI. Volume is 2560x2560x676 and data type is uchar.</p>
<pre><code>"Volume" Reader has successfully read the file "E:/large_Uchar.nrrd" "[74.52s]"
Switch to module:  "VolumeRendering"
Generic Warning: In C:\S\B\VTK\Rendering\VolumeOpenGL2\vtkOpenGLGPUVolumeRayCast
Mapper.cxx, line 1230
Error after glDrawElements in RenderVolumeGeometry! 1 OpenGL errors detected
  0 : (1285) Out of memory

Generic Warning: In C:\S\B\VTK\Rendering\VolumeOpenGL2\vtkOpenGLGPUVolumeRayCast
Mapper.cxx, line 1230
Error after glDrawElements in RenderVolumeGeometry! 1 OpenGL errors detected
  0 : (1285) Out of memory
</code></pre>
<p>This should not get an out of memory on this card, especially the same volume renders fine on a Quadro P4000 with 8GB of RAM. This is memory usage as reported by nvidia-smi on the same machine during the rendering attempt. As you can see only ~300MB of 11GB was being used at the moment.</p>
<pre><code>C:\Program Files\NVIDIA Corporation\NVSMI&gt;nvidia-smi.exe
Fri Apr 26 14:34:22 2019
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 425.31       Driver Version: 425.31       CUDA Version: 10.1     |
|-------------------------------+----------------------+----------------------+
| GPU  Name            TCC/WDDM | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 108... WDDM  | 00000000:91:00.0  On |                  N/A |
| 30%   52C    P0    64W / 250W |    311MiB / 11264MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      5384    C+G   ...86)\Webex\Webex\Applications\ptOIEx.exe N/A      |
|    0      7376    C+G   C:\Windows\system32\Dwm.exe                N/A      |
|    0      8128    C+G   ...icer-build\bin\Debug\SlicerApp-real.exe N/A      |
|    0      8748    C+G   ...o\2017\Community\Common7\IDE\devenv.exe N/A      |
+-----------------------------------------------------------------------------+</code></pre>

---

## Post #14 by @lassoan (2019-04-26 21:49 UTC)

<p>You can try if this GL logger tool can give more information: <a href="https://github.com/dtrebilco/glintercept" rel="nofollow noopener">https://github.com/dtrebilco/glintercept</a></p>
<p>Anyway, I would suggest to report this to VTK (reproduce it with a VTK example) or maybe to the Paraview forum (provide step-by-step description of what you do). Also provide a sample data set they can test with (it can be some synthetic volume that can be compressed very well).</p>

---

## Post #15 by @muratmaga (2019-04-30 16:24 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. I couldn’t get glintercept to log anything, but I didn’t spend a lot of time with the configuration either.</p>
<p>Meanwhile we encountered a strange issue with the Debugging through VS. Slicer was built (in debug mode) and works normally. When we set SlicerApp in VS as the startup project and start debugging, we immediately get this error message <strong>“The program can’t start because vtkRenderingGL2PSOpenGL2-8.2.dll is missing from your computer”</strong>, and debugger fails.</p>
<p><a class="mention" href="/u/pieper">@pieper</a>  Any ideas why this might be?</p>

---

## Post #16 by @pieper (2019-04-30 16:41 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> did you <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Windows" rel="nofollow noopener">start visual studio via the slicer launcher</a>?</p>

---

## Post #17 by @muratmaga (2019-04-30 18:11 UTC)

<p>We opened the Slicer.sln within the Slicer-build folder, navigate down to the SLicerApp to debug.</p>

---

## Post #18 by @muratmaga (2019-04-30 18:15 UTC)

<p>Nevermind that fixed it. Debuggin now.</p>

---

## Post #19 by @muratmaga (2019-05-17 23:11 UTC)

<p>Reporting few more things for posterity. This issue appears to be with Geforce cards, or at least specifically 1080TIs we had in the lab. We had rendered large datasets up to hardware limits of Quadro RTX4000 and P4000, successfully, even using the same driver as Geforce (or at least, all required was a reboot when we swapped cards). This was with today nightly (5/16).</p>
<p>Specifically things seems to work if all dimensions are lower than the reported MAX_3D_TExture_SIZE variable and the full dataset fits into GPU’s RAM. For example, resampled MRhead.nrrd 14222x256x130 (short) works perfectly well on Quadro RTX4000, as well as a version 1969x1969x1878(uchar).</p>
<p>We don’t have any other recent Geforce cards to test this any further, but it looks like people who will be working with large microCT derived datasets can benefit from Quadro line.</p>

---

## Post #20 by @lassoan (2019-05-18 17:14 UTC)

<p>Thank you for the useful information. We had bad experience with Quadro cards in the past: they had many more compatibility issues than GeForce cards. But it is good to know that they may work better for volume rendering of large volumes.</p>
<p>We have about 30 computers in our lab with various graphics cards, so if you can set up a quick test (test data and script) then I could ask people to run it and report their results.</p>

---

## Post #21 by @RemyB (2025-12-15 12:18 UTC)

<p>Hi everyone, reopening the thread in 2025<br>
Did we get any update on the issue or are there any way to reconstruct  multiple resolutions in order to fit texture in the renderer?</p>
<p>On Windows with a Quadro M6000 24GB ram I can easily load a 13GB dataset with Imaris softwarer but in 3D slicer, the GPU vtk render fails with error “[VTK] Invalid texture dimensions [1776, 1804, 2221]”</p>
<p>I am gonna try to see if using Gemini/claude and chatGPT we cannot solve the problem by creating an extension to be able to render at multiple resolution depending on the zoom factor.</p>

---

## Post #22 by @pieper (2025-12-15 13:39 UTC)

<p>You can use CropVolume to resample to something that fits. Probably Imaris does this behind the scenes without telling you.</p>

---

## Post #23 by @muratmaga (2025-12-15 16:39 UTC)

<aside class="quote no-group" data-username="RemyB" data-post="21" data-topic="6546">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/remyb/48/79685_2.png" class="avatar"> RemyB:</div>
<blockquote>
<p>Quadro M6000 24GB ram I can easily load a 13GB dataset with Imaris softwarer but in 3D slicer, the GPU vtk render fails with error “[VTK] Invalid texture dimensions [1776, 1804, 2221]”</p>
</blockquote>
</aside>
<p>I think you are hitting the same problem as the macOS devices, that the texture dimensions on your driver is capped at 2K.</p>
<p>But I thought that’s was addressed wtih this change, <a href="https://github.com/Slicer/Slicer/pull/8430/commits/e3f8790f828a50ea7d0da72b8e7cd0998d6d42b4" class="inline-onebox" rel="noopener nofollow ugc">ENH: Make it easier to render large volumes on macOS by lassoan · Pull Request #8430 · Slicer/Slicer · GitHub</a></p>
<p>What Slicer version are you using?</p>

---

## Post #24 by @RemyB (2025-12-15 19:48 UTC)

<p>I think Imaris uses image pyramid because it converts first to an imaris file format and if I open the converted image in FIJI, I can select between different size of the image stack.</p>

---

## Post #25 by @RemyB (2025-12-15 20:04 UTC)

<p>Thanks,</p>
<p>I’m using 5.10.0<br>
It renders well using CPU (very slow) but the GPU render does not work</p>
<p>Based on infos in your link I set this following snippet in the python console to try to force to split volume in smaller chunks</p>
<p>slicer.vtkMRMLVolumeRenderingDisplayableManager.SetMaximum3DTextureSize(2048)</p>
<p>But then when trying to render with GPU  the software crash</p>

---

## Post #26 by @muratmaga (2025-12-15 20:20 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="23" data-topic="6546">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>thought that’s was addressed</p>
</blockquote>
</aside>
<p>On second look that patches things only for the MacOS. <a class="mention" href="/u/lassoan">@lassoan</a> is there a specific reason why the partitioning of the textures is done for MacOS. Other cards on other platforms can suffer from the same problem. Is not possible to detect the maximum texture size of the driver being used and determine whether texture partitioning is necessary or not?</p>
<p><a class="mention" href="/u/remyb">@RemyB</a></p>
<p>use crop volume on your original data with scaling factor of 1.08 and then use resultant volume should render fine. Slicer does not support multiresolution, so you will need to manually reduce it to the size it works with your GPU at the moment.</p>

---

## Post #27 by @lassoan (2025-12-15 20:48 UTC)

<p>It is not trivial to get the maximum 3D texture size via VTK API and on Windows you would get 16384 on most GPUs.</p>
<p>If you want to check the maximum size then you can copy-paste this into the Python console in Slicer:</p>
<pre data-code-wrap="python"><code class="lang-python">pip_install('PyOpenGL')
from OpenGL.GL import *
renWin = vtk.vtkRenderWindow()
renWin.Render()
print(glGetIntegerv(GL_MAX_3D_TEXTURE_SIZE))
</code></pre>
<p>You can also use the <code>Crop volume</code> module to crop or resample your volume to see what is the size it can cope with.</p>
<p>Setting the maximum texture size by <code>slicer.vtkMRMLVolumeRenderingDisplayableManager.SetMaximum3DTextureSize(2048)</code> should work, but it can slow down the rendering tremendously. Due to this slowdown it may be possible that the GPU does not respond within the allowed “TDR delay” time period and so the operating system shuts down the application. You can confirm this by checking the Windows Event Viewer - if you can see TDR errors in the log and you want to prevent the “crash” then you can increase the TDR delay value (in the Windows registry).</p>

---

## Post #28 by @RemyB (2025-12-15 21:24 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> THanks it seems to solve the issue but now I am hitting a TDR delay.<br>
Anyway even with a 2x scale down, the rendering is really slow.<br>
I guess the Quadro M6000 is not that powerful (and seems the case when looking at comparisons <a href="https://www.techpowerup.com/gpu-specs/quadro-m6000.c2638" class="inline-onebox" rel="noopener nofollow ugc">NVIDIA Quadro M6000 Specs | TechPowerUp GPU Database</a> )</p>

---

## Post #29 by @RemyB (2025-12-15 21:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  Thanks a lot.<br>
I’m indeed probably getting TDR delay issues. Even if  Iincreases the delay value it will anyway not be possible to work with it, that is really too slow.</p>
<p>I really think it would be great to develop for future versions a new rendering module that can use or generate image pyramid. If the Render module would have been python  I coudl have given a try but the Render this is a loadable module and C++ is million years away from what  I can do</p>

---

## Post #30 by @lassoan (2025-12-15 21:49 UTC)

<p>You can implement the pyramid rendering in Python. You don’t need to use any C++ at all!</p>
<p>A very simple implementation is the following (with just two pyramid levels):</p>
<ul>
<li>Create a new Slicer Python scripted module where the user can select a volume and enable/disable volume rendering.</li>
<li>When the user enables volume rendering then you create a volume that is 1/2 downscaled along each axis (1/8 size in total) and show that volume using volume rendering; and add an observer to the camera node of each 3D view where this volume is displayed.</li>
<li>When you detect that the camera in a certain view is highly zoomed in on the volume then crop the original (full-resolution) volume to the visible region and show that cropped volume using volume rendering (and hide the low-resolution volume in that view).</li>
<li>Keep observing the camera and adjust the cropped image as needed. When the user moves the camera then you can temporarily (while you are getting the new cropped volume) show the half-resolution volume.</li>
</ul>
<p>If you work with very high resolution volumes (not just few thousand but few ten thousand voxels along each axis) then you can implement multi-level pyramids. At this point it starts to make sense to use xarray (maybe with dask), which make it really easy to get an arbitrary region of a volume at arbitrary resolution. You can find a basic example of using xarray in Slicer in this <a href="https://github.com/gaoyi/SlicerBigImage/blob/main/NgffImageIO/NgffImageIO.py">OME-NGFF image importer</a>.</p>
<p>This is all pure Python, with some basic low-level infrastructure implemented in C++, as always.</p>

---

## Post #31 by @jamesobutler (2025-12-15 22:04 UTC)

<p>Didn’t <a class="mention" href="/u/fbordignon">@fbordignon</a> implement a type of pyramid rendering in their Slicer based custom app <a href="https://github.com/petrobras/GeoSlicer/tree/main/src/modules" class="inline-onebox" rel="noopener nofollow ugc">GeoSlicer/src/modules at main · petrobras/GeoSlicer · GitHub</a>?</p>
<p>or maybe SlicerBigImage (<a href="https://github.com/gaoyi/SlicerBigImage" class="inline-onebox" rel="noopener nofollow ugc">GitHub - gaoyi/SlicerBigImage: Large (GB and above) scale microscopic image computing using 3D Slicer</a>)?</p>

---

## Post #32 by @muratmaga (2025-12-15 22:10 UTC)

<aside class="quote no-group" data-username="RemyB" data-post="28" data-topic="6546">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/remyb/48/79685_2.png" class="avatar"> RemyB:</div>
<blockquote>
<p>I guess the Quadro M6000 is not that powerful</p>
</blockquote>
</aside>
<p>That card is almost a decade old. If you want to see how Slicer performs on modern hardware, give it a try to the morphocloud: <a href="https://morphocloud.org/" rel="noopener nofollow ugc">https://morphocloud.org/</a></p>
<p>You should have no problem rendering that data on the standard g3.l instance, but to be safe you can go for one higher, g3.xl.</p>

---

## Post #33 by @RemyB (2025-12-16 06:13 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thank you so much.</p>
<p>I guess I’m gonna have a lot of fun trying to implement this during Christmas Holidays  <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=15" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #35 by @RemyB (2025-12-16 06:16 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> thanks for the link. Good to know.</p>
<p>I can acces better cards, I will try with that</p>

---
