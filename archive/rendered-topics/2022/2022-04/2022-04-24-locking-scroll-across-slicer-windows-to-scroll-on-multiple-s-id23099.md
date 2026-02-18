# Locking scroll across slicer windows - to scroll on multiple scans concurrently

**Topic ID**: 23099
**Date**: 2022-04-24
**URL**: https://discourse.slicer.org/t/locking-scroll-across-slicer-windows-to-scroll-on-multiple-scans-concurrently/23099

---

## Post #1 by @nuttay (2022-04-24 02:28 UTC)

<p>Hi community.</p>
<p>I have tried to search the forum but couldn’t find an answer for this.</p>
<p>I have several axial (transversal) MRI scans of the same subject. I load the different scans (DICOM/NIFTI) in separate windows but I can’t figure out how to scroll on them concurrently. I.e. all scans in each window move at the same time when I scroll.</p>
<p>This would be a super super useful feature.</p>
<p>If this doesn’t already exists, can somebody point me in the right direction to implement it if possible (I can code in Python, but never played with 3D slicer)</p>
<p>/ AP</p>

---

## Post #2 by @lassoan (2022-04-24 03:07 UTC)

<p>This feature is called <code>view link</code>. You can activate it by clicking on the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">view link button in the slice view controller</a>. Scroll position is synchronized across all views that have the same orientation, so all you need to do is to enable view link and set a common orientation (e.g., axial).</p>

---

## Post #3 by @nuttay (2022-04-24 17:39 UTC)

<p>Thank you for the swift response Andras. It seems this doesn’t work if I have selected “rotate volume to plane” for my scans.</p>
<p>Is this expected behaviour?</p>

---

## Post #4 by @pieper (2022-04-24 17:47 UTC)

<p>Yes, that’s expected if they don’t have the same reformat orientation.</p>
<p>Another option would be to have them all in their ‘volume plane’ orientation and them have one view as a sagittal or coronal and then use the shift-mouse move to scroll through all the other views.</p>

---

## Post #5 by @lassoan (2022-04-24 19:05 UTC)

<p>To set the same orientation for all the views in the same view group, change the view orientation (e.g., choose axial, sagittal, coronal) of any slice view <em>after</em> linking the slice views.</p>

---

## Post #6 by @nuttay (2022-04-26 17:48 UTC)

<p>Wow, that actually works great.</p>
<p>Thanks Andras and Steve.</p>

---
