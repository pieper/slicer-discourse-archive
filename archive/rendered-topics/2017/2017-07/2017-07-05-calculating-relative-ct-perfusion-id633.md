# Calculating Relative CT Perfusion

**Topic ID**: 633
**Date**: 2017-07-05
**URL**: https://discourse.slicer.org/t/calculating-relative-ct-perfusion/633

---

## Post #1 by @hph10128 (2017-07-05 20:00 UTC)

<p>Hi!</p>
<p>I was wondering if there were any modules or extensions that could do a relative perfusion CT calculation. I have an absolute perfusion CBF and CBV and want to calculate relative CBF and CBVs. If not, if any one has any suggestions on how to tackle this in python, it would be greatly appreciated.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-07-05 20:41 UTC)

<p>You can perform computation on voxels by numpy array operations - see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume</a>.</p>
<p>You may also use SimpleFilters module for basic arithmetic operations on volumes (add, subtract, multiply, divide, invert, min, max, …).</p>

---

## Post #3 by @habril (2018-09-18 10:35 UTC)

<p>Hi! Is there a slicer module to calculate perfusion maps on CT images?</p>

---

## Post #4 by @lassoan (2018-09-18 19:15 UTC)

<p>There are some related modules that you might find usable:</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer">https://www.slicer.org/wiki/Documentation/Nightly/Modules/MultiVolumeExplorer</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DSC_MRI_Analysis">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DSC_MRI_Analysis</a></li>
<li><a href="https://github.com/millerjv/PkModeling">https://github.com/millerjv/PkModeling</a></li>
</ul>

---
