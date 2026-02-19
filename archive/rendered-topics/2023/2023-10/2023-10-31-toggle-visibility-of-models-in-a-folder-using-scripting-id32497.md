---
topic_id: 32497
title: "Toggle Visibility Of Models In A Folder Using Scripting"
date: 2023-10-31
url: https://discourse.slicer.org/t/32497
---

# Toggle visibility of models in a folder using scripting

**Topic ID**: 32497
**Date**: 2023-10-31
**URL**: https://discourse.slicer.org/t/toggle-visibility-of-models-in-a-folder-using-scripting/32497

---

## Post #1 by @Chris_Klink (2023-10-31 05:23 UTC)

<p>Hi Experts,<br>
I’m trying to toggle the visibility of individual models inside a folder from a Python script. I can toggle the visibility of the entire folder, but all examples I can find of how to loop over the children don’t work because the display folder object does not have a get children or getnumberofchildren attribute. I must be overlooking something obvious and would appreciate some pointers.<br>
Thanks!<br>
Chris</p>

---

## Post #2 by @lassoan (2023-11-01 14:57 UTC)

<p>The folder display node is a MRML node. It does not know how to iterate through the subject hierarchy. Instead, you can:</p>
<ul>
<li>get the subject hierarchy node</li>
<li>get the subject hierarchy item ID corresponding to the folder display node</li>
<li>use the subject hierarchy node to iterate through children of that subject hierarchy item using its ID</li>
</ul>

---
