# How to change display layer of markups?

**Topic ID**: 8960
**Date**: 2019-10-30
**URL**: https://discourse.slicer.org/t/how-to-change-display-layer-of-markups/8960

---

## Post #1 by @jamesobutler (2019-10-30 13:33 UTC)

<p>Is there a way to manage what layer a markup should be displayed relative to other models?</p>
<p>As shown in the image below, the markups are displayed behind the SurfaceCut segment model.  I would like to have the option of showing the fiducial on top of the segment model.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a853a27535d71724bd7946d74923a7211235c812.png" alt="fiducial-glyph-layer" data-base62-sha1="o15oSKXbQdMcGf5CzXA82csq5Bo" width="311" height="191"></p>

---

## Post #2 by @lassoan (2019-10-30 15:40 UTC)

<p>Changing rendering layers is more intrusive, it could break things, but you can get low-level access to VTK mappers and modify coincident topology parameters. There is also a chance that you can change the order by changing in what order you add nodes to the scene.</p>
<p>We plan to add surface area display to closed curve markups and there we will be able to tune the order more easily. Current progress is that markups module can already compute the surface area polygon (even for non-planar curves), but display has not been implemented yet.</p>

---
