---
topic_id: 8009
title: "Listing Of Known Working Gpu Card And Associated Datasets"
date: 2019-08-13
url: https://discourse.slicer.org/t/8009
---

# Listing of known working GPU card and associated datasets

**Topic ID**: 8009
**Date**: 2019-08-13
**URL**: https://discourse.slicer.org/t/listing-of-known-working-gpu-card-and-associated-datasets/8009

---

## Post #1 by @jcfr (2019-08-13 18:09 UTC)

<p>To help Slicer users understand which graphics card works best for which tasks, I would appreciate if you could comment below with details like:</p>
<ul>
<li>Slicer version</li>
<li>GPU card description (name, memory, …)</li>
<li>Operating System, CPU, memory</li>
<li>Image dimension, spacing</li>
<li>Volume rendering settings</li>
<li>Screen resolution</li>
</ul>
<p>Thanks for your inputs,</p>

---

## Post #2 by @chir.set (2019-08-14 08:48 UTC)

<p><em>Slicer version</em><br>
latest git home built</p>
<p><em>Hosts</em><br>
AMD kaveri(1 GB) + AMD Topaz (2 GB)<br>
AMD A10 APU<br>
RAM : 12 GB</p>
<p>AMD RX 480 (8 GB)<br>
AMD Phenom™ II X6 1100T CPU<br>
RAM : 16 GB</p>
<p>AMD Cape Verde Pro (1 GB)<br>
AMD FX-4300<br>
RAM : 8 GB</p>
<p>AMD VEGA 8 (1 GB shared VRAM)<br>
AMD Ryzen 5 - 2500U APU<br>
RAM : 16 GB</p>
<p>AMD VEGA 8 (1 GB shared VRAM) + NVidia (2 GB) (unknown model, mid-level)<br>
AMD Ryzen 5 - 2500U APU<br>
RAM : 8 GB</p>
<p><em>Operation system</em><br>
Linux x86_64 on all hosts</p>
<p><em>Image dimension</em><br>
512 x 512 x [up to ~2200]<br>
Spacing : 0.3 to 2 mm</p>
<p><em>Volume rendering settings</em><br>
Sum of VRAM available<br>
Quality : normal<br>
VTK GPU raycasting</p>
<p><em>Screen resolution</em><br>
1440x900, 1920x1080, 2560x1440</p>
<p><em>Modules</em><br>
amdgpu<br>
NVidia proprietary</p>

---

## Post #3 by @pieper (2019-08-14 20:57 UTC)

<p>I’ve had good luck lately with windows (nvidia 1080) mac (AMD FirePro D700 6 GB) and linux (nvidia v100 16G) on pretty much any volume I’ve tried at any screen resolution.  Also the software fallback rendering on a <a href="https://github.com/pieper/SlicerDockers" rel="nofollow noopener">docker x11</a> also works remarkably well.</p>
<p>So maybe the other side of the question is what <em>doesn’t</em> work?  Off the top of my head I think maybe some linux drivers, some older Intel GPUs.  Any other broad categories?</p>

---

## Post #4 by @muratmaga (2019-08-14 21:00 UTC)

<p>I thought a google sheet might be a bit more useful to compile this information in a more structured way.</p>

---

## Post #5 by @Amine (2019-08-14 21:11 UTC)

<p>Smooth volume renderings on:<br>
Slicer 4.10 and 4.11<br>
GPU: Nvidia gtx 970 4Gb<br>
CPU: i7 4770s<br>
Memory 16gb<br>
Resolution full hd<br>
Os: win 10<br>
Image dimensions around 512x512×300 (0.89x0.89x1)<br>
Volume rendering settings: Gpu rendering</p>

---

## Post #6 by @jcfr (2019-08-14 21:21 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="8009" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I thought a google sheet might be a bit more useful to compile this information in a more structured way.</p>
</blockquote>
</aside>
<p>Great idea. Here is a link to publicly editable spreadsheet: <a href="http://bit.ly/slicer-working-gpu-and-dataset-specs" class="inline-onebox">3D Slicer - Listing of known working GPU card and associated datasets - Google Sheets</a></p>
<p>If you already posted the spec, consider adding the info to the document and editing your previous post. Thanks</p>

---

## Post #7 by @Alex_Vergara (2020-02-13 13:36 UTC)

<p>Not running on</p>
<ul>
<li>Slicer-4.11.0-2020-02-12-linux-amd64</li>
<li>Linux Ubuntu18.04 x64</li>
<li>NVidia Driver: 440.48.02</li>
<li>NVidia card:  GeForce GTX TITAN Black</li>
<li>GPU UUID: GPU-c8227551-5eff-d32e-ae22-c4cb4ee605db</li>
</ul>
<p>Slicer won’t open with error</p>
<pre><code class="lang-bash">Switch to module:  "Welcome"
QOpenGLWidget: Failed to create context
.............................. (same 15 times)
QOpenGLWidget: Failed to create context
composeAndFlush: QOpenGLContext creation failed
composeAndFlush: makeCurrent() failed
.............................. (same 1e6 times)
composeAndFlush: makeCurrent() failed
error: [/home/alex/Documents/Slicer-4.11.0-2020-02-12-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #8 by @lassoan (2020-02-13 13:45 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="7" data-topic="8009">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Not running on</p>
<ul>
<li>Slicer-4.11.0-2020-02-12-linux-amd64</li>
<li>Linux Ubuntu18.04 x64</li>
<li>NVidia Driver: 440.48.02</li>
</ul>
</blockquote>
</aside>
<p>I don’t think that this card would not support OpenGL. This is most likely just a configuration error.</p>
<p>Does glxgear or other basic OpenGL applications work?</p>

---

## Post #9 by @Alex_Vergara (2020-02-13 14:13 UTC)

<p>hmm, probably</p>
<pre><code class="lang-bash">alex@CRCTcalcul:~/Downloads/nvidia$ sudo nvidia-smi
Failed to initialize NVML: Driver/library version mismatch
</code></pre>
<p>I’ll try to solve that and reply with an answer<br>
Edit:<br>
I have reinstalled Cuda toolkit with bundled nvidia driver and now it it running <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---
