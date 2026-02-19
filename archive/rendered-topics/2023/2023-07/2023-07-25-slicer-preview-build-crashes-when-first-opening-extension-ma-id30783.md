---
topic_id: 30783
title: "Slicer Preview Build Crashes When First Opening Extension Ma"
date: 2023-07-25
url: https://discourse.slicer.org/t/30783
---

# Slicer preview build crashes when first opening extension manager

**Topic ID**: 30783
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/slicer-preview-build-crashes-when-first-opening-extension-manager/30783

---

## Post #1 by @Justin_Kirby (2023-07-25 15:10 UTC)

<p>I got the following error after a fresh installation of the Preview Build (7-25) on Windows 10 when clicking “Install Extensions” on the Slicer homescreen:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eaa2b09315aa51ed1d802ace77963f8b3eb5bbb.png" alt="image" data-base62-sha1="8WmbzwixI3khN81MpZRtRk037XJ" width="618" height="291"></p>
<p>It crashed the program completely.  I don’t see any errors in the log file though.  When I tried again to open Slicer this “Install Extensions” button works fine the next time.</p>
<p>I ran into exactly the same behavior installing the last few days of preview builds where it fails the first time and works without error in subsequent attempts.</p>

---

## Post #2 by @pieper (2023-07-28 00:58 UTC)

<p>Thanks for reporting this <a class="mention" href="/u/justin_kirby">@Justin_Kirby</a>.  Can anyone else running on windows can report if this happens to them?</p>

---

## Post #3 by @jamesobutler (2023-07-28 12:56 UTC)

<p>On my corporate laptop running Windows 10 Enterprise 21H2, Slicer 5.3.0-2023-07-26 and Slicer 5.3.0-2023-07-25 both launched extension manager the first time successfully. I had these installed into the default user data location.</p>

---

## Post #4 by @pieper (2023-07-28 14:10 UTC)

<p>Thanks for testing <a class="mention" href="/u/jamesobutler">@jamesobutler</a> .  <a class="mention" href="/u/justin_kirby">@Justin_Kirby</a> is there anything you can think of that’s unique to your machine where the issue occurs?</p>

---

## Post #5 by @Justin_Kirby (2023-07-28 18:24 UTC)

<p>It’s my work laptop so there are a bunch of security things that prevent installations, etc but I can’t see why that would matter if it works properly the 2<sup>nd</sup> time I launch Slicer. I also have a bunch of preview slicer installations on my laptop, but I doubt that’s unique to me. It’s probably not worth chasing this down any further if this isn’t a widespread issue. It’s easy for me to work around for now and I’m hoping to get a new laptop sometime soon anyway <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @lassoan (2023-07-28 20:52 UTC)

<p>I haven’t experienced this and have not heard about this problem from others either, but it would be nice to fix it. It is hard to know what could cause this error (it launches a Chromium browser that does a tons of things and there is also a lot of network comunication to query the extensions list from the server, etc.). Could you maybe build Slicer in debug mode to see where the error occurs?</p>

---
