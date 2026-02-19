---
topic_id: 18298
title: "How To Undo Smoothing"
date: 2021-06-23
url: https://discourse.slicer.org/t/18298
---

# How to undo Smoothing

**Topic ID**: 18298
**Date**: 2021-06-23
**URL**: https://discourse.slicer.org/t/how-to-undo-smoothing/18298

---

## Post #1 by @arezoo.movahed (2021-06-23 12:33 UTC)

<p>Hello,<br>
Is there any possibility to undo smoothing after saving?<br>
I created a human heart model and used smoothing, but we changed our strategy and I need the rough model now.<br>
Your prompt response is highly appreciated.<br>
Thank you in advance.</p>

---

## Post #2 by @hherhold (2021-06-23 12:36 UTC)

<p>If you’re referring to smoothing done by “Show 3D” in segment editor, this is the smoothing performed on the 3D viewed model. It does not affect your segmentation, and can be turned off and the smoothing level changed interactively.</p>

---

## Post #3 by @hherhold (2021-06-23 12:37 UTC)

<p>Quick clarification - once you turn off or reduce smoothing, you may need to re-export that segment to a new model and re-save it. Hope this helps.</p>

---

## Post #4 by @arezoo.movahed (2021-07-21 15:46 UTC)

<p>Thank you for your response, but unfortunately, I don’t know how to do that. I can export the STL format but I guess you mean something else should be done. Please provide me with some guidance.</p>

---

## Post #5 by @arezoo.movahed (2021-07-21 15:52 UTC)

<p>Hello,<br>
I used smoothing tool, median, for my heart model and the problem is so many walls are removed, for example two atriums are connected now! Please let me know how I can undo smoothing, otherwise I have to add walls manually and it would take ages for me.<br>
I would be truly grateful if somebody could connect to my laptop by zoom, anydesk and the like to check my model and give me some advice.<br>
Thank you in advance.<br>
Sincerely<br>
Arezoo</p>

---

## Post #6 by @lassoan (2021-07-25 15:12 UTC)

<p>To ensure that simplification does not remove walls, you can keep each ventricle as a separate segment and only merge or hollow them after smoothing.</p>

---
