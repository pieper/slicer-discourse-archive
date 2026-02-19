---
topic_id: 30239
title: "Loading Folders And Data"
date: 2023-06-26
url: https://discourse.slicer.org/t/30239
---

# Loading folders and data

**Topic ID**: 30239
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/loading-folders-and-data/30239

---

## Post #1 by @Patrick_Li (2023-06-26 16:51 UTC)

<p>I’m looking for a way to load a directory. For example, I want to be able to load the selected folder in the screenshot from a specific directory on my device. While I’ve found loadVolume() and loadSegmentation() functions, I haven’t found one for directories.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de8d29d1bb8063a1036c5461ac642b98ac9e4ff.png" data-download-href="/uploads/short-url/fGiRBEwh1mYtxpNC54cOEspAS0T.png?dl=1" title="Screenshot 2023-06-26 125053" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de8d29d1bb8063a1036c5461ac642b98ac9e4ff_2_390x500.png" alt="Screenshot 2023-06-26 125053" data-base62-sha1="fGiRBEwh1mYtxpNC54cOEspAS0T" width="390" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de8d29d1bb8063a1036c5461ac642b98ac9e4ff_2_390x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de8d29d1bb8063a1036c5461ac642b98ac9e4ff.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de8d29d1bb8063a1036c5461ac642b98ac9e4ff.png 2x" data-dominant-color="F1F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-26 125053</span><span class="informations">458×587 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-06-28 03:08 UTC)

<p>You can get the list of files in a folder using standard Python functions and then call <code>slicer.util.loadNodeFromFile(filepath)</code> for each file.</p>

---
