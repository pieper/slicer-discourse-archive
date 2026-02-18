# Radiomic features

**Topic ID**: 41875
**Date**: 2025-02-25
**URL**: https://discourse.slicer.org/t/radiomic-features/41875

---

## Post #1 by @Aya_Gamal (2025-02-25 22:53 UTC)

<p>When I extract features from quantitative indices or quantitative reporting, the values of min, max, mean, and TLG are extremely high. Is this normal, or is there a problem<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb40d0b3342b317e35a4f3e240f2e991d349c17d.png" data-download-href="/uploads/short-url/t03N8n3tit9j0NqNEsfOAYBciUR.png?dl=1" title="Screenshot 2025-02-26 003922" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb40d0b3342b317e35a4f3e240f2e991d349c17d_2_454x500.png" alt="Screenshot 2025-02-26 003922" data-base62-sha1="t03N8n3tit9j0NqNEsfOAYBciUR" width="454" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb40d0b3342b317e35a4f3e240f2e991d349c17d_2_454x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb40d0b3342b317e35a4f3e240f2e991d349c17d_2_681x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb40d0b3342b317e35a4f3e240f2e991d349c17d.png 2x" data-dominant-color="F0F2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-26 003922</span><span class="informations">726×798 30.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
?</p>

---

## Post #2 by @pieper (2025-02-26 00:10 UTC)

<p>It depends on your data.  If you mouse over in slicer and look at the data probe you can see if the numbers make sense.</p>

---

## Post #3 by @Aya_Gamal (2025-02-26 00:17 UTC)

<p><a class="mention" href="/u/steve">@steve</a><br>
Yes when I put mouse over in slicer ,it appears in data probe large numbers also, but when extract TLG using the same volume with another software,it gives small number ,I don’t understand that difference</p>

---

## Post #4 by @pieper (2025-02-26 00:24 UTC)

<p>You can also try segment statistics.  Perhaps the other software reads the data differently.</p>

---
