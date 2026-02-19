---
topic_id: 8214
title: "Slicelet Performance"
date: 2019-08-28
url: https://discourse.slicer.org/t/8214
---

# Slicelet Performance

**Topic ID**: 8214
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/slicelet-performance/8214

---

## Post #1 by @burnhamd (2019-08-28 19:27 UTC)

<p>I have been working on a slicelet where I create my own “main window”.  I originally decided to go this route so that I could define the UI in the QTDesigner.  My UI diverges quite a bit from the default main window.</p>
<p>However, I noticed that having the two layoutmanager widgets causes a performance hit on my system.  If I add volume rendering and have a second layout manager, I am only able to get about 1fps.</p>
<p>Is the current method of implementing slicelets to only modify the default main window of slicer?  This seems like it would make it difficult to develop a more customized UI since I would need to hide existing widgets using code and then add widgets individually to the main window.  Are there any suitable alternatives to this approach?</p>

---

## Post #2 by @cpinter (2019-08-28 19:45 UTC)

<p>The older way of creating slicelets by adding a new window with its own layout manager was surpassed by the newer way (originally called guidelets, which entails customizing the existing main window) just because of these performance limitations (and partly because Slicer does not fully support more than one layout managers).</p>
<p>If you don’t want to hide UI elements but want to go the additive way, you can use the new SlicerCustomApp concept instead<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/2717525?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" target="_blank" rel="nofollow noopener">KitwareMedical/SlicerCustomAppTemplate</a></h3>

<p>Template to be used as a starting point for creating a custom 3D Slicer application - KitwareMedical/SlicerCustomAppTemplate</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
