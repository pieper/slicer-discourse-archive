# Segment comparison - DICE coefficient is wrong!

**Topic ID**: 30000
**Date**: 2023-06-13
**URL**: https://discourse.slicer.org/t/segment-comparison-dice-coefficient-is-wrong/30000

---

## Post #1 by @Teddy (2023-06-13 02:54 UTC)

<p>I used two same segments for comparison and calculate DICE using RTslicer module, but get the wrong result.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b70309ff501465b3286cfe0bb2ebe60f7294181.jpeg" data-download-href="/uploads/short-url/aLmaV15jSkgM9uElFLUT83UxbYR.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b70309ff501465b3286cfe0bb2ebe60f7294181_2_690x281.jpeg" alt="image" data-base62-sha1="aLmaV15jSkgM9uElFLUT83UxbYR" width="690" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b70309ff501465b3286cfe0bb2ebe60f7294181_2_690x281.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b70309ff501465b3286cfe0bb2ebe60f7294181_2_1035x421.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b70309ff501465b3286cfe0bb2ebe60f7294181_2_1380x562.jpeg 2x" data-dominant-color="6D6D74"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1937×790 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2023-06-13 04:09 UTC)

<p>Can’t reproduce. I am getting the expected 1.0. Make sure both segments have the same information. The simplest would be copying the contents of one segment to the other via the logical operators.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9902d973ac878591d9df649d6d053227c033367.jpeg" data-download-href="/uploads/short-url/sL6S2MmkxO2NyVvVe7PCDVFjPFl.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9902d973ac878591d9df649d6d053227c033367_2_690x448.jpeg" alt="image" data-base62-sha1="sL6S2MmkxO2NyVvVe7PCDVFjPFl" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9902d973ac878591d9df649d6d053227c033367_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c9902d973ac878591d9df649d6d053227c033367_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c9902d973ac878591d9df649d6d053227c033367.jpeg 2x" data-dominant-color="828288"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1312×852 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @muratmaga (2023-06-13 04:14 UTC)

<aside class="quote no-group" data-username="Teddy" data-post="1" data-topic="30000">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/da6949/48.png" class="avatar"> Teddy:</div>
<blockquote>
<p>but get the wrong result.</p>
</blockquote>
</aside>
<p>Most likely during your segmentation you didn’t allow overlap between segments (by default changes modify all segments), hence there is no overlap between two segmentation and the reported value of 0.</p>

---
