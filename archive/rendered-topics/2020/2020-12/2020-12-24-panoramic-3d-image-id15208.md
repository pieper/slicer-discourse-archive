---
topic_id: 15208
title: "Panoramic 3D Image"
date: 2020-12-24
url: https://discourse.slicer.org/t/15208
---

# Panoramic 3D image

**Topic ID**: 15208
**Date**: 2020-12-24
**URL**: https://discourse.slicer.org/t/panoramic-3d-image/15208

---

## Post #1 by @aldoSanchez (2020-12-24 03:55 UTC)

<p>Hi today Im working with the images creater like<br>
cap = ScreenCapture.ScreenCaptureLogic().capture3dViewRotation(getNode(‘vtkMRMLViewNode1’),-180,180,15,0,“C:/Users/aldot/Desktop/python”,‘image_%05d.png’)</p>
<p>and I want to do a panoramic image merge all of them in one I just want to know if is possible with a slicer or I need another program like PhotoShop</p>

---

## Post #2 by @lassoan (2020-12-24 05:36 UTC)

<p>360 degree photos make sense only for rendering scenes where you are in the middle and you <em>look around</em>, while in medical imaging you are usually outside the volume of interest and <em>look at</em> a 3D object. That’s why we have the rotating video export option and have not added the 360 panorama option.</p>
<p>Anyway, we’ll soon update VTK in Slicer to VTK9, which has a <a href="https://github.com/Kitware/VTK/blob/master/Rendering/OpenGL2/vtkPanoramicProjectionPass.h">vtkPanoramicProjectionPass class</a> that should make it very simple to create panoramic renderings.</p>
<p>Instead of a panoramic image, it would be generally more relevant to create VR180 video or side-by-side stereo video (viewable on a VR headset). Both should be quite straightforward to implement.</p>

---

## Post #3 by @aldoSanchez (2020-12-24 06:13 UTC)

<p>The main idea is to use this panoramic picture to make <strong>Augmented reality</strong><br>
so the 3D object could be used or panoramic for inside staff</p>

---

## Post #4 by @lassoan (2020-12-24 06:29 UTC)

<p>Panoramic image is useful if you are inside the patient and want to render the surroundings, which only happens in endoscopic AR, but even then, typically you want to overlay tumors or trajectories and not an entire 360 box.</p>
<p>What would you like to display over the patient? Burr hole position, drill/needle insertion trajectory, vertebral models, …? They are all just take up a very small part of the field of view, so panoramic 360 view is not relevant. Normally you add a tracking reference on the patient and display a 3D model anchored relative to that reference marker (but if you don’t need robust registration then markerless tracking works, too).</p>
<p>You can try the open-source surgical AR system developed by Etienne Leger (it integrates with Slicer, I think Slicer or maybe Ibis renders the overlay and it is sent to the AR tablet using OpenIGTLink): <a href="https://link.springer.com/article/10.1007/s11548-020-02155-6">https://link.springer.com/article/10.1007/s11548-020-02155-6</a></p>
<p>There are some other earlier efforts related to this - some of the links may still be useful: <a href="https://www.slicer.org/wiki/Documentation/Labs/Augmented_Reality_and_Virtual_Reality_support">https://www.slicer.org/wiki/Documentation/Labs/Augmented_Reality_and_Virtual_Reality_support</a></p>

---

## Post #5 by @aldoSanchez (2020-12-24 06:55 UTC)

<p>Wow thanks for the information, I will give it a look and hopefully it will work I want to show the outside of the brain like 3D models and inside like panoramic 360 view in AR.</p>

---
