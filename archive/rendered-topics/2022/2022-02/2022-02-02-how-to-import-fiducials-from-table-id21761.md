---
topic_id: 21761
title: "How To Import Fiducials From Table"
date: 2022-02-02
url: https://discourse.slicer.org/t/21761
---

# How to import fiducials from table

**Topic ID**: 21761
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/how-to-import-fiducials-from-table/21761

---

## Post #1 by @muratmaga (2022-02-02 18:30 UTC)

<p>I have csv file that is in LPS coordinates. I loaded the table to Slicer, when I use the import functionality of the Markups tool to save them in a PointList object, the coordinates all show as 0,0,0. There is an error message that read.</p>
<p><code>GetItemByDataNode: Invalid data node to find</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f7186040c007b1b53fef6bf9941317f69f18487.jpeg" data-download-href="/uploads/short-url/bkMWtqSDS88gBrqLCD3WgYSsV6L.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f7186040c007b1b53fef6bf9941317f69f18487_2_690x349.jpeg" alt="image" data-base62-sha1="bkMWtqSDS88gBrqLCD3WgYSsV6L" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f7186040c007b1b53fef6bf9941317f69f18487_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f7186040c007b1b53fef6bf9941317f69f18487_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f7186040c007b1b53fef6bf9941317f69f18487_2_1380x698.jpeg 2x" data-dominant-color="BCBCBC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×972 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What am I doing wrong?</p>

---

## Post #2 by @muratmaga (2022-02-02 18:35 UTC)

<p>OK. Changing the row labels to lower case (from LPS to lps) made it work. I think this asking too much from the user. Can the code automatically correct this?<br>
<a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---
