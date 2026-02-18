# Trying to re-create model smoothing in python code.

**Topic ID**: 30102
**Date**: 2023-06-18
**URL**: https://discourse.slicer.org/t/trying-to-re-create-model-smoothing-in-python-code/30102

---

## Post #1 by @Adam_Mcarthur (2023-06-18 12:35 UTC)

<p>Hey folks, right now I am converting .nii files into .ply files, and then trying to smooth them. This doesn’t seem to work.</p>
<p>Essentially, I want to do the same smoothing 3D Slicer does on segmentation when you turn them into a 3D Model. How would I re-create this in python code? Do I need to do a different conversion?</p>
<p>Even if I could get some information on what 3D Slicer is doing behind the scenes here that would be great.</p>
<p>What I have: <a href="https://drive.google.com/uc?id=1cm0FsXB5ffoLB01HduRyDXK8UB7vkkFX" rel="noopener nofollow ugc">https://drive.google.com/uc?id=1cm0FsXB5ffoLB01HduRyDXK8UB7vkkFX</a></p>
<p>What I want: <a href="https://drive.google.com/uc?id=1F7e5A8L3UK4GOB8NERdwShcow-ghOVkz" rel="noopener nofollow ugc">https://drive.google.com/uc?id=1F7e5A8L3UK4GOB8NERdwShcow-ghOVkz</a><br>
(Same thing but smoothed: ignore colours)</p>
<p>Thanks in advance :))</p>

---

## Post #2 by @lassoan (2023-06-18 12:37 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a> shows you examples of how to load an image file as segmentation and export smoothed closed surface representation to model node or files.</p>

---

## Post #3 by @Adam_Mcarthur (2023-06-19 21:06 UTC)

<p>Thanks, but I don’t think this is entirely what I want to do - I more want to replicate 3D Slicers behaviour using native python models.</p>
<p>I have tried things like this with no success. Any suggestions on what the actual step I am missing is?</p>
<pre><code class="lang-py">.....
import nibabel as nib
import numpy as np
from skimage import measure
from plyfile import PlyData, PlyElement

from scipy.ndimage import gaussian_filter


nii_file = "./test/test.nii"
model_file = "./test/final.ply"

nifti_file = nib.load(nii_file)
np_array = nifti_file.get_fdata()  # type: ignore [attr-defined]

# Smoothing
smoothed = gaussian_filter(np_array, sigma=1)

# Apply zoom to increase the resolution of the 3D data
verts, faces, _, values = measure.marching_cubes(np_array, 0)
...
</code></pre>

---

## Post #4 by @Eva91 (2025-02-28 15:03 UTC)

<p>I am actually in need of the same thing. Have you come up with a good solution? In that case, would you mind sharing ?</p>

---
