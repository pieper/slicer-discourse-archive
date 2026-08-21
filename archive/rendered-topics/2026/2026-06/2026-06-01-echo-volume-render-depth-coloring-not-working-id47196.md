---
topic_id: 47196
title: "Echo Volume Render depth coloring not working"
date: 2026-06-01
url: https://discourse.slicer.org/t/47196
last_bumped: 2026-08-20T17:55:03.389Z
---

# Echo Volume Render depth coloring not working

**Topic ID**: 47196
**Date**: 2026-06-01
**URL**: https://discourse.slicer.org/t/echo-volume-render-depth-coloring-not-working/47196

---

## Post #1 by @aabrown100-git (2026-06-01 21:49 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2.jpeg" data-download-href="/uploads/short-url/i16byBHVexlMGQkd2gnWoeJkopk.jpeg?dl=1" title="Screenshot 2026-06-01 at 2.47.03 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2_2_690x393.jpeg" alt="Screenshot 2026-06-01 at 2.47.03 PM" data-base62-sha1="i16byBHVexlMGQkd2gnWoeJkopk" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e46f50c77ff3b37980b017d37871a166691faf2_2_1380x786.jpeg 2x" data-dominant-color="A09EA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-06-01 at 2.47.03 PM</span><span class="informations">2672×1522 519 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My volume rendering of a 3D echo image does not show depth dependent coloring, like in this demo video: <a href="https://www.youtube.com/watch?v=hzxzUILNhnA&amp;list=PLIFpHI5hhxkszTWJTaWDM-eGTR8zBubSA&amp;index=14" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=hzxzUILNhnA&amp;list=PLIFpHI5hhxkszTWJTaWDM-eGTR8zBubSA&amp;index=14</a>. I tried adjusting the various sliders, but they seems to have no effect, except for “Depth coloring” which just changes the render color uniformly.</p>
<p>3D Slicer 5.10.0, 2026 Macbook Pro, M5 Pro chip.</p>

---

## Post #2 by @aabrown100-git (2026-08-03 19:25 UTC)

<p>Pinging this in hopes of getting some advice!</p>

---

## Post #3 by @mikebind (2026-08-05 05:55 UTC)

<p>Try narrowing the range on the depth coloring slider, it is currently stretching the depth colormap over 500 mm, and my guess is that the rendered echo region covers a small slice of that, so the color range you see is just a small slice of the colormap.  Slide the whole range until the rendered region is a medium depth color, then bring in the edges until you see the range of the colormap that you would like (presumably most of it).</p>

---

## Post #4 by @aabrown100-git (2026-08-05 18:52 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> Thanks for the advice. I tried increasing the “Depth range” to [-10000, 10000], and decreasing to [-10, 10]. For each, sliding the range as well as the min and max had no effect. I’ve attached screen recordings. Please let me know if I’m doing anything obviously wrong!</p>
<div class="youtube-onebox lazy-video-container" data-video-id="Y1rn2ysKFHg" data-video-title="Screen Recording 2026 08 05 at 11 25 37 AM" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Y1rn2ysKFHg" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://i.ytimg.com/vi/Y1rn2ysKFHg/hqdefault.jpg" title="Screen Recording 2026 08 05 at 11 25 37 AM" width="480" height="360">
  </a>
</div>

<div class="youtube-onebox lazy-video-container" data-video-id="jbEk3bYk2ZU" data-video-title="Screen Recording 2026 08 05 at 11 28 23 AM" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=jbEk3bYk2ZU" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://i.ytimg.com/vi/jbEk3bYk2ZU/hqdefault.jpg" title="Screen Recording 2026 08 05 at 11 28 23 AM" width="480" height="360">
  </a>
</div>


---

## Post #5 by @mikebind (2026-08-05 20:27 UTC)

