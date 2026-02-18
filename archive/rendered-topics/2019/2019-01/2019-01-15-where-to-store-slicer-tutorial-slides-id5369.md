# Where to store Slicer tutorial slides?

**Topic ID**: 5369
**Date**: 2019-01-15
**URL**: https://discourse.slicer.org/t/where-to-store-slicer-tutorial-slides/5369

---

## Post #1 by @lassoan (2019-01-15 05:03 UTC)

<p>Most tutorials are created using PowerPoint but published on the Slicer wiki as pdf. To facilitate contributions, we should make the source files available in GitHub. Which repository should we use?</p>
<p>There are these existing repositories that we might consider but we could also create a new one:</p>
<ul>
<li><a href="https://github.com/Slicer/tutorials.slicer.org" rel="nofollow noopener">https://github.com/Slicer/tutorials.slicer.org</a></li>
<li><a href="https://github.com/Slicer/Slicer-DataStore" rel="nofollow noopener">https://github.com/Slicer/Slicer-DataStore</a></li>
<li><a href="https://github.com/Slicer/SlicerTestingData" rel="nofollow noopener">https://github.com/Slicer/SlicerTestingData</a></li>
</ul>
<p><a class="mention" href="/u/spujol">@spujol</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @jcfr (2019-01-15 14:23 UTC)

<p>Do we want to manage the original slide document (ppt, …) as (1) “text file” or as (2) “release asset” ?</p>
<p>(1) this approach is well suited for document that compress well and can be efficiently managed using source control management like git. This does not apply for slide document because they do not compress well. (to some extent svn would be more suited as it would only check out one version of the document at a time)</p>
<p>(2) this approach is to both work around the fact a git repo would get large very quickly and leverage the free storage offered by GitHub.</p>
<blockquote>
<p><a href="https://github.com/Slicer/tutorials.slicer.org">tutorials.slicer.org</a></p>
</blockquote>
<p>The aim of this project was to host the actual html sources of a future portal for tutorial, I think original slide document (powerpoint, openoffice, …) should be uploaded somewhere else. May be as release assets ?</p>
<blockquote>
<p><a href="https://github.com/Slicer/Slicer-DataStore">https://github.com/Slicer/Slicer-DataStore </a></p>
</blockquote>
<p>This repo hold the sources of the DataStore extension. I don’t think it is a good option.</p>
<blockquote>
<p><a href="https://github.com/Slicer/SlicerTestingData">https://github.com/Slicer/SlicerTestingData </a></p>
</blockquote>
<p>This repo supports the upload of testing data as release assets and their  retrieval based on their hashsum. Original slide documents could be uploaded there or in a different repo using a similar mechanism.</p>

---

## Post #3 by @spujol (2019-01-15 17:28 UTC)

<p>The original materials could be uploaded as release assets in a new SlicerTutorialData repository on GitHub.</p>

---
