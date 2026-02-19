---
topic_id: 32218
title: "Textnode Not Shown In Save Dialog"
date: 2023-10-13
url: https://discourse.slicer.org/t/32218
---

# Textnode not shown in save dialog

**Topic ID**: 32218
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/textnode-not-shown-in-save-dialog/32218

---

## Post #1 by @Jeff_Zeyl (2023-10-13 17:42 UTC)

<p>On slicer 5.4.0 after creating a new text node from within the texts module, the textnode does not appear in the save dialog, though other nodes do appear. It’s still saved in the scene file. Is there a way to have the txt file node appear in this dialog?</p>

---

## Post #2 by @lassoan (2023-10-13 18:01 UTC)

<p>By default, short text (&lt;256 characters) is saved in the scene file to avoid polluting the file system with many tiny files. You can call this method of the text node to force saving it into a separate file regardless of text length:</p>
<pre><code>myTextNode.SetForceCreateStorageNode(slicer.vtkMRMLTextNode.CreateStorageNodeAlways)
</code></pre>

---
