---
topic_id: 32238
title: "How Can I Update The Contents Of The Warning Window In Slice"
date: 2023-10-16
url: https://discourse.slicer.org/t/32238
---

# How can I update the contents of the warning window in Slicer?

**Topic ID**: 32238
**Date**: 2023-10-16
**URL**: https://discourse.slicer.org/t/how-can-i-update-the-contents-of-the-warning-window-in-slicer/32238

---

## Post #1 by @dsa934 (2023-10-16 06:58 UTC)

<p>Operating system:window 10<br>
Slicer version: 5.4</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db193ca135ce671256349c066ffc4ef7bae44b13.png" alt="image" data-base62-sha1="vgeDpCyEzUAjDd2S2l40NdBWgfh" width="543" height="265"></p>
<p>I made it to display a notification window via QtMessageBox when certain conditions are not met.</p>
<p>But how can I update a new alert window to an existing alert window without multiple alert windows appearing as shown above?</p>

---

## Post #2 by @lassoan (2023-10-16 18:06 UTC)

<p>You can modify properties of your messagebox object to change its text.</p>
<p>Note that this question is not specific to Slicer but in general about how to use Qt in Python. Bing Chat or ChatGPT should be able to answer these kind of generic questions accurately. You can even ask Slicer-specific questions, but those answers more often require some adjustments.</p>

---

## Post #3 by @dsa934 (2023-10-16 23:22 UTC)

<p>To be precise, I am curious about the function to delete only the msgbox among the various objects rendered in the slicer window.</p>
<p>For example, the ‘slicer.mrmlScene.Clear()’ command deletes all objects in the slicer. Where can I find information about deleting only specific objects?</p>
<p>Ah, while I was replying, I suddenly remembered a method.</p>

---

## Post #4 by @jamesobutler (2023-10-16 23:43 UTC)

<aside class="quote no-group" data-username="dsa934" data-post="3" data-topic="32238">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dsa934/48/17907_2.png" class="avatar"> dsa934:</div>
<blockquote>
<p>Ah, while I was replying, I suddenly remembered a method.</p>
</blockquote>
</aside>
<p>Please post here if what you remembered worked. Since this thread already exists, it can serve as future reference for someone running into the same issue as you.</p>

---
