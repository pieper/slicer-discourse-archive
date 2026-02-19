---
topic_id: 24233
title: "Problem Importing Jpeg Series"
date: 2022-07-07
url: https://discourse.slicer.org/t/24233
---

# Problem importing JPEG series 

**Topic ID**: 24233
**Date**: 2022-07-07
**URL**: https://discourse.slicer.org/t/problem-importing-jpeg-series/24233

---

## Post #1 by @marco1 (2022-07-07 19:01 UTC)

<p>Hi,</p>
<p>I’m currently importing JPEG series of brain MRIs for a volumetric tumor analysis. I’m having no problems importing axial sequences, but importing sagittal or coronal sequences always ends up with the sequences in the wrong order (IE, axial will be associated with coronal, sagittal with axial…etc) making it impossible to get all 3 isovolumetric sequences. Changing the associated sequences in reformat module or trying to change the views directly in the boxes does not fix things.</p>
<p>Thank you people!</p>

---

## Post #2 by @pieper (2022-07-07 19:05 UTC)

<p>First off, JPEG is not a good format for storing brain MRIs for many reasons (it’s only 8 bit not the typical 10-12 of MRI, compression is lossy, there’s no geometry information…) so the best would be if you could get the original dicom data.</p>
<p>If you must work with the jpegs, then you should convert them to scalar (with the Vector to Scalar Volume module).  Then you can apply a Transform to put them in the correct orientation (if you can - beware of left-right flips).  Then harden the transform and save as something like NRRD format.</p>

---

## Post #3 by @marco1 (2022-07-07 19:15 UTC)

<p>Yeah unfortunately I only have access to the JPEG files and not the original DICOM.</p>
<p>How exactly would I need to apply the transform?<br>
Thank you for your answer!</p>

---

## Post #4 by @pieper (2022-07-07 19:18 UTC)

<p>You’ll just need to apply a transform to the volume and use the harden transform feature.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html</a></p>

---

## Post #5 by @lassoan (2022-07-07 20:07 UTC)

<p>You can also use <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks">ImageStacks module</a> in SlicerMorph extension to import a JPEG stack. You can click the <code>Reverse</code> checkbox to flip the Z axis.</p>
<p>However, I fully agree with <a class="mention" href="/u/pieper">@pieper</a> in that you should get the original MRIs. Your study protocol should allow you to access to the actual images (potentially after anonymization, defacing, etc.). Analysis results from some JPEGs (that are essentially just screenshots of the PACS viewer, acquired with current viewing settings) might not represent what you can get from the actual data.</p>

---

## Post #6 by @marco1 (2022-07-07 22:04 UTC)

<p>Thanks for the answers.</p>
<p>I agree about the DICOM files, however the PACS I have access to only allows me to export as JPEG files. I’ll ask my supervisor about a DICOM export but for the meantime JPEG remains the only option… unless there’s a secret DICOM export feature on my PACS I don’t know about.</p>

---

## Post #7 by @pieper (2022-07-07 22:13 UTC)

<p>It would be very unusual for a PACS not to have a dicom export option, for all the reasons noted above.  But there may be policy reasons why your access is restricted, so it’s good to ask and see if you can get the dicom data as it will be better for whatever work you have planned.</p>

---
