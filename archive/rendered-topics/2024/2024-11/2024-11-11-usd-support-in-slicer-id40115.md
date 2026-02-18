# USD support in Slicer

**Topic ID**: 40115
**Date**: 2024-11-11
**URL**: https://discourse.slicer.org/t/usd-support-in-slicer/40115

---

## Post #1 by @muratmaga (2024-11-11 04:57 UTC)

<p>There was some talk about USD format support in Slicer (e.g., <a href="https://discourse.slicer.org/t/open-source-human-anatomy-atlas/17734/7" class="inline-onebox">Open source Human Anatomy Atlas - #7 by pieper</a>)</p>
<p>Was there any movement towards it?</p>

---

## Post #2 by @pieper (2024-11-11 14:36 UTC)

<p>I haven’t seen a lot of interest in it, but there is a set of vtk C++ code for exporting to it if we wanted to.  Do you have a particular use case in mind?</p>
<aside class="onebox githubrepo" data-onebox-src="https://github.com/NVIDIA-Omniverse/ParaViewConnector">
  <header class="source">

      <a href="https://github.com/NVIDIA-Omniverse/ParaViewConnector" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/8ee4699206425fdb069bb800e0ab4e15/NVIDIA-Omniverse/ParaViewConnector" class="thumbnail">

  <h3><a href="https://github.com/NVIDIA-Omniverse/ParaViewConnector" target="_blank" rel="noopener">GitHub - NVIDIA-Omniverse/ParaViewConnector: Plugin for Kitware ParaView adding Omniverse and...</a></h3>

    <p><span class="github-repo-description">Plugin for Kitware ParaView adding Omniverse and USD support</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @muratmaga (2024-11-11 16:56 UTC)

<p>Nothing in particular at the moment, but given it is popularity we might eventually need it as an export format in Slicer. Particularly if it can support (not sure if it does) more object types than glTF.</p>

---

## Post #4 by @pieper (2024-11-11 17:13 UTC)

<p>USD was designed for a very different use case so probably could export many things (rendering related and maybe transforms and such) and also define extensions  for slicer-specific data concepts.  I just haven’t seen a lot of demand for it yet but maybe Blender i/o will be a driver.  Since Omniverse is a paid service it’s hard for me to see it gaining much traction for our community but we’ll see how things evolve.</p>

---

## Post #5 by @jcfr (2024-11-11 17:18 UTC)

<p>The following discussion is likely relevant:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://discourse.vtk.org/t/openusd-support/12198">
  <header class="source">
      <img src="https://discourse.vtk.org/uploads/default/optimized/1X/6c8eb860cf266ca35755a0f95e95251fbe63514d_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://discourse.vtk.org/t/openusd-support/12198" target="_blank" rel="noopener" title="04:10PM - 24 August 2023">VTK – 24 Aug 23</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/369;"><img src="https://discourse.vtk.org/uploads/default/original/1X/b7d45ff6520965c4fbd148f8d0b1f7720956fa24.png" class="thumbnail" width="690" height="369"></div>

<div class="title-wrapper">
  <h3><a href="https://discourse.vtk.org/t/openusd-support/12198" target="_blank" rel="noopener">OpenUSD Support</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #0088CC;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Development</span>
        </span>
      </span>
    <div class="topic-header-extra">
      <div class="list-tags">
        <div class="discourse-tags">
          <svg class="fa d-icon d-icon-tag svg-icon svg-string"><use href="#tag"></use></svg>
            <span class="discourse-tag simple">proposal</span>
        </div>
      </div>
    </div>
  </div>
</div>

  <p>I would like to understand the VTK community’s perspective on potential support for the OpenUSD standard. This thread was prompted by discussion at today’s VTK.js developers meeting.  Overview Universal Scene Description is an open source project...</p>

  <p>
    <span class="label1">Reading time: 2 mins 🕑</span>
      <span class="label2">Likes: 9 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
