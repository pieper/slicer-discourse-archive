---
topic_id: 17838
title: "Convert Seg Nrrd To Nrrd Labelmap"
date: 2021-05-28
url: https://discourse.slicer.org/t/17838
---

# Convert .seg.nrrd to nrrd labelmap

**Topic ID**: 17838
**Date**: 2021-05-28
**URL**: https://discourse.slicer.org/t/convert-seg-nrrd-to-nrrd-labelmap/17838

---

## Post #1 by @siyuan (2021-05-28 12:34 UTC)

<p>Hi, I was wondering how I could convert .seg.nrrd to a nrrd labelmap using pure python.<br>
Here is an attempt from my friend. It works but it may throw a broadcasting error sometime.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/636cb1ee4a9ec55c0ce4d748bd0c4cb46754804e.png" data-download-href="/uploads/short-url/eby99u0TViM63hFABN2RTXTIug6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/636cb1ee4a9ec55c0ce4d748bd0c4cb46754804e.png" alt="image" data-base62-sha1="eby99u0TViM63hFABN2RTXTIug6" width="689" height="413" data-dominant-color="070707"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1206×723 21.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot.</p>

---

## Post #2 by @lassoan (2021-05-28 21:37 UTC)

<p>Good news: segmentation is already a labelmap. You can use any nrrd file reader. There is an <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-information-from-segmentation-nrrd-file-header">example in the script repository</a> of how to extract information about the segments from the custom fields in the header. This script is usable in any Python environment, not just in Slicer’s.</p>
<p>I’m in the process of creating a standalone Python package (that can be pip installed into any Python environment) for convenient reading/writing of Slicer-specific file formats (segmentations, markups, etc.) from Python, but it will probably take a week or so to become available.</p>

---

## Post #3 by @siyuan (2021-05-29 04:02 UTC)

<p>Thank you for reply, and this will help me a lot. <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"> <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #4 by @lassoan (2021-05-29 04:48 UTC)

<p>I created a first version of the <code>slicerio</code> package. It can read and write .seg.nrrd files:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://pypi.org/static/images/favicon.6a76275d.ico" class="site-icon" width="15" height="15">

      <a href="https://pypi.org/project/slicerio/" target="_blank" rel="noopener">PyPI</a>
  </header>

  <article class="onebox-body">
    <img src="https://pypi.org/static/images/twitter.90915068.jpg" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://pypi.org/project/slicerio/" target="_blank" rel="noopener">slicerio</a></h3>

  <p>Utilities for 3D Slicer</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Please try it and let me know if you find it useful or if you need more features.</p>

---

## Post #5 by @siyuan (2021-08-01 17:11 UTC)

<p>For those who still use old-version Slicer:<br>
Python package pynrrd can read the header of a .seg.nrrd and you will find some ‘extend’ keywords. These keywords define the local-region of label and what u need to do is to map it back to reference size.<br>
For exmaple, in the following picture: the Segmentation_ReferenceImageExtentOffset 344 257 12 means your segmentation start from 344 in x, 257 in y, 12 in z and then based on the size of segmentation array, you can easily map it to reference volume size. Code will be uploaded soon.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eab8a1f2da6631b9236daabf34ba9d09dcbf3324.png" data-download-href="/uploads/short-url/xuriHthiEotPrIlh34uLwOS6Pg8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eab8a1f2da6631b9236daabf34ba9d09dcbf3324_2_690x357.png" alt="image" data-base62-sha1="xuriHthiEotPrIlh34uLwOS6Pg8" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eab8a1f2da6631b9236daabf34ba9d09dcbf3324_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eab8a1f2da6631b9236daabf34ba9d09dcbf3324_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eab8a1f2da6631b9236daabf34ba9d09dcbf3324_2_1380x714.png 2x" data-dominant-color="EBE9E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1800×932 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @fghazouani (2021-12-14 15:55 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a><br>
I manage to use the slicerio package to read a .seg.nrrd file and to get the number of segments.<br>
My question know how I can display each segment (label) from the extracted segment information.</p>
<p>Thank you</p>

---

## Post #7 by @lassoan (2021-12-14 17:32 UTC)

<p>It depends on what software would you like to use for image display. For very primitive visualizations you can use matplotlib (you can then just use <code>slicerio.extract_segments</code> for each segment), but for proper evaluation of 3D segmentations, multiple segments, overlay on the input image, in 2D and 3D, all in correct physical space, etc. you would probably much better off using Slicer. You can use Slicer as a Jupyter notebook kernel if you prefer using Jupyter notebooks instead of the Slicer GUI.</p>

---

## Post #8 by @fghazouani (2021-12-15 08:21 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your answer.<br>
I know that Slicer is the best tool to display segments and overlay on the input image, what I need is to do the same thing, i.e., get segment by segment and not all overlayed on the image.<br>
I have succeed by using SimpleITK to overlay segments with the input image, but now i want to use <code>slicerio.extract_segments</code> to extract each segment separately like in the figure below.<br>
I know that <code>slicerio.extract_segments</code> provide a voxel arrays, (for example with shape [512, 512, 170]), but how I can use <code>slicerio.extract_segments</code> for each segment from this voxel arrays.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96fdfac16956b63ebbbefd9de175a7383cbc4c00.png" data-download-href="/uploads/short-url/lxJLGFMbdNnRCdf1J7U7erB8Wic.png?dl=1" title="segments" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96fdfac16956b63ebbbefd9de175a7383cbc4c00_2_690x136.png" alt="segments" data-base62-sha1="lxJLGFMbdNnRCdf1J7U7erB8Wic" width="690" height="136" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96fdfac16956b63ebbbefd9de175a7383cbc4c00_2_690x136.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96fdfac16956b63ebbbefd9de175a7383cbc4c00.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96fdfac16956b63ebbbefd9de175a7383cbc4c00.png 2x" data-dominant-color="DEE9EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segments</span><span class="informations">720×142 20.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21f05b67268d3575dbf863ad79bd4fe52c3fc4fa.png" alt="image" data-base62-sha1="4QeIAgXxYLd8LIMjmSQQ9UFlHSi" width="304" height="130"></p>

---

## Post #9 by @lassoan (2021-12-16 06:00 UTC)

<p>You can get voxels of a single segment into <code>segment_voxel</code> numpy array like this:</p>
<pre><code class="lang-python">input_filename = "path/to/Segmentation.seg.nrrd"
segment_name = "ribs"
label_value = 1

import slicerio
segmentation_info = slicerio.read_segmentation_info(input_filename)
voxels, header = nrrd.read(input_filename)
segment_voxels, segment_header = slicerio.extract_segments(voxels, header, segmentation_info, [(segment_name, label_value)])
</code></pre>

---

## Post #10 by @fghazouani (2021-12-16 15:42 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>Thank you very much for your help.<br>
It work very well now!</p>

---
