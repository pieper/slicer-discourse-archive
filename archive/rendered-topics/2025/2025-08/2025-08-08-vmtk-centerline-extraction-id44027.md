# VMTK, Centerline Extraction

**Topic ID**: 44027
**Date**: 2025-08-08
**URL**: https://discourse.slicer.org/t/vmtk-centerline-extraction/44027

---

## Post #1 by @Paria.M (2025-08-08 15:11 UTC)

<p>Hi everyone,</p>
<p>I want to extract the centerline using VMTK. When I select the Endpoints, the extracted centerline does not cross the points properly, and its far from the Endpoints! Can anyone help me to see what is the problem.</p>
<p>Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f2c9820dacfbf0397de86622c29c1997d07bb78.png" data-download-href="/uploads/short-url/2aeHHft4V7gQIAuP0k8o6Mp9HFm.png?dl=1" title="Screenshot (232)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f2c9820dacfbf0397de86622c29c1997d07bb78_2_427x500.png" alt="Screenshot (232)" data-base62-sha1="2aeHHft4V7gQIAuP0k8o6Mp9HFm" width="427" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f2c9820dacfbf0397de86622c29c1997d07bb78_2_427x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f2c9820dacfbf0397de86622c29c1997d07bb78_2_640x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f2c9820dacfbf0397de86622c29c1997d07bb78_2_854x1000.png 2x" data-dominant-color="9D9BAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (232)</span><span class="informations">864×1011 213 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2025-08-08 15:51 UTC)

<p>Near the end of the surface, the first/last computed centerline point will be away from the end of the  surface by the maximum inscribed sphere’s radius at that point.</p>
<p>Either your get your end points further from the ends of the input surface or you extend the surface.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a1d76e6de64eb45a3254c57f67780b9724d77b1.png" data-download-href="/uploads/short-url/azEswJrnTXHyhkGZHzppMd5j6gx.png?dl=1" title="last_centerline_point" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a1d76e6de64eb45a3254c57f67780b9724d77b1_2_481x500.png" alt="last_centerline_point" data-base62-sha1="azEswJrnTXHyhkGZHzppMd5j6gx" width="481" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a1d76e6de64eb45a3254c57f67780b9724d77b1_2_481x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a1d76e6de64eb45a3254c57f67780b9724d77b1_2_721x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a1d76e6de64eb45a3254c57f67780b9724d77b1.png 2x" data-dominant-color="7D857D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">last_centerline_point</span><span class="informations">914×950 51.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Paria.M (2025-08-08 16:17 UTC)

<p>Thanks for your reply. You mean that I should consider the endpoints a little bit far from the desired endpoints?</p>

---

## Post #4 by @chir.set (2025-08-08 17:05 UTC)

<aside class="quote no-group" data-username="Paria.M" data-post="3" data-topic="44027">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/paria.m/48/80791_2.png" class="avatar"> Paria.M:</div>
<blockquote>
<p>a little bit far from the desired endpoints</p>
</blockquote>
</aside>
<p>Place the endpoints a little bit far from the ends of the tubular surface, at least by the maximum inscribed sphere’s radius.</p>

---
