---
topic_id: 10887
title: "Why The The Tool Of Scissor Become Slower After I Undated My"
date: 2020-03-28
url: https://discourse.slicer.org/t/10887
---

# Why the the tool of scissor become slower after I undated my computer?

**Topic ID**: 10887
**Date**: 2020-03-28
**URL**: https://discourse.slicer.org/t/why-the-the-tool-of-scissor-become-slower-after-i-undated-my-computer/10887

---

## Post #1 by @researchtomliu (2020-03-28 11:33 UTC)

<p>I have updated my computer to make the 3D-Slicer run faster. The new CPU is AMD 2950X and the GPU is RTX 2080Ti. But when I performed the software to deal with the DICOM data, I found that running of scissor tool in the modules of segment editor is too slow, even significantly slower than my old computer with the GPU 1070. Can someone help me to solve this problem?</p>

---

## Post #2 by @lassoan (2020-03-28 14:24 UTC)

<p>GPU is used for visualization only (with a few exceptions), so having a stronger GPU is not expected to change processing speed.</p>
<p>To speed up editing operations, disable 3D display (or at least disable smoothing) and/or crop and resample the master volume (using Crop volume module) before starting segmentation.</p>

---

## Post #3 by @hherhold (2020-03-28 14:48 UTC)

<p>I seem to remember something about 2080’s not supporting OpenGL properly and this causing issues? I may be mis-remembering this, my brain is totally fried this week.</p>

---

## Post #4 by @researchtomliu (2020-03-28 16:05 UTC)

<p>Thanks, I found that only the scissor was encumbered by the new GPU, the other modules ran faster than them on my old computer.</p>

---

## Post #5 by @lassoan (2020-03-28 17:49 UTC)

<p>Could you take a screen capture video of what you do (or give a very detailed description) so that we can reproduce it? Is drawing the line takes longer, or the update of the segmentation after you release the mouse button? How long do you have to wait? How many segments do you have? What are the dimensions of the segmented volume? Can you reproduce it using any of the data sets downloaded using Slicer’s Sample Data module?</p>

---

## Post #6 by @zyy_13579 (2021-04-25 05:48 UTC)

<p>I use CTChest did test. Threshold set 72-3071,<br>
PC1<br>
CPU:AMD 4800U,(Laptop)<br>
Memory:16G 3200Mhz,<br>
GPU:Vega8</p>
<p>PC2<br>
CPU:Intel i7 10700,(Desktop)<br>
Memory:16G 3200Mhz,<br>
GPU:RTX 3060</p>
<p>PC3<br>
CPU:Intel i7 7700HQ,(MacBookPro15)<br>
Memory:16G 2133Mhzz,<br>
GPU:Radeon Pro 555</p>
<p>PC4<br>
CPU:Intel i5 8265U,(Laptop)<br>
Memory:8G 2600Mhz,<br>
GPU:Intel 620HD</p>
<p>Test Case one : Show 3D.<br>
PC1,Cost time: 16s<br>
PC2,Cost time: 10s<br>
PC2,Cost time: 19s<br>
PC4,Cost time: 15s</p>
<p>Test Case tow : Cut the surface behind chest.<br>
PC1,Cost time: 16s<br>
PC2,Cost time: 10s<br>
PC3,Cost time: 19s<br>
PC4,Cost time: 15s</p>
<p>Why amd 4800u is slower than intel 8265u? It shoud not happen<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8de548dd67ce85e7ea9284c9fb42afa9044aa82.jpeg" alt="cpu" data-base62-sha1="o5SyrheDK3cBL2jlOoHbVgrzhwC" width="689" height="448"></p>

---

## Post #7 by @lassoan (2021-04-25 13:02 UTC)

<p>What operating system and Slicer version did you use for the testing?</p>
<p>Please try the latest Slicer Preview Release, as surface smoothing (which used to be the main performance bottleneck during 3D model generation) is 40x faster in the new version.</p>
<p>Also make sure to enable maximum speed in your power management settings.</p>
<p>You can try to attach a profiler to see where most of the time is spent (e.g. VerySleepy on Windows).</p>
<p>Slicer uses TBB, which uses sophisticated parallelization methods, which may not work as well on AMD as on Intel, but with a quick web search I did not find much (if 2x slowdown of TBB on AMD vs. Intel was a common thing then it should have been widely reported).</p>

