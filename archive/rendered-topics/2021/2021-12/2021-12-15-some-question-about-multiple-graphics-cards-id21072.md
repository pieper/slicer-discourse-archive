---
topic_id: 21072
title: "Some Question About Multiple Graphics Cards"
date: 2021-12-15
url: https://discourse.slicer.org/t/21072
---

# Some question about multiple graphics cards

**Topic ID**: 21072
**Date**: 2021-12-15
**URL**: https://discourse.slicer.org/t/some-question-about-multiple-graphics-cards/21072

---

## Post #1 by @476663616 (2021-12-15 08:25 UTC)

<p>My lab has a server with multiple graphics cards. I am doing machine learning related operations, but slicer seems to work on graphics card 0 by default. Recently, many people are running programs, and my Slicer always prompts out of memory. How can I change the working graphics card of the Slicer?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04b750152dae2b4ec34342a7dc0e7e95f7e78c98.png" alt="1639556471(1)" data-base62-sha1="FIEES5LidmnCyhuroB7q5W9uic" width="634" height="421"><br>
I have tried the code:CUDA_VISIBLE_DEVICES=1, but it seems to help nothing…</p>
<p>Thanks for any help!</p>

---

## Post #2 by @pieper (2021-12-15 13:47 UTC)

<p>For graphics operations Slicer will use the card that’s configured for the X server (e.g. in xorg.conf).  If you are running cuda or other GPU code in Slicer you can select whichever devices are detected by the drivers.</p>

---
