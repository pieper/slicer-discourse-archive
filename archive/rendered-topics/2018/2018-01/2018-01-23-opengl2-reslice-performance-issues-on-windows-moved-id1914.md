# OpenGL2 reslice performance issues on windows (moved)

**Topic ID**: 1914
**Date**: 2018-01-23
**URL**: https://discourse.slicer.org/t/opengl2-reslice-performance-issues-on-windows-moved/1914

---

## Post #1 by @ihnorton (2018-01-23 16:44 UTC)

<p>Thread moved from <a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/6">here</a> where <code>@pieper</code> said:</p>
<blockquote>
<p>Other notes: the nightly crashes when started over remote desktop but the 4.8.1 release does not (probably the OpenGL2 issue) and I see the same slowdown in Slice rendering that Andras reported.</p>
</blockquote>

---

## Post #2 by @lassoan (2018-01-18 15:41 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/6">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>the nightly crashes when started over remote desktop but the 4.8.1 release does not (probably the OpenGL2 issue)</p>
</blockquote>
</aside>
<p>Yes, this is a known issue - see details and workarounds <a href="https://issues.slicer.org/view.php?id=4252">here</a>.</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/6">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>I see the same slowdown in Slice rendering that Andras reported</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a> Can you try if disabling “Threaded optimization” (in Windows Control Panel → NVidia Control Panel) makes it better?</p>

---

## Post #3 by @pieper (2018-01-18 15:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="9" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/9">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>Yes, this is a known issue - see details and workarounds here.</p>
</blockquote>
</aside>
<p>Yes, that’s what I meant by ‘the OpenGL2 issue’</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="9" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/9">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> Can you try if disabling “Threaded optimization” (in Windows Control Panel -&gt; NVidia Control Panel) makes it better?</p>
</blockquote>
</aside>
<p>I tried a bit but it didn’t obviously help.  I changed the setting to Off and restarted Slicer.  Do you need to restart the machine or something to make it work?  In any case we should try to get to the heart of the issue because users won’t want to change that level of config just to run Slicer.</p>
<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/10">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>vtkmodules package is not expected to exist in the current nightly</p>
</blockquote>
</aside>
<p>must happen during the installer step then?</p>

---

## Post #4 by @lassoan (2018-01-18 16:18 UTC)

<aside class="quote no-group quote-post-not-found" data-username="pieper" data-post="13" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/13">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>Do you need to restart the machine or something to make it work?</p>
</blockquote>
</aside>
<p>Yes, you need to restart your computer.</p>
<aside class="quote no-group quote-post-not-found" data-username="pieper" data-post="13" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/13">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>In any case we should try to get to the heart of the issue because users won’t want to change that level of config just to run Slicer.</p>
</blockquote>
</aside>
<p>Completely agree. Some gamers keep this option turned off to get more predictable frame rates, but Slicer should not require this. Anyway, let’s see first if it fixes the performance problem for you.</p>

---

## Post #5 by @pieper (2018-01-18 21:15 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="15" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/15">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>Yes, you need to restart your computer.</p>
</blockquote>
</aside>
<p>Interesting:<br>
with threading optimization on: 8 fps<br>
with threading optimization off, then restart slicer: 15 fps<br>
with threading optimization off, then restart computer: 16.6 fps</p>

---

## Post #6 by @lassoan (2018-01-18 21:27 UTC)

<p>What frame rate do you get with Slicer-4.8.1?</p>

---

## Post #7 by @pieper (2018-01-18 23:12 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="20" data-topic="1868" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/20">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>What frame rate do you get with Slicer-4.8.1?</p>
</blockquote>
</aside>
<p>41.6 fps with 4.8.1(same machine, same data, slightly bigger slice window size 272x412, instead of 186x420 for the nightly)</p>

---

## Post #8 by @lassoan (2018-01-19 00:30 UTC)

<p>This slowdown is unacceptable.<br>
<a class="mention" href="/u/jcfr">@jcfr</a> Do you think the VTK team could investigate this? What can we do to move things forward?</p>

---

## Post #9 by @pieper (2018-01-19 01:10 UTC)

<p>For the record, my system is running a GTX 1080 that runs everything else very fast.</p>
<p>Has anyone tried profiling their GPU? e.g. with <a href="https://www.nvidia.com/object/nsight.html">https://www.nvidia.com/object/nsight.html</a></p>

---

## Post #10 by @jcfr (2018-01-19 13:39 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="22" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868/22">Vtk python does not import on today's windows nightly</a></div>
<blockquote>
<p>Do you think the VTK team could investigate this? What can we do to move things forward?</p>
</blockquote>
</aside>
<p>Cc: <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a></p>

