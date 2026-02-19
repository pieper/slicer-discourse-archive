---
topic_id: 646
title: "Cleaning Up Search Results Robots Txt Exclusion For Old Docu"
date: 2017-07-07
url: https://discourse.slicer.org/t/646
---

# Cleaning up search results: robots.txt exclusion for old documentation

**Topic ID**: 646
**Date**: 2017-07-07
**URL**: https://discourse.slicer.org/t/cleaning-up-search-results-robots-txt-exclusion-for-old-documentation/646

---

## Post #1 by @ihnorton (2017-07-07 16:12 UTC)

<p>Slicer’s search results are currently not as helpful as they could be. For example, the top results for the following searches are almost all outdated versioned wiki pages (often 3.6 or very early 4.x series):</p>
<p><a href="https://www.google.com/search?hl=en&amp;q=slicer+editor&amp;pws=0">slicer editor</a><br>
<a href="https://www.google.com/search?hl=en&amp;q=slicer+image+guidance&amp;pws=0">slicer image guidance</a><br>
<a href="https://www.google.com/search?hl=en&amp;q=slicer+navigation&amp;pws=0">slicer navigation</a><br>
<a href="https://www.google.com/search?hl=en&amp;q=slicer+diffusion+tutorial&amp;pws=0">slicer diffusion tutorial</a><br>
<a href="https://www.google.com/search?hl=en&amp;q=slicer+openigtlink&amp;pws=0">slicer openigtlink</a></p>
<p>Considering that we are now de facto using nightly as a rolling release, I’d like to propose excluding older wiki documentation versions from indexing by using the following entry in the <a href="https://github.com/Slicer/slicer.org/blob/slicer-org/robots.txt">slicer.org robots.txt</a>. (if that’s too extreme, we could also allow <code>/4.6</code>)</p>
<pre><code>Disallow: /wiki/Documentation/*
Allow: /wiki/Documentation/Nightly/*
</code></pre>
<p>Based on <a>mediawiki</a> and <a href="https://developers.google.com/search/reference/robots_txt#order-of-precedence-for-group-member-records">google</a> documentation, this should result in <em>only</em> the nightly documentation being indexed.</p>
<hr>
<p>It may also be useful to disallow searching the images folder, which will prevent old PDF versions from being indexed:</p>
<pre><code>/w/images/*
</code></pre>
<p>The upshot would be better control over visibility and versioning by eliminating direct PDF links in search results, but I’m not sure about downside ramifications if any.</p>
<hr>
<p>cc <a class="mention" href="/u/freephile">@freephile</a> <a class="mention" href="/u/mhalle">@mhalle</a></p>

---

## Post #2 by @pieper (2017-07-07 19:01 UTC)

<p>But aren’t the page ranks based on other pages that link to our pages?  I’d guess that’s why some of the older links are still the highest hits.</p>
<p>Are we sure that blocking the old pages from scanning would make the now pages show up at the top of google, or maybe the links to older pages just stop being considered.</p>
<p>Currently we have the banner on old pages that suggests people look at the newer pages – but maybe we should actually redirect to the newest instead with a banner option to go back to the older page.</p>

---

## Post #3 by @lassoan (2017-07-07 19:59 UTC)

<p>Instead of specific versions, probably the best would be to only have two versions of the documentation in the search results: “stable” and “latest”. But then it would be difficult to retrieve documentation for specific software versions.</p>
<p>Overall, I’ve lost faith in the wiki to be used for user guide (reference manual, detailed documentation of modules). I think documentation generated from the code, stored in the same repository as the code, made available through ReadTheDocs and as a downloadable pdf for each specific version would be a more sustainable solution. You can have a look at how Segment Editor’s documentation looks like in ReadTheDocs now: <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html</a>.</p>

---

## Post #4 by @fedorov (2017-07-07 20:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I’ve lost faith in the wiki to be used for user guide</p>
</blockquote>
</aside>
<p>Me too, a while ago.</p>
<p>So now that we have two different mechanisms for documentation - what are the advantages of keeping using the wiki as the primary/recommended?</p>
<p>Are instructions on populating content on ReadTheDocs available somewhere? Or is this just an experiment?</p>

---

## Post #5 by @lassoan (2017-07-07 20:14 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="4" data-topic="646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Are instructions on populating content on ReadTheDocs available somewhere?</p>
</blockquote>
</aside>
<p>It’s still experimental, but the mechanism works very nicely, just the content is not there yet.</p>
<p>If you just want to make edits to an existing page then click “Edit on GitHub” link at the top. Once you finished your edits GitHub will offer to create a pull request for you automatically, just accept that and you are good to go. Once the pull request is merged, the documentation is rebuilt automatically.</p>
<p>If you want to make significant edits, adding lots of pages, etc. then you can work on <a href="https://github.com/Slicer/Slicer/tree/rst-user-and-dev-guide">this branch</a> locally, generate documentation using Sphinx, etc. and once you are done you can send a pull request with all your changes.</p>

---

## Post #6 by @pieper (2017-07-07 20:15 UTC)

<p>We still have the problem of SEO - searching for ‘slicer segmentation editor’ still takes you to the wiki which doesn’t (yet) link to readthedocs.</p>

---

## Post #7 by @lassoan (2017-07-07 20:42 UTC)

<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>searching for ‘slicer segmentation editor’ still takes you to the wiki which doesn’t (yet) link to readthedocs</p>
</blockquote>
</aside>
<p>Yes, for now. I expect that when we’ll start using readthedocs for real then it’ll move up in the page ranks. Google finds readthedocs documentation pages of other projects.</p>

---
