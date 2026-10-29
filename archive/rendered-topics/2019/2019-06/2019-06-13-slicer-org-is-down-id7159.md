---
topic_id: 7159
title: "Slicer.org is down"
date: 2019-06-13
url: https://discourse.slicer.org/t/7159
last_bumped: 2026-10-28T20:54:51.395Z
---

# Slicer.org is down

**Topic ID**: 7159
**Date**: 2019-06-13
**URL**: https://discourse.slicer.org/t/slicer-org-is-down/7159

---

## Post #1 by @lassoan (2019-06-13 14:00 UTC)

<p><a href="http://www.slicer.org">www.slicer.org</a> and <a href="http://issues.slicer.org">issues.slicer.org</a> are down. Could somebody have a look?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/093843b77020c966842fc03532aa50dad1e6bfeb.png" alt="image" data-base62-sha1="1jyQi3BYp4i5AxfLHwWxIOEkceT" width="505" height="497"></p>
<p><a class="mention" href="/u/freephile">@freephile</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #2 by @pieper (2019-06-13 14:30 UTC)

<p><a href="http://na-mic.org" rel="nofollow noopener">na-mic.org</a> and the wikis are down too.</p>
<p><a class="mention" href="/u/mhalle">@mhalle</a></p>

---

## Post #3 by @mhalle (2019-06-13 15:28 UTC)

<p>I just talked to Greg, he’s already working on it.</p>
<p>—Mike</p>

---

## Post #4 by @rkikinis (2019-06-13 16:31 UTC)

<p>Thanks for the update</p>

---

## Post #5 by @lassoan (2026-10-27 18:11 UTC)

<p>Happened again, <a href="http://slicer.org">slicer.org</a> is down:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7294761b56be00dc7d112456796865aba8a1c250.png" data-download-href="/uploads/short-url/glCvx7zDscBcXwMLTTB7uquK5Bm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7294761b56be00dc7d112456796865aba8a1c250_2_491x500.png" alt="image" data-base62-sha1="glCvx7zDscBcXwMLTTB7uquK5Bm" width="491" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7294761b56be00dc7d112456796865aba8a1c250_2_491x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7294761b56be00dc7d112456796865aba8a1c250_2_736x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7294761b56be00dc7d112456796865aba8a1c250_2_982x1000.png 2x" data-dominant-color="313232"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×1065 43.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Sam_Horvath (2026-10-28 17:25 UTC)

<p>Status update: We are working on relocating the hosting of the main landing page, <a class="mention" href="/u/mhalle">@mhalle</a> we just need to get the DNS record updated</p>

---

## Post #7 by @mhalle (2026-10-28 18:18 UTC)

<p>What record do you need?</p>

---

## Post #8 by @Sam_Horvath (2026-10-28 20:51 UTC)

<p>For <a href="http://slicer.org">slicer.org</a>, We need to remove the existing A records for root and www, then add the for A / AAAA records from github: <a href="https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#dns-records-for-your-custom-domain" class="inline-onebox">Managing a custom domain for your GitHub Pages site - GitHub Docs</a></p>
<p>Also add a CNAME record for www to <a href="http://slicer.github.io">slicer.github.io</a></p>

---

## Post #9 by @Sam_Horvath (2026-10-28 20:54 UTC)

<p>Or we could just do that transfer of the domain to Kitware, and we’ll take care of it</p>

---
