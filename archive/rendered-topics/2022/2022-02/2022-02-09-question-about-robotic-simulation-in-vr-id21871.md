---
topic_id: 21871
title: "Question About Robotic Simulation In Vr"
date: 2022-02-09
url: https://discourse.slicer.org/t/21871
---

# Question about robotic simulation in VR

**Topic ID**: 21871
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/question-about-robotic-simulation-in-vr/21871

---

## Post #1 by @user5 (2022-02-09 15:07 UTC)

<p>I am trying to use a robotic model to do needle insertion. It may include robotic simulation and transform. I would like to show and operate in SlicerVR which use the VR controller to control the robotic simulation and transform.<br>
Is SlicerVR able to perform these tasks?</p>

---

## Post #2 by @pieper (2022-02-09 15:11 UTC)

<p>Yes, that should all be possible.  SlicerVR shows you everything that’s in the 3D views, so you can set up OpenIGTLink, links to ROS, etc.  For sure some amount of customization would be needed to make it more usable, but this should all be doable in python.</p>

---

## Post #3 by @user5 (2022-02-10 14:57 UTC)

<p>If I want to make customization function in Python for SlicerVR, which file I should go to modify?</p>

---

## Post #4 by @pieper (2022-02-10 15:03 UTC)

<p>It depends on what you are trying to accomplish with your customization.  You’ll need to read the code to figure out.</p>

---

## Post #5 by @user5 (2022-02-10 15:47 UTC)

<p>Which folder contain those code?<br>
Also, I would like to ask that does SlicerVR has any tutorial for beginner development?</p>

---

## Post #6 by @pieper (2022-02-10 16:22 UTC)

<p>This material is all very new, so no developer tutorials that I know of.</p>
<p>The VR code is here:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/KitwareMedical/SlicerVirtualReality/tree/master/VirtualReality">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerVirtualReality/tree/master/VirtualReality" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/KitwareMedical/SlicerVirtualReality/tree/master/VirtualReality" target="_blank" rel="noopener">SlicerVirtualReality/VirtualReality at master ·...</a></h3>

  <p><a href="https://github.com/KitwareMedical/SlicerVirtualReality/tree/master/VirtualReality" target="_blank" rel="noopener">master/VirtualReality</a></p>

  <p><span class="label1">A Slicer extension that enables user to interact with a Slicer scene using virtual reality. - SlicerVirtualReality/VirtualReality at master · KitwareMedical/SlicerVirtualReality</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2022-02-10 19:42 UTC)

<p>The great thing about SlicerVirtualReality is that behaviors in the scene can be defined using Python-scripting the same way in virtual reality as you would do it for the regular desktop experience. Typically the user just moves objects around and you add observers to those transforms (or directly to the controllers pose), and then you react to those changes any way you want (update some other transforms, show/hide object, change any other properties of any objects in the scene). You can find lots of code snippets for manipulating objects (that are all usable in virtual reality) in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>.</p>
<p>Very soon (or maybe already) you can display Qt widgets in the immersive view, which will make it trivial to add buttons, sliders, etc. that can be manipulated without peeking out of the headset.</p>
<p>If you have questions about how to implement a particular behavior then let us know and we can give more specific instructions.</p>

---

## Post #9 by @user5 (2022-02-11 18:00 UTC)

<p>I find that the file format in GitHub is .cxx which is different with the file format in 3D Slicer’s extension root folder which is .pyd. Can I directly use .cxx file to replace .pyd file?</p>

---

## Post #10 by @lassoan (2022-02-11 19:19 UTC)

<p>You need to build the source cxx files (implemented in C++) to generate executable, Python-wrapped code.</p>

---

## Post #11 by @user5 (2022-02-16 03:27 UTC)

<p>I am already trying to modify the SlicerVR extension in visual studio 2017. I follow this link to build .pyd file.</p>
<blockquote>
<p><a href="https://www.youtube.com/watch?v=9q-LHP7cMfg&amp;ab_channel=PyCon2014" rel="noopener nofollow ugc">Building a C++ extension for Python 3.5 on Windows - YouTube</a></p>
</blockquote>
<p>Since visual studio 2017 does not have VTK Modules, I have followed this link to import VTK Modules into visual studio 2017.</p>
<blockquote>
<p><a href="https://jacky-ttt.medium.com/day039-how-to-include-and-link-vtk-boost-and-glm-in-visual-studio-2017-on-windows-2c611d63dd09" rel="noopener nofollow ugc">Day039 — How to include and link VTK, Boost and GLM in Visual Studio 2017 on Windows | by Jacky Tsang | Medium</a></p>
</blockquote>
<p>But the build is failed.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abe9424c2a193774574687e8600e3798a2e6ec90.png" data-download-href="/uploads/short-url/owNoXbS8SlN2CMCK3R9Oprayyvm.png?dl=1" title="擷取11" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abe9424c2a193774574687e8600e3798a2e6ec90_2_690x377.png" alt="擷取11" data-base62-sha1="owNoXbS8SlN2CMCK3R9Oprayyvm" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abe9424c2a193774574687e8600e3798a2e6ec90_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abe9424c2a193774574687e8600e3798a2e6ec90_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abe9424c2a193774574687e8600e3798a2e6ec90_2_1380x754.png 2x" data-dominant-color="E5E7EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">擷取11</span><span class="informations">1843×1008 94.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is it has anything that I am missing to add?</p>

---
