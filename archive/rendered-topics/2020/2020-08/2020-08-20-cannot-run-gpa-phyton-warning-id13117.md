---
topic_id: 13117
title: "Cannot Run Gpa Phyton Warning"
date: 2020-08-20
url: https://discourse.slicer.org/t/13117
---

# Cannot run GPA phyton warning

**Topic ID**: 13117
**Date**: 2020-08-20
**URL**: https://discourse.slicer.org/t/cannot-run-gpa-phyton-warning/13117

---

## Post #1 by @Sandra_Ospina (2020-08-20 17:27 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11<br>
Expected behavior: Visualizar 3d volumen in GPA<br>
Actual behavior: Not running</p>
<p>Hello, I can´t  do some operations in the GPA moduel, when I try to paste the code in the phyton window, I got this message:  UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.</p>
<p>What can i do?</p>

---

## Post #2 by @lassoan (2020-08-20 17:31 UTC)

<p>Thanks for letting us know. This is not an error. When a package imports “pandas” package then pandas logs this warning. It is highly unlikely that you will need lzma compression, but if yes, then you’ll get an error message, so you can safely ignore the warning.</p>
<p>Anyway, this issue is tracked <a href="https://github.com/Slicer/Slicer/issues/4920">here</a>, but unless it blocks someone from doing something, its priority will remain low.</p>

---

## Post #3 by @Sandra_Ospina (2020-08-21 14:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13117">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Anyway, this issue is tracked <a href="https://github.com/Slicer/Slicer/issues/4920" rel="noopener nofollow ugc">here</a>, but unless it blocks someone from doing something, its priority will remain low.</p>
</blockquote>
</aside>
<p>Thank you very much!</p>

---

## Post #4 by @smrolfe (2020-08-21 15:55 UTC)

<p>Hi <a class="mention" href="/u/sandra_ospina">@Sandra_Ospina</a> can you follow up with me if you are still having issues running this module?</p>

---

## Post #5 by @Sandra_Ospina (2020-08-21 16:03 UTC)

<p>Hi Sara! Actually I was able to run it…I think the problem is my computer memory. Thank you!</p>

---
