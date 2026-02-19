---
topic_id: 14941
title: "Remove Dental Fillings Artifacts From Ct Scan"
date: 2020-12-08
url: https://discourse.slicer.org/t/14941
---

# Remove dental fillings artifacts from CT scan

**Topic ID**: 14941
**Date**: 2020-12-08
**URL**: https://discourse.slicer.org/t/remove-dental-fillings-artifacts-from-ct-scan/14941

---

## Post #1 by @jess (2020-12-08 15:05 UTC)

<p>I’m new to 3D Slicer and medical imaging in general. I have a CT scan of my head and wanted to extract a clean 3d model of my skull. My dental fillings appear to cause some kind of reflections that show as rays in the scan, and they look like spikes coming out of my mouth in the 3d model.</p>
<p>Is there anyway to correct this in Slicer or will I have to just manually edit the model?</p>

---

## Post #2 by @lassoan (2020-12-08 19:46 UTC)

<p>In general, it is better to use iterative reconstruction methods or post-processing to remove metal streak (beam hardening) artifacts.</p>
<p>However, if you just need to fix a specific image then you can remove the artifacts with some manual editing. For example, you can use Scissors effect to detach the artifact from the tooth, remove the detached part using Islands effect, and and touch up the surface using Smoothing effect’s brush.</p>

---

## Post #3 by @manjula (2020-12-08 20:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14941">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>iterative reconstruction methods or post-processing to remove metal streak</p>
</blockquote>
</aside>
<p>Dear Prof Lasso,</p>
<p>Can you please elaborate on both the process and or direct me to a guide?</p>
<p>thanks</p>

---

## Post #4 by @lassoan (2020-12-08 20:58 UTC)

<p>You can reduce beam hardening artifacts by iterative reconstruction methods. These methods work on the sinogram (raw CT acquisition data, before the 3D image is reconstructed), therefore they need to be built into the acquisition system.</p>
<p>There are post-processing methods that try to detect and suppress beam hardening artifacts while not modifying other parts of the image. These only work for specific applications, where you know what to expect to have in the image. For example, it is possible to develop algorithms that automatically recognize teeth and bone in a human head CT and suppress all other bright streaks in the image.</p>

---
