# Scalar Color Mapping widget is missing in Volume Rendering

**Topic ID**: 19715
**Date**: 2021-09-17
**URL**: https://discourse.slicer.org/t/scalar-color-mapping-widget-is-missing-in-volume-rendering/19715

---

## Post #1 by @muratmaga (2021-09-17 02:00 UTC)

<p>This is with 9-15 Preview on windows:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c368383dd1bf48576d2bc7fa6d2b8b52f7961d11.png" alt="image" data-base62-sha1="rSEozLmXucbbN8gO6RjbFo6ov4Z" width="625" height="436"></p>

---

## Post #2 by @muratmaga (2021-09-17 03:49 UTC)

<p>OK. I have no idea what happened. Restarted the application it is there now!</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22c6b609c309f5e55f51c07f913f7bb71e28813e.png" alt="image" data-base62-sha1="4XDYaJyaFWWDOTy4BIHzS4PoUea" width="608" height="469"></p>

---

## Post #3 by @lassoan (2021-09-18 00:06 UTC)

<p>This is a feature that probably has not been announced properly <a href="https://discourse.slicer.org/t/color-rgb-volume-rendering/19732">until now</a>. When you load a color (RGB or RGBA) volume then it is rendered using the color stored in each voxel. Since no scalar-&gt;color mapping is performed, the “Scalar Color Mapping” section is not displayed.</p>

---
