# Converting .stl files into segments for editing

**Topic ID**: 7764
**Date**: 2019-07-26
**URL**: https://discourse.slicer.org/t/converting-stl-files-into-segments-for-editing/7764

---

## Post #1 by @stl (2019-07-26 00:37 UTC)

<p>Operating system:Windows<br>
Slicer version: 4.10</p>
<p>Hi,</p>
<p>I have a group of .stl files that I have downloaded for a region of the body. I would like to convert them into segments that I can edit to further refine the model.</p>
<p>I am unable to take the .stl (model) files and import them as segments into a segmentation. Is there a way to do this?</p>
<p>Thanks!</p>

---

## Post #2 by @fedorov (2019-07-26 00:38 UTC)

<aside class="quote no-group" data-username="stl" data-post="1" data-topic="7764">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/6de8d8/48.png" class="avatar"> stl:</div>
<blockquote>
<p>I am unable to take the .stl (model) files and import them as segments into a segmentation.</p>
</blockquote>
</aside>
<p>What do you mean? How did you try to load them into Slicer, and what happened?</p>

---

## Post #3 by @stl (2019-07-26 01:00 UTC)

<p>Thanks for the quick response.</p>
<p>I can load the stl files and also view them. However I need to edit the files. I read that they need to be converted into segments and that’s where I’m getting stuck. I see no options to convert the stl files into segments in a segmentation.</p>
<p>Thanks!</p>

---

## Post #4 by @fedorov (2019-07-26 01:27 UTC)

<p>Did you see this documentation page, and the “Import …” section: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a></p>
<p>Please let us know if this answers your question.</p>

---

## Post #5 by @stl (2019-07-26 02:12 UTC)

<p>I did try that but there’s nothing under “Copy/Move segments” after I’ve loaded the stl files. I’ve included a screenshot.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbd9bd18be0f5fd0bd4c39060d3d0ff491c1562d.png" data-download-href="/uploads/short-url/t5lqCIgIB3LjQaIDG3HUTKbpkVD.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbd9bd18be0f5fd0bd4c39060d3d0ff491c1562d_2_690x340.png" alt="image" data-base62-sha1="t5lqCIgIB3LjQaIDG3HUTKbpkVD" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbd9bd18be0f5fd0bd4c39060d3d0ff491c1562d_2_690x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbd9bd18be0f5fd0bd4c39060d3d0ff491c1562d_2_1035x510.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbd9bd18be0f5fd0bd4c39060d3d0ff491c1562d_2_1380x680.png 2x" data-dominant-color="B0B2BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1913×943 66.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2019-07-26 02:18 UTC)

<p>You can import models using “Export/import models and labelmaps” section.</p>
<p>You may also load the STL file directly as segmentation (see instructions in <a href="https://discourse.slicer.org/t/3d-model-to-segmentation/5135/2">this post</a>).</p>

---
