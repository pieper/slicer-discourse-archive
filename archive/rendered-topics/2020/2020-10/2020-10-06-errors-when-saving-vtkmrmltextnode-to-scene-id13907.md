# Errors when saving vtkMRMLTextNode to scene

**Topic ID**: 13907
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/errors-when-saving-vtkmrmltextnode-to-scene/13907

---

## Post #1 by @mikebind (2020-10-06 20:27 UTC)

<p>I was following the suggestion from <a href="https://discourse.slicer.org/t/whats-the-best-approach-to-saving-additional-data-associated-with-a-module/9018/3">here</a> to use a vtkMRMLTextNode when the amount of text to store is a bit large or complex for a ParameterNode.  However, I now get errors when trying to save the scene.  Specifically, I get red “X” icons next to any text node I try to save, and the following error in the log:</p>
<pre><code>No writer found to write file QVariant(QString, "C:/Users/mikeb/Documents/Neuro/TEMP/Testing/Slicer/RSO_TextNode.txt") of type "MyFileType"
</code></pre>
<p>No .txt files are saved and when I load the scene the text nodes are empty.<br>
Also, in the Save dialog, the text nodes always show “Not Modified” in the status regardless of whether they have been modified or not (and since they’ve never actually been successfully saved, they should probably all show as “Modified” until a successful save).</p>
<p>I have tried fiddling a bit with the SetForceCreateStorageNode() function and tried CreateDefaultStorageNode(), but neither seemed to affect the saving bug.</p>

---

## Post #2 by @lassoan (2020-10-06 20:51 UTC)

<p>This false alarm is caused by a testing script. I’ll submit a fix soon.</p>

---

## Post #3 by @mikebind (2020-10-06 21:10 UTC)

<p>Thanks!  Is there a workaround until then?</p>

---

## Post #4 by @lassoan (2020-10-07 03:44 UTC)

<p>Fixed - <a href="https://github.com/Slicer/Slicer/commit/23171356da12fb67ed3232822a524d2f6abf9f37">https://github.com/Slicer/Slicer/commit/23171356da12fb67ed3232822a524d2f6abf9f37</a>. As a workaround, you can delete <code>SlicerScriptedFileReaderWriterTest.py</code>.</p>

---
