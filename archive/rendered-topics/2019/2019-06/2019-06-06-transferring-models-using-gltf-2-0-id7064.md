---
topic_id: 7064
title: "Transferring Models Using Gltf 2 0"
date: 2019-06-06
url: https://discourse.slicer.org/t/7064
---

# Transferring models using glTF 2.0

**Topic ID**: 7064
**Date**: 2019-06-06
**URL**: https://discourse.slicer.org/t/transferring-models-using-gltf-2-0/7064

---

## Post #1 by @jcfr (2019-06-06 17:09 UTC)

<p>To follow up on an <a href="http://massmail.spl.harvard.edu/public-archives/slicer-users/2017/011982.html">email</a> from <a class="mention" href="/u/pieper">@pieper</a> from 2017</p>
<blockquote>
<p>Transferring models is still a work in progress, but lately I’m looking at glTF [5] as an interesting option.</p>
</blockquote>
<p>I would like to mention that VTK has an improved support for glTF 2.0. It should be possible to create a Slicer extension leveraging the new <a href="https://vtk.org/doc/nightly/html/classvtkGLTFImporter.html#details">vtkGLTFReader</a>, <a href="https://vtk.org/doc/nightly/html/classvtkGLTFImporter.html#details">vtkGLTFImporter</a> and <a href="https://vtk.org/doc/nightly/html/classvtkGLTFExporter.html#details">vtkGLTFExporter</a> classes.</p>
<p>You can read more details about the functionality here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.kitware.com/introducing-gltf-2-0-support-in-vtk-and-paraview/">
  <header class="source">
      <img src="https://www.kitware.com/main/wp-content/themes/kitwarean/assets/img/favicon/android-icon-192x192.png" class="site-icon" width="192" height="192">

      <a href="https://www.kitware.com/introducing-gltf-2-0-support-in-vtk-and-paraview/" target="_blank" rel="noopener">kitware.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/467;"><img src="https://www.kitware.com/main/wp-content/uploads/2019/05/gltf-1.png" class="thumbnail" width="690" height="467"></div>

<h3><a href="https://www.kitware.com/introducing-gltf-2-0-support-in-vtk-and-paraview/" target="_blank" rel="noopener">Introducing glTF 2.0 support in VTK and ParaView</a></h3>

  <p>The glTF file format glTF is an API-neutral royalty-free specification for the efficient transmission and loading of 3D scenes and models by applications. It is specified by Khronos Group (the consortium behind standards such as OpenGL, Vulkan and...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @cpinter (2019-06-06 17:20 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="7064">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>It should be possible to create a Slicer extension leveraging the new <a href="https://vtk.org/doc/nightly/html/classvtkGLTFImporter.html#details">vtkGLTFReader</a>, <a href="https://vtk.org/doc/nightly/html/classvtkGLTFImporter.html#details">vtkGLTFImporter</a> and <a href="https://vtk.org/doc/nightly/html/classvtkGLTFExporter.html#details">vtkGLTFExporter</a> classes</p>
</blockquote>
</aside>
<p>We’re working on this extension. It should be available soon.</p>

---

## Post #4 by @pieper (2019-08-01 19:18 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> - is there news to report on the glTF extension?  For context, I understand that the latest Blender <a href="https://docs.blender.org/manual/en/dev/addons/io_scene_gltf2.html" rel="nofollow noopener">supports glTF import and export</a> so it would be great for interoperability.</p>

---

## Post #5 by @cpinter (2019-08-01 19:37 UTC)

<p>We added a module that exports a valid glTF file from the Slicer scene at the project week. Here it is:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/PerkLab/SlicerOpenAnatomy" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/31492031?s=400&amp;amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/PerkLab/SlicerOpenAnatomy" target="_blank" rel="nofollow noopener">PerkLab/SlicerOpenAnatomy</a></h3>

<p>3D Slicer extension for exporting Slicer scenes to use in the OpenAnatomy.org browser - PerkLab/SlicerOpenAnatomy</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>I’m sure it will need some tweaking, but this works already.</p>

---
