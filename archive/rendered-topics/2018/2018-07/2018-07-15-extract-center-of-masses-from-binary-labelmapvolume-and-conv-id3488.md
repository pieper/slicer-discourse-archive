---
topic_id: 3488
title: "Extract Center Of Masses From Binary Labelmapvolume And Conv"
date: 2018-07-15
url: https://discourse.slicer.org/t/3488
---

# Extract Center of masses from binary LabelMapVolume and convert to Fiducials?

**Topic ID**: 3488
**Date**: 2018-07-15
**URL**: https://discourse.slicer.org/t/extract-center-of-masses-from-binary-labelmapvolume-and-convert-to-fiducials/3488

---

## Post #1 by @shahrokh (2018-07-15 13:32 UTC)

<p>Hi Slicer developers</p>
<p>I have a binary labelMapVolume (512x512x173). It contains a large number of regions almost circular  (approximately each area of about 20 pixels) at its axial sections.</p>
<p>I have two questions:<br>
1- How can I determine the center of masses these regions as a pixel, separately?<br>
2- How can I convert these center of masses <strong>to</strong> fiducials?</p>
<p>Please guide me,<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2018-07-15 14:27 UTC)

<p>You can use Islands effect to split the segment so that each island is put in a separate segment. You can then use numpy or VTK or SimpleITK to compute center of gravity.</p>
<p>You may also find SimpleITK or vtkITK label filters to get island properties directly from the original (non-split) labelmap image.</p>

---

## Post #3 by @pieper (2018-07-15 15:05 UTC)

<p><a class="mention" href="/u/shahrokh">@shahrokh</a> as you find a good working solutions for your questions please post them so others can benefit.</p>

---

## Post #4 by @apparrilla (2023-09-15 19:15 UTC)

<p>Hi everyone!<br>
I have same problem as <a class="mention" href="/u/shahrokh">@shahrokh</a> and I´ve explore <a class="mention" href="/u/lassoan">@lassoan</a> solutions.</p>
<p>For center of mass by numpy, I´ve found something like:</p>
<pre><code class="lang-auto">def center_of_mass(array: np.ndarray):
    total = array.sum()
    # alternatively with np.arange as well
    x_coord = (array.sum(axis=1) @ range(array.shape[0])) / total
    y_coord = (array.sum(axis=0) @ range(array.shape[1])) / total
    return x_coord, y_coord
</code></pre>
<p>What I really have trouble with is the way to access labels inside labelmap…</p>
<pre><code class="lang-auto">labelmapNode = slicer.util.loadLabelVolume(mask_file_path)
labelmapArray = slicer.util.arrayFromVolume(labelmapNode)
secondLabelVoxels = labelmapArray[labelmapArray==1]
print(center_of_mass(secondLabelVoxels ))
</code></pre>
<p>Print result:</p>
<pre><code class="lang-auto">(nan, nan)
</code></pre>
<p>I´ll appreciate some help with this…<br>
Thanks in advance!</p>

---

## Post #5 by @lassoan (2023-09-16 13:04 UTC)

<p>Your probably get NaN site to division by zero. Make sure your never attempt to divide by <code>total</code> if the value is zero.</p>
<p>Similar questions have come up several times since this topic was created 5 years ago. Please search a bit in this forum (the built-in search in discourse is not that great, so you may have better luck with Google or Bing Chat). If you ask here or at other related topics then make sure you describe what you want to achieve, because center of a segment can be interpreted in many different ways (e.g., do you need a center point that is inside the segment?).</p>

---
