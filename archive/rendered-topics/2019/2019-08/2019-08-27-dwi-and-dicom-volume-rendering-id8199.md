# DWI and DICOM Volume Rendering

**Topic ID**: 8199
**Date**: 2019-08-27
**URL**: https://discourse.slicer.org/t/dwi-and-dicom-volume-rendering/8199

---

## Post #1 by @eliseberning (2019-08-27 17:31 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>Hello,</p>
<p>I have routinely been loading MRI DICOM images and performing a volume rendering for my data analysis. The DICOM files are a folder of IMA files and I save them as a NRRD file (Node Type: Volume). This past week, I wanted to see a DTI scan and downloaded the DWI Convert extension under Diffusion.</p>
<p>I want to still be able to perform volume rendering on DICOM files, but when I load the exact same DICOM folders (IMA files), they are automatically loaded as DWI volume and not able to be volume rendered. I noticed that when I go to save the files in 3D slicer, the Node Type should be Volume, but is saving as a DiffusionWeightedVolume. Please let me know if there is a way to change the Node type or any other fixes.</p>
<p>Thank you!</p>

---

## Post #2 by @ljod (2019-08-27 18:40 UTC)

<p>Hi! Did you install the full SlicerDMRI extension? It sounds like perhaps you just installed DWI convert, but that would not be expected to work well.</p>
<p>Let us know. Thanks!</p>

---

## Post #3 by @eliseberning (2019-08-27 19:41 UTC)

<p>Hi Lauren,</p>
<p>Yes, I have already installed the SlicerDMRI extension. I also downloaded UKFTractography extension, if that is of any help.</p>

---

## Post #4 by @pieper (2019-08-27 20:04 UTC)

<p>If you load through the DICOM module you can use advanced mode to select whether to load as diffusion or scalar volumes.  Once you have dmri installed it will try to load as diffusion if they file looks like diffusion (has diffusion-related header tags).  Without dmri they would be loaded as scalar volumes by default.</p>

---

## Post #5 by @eliseberning (2019-08-27 20:16 UTC)

<p>Thank you! Choosing the scalar under Advanced worked</p>

---
