# Smoothing algorithm 

**Topic ID**: 31060
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/smoothing-algorithm/31060

---

## Post #1 by @Alessia1 (2023-08-09 11:27 UTC)

<p>I would like to know which smoothing algorithm is used in Total Segmentator. It would be very helpful in my thesis study. Thanks in advance.</p>

---

## Post #2 by @lassoan (2023-08-09 11:28 UTC)

<p>No smoothing algorithm is used in TotalSegmentator module. Do you mean that you are interested in the algorithm that converts binary labelmap representation of the segmentation to closed surface representation?</p>

---

## Post #3 by @Alessia1 (2023-08-09 15:52 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bacce5ac30128041ace51f115f2495463897d5ed.png" alt="Schermata 2023-08-09 alle 17.43.42" data-base62-sha1="qEvNzOUfNJQ6fgu5yVdc1uEpO3P" width="616" height="219"></p>
<p>I’m referring to when, after having shown 3D and then marching cubes, I can modify the smoothing factor and I was wondering by which algorithm it was performed. I attach the photo</p>

---

## Post #4 by @lassoan (2023-08-09 16:37 UTC)

<p>That smoothing algorithm is an ideal low-pass filter implemented in this class:</p>
<p><a href="https://vtk.org/doc/nightly/html/classvtkWindowedSincPolyDataFilter.html#details" class="onebox" target="_blank" rel="noopener">https://vtk.org/doc/nightly/html/classvtkWindowedSincPolyDataFilter.html#details</a></p>

---
