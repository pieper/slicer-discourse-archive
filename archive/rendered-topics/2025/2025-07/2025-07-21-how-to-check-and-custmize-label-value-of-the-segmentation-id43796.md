# How to check and custmize label value of the segmentation?

**Topic ID**: 43796
**Date**: 2025-07-21
**URL**: https://discourse.slicer.org/t/how-to-check-and-custmize-label-value-of-the-segmentation/43796

---

## Post #1 by @phranchi (2025-07-21 14:12 UTC)

<p>Hi everyone,</p>
<p>I want to export my segmentation to label map for deep learning. The deep learning tool requires every segmentation in the same label map file and I do need to keep all the label value for each segmentation the same across all the label map files I feed into the tool. However, I failed to find the information for the segmentation’s label value, nor did I find how to appoint a label value to a specific segmentation. Is there a built in function for that in 3d slicer?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2025-07-21 14:30 UTC)

<p>This is a very common need and there are se erap ways to achieve it.</p>
<p>The most important is to <a href="https://github.com/SlicerMorph/Tutorials?tab=readme-ov-file#creating-custom-color-tables-with-terminologies">use standard terminology</a> for segments when you create the segmentation. If you use Auto3DSeg or TotalSegmentator then it is already done.</p>
<p>You can then either choose a color table when you export the segmentation (that maps terminology to label value); or use <a href="https://pypi.org/project/slicerio/">slicerio Python package</a> to get segments as a numpy array from a .seg.nrrd file.</p>

---

## Post #3 by @phranchi (2025-07-22 05:08 UTC)

<p>Thank you very much, Lassoan.</p>
<p>I have adopted color table as you suggested. However, how do I know exactly which label is mapped to each segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f85b37c2b840c72ec35adab75be6f5383708c2a9.png" data-download-href="/uploads/short-url/zr3QrMQ6jDF5iFPyxYoZrkYjUg1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85b37c2b840c72ec35adab75be6f5383708c2a9_2_689x288.png" alt="image" data-base62-sha1="zr3QrMQ6jDF5iFPyxYoZrkYjUg1" width="689" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85b37c2b840c72ec35adab75be6f5383708c2a9_2_689x288.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85b37c2b840c72ec35adab75be6f5383708c2a9_2_1033x432.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f85b37c2b840c72ec35adab75be6f5383708c2a9.png 2x" data-dominant-color="F2F2F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1279×534 52.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b3f7e5cfee51a0c89ad82bbe267c1bd7afcb87f.png" data-download-href="/uploads/short-url/1BvhLGGhSOUNBdyUftUN0DLD8Bh.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b3f7e5cfee51a0c89ad82bbe267c1bd7afcb87f_2_690x391.png" alt="image" data-base62-sha1="1BvhLGGhSOUNBdyUftUN0DLD8Bh" width="690" height="391" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b3f7e5cfee51a0c89ad82bbe267c1bd7afcb87f_2_690x391.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b3f7e5cfee51a0c89ad82bbe267c1bd7afcb87f_2_1035x586.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/b/0b3f7e5cfee51a0c89ad82bbe267c1bd7afcb87f_2_1380x782.png 2x" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1634×927 67.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
You see in my training, I need to specify each segmentation’s label value in the nrrd file. Do you know where can I check this?</p>
<p>Thanks!</p>

---
