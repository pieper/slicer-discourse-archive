# Loading vtkMRMLTextNode with arbitrary file name extension

**Topic ID**: 29747
**Date**: 2023-05-31
**URL**: https://discourse.slicer.org/t/loading-vtkmrmltextnode-with-arbitrary-file-name-extension/29747

---

## Post #1 by @benzwick (2023-05-31 09:48 UTC)

<p>Is it possible to load a <a href="https://apidocs.slicer.org/main/classvtkMRMLTextNode.html" rel="noopener nofollow ugc">vtkMRMLTextNode</a> with a file extension other than txt, xml or json? For example, I want to load a text file with the extension “.inp” but Slicer only shows the option to load it as a volume.</p>

---

## Post #2 by @lassoan (2023-05-31 13:55 UTC)

<p>Allowing a reader to accept arbitrary file extension leads to user confusion, so I would try to avoid doing that. Fortunately, it is not needed anymore because it is really easy to create a scripted reader for any file format.</p>
<p>You can add a few ten lines of Python script to any of your Python scripted modules that specify that the module can read of .inp files. When the user tries to open such a file then the reader can inspect the file (e.g., read the first few lines of the file to see if is indeed a file it can handle) and then offer it for reading. You can similarly specify a writer plugin. <a href="https://github.com/Slicer/Slicer/blob/main/Applications/SlicerApp/Testing/Python/SlicerScriptedFileReaderWriterTest.py">See complete examples here</a>.</p>

---

## Post #3 by @benzwick (2023-05-31 14:37 UTC)

<p>That’s perfect! I thought this was only possible using C++.</p>

---
