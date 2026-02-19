---
topic_id: 31223
title: "Error To Load Obj File Message Failed To Read Node Null Null"
date: 2023-08-18
url: https://discourse.slicer.org/t/31223
---

# Error to load .obj file message: “Failed to read node (null ((null)) ... "

**Topic ID**: 31223
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/error-to-load-obj-file-message-failed-to-read-node-null-null/31223

---

## Post #1 by @estro (2023-08-18 15:22 UTC)

<p>Hello, I am running into an error message logged as:</p>
<p>vtkMRMLStorageNode::ReadData: Failed to read node (null) ((nul)) from filename= … .obj’</p>
<p>This is all that the error message gives me when I tried importing an .obj file as Segmentation. Any help is appreciated!</p>

---

## Post #2 by @muratmaga (2023-08-18 16:17 UTC)

<p>Can you load the model as a model into Slicer? If that works you can right click and choose convert to segmentation object.</p>
<p>Otherwise it might be something wrong with the file/format</p>

---

## Post #3 by @lassoan (2023-08-18 20:21 UTC)

<p>Could you please provide the full application log (upload somewhere and post the link here)?<br>
You can get the application log using the menu: Help / Report a bug.</p>

---
