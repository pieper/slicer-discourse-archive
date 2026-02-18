# Rotate model around specific point

**Topic ID**: 16846
**Date**: 2021-03-30
**URL**: https://discourse.slicer.org/t/rotate-model-around-specific-point/16846

---

## Post #1 by @Mik (2021-03-30 11:52 UTC)

<p>What is the easiest way to rotate model around specific point or a new origin?</p>
<p>The model of table top by default rotates around origin (0, 0, 0). I want to simulate the pitch and roll angles of the table top around specific point or ball joint with coordinates (Itx, Ity, Itz). Usually that means that i must translate models into new origin, than rotate models, and translate them back.</p>
<p>Should i use only hierarchy of transforms, or is there another way?</p>
<p>Here is a sketch of the issue, default coordinate system and origin XtYt (black arrows), new system is Xt’Yt’ (red arrows).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d33778fe0cb18095f8a92d2e5cdca54fbb1b8da.png" data-download-href="/uploads/short-url/mqFehYDk07G3wTww0eCy95ktkr8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d33778fe0cb18095f8a92d2e5cdca54fbb1b8da_2_690x420.png" alt="image" data-base62-sha1="mqFehYDk07G3wTww0eCy95ktkr8" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d33778fe0cb18095f8a92d2e5cdca54fbb1b8da_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d33778fe0cb18095f8a92d2e5cdca54fbb1b8da.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d33778fe0cb18095f8a92d2e5cdca54fbb1b8da.png 2x" data-dominant-color="8795B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1000×610 33.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @manjula (2021-03-30 12:20 UTC)

<p>Maybe this is what you looking for ?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_point" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_point</a></p>
<p>And video made by Prof Lasso</p>
<p><a href="https://1drv.ms/v/s!Arm_AFxB9yqHucN9pd6edw1a1cgxbg?e=x5SJOd" class="onebox" target="_blank" rel="noopener nofollow ugc">https://1drv.ms/v/s!Arm_AFxB9yqHucN9pd6edw1a1cgxbg?e=x5SJOd</a></p>

---

## Post #3 by @Mik (2021-03-30 12:35 UTC)

<p>Thank you, that is enough.</p>

---
