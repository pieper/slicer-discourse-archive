---
topic_id: 33603
title: "Creating Segmentation On Stl Files To Get Centreline Of Arte"
date: 2024-01-03
url: https://discourse.slicer.org/t/33603
---

# Creating Segmentation on stl files to get centreline of artery

**Topic ID**: 33603
**Date**: 2024-01-03
**URL**: https://discourse.slicer.org/t/creating-segmentation-on-stl-files-to-get-centreline-of-artery/33603

---

## Post #1 by @Luxalyn (2024-01-03 15:02 UTC)

<p>Hello;<br>
I’m extremely new to 3D Slicer, and for a couple days I’ve been trying to implement segmentation on an artery stl file to get the centerline of it. I have tried these steps but it didnt work. i dont know why and all i can see is my model on the right top corner.</p>
<ul>
<li>Drag-and-drop STL file to Slicer window and in Add data dialog, choose “Segmentation” in Description column (there is no need to load as model and then import to segmentation but you can directly load as segmentation)</li>
<li>Go to Segment Editor and click “Specify geometry” button (next to Master volume selector)</li>
<li>Choose current segmentation node as source geometry, set spacing values, and click OK</li>
</ul>
<p>May someone please show me how to apply segmentation to a STL file to get the centerline of it?</p>
<p>Sincerely</p>
<p>Ali</p>

---

## Post #2 by @Deep_Learning (2024-01-03 17:48 UTC)

<p>Check out the VMTK extension</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/vmtk/SlicerExtension-VMTK">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/vmtk/SlicerExtension-VMTK" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/4c881939259cc210e975760989cc95a674cc0d2884a0814d0ca74a96b8355e9c/vmtk/SlicerExtension-VMTK" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/vmtk/SlicerExtension-VMTK" target="_blank" rel="noopener nofollow ugc">GitHub - vmtk/SlicerExtension-VMTK</a></h3>

  <p>Contribute to vmtk/SlicerExtension-VMTK development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
