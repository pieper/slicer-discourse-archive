# Matching Monai orientation with "arrayFromVolume" output

**Topic ID**: 37810
**Date**: 2024-08-09
**URL**: https://discourse.slicer.org/t/matching-monai-orientation-with-arrayfromvolume-output/37810

---

## Post #1 by @chbricout (2024-08-09 22:11 UTC)

<p>Hi everyone,</p>
<p>I’m developing a simple extension to integrate a motion estimation model into Slicer. I’m using MONAI for most of the training, including data loading. However, I’ve noticed that the volume I get when using <code>slicer.util.arrayFromVolume</code> is rotated compared to the output from my MONAI pipeline.</p>
<p>Has anyone else encountered this issue? If so, how did you resolve it? Specifically, I’m trying to determine how to retrieve the orientation of the array returned by Slicer so I can decide which transform to apply.</p>
<p>Thanks in advance for your help!<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c060a244cc8bfe412893a98f682c8fe196baaf2.jpeg" alt="image" data-base62-sha1="aQxe6MUNgzMRTWcRTiBbHgdStpg" width="553" height="332"></p>

---

## Post #2 by @pieper (2024-08-11 21:32 UTC)

<p>A raw numpy array doesn’t have the <code>ijkToRAS</code> (index to physical) transform. See <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html">https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html</a></p>

---
