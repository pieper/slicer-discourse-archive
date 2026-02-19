---
topic_id: 19377
title: "Orthogonal Reformat"
date: 2021-08-26
url: https://discourse.slicer.org/t/19377
---

# Orthogonal reformat

**Topic ID**: 19377
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/orthogonal-reformat/19377

---

## Post #1 by @Gonzalo_Rojas_Costa (2021-08-26 18:31 UTC)

<p>Hi:</p>
<p>I am reformating an isotropic MRI using the reformat widget. How can I do this reformatting so that the slices are orthogonal to each other?</p>
<p>Sincerely,</p>
<p>Gonzalo Rojas Costa</p>

---

## Post #2 by @lassoan (2021-08-27 01:47 UTC)

<p>The reformat widget is not very powerful and I don’t think it supports suchorthogonality constraint.</p>
<p>Instead, you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">rotate slice views</a> by displaying slice intersections and then:</p>
<ul>
<li>use Ctrl + Alt + Left-click-and-drag using your mouse, or</li>
<li>pinch-and-rotate on touchscreen (on Windows) or on the touchpad (on macOS), or</li>
<li>or define the desired orientation using a transform and then use “Volume reslice driver” module in SlicerIGT extension to show orthogonal slices</li>
</ul>
<p>There are specialized modules for orthogonal reslicing along curves, etc.</p>

---

## Post #3 by @Gonzalo_Rojas_Costa (2021-09-02 18:41 UTC)

<p>Using the first solution, how can I save the images reformated?</p>

---

## Post #4 by @lassoan (2021-09-02 19:51 UTC)

<p>See complete example for accessing image data of reformatted slices in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume">script repository</a>.</p>

---