<p>Hm, that does seem odd. I just confirmed that I can get sensible depth renderings using this module.  I’m using Slicer 5.10.0, the same as you.</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91e20786581ff97d5f850cf3545beaa88ddeabc9.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d0226be85b60a669120fa61647f817b1b98ccf3.jpeg" data-video-base62-sha1="kOxuVZA55zrIvOX8wGPyufkqqud.mp4">
  </div>I have observed in the past that Echo Volume Render does not play well with any manual adjustment of settings in the Volume Rendering module.  Any chance that you touched something there?  If so, I would try just reopening Slicer and starting from scratch in the Echo Volume Render module, which will reset any confused settings. Beyond that, I would try a different echo volume to see if the issue seems specific to this dataset.  Has this worked for you in the past?<p></p>

---

## Post #6 by @aabrown100-git (2026-08-13 22:33 UTC)

<p>Thanks Mike, I tried reopening Slicer and also using a different echo volume, but no dice. (This hasn’t worked for me in the past).</p>
<p>When you get a chance, could you try the following steps and let me know if it works.</p>
<ol>
<li>
<p>Open Slicer 5.12.3</p>
</li>
<li>
<p>Install SlicerHeart extension</p>
</li>
<li>
<p>Download the SlicerHeart “Mitral” dataset in the Sample Data module.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1.jpeg" data-download-href="/uploads/short-url/6t9FMEhFRgTl6F5blJVhKOcYsr7.jpeg?dl=1" title="Screenshot 2026-08-13 at 3.30.00 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1_2_690x410.jpeg" alt="Screenshot 2026-08-13 at 3.30.00 PM" data-base62-sha1="6t9FMEhFRgTl6F5blJVhKOcYsr7" width="690" height="410" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1_2_690x410.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1_2_1035x615.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d58c4fdf001550b8cad95913e3951361beb7da1_2_1380x820.jpeg 2x" data-dominant-color="B0ADAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-08-13 at 3.30.00 PM</span><span class="informations">2928×1744 550 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>Switch to the Echo Volume Render module and see if the volume render has depth color (it does not for me)</li>
</ol>

---

## Post #7 by @mikebind (2026-08-18 14:45 UTC)

<p>I got a chance to try this, and yes, I see some depth coloring before adjusting any settings (just loaded the “Mitral” dataset) and hit Apply after installing Slicer 5.12.3 and SlicerHeart.  This is what I see (just rotated the 3D a bit to show the color variation a little better):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8593e04a78fb942ae4f14f14a5b2999092aadd38.jpeg" data-download-href="/uploads/short-url/j3GkfX4GRaOoaNbAPQKcq5bRsRa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8593e04a78fb942ae4f14f14a5b2999092aadd38_2_690x396.jpeg" alt="image" data-base62-sha1="j3GkfX4GRaOoaNbAPQKcq5bRsRa" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8593e04a78fb942ae4f14f14a5b2999092aadd38_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8593e04a78fb942ae4f14f14a5b2999092aadd38_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8593e04a78fb942ae4f14f14a5b2999092aadd38_2_1380x792.jpeg 2x" data-dominant-color="717074"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1102 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @aabrown100-git (2026-08-19 04:33 UTC)

<p>Thanks Mike, I also tried again just to be sure and I still don’t see any depth coloring. Any idea what might be happening here? I have a 2026 MacBook Pro with M5 Pro chip, if that’s relevant.</p>
<p>If anybody else comes across this issue, could you please download the sample “Mitral” dataset and report if you see depth coloring or not.</p>

---

## Post #9 by @mikebind (2026-08-20 06:37 UTC)

<p>I’m on Windows 11.  This could potentially be a Mac issue.  Perhaps someone else can weigh in on whether they can reproduce this on a recent Mac.</p>

---

## Post #10 by @muratmaga (2026-08-20 17:55 UTC)

