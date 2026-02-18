# Slicer binary download is extremely slow

**Topic ID**: 364
**Date**: 2017-05-23
**URL**: https://discourse.slicer.org/t/slicer-binary-download-is-extremely-slow/364

---

## Post #1 by @fedorov (2017-05-23 19:07 UTC)

<p>I started it about 20 min ago, and it gets slower and slower. Downloading from BWH on a wired connection. As I am writing this, the bandwidth dropped further to 3.5 Kb/s.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd4a37b4df424b50306faef235df40b3b4454c90.png" alt="image" data-base62-sha1="vzCwWTOJi8N3M4ZBRLP64NoFkxG" width="682" height="181"></p>

---

## Post #2 by @fedorov (2017-05-23 19:10 UTC)

<p>After I wrote the initial message, I checked the bandwidth on the connection, and it hovers under 10 Mbps, which is low. Perhaps something else is going on here.</p>

---

## Post #3 by @lassoan (2017-05-23 19:13 UTC)

<p>I’ve tried downloading Slicer now. Both the stable and nightly versions downloaded in about 45 seconds.</p>

---

## Post #4 by @mhalle (2017-05-23 19:22 UTC)

<p>Downloading at home right now takes less then a minute.</p>
<p>Sounds like a BWH network problem.</p>
<p>–Mike</p>

---

## Post #5 by @pieper (2017-05-23 20:31 UTC)

<p>I believe there is some kind of anti-virus or other scanner on the BWH firewall that gets very bogged down with big downloads.</p>

---

## Post #6 by @jcfr (2017-05-23 22:54 UTC)

<p>For comparison, is this download fast on BWH network ?<br>
See <a href="https://github.com/Slicer/Slicer/releases/download/v4.5.0-1/Slicer-4.5.0-1-linux-amd64.tar.gz">https://github.com/Slicer/Slicer/releases/download/v4.5.0-1/Slicer-4.5.0-1-linux-amd64.tar.gz</a></p>

---

## Post #7 by @fedorov (2017-05-24 16:00 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="6" data-topic="364">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>For comparison, is this download fast on BWH network ?</p>
</blockquote>
</aside>
<p>Download of the nightly from Midas: 5m51s total time (today it is much faster!) ← total download size 179M (effective bw 0.5 MB/s)<br>
Download of the stable from GitHub: 2m41s total time ← total download size 255M ( effective bw 1.59 MB/s)</p>
<p>So GitHub download (apparently served from Amazon) is over 3 times faster than download from Kitware, as measured on the internal BWH network, as of today.</p>

---

## Post #8 by @ihnorton (2017-05-24 16:11 UTC)

<p>Not that I have any objection to github, but just to note that the github download is served over https, so it may not be directly comparable – if scanning Steve mentioned is the issue, it is unlikely to be happening for an https download. From Andras message it sounds like Kitware-hosted downloads are fast elsewhere, which has also been my experience when downloading at home.</p>

---

## Post #9 by @cpinter (2017-05-24 16:29 UTC)

<p>I just downloaded the nightly in about 50 seconds. It may be related to some setting on your machine or in your network.</p>

---

## Post #10 by @fedorov (2017-05-24 16:31 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> IMHO, for a user downloading Slicer, I believe time is very directly comparable.</p>
<p>Anyway, I just reported the times to respond to <a class="mention" href="/u/jcfr">@jcfr</a> request.</p>
<p>Few points to note though:</p>
<ul>
<li>the firewall issue at Partners is hardly unique, and will be common in the hospitals, companies, and other restricted environments. But indeed I have no data to prove or disprove how common this issue is in firewalled locations.</li>
<li>arguably, many of our users are operating from such closed environments, and those are the users we should aspire to keep happy.</li>
</ul>
<p><a class="mention" href="/u/cpinter">@cpinter</a> it may indeed be unique to my machine or network, but I have not changed anything I can think of recently, and have no interest or time to contact hospital IT and explain what is going on, and why it is important for them to debug this issue.</p>

---

## Post #11 by @mhalle (2017-05-24 16:54 UTC)

<p>I’ve logged the issue with Partners.  Partners antivirus scanning has been upgraded since the recently ransomware attacks, so that might be the cause (and not surprisingly so).</p>
<p>–Mike</p>

---
