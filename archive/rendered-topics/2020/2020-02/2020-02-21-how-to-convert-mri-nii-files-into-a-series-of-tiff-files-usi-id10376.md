# How to Convert MRI nii files into a series of tiff files using 3D Slicer 4.10?

**Topic ID**: 10376
**Date**: 2020-02-21
**URL**: https://discourse.slicer.org/t/how-to-convert-mri-nii-files-into-a-series-of-tiff-files-using-3d-slicer-4-10/10376

---

## Post #1 by @Ali_khattak (2020-02-21 04:13 UTC)

<p>Hello all,<br>
this is my first question in this forum please guide me<br>
I am using ADNI images for my project of Alzheimer disease detection and classification using CNN but I have 3D images which need high performance GPU and Ultimate performance system so to avoid it I want to convert my each MRI <code>nii</code> file into 2D slice (tiff or PNG) files How I will convert through 3D slicer please help me in this regard.<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2020-02-25 00:11 UTC)

<p>I would recommend to convert from scientific (nifti, nrrd, …) to consumer file formats (png, tiff, …) as a temporary workaround (if you want to quickly try a network and don’t want to spend any time with formatting the input data).</p>
<p>To simply write out the native voxel values, you can do this:</p>
<pre><code class="lang-python">pip_install("imageio")
import imageio

voxelArray = slicer.util.arrayFromVolume(myVolumeNode)
for i in range(len(outputLabelmapVolumeArray)):
    imageio.imwrite(f'{outputDir}/image_{i:03}.tiff', outputLabelmapVolumeArray[i])
</code></pre>
<p>However, probably you would want to normalize the image size, resolution, maybe even intensity values.</p>

---
