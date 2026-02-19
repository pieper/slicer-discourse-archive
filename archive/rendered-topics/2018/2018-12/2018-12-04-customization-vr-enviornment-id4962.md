---
topic_id: 4962
title: "Customization Vr Enviornment"
date: 2018-12-04
url: https://discourse.slicer.org/t/4962
---

# Customization VR enviornment

**Topic ID**: 4962
**Date**: 2018-12-04
**URL**: https://discourse.slicer.org/t/customization-vr-enviornment/4962

---

## Post #1 by @M_pavi (2018-12-04 20:10 UTC)

<p>My problem is to customize Virtual reality space. In specifically</p>
<ol>
<li>I did render 3D and 4D data in the same VR environment at the same time.</li>
<li>Where I did change the background color by using python interactor ( the problem is when I c<br>
load the scene want to change background color every time.)</li>
<li>Where I need to customize VR space for an instance to add some sounds, fix the volume in the desired position and some more function etc.</li>
</ol>
<p>Can someone help me how to develop those things ( how to develop the  VR environment (functions )<br>
I went through <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md" rel="nofollow noopener">https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/DeveloperGuide.md</a> but I couldn’t understand that how to develop further.</p>

---

## Post #2 by @lassoan (2018-12-05 06:33 UTC)

<p>If you directly manipulate renderers, render windows, etc. then their state is usually not saved in the scene. Make sure you modify MRML nodes instead. For example, you can change view background as shown in this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_3D_view_background_color" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4962">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>add some sounds</p>
</blockquote>
</aside>
<p>How do you add sounds?</p>
<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4962">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>fix the volume in the desired position</p>
</blockquote>
</aside>
<p>You apply transform to a volume to set its position in the world coordinate system. A transform is automatically created if you grab and move a node using a controller. Transforms are stored in the scene and used when you reload the scene.</p>
<p>Currently we only save magnification component of PhysicalToWorld matrix in the view node (vtkMRMLVirtualRealityViewNode). View position and orientation is set when you activate virtual reality display, based on the view position/orientation in the regular 3D view. View position/orientation in the regular 3D view is saved in the scene. So, if you save the scene then view position/orientation in virtual reality should be saved/restored by scene save/load.</p>
<aside class="quote no-group" data-username="M_pavi" data-post="1" data-topic="4962">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/54ee81/48.png" class="avatar"> M_pavi:</div>
<blockquote>
<p>Can someone help me how to develop those things</p>
</blockquote>
</aside>
<p>For low-level customization, you need to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">build Slicer</a> and then build SlicerVirtualReality extension. However, you should be able to do many things by just Python scripting. Let us know what exactly you would like to do and we can give advice for implementation.</p>

---
