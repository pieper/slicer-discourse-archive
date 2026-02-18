# Extension Manager crash

**Topic ID**: 44199
**Date**: 2025-08-25
**URL**: https://discourse.slicer.org/t/extension-manager-crash/44199

---

## Post #1 by @Catalina_Balzo (2025-08-25 18:46 UTC)

<p>Hi, I recently tried to upgrade my slicer from version 5.6 to 5.8.1, but I encountered a serious problem. Version 5.8.1 runs fine, but whenever I try to open the Extension Manager the program crashes. Because of this, I had to go back to the older version, where extension manager works perfectly fine. Is anyone else experiencing the same issue?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2025-08-25 18:49 UTC)

<p>Does the latest Slicer preview release work well?<br>
What operating system do you use?<br>
Can you share a screen capture video so that we can see exactly what is happening?</p>

---

## Post #3 by @Catalina_Balzo (2025-08-25 20:45 UTC)

<p>Hi Andras, I followed the steps you mentioned in another topic and it worked. I copied the entire 5.8.1 folder to a USB drive and ran the program from there, and the Extension Manager worked. It seems that the two versions interfere with each other. Thank you for your reply!</p>

---

## Post #4 by @muratmaga (2025-08-26 10:01 UTC)

<aside class="quote no-group" data-username="Catalina_Balzo" data-post="3" data-topic="44199">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/catalina_balzo/48/80885_2.png" class="avatar"> Catalina_Balzo:</div>
<blockquote>
<p>I copied the entire 5.8.1 folder to a USB drive and ran the program from there, and the Extension Manager worked.</p>
</blockquote>
</aside>
<p>This suggests you originally installed Slicer in a place that extension manager cannot write (perhaps to C:/Program Files, or maybe using admin credentials).</p>

---
