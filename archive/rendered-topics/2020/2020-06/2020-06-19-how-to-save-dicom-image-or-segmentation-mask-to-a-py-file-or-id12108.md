---
topic_id: 12108
title: "How To Save Dicom Image Or Segmentation Mask To A Py File Or"
date: 2020-06-19
url: https://discourse.slicer.org/t/12108
---

# How to save dicom image or segmentation mask to a .py file or .nii file?

**Topic ID**: 12108
**Date**: 2020-06-19
**URL**: https://discourse.slicer.org/t/how-to-save-dicom-image-or-segmentation-mask-to-a-py-file-or-nii-file/12108

---

## Post #1 by @SummerZ2020 (2020-06-19 05:13 UTC)

<p>I used the “segment editor” to get the bone tissue just now. and then I need save the segmentation mask to a .py file. I did not find how to do it in GUI, so I tried to do it with python script.I tried to get the data from node and save the numpy array to .py file. but i found seems there is not data array in the saved test.py file.  here is the python code :<br>
import numpy as np<br>
bone_arr = np.array(‘Segment_1’)<span class="hashtag">#Segment_1</span> is the bone mask<br>
np.save(‘d:\test.npy’,bone_arr)<br>
And then I tried to use “savenode” save the segmentation node to .py file. But I failed, seems the node can not be saved as .py file. And I do not know how to get the data array (segmentation)from the node easily in python script.Or can i save the segmentation mask to the .nii or .py file in GUI?<br>
thank you in advance.</p>

---

## Post #2 by @pieper (2020-06-19 21:15 UTC)

<p>You need to export to a labelmap first, which you can do in the Segmentations module panel shown below.  Then you can do:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; a = array("Segmentation-label")
&gt;&gt;&gt; numpy.save('/tmp/x.py', a)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f706f6fdd556c0e32bf024a393a90e71ff48150.png" alt="image" data-base62-sha1="ksVawGSJqRs7rF7vmrg9sf0ASkw" width="513" height="168"></p>

---

## Post #3 by @SummerZ2020 (2020-06-22 01:33 UTC)

<p>Your answer works. Thanks a lot.</p>

---

## Post #5 by @Deep_Learning (2023-08-31 15:26 UTC)

<p>Bump…<br>
Loading two nii.gz (volume and segmentation(only 1 segment)).</p>
<p>Modifying the segmentation.<br>
Converting to binary labelmap.<br>
Export to file (.nii.gz).</p>
<p>Exported file is much smaller than the volume/orig segmentation.<br>
Seems to be limited by the segmentation bounding box.</p>
<p>Is it possible to export the segmentation with the original dimensions.  (ie compatable with pyradiomics)?</p>

---

## Post #6 by @pieper (2023-08-31 15:33 UTC)

<p>Saving the full dimensions should be the default now, so try with the latest version.</p>

---

## Post #7 by @Deep_Learning (2023-08-31 17:51 UTC)

<p>Ughhh… Thank you…</p>
<p>I cannot duplicate it today.<br>
But I have a bunch of cropped segmentations from yesterday…</p>
<p>Not sure how it happened, but it did…<br>
Was able to reset the geometry one by one…</p>

---
