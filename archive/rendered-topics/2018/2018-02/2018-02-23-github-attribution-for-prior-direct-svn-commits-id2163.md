# GitHub attribution for prior direct SVN commits

**Topic ID**: 2163
**Date**: 2018-02-23
**URL**: https://discourse.slicer.org/t/github-attribution-for-prior-direct-svn-commits/2163

---

## Post #1 by @ihnorton (2018-02-23 23:39 UTC)

<p>Related to <a class="mention" href="/u/jcfr">@jcfr</a>’s earlier <a href="https://discourse.slicer.org/t/commit-message-collaborative-work-and-acknowledgment/2160">post</a>: it is possible to link SVN direct-commit history in Slicer github to each contributor’s profile, although this must be done individually by the contributor, because github does not support mailmap. The following steps allow authors to claim their direct commits in the SVN history, which will then show up in the <a href="http://github.com/slicer/slicer" class="inline-onebox">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a> contributor list, and on the author’s github profile.</p>
<p>Steps:</p>
<ol>
<li>Go to Github settings</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a8b9370b83e2af80ef892c0d2293be65adaffa7.png" alt="image" data-base62-sha1="hu5i4o6O8dNZlxb4clkGL3OogzJ" width="191" height="290"></p>
<ol start="2">
<li>From the side bar, select “Emails”, then “Add email address”</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c504a0bba5c25c331ef06637903d93daf239c7d1.png" data-download-href="/uploads/short-url/s6TYyVTk0DW4OtSEzXfRgVwOY4p.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c504a0bba5c25c331ef06637903d93daf239c7d1_2_690x136.png" alt="image" data-base62-sha1="s6TYyVTk0DW4OtSEzXfRgVwOY4p" width="690" height="136" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/5/c504a0bba5c25c331ef06637903d93daf239c7d1_2_690x136.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c504a0bba5c25c331ef06637903d93daf239c7d1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c504a0bba5c25c331ef06637903d93daf239c7d1.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">740×146 9.45 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="3">
<li>Add “svn username”@<code>3bd1e089-480b-0410-8dfb-8563597acbee</code></li>
</ol>
<hr>
<p>Slicer has many more than the 7 contributors currently listed, so would be great if people could consider doing the steps above. Similar to “stars”, I think one of the quick heuristics people look at these days when considering a project on GitHub is the total number of contributors (proxy for community) as well as history of top contributors (proxy for sustained development).</p>
<p>Pinging a few active people with suggestion ready to copy and paste…</p>
<p><a class="mention" href="/u/nicole_aucoin">@Nicole_Aucoin</a>  naucoin@3bd1e089-480b-0410-8dfb-8563597acbee<br>
<a class="mention" href="/u/lassoan">@lassoan</a> lassoan@3bd1e089-480b-0410-8dfb-8563597acbee<br>
<a class="mention" href="/u/cpinter">@cpinter</a> pinter@3bd1e089-480b-0410-8dfb-8563597acbee<br>
<a class="mention" href="/u/fedorov">@fedorov</a> fedorov@3bd1e089-480b-0410-8dfb-8563597acbee<br>
<a class="mention" href="/u/ljod">@ljod</a> lauren@3bd1e089-480b-0410-8dfb-8563597acbee<br>
<a class="mention" href="/u/msmolens">@msmolens</a> msmolens@3bd1e089-480b-0410-8dfb-8563597acbee<br>
<a class="mention" href="/u/tokjun">@tokjun</a> tokuda@3bd1e089-480b-0410-8dfb-8563597acbee</p>

---

## Post #2 by @ihnorton (2018-02-23 23:41 UTC)

<p>(<a class="mention" href="/u/jcfr">@jcfr</a> has mentioned rewriting the git history if we move so that everyone is attributed, but this is quick/simple for now)</p>

---

## Post #3 by @Nicole_Aucoin (2018-02-26 15:00 UTC)

<p>I added the email you gave above, but the contributor list hasn’t updated yet. It’s the same hash for every contributor?</p>

---

## Post #4 by @ihnorton (2018-02-26 15:16 UTC)

<aside class="quote no-group" data-username="Nicole_Aucoin" data-post="3" data-topic="2163">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ebca7d/48.png" class="avatar"> Nicole_Aucoin:</div>
<blockquote>
<p>It’s the same hash for every contributor?</p>
</blockquote>
</aside>
<p>Yes, apparently it’s the svn repository UUID:</p>
<pre><code class="lang-auto">BWH003265:s5 inorton$ git svn info
Path: .
URL: http://svn.slicer.org/Slicer4/trunk
Repository Root: http://svn.slicer.org/Slicer4
Repository UUID: 3bd1e089-480b-0410-8dfb-8563597acbee
Revision: 26553
</code></pre>
<p>However, I don’t think the list updates immediately – they probably batch process the email&lt;-&gt;commit history matching for new emails (too expensive to do realtime?).</p>
<p>Andrey was not listed on Friday, but is today.</p>

---

## Post #5 by @Nicole_Aucoin (2018-02-26 15:28 UTC)

<p>Makes sense, will check again later this week.</p>

---
