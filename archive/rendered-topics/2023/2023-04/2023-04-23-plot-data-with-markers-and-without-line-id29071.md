---
topic_id: 29071
title: "Plot Data With Markers And Without Line"
date: 2023-04-23
url: https://discourse.slicer.org/t/29071
---

# Plot data with Markers and without Line

**Topic ID**: 29071
**Date**: 2023-04-23
**URL**: https://discourse.slicer.org/t/plot-data-with-markers-and-without-line/29071

---

## Post #1 by @keri (2023-04-23 20:21 UTC)

<p>Hi,</p>
<p>It seems I can’t show markers.<br>
I loaded the sample data:</p>
<pre><code class="lang-python"># Get a volume from SampleData and compute its histogram
import SampleData
import numpy as np
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)

chartNode = slicer.util.plot(histogram, xColumnIndex = 1)
chartNode.SetYAxisRangeAuto(False)
chartNode.SetYAxisRange(0, 4e5)
</code></pre>
<p>But can’t remember how to hide line and show markers?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/026fdefc8ac258792b448d453571a6a23c62955a.png" data-download-href="/uploads/short-url/lyDwHP9uSUpe8sJLBgZ6U9UuW6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/026fdefc8ac258792b448d453571a6a23c62955a_2_690x366.png" alt="image" data-base62-sha1="lyDwHP9uSUpe8sJLBgZ6U9UuW6" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/026fdefc8ac258792b448d453571a6a23c62955a_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/026fdefc8ac258792b448d453571a6a23c62955a_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/026fdefc8ac258792b448d453571a6a23c62955a_2_1380x732.png 2x" data-dominant-color="9B9C9A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1020 391 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><strong>Slicer: 5.0.2 r30822 / a4420c3</strong><br>
<strong>Windows 11</strong></p>

---

## Post #2 by @keri (2023-04-23 23:37 UTC)

<p>It seems only <code>cross</code> and <code>square</code> marker styles works even they both represented as circles.<br>
<code>plus</code>, <code>circle</code>, <code>diamond</code> doesn’t work at all.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e97aa66773053a6afc1d752be6b9f13280832d9.png" data-download-href="/uploads/short-url/255CR06lmTBkCaN9DqPDNBoXY8N.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e97aa66773053a6afc1d752be6b9f13280832d9_2_690x298.png" alt="image" data-base62-sha1="255CR06lmTBkCaN9DqPDNBoXY8N" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e97aa66773053a6afc1d752be6b9f13280832d9_2_690x298.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/e/0e97aa66773053a6afc1d752be6b9f13280832d9_2_1035x447.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e97aa66773053a6afc1d752be6b9f13280832d9.png 2x" data-dominant-color="F5F6F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1116×483 28.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @jamesobutler (2023-04-24 00:37 UTC)

<p>I have attempted to replicate the issue using Slicer 5.0.2 like you and also latest Slicer stable 5.2.2, but I wasn’t able to replicate. Maybe a graphical issue of some sort. Can you replicate on another machine? What type of graphics might you be using (integrated, discrete GPU)? Anything else potentially unique about your setup?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc7fc1872adfc3ca7f0d17a725074a17677399bb.png" data-download-href="/uploads/short-url/A1I2nOCFlrUmuCaT78W7zz4aSp5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc7fc1872adfc3ca7f0d17a725074a17677399bb_2_690x370.png" alt="image" data-base62-sha1="A1I2nOCFlrUmuCaT78W7zz4aSp5" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc7fc1872adfc3ca7f0d17a725074a17677399bb_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc7fc1872adfc3ca7f0d17a725074a17677399bb_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc7fc1872adfc3ca7f0d17a725074a17677399bb_2_1380x740.png 2x" data-dominant-color="A9A9A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pearsonm (2023-04-24 00:43 UTC)

<p>In the Series tab you need to change Data series from PlotSeries to Y first.</p>

---

## Post #5 by @muratmaga (2023-04-24 02:26 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="29071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>r 5.0.2 like you and also latest Slicer stable 5.</p>
</blockquote>
</aside>
<p>We have that issue for a long-while, in GPA plots as well (only square is available). There is also this thread from the old, which doesn’t work for me… <a href="https://discourse.slicer.org/t/setting-of-markerstyle-does-not-work/9073/8" class="inline-onebox">Setting of MarkerStyle does NOT work! - #8 by aiden.zhu</a></p>

---

## Post #6 by @keri (2023-04-24 08:32 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> hi,</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="29071">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Can you replicate on another machine? What type of graphics might you be using (integrated, discrete GPU)?</p>
</blockquote>
</aside>
<p>I tried on Ubuntu PC and there was no such error, i.e. everything works as expected.</p>
<p>On Windows 11 laptop I tried both integrated <code>AMD Radeon(TM) Graphics</code> and discrete <code>NVIDIA GeForce RTX 3050 Laptop GPU</code> but one of them worked. Still able to set only <code>cross</code> and <code>square</code> and they are shown as <code>circle</code>.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> thank you for the post.<br>
The proposition from the post works.<br>
If I set <code>$Env:SLICER_OPENGL_PROFILE = "core"</code> then it works fine.</p>

---
