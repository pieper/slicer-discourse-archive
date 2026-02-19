---
topic_id: 15127
title: "Setting Visibility To Off In Volume Rendering Does Not Unloa"
date: 2020-12-18
url: https://discourse.slicer.org/t/15127
---

# Setting visibility to off in Volume Rendering does not unload the volume from texture memory

**Topic ID**: 15127
**Date**: 2020-12-18
**URL**: https://discourse.slicer.org/t/setting-visibility-to-off-in-volume-rendering-does-not-unload-the-volume-from-texture-memory/15127

---

## Post #1 by @muratmaga (2020-12-18 02:39 UTC)

<p>As it is, once the volume is loaded onto the GPU texture memory, turning off its visibility does not unload it. Any subsequent volumes selected to render in the same session add to this memory usage (I am tracking through nvidia-smi). As far as I can tell, the only time they are unloaded is when the node is deleted, or scene is reset.</p>
<p>This behavior makes perfect sense in terms of performance and I don’t think it shouldn’t be changed. But I also think it might good to have a way to modify this behavior on-demand. It is a corner case, but an important one for people rendering large volumes on shared systems (linux).  A typical use case would be running multiple docker instances using the same GPU.</p>

---

## Post #2 by @pieper (2020-12-18 15:46 UTC)

<p>Good point - as a workaround for now you can toggle between CPU and GPU rendering and that will flush the volumes from GPU memory.</p>

---

## Post #3 by @muratmaga (2020-12-18 17:11 UTC)

<p>It does, but adds up quite a bit of time, because you need to enable CPU rendering, not just switch.</p>

---

## Post #4 by @pieper (2020-12-18 17:15 UTC)

<p>If you make the volume invisible first then switching is fast.</p>

---

## Post #5 by @lassoan (2020-12-18 17:18 UTC)

<p>I’ve added an “Auto-release resources” checkbox to volume rendering module. If you check that that hiding a volume rendering also releases all graphics resources. Pull request is submitted: <a href="https://github.com/Slicer/Slicer/pull/5352">https://github.com/Slicer/Slicer/pull/5352</a></p>

---

## Post #6 by @muratmaga (2020-12-18 17:19 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="15127" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>If you make the volume invisible first then switching is fast.</p>
</blockquote>
</aside>
<p>Nope, doesn’t work with latest stable. It only flushes after it visibility set to on.</p>

---

## Post #7 by @pieper (2020-12-18 17:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="15127">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>It only flushes after it visibility set to on.</p>
</blockquote>
</aside>
<p>For me it works by toggling when the volume is not visible - this video shows nvidia-smi while doing the operations.</p>          <div class="onebox video-onebox">
            <video width="100%" height="100%" controls="">
              <source src="https://dl.dropboxusercontent.com/s/868eatupnahb2a1/gpu-memory-volume-rendering-2020-12-18%20at%2012.29.57%20PM.mov?dl=0">
              <a href="https://dl.dropboxusercontent.com/s/868eatupnahb2a1/gpu-memory-volume-rendering-2020-12-18%20at%2012.29.57%20PM.mov?dl=0" rel="noopener">https://dl.dropboxusercontent.com/s/868eatupnahb2a1/gpu-memory-volume-rendering-2020-12-18%20at%2012.29.57%20PM.mov?dl=0</a>
            </video>
          </div>


---

## Post #8 by @muratmaga (2020-12-18 18:19 UTC)

<p>Himm, that’s not the behavior I see on Linux stable. Perhaps some driver etc version difference. In any event, <a class="mention" href="/u/lassoan">@lassoan</a>’s solution seems a good one. Particularly it can be set to be default, through .slicerrc.py or some sort of a starting script.</p>

---

## Post #9 by @lassoan (2020-12-18 18:48 UTC)

<p>Default state of auto-release flag can be set  in application settings the same way as other volume rendering settings (surface smoothing, etc).</p>

---

## Post #10 by @pieper (2020-12-18 19:22 UTC)

<p>Haha, while we were trying to still investigating Andras went ahead and fixed it!  Thanks <a class="mention" href="/u/lassoan">@lassoan</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #11 by @muratmaga (2021-01-22 16:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="15127" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve added an “Auto-release resources” checkbox to volume rendering module. If you check that that hiding a volume rendering also releases all graphics resources. Pull request is submitted: <a href="https://github.com/Slicer/Slicer/pull/5352">https://github.com/Slicer/Slicer/pull/5352 </a></p>
</blockquote>
</aside>
<p>I tried this on Linux r29631, and I didn’t see a difference in behavior when “auto release resources” is checked. I enabled volume rendering for MRHead. Checked with nvidia-smi that Slicer was using 104MB of texture memory, then I set its visibility off and rerun nvidia-smi which still reported 104MB being used by Slicer. If I delete the MRHead node, then this memory is released, but toggling visibility on/off doesn’t seem to unload the volume from GPU memory.</p>