<p>Same here, no depth rendering on M3 Pro. I asked claude to diagnose and fix it. It seems mac specific. With the fix it renders correctly:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a8f8452b9b9e9f4cf5d8070102ba5917262b73e.jpeg" data-download-href="/uploads/short-url/3MXTEVFOjuxeiRqsdD6gp2866Au.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8f8452b9b9e9f4cf5d8070102ba5917262b73e_2_690x467.jpeg" alt="image" data-base62-sha1="3MXTEVFOjuxeiRqsdD6gp2866Au" width="690" height="467" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8f8452b9b9e9f4cf5d8070102ba5917262b73e_2_690x467.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8f8452b9b9e9f4cf5d8070102ba5917262b73e_2_1035x700.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a8f8452b9b9e9f4cf5d8070102ba5917262b73e_2_1380x934.jpeg 2x" data-dominant-color="22221F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1442×976 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It should open a PR on the repo shortly.</p>
<h2><a name="p-135480-diagnosis-reading-a-vtk-shader-variable-that-no-longer-exists-1" class="anchor" href="#p-135480-diagnosis-reading-a-vtk-shader-variable-that-no-longer-exists-1" aria-label="Heading link"></a>Diagnosis: reading a VTK shader variable that no longer exists</h2>
<p>I drove your running Slicer over the MCP server on <code>localhost:2026</code>, reproduced the thread’s exact steps (Mitral sample → Echo Volume Render), and instrumented the GLSL. It is <strong>not</strong> a Mac driver bug in the general sense — it’s a real bug in SlicerHeart that only <em>manifests</em> on your driver.</p>
<p><strong>Environment:</strong> Slicer 5.12.3 (rev 34627), macOS 26.6.1, Apple M3 Pro, OpenGL 4.1 Metal, <strong>VTK 9.6.2</strong>.</p>
<h3><a name="p-135480-root-cause-2" class="anchor" href="#p-135480-root-cause-2" aria-label="Heading link"></a>Root cause</h3>
<p><code>EchoVolumeRender.py:659</code> computes the camera position for the depth ramp from a shader global:</p>
<pre><code class="lang-auto">vec3 camInTexCoord = (ip_inverseTextureDataAdjusted * vec4(g_eyePosObj.xyz,1.0)).xyz;

</code></pre>
<p><code>g_eyePosObj</code> was assigned by VTK’s ray-cast shader up to <strong>VTK 9.2</strong>:</p>
<pre><code class="lang-auto">g_eyePosObj = in_inverseVolumeMatrix[0] * vec4(in_cameraPos, 1.0);   // vtkVolumeShaderComposer.h, v9.2.6:435

