---
topic_id: 36237
title: "3Dslicer Crashes In Vritual Reality Module When Depressing G"
date: 2024-05-17
url: https://discourse.slicer.org/t/36237
---

# 3DSlicer crashes in Vritual Reality module when depressing grip buttons on both controllers

**Topic ID**: 36237
**Date**: 2024-05-17
**URL**: https://discourse.slicer.org/t/3dslicer-crashes-in-vritual-reality-module-when-depressing-grip-buttons-on-both-controllers/36237

---

## Post #1 by @raisazf (2024-05-17 17:20 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.6.2<br>
Expected behavior: volume transformation with controllers in Virtual Reality module<br>
Actual behavior: 3DSlicer crashes when grip buttons pressed simultaneously on both controllers</p>
<p>Hello,</p>
<p>I’m trying to run 3DSlicer Virtual Reality on the Meta Quest Pro with Meta Quest Touch Pro controllers. Currently, I’m able to fly using using thumbstick on the right controller. However, 3DSlicer crashes when grip button depressed on both controllers.</p>
<p>Software and GPU info:</p>
<p>Meta Quest Link App version 65.0.0.499.343</p>
<p>Steam Beta Branch:  Stable Client<br>
Steam Version:  1715635533<br>
Steam Client Build Date:  Mon, May 13 6:04 PM UTC -08:00<br>
Steam Web Build Date:  Mon, May 13 2:06 PM UTC -08:00<br>
Steam API Version:  SteamClient021.</p>
<p>with SteamVR 2.5.5</p>
<p>GPU: NVIDIA DeForce RTX 4090 (laptop) with 16GB RAM</p>
<p>I’d appreciate your assistance in resolving this issue.</p>
<p>Best,<br>
Raisa</p>

---

## Post #2 by @cpinter (2024-05-21 08:56 UTC)

<p>SlicerVR is currently under major rework, and although the majority of the new infrastructure is in place, there are still problems that can be expected.</p>
<p>I suggest that you see if this problem is already listed here</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/SlicerVirtualReality/issues">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/80a9c14d6c2f886262b762ddab0c41eebbe139f9cd41810ea1775ec6a9daa630/KitwareMedical/SlicerVirtualReality" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues" target="_blank" rel="noopener">Issues · KitwareMedical/SlicerVirtualReality</a></h3>

  <p>A Slicer extension that enables user to interact with a Slicer scene using virtual reality. - Issues · KitwareMedical/SlicerVirtualReality</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
and add a new ticket there.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> please let us know if you disagree.</p>

---
