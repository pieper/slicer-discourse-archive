# Grey Scale Color Inversion not Saving/Exporting in DICOM

**Topic ID**: 26759
**Date**: 2022-12-16
**URL**: https://discourse.slicer.org/t/grey-scale-color-inversion-not-saving-exporting-in-dicom/26759

---

## Post #1 by @Bethrg (2022-12-16 01:31 UTC)

<p>Hello,</p>
<p>I have an MRI DICOM image stack for which I need to invert the colors (to make it appear like a CT), save the change, and then export that “negative”, also as a DICOM to use in another treatment planning software.</p>
<p>I am able to invert the colors by using the Volumes&gt;InvertedGrey. My issue is getting the change to save/export correctly.</p>
<p>I have tried:</p>
<ol>
<li>Directly exporting with the change active using DICOM Database&gt;Export to DICOM&gt;Export Series</li>
<li>Saving the scene with default settings - reopening, then exporting as described above</li>
<li>Saving the scene - reopening, exporting using “Create a DICOM series”</li>
<li>Saving the inverted file as a .mrb (which preserves the color inversion upon reopening) and then also exporting both ways described in 1 and 2.</li>
</ol>
<p>In all cases, when I go to open the newly exported file, it is the exact same as my initial DICOM.</p>
<p>Any assistance would be greatly appreciated.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2022-12-16 01:44 UTC)

<p>This is not unexpected, since DICOM images are “lossy” with respect to what you see in Slicer in the sense that we don’t export the lookup table.  You could look into constructing a custom DICOM header and might be able to achieve what you want, but an easier way might be modify the data directly.  E.g. like <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume">this example with a numpy array</a> except with a line like <code>voxelArray[:] = -1 * voxelArray</code> and then fix the window/level and export to DICOM.</p>

---
