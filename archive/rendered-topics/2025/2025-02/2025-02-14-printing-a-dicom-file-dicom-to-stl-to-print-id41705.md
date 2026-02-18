# printing a dicom file, dicom to ???STL to print

**Topic ID**: 41705
**Date**: 2025-02-14
**URL**: https://discourse.slicer.org/t/printing-a-dicom-file-dicom-to-stl-to-print/41705

---

## Post #1 by @Wannab3ddentist (2025-02-14 16:40 UTC)

<p>Operating system:winn pro11<br>
Slicer version:5.8.0<br>
Expected behavior:<br>
Actual behavior:<br>
can i find step by step instructions for converting dicom to stl file for printing?</p>

---

## Post #2 by @Arash1 (2025-02-17 16:39 UTC)

<p>Hi<br>
Assuming that you have a segment that is what you want to 3D print, go to the <em>Segment Editor</em>, click on the green arrow and it will direct you to the <em>Segmentations</em> module. You could do this by directly going to the module as well. Now in the <em>Segmentations</em> module, <em>Export to files</em>, you can choose between STL or OBJ, and other formats. You will have your file exported to the <em>Destination folder</em>.<br>
One side note is now that the file you have might not be directly “printable”. One option is to use Meshmixer to “inspect” your model, and it will “repair” your model, but as much as this software is helpful, it can change your model depending on your segmentation and processing. Depending on what your model is, you can directly take it to your 3D printing slicing software, and if there are errors, you can repair it there.<br>
Please let me know if you have other questions.<br>
Best,<br>
Arash</p>

---

## Post #3 by @Arash1 (2025-02-17 16:39 UTC)

<p>You might want to take a look at this as well.<br>
<a href="https://slicer.readthedocs.io/en/5.6/user_guide/modules/segmentations.html" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation</a></p>

---

## Post #4 by @Wannab3ddentist (2025-02-17 17:55 UTC)

<p>Thanks for helping. I finally figured it out with trial and error last week, but I’m getting an “Error opening file” when I try to open it in mesh mixer. Tried to re-upload , segment and export again only to get the same result.</p>
<p>I am a dentist and am trying to print the mandible of a patient for implant surgery. I found a dental website that I have not tried yet. I think it will allow me to do the same thing as the 3D slicer.<br>
Thanks again,<br>
Owen</p>

---

## Post #5 by @Arash1 (2025-02-17 18:07 UTC)

<p>My apologies for the delay. Can you open it with the slicing software? Prusa as an example. 3D Slicer should be able to cover it all.<br>
Another option is to use the (<a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerMONAIAuto3DSeg: Extension for 3D Slicer for running MONAI Auto3DSeg models</a>). The Whole Head Segmentation should be able to do it.<br>
The other option is <a href="https://github.com/gaudot/SlicerDentalSegmentator" rel="noopener nofollow ugc">GitHub - gaudot/SlicerDentalSegmentator: 3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes.</a></p>
<p>Please let me know if I can be of any help.<br>
Best,<br>
Arash</p>

---
