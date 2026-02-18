# 3D Slicer MHD Color Visualization

**Topic ID**: 13419
**Date**: 2020-09-10
**URL**: https://discourse.slicer.org/t/3d-slicer-mhd-color-visualization/13419

---

## Post #1 by @Luis_Carlos_Carneiro (2020-09-10 12:04 UTC)

<p>Dear All,</p>
<p>I am trying to visualize the MHD file with the following header in 3D Slicer without success:</p>
<p>ObjectType = Image<br>
NDims = 3<br>
BinaryData = True<br>
BinaryDataByteOrderMSB = False<br>
CompressedData = False<br>
TransformMatrix = 1 0 0 0 1 0 0 0 1<br>
Offset = 0 0 0<br>
CenterOfRotation = 0 0 0<br>
AnatomicalOrientation = RAI<br>
ElementSpacing = 0.29999999999999999 0.29999999999999999 0.29999999999999999<br>
DimSize = 768 768 576<br>
ElementType = MET_UCHAR_ARRAY<br>
ElementNumberOfChannels = 3<br>
ElementDataFile = seg_final.raw</p>
<p>I can visualize in ITK-SNAP.</p>
<p>Must I do something?</p>
<p>Thanks,</p>
<p>Luis Gonçalves</p>

---

## Post #2 by @lassoan (2020-09-10 12:21 UTC)

<p>You can only load scalar images (<code>ElementNumberOfChannels = 1</code>) from mhd files.</p>
<p>If you want to load vector images or displacement fields then use nrrd file format (nhdr header file) instead. You can create a nhdr header for your data using <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess extension</a>.</p>
<p>To load segmentation data, do not store it as color image! Segmentations are scalar images and you assign the color to each scalar value using a color map (or by importing it into a segmentation).</p>
<p>To make a labelmap volume file loaded as labelmap volume by default, add <code>-label</code> suffix to the filename (<code>example-label.nrrd</code>); to make it loaded as segmentation by default, use <code>.seg.nrrd</code> extension (<code>example.seg.nrrd</code>). Otherwise you need to would need to click on “Show options” and “Labelmap” checkboxes in Add Data window.</p>

---
