---
topic_id: 1176
title: "Stacking Ct Images"
date: 2017-10-05
url: https://discourse.slicer.org/t/1176
---

# Stacking CT images

**Topic ID**: 1176
**Date**: 2017-10-05
**URL**: https://discourse.slicer.org/t/stacking-ct-images/1176

---

## Post #1 by @jbassein (2017-10-05 01:35 UTC)

<p>Operating system: Windows 7 enterprise<br>
Slicer version: 4.6<br>
Expected behavior: Stacking images<br>
Actual behavior: When I load a series of CT images into slicer, they do not seem to automatically stack into one scrollable image that I can move up and down through. How do I accomplish this?</p>

---

## Post #2 by @pieper (2017-10-05 12:31 UTC)

<p>Start by going through the tutorial with the sample data:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_3D_Visualization_of_DICOM_images_for_Radiology_Applications" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_3D_Visualization_of_DICOM_images_for_Radiology_Applications</a></p>
<p>If the same steps don’t work for your own data, try the suggestions in the FAQ:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>
<p>Then let us know if there are still outstanding issues.</p>
<p>-Steve</p>

---

## Post #3 by @jbassein (2017-10-05 20:56 UTC)

<p>Hi Steve!!!</p>
<p>This is great. Thank you so much for recommending this tutorial. It really<br>
helped load my images properly and teach me how to do basic 3D rendering. I<br>
am trying to go through the lung CT tutorial, however there seems to be<br>
some data missing from the 3DVisualizationDICOM_part2<br>
<a href="https://www.slicer.org/w/images/0/0b/3DVisualization_DICOM_images_part2.zip" rel="nofollow noopener">https://www.slicer.org/w/images/0/0b/3DVisualization_DICOM_images_part2.zip</a>.<br>
Whenever I try to load the dataset4_chest I do not see any patient samples<br>
or visual images. I looked through the file and it seems that most of the<br>
corresponding samples images have disappeared. Could you please check to<br>
see if the link is broken or maybe there is something wrong with the linked<br>
to the file?</p>
<p>Thanks so much!!!</p>
<p>Jed</p>

---

## Post #4 by @pieper (2017-10-05 21:19 UTC)

<p>Hi Jed - not sure what the issue is - when I load the LungSegments_Scene.mrb with 4.6 and with a recent nightly build everything looks as expected.</p>
<p>Are you sure you are dragging the .mrb file into Slicer and not the containing directory?  (If you drag the directory it tries to open as DICOM by default unless you switch to “Any Data”).</p>
<p>HTH,<br>
Steve</p>

---

## Post #5 by @jbassein (2017-10-05 21:32 UTC)

<p>Hi Steve!!!</p>
<p>Yes that was exactly the problem. I was dragging the directory in rather<br>
than the file. I dragged the file in and it seems to be working fine.<br>
Thanks so much for your help and support!</p>
<p>Jed</p>

---
