# Creating sub-segments

**Topic ID**: 18420
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/creating-sub-segments/18420

---

## Post #1 by @trash_imp (2021-06-30 08:08 UTC)

<p>While implementing <code>Grow from seeds</code>,</p>
<ul>
<li>
<p>In Slicer3D, we create new Segments when we want to split the dicom, and then we click on implement.</p>
</li>
<li>
<p>I want to modify segments so that the children of a segment(sub-segments) are the split parts of the dicom, and we can click on a child to display it in 3D. When I hide a segment all its split masks also hide and when new segment is created, it will have no children initially.</p>
</li>
</ul>

---

## Post #2 by @lassoan (2021-07-02 03:36 UTC)

<p>Segmentations contain a list of segments (not a hierarchy). However, once you created all your segments, you can export them to models and you can organize models into a hierarchy by creating folders and drag-and-dropping models into the folders in the Data module.</p>

---
