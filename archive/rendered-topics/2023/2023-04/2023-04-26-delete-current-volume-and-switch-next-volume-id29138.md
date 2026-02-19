---
topic_id: 29138
title: "Delete Current Volume And Switch Next Volume"
date: 2023-04-26
url: https://discourse.slicer.org/t/29138
---

# delete current volume and switch next volume.

**Topic ID**: 29138
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/delete-current-volume-and-switch-next-volume/29138

---

## Post #1 by @Benjamin-JZ (2023-04-26 12:01 UTC)

<p>I want make a button for something,I need to delete current volume in my button signal slot.how can i do that?</p>

---

## Post #2 by @pearsonm (2023-04-26 23:38 UTC)

<p>Do you mean a single volume or the whole scene?</p>
<p>For the scene you can call<br>
<code>slicer.mrmlScene.Clear()</code></p>
<p>For a single node you can call<br>
<code>slicer.mrmlScene.RemoveNode(volumeNode)</code></p>

---

## Post #3 by @Benjamin-JZ (2023-04-27 02:51 UTC)

<p>Thank you for reply. i got done.But i want to ask new question that can i pick a volume which is i wanted in mutiple volumes situation ?if yes,Please teach me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @Benjamin-JZ (2023-04-27 07:27 UTC)

<p>oh,i got one more question,which is that i want to export a segmentation to files with nifit format.<br>
I have readed the developer guide ,But still don’t know how should i do. <img src="https://emoji.discourse-cdn.com/twitter/grimacing.png?v=12" title=":grimacing:" class="emoji" alt=":grimacing:" loading="lazy" width="20" height="20"></p>

---
