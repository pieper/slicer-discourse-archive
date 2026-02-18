# How to convert .xfm file to regular .tfm file to import in Slicer

**Topic ID**: 7784
**Date**: 2019-07-28
**URL**: https://discourse.slicer.org/t/how-to-convert-xfm-file-to-regular-tfm-file-to-import-in-slicer/7784

---

## Post #1 by @ljc19800331 (2019-07-28 02:57 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello, I have download the data and the transformation file is .xfm. Is there a good way in python or 3D slicer that I could directly read the transformation and convert my MRI data to the standard coordinate system? Thanks.</p>
<p>example:<br>
MNI Transform File</p>

---

## Post #2 by @lassoan (2019-07-29 04:11 UTC)

<p>What is an xfm file? Can you save the transform as a standard ITK transform file instead? Slicer can already read those, either text or binary, even if they are composite transforms.</p>
<p>The example MNI transform file did not come through. If you want to share a file, the best way is typically to upload it to a cloud storage service (onedrive, gdrive, dropbox, etc) and post the link here.</p>
<p>If ITK library already supports reading of these transform files then we should be make it available in Slicer.</p>

---

## Post #3 by @ljc19800331 (2019-07-29 04:32 UTC)

<p>Thanks. The file is shown in this link:<br>
<aside class="onebox googledrive">
  <header class="source">
      <a href="https://drive.google.com/file/d/1gbKUqoABoL4BKwZMrqwyzsR-izgevrqV/view?usp=sharing" target="_blank" rel="nofollow noopener">drive.google.com</a>
  </header>
  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1gbKUqoABoL4BKwZMrqwyzsR-izgevrqV/view?usp=sharing" target="_blank" rel="nofollow noopener"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1gbKUqoABoL4BKwZMrqwyzsR-izgevrqV/view?usp=sharing" target="_blank" rel="nofollow noopener">14_transform_mr_back_in_native.xfm</a></h3>

<p>Google Drive file.</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>This file is downloaded from open source dataset: <a href="http://nist.mni.mcgill.ca/?page_id=672" rel="nofollow noopener">http://nist.mni.mcgill.ca/?page_id=672</a></p>
<p>Thanks.</p>

---
