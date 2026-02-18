# 2020.09.21 Hangout w/ Project Week Discussion

**Topic ID**: 13594
**Date**: 2020-09-21
**URL**: https://discourse.slicer.org/t/2020-09-21-hangout-w-project-week-discussion/13594

---

## Post #1 by @jcfr (2020-09-21 18:34 UTC)

<p>Tomorrow, we will be having our next weekly hangout at 10:00 AM ET until 11 AM ET.</p>
<p>Anyone is welcome to join to ask questions at <a href="https://bit.ly/slicer-googlemeet-hosted-by-kitware">https://bit.ly/slicer-googlemeet-hosted-by-kitware </a></p>
<p>Agenda (10:00 - 10:30):</p>
<ul>
<li>Slicer 5 + VTK 9 checkin</li>
<li>Discuss the creation of a standalone project to maintain Slicer Volume Rendering presets. More details below. (cc: <a class="mention" href="/u/forrest.li">@forrest.li</a> <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a>)</li>
</ul>
<p>Agenda (10:30 - 11:00):</p>
<ul>
<li>We will be brainstorming ideas for what a fully virtual January project week could look like.</li>
</ul>
<p>Feel free to post to this thread to request/suggest a topic!</p>
<p>Thanks<br>
Sam and J-Christophe</p>
<h2>Standalone project for organizing volume rendering presets</h2>
<p><strong>Goal</strong>: Streamline maintenance and distribution of the presets to facilitate (1) re-use and (2) integration of improvements.</p>
<p><strong>Proposed approach</strong></p>
<p>Create a repository called <code>Slicer/SlicerVTKVolumeRenderingTransferFunctions</code> distributed (for example) as:</p>
<ul>
<li>git submodule, cmake external project  (e.g faciliate integraiton in any project)</li>
<li>python package (e.g support re-use in Jupyter env.)</li>
<li>npm package  (e.g to streamline integration in <a href="https://kitware.github.io/vtk-js/index.html">vtk.js</a>)</li>
<li>VTK remote module (e.g to streamline interation in VTK or paraview based applications)</li>
</ul>
<p><strong>Open questions</strong></p>
<ul>
<li>Which distribution mechanism should we implement first ?</li>
</ul>
<p><strong>Requirements</strong></p>
<ul>
<li>Add versioning, changelog, contributing, license and documentation</li>
<li>Add thumbnail for each preset</li>
<li>Distribute as both XML and json files</li>
</ul>

---

## Post #2 by @lassoan (2020-09-21 19:53 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="13594">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Slicer/SlicerVTKVolumeRenderingTransferFunctions</p>
</blockquote>
</aside>
<p>Sounds good. Volume rendering presets are not just about transfer functions but also shading, material properties, mode (composite, minimum intensity projection, maximum intensity projection), jittering, shader properties, etc. So, the name should be more general, something like <code>SlicerVTKVolumeRenderingPresets</code>.</p>
<p>Instead of reinventing yet another custom file format, it would be nicer if we could build on an existing one. For example, we could define custom glTF extension for storing volume rendering presets.</p>
<aside class="quote no-group" data-username="jcfr" data-post="1" data-topic="13594">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Distribute as both XML and json files</p>
</blockquote>
</aside>
<p>Minor detail, but probably it will be better to focus on a single format and do it well.</p>

---

## Post #3 by @pieper (2020-09-21 20:05 UTC)

<p>We could be inspired by the material property definitions and extensions in glTF:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/KhronosGroup/glTF/tree/main/extensions">
  <header class="source">

      <a href="https://github.com/KhronosGroup/glTF/tree/main/extensions" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/KhronosGroup/glTF/tree/main/extensions" target="_blank" rel="noopener"></a></h3>

  <p><a href="https://github.com/KhronosGroup/glTF/tree/main/extensions" target="_blank" rel="noopener">//github.com/KhronosGroup/glTF/tree/main/extensions</a></p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>On a related topic, we should look at how to standardize encoding of metatdata in glTF.</p>
<p>It would also be great to investigate volumes in glTF, but the standard states:</p>
<blockquote>
<p><strong>Implementation Note</strong>  glTF 2.0 supports only 2D textures.</p>
</blockquote>

---

## Post #4 by @lassoan (2020-09-21 20:33 UTC)

<p>It would be nice if 3D volumes were standard glTF but it is not a big issue if we need to define custom extensions for volume storage.</p>

---

## Post #5 by @pieper (2020-09-21 20:35 UTC)

<p>Yes, we’ll need custom extensions for our metadata anyway.</p>

---

## Post #6 by @Sam_Horvath (2020-09-22 13:40 UTC)

<p>I’d like to also look at the launchProcess crash: <a href="https://github.com/Slicer/Slicer/issues/5078" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/5078</a></p>

---

## Post #7 by @jcfr (2020-09-28 18:24 UTC)

<blockquote>
<p>Standalone project for organizing volume rendering presets</p>
</blockquote>
<p>This is now tracked in <a href="https://github.com/Slicer/Slicer/issues/5206" class="inline-onebox">Create SlicerVTKVolumeRenderingPresets repository · Issue #5206 · Slicer/Slicer · GitHub</a></p>

---
