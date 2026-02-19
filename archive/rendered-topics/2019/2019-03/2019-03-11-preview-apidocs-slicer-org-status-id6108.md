---
topic_id: 6108
title: "Preview Apidocs Slicer Org Status"
date: 2019-03-11
url: https://discourse.slicer.org/t/6108
---

# Preview.apidocs.slicer.org status

**Topic ID**: 6108
**Date**: 2019-03-11
**URL**: https://discourse.slicer.org/t/preview-apidocs-slicer-org-status/6108

---

## Post #1 by @fedorov (2019-03-11 17:55 UTC)

<p>Is <a href="https://github.com/Slicer/preview.apidocs.slicer.org">preview.apidocs.slicer.org</a> something that is supposed to be usable or “previewable”?</p>
<p>Currently, the link shows the below, which I am not sure corresponds to the description of that resource:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/086f9ff29e1aa67183b9b079b27ff6bff34e2a15.png" alt="image" data-base62-sha1="1cCYr4HUz2ncqv18K074KR3VheB" width="656" height="232"></p>
<p>According to the readme at <a href="https://github.com/Slicer/preview.apidocs.slicer.org:">https://github.com/Slicer/preview.apidocs.slicer.org:</a></p>
<blockquote>
<p>This project hosts the Slicer API documentation served from <a href="http://preview.apidocs.slicer.org/">http://preview.apidocs.slicer.org</a></p>
</blockquote>

---

## Post #2 by @fedorov (2019-03-11 17:57 UTC)

<p>Maybe it is superseded by <a href="http://apidocs.slicer.org/" rel="nofollow noopener">http://apidocs.slicer.org/</a>? Should we remove “preview” from the github organization if this is the case? Some users may discover this resource by browsing the Slicer GitHub organization content.</p>

---

## Post #3 by @jcfr (2019-03-11 18:12 UTC)

<ul>
<li>
<p><a href="https://apidocs.slicer.org">https://apidocs.slicer.org</a> is the released documentation associated Github project with more details is <a href="https://github.com/Slicer/apidocs.slicer.org" class="inline-onebox">GitHub - Slicer/apidocs.slicer.org: This project hosts and serves the Slicer API documentation</a></p>
</li>
<li>
<p><a href="https://preview.apidocs.slicer.org">https://preview.apidocs.slicer.org</a> is for “previewing” documentation associated with PR. Associated github project with more details is <a href="https://github.com/Slicer/preview.apidocs.slicer.org" class="inline-onebox">GitHub - Slicer/preview.apidocs.slicer.org: This project hosts and serves a preview version of Slicer API documentation</a></p>
</li>
</ul>
<p>The “Details” link leads to the <a href="https://preview.apidocs.slicer.org">https://preview.apidocs.slicer.org</a> website.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99400e5d6f520c4677f67acb349de22fe0acbff7.png" data-download-href="/uploads/short-url/lRIi8DduK8wU9ic7cabpQPtxdMX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99400e5d6f520c4677f67acb349de22fe0acbff7_2_690x87.png" alt="image" data-base62-sha1="lRIi8DduK8wU9ic7cabpQPtxdMX" width="690" height="87" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/99400e5d6f520c4677f67acb349de22fe0acbff7_2_690x87.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99400e5d6f520c4677f67acb349de22fe0acbff7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99400e5d6f520c4677f67acb349de22fe0acbff7.png 2x" data-dominant-color="F3F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">911×115 10.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jcfr (2019-03-11 18:15 UTC)

<p>If you would like to add more details, you could update the <code>index.html</code> page available at: <a href="https://github.com/Slicer/preview.apidocs.slicer.org/blob/gh-pages-reset/index.html" rel="nofollow noopener">https://github.com/Slicer/preview.apidocs.slicer.org/blob/gh-pages-reset/index.html</a></p>

---

## Post #5 by @fedorov (2019-03-11 18:41 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="6108">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p><a href="https://preview.apidocs.slicer.org">https://preview.apidocs.slicer.org</a> is for “previewing” documentation associated with PR.</p>
</blockquote>
</aside>
<p>Makes sense now that you explain it! Thanks! Should I make a pull request to replace</p>
<blockquote>
<p>This project hosts the Slicer API documentation served from <a href="http://preview.apidocs.slicer.org/">http://preview.apidocs.slicer.org</a></p>
</blockquote>
<p>with</p>
<blockquote>
<p>This project hosts the preview of Slicer API documentation associated with PRs, served from <a href="http://preview.apidocs.slicer.org/">http://preview.apidocs.slicer.org</a></p>
</blockquote>
<p>?</p>

---

## Post #6 by @jcfr (2019-03-11 19:03 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="6108">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Should I make a pull request</p>
</blockquote>
</aside>
<p>In fact, no need for a PR, I suggest you directly update these two files (you already have push access):</p>
<ul>
<li><a href="https://github.com/Slicer/preview.apidocs.slicer.org/blob/gh-pages-reset/index.html" class="inline-onebox">preview.apidocs.slicer.org/index.html at gh-pages-reset · Slicer/preview.apidocs.slicer.org · GitHub</a></li>
<li><a href="https://github.com/Slicer/preview.apidocs.slicer.org/blob/gh-pages/index.html" class="inline-onebox">preview.apidocs.slicer.org/index.html at gh-pages · Slicer/preview.apidocs.slicer.org · GitHub</a></li>
</ul>
<p>To understand the rational for updating the two files, you could read <a href="https://github.com/Slicer/preview.apidocs.slicer.org#reset-of-gh-pages-branch-using-travisci-cron-job">here</a></p>

---

## Post #7 by @fedorov (2019-03-11 19:10 UTC)

<p>Sounds good, I will look later. If I am the only one confused, no need to make any changes. Let’s leave as is.</p>

---

## Post #8 by @jcfr (2019-03-11 19:25 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="7" data-topic="6108">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>If I am the only one confused, no need to make any changes</p>
</blockquote>
</aside>
<p>The change makes complete sense <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
