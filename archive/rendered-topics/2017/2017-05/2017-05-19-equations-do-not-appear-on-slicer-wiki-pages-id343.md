# Equations do not appear on Slicer wiki pages

**Topic ID**: 343
**Date**: 2017-05-19
**URL**: https://discourse.slicer.org/t/equations-do-not-appear-on-slicer-wiki-pages/343

---

## Post #1 by @lassoan (2017-05-19 01:46 UTC)

<p>Question moved here from <a href="http://slicer-devel.65872.n3.nabble.com/wiki-troubles-td4038511.html">mailing list</a>:</p>
<p>Hey guys,</p>
<p>I wanted to point of of my students to the coordinate systems wiki page and it is in a pretty bad shape.<br>
Anyone aware of this?</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<p>I also attach a screenshot.</p>
<p>Thanks,<br>
Attila</p>

---

## Post #2 by @lassoan (2017-05-19 02:02 UTC)

<p>Submitted a bug report: <a href="http://na-mic.org/Mantis/view.php?id=4374">http://na-mic.org/Mantis/view.php?id=4374</a></p>

---

## Post #3 by @mhalle (2017-05-19 02:19 UTC)

<p>Looks like <a href="https://formulasearchengine.com/" rel="nofollow noopener">https://formulasearchengine.com/</a> , which the wiki module uses for math formatting, is busted.  At this point, I can’t find any information about the site or its status.  If anyone has any insight or workaround, I can pass it onto our maintainer.</p>
<p>–Mike</p>

---

## Post #4 by @pieper (2017-05-19 11:32 UTC)

<p>Probably there’s a newer way to embed latex in mediawiki pages.  Yes, it<br>
would be great if Greg could look into it.</p>

---

## Post #5 by @jcfr (2017-05-19 17:44 UTC)

<p>While  <a href="https://formulasearchengine.com/">https://formulasearchengine.com/</a>  does not work, the url:</p>
<p><a href="http://api.formulasearchengine.com/v1/">http://api.formulasearchengine.com/v1/</a></p>
<p>seems to be valid.</p>
<p>Also for production server, it is recommended to use our own mathoid server. See <a href="https://www.mediawiki.org/wiki/Extension:Math">https://www.mediawiki.org/wiki/Extension:Math</a></p>

---

## Post #6 by @mhalle (2017-05-19 19:10 UTC)

<p>When I tested it yesterday I don’t think the HTTP endpoint wasn’t working, so maybe they’re working on things or moving them around.</p>
<p>At any rate, there are often problems running HTTP services on SSL-secured pages, so even if it work it wouldn’t be ideal.</p>
<p>Running our own server for just this?  Ugh.</p>
<p>–Mike</p>

---

## Post #7 by @pieper (2017-05-19 19:45 UTC)

<p>By the way, no server is really needed -<br>
<a href="http://manuels.github.io/texlive.js/" class="onebox" target="_blank">http://manuels.github.io/texlive.js/</a></p>
<p>But whatever is easiest to install and maintain.  There are other pages on<br>
the na-mic wiki with equations and it would be good to have modern<br>
supported mediawiki solution.</p>

---

## Post #8 by @jcfr (2017-05-22 13:43 UTC)

<aside class="quote no-group" data-username="pieper" data-post="7" data-topic="343">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>By the way, no server is really needed -<br>
<a href="http://manuels.github.io/texlive.js/">http://manuels.github.io/texlive.js/</a></p>
</blockquote>
</aside>
<p>Looks neat, but still require some work to be integrated.</p>
<p>Instead, I would suggest to look into <a href="https://www.mathjax.org/">https://www.mathjax.org/</a></p>

---

## Post #9 by @pieper (2017-05-22 14:43 UTC)

<p>We should probably let Greg advise us on the best solution for mediawiki integration.</p>
<p><a href="https://www.mediawiki.org/wiki/Extension:Math#MathJax" class="onebox" target="_blank">https://www.mediawiki.org/wiki/Extension:Math#MathJax</a></p>

---
