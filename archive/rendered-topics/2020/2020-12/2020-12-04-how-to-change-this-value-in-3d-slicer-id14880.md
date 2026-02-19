---
topic_id: 14880
title: "How To Change This Value In 3D Slicer"
date: 2020-12-04
url: https://discourse.slicer.org/t/14880
---

# How to change this value in 3D slicer?

**Topic ID**: 14880
**Date**: 2020-12-04
**URL**: https://discourse.slicer.org/t/how-to-change-this-value-in-3d-slicer/14880

---

## Post #1 by @NoobForSlicer (2020-12-04 08:09 UTC)

<p>1.What is this? why this can not be changed, when click on it can not change it.</p>
<ol start="2">
<li>what exact command controls this parameters because my script adds here -1 and -1 there.</li>
</ol>
<p>if i would know which command controls this, I could look it up in the script and modify it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a472e80d87e916f7fdfd1ea59c73a257c1cbca4.png" data-download-href="/uploads/short-url/m0O2g4jn8aZnqv9sXOe8QSAqoiU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a472e80d87e916f7fdfd1ea59c73a257c1cbca4.png" alt="image" data-base62-sha1="m0O2g4jn8aZnqv9sXOe8QSAqoiU" width="690" height="219" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×343 9.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2020-12-04 11:08 UTC)

<p>These values are the elements of the direction matrix of the volume based on which it is placed in the RAS coordinate systems (from IJK which is the voxel space of the volume). You cannot change it manually because:</p>
<ol>
<li>This matrix is a component of the whole IJK2RAS matrix, which also contains origin and scaling</li>
<li>Editing manually a direction matrix is not a good idea because that way you couldn’t guarantee a valid matrix (orthogonal axes, etc)</li>
</ol>
<p>The easiest way to modify the volume directions is applying a transformation on top of it, for which see the Transforms module.</p>

---
