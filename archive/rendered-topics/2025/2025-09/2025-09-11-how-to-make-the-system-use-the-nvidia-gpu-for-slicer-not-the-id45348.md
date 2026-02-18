# How to make the system use the NVIDIA GPU for Slicer (not the integrated Intel graphics)

**Topic ID**: 45348
**Date**: 2025-09-11
**URL**: https://discourse.slicer.org/t/how-to-make-the-system-use-the-nvidia-gpu-for-slicer-not-the-integrated-intel-graphics/45348

---

## Post #1 by @johny723 (2025-09-11 19:50 UTC)

<p>Hi, I have a different problem.</p>
<p>My setup: Intel Core i9-13980HX, 64 GB RAM DDR5, GeForce RTX 4090 - 16GB GDDR6</p>
<p>Windows 11</p>
<p>MetaQuest 3 128</p>
<p>I tried 5.8.1, 5.9. and 5.6.2 Slicer versions.</p>
<p>I keep getting “incorrect graphic card” error message when trying to use the VR module.</p>
<p>Seems like the Slicer3D works with an internal graphic card of my laptop, but the SteamVR only uses my RTX 4090. I am not able to make it work. When I force the laptop to use just one graphic card in the Device Manager, it does not help either.</p>
<p>I had the VR module working on my older laptop with slower both CPU and graphic card {nvidia rtx 4080, amd ryzen 7900 9}, but this one somehow can not make it work. What should I do? Thanks</p>

---

## Post #2 by @muratmaga (2025-09-12 00:34 UTC)

<aside class="quote no-group" data-username="johny723" data-post="1" data-topic="45348">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/7ea924/48.png" class="avatar"> johny723:</div>
<blockquote>
<p>Seems like the Slicer3D works with an internal graphic card of my laptop</p>
</blockquote>
</aside>
<p>You should use the GPU setting in Windows to force it to 4090. By default it favors built-in GPU for power optimization.</p>

---

## Post #3 by @johny723 (2025-11-30 03:37 UTC)

<p>So far I have tried the following:</p>
<p>installing the latest version of Cuda</p>
<p>uninstalling and installing Slicer3D 5.8, 5.9, and 5.10</p>
<p>disabling integrated GPU in Device manager</p>
<p>forcing NVDIA GPU for 3D in NVDIA control panel / both globally and specifically for Slicer3D</p>
<p>Nothing works. My old laptop can use RTX 4070 and it uses it all the time instead of the integrated card for both Slicer 3D and VR, while my new { much more powerful} laptop can not use the RTX 4090 for anything related to Slicer 3D.</p>
<p>Any new ideas?</p>

---

## Post #4 by @yufu_cao (2025-11-30 23:18 UTC)

<p>Windows 11 settings:</p>
<blockquote>
<p>On Windows 11 you can force 3D Slicer (or any other program) to use the dedicated NVIDIA GPU:</p>
<ol>
<li>Open <strong>Settings → System → Display → Graphics</strong>.</li>
<li>At the top, make sure <strong>Hardware-accelerated GPU scheduling</strong> is <strong>On</strong>.</li>
<li>In the <strong>Custom settings for applications</strong> section, click <strong>Add an app → Add a desktop app</strong>, then browse to your Slicer installation folder and select <strong><code>Slicer.exe</code></strong> (for example:<br>
<code>C:\Program Files\slicer.org\3D Slicer 5.10.0\Slicer.exe</code>).</li>
<li>After Slicer appears in the list, click it to expand the entry and choose <strong>GPU preference</strong>.</li>
<li>In the drop-down menu, change it from <strong>Let Windows decide</strong> to <strong>High performance (NVIDIA GeForce RTX 50xx/40xx)</strong>.</li>
<li>Click <strong>Save</strong> if Windows shows a confirmation.</li>
</ol>
<p>After this, Windows will always try to launch Slicer with the high-performance NVIDIA GPU instead of the integrated Intel graphics.</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04f708f18b21e01ae9b71b386201833e08f2f4f5.png" data-download-href="/uploads/short-url/HVb976ANUKTvdRgypGmPtIDxQN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04f708f18b21e01ae9b71b386201833e08f2f4f5_2_627x500.png" alt="image" data-base62-sha1="HVb976ANUKTvdRgypGmPtIDxQN" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04f708f18b21e01ae9b71b386201833e08f2f4f5_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04f708f18b21e01ae9b71b386201833e08f2f4f5_2_940x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04f708f18b21e01ae9b71b386201833e08f2f4f5.png 2x" data-dominant-color="E8EDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1200×956 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @johny723 (2025-11-30 23:48 UTC)

<p>My MSI Titan Gt77 seems to be stubborn and does not like those changes. On the bright side, Slicer 5.11 uses both my GPUs, so the 4090 does not idle anymore at last.</p>
<p>Sticking with the 5.11 appears to be the easiest way to fix this issue.</p>

---

## Post #6 by @pieper (2025-12-01 03:42 UTC)

<p>I don’t use windows often, so this may be wrong, but you may also need to set <code>SlicerApp-real.exe</code> to use the discrete GPU.</p>

---
