---
topic_id: 8045
title: "Loading Only Specific Images In A Folder"
date: 2019-08-15
url: https://discourse.slicer.org/t/8045
---

# Loading only specific images in a folder. 

**Topic ID**: 8045
**Date**: 2019-08-15
**URL**: https://discourse.slicer.org/t/loading-only-specific-images-in-a-folder/8045

---

## Post #1 by @garbulinskamaja (2019-08-15 15:05 UTC)

<p>I have a folder with 460 images. I would like to load only 3 of them at the same time. Not one and not 460 using the python interactor.<br>
Now to load all of them I am using this code:</p>
<pre><code class="lang-python">image_path_slicer = os.path.join(project_path, "data/06_WK1_01_crop_0000.tif")
[success, volume] = slicer.util.loadVolume(filename = image_path_slicer, returnNode=True) 
</code></pre>
<p>So, is there anyway I could choose “06_WK1_01_crop_0000.tif”, “06_WK1_01_crop_0001.tif”, “06_WK1_01_crop_0002.tif” and load only these without creating a new folder with just these files?</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @lassoan (2019-08-15 15:09 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.loadVolume" rel="nofollow noopener"><code>singleFile</code></a> argument to force loading a single file. Example for recent Slicer Preview Release (<code>returnNode</code> argument is no longer needed):</p>
<pre><code class="lang-python">volume = slicer.util.loadVolume(filename = image_path_slicer, singleFile=True)
</code></pre>

---
