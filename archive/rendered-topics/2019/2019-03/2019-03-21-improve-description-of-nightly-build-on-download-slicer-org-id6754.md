---
topic_id: 6754
title: "Improve Description Of Nightly Build On Download Slicer Org"
date: 2019-03-21
url: https://discourse.slicer.org/t/6754
---

# Improve description of nightly build on download.slicer.org

**Topic ID**: 6754
**Date**: 2019-03-21
**URL**: https://discourse.slicer.org/t/improve-description-of-nightly-build-on-download-slicer-org/6754

---

## Post #1 by @lassoan (2019-03-21 15:07 UTC)

<p>Should we add a note to the download page that nightly build is only recommended for developers until further notice?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/fedorov">@fedorov</a></p>

---

## Post #2 by @fedorov (2019-03-21 15:24 UTC)

<p>Maybe we should add a link to the latest stable nightly?</p>
<p>Why not revert the change, now that we know it broke many things, and take it a bit slower confirming a least the key extensions are working, and giving some warning and instructions for other extension developers to migrate? Is there a real need to rush this?</p>
<p>I understand it is virtually impossible to test everything on all platforms without factories, but it sounds like there are very obvious and easily reproducible issues that need fixing.</p>

---

## Post #3 by @pieper (2019-03-21 15:55 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="9" data-topic="6214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/slicerrt-does-not-build-due-to-missing-itk-remote-module/6214/9">SlicerRT does not build due to missing ITK remote module</a></div>
<blockquote>
<p>Should we add a note to the download page that nightly build is only recommended for developers until further notice?</p>
</blockquote>
</aside>
<aside class="quote no-group quote-post-not-found" data-username="fedorov" data-post="10" data-topic="6214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"><a href="https://discourse.slicer.org/t/slicerrt-does-not-build-due-to-missing-itk-remote-module/6214/10">SlicerRT does not build due to missing ITK remote module</a></div>
<blockquote>
<p>Maybe we should add a link to the latest stable nightly?</p>
</blockquote>
</aside>
<p>I think these are both good ideas - I also wonder if we could add something like a “status” line to the download page that indicates what the overall developer feeling is about the nightlies.  Right now the status would be “unstable because new features are being tested” but just before the release 4.10 it would be “pretty stable and contains many new features and fixes”.  Right now users only get our opinions about the status if they ask or follow the forum closely.</p>

---
