# Getting linear distances between fiducial landmarks

**Topic ID**: 33065
**Date**: 2023-11-27
**URL**: https://discourse.slicer.org/t/getting-linear-distances-between-fiducial-landmarks/33065

---

## Post #1 by @paleomariomm (2023-11-27 15:46 UTC)

<p>I have created 5 fiducial markups in Slicer.</p>
<p>I would like to obtain the linear measurements between all of them (two by two).</p>
<p>I know that by selecting two points and right clicking we can obtain the linear measurement between those two landmarks. However, I was unable to find a way to get all linear distances.</p>
<p>Is there a way? maybe a quick Python script?</p>
<p>This is the example<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7226a83079ade1d7930696804dfcf6e0ba168c6c.jpeg" data-download-href="/uploads/short-url/ghPfJNsWRgtBgW1fi5oPRTzHKB6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7226a83079ade1d7930696804dfcf6e0ba168c6c_2_656x500.jpeg" alt="image" data-base62-sha1="ghPfJNsWRgtBgW1fi5oPRTzHKB6" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7226a83079ade1d7930696804dfcf6e0ba168c6c_2_656x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7226a83079ade1d7930696804dfcf6e0ba168c6c_2_984x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7226a83079ade1d7930696804dfcf6e0ba168c6c_2_1312x1000.jpeg 2x" data-dominant-color="9C9DAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1389×1058 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2023-11-27 16:00 UTC)

<aside class="quote no-group" data-username="paleomariomm" data-post="1" data-topic="33065">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paleomariomm/48/68475_2.png" class="avatar"> paleomariomm:</div>
<blockquote>
<p>I would like to obtain the linear measurements between all of them (two by two).</p>
</blockquote>
</aside>
<p>If you mean all pairwaise distance, no there is no GUI way of doing it. You need to write a short python script.</p>

---

## Post #3 by @paleomariomm (2024-01-16 16:22 UTC)

<p>Finally we solved this by exporting landmarks in JSON files and importing in R. Thanks</p>

---

## Post #4 by @jumbojing (2024-01-16 16:33 UTC)

<p>psDst = lambda pN: np.linalg.norm(ndA(pN), axis=-1, keepdims=True)  # return (n, 1)</p>
<h1><a name="p-105556-psdstps-p-1" class="anchor" href="#p-105556-psdstps-p-1" aria-label="Heading link"></a>psDst(ps-p)</h1>

---
