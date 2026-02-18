# 3D model on cellphone 

**Topic ID**: 36642
**Date**: 2024-06-07
**URL**: https://discourse.slicer.org/t/3d-model-on-cellphone/36642

---

## Post #1 by @BaptisteSVD (2024-06-07 14:20 UTC)

<p>Hi,</p>
<p>Is there a way to visualize the 3D reconstruction from 3D slicer on a cellphone ?<br>
Thank you!</p>

---

## Post #2 by @JASON (2024-09-30 23:02 UTC)

<p><a class="mention" href="/u/baptistesvd">@BaptisteSVD</a>  The easiest is to export is OBJ and upload to a service like <a href="https://sketchfab.com/" rel="noopener nofollow ugc">sketchFab</a>.  <a href="https://skfb.ly/6YJCV" rel="noopener nofollow ugc">EXAMPLE</a>.</p>
<p>If you want to host it yourself and have more control, consider using the<br>
<a href="https://github.com/PerkLab/SlicerOpenAnatomy" rel="noopener nofollow ugc">OpenAnatomy module</a>, which can export mesh as GLTF.</p>
<p>You can make your own WebGL viewer to display the GLTF on a webpage. Consider using Three.js.  Here’s an <a href="https://threejs.org/examples/?q=gltf#webgl_loader_gltf" rel="noopener nofollow ugc">example GLTF loader</a>.</p>

---

## Post #3 by @BaptisteSVD (2024-10-02 13:58 UTC)

<p>Thank you very much for your answer, I think it will help me a lot !</p>

---

## Post #4 by @lassoan (2024-10-02 18:32 UTC)

<p>Yes, sure there are many possible approaches. The simplest is probably to export model using SlicerOpenAnatomy extension, upload to dropbox, and send a <a href="http://3dviewer.net">3dviewer.net</a> link to recipients as described <a href="https://github.com/PerkLab/SlicerOpenAnatomy/tree/master/OpenAnatomyExport#quick-start">here</a>.</p>

---

## Post #5 by @BaptisteSVD (2024-10-17 07:53 UTC)

<p>Thanks a lot for your help!</p>

---
