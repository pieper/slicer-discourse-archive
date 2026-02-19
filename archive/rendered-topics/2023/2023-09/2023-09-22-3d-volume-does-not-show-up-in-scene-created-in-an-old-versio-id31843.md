---
topic_id: 31843
title: "3D Volume Does Not Show Up In Scene Created In An Old Versio"
date: 2023-09-22
url: https://discourse.slicer.org/t/31843
---

# 3D volume does not show up in scene created in an old version of Slicer

**Topic ID**: 31843
**Date**: 2023-09-22
**URL**: https://discourse.slicer.org/t/3d-volume-does-not-show-up-in-scene-created-in-an-old-version-of-slicer/31843

---

## Post #1 by @thkarag (2023-09-22 10:57 UTC)

<p>Some years ago, I have created a 3D mesh from an .nrrd file, using Volume Rendering using Slicer version 4.11 and saved it into a .mrml file. When I open this .mrml file in Slicer 5.2 the 3D volume does not show up and i get the following error in the Python console:</p>
<p>[Qt] class QList __cdecl qSlicerCoreIOManagerPrivate::writers(const class QString &amp;,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLScene ) const warning: Unable to find node with ID “” in the given scene.</p>
<p>Slicer version: 5.2.2</p>

---

## Post #2 by @muratmaga (2023-09-22 11:00 UTC)

<aside class="quote no-group" data-username="thkarag" data-post="1" data-topic="31843">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thkarag/48/66477_2.png" class="avatar"> thkarag:</div>
<blockquote>
<p>file. When I open this .mrml file in Slicer 5.2 the 3D volume does not show up and i get the following error in the Python console:</p>
</blockquote>
</aside>
<p>Can you still open this MRML file in 4.11 correctly? I.e., is the NRRD file still in the right place, or maybe it has been renamed?</p>
<p>You can still open the NRRD directly by  dragging and dropping it into the Slicer window (5.2.2)</p>

---

## Post #3 by @thkarag (2023-09-22 11:01 UTC)

<p>The mrml file opens correctly in Slicer 4.11 and the 3D volume is viewed properly.</p>

---

## Post #4 by @lassoan (2023-09-22 18:28 UTC)

<p>Please use the latest Slicer Stable Release (currently Slicer-5.4.0) and let us know if you still see any errors. If you do then we would need a scene that reproduces the issue, so you can either share your scene (upload somewhere and post the link here or in a private message) or try to recreate a problematic scene with some sample data set and share that.</p>
<p>If the volume loads correctly just volume rendering does not appear then you can load just the NRRD file and set up volume rendering for this volume.</p>

---
