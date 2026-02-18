# Saving resliced images from an ultrasound volume

**Topic ID**: 21900
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/saving-resliced-images-from-an-ultrasound-volume/21900

---

## Post #1 by @askaderd (2022-02-10 21:29 UTC)

<p>Hi there,</p>
<p>I’d like to reslice an ultrasound volume at coordinates defined by given transforms (this is so that I can feed in optical tracking data to reslice the ultrasound volume). I initially tried the Volume Reslice Driver within the IGT module and that worked to reslice the volume but there doesn’t seem to be any way of saving the resliced images. Is there something I’m missing?</p>
<p>Any help would be appreciated!</p>

---

## Post #2 by @lassoan (2022-02-12 17:12 UTC)

<p>You can write a few-line Python script that iterates through the sequence and for each timepoint you save the output to file. The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#browse-a-sequence-and-access-currently-displayed-nodes">script repository</a> probably contains examples for everything that you need, but if you cannot find out how to do something then you can ask here.</p>

---
