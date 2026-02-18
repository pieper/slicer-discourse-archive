# Slicer training page

**Topic ID**: 32513
**Date**: 2023-10-31
**URL**: https://discourse.slicer.org/t/slicer-training-page/32513

---

## Post #1 by @lassoan (2023-10-31 20:14 UTC)

<p>The <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training">Slicer training page</a> has been seriously outdated in the past several years, in content (most content is very old), functionality (hard to find what is applicable to current Slicer version; users cannot edit the page), and look&amp;feel.</p>
<p>Where should we move the page where all these issues can be fixed?</p>
<ul>
<li>Slicer source code repository: all other documentation is managed there, versioning would be automatically synchronized with the application, all the infrastructure for publishing, preview, etc. are already set up</li>
<li>Separate github repository: it could be managed separately from the application development, updates would not add noise to the code repository; we could use different template/style than the main Slicer documentation</li>
<li>Some other solutions… in essence, we would need to present a table (each row containing title, authors, description, keywords, creation/update date, Slicer version, thumbnail, URL) in some pretty, configurable way (e.g., sort and filter would be nice)</li>
</ul>
<p><a class="mention" href="/u/spujol">@spujol</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>

---

## Post #2 by @jcfr (2023-10-31 21:08 UTC)

<blockquote>
<p>present a table (each row containing title, authors, description, keywords, creation/update date, Slicer version, thumbnail, URL) in some pretty, configurable way</p>
</blockquote>
<p>We could add such a page to the  <code>slicer.org</code><sup class="footnote-ref"><a href="#footnote-102627-1" id="footnote-ref-102627-1">[1]</a></sup> where we would also describe our approach to training, provide some history, list past training events, …</p>
<p>For reference, associated Slicer issue is <a href="https://github.com/Slicer/Slicer/issues/6676">#6676</a></p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-102627-1" class="footnote-item"><p><a href="https://github.com/slicer/slicer.org">https://github.com/slicer/slicer.org</a> <a href="#footnote-ref-102627-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #3 by @pieper (2023-10-31 21:11 UTC)

<p>+1 for improving the training information.</p>
<p>Do people have examples of well organized training sites we could emulate?</p>

---

## Post #4 by @lassoan (2023-11-01 03:13 UTC)

<p>I like this style that Jc recommended: <a href="https://github.com/pyvideo/data/" class="inline-onebox">GitHub - pyvideo/data: Python related videos and metadata powering PyVideo.</a></p>

---
