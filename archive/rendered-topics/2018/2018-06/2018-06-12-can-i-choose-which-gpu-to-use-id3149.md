# Can I choose which GPU to use?

**Topic ID**: 3149
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/can-i-choose-which-gpu-to-use/3149

---

## Post #1 by @Fernando (2018-06-12 10:52 UTC)

<p>Hi all,</p>
<p>I’m using a gaming laptop (Dell Alienware 13 R3) which comes with an NVIDIA GeForce GTX 1060 GPU. Is there a way to configure Slicer to use it instead of the default GPU?</p>

---

## Post #2 by @wpgao (2018-06-12 11:11 UTC)

<p>Maybe the integrated GPU should be disabled, then 1060 will be automatically selected as the default GPU! This is done not in the Slicer But in the system  configuration or nvidia application!</p>

---

## Post #3 by @Fernando (2018-06-12 11:25 UTC)

<p>But I don’t want the integrated GPU to be disabled all the time. I need it when I’m, for example, using the other one for deep learning while I keep working on other stuff.</p>

---

## Post #4 by @lassoan (2018-06-12 12:33 UTC)

<p>You can select which application should use which GPU in Nvidia control panel. The Slicer main application is SlicerApp-real.exe, you need to select that executable (Slicer.exe is only the application launcher).</p>
<p>Slicer’s GPU load is probably negligible, unless you use volume rendering, display extremely large models, or view the scene in a virtual reality headset.</p>

---

## Post #5 by @Fernando (2018-06-12 12:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="3149">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can select which application should use which GPU in Nvidia control panel. The Slicer main application is SlicerApp-real.exe, you need to select that executable (Slicer.exe is only the application launcher).</p>
</blockquote>
</aside>
<p>Thanks, Andras.</p>
<p>I’m using approx. <code>300x400x330</code> images, Volume Rendering and large meshes.</p>
<p>As a reference, here’s what I did:</p>
<ol>
<li>Go to Desktop</li>
<li>Right click and select NVIDIA Control Panel</li>
<li>On the left panel, 3D Settings → Manage 3D settings</li>
<li>Open Program Settings tab</li>
<li>Click on Add and Browse for the app (in my case, <code>C:\Program Files\Slicer 4.9.0-2018-06-02\bin\SlicerApp-real.exe</code></li>
<li>Select the preferred graphics processor: “High-performance NVIDIA processor”</li>
</ol>

---
