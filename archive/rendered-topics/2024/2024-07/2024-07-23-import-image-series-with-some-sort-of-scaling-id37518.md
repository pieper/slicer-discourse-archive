# Import image series with some sort of scaling?

**Topic ID**: 37518
**Date**: 2024-07-23
**URL**: https://discourse.slicer.org/t/import-image-series-with-some-sort-of-scaling/37518

---

## Post #1 by @boiler (2024-07-23 12:54 UTC)

<p>Hi all,<br>
I’ve an PNG image series, every slice has some distance. During import, the slice are “as minimal as” possible arranged, so my top view is very narrow. Can I somehome scale the 2D view or give somehow a distance to the slices? Alternatively it’s possible to duplicate the images, but that somehow only an improvised solution…<br>
Thanks a lot.<br>
M.</p>

---

## Post #2 by @muratmaga (2024-07-23 16:48 UTC)

<p>If you know the real spacing value of the slices, you can modify the image spacing setting through the <code>Volumes</code> module after you import them.</p>
<p>or better yet, use the <code>ImageStacks</code> module from SlicerMorph extension and set the correct image spacing (x, y, and z) at the time of import and don’t need to mess with it later.</p>

---
