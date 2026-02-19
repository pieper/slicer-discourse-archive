---
topic_id: 3279
title: "Defining Roi Dimensions And Position"
date: 2018-06-25
url: https://discourse.slicer.org/t/3279
---

# Defining ROI dimensions and position

**Topic ID**: 3279
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/defining-roi-dimensions-and-position/3279

---

## Post #1 by @stevenagl12 (2018-06-25 16:13 UTC)

<p>Hi, I was wondering if there is a way to define the dimensions and position of an ROI exactly either programmatically or through a given module? I am trying to do it more efficiently than dropping the ROI points and manually manipulating them.</p>

---

## Post #2 by @lassoan (2018-06-25 16:30 UTC)

<p>You can edit ROI position and size using Annotations module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea29daee9bfb40c3016c7752b551018d5d1d95b.png" data-download-href="/uploads/short-url/rcr7AHHoRiN4zXFRjqATCota2jV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bea29daee9bfb40c3016c7752b551018d5d1d95b_2_594x500.png" alt="image" data-base62-sha1="rcr7AHHoRiN4zXFRjqATCota2jV" width="594" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bea29daee9bfb40c3016c7752b551018d5d1d95b_2_594x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bea29daee9bfb40c3016c7752b551018d5d1d95b_2_891x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea29daee9bfb40c3016c7752b551018d5d1d95b.png 2x" data-dominant-color="CFCFCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1152×969 77.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can set ROI position and size by modifying the corresponding vtkMRMLAnnotationROINode node.</p>

---