---

## Post #8 by @zyy_13579 (2021-04-26 03:13 UTC)

<p>System: Windows10pro 20H2<br>
Slicer Version: latest statble release 4.11.20210226<br>
I has been try latest Preview Release in PC1.Really fast,from 16s decrease to 4-5s.<br>
Great Job！ <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #9 by @muratmaga (2021-04-26 04:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="10887">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Please try the latest Slicer Preview Release, as surface smoothing (which used to be the main performance bottleneck during 3D model generation) is 40x faster in the new version.</p>
</blockquote>
</aside>
<p>This great! Has been a major issue for us…</p>

---

## Post #10 by @chir.set (2021-04-26 10:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="10887">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer uses TBB</p>
</blockquote>
</aside>
<p>Does it concern Linux builds also ? If so, what would be the configuration parameters to cmake ? TIA.</p>

---

## Post #11 by @lassoan (2021-04-26 13:17 UTC)

<p>Relevant CMake variables and logic is here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/d06e71c8a67c2801ddd78b8f17a663256bae5d7d/CMakeLists.txt#L484..L501" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/d06e71c8a67c2801ddd78b8f17a663256bae5d7d/CMakeLists.txt#L484..L501" target="_blank" rel="noopener">Slicer/Slicer/blob/d06e71c8a67c2801ddd78b8f17a663256bae5d7d/CMakeLists.txt#L484..L501</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="474" style="counter-reset: li-counter 473 ;">
<li>endif()</li>
<li>
</li>
<li>#-----------------------------------------------------------------------------</li>
<li># Slicer VTK Options</li>
<li>#-----------------------------------------------------------------------------</li>
<li>set(_backend "OpenGL2")</li>
<li>set(Slicer_VTK_RENDERING_BACKEND "${_backend}" CACHE STRING "Rendering backend." FORCE)</li>
<li>mark_as_superbuild(Slicer_VTK_RENDERING_BACKEND)</li>
<li>set(Slicer_VTK_RENDERING_USE_${Slicer_VTK_RENDERING_BACKEND}_BACKEND 1)</li>
<li>
</li>
<li class="selected"># Slicer build is only tested with Sequential and TBB. OpenMP might work.</li>
<li># Use TBB by default only on Windows, as it has not been tested on other platforms.</li>
<li>if(WIN32)</li>
<li>  set(Slicer_DEFAULT_VTK_SMP_IMPLEMENTATION_TYPE "TBB")</li>
<li>else()</li>
<li>  set(Slicer_DEFAULT_VTK_SMP_IMPLEMENTATION_TYPE "Sequential")</li>
<li>endif()</li>
<li>set(Slicer_VTK_SMP_IMPLEMENTATION_TYPE ${Slicer_DEFAULT_VTK_SMP_IMPLEMENTATION_TYPE}</li>
<li>  CACHE STRING "Which multi-threaded parallelism implementation to use in VTK. Options are Sequential or TBB.")</li>
<li>set_property(CACHE Slicer_VTK_SMP_IMPLEMENTATION_TYPE</li>
<li>  PROPERTY</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>You can use system TBB or make Slicer download/build TBB as part of the supervuild process. You can find additional logic for this if you search for <code>Slicer_USE_TBB</code> in the source code.</p>
<p>In official Slicer releases TBB is probably only used on Windows. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> can you confirm?</p>

---

## Post #12 by @Sam_Horvath (2021-04-26 13:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="10887">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>Slicer_VTK_SMP_IMPLEMENTATION_TYPE</code></p>
</blockquote>
</aside>
<p>Correct, the Linux and macOS releases do not use TBB.</p>

---

## Post #13 by @hherhold (2021-04-26 13:37 UTC)

<p>Is there a particular reason for this? Just not tested yet?</p>
<p>Thanks!</p>

---

## Post #14 by @Sam_Horvath (2021-04-26 17:05 UTC)

<p>Yes, so far as I know, we haven’t had the bandwidth to test on the other platforms.</p>

---

## Post #15 by @lassoan (2021-04-26 20:20 UTC)

<p>As far as I know, Slicer with TBB has not been tested on Linux. I guess the main reason is that in most of the funded projects, Slicer is used on Linux on servers in special/virtualized/limited hardware environments, where TBB might not help much and/or cause compatibility issues.</p>

---
