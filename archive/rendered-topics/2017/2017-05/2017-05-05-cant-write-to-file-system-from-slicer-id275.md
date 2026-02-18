# Can't write to file system from Slicer

**Topic ID**: 275
**Date**: 2017-05-05
**URL**: https://discourse.slicer.org/t/cant-write-to-file-system-from-slicer/275

---

## Post #1 by @tdiprima (2017-05-05 20:43 UTC)

<p>I really could use some advice, not sure what to do at this point.</p>
<p>So we’re trying to write a zip file, for the user, to a directory of their choosing.<br>
The procedure works on Linux and Mac, but not Windows.<br>
The problem is, no matter what directory we try to write to on Windows, it doesn’t want to write to any of them.</p>
<p>Let’s say we try to write a zip file to the user’s home folder.  The zip file gets created, but with zero bytes.</p>
<p>This is the error that occurs:<br>
<code>UpdateFileList: Failed to create directoryTempWriteoriginal</code></p>
<p>It looks like the error is being generated from here: vtkMRMLVolumeArchetypeStorageNode.cxx, but it’s not clear <strong>why</strong> it can’t create the directory.</p>
<p>Test 1: The user is able to create a directory to their file system outside of Slicer.  Pass.</p>

---

## Post #2 by @lassoan (2017-05-05 21:17 UTC)

<p>The temporary directory path points to an invalid/read-only location. Edit your application settings.</p>

---
