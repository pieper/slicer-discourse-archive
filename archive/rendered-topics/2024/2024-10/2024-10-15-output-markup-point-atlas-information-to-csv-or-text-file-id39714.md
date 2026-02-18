# Output markup point atlas information to csv or text file

**Topic ID**: 39714
**Date**: 2024-10-15
**URL**: https://discourse.slicer.org/t/output-markup-point-atlas-information-to-csv-or-text-file/39714

---

## Post #1 by @rhh (2024-10-15 19:24 UTC)

<p>I have many MR scans with an atlas warped to the scan and about 20 markup points within the brain. I hover the mouse over each markup point, and the individual atlas region corresponding to each markup point is listed in the data probe section. Then, I manually record the atlas location. This is tedious and time consuming. Is it possible to export this information into a .csv file, text file, or log file?</p>

---

## Post #2 by @muratmaga (2024-10-15 19:48 UTC)

<p>This the function of the pointList. You should save your markups, and see their coordinates. You can also use the import/export functionality in Markups module to export the control point coordinates as a csv file.</p>

---

## Post #3 by @rhh (2024-10-15 20:51 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b31650df798dc7734160b1005a443581a621541.jpeg" data-download-href="/uploads/short-url/hzOyvDpuVipeVownleoBmvsNgYx.jpeg?dl=1" title="Capture0.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b31650df798dc7734160b1005a443581a621541_2_690x400.jpeg" alt="Capture0.PNG" data-base62-sha1="hzOyvDpuVipeVownleoBmvsNgYx" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b31650df798dc7734160b1005a443581a621541_2_690x400.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b31650df798dc7734160b1005a443581a621541_2_1035x600.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b31650df798dc7734160b1005a443581a621541_2_1380x800.jpeg 2x" data-dominant-color="8B8B8B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture0.PNG</span><span class="informations">1680×976 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the attached image, I imported the RAS coordinates from a CSV file as markup points and overlaid them on an atlas warped to an MRI scan. When I hover the mouse over point L-8 for example the atlas region is shown as “Caudate Putamen.” Currently, the atlas region must be manually recorded. Is there a way to export to a csv file the atlas region that corresponds to each markup point?</p>

---

## Post #4 by @muratmaga (2024-10-15 21:08 UTC)

<p>I don’t think you can do this automatically from UI, but you can. Manually enter this information in the description field of the control point. Or even rename it to it (i.e., if they are all unique).</p>
<p>You can also possibly write a short python script to do that.</p>

---

## Post #5 by @rhh (2024-10-21 14:26 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="39714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>hink you can do this automatically from UI, but you can. Manually enter this information in the description fiel</p>
</blockquote>
</aside>
<p>I am hoping to avoid manual labor. Can the data probe output be saved to a text file using a Python script?</p>

---

## Post #6 by @muratmaga (2024-10-21 17:24 UTC)

<p>You may want to explore the Script Repository for example of this. You know the coordinate of the landmark, and you can get the coordinates of the segments. So it shouldn’t be difficult to the intersect those to via python script.</p>

---
