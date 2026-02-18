# Slicer VR problems

**Topic ID**: 4661
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/slicer-vr-problems/4661

---

## Post #1 by @M_pavi (2018-11-06 18:51 UTC)

<p>I am new to 3D slicer VR.  I could able to render view but seems I can’t do any customization to change settings. I did change background color but I want to create VR space and fix the object and saved VR scene. Is there any tutorial or guide to follow to learn more on slicer VR</p>

---

## Post #2 by @cpinter (2018-11-06 19:04 UTC)

<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4661">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>but I want to create VR space and fix the object</p>
</blockquote>
</aside>
<p>Can you please elaborate? I’m not sure what creating VR space or fixing object means. Thanks!</p>

---

## Post #3 by @M_pavi (2018-11-06 19:42 UTC)

<p>sure I want to do some customization like fixing the object ( object should be fixed in given position)  in desire position on the VR space.</p>
<p>Also Can we do changes with the controllers ( I am using HTC VIVE) I don’t want to show controllers in  the VR view. Is that possible ?</p>

---

## Post #4 by @cpinter (2018-11-06 19:48 UTC)

<p>I’m sorry I still don’t know what do you mean by “fixing the object”. Do you want to disable it being movable by the controller?</p>
<p>You can do any customization in the C++ code, see</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/tree/master/Rendering/OpenVR">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/vtk/vtk/tree/master/Rendering/OpenVR" target="_blank" rel="noopener">GitLab</a>
  </header>

  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar" width="146" height="146">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/tree/master/Rendering/OpenVR" target="_blank" rel="noopener">Rendering/OpenVR · master · VTK / VTK · GitLab</a></h3>

  <p>Visualization Toolkit</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/SlicerVirtualReality">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/KitwareMedical/SlicerVirtualReality" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/2afd9df8cb63c856ca5133fc5a8e178d30b6f8baf8885014677a5f24bb99d53d/KitwareMedical/SlicerVirtualReality" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/SlicerVirtualReality" target="_blank" rel="noopener">GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables...</a></h3>

  <p>A Slicer extension that enables user to interact with a Slicer scene using virtual reality. - GitHub - KitwareMedical/SlicerVirtualReality: A Slicer extension that enables user to interact with a S...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @M_pavi (2018-11-06 19:51 UTC)

<p>Yeh exactly, want to disable it from being movable by the controller? I want to place the object in the desired location in VR space.</p>

---

## Post #6 by @lassoan (2018-11-07 03:25 UTC)

<p>To prevent an object from being grabbed and moved, set the node’s “Selectable” property to False. You can do it programmatically as shown in <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md">Developer guide</a> or in the GUI as explained in the <a href="https://github.com/KitwareMedical/SlicerVirtualReality/#controllers">User guide</a>.</p>

---
