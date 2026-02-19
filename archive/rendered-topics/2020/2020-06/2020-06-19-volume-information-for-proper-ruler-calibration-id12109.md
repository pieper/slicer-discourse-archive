---
topic_id: 12109
title: "Volume Information For Proper Ruler Calibration"
date: 2020-06-19
url: https://discourse.slicer.org/t/12109
---

# Volume Information for Proper Ruler Calibration

**Topic ID**: 12109
**Date**: 2020-06-19
**URL**: https://discourse.slicer.org/t/volume-information-for-proper-ruler-calibration/12109

---

## Post #1 by @Angel (2020-06-19 06:19 UTC)

<p>Hello,</p>
<p>I have been trying to use Slicer to take measurements using the ruler tool on JPEG images of a chicken embryo heart. The heart is only about 5 mm across and I have been getting measurements around 300 mm across the heart from the ruler. I tried to manipulate the information in the volume module using the image information. However, the image became extremely zoomed in and I am unsure as to why this occurred. Is there any way that I should be manipulating the volume information so that I can get a proper view of the heart along with correct measurements? The image information is is below and I set the image dimensions to 512 mm x 512 mm x 512 mm and the image spacing to be 16 mm.</p>
<p>VolumeSize 512 512 512</p>
<p>VoxelSize 16</p>
<p>VolumePosition 0 0 0</p>
<p>VolumeScale 0.020 0.020 0.020</p>
<p>Field 0 (Position 0 Size 16 Name “data” Format ui Scale 0.588235 Offset -1294.117676)</p>
<p>I would appreciate any help!</p>

---

## Post #2 by @muratmaga (2020-06-19 06:34 UTC)

<p>Perhaps you mean 16 micron, not 16mm for image spacing? 512x512x512 at 16mm image spacing would give you a field of view that is 8m across.</p>
<p>So, instead of entering 16, enter 0.016mm as your image spacing. Better yet, use <code>ImageStacks</code> from SlicerMorph to import your JPG sequence and specify the correct spacing at the time of import, so that you don’t have to fiddle with it later on.</p>
<p>I am not sure what the VolumeScale field mean? Where is this data coming from? OPT?<br>
Also you may want to switch to MarkupsLine tool as oppose ruler, since Ruler tool will soon be deprecated.</p>

---

## Post #3 by @Angel (2020-06-19 16:21 UTC)

<p>Hello,</p>
<p>I really appreciate your help. The image spacing was 16 microns, and I am getting the correct measurements now. The file was opened using Notepad, so that is where the data came from. I will look into using ImageStacks and the MarkupsLine tool for sure.</p>
<p>Thank you!</p>

---
