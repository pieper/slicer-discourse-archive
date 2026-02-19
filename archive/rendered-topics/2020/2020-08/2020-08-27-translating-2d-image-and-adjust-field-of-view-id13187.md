---
topic_id: 13187
title: "Translating 2D Image And Adjust Field Of View"
date: 2020-08-27
url: https://discourse.slicer.org/t/13187
---

# Translating 2D image and adjust field of view

**Topic ID**: 13187
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/translating-2d-image-and-adjust-field-of-view/13187

---

## Post #1 by @PaoloZaffino (2020-08-27 09:15 UTC)

<p>Hi all,<br>
I would like to move a model and a 2D slice on the basis of a translation.<br>
The model translates without problem but, for the 2D slice, I have to click on the button “adjust field of view” (the small rectangle) to see it.<br>
Is there a trick to do this in an automatic way? A python line of code could work as well.</p>
<p>Thank you.</p>
<p>Paolo</p>

---

## Post #2 by @lassoan (2020-09-04 03:07 UTC)

<p>Usually we position images by applying a transform and using Volume Reslice Driver (in SlicerIGT extension). Volume Reslice Driver module takes care of keeping the image in the field of the slice view.</p>

---
