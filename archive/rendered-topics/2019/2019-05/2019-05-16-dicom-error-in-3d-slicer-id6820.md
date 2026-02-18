# DICOM error in 3D slicer

**Topic ID**: 6820
**Date**: 2019-05-16
**URL**: https://discourse.slicer.org/t/dicom-error-in-3d-slicer/6820

---

## Post #1 by @bibi (2019-05-16 15:01 UTC)

<p>Operating system:<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
Actual behavior:<br>
hi, why 3D Slicer don’t open my DICOM data? but it can open them when I chose “add data”.</p>

---

## Post #2 by @lassoan (2019-05-17 03:27 UTC)

<p>What kind of data set it is?<br>
Could you try the latest stable version of Slicer?</p>

---

## Post #3 by @bibi (2019-05-17 06:17 UTC)

<p>Cardiac data set, and my images are acquired with MRI modality.</p>

---

## Post #4 by @lassoan (2019-05-17 12:25 UTC)

<p>Is it a time sequence of slices or volumes or just a plain 3D volume? Regular 3D volumes should be possible to load without issues. Time sequences can be stored in many different ways, so loading of those may require some tuning.</p>
<p>Do you see any errors or warnings in the application log? (<code>X</code> icon in the lower-right corner of the application window)</p>

---

## Post #5 by @bibi (2019-05-17 13:03 UTC)

<p>thanks for your attention,</p>
<p>so, no difference between use of 4.8.1 version or 4.11.0 version  both of them can’t open DICOM data for me. but with another systems open them clearly!</p>
<p>there are many sequences from one patient. i can load DICOM data, after some steps for loading data, when i press load key, dont show any thing. please HELP me</p>

---

## Post #6 by @lassoan (2019-05-17 13:10 UTC)

<p>Is it a time sequence of slices or volumes or just a plain 3D volume?</p>
<p>Do you see any errors or warnings in the application log? (you can see the log if you click <code>X</code>  icon in the lower-right corner of the application window)</p>
<p>Can you share an anonymized data set (or a phantom data set acquired with the same acquisition protocol)?</p>

---

## Post #7 by @lassoan (2019-05-19 13:22 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/loading-of-ge-kretz-ultrasound-volumes-vol-file/808/63">Loading of GE/Kretz ultrasound volumes (.vol file)</a></p>

---

## Post #8 by @bibi (2019-05-18 20:05 UTC)

<p>Thanks, i try to solve the problem, and i do it, on of my friend is very expert about 3D slicer…every thing is OK.</p>

---

## Post #9 by @lassoan (2019-05-19 13:23 UTC)

<p>Could you share with us what was the solution so that we can learn from it (what we can improve in the future)? Thank you.</p>

---
