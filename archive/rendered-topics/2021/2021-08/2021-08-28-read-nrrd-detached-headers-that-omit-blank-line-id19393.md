---
topic_id: 19393
title: "Read Nrrd Detached Headers That Omit Blank Line"
date: 2021-08-28
url: https://discourse.slicer.org/t/19393
---

# Read NRRD detached headers that omit blank line

**Topic ID**: 19393
**Date**: 2021-08-28
**URL**: https://discourse.slicer.org/t/read-nrrd-detached-headers-that-omit-blank-line/19393

---

## Post #1 by @Chris_Rorden (2021-08-28 12:52 UTC)

<p>I have a feature request to allow Slicer to detect NRRD detached headers where the user omits the trailing blank line. Tested on Slicer 4.13.0-2021-08-24 r30133 / 5af0a09</p>
<p>The <a href="http://teem.sourceforge.net/nrrd/format.html" rel="noopener nofollow ugc">NRRD format specification</a> clearly states <code>After the header, there is a single blank line containing zero characters.</code> However, this requirement is not obvious to users who create text-only detached headers. Currently, Slicer will fail to load a <code>.nhdr</code> file that omits this blank line. Slicer generates a vague error message, and since most text editors do not show white space the issue is not obvious. I would suggest that Slicer either read nhdr files that omit the trailing blank line, or detect this and warn the user that the image is not valid. So while Slicers current behavior is strictly correct, it could be extended to prevent this simple error.</p>
<p>All of these <a href="https://klacansky.com/open-scivis-datasets/" rel="noopener nofollow ugc">datasets</a> exhibit this <a href="https://klacansky.com/open-scivis-datasets/metadata/" rel="noopener nofollow ugc">issue</a>. One can directly download a dataset to see the issue:</p>
<pre><code class="lang-auto">curl -LO https://klacansky.com/open-scivis-datasets/metadata/neghip.nhdr 
curl -LO http://cdn.klacansky.com/open-scivis-datasets/neghip/neghip_64x64x64_uint8.raw
</code></pre>

---

## Post #2 by @pieper (2021-08-31 19:07 UTC)

<p>Hi <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> - thanks for reporting this; supporting this small deviation is probably a friendly thing to do for the reasons you cite.  However, when I downloaded the data using the steps you reported it loaded fine for me (on mac with my local build and a binary release).  Are you sure these file can be used to replicate?  Is there another that are broken?  In any case this might be something to be addressed at the ITK or teem level if we think that supporting these files is a good idea in general.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/174105360039742709ee9a58e8f4438319f43d99.jpeg" data-download-href="/uploads/short-url/3jIhOl08z1ECW2qJ4Q0QTaJ4Dbz.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/174105360039742709ee9a58e8f4438319f43d99_2_628x500.jpeg" alt="image" data-base62-sha1="3jIhOl08z1ECW2qJ4Q0QTaJ4Dbz" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/174105360039742709ee9a58e8f4438319f43d99_2_628x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/174105360039742709ee9a58e8f4438319f43d99.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/174105360039742709ee9a58e8f4438319f43d99.jpeg 2x" data-dominant-color="313133"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">769×612 58.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
