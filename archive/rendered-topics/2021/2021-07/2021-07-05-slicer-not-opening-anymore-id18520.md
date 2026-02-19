---
topic_id: 18520
title: "Slicer Not Opening Anymore"
date: 2021-07-05
url: https://discourse.slicer.org/t/18520
---

# Slicer not opening anymore

**Topic ID**: 18520
**Date**: 2021-07-05
**URL**: https://discourse.slicer.org/t/slicer-not-opening-anymore/18520

---

## Post #1 by @bcolbert (2021-07-05 15:21 UTC)

<p>I am using a Windows desktop with plenty of RAM (64gb, no other programs open). Slicer worked fine until 20minutes ago when it crashed my computer when opening up a relatively small dataset. Computer restarted and now I am unable to open slicer.</p>
<p>When I open the program I get the initial window and the program shows up in the task manager, then a few seconds later the status in task manager changes to “suspending” and then closes out.</p>
<p>I have uninstalled and reinstalled slicer and am using latest stable version. Other programs appear to run fine on the computer. Any ideas?</p>

---

## Post #2 by @geoffkfleee (2021-07-05 21:27 UTC)

<p>So a ‘fun’ bug I noticed is that Slicer has trouble opening on non-primary monitors. <a href="https://trac.wxwidgets.org/ticket/18532" rel="noopener nofollow ugc">I believe it is closely related to this issue, or some variation of it.</a> It’s not you. It’s OpenGL.</p>
<p>An experiment to verify this is to unplug the second monitor or any other non-primary monitor, open Slicer, and see if it works. You may have to try moving it if it’s starting off-screen.</p>
<p>Cheers.</p>

---

## Post #3 by @bcolbert (2021-07-05 22:01 UTC)

<p>I think this was some obscure issue related to my PC. I got another BSOD when the computer restarted it went into recovery mode. After restarting again slicer worked fine. Who knows.</p>

---
