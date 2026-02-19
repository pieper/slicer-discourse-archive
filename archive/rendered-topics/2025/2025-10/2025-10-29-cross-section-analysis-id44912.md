---
topic_id: 44912
title: "Cross Section Analysis"
date: 2025-10-29
url: https://discourse.slicer.org/t/44912
---

# Cross-section analysis

**Topic ID**: 44912
**Date**: 2025-10-29
**URL**: https://discourse.slicer.org/t/cross-section-analysis/44912

---

## Post #1 by @bserrano (2025-10-29 10:14 UTC)

<p>Hi all,</p>
<p>We are using cross-section analysis to extract vessel radius. For some centerline nodes, the module prints the message <em>“Consider improving the input surface”</em> and then gives an error when attempting to extract the radius at those points (see video below).</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12c69ee72511acc7c5eb1722ff92a7d20cbe9665.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad1074f224469a956173477249c641d3073ee38f.jpeg" data-video-base62-sha1="2G68w702XaVYrBrnlP37mjwncu9.mp4">
  </div><p></p>
<p>After smoothing the geometry, the issue disappears (see video below).</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be3ec9ee40ce95ca902caaa51ce7065732a4bab6.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7f394f5ebc9842b9cb1ecb64225f96c4e29717b.jpeg" data-video-base62-sha1="r8Zf6YIyFd725yYcQYVIUAMz8d8.mp4">
  </div><p></p>
<p>How can we proactively detect and address these kinds of issues? The geometry appeared correct from the start, so it’s unclear why the errors occur.</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @chir.set (2025-10-29 13:03 UTC)

<aside class="quote no-group" data-username="bserrano" data-post="1" data-topic="44912">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/bserrano/48/17034_2.png" class="avatar"> bserrano:</div>
<blockquote>
<p>proactively detect and address</p>
</blockquote>
</aside>
<p>It has not been possible to identify segments that would generate empty cross-sections. If observed, it should be addressed by any means as you did. For people who do not use the python console, such situations become apparent in the plot chart.</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2025-11-10 07:49 UTC)

<p>Hi to everyone!</p>
<p>Today I am facing the same issue:</p>
<p>The first image crashes the CSA module in the red point</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26f0eb6c74ee095302b29aa14050175a59ffa55d.jpeg" data-download-href="/uploads/short-url/5yujkwlfBExx8kfRJBycaShrvAN.jpeg?dl=1" title="Captura de pantalla 2025-11-10 084250" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26f0eb6c74ee095302b29aa14050175a59ffa55d_2_690x487.jpeg" alt="Captura de pantalla 2025-11-10 084250" data-base62-sha1="5yujkwlfBExx8kfRJBycaShrvAN" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26f0eb6c74ee095302b29aa14050175a59ffa55d_2_690x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26f0eb6c74ee095302b29aa14050175a59ffa55d_2_1035x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26f0eb6c74ee095302b29aa14050175a59ffa55d_2_1380x974.jpeg 2x" data-dominant-color="C8BDB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2025-11-10 084250</span><span class="informations">2196×1550 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But, this image with the ‘spiked voxel’ cleaned do not breaks the execution in the red point.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74b9404cb88a14fb0717b3570f9dcfb440cb2e49.jpeg" data-download-href="/uploads/short-url/gEAhGYNrMVdDXHJHeskWfzcSqPn.jpeg?dl=1" title="Captura de pantalla 2025-11-10 084319" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74b9404cb88a14fb0717b3570f9dcfb440cb2e49_2_673x500.jpeg" alt="Captura de pantalla 2025-11-10 084319" data-base62-sha1="gEAhGYNrMVdDXHJHeskWfzcSqPn" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74b9404cb88a14fb0717b3570f9dcfb440cb2e49_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74b9404cb88a14fb0717b3570f9dcfb440cb2e49_2_1009x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74b9404cb88a14fb0717b3570f9dcfb440cb2e49_2_1346x1000.jpeg 2x" data-dominant-color="C9BFBC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2025-11-10 084319</span><span class="informations">2224×1650 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any idea of how to automatically repair it? Or what is exactly crashing inside the CSA module?</p>

---
