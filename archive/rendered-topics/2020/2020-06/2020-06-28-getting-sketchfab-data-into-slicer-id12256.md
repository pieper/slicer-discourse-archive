---
topic_id: 12256
title: "Getting Sketchfab Data Into Slicer"
date: 2020-06-28
url: https://discourse.slicer.org/t/12256
---

# Getting sketchfab data into Slicer

**Topic ID**: 12256
**Date**: 2020-06-28
**URL**: https://discourse.slicer.org/t/getting-sketchfab-data-into-slicer/12256

---

## Post #1 by @muratmaga (2020-06-28 18:17 UTC)

<p>SKetchfab uses a format called .gltf, which Slicer doesn’t seem to recognize. What would it take to support that?</p>

---

## Post #2 by @pieper (2020-06-28 18:42 UTC)

<p>That should become available when we upgrade to the latest VTK.  If it’s really in the critical path we could maybe add the classes directly to slicer (under a mangled name) as a workaround.</p>
<aside class="quote" data-post="1" data-topic="7064">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/transferring-models-using-gltf-2-0/7064">Transferring models using glTF 2.0</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    To follow up on an <a href="http://massmail.spl.harvard.edu/public-archives/slicer-users/2017/011982.html">email</a> from <a class="mention" href="/u/pieper">@pieper</a> from 2017 

Transferring models is still a work in progress, but lately I’m looking at glTF [5] as an interesting option. 

I would like to mention that VTK has an improved support for glTF 2.0. It should be possible to create a Slicer extension leveraging the new <a href="https://vtk.org/doc/nightly/html/classvtkGLTFImporter.html#details">vtkGLTFReader</a>, <a href="https://vtk.org/doc/nightly/html/classvtkGLTFImporter.html#details">vtkGLTFImporter</a> and <a href="https://vtk.org/doc/nightly/html/classvtkGLTFExporter.html#details">vtkGLTFExporter</a> classes. 
You can read more details about the functionality here: 
<a href="https://blog.kitware.com/introducing-gltf-2-0-support-in-vtk-and-paraview" class="onebox" target="_blank" rel="noopener">https://blog.kitware.com/introducing-gltf-2-0-support-in-vtk-and-paraview</a>
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2020-06-28 19:46 UTC)

<p>We have already backported gltf support from latest VTK version in OpenAntomy extension.</p>
<p>I’ve recently added support scripted file reader plugins, so it should be easy to add a script that makes gltf files loadable via “Add data” dialog.</p>

---

## Post #4 by @pieper (2020-06-28 20:22 UTC)

<p>Cool, yes, we should be able to do a <a href="https://github.com/Slicer/Slicer/blob/21fa3d053e3eba4a18c50d7ba59a9495e3f266a9/Base/QTCore/qSlicerScriptedFileReader.h"><code>qSlicerScriptedFileReader</code></a> for that.</p>

---

## Post #5 by @muratmaga (2020-06-29 03:49 UTC)

<p>Sounds great. <a class="mention" href="/u/pieper">@pieper</a> let’s talk about this sometime this week.</p>

---
