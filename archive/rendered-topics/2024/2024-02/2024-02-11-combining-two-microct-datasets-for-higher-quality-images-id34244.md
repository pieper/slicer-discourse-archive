# Combining two microCT Datasets for higher Quality images

**Topic ID**: 34244
**Date**: 2024-02-11
**URL**: https://discourse.slicer.org/t/combining-two-microct-datasets-for-higher-quality-images/34244

---

## Post #1 by @nixxon94 (2024-02-11 04:42 UTC)

<p>Hello everyone,<br>
I am looking to combine two micro-CT scans in such a way that I get a new image stack that might have reduced noise.<br>
I have two scans of the same specimen in the exact same position and aquisition protocols. I am looking to reduce image noise and create a new image stack.<br>
I have tried this approach : <a href="https://github.com/maitek/image_stacking" class="inline-onebox" rel="noopener nofollow ugc">GitHub - maitek/image_stacking: Automatic Image Stacking in OpenCV</a><br>
but I am running into issues with cv2 on my python install for some reason and wondering if there is a more elegant way of doing this in slicer.</p>

---

## Post #2 by @muratmaga (2024-02-11 06:04 UTC)

<p>I don’t think there is such an averageVolumes module, but If they are already aligned, and have the exact same dimensions what you want to do is quite simply taking an average of two numpy arrays using <code>arrayFromVolume</code> method and saving as a new volume.</p>
<p>You can see example of python scripts interacting 3D volumes  as numpy arrays here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-value-of-a-volume-at-specific-voxel-coordinates" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>
<p>But increasing the signal to noise ratio at the acquisition time is more meaningful then trying to rescan. This is usually done by frame averaging (acquiring multiple frames -anywhere from 2 to 20- at the same rotation step, and average them).</p>
<p>If the original projections were not high quality, averaging two reconstructions from two acquisitions are not likely to give you a much better result. I suspect what you are trying to do would be roughly equivalent to running a median filter on one of the volumes.</p>

---

## Post #3 by @nixxon94 (2024-02-11 13:41 UTC)

<p>Thank you very much for your reply! I will look into the array averaging method.</p>

---
