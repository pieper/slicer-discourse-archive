# Visualization annoyance in several parts

**Topic ID**: 8654
**Date**: 2019-10-03
**URL**: https://discourse.slicer.org/t/visualization-annoyance-in-several-parts/8654

---

## Post #1 by @Alex_Vergara (2019-10-03 08:05 UTC)

<p>I know this is no bug, properly said, but is annoying enough to be considered as is.</p>
<p>The following elements does not allow scrolling: <code>Subject hierarchy item information</code>, <code>Node information</code>, <code>All nodes</code> . This makes almost impossible to read the sections, the solution is simple: add a scroll bar. See:</p>
<p><code>Subject hierarchy item information</code><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43718a2f5873d15ad9c80494b8c1f4abc9ec9cc0.png" data-download-href="/uploads/short-url/9CDfoNFVQZTe1LEY1xt7nr1Q15S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43718a2f5873d15ad9c80494b8c1f4abc9ec9cc0_2_225x500.png" alt="image" data-base62-sha1="9CDfoNFVQZTe1LEY1xt7nr1Q15S" width="225" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43718a2f5873d15ad9c80494b8c1f4abc9ec9cc0_2_225x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43718a2f5873d15ad9c80494b8c1f4abc9ec9cc0_2_337x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43718a2f5873d15ad9c80494b8c1f4abc9ec9cc0_2_450x1000.png 2x" data-dominant-color="E0E1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">538×1195 65.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><code>Node information</code><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64d96025ab8bc1151bfeb8097f0717c819a42cf6.png" data-download-href="/uploads/short-url/eo9tgCy27TrLhSrfo3ekDng1ovY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64d96025ab8bc1151bfeb8097f0717c819a42cf6_2_228x500.png" alt="image" data-base62-sha1="eo9tgCy27TrLhSrfo3ekDng1ovY" width="228" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64d96025ab8bc1151bfeb8097f0717c819a42cf6_2_228x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64d96025ab8bc1151bfeb8097f0717c819a42cf6_2_342x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64d96025ab8bc1151bfeb8097f0717c819a42cf6_2_456x1000.png 2x" data-dominant-color="DEDFE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">543×1188 66.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><code>All nodes</code><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c034b4ae9f53e0d359f234f96b64b78b225b8886.png" data-download-href="/uploads/short-url/rqkAWRPDZSFeZ0IQkDmXDUIiWOi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c034b4ae9f53e0d359f234f96b64b78b225b8886_2_222x500.png" alt="image" data-base62-sha1="rqkAWRPDZSFeZ0IQkDmXDUIiWOi" width="222" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c034b4ae9f53e0d359f234f96b64b78b225b8886_2_222x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c034b4ae9f53e0d359f234f96b64b78b225b8886_2_333x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c034b4ae9f53e0d359f234f96b64b78b225b8886_2_444x1000.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">535×1200 77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-10-03 15:05 UTC)

<p>Scrollable area within scrollable area is usually quite hard to navigate, if you can send a pull request with a suggestion of what should be changed then we can have a look.</p>
<p>However, I would recommend to use “Node info” module in “Debugging tools” extension for inspecting node properties. It allows browsing the MRML tree by node references, creating variables on the Python console and dockable “Node information” widgets:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0881487becb96fdcaa21917cb6c6cd1cbd69d445.png" data-download-href="/uploads/short-url/1deO4tpwxOlZN3RKmLabUgHIhSt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0881487becb96fdcaa21917cb6c6cd1cbd69d445_2_690x438.png" alt="image" data-base62-sha1="1deO4tpwxOlZN3RKmLabUgHIhSt" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0881487becb96fdcaa21917cb6c6cd1cbd69d445_2_690x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0881487becb96fdcaa21917cb6c6cd1cbd69d445_2_1035x657.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0881487becb96fdcaa21917cb6c6cd1cbd69d445_2_1380x876.png 2x" data-dominant-color="DCDBDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1434 558 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The module could be extended to also show associated subject hierarchy item information.</p>

---

## Post #3 by @Alex_Vergara (2019-10-03 15:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The module could be extended to also show associated subject hierarchy item information.</p>
</blockquote>
</aside>
<p>Yes please!!<br>
And also have a look at <code>All nodes</code>, It is very unreadable</p>

---

## Post #4 by @lassoan (2019-10-03 18:41 UTC)

<aside class="quote no-group quote-modified" data-username="Alex_Vergara" data-post="3" data-topic="8654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<blockquote>
<p>The module could be extended to also show associated subject hierarchy item information.</p>
</blockquote>
<p>Yes please!!</p>
</blockquote>
</aside>
<p>I meant that <em>you</em> can easily extend it. It is a tiny Python scripted module that you can customize it to do what you need. If you think your changes could be useful for others, too, then please send a pull request.</p>

---

## Post #5 by @Alex_Vergara (2019-10-23 08:31 UTC)

<p>I can’t see where this script is located, may you enlighten me please?</p>

---

## Post #6 by @lassoan (2019-10-23 13:29 UTC)

<p>The module is available here: <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/NodeInfo/NodeInfo.py" rel="nofollow noopener">https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/NodeInfo/NodeInfo.py</a></p>

---
