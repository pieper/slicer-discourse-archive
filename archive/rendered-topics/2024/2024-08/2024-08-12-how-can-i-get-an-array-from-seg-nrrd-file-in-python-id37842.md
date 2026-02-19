---
topic_id: 37842
title: "How Can I Get An Array From Seg Nrrd File In Python"
date: 2024-08-12
url: https://discourse.slicer.org/t/37842
---

# How can I get an array from seg.nrrd file in Python?

**Topic ID**: 37842
**Date**: 2024-08-12
**URL**: https://discourse.slicer.org/t/how-can-i-get-an-array-from-seg-nrrd-file-in-python/37842

---

## Post #1 by @rim (2024-08-12 12:39 UTC)

<p>I want to read the data from the seg.nrrd file using the nrrd.read() function and obtain it in array format as a 3D array. However, the data in the seg.nrrd file consists only of arrays filled with zeros.</p>
<p>What might I be missing?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a87c52057bfa27829489fc5775261f65e143f66.png" data-download-href="/uploads/short-url/64eWgbInuKwlyAr0FB4yoDiVE9w.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a87c52057bfa27829489fc5775261f65e143f66_2_690x179.png" alt="image" data-base62-sha1="64eWgbInuKwlyAr0FB4yoDiVE9w" width="690" height="179" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a87c52057bfa27829489fc5775261f65e143f66_2_690x179.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a87c52057bfa27829489fc5775261f65e143f66_2_1035x268.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a87c52057bfa27829489fc5775261f65e143f66_2_1380x358.png 2x" data-dominant-color="3F3F36"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1484×385 47.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-08-12 12:42 UTC)

<p>You are probably not missing anything. Labelmap files containing segmentations are usually mostly zeros.</p>
<p>What do you get if you run this command?</p>
<pre data-code-wrap="python"><code class="lang-python">print(np.count_nonzero(label_mask))
</code></pre>

---
