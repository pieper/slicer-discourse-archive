---
topic_id: 32004
title: "Cant Hide Segmentations"
date: 2023-10-03
url: https://discourse.slicer.org/t/32004
---

# Can't Hide Segmentations

**Topic ID**: 32004
**Date**: 2023-10-03
**URL**: https://discourse.slicer.org/t/cant-hide-segmentations/32004

---

## Post #1 by @sldamico13 (2023-10-03 04:07 UTC)

<p>Operating system: MacOS<br>
Slicer version: 5.4.0<br>
Expected behavior: Segmentations are not visible when hidden in both 3D and sectional views.<br>
Actual behavior: Segmentations cannot be hidden. I can only see the background segmentation which is just a yellow box. I tried opening the file in the 5.0.3 version as well but the same thing happened. Turning the eye icon on causes the segmentations to overlay themselves, and turning the eye icon off doesn’t remove the segmentations. How can I fix this?</p>

---

## Post #2 by @muratmaga (2023-10-03 04:48 UTC)

<p>that functionality works well. make sure you have only one segmentation in your scene. sounds like you have an extra, a left over one.</p>

---

## Post #3 by @lassoan (2023-10-03 13:42 UTC)

<p>If your save the scene, restart Slicer, and load it again does it still not work as you expect? Can you share the scene with us (save the scene as an scene bundle file, upload it somewhere, and post the link here)?</p>

---

## Post #4 by @sldamico13 (2023-10-03 14:23 UTC)

<p>Saving and restarting Slicer doesn’t seem to work. This problem started affecting the 3D view after Slicer quit unexpectedly a few minutes after saving.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/scl/fi/spihz0b6g1y0lzj31ss3f/2023-04-24-Scene.mrb?rlkey=0w3gyxw3wlor0hpwnxos2qy5w&amp;dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/scl/fi/spihz0b6g1y0lzj31ss3f/2023-04-24-Scene.mrb?rlkey=0w3gyxw3wlor0hpwnxos2qy5w&amp;dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img width="160" height="160" src="https://www.dropbox.com/static/metaserver/static/images/opengraph/opengraph-content-icon-file-unknown-landscape.png" class="thumbnail onebox-avatar">

<h3><a href="https://www.dropbox.com/scl/fi/spihz0b6g1y0lzj31ss3f/2023-04-24-Scene.mrb?rlkey=0w3gyxw3wlor0hpwnxos2qy5w&amp;dl=0" target="_blank" rel="noopener nofollow ugc">2023-04-24-Scene.mrb</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
