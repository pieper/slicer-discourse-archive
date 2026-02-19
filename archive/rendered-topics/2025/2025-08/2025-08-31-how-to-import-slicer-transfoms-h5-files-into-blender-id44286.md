---
topic_id: 44286
title: "How To Import Slicer Transfoms H5 Files Into Blender"
date: 2025-08-31
url: https://discourse.slicer.org/t/44286
---

# How to import slicer transfoms (.h5 files) into Blender?

**Topic ID**: 44286
**Date**: 2025-08-31
**URL**: https://discourse.slicer.org/t/how-to-import-slicer-transfoms-h5-files-into-blender/44286

---

## Post #1 by @apparrilla (2025-08-31 00:05 UTC)

<p>Hi everyone!</p>
<p>I want to extract rotation and position data from an Slicer transform (TR.h5) into Blender.</p>
<p>For now, I did:</p>
<p>1.- Install h5py library in Blender with add-on blender_pip: Python module manager from <a href="https://github.com/amb/blender_pip" class="inline-onebox" rel="noopener nofollow ugc">GitHub - amb/blender_pip: A Blender addon for managing Python modules inside Blender with PIP</a></p>
<p>2.- Extract matrix values:</p>
<blockquote>
<p>with h5py.File(path, “r”) as f:<br>
g = f[group]<br>
params = np.array(g[‘TransformParameters’][:], dtype=float)<br>
fixed  = np.array(g[‘TransformFixedParameters’][:], dtype=float) if ‘TransformFixedParameters’ in g else np.zeros(3)</p>
</blockquote>
<p>I don´t know how to build a valid matrix to make a Blender transform from these data.</p>
<p>Thanks in advance for any help!</p>

---

## Post #2 by @lassoan (2025-08-31 19:34 UTC)

<p>You don’t have to install h5py (HDF5 can be a problematic library due to ABI incompatibilities). It is easier to save the transform as a text file (.tfm format) and then you can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#convert-between-itk-and-slicer-linear-transforms">this code snippet in the script repository</a> to get the transformation matrix.</p>
<p>However, I would recommend not to waste time with saving and loading files. It is easier to start an OpenIGTLink server in Slicer (using OpenIGTLink extension) to expose any number of transforms, then in Blender use <a href="https://pypi.org/project/pyigtl/">pyigtl</a> to get transforms from Slicer in real-time (or send transforms to Slicer). You can also send/receive meshes, images, etc.</p>

---
