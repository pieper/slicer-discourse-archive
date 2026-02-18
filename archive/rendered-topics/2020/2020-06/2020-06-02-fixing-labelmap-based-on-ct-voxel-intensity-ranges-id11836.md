# Fixing labelmap based on CT voxel intensity ranges

**Topic ID**: 11836
**Date**: 2020-06-02
**URL**: https://discourse.slicer.org/t/fixing-labelmap-based-on-ct-voxel-intensity-ranges/11836

---

## Post #1 by @Vincent_C (2020-06-02 19:20 UTC)

<p>Hi all,</p>
<p>I am wondering if there is a function to fix labels that are “out-of-range” based on CT voxel intensity ranges or HU ranges. For example, for all label values equal to 1 below -29 and above 150 intensity, I want to change it to “0” as a fix for over-segmentation. I was exploring the Simple Filters modules but could not find anything to achieve this. Is there a function in Slicer specifically do this for labelmap volumes? Or must this be performed on segmentation nodes in Segment Editor and converted to a labelmap?</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2020-06-02 21:19 UTC)

<p>You can do pretty much anything by accessing the volume as a numpy array.  Maybe you want something like this:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Accessing_Volume_data_as_numpy_array</a></p>
<pre><code class="lang-auto">a[:] = numpy.clip(a, -29, 150)
</code></pre>

---
