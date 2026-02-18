# Volume NRRD - Number of bits per pixel

**Topic ID**: 26112
**Date**: 2022-11-07
**URL**: https://discourse.slicer.org/t/volume-nrrd-number-of-bits-per-pixel/26112

---

## Post #1 by @lucas_sd (2022-11-07 13:44 UTC)

<p>Hi everyone,</p>
<p>Im working for the first time with a .NRRD file, and in the section “volume information”, I can see the dimensions, etc. I put the header of the file at the end.</p>
<p>I need for my study know the number of bits per pixel of each image, so anyone know how to find this info?</p>
<p>Thanks, Lucas.</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: int
dimension: 3
space: left-posterior-superior
sizes: 99 99 70
space directions: (-0.16734984152442534, ...)
kinds: domain domain domain
endian: little
encoding: gzip
space origin: (28.155725441615157,32.267068921044682,65.30072153815496)
</code></pre>

---

## Post #2 by @lassoan (2022-11-07 19:10 UTC)

<aside class="quote no-group" data-username="lucas_sd" data-post="1" data-topic="26112">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucas_sd/48/17087_2.png" class="avatar"> lucas_sd:</div>
<blockquote>
<p><code>type: int</code></p>
</blockquote>
</aside>
<p>According to <a href="https://teem.sourceforge.net/nrrd/format.html#type">nrrd file format specification</a>, <code>int</code> means “signed 4-byte integer”.</p>

---
