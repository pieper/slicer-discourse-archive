# Stream IGTLink Data from one computer to another when on same network

**Topic ID**: 5263
**Date**: 2019-01-03
**URL**: https://discourse.slicer.org/t/stream-igtlink-data-from-one-computer-to-another-when-on-same-network/5263

---

## Post #1 by @aab (2019-01-03 14:59 UTC)

<p>Operating system: Windows 64 bit<br>
Slicer version: 4.4.0</p>
<p>Hi all,<br>
I’m using IGTLink with an NDI Tracking system (Polaris Vicra - communicates serrially using USB) and I want to be able to stream the locational data I get from my laptop to another. Both are on the same network and are pingable.<br>
My network protocol knowledge is a bit limited but since there is a hostname and port assigned, I should be able to use this? Has anyone ever tried doing this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7912e16d447a6fac6310fc183b20865fc5432f60.png" data-download-href="/uploads/short-url/hh4dYjamQfgUFZ8RakejpWxNvZm.png?dl=1" title="IGTLink" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/7912e16d447a6fac6310fc183b20865fc5432f60.png" alt="IGTLink" data-base62-sha1="hh4dYjamQfgUFZ8RakejpWxNvZm" width="512" height="500" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IGTLink</span><span class="informations">570×556 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-01-03 15:33 UTC)

<p>This is a very common use case. We use <a href="http://www.plustoolkit.org" rel="nofollow noopener">Plus toolkit</a> for acquiring tracking data from NDI tracker and broadcast it via OpenIGTLink.</p>

---

## Post #3 by @MARKRONSON (2019-08-22 13:12 UTC)

<p>yes, i am facing the similar issue . and i am looking for a solution to it. if anyone out there knows the answer to it , kindly reply here</p>

---

## Post #4 by @lassoan (2019-08-22 13:42 UTC)

<p>See step-by-step tutorials at <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT website Tutorials section</a>.</p>

---
