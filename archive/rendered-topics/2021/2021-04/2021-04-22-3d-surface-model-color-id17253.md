---
topic_id: 17253
title: "3D Surface Model Color"
date: 2021-04-22
url: https://discourse.slicer.org/t/17253
---

# 3D surface model color

**Topic ID**: 17253
**Date**: 2021-04-22
**URL**: https://discourse.slicer.org/t/3d-surface-model-color/17253

---

## Post #1 by @anromero (2021-04-22 15:52 UTC)

<p>I’ve imported .ply files to do some landmarking for a geometric morphometrics project. Is there a way to set the surface to be the image collected from the surface scanner? This is an option in the old software Landmark Editor and it really helps with visualizing flat sutures.</p>

---

## Post #2 by @muratmaga (2021-04-22 16:00 UTC)

<p>I am not sure what mean by “set the surface to be the image collected from the surface scanner”? Are you talking about color texture? If so, you have to use the TextureModel module from SlicerIGT. If not please provide a more detailed description of what you want to do (or a screenshot)?</p>

---

## Post #3 by @anromero (2021-04-22 16:30 UTC)

<p>Yes, I think that is what I’m referring to. Do I need the models to be in an OBJ format for this module to work?</p>

---

## Post #4 by @muratmaga (2021-04-22 17:03 UTC)

<p>I don’t work with textured scans, but I don’t think you need it to be OBJ as long as you can load the textures separately (in JPG or other formats Slicer can read).<br>
[Edit: Based on this thread, you might need it OBJ after all <a href="https://discourse.slicer.org/t/displaying-textured-3d-models/2521/9" class="inline-onebox">Displaying textured 3D models - #9 by tsehrhardt</a>]<br>
<a class="mention" href="/u/lassoan">@lassoan</a>  is this still the case.</p>

---

## Post #5 by @lassoan (2021-04-22 17:12 UTC)

<p>You can display a full-color mesh in two ways:</p>
<ul>
<li>mesh+texture: the mesh contains texture coordinates for each point and the texture image is stored in a separate file. Slicer can read texture coordinates from meshes stored in VTK, VTP, OBJ, and maybe PLY format. You can load the texture image from any file (JPG, PNG, …) and apply it to the mesh using Texture model module. Texture module can also write the color to point data, so you can save a vertex-colored mesh in a VTK, VTP, or PLY file.</li>
<li>vertex-colored mesh: the mesh contains RGB value for each point. Slicer can read such meshes from VTK, VTP, and PLY files. Colored PLY file reading was just added a few days ago, so you need the very latest Slicer Preview Release.</li>
</ul>

---

## Post #6 by @tsehrhardt (2021-04-23 12:10 UTC)

<p>I visualize per vertex color on PLY in Models by checking “Visible” under Scalars, selecting RGBA under Active Scalar, and Direct color mapping under Scalar Range Mode. The alpha displays properly as well.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> does the addition to the Preview do this automatically now?</p>

---

## Post #7 by @lassoan (2021-04-23 12:24 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="6" data-topic="17253">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>does the addition to the Preview do this automatically now?</p>
</blockquote>
</aside>
<p>Yes, RGB and RGBA arrays are now automatically recognized and shown by default. They are now also saved in PLY format (previously, color was only saved when using VTK or VTP format).</p>

---

## Post #8 by @anromero (2021-04-23 17:37 UTC)

<p>This worked! Thank you!</p>

---
