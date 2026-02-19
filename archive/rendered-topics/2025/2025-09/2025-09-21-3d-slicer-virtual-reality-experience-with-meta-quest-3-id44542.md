---
topic_id: 44542
title: "3D Slicer Virtual Reality Experience With Meta Quest 3"
date: 2025-09-21
url: https://discourse.slicer.org/t/44542
---

# 3D Slicer Virtual Reality Experience with Meta Quest 3

**Topic ID**: 44542
**Date**: 2025-09-21
**URL**: https://discourse.slicer.org/t/3d-slicer-virtual-reality-experience-with-meta-quest-3/44542

---

## Post #1 by @manjula (2025-09-21 07:25 UTC)

<p>I’m writing to share my initial experience using the 3D Slicer VR extension with a Meta Quest 3 on Windows 11 and to ask for some guidance.</p>
<p><strong>My Setup:</strong></p>
<ul>
<li>
<p><strong>Headset:</strong> Meta Quest 3</p>
</li>
<li>
<p><strong>PC OS:</strong> Windows 11</p>
</li>
<li>
<p><strong>Connection Methods Tested:</strong> Meta Link (Air Link) and SteamVR</p>
</li>
</ul>
<p><strong>Observations:</strong></p>
<ol>
<li>
<p><strong>Meta Link (Wireless):</strong> The connection was laggy and unstable. I attribute this to my 2.4 GHz Wi-Fi network and the lack of a direct cable connection.</p>
</li>
<li>
<p><strong>SteamVR (Wireless):</strong> This provided a much smoother and more responsive experience, even on the same network configuration. The rendering and head-tracking were excellent.</p>
</li>
<li>
<p><strong>3D Slicer VR Extension (via SteamVR):</strong> While the scene rendered perfectly, I encountered issues with controller bindings. Most controls were non-functional, except for basic vertical movement (up and down). My attempts to reconfigure bindings did not resolve the issue.</p>
</li>
<li>
<p><strong>Standalone SlicerVR Application:</strong> In contrast, launching the SlicerVR application directly was far more successful. All controller functions worked as expected, allowing for full interaction with the models.</p>
</li>
</ol>
<p>Based on this, I have a few questions for the community:</p>
<ul>
<li>
<p>Is the controller binding issue with the VR extension a known problem for the Meta Quest 3?</p>
</li>
<li>
<p>Are there recommended SteamVR binding profiles or a specific setup guide for the Quest 3 that I might have missed?</p>
</li>
<li>
<p>What is the recommended workflow for the best VR experience? Is using the standalone SlicerVR app the preferred method over launching it from within the main 3D Slicer application?</p>
</li>
</ul>
<p>Thank you for any insights or advice you can offer.</p>
<p>Thank you</p>
<p><strong>3D Slicer Virtual Reality Extension</strong></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/badc41289595e6c442afe57d17fbd61bf7a3dbc6.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c828ad901c7c662556701511bb69ff25ada5831.png" data-video-base62-sha1="qF2HyYInleB07n776BUDEkyFniS.mp4">
  </div><p></p>
<p><strong>Direct App</strong></p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d80ee1eaf6094ce88d0c4765dd659a81f9b616c0.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a837e6f82fe3de69ae222cb48e3d3d1f3ee511e.png" data-video-base62-sha1="uPl1bPMEIFRtRHr8E6sQ4mEP4iI.mp4">
  </div><p></p>

---

## Post #2 by @LucasGandel (2025-09-30 09:35 UTC)

<p>Thanks for sharing your experience!</p>
<blockquote>
<p>Is the controller binding issue with the VR extension a known problem for the Meta Quest 3?</p>
</blockquote>
<p>Looking at the <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/6da6ab13451ae324092b6e6c0be3434279cd95a1/DeveloperGuide.md?plain=1#L41" rel="noopener nofollow ugc">DeveloperGuide</a>, it looks like controller bindings are directly fetch from VTK which does not provide default bindings for the Meta Quest 3. I have a <a href="https://gitlab.kitware.com/vtk/vtk/-/merge_requests/11965/diffs" rel="noopener nofollow ugc">draft PR</a> on VTK that should provide support for basic interactions with this device when using OpenXR as a backend.</p>
<p>You can try to locate the json files provided by the 3D Slicer VR Extension on your machine and apply the modifications from my PR and it should work.</p>

---

## Post #3 by @cpinter (2025-09-30 10:10 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a> Just letting you know that the SlicerVR extension is up again since quite recently, so I suggest using the latest Slicer / SlicerVR.</p>

---