</code></pre>
<p><strong>VTK 9.3 deleted that assignment</strong> and replaced it with the uniform <code>in_eyePosObjs[]</code>. The bare declaration <code>vec4 g_eyePosObj;</code> still sits in <code>raycasterfs.glsl:32</code>, so the shader compiles cleanly — it just reads an <strong>uninitialized variable</strong>. I dumped the linked fragment shader from your GPU to confirm: <code>g_eyePosObj</code> appears exactly twice, the declaration and SlicerHeart’s read. It is never written.</p>
<h3><a name="p-135480-evidence-from-your-gpu-3" class="anchor" href="#p-135480-evidence-from-your-gpu-3" aria-label="Heading link"></a>Evidence from your GPU</h3>
<p>Rendering <code>dist</code> (the near↔far interpolation ratio) directly as greyscale, over the volume region:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>eye-position expression</th>
<th>dist <span class="mention">@00</span>° (mean, std)</th>
<th>dist@90@90°</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>g_eyePosObj</code> (shipped)</td>
<td><strong>0.0, 0.0</strong></td>
<td><strong>0.0, 0.0</strong></td>
</tr>
<tr>
<td><code>vec3(0.0)</code> (what a zero-init driver gives)</td>
<td>61.9, 102.6</td>
<td>47.6, 84.3</td>
</tr>
<tr>
<td><code>in_eyePosObjs[0]</code> (correct)</td>
<td>49.8, 82.3</td>
<td>40.1, 71.7</td>
</tr>
</tbody>
</table>
</div><p><code>dist</code> collapses to <strong>exactly 0 everywhere</strong>, so <code>mix(rgbNear, rgbFar, 0)</code> returns <code>rgbNear</code> for every voxel. That is precisely the reported symptom: the Depth coloring slider still moves <code>hueNear</code>, so the whole volume shifts hue <em>uniformly</em>, and no other slider does anything visible.</p>
<p>Hue statistics confirm the shipped shader is completely camera-independent, while the fixed one tracks the camera:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>camera azimuth</th>
<th>shipped (hue mean, std)</th>
<th>fixed</th>
</tr>
</thead>
<tbody>
<tr>
<td>0°</td>
<td>0.577, 0.059</td>
<td>−0.181, 0.193</td>
</tr>
<tr>
<td>45°</td>
<td>0.581, 0.056</td>
<td>−0.111, 0.209</td>
</tr>
<tr>
<td>90°</td>
<td>0.579, 0.060</td>
<td>−0.042, 0.260</td>
</tr>
<tr>
<td>135°</td>
<td>0.580, 0.057</td>
<td>−0.092, 0.245</td>
</tr>
</tbody>
</table>
</div><p>Visual comparison written to <code>/tmp/echo_depth_comparison.png</code> — top row shipped (0°, 90°), bottom row fixed:</p>
<p>The fix produces exactly the tutorial appearance: near structures warm/tan, far structures blue, and the ramp rotates with the view.</p>
<h3><a name="p-135480-why-mike-couldnt-reproduce-it-on-windows-4" class="anchor" href="#p-135480-why-mike-couldnt-reproduce-it-on-windows-4" aria-label="Heading link"></a>Why Mike couldn’t reproduce it on Windows</h3>
<p>Reading an uninitialized GLSL global is undefined behavior. NVIDIA/Windows drivers zero-initialize, so <code>g_eyePosObj</code> reads as <code>(0,0,0,0)</code> and <code>camInTexCoord</code> becomes a fixed point near the world origin — which still yields a plausible-looking gradient (row 2 of the table above), so it <em>looks</em> like it works. It’s actually anchored to the world origin rather than the camera, i.e. a latent bug there too. Apple’s compiler leaves the register with garbage far outside the volume, <code>dist</code> clamps to 0, and the effect vanishes entirely. Any Mac vs. Windows split here is a coin flip on driver behavior, not a designed difference.</p>
<h3><a name="p-135480-fix-5" class="anchor" href="#p-135480-fix-5" aria-label="Heading link"></a>Fix</h3>
<p>Three lines in <code>EchoVolumeRender.__init__</code>, patch at <code>/private/tmp/claude-1950572333/-Users-amaga/74cd5809-e665-448d-b0fd-43749d08a8fd/scratchpad/echovolumerender-depth-coloring.patch</code>:</p>
<pre><code class="lang-auto">    if vtkVersion &gt;= 903:
      self.computeColorReplacement = self.computeColorReplacement.replace(
        "g_eyePosObj.xyz", "in_eyePosObjs[0].xyz")

</code></pre>
<p><code>in_eyePosObjs[i]</code> is the eye position in dataset space (<code>vtkOpenGLGPUVolumeRayCastMapper.cxx:3519</code>) — the same space the old <code>g_eyePosObj</code> held, so it’s a drop-in. VTK ≤ 9.2 keeps the old path. SlicerHeart <code>master</code> still has the bug at line 659, and I found no existing issue for it.</p>
<p>Two notes:</p>
<ul>
<li>I left the fixed shader <strong>active in your running Slicer session only</strong> — the installed module file is untouched, so it reverts on restart.</li>
<li>Separately, your log shows <code>vtkOpenGLVolumeOpacityTable: does not support the required texture size of 262144, falling back to 16384</code>. That’s macOS’s max texture size and is unrelated to this — worth knowing but not the cause.</li>
</ul>

---
