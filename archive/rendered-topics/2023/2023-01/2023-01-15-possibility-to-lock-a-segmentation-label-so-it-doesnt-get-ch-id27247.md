# Possibility to lock a segmentation label so it doesn't get changed when modifying others?

**Topic ID**: 27247
**Date**: 2023-01-15
**URL**: https://discourse.slicer.org/t/possibility-to-lock-a-segmentation-label-so-it-doesnt-get-changed-when-modifying-others/27247

---

## Post #1 by @a.mohseni (2023-01-15 10:48 UTC)

<p>So after adding my first label, i wanted to add another one inside of the same CT scan by using the scissor and rectangle tool, but now i’m seeing that it modified the first label as a part of it has been cut out. Is there a way to lock the first label so it isn’t modifiable anymore, but it still can be exported together with the other label(s)? thanks in advance!</p>

---

## Post #2 by @muratmaga (2023-01-15 22:19 UTC)

<p>You can achieve this in couple ways. The simplest is to turn off the visibility of the segment you want NOT changed, and make sure the Modify other Segments field is set to “Visible Segments Only” (or allow overlap).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7beca5971aa70ad64d363411c88d2c03485fdbde.png" data-download-href="/uploads/short-url/hGhK1GKv6p7PE2VYcvApD5qyTjU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7beca5971aa70ad64d363411c88d2c03485fdbde_2_368x375.png" alt="image" data-base62-sha1="hGhK1GKv6p7PE2VYcvApD5qyTjU" width="368" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7beca5971aa70ad64d363411c88d2c03485fdbde_2_368x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7beca5971aa70ad64d363411c88d2c03485fdbde_2_552x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7beca5971aa70ad64d363411c88d2c03485fdbde_2_736x750.png 2x" data-dominant-color="F0F2F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1104×1123 65.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
