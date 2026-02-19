---
topic_id: 641
title: "Windows Slicer Util Loadvolume Loads Wrong Volume"
date: 2017-07-06
url: https://discourse.slicer.org/t/641
---

# [Windows] slicer.util.loadVolume loads wrong volume

**Topic ID**: 641
**Date**: 2017-07-06
**URL**: https://discourse.slicer.org/t/windows-slicer-util-loadvolume-loads-wrong-volume/641

---

## Post #1 by @che85 (2017-07-06 22:42 UTC)

<p>Hi developers,</p>
<p>I am having the following problems under Windows when programmatically loading a volume. Always the wrong volume is loaded into Slicer. The directory that I shared here has two volumes:</p>
<p>a. MRI Prostate image (two files)<br>
b. ZFrame template (one file)</p>
<p>Please try the following on Windows:</p>
<h2>load prostate image</h2>
<p>This is supposed to load the prostate volume, but it doesn’t. It loads the template image which is located in the same directory.<br>
<code><br>
prostateVolume = slicer.util.loadVolume(‘a000001.dcm’, returnNode=True)<br>
</code></p>
<p>#<a class="hashtag" href="https://discourse.slicer.org/tag/load">#<span>load</span></a> template image<br>
<code><br>
templateVolume = slicer.util.loadVolume(‘b000001.dcm’, returnNode=True)<br>
</code></p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/sh/klhh0566rggt0o5/AAB9vVwULXBNbfnag3tEB50sa?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:214/200;"><img src="https://cfl.dropboxstatic.com/static/images/logo_catalog/glyph_m1%402x.png" class="thumbnail" width="214" height="200"></div>

<h3><a href="https://www.dropbox.com/sh/klhh0566rggt0o5/AAB9vVwULXBNbfnag3tEB50sa?dl=0" target="_blank" rel="nofollow noopener">Dropbox - Error</a></h3>

<p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Does anyone know what the problem is here? Those issues neither occur on MacOS nor on Ubuntu.</p>
<p>I noticed that when using the “add data” dialog sometimes the files are classified as “Scalar overlay” which is not loaded correctly.</p>
<p>Thanks<br>
Christian</p>

---

## Post #2 by @lassoan (2017-07-06 23:03 UTC)

<p>I guess you need to specify that it should be loaded as a single file and not as a multi-file DICOM series:</p>
<pre><code>prostateVolume = slicer.util.loadVolume('a000001.dcm', {'singleFile': True}, returnNode=True)</code></pre>

---

## Post #3 by @che85 (2017-07-07 01:18 UTC)

<p>It works with the setting singleFile to True but that doesn’t solve the problem since the dataset has more than one slice.  <code>a000001.dcm</code> and <code>a000002.dcm</code> belong to the same dataset.</p>
<p>And it doesn’t explain why it works as expected on Ubuntu and MacOS without even adding anything else than I am using in the first post.</p>
<p>When I manually selected the file in the “add data”-dialog and set explicitly description to “Volume” then it works even when I uncheck property <code>singleFile</code></p>

---

## Post #4 by @lassoan (2017-07-07 04:49 UTC)

<p>I’ve debugged into this and the problem is caused by using backslash path separator character or drive letter capitalization. I’ve made file comparison mechanism more robust (normalizing filenames before comparison) in r26146, which should fix the problem.</p>

---

## Post #5 by @che85 (2017-07-07 13:40 UTC)

<p>I am glad that you found something. I will try with the next nightly build. Thanks a lot!</p>

---

## Post #6 by @fedorov (2017-07-07 14:24 UTC)

<p><a class="mention" href="/u/che85">@che85</a> why would you want to use this loader for a DICOM series instead of the ScalarVolume DICOM plugin?</p>

---

## Post #7 by @che85 (2017-07-07 14:39 UTC)

<p>We used to do that in SliceTracker and I was not looking for a workaround. We can switch to that if you prefer.</p>

---

## Post #8 by @fedorov (2017-07-07 14:49 UTC)

<p>I didn’t realize this is going on. I would definitely switch to the DICOM plugin. Most likely, that util function is just using straight ITK reader, since it is the same call that is used to read non-DICOM data.</p>

---

## Post #9 by @lassoan (2017-07-07 15:06 UTC)

<p>Ultimately, scalar images are always read by ITK reader. The difference is how the list of files is determined and how they deal with inconsistencies (varying spacing, non-parallel slices, etc).</p>
<p>ScalarVolume DICOM plugin requires a list of files (files may spread across various folders) and the plugin sorts all the files and provides the file list to the ITK reader.</p>
<p>When you load a DICOM volume using slicer.util.loadVolume then the ITK reader receives only a single filename and the ITK reader determines the file list (it considers filenames in the same folder, checks series UID match, and sorts based on image position patient).</p>

---
