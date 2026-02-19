---
topic_id: 85
title: "Problems To Connect To The Discourse Forum From Uofm"
date: 2017-04-12
url: https://discourse.slicer.org/t/85
---

# Problems to connect to the discourse forum from UofM

**Topic ID**: 85
**Date**: 2017-04-12
**URL**: https://discourse.slicer.org/t/problems-to-connect-to-the-discourse-forum-from-uofm/85

---

## Post #1 by @bpaniagua (2017-04-12 15:17 UTC)

<p>Hi!</p>
<p>Lucia Cevidanes, Priscille de Dumast and Clement Mirabel havent been able to connect to our <a href="http://discourse.slicer.org">discourse.slicer.org</a> forum. I am posting their problems on their behalf since they cant access the forum.</p>
<p>Clement says:</p>
<blockquote>
<p>Have you been able to go on the website via your laptop? I can only connect with my smartphone.</p>
</blockquote>
<p>Lucia says:</p>
<blockquote>
<p>I cannot access it  from my laptop either. Can you please  try the  imacs too? Thanks!</p>
</blockquote>
<p>Priscille says:</p>
<blockquote>
<p>I tried all day long yesterday from the lab on my laptop without success, but I was finally able to log in yesterday evening at home!<br>
Now everything works fine both on my laptop and on the iMacs.</p>
</blockquote>
<blockquote>
<p>Could there be a problem with the Eduroam wifi with this website?</p>
</blockquote>
<p>Any idea of what might be happening?<br>
Thank you!</p>
<p>Bea</p>

---

## Post #2 by @ihnorton (2017-04-12 16:34 UTC)

<p>Do you have any more information about what happens? If the response is “URL not found” then my guess would be there was some hang-up in propagation of the DNS update which added (CNAME for) <a href="http://discourse.slicer.org">discourse.slicer.org</a></p>
<p>Could you have them try:</p>
<ul>
<li>
<code>ping discourse.slicer.org</code> in a command prompt/shell</li>
<li>temporarily changing their DNS server to 8.8.8.8 &amp; 8.8.4.4 (Google DNS servers)? Be sure to write down the old settings…</li>
<li>ping again, and try force-reloading the page (command-shift-R/ctrl-shift-R on mac/windows)</li>
</ul>
<p>There’s some other less likely possibilities, but let’s eliminate the simple one first.</p>

---

## Post #3 by @bpaniagua (2017-04-12 16:55 UTC)

<p>The ping command is fine</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4c57c7188740d1edb88df516d841af57532fc44.png" data-download-href="/uploads/short-url/wDNYt2mne2QJMzbPnr6g5AJ2aQ4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4c57c7188740d1edb88df516d841af57532fc44.png" alt="image" data-base62-sha1="wDNYt2mne2QJMzbPnr6g5AJ2aQ4" width="690" height="255" data-dominant-color="222222"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">930×344 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
And changing the DNS server changed neither the connection nor the ping answer.</p>

---

## Post #4 by @ihnorton (2017-04-12 17:48 UTC)

<p>That’s odd… so, probably not network problem. Are they using the same browser? What is the error message? Can they reach the landing page, but then get a login error? Can they open <a href="http://discourse.org">discourse.org</a> or some of the other hosted customers? (see list here: <a href="http://www.discourse.org/customers">http://www.discourse.org/customers</a>)</p>
<p>I guess it is possible the domain is blocked, but usually they would get a specific notice about that.</p>

---

## Post #5 by @ihnorton (2017-04-12 21:23 UTC)

<p>From email follow-up: the problem only happens on some wifi networks, but works fine on others. They are going to contact university IT.</p>

---