---

## Post #11 by @Prashant_Pandey (2019-10-29 23:50 UTC)

<p>I just wanted to say I still experienced this issue in 4.10.2.<br>
I used <a class="mention" href="/u/lassoan">@lassoan</a> tip and turned off threaded optimization in Nvidia control panel.<br>
Performance jumped from 8-10 fps to 18fps when rendering two volumes in two different 3D views with transformed ROIs dynamically cropping the volume.</p>

---

## Post #12 by @lassoan (2019-10-30 00:26 UTC)

<aside class="quote no-group" data-username="Prashant_Pandey" data-post="11" data-topic="1914">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/c0e974/48.png" class="avatar"> Prashant_Pandey:</div>
<blockquote>
<p>I just wanted to say I still experienced this issue in 4.10.2</p>
</blockquote>
</aside>
<p>What operating system, CPU, and graphics card do you have?</p>

---

## Post #13 by @Prashant_Pandey (2019-10-30 00:38 UTC)

<p>Windows 10, Intel i7-6700HQ @ 2.6GHz, nVidia GTX 1070, 32GB RAM</p>

---

## Post #14 by @lassoan (2019-10-30 03:29 UTC)

<p>This is odd. On computers that we tested on, using Intel TBB as SMP backend took care of interference of NVidia threaded optimization (see <a href="https://github.com/Slicer/Slicer/pull/930">https://github.com/Slicer/Slicer/pull/930</a>).</p>
<p>Have you built Slicer or extensions yourself? Do you use Intel TBB as SMP backend? (by default, it is used on Windows, but you can double-check the value of <code>Slicer_VTK_SMP_IMPLEMENTATION_TYPE</code> CMake variable).</p>
<p>Does calling <code>vtk.vtkMultiThreader.SetGlobalMaximumNumberOfThreads(1)</code> make any difference?</p>
<p>Maybe you can try to update your NVidia drivers. It would be also nice if you could test on a more recent computer (6th generation Intel CPUs are about 5 years old now, maybe a new model could be significantly faster).</p>

---

## Post #15 by @muratmaga (2019-10-30 03:48 UTC)

<p>Have you tried setting the default rendering quality to Normal, instead of Adaptive? For me that usually makes a significant difference…</p>

---

## Post #16 by @Prashant_Pandey (2019-10-30 03:52 UTC)

<p>I haven’t built Slicer or any extensions myself - I’m using the prebuilt binary and all extensions are installed using the extensions browser. I wrote a couple of python modules for my project using the extension wizard.</p>
<p>A couple of things to note which are different from the github issue you linked. I noticed a speed up in volume rendering, instead of slice scrolling, by disabling threaded optimization. Secondly, this is on a laptop and not a desktop.</p>
<p>I will try on a newer CPU, but the newest I have available is a desktop i7-7700 with nvidia 1060.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I tried changing between adaptice and normal, but this didn’t make a huge difference in frame rate. The biggest speed up (in addition to disabling threaded optim.) was by not using a dynamic cropping ROI.</p>

---

## Post #17 by @muratmaga (2019-10-30 04:05 UTC)

<p>If this is a laptop, you are certain that Slicer using the Nvidia GPU (not the integrated intel one).</p><aside class="quote" data-post="1" data-topic="3149">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fernando/48/5640_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/can-i-choose-which-gpu-to-use/3149">Can I choose which GPU to use?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi all, 
I’m using a gaming laptop (Dell Alienware 13 R3) which comes with an NVIDIA GeForce GTX 1060 GPU. Is there a way to configure Slicer to use it instead of the default GPU?
  </blockquote>
</aside>


---

## Post #18 by @Prashant_Pandey (2019-10-30 04:22 UTC)

<p>Good point. I checked my nvidia settings and it is ambiguous whether Slicer was using the integrated or nvidia GPU (the options and menu are different from the thread you linked). I will test again tomorrow with the same setup, this time focing slicer to use the nvidia gpu and report on the frame rate.</p>

---

## Post #19 by @muratmaga (2019-10-30 04:24 UTC)

<p>Installation path will differ, but the important thing to make sure that <code>SlicerApp-real.exe</code> is added, not Slicer.exe</p>

---

## Post #20 by @Prashant_Pandey (2019-10-30 20:18 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/lassoan">@lassoan</a> The framerate didn’t change when forcing slicer to use the nvidia GPU, which implies it was using it previously. I’ve attached a screenshot of the nvidia control panel settings:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fa24e60f41ee00a4a0518080d21b75c572c857f.png" data-download-href="/uploads/short-url/fVyJN5Yr2relXsJqjrxwvw2Vg4L.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fa24e60f41ee00a4a0518080d21b75c572c857f.png" alt="image" data-base62-sha1="fVyJN5Yr2relXsJqjrxwvw2Vg4L" width="603" height="500" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">663×549 19.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @lassoan (2019-10-30 20:53 UTC)

<p>This does not show the important part: have you set Slicer.exe or SlicerApp-real.exe to use the GPU?</p>

---

## Post #22 by @Prashant_Pandey (2019-10-30 21:06 UTC)

<p>It’s slicerapp-real.exe</p>

---

## Post #23 by @lassoan (2019-10-31 02:31 UTC)

<p>Do you see different values in “Reslicing” test in “Performance Tests” module when you enable/disable Slicer to use the NVidia GPU?</p>

---

## Post #24 by @Prashant_Pandey (2019-10-31 03:27 UTC)

<p>No difference, I get 60fps both ways. Nvidia control panel doesnt give me the option to disable the nvidia gpu - just to switch between ‘Auto-select’ and ‘GTX 1070’.</p>
<p>I actually think, unusually, my laptop only has the nvidia GPU and no integrated intel gpu - I checked in device manager and ‘dxdiag’.</p>
<p>Maybe I should start a separate thread - but is there a way to improve the frame rate in general and specifically for volume rendering? When rendering two volumes my frame rate never goes higher than ~18-19 fps. I’ve selected ‘adaptive’ and told Slicer that the GPU memory is 8GB. However I can see that only about ~25% of the GPU memory is being utilized.</p>

---

## Post #25 by @lassoan (2019-10-31 04:09 UTC)

<p>60fps is due to vsync lock, you reached the max refresh rate. It is usually does not work like this on an integrated graphics card, so this also suggest that Slicer uses the NVidia GPU.</p>
<p>Improving frame rate for volume rendering is very different from improving frame rate in general.</p>
<p>Volume rendering is usually very fast on a fast GPU, because the entire image is uploaded in the GPU memory and the CPU barely needs to do anything. It would be great if you could do some profiling. Best is if you build Slicer in RelWithDebInfo mode and use VisualStudio performance profiler. But first you may just try to attach VerySleepy to your current Slicer and see if any method call stands out as potential culprit.</p>
<p>Is rendering much faster if you don’t keep changing the clipping plane? Maybe changing the clipping plane triggers shader recompilations or other lengthy operations. Is it faster if you render in only one 3D view or render only a single volume?</p>

---

## Post #26 by @Prashant_Pandey (2019-10-31 05:11 UTC)

<p>Yes, rendering is slightly faster (20-25fps) when the clipping plane isn’t changing and there is only one volume being rendered. When there are two volumes and clipping plane it’s about 15 fps. When I use the depth peeling option it drops further to 10fps.</p>
<p>In task manager I can see that slicer is using significant CPU resources (approx 40%) while GPU usage is 10-25%. I haven’t used the other profiling tools before, but I will give them a go.</p>

---

## Post #27 by @muratmaga (2019-10-31 17:01 UTC)

<p>In Nvidia control panel, does changing the power management from “optimal power” to “performance” help?</p>

---

## Post #28 by @Prashant_Pandey (2019-10-31 21:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> here is the profiling (using very sleepy) from when I am doing volume rendering and dynamic cropping. I don’t really know what this information means so I would appreciate if you could help me understand what’s going on.  <a href="https://drive.google.com/open?id=1DayvbsKzwnw_2EALrltEnNPokEwjqkt7" rel="nofollow noopener">https://drive.google.com/open?id=1DayvbsKzwnw_2EALrltEnNPokEwjqkt7</a></p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> No significant difference between using the optimal power and maximum/performance power settings.</p>
<p>Additionally I have noticed that the longer a scene is loaded, the general frame rate for all views/visualizations drops over time even if no new data has been loaded into the scene. For example frame rated dropped by 4-6 fps when volume rendering when the scene had been loaded for about an hour.</p>

---

## Post #29 by @Prashant_Pandey (2019-11-12 00:18 UTC)

<p>Small update: A few settings in Nvidia control panel which have helped overall framerate improve (particularly in Slice Views)<br>
Threaded Optimization: ON<br>
Vsync: OFF (I don’t think this is doing much for the 3D viewer)<br>
Maximum pre-rendered frames: 1 (AKA ‘Low Latency Mode’ in updated nvidia control panel - turn it on)</p>
<p>With these 2D reslicing is very very smooth. However, two 3D volume renderings using depth peeling and dynamic ROI cropping are still at roughly 14-15 fps. I think this is partly due to the ROI as I mentioned above, but also because I have a few models being displayed with opacities &lt; 1.</p>

---
