# Resample image volume along user-defined plane

**Topic ID**: 37146
**Date**: 2024-07-02
**URL**: https://discourse.slicer.org/t/resample-image-volume-along-user-defined-plane/37146

---

## Post #1 by @1000_tiny_slices (2024-07-02 11:37 UTC)

<p>I would like to transform and resample my CT volume so that a user-defined plane becomes one of the orthogonal slices. I used to do this in AVIZO by defining points, best-fitting a plane to those points and then resampling the image volume with the plane as a reference object. How can I go about doing something like this efficiently in 3D Slicer?</p>

---

## Post #2 by @pieper (2024-07-05 16:32 UTC)

<p>See discussion here: <a href="https://discourse.slicer.org/t/non-orthogonal-reslice/37213/2" class="inline-onebox">Non Orthogonal reslice - #2 by pieper</a></p>

---

## Post #3 by @chir.set (2024-07-05 17:08 UTC)

<p>Try also ‘Curved planar reformat’ module with a curve using only 2 control points as a line. Use a much greater ‘Slice size’ parameter than the default to better understand the result. You’ll have a cropped volume along the line with the slice views reformatted along the line as an axis. I don’t know at all what would be the result with AVIZO, just worth a try.</p>

---

## Post #4 by @lassoan (2024-07-06 01:21 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-slice-from-volume">this code snippet</a> to set up a markup ROI node from plane node and use this ROI to resample the volume. The code snippet extracts a single slice but it can be easily modified to extract more slices by modifying the extents (last two numbers in <code>imageData.SetExtent(...)</code>).</p>

---

## Post #5 by @1000_tiny_slices (2024-07-10 17:46 UTC)

<p>Thanks so much, this community is awesome! This is my preferred solution for me because it’s most similar to my previous workflow (I didn’t have to manually drag and rotate). However, it requires the Python console.  I don’t code Python, so I was thankful for the instructions about modifying code in the repository.</p>
<p>For anyone wanting more info about this solution, I defined an anatomical reference plane that sits about in the middle of the head (dividing it into top and  bottom halves).</p>
<p>The set extent command is in reference to that plane. For the coordinate system of my scan, the second to last number in that line of code defines the number of slices that will be resampled below my reference plane and the last number defines the number of slices that will be resampled above my reference.</p>

---

## Post #6 by @1000_tiny_slices (2024-07-10 17:52 UTC)

<p>Thanks so much, this community is awesome!</p>
<p>This solution has the advantage of being more user-friendly because all of the user interface options. I don’t prefer it because the plane I am trying to display  can be difficult to define precisely by dragging and rotating.</p>
<p>This is also a great solution, just depends on how precise you need your reference plane to be and how different the location/orientation of the begining and target ending volumes.</p>

---

## Post #7 by @1000_tiny_slices (2024-07-16 13:39 UTC)

<p>Could this block of code be modified to set the fill value for the resampled volume?</p>

---

## Post #8 by @lassoan (2024-07-16 18:19 UTC)

<p>Yes, you can specify the fill value in the <code>parameters</code> variable. See how to get the list of parameter names <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#get-list-of-parameter-names">here</a>.</p>

---
