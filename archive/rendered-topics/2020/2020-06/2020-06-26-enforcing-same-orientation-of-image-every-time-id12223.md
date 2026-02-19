---
topic_id: 12223
title: "Enforcing Same Orientation Of Image Every Time"
date: 2020-06-26
url: https://discourse.slicer.org/t/12223
---

# Enforcing same orientation of image every time

**Topic ID**: 12223
**Date**: 2020-06-26
**URL**: https://discourse.slicer.org/t/enforcing-same-orientation-of-image-every-time/12223

---

## Post #1 by @rohan_n (2020-06-26 00:05 UTC)

<p>For a Python scripted module, I am loading a series of DICOM images for a DCE MR image into a volume with this syntax:</p>
<pre><code class="lang-python">plugin = slicer.modules.dicomPlugins['DICOMScalarVolumePlugin']()
loadables = plugin.examine([files])
volume = plugin.load(loadables[0])
volumeArray=slicer.util.arrayFromVolume(volume)
</code></pre>
<p>For most MR exams, the variable volume orders the axial slices such that the first slice is closest to the patient’s foot and the last slice is closest to the patient’s head. However, for some exams, volume sorts the slices in the opposite order of this, with first slice closest to head and last slice closest to foot.<br>
In my code, I want to be able to identify when volume has the Head --&gt; Foot orientation so that I can force the image to have the Foot --&gt; Head orientation instead.<br>
How can I do this? Is there any particular DICOM header field that causes Slicer to load images in the Head --&gt; Foot orientation? If not, do loadables or volume contain any information that will be helpful?<br>
So far, I tried looking at the IJKToRAS matrix of volume as well as the Slice Location header field of the DICOMs that were loaded into volume, but neither of those 2 options seem to help me identify when volume has the orientation that I don’t want.</p>
<p>Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @lassoan (2020-06-26 02:25 UTC)

<p>Axis order depends on how the image was acquired, but the exact mapping normally does not matter, as all image processing is be done in physical space anyway.</p>
<p>Head-&gt;Foot direction = Superior-&gt;Inferior direction = -S axis direction. Direction of S axis in IJK coordinate system is defined in the third column of the RASToIJK matrix.</p>

---
