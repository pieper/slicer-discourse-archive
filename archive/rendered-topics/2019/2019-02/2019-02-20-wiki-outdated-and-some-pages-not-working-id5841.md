---
topic_id: 5841
title: "Wiki Outdated And Some Pages Not Working"
date: 2019-02-20
url: https://discourse.slicer.org/t/5841
---

# Wiki outdated and some pages not working

**Topic ID**: 5841
**Date**: 2019-02-20
**URL**: https://discourse.slicer.org/t/wiki-outdated-and-some-pages-not-working/5841

---

## Post #1 by @Alex_Vergara (2019-02-20 10:39 UTC)

<p>the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/StartHere" rel="nofollow noopener">developers starting guide</a> is completely outdated.</p>
<ol>
<li>the bug tracker in MantisBT is not accepting new users.</li>
<li>the Bootcamp is based on google+ which will close on April 2, 2019</li>
</ol>
<p>So I think some actions are need to preserve the comunity.</p>

---

## Post #2 by @jamesobutler (2019-02-20 15:52 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, the following items were on the agenda for a weekly hangout recently. Do you have any meeting notes that you could share with the community?  I have seen <a href="https://github.com/Slicer/Slicer/pull/686" class="inline-onebox" rel="noopener nofollow ugc">EM Segmenter not usable after closing a scene with EMSegmenter node · Issue #686 · Slicer/Slicer · GitHub</a> as work towards the ReadTheDocs transition.</p>
<aside class="quote" data-post="2" data-topic="5741">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/2019-2-12-hangout/5741/2">2019.2.12 Hangout</a> <a class="badge-category__wrapper " href="/c/community/hangout/20"><span data-category-id="20" style="--category-badge-color: #12A89D; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This category is used to announce hangouts and organize associated notes."><span class="badge-category__name">Weekly meetings</span></span></a>
  </div>
  <blockquote>
    Documentation

Read The Docs transition
Extension documentation

Papers/citations listing format
  </blockquote>
</aside>

<p>Is a lot of this waiting on the transition to Github?  Any timeline or way to move this along so that community members who are willing to update documentation now can contribute in a meaningful way?</p>
<p>Tagging others: <a class="mention" href="/u/jcfr">@jcfr</a>, <a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #3 by @pieper (2019-02-20 17:53 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="1" data-topic="5841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>the bug tracker in MantisBT is not accepting new users.</p>
</blockquote>
</aside>
<p>is this really the case?  I believe it is still the active issue tracker, even though people tend to use github and discourse more these days.</p>

---

## Post #4 by @jcfr (2019-02-20 18:12 UTC)

<p>You should be able to create an account on the issue tracker using the “Signup for a new account” link:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bea131edd40712c66a73202804b08fb09a6c25a.png" alt="image" data-base62-sha1="jXJS0w2LlN0ZLPZrykeCECRByH0" width="510" height="107"></p>

---

## Post #5 by @jcfr (2019-02-20 18:15 UTC)

<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> Thanks for pointing out these issues <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=6" title=":+1:" class="emoji" alt=":+1:"></p>
<p>We just removed the link to Google+ from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/StartHere" rel="nofollow noopener">StartHere</a> page.</p>
<p>Let us know if you identify other discrepancies.</p>

---

## Post #6 by @cpinter (2019-02-20 18:16 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="1" data-topic="5841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/StartHere">developers starting guide </a> is completely outdated</p>
</blockquote>
</aside>
<p>Can you please be more specific which parts are completely outdated so that we can fix the biggest issues until the new documentation is up?</p>

---

## Post #7 by @jamesobutler (2019-02-21 01:49 UTC)

<p>I know everyone has a lot of things going on, but is there an expected timeline for the new documentation? That open pull request is quite old.</p>
<p>I’m more likely to issue a pull request to update some documentation, than tell someone how to clarify the wiki and suggest a new formatting of the page.</p>

---

## Post #8 by @lassoan (2019-02-21 04:44 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="7" data-topic="5841">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>is there an expected timeline for the new documentation</p>
</blockquote>
</aside>
<p>It is ready. You can send pull requests to <a href="https://github.com/Slicer/Slicer/tree/rst-user-and-dev-guide">this branch</a> and once the pull request is merged, the <a href="https://slicer.readthedocs.io/en/latest/index.html">documentation on ReadTheDocs</a> is updated automatically within minutes.</p>
<p>We’ll migrate content from the wiki page-by-page. Contribution from anyone is welcome. Once the content is moved from a wiki page, the page content is replaced with a link to the new location (using <a href="https://www.slicer.org/wiki/Template:Documentation/Nightly/slicer-manual-base-url">this template</a>).</p>
<p>We’ll advertise this more after we migrate Slicer’s main repository to GitHub (currently it is a mirror of the official SVN repository).</p>

---
