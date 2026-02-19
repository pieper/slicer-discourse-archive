---
topic_id: 25890
title: "Cannot Reach Extension Web Server"
date: 2022-10-25
url: https://discourse.slicer.org/t/25890
---

# Cannot reach extension web server

**Topic ID**: 25890
**Date**: 2022-10-25
**URL**: https://discourse.slicer.org/t/cannot-reach-extension-web-server/25890

---

## Post #1 by @ferhue (2022-10-25 09:56 UTC)

<p>Hello, today I was trying to install one extension, but I am unable to access the server. This is the message I get within Slicer’s extension manager:</p>
<h1><a name="p-85097-extensions-can-not-be-installed-1" class="anchor" href="#p-85097-extensions-can-not-be-installed-1" aria-label="Heading link"></a>Extensions can not be installed.</h1>
<ul>
<li>Failed to load extension page using this URL: <strong><a href="https://extensions.slicer.org/catalog/All/30893/linux" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a></strong></li>
<li>Check that <strong>3D Slicer</strong> is properly installed. <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#installing-3d-slicer" rel="noopener nofollow ugc">Read more…</a></li>
</ul>
<p>Try Again</p>
<p>I am using Ubuntu 22.04 and Slicer 5.0.3 stable.</p>
<p>I also tried directly entering from different web browsers the extensions website, to no avail.</p>
<p>Is someone experiencing the same?<br>
Thanks!</p>

---

## Post #2 by @jay1987 (2022-10-25 12:43 UTC)

<p>i meet the problem before and use vpn to solve this problem</p>

---

## Post #3 by @ferhue (2022-10-25 13:23 UTC)

<p>oh, I see… so maybe it’s the same issue as in <a href="https://discourse.slicer.org/t/new-release-5-0-3-unable-to-download-extension/24524/2" class="inline-onebox">New release 5.0.3, unable to download extension - #2 by lassoan</a><br>
Thanks.</p>

---

## Post #4 by @ferhue (2022-11-07 16:16 UTC)

<p>I solved this now by adding 8.8.8.8 and 8.8.4.4 to the DNS nameservers, without having to use any VPN.</p>

---

## Post #5 by @lassoan (2022-11-07 18:14 UTC)

<p>Thank you. These IP addresses are Google’s DNS servers, which are safe to use. Maybe your previous DNS settings were not correct, or the DNS servers were misconfigured (either accidentally, or intentionally - to try to restrict what sites can be accessed).</p>

---

## Post #6 by @ferhue (2022-11-07 18:38 UTC)

<p>Well, the default DNS servers were those from my university (local), so probably intentionally restrictive.</p>

---
