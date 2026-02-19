---
topic_id: 39629
title: "Visualization Of A Vtk File"
date: 2024-10-10
url: https://discourse.slicer.org/t/39629
---

# Visualization of a vtk file

**Topic ID**: 39629
**Date**: 2024-10-10
**URL**: https://discourse.slicer.org/t/visualization-of-a-vtk-file/39629

---

## Post #1 by @lolamartinalonso (2024-10-10 08:50 UTC)

<p>Hi community,</p>
<p>I am trying to open a vtk file in 3DSlicer. I open it as Model, and then in the Model module I try to visualize it but I can not see anything.</p>
<p>In Paraview I have to visualize it as Point Gaussian.</p>
<p>Can you help me visualizing it?</p>
<p>This is the files that I am trying to open:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/88713e7c25a1bbcdac55c09694ca4acb20241010045215/491e87?t_exp=1728795135&amp;t_lsid=6aa2f330-f2a8-4a2c-b7a9-0bc110951a9b&amp;t_s=download_link&amp;t_ts=1728535935">
  <header class="source">
      <img src="https://wetransfer.com/favicon.ico" class="site-icon" width="64" height="64">

      <a href="https://wetransfer.com/downloads/88713e7c25a1bbcdac55c09694ca4acb20241010045215/491e87?t_exp=1728795135&amp;t_lsid=6aa2f330-f2a8-4a2c-b7a9-0bc110951a9b&amp;t_s=download_link&amp;t_ts=1728535935" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://wetransfer.com/downloads/88713e7c25a1bbcdac55c09694ca4acb20241010045215/491e87?t_exp=1728795135&amp;t_lsid=6aa2f330-f2a8-4a2c-b7a9-0bc110951a9b&amp;t_s=download_link&amp;t_ts=1728535935" target="_blank" rel="noopener nofollow ugc">Big files vtk</a></h3>

  <p>2 files sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks a lot</p>

---

## Post #2 by @pieper (2024-10-10 13:49 UTC)

<p>This is an unstructured grid with points but no cells.  We don’t have a rendering mode for that by default because it hasn’t come up before or at least not offen enough for someone to add a mode.  You can use vtk filters to add cells or create a polydata with glyphs at the points, whatever make sense for your use case.</p>
<p>If you find something useful it could be added to the models displayable manager to handle this case.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec78979a3bae200d05e8ea8f0289e25b7437cf6c.png" data-download-href="/uploads/short-url/xJV38zp3TbRv4mJq4ysNQydm4B6.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec78979a3bae200d05e8ea8f0289e25b7437cf6c_2_690x273.png" alt="image" data-base62-sha1="xJV38zp3TbRv4mJq4ysNQydm4B6" width="690" height="273" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec78979a3bae200d05e8ea8f0289e25b7437cf6c_2_690x273.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec78979a3bae200d05e8ea8f0289e25b7437cf6c_2_1035x409.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec78979a3bae200d05e8ea8f0289e25b7437cf6c_2_1380x546.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1612×638 67.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
