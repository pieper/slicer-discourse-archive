# Open files from multiple subdirectories

**Topic ID**: 3035
**Date**: 2018-06-01
**URL**: https://discourse.slicer.org/t/open-files-from-multiple-subdirectories/3035

---

## Post #1 by @ladybug (2018-06-01 09:16 UTC)

<p>Hello,</p>
<p>I’m trying to open files with extension .nrrd from multiple subfolders. So far I only got to open one file at a time. This is the working version:<br>
dir_path = qt.QFileDialog.getOpenFileName(self.parent, ‘Open file’, ‘D:\SlicerTest\THA’, “All Files (*.nrrd)”)<br>
dir_path = dir_path.replace("\", “/”)</p>
<p>The other version that is not working (the files with my .nrrd extension are not even visible) looks as follows:<br>
dir_path = qt.QFileDialog.getExistingDirectory(None, ‘Open folder’, ‘/home/’, qt.QFileDialog.ShowDirsOnly)<br>
Also, I would like to select the folders that I want to open, e.g. from 89 to 95.</p>
<p>I would appreciate any feedback.<br>
Best!</p>

---

## Post #2 by @ihnorton (2018-06-01 13:47 UTC)

<aside class="quote no-group" data-username="ladybug" data-post="1" data-topic="3035">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/46a35a/48.png" class="avatar"> ladybug:</div>
<blockquote>
<p>I’m trying to open files with extension .nrrd</p>
</blockquote>
</aside>
<p>Have a look at the utility functions to open files via python, starting here:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/dc998411aff0cc92c137374a297de6a1c5c52a88/Base/Python/slicer/util.py#L320" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/dc998411aff0cc92c137374a297de6a1c5c52a88/Base/Python/slicer/util.py#L320</a></p>
<aside class="quote no-group" data-username="ladybug" data-post="1" data-topic="3035">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/46a35a/48.png" class="avatar"> ladybug:</div>
<blockquote>
<p>I would like to select the folders that I want to open, e.g. from 89 to 95.</p>
</blockquote>
</aside>
<p>You can use python’s directory iteration tool to get the file or directory names, and then test the filename to make your selection, see:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/dc998411aff0cc92c137374a297de6a1c5c52a88/Base/Python/slicer/util.py#L1317-L1329" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/dc998411aff0cc92c137374a297de6a1c5c52a88/Base/Python/slicer/util.py#L1317-L1329</a></p>

---