---

## Post #12 by @lassoan (2021-01-22 18:47 UTC)

<p>I see GPU memory usage decrease in Windows using renderdoc if I hide volume rendering while “Auto-release resources is enabled” (using Slicer 4.13.0-2021-01-16 (revision 29612 / d264109) win-amd64 - installed release).</p>
<p>Memory usage changes in Task Manager (Shared GPU memory), too, but those reports are less consistent. After a volume is hidden or removed not all memory is released, but when loading volume again, the memory is reused. So, it seems that the currently allocated memory is reported rather than the actually used amount. Maybe nvidia-smi reports something similar.</p>
<p>I would recommend to try volume rendering of very large volumes in multiple processes to confirm that memory is actually released when needed; or use a tool like renderdoc to get more reliable information about the actual state of the rendering pipeline.</p>
<hr>
<p>If you want to try renderdoc:</p>
<ul>
<li>launch renderdoc using <code>Slicer --launch qrenderdoc</code>
</li>
<li>launch Slicer from it using File / Launch Application → SlicerApp-real</li>
<li>capture frames before/after rendering and show/hide, etc.</li>
<li>load each capture and check “Statistics” tab</li>
</ul>
<p>For example:</p>
<p>After loading CTChest:</p>
<pre><code class="lang-auto">12 Textures - 27.05 MB (27.05 MB over 32x32), 6 RTs - 20.54 MB.
Avg. tex dimension: 963.333x758.333 (1155.6x909.6 over 32x32)
2 Buffers - 0.00 MB total 0.00 MB IBs 0.00 MB VBs.
47.59 MB - Grand total GPU buffer + texture load.
</code></pre>
<p>After showing volume rendering (140MB total GPU memory usage):</p>
<pre><code class="lang-auto">17 Textures - 166.07 MB (166.05 MB over 32x32), 7 RTs - 23.34 MB.
Avg. tex dimension: 936.4x506.5 (1048.33x843.333 over 32x32)
15 Buffers - 0.00 MB total 0.00 MB IBs 0.00 MB VBs.
189.41 MB - Grand total GPU buffer + texture load.
</code></pre>
<p>After hiding volume rendering (back to where it was before volume rendering):</p>
<pre><code class="lang-auto">12 Textures - 27.05 MB (27.05 MB over 32x32), 6 RTs - 20.54 MB.
Avg. tex dimension: 963.333x758.333 (1155.6x909.6 over 32x32)
9 Buffers - 0.00 MB total 0.00 MB IBs 0.00 MB VBs.
47.59 MB - Grand total GPU buffer + texture load.
</code></pre>
<p>After deleting the volume from the scene (no change in GPU memory usage):</p>
<pre><code class="lang-auto">12 Textures - 27.05 MB (27.05 MB over 32x32), 6 RTs - 20.54 MB.
Avg. tex dimension: 963.333x758.333 (1155.6x909.6 over 32x32)
15 Buffers - 0.00 MB total 0.00 MB IBs 0.00 MB VBs.
47.59 MB - Grand total GPU buffer + texture load.
</code></pre>

---

## Post #13 by @muratmaga (2021-01-22 23:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="15127">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you want to try renderdoc:</p>
</blockquote>
</aside>
<p>I think VirtualGL I am using for remote connection is interfering with debugging. After launching SlicerApp-real, there is nothing to capture, and qrenderdoc shows lots of these errors:</p>
<pre><code>Core 21855 15:14:50 gl_driver.cpp(3141) Log Got a Debug message from GL_DEBUG_SOURCE_API, type GL_DEBUG_TYPE_ERROR, ID 1282, severity GL_DEBUG_SEVERITY_HIGH:
Core 21855 15:14:50 gl_driver.cpp(3141) Log 'GL_INVALID_OPERATION error generated. Object is owned by another context and may not be bound here.'
</code></pre>
<p>I will try with a regular installation later.</p>

---

## Post #14 by @muratmaga (2021-01-22 23:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="15127">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to try volume rendering of very large volumes in multiple processes to confirm that memory is actually released when needed;</p>
</blockquote>
</aside>
<p>Confirmed. WHen working with really large volumes (&gt;10GB+), I can see memory being released with Nvidia-smi when I uncheck the visibility. As you guessed MRhead was too small to see the differential.</p>
<p>Awesome, thank you!</p>

---
