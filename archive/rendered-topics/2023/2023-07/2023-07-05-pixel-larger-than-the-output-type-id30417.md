# Pixel larger than the output type

**Topic ID**: 30417
**Date**: 2023-07-05
**URL**: https://discourse.slicer.org/t/pixel-larger-than-the-output-type/30417

---

## Post #1 by @Sakuranezumi (2023-07-05 19:08 UTC)

<p>Hi manager, the Dicom images downloaded from the pacs always shows the “pixel larger than the output tpye” and with the information “could not load xxx as Scalar volume”.The dicom reader was setted to be GDCM approach.I have already checked the document which told me to go to the module “cast scalar volume” and choose the float, it also doesn’t work. Is there any way to raise the pixel output in the slicer? Thx!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a696c828712832cdcd7faec933d6cf9bea24abad.png" data-download-href="/uploads/short-url/nLIj8QWjYdhjnTgGUDqQT2H3HJ3.png?dl=1" title="图片2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a696c828712832cdcd7faec933d6cf9bea24abad_2_690x42.png" alt="图片2" data-base62-sha1="nLIj8QWjYdhjnTgGUDqQT2H3HJ3" width="690" height="42" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a696c828712832cdcd7faec933d6cf9bea24abad_2_690x42.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a696c828712832cdcd7faec933d6cf9bea24abad_2_1035x63.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a696c828712832cdcd7faec933d6cf9bea24abad.png 2x" data-dominant-color="FEEDED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图片2</span><span class="informations">1280×78 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-07-05 20:28 UTC)

<p>If you can share example data (not patient data) that replicates the issue someone can probably look.  But my guess is that this is some kind of non-standard dicom data so you may not have much luck.</p>

---

## Post #3 by @Sakuranezumi (2023-07-06 10:02 UTC)

<p>Thank you for your reply <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_three_hearts.png?v=12" title=":smiling_face_with_three_hearts:" class="emoji" alt=":smiling_face_with_three_hearts:" loading="lazy" width="20" height="20"> but what weird is, another set of the Images can be imported and 3d slicer worked well , which also comes from the same PACS system. <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"> . The engineer in our hospital said that the images are 100% in the form of dicom， truely confused now</p>

---

## Post #4 by @pieper (2023-07-06 13:36 UTC)

<p>Probably it’s not dependent on the PACS itself but the modality that created the data.  If you can’t share a de-identified example it’s hard for us to say.  There are lots of lower-level dicom tools you could use to investigate. Try using a the File Editor feature at this site to figure out what’s going on <a href="https://dicom.innolitics.com/ciods" class="inline-onebox">All CIODs – DICOM Standard Browser</a></p>

---

## Post #5 by @lassoan (2023-07-06 13:49 UTC)

<p>What software created the image?<br>
What is the voxel type of the image? Double floating point?<br>
Does the image load correctly if you use DCMTK approach?</p>

---

## Post #6 by @Sakuranezumi (2023-07-06 13:51 UTC)

<p>I am sorry sir, this is my first time trying to get help in the community,  i don’t know how to share a dicom file directly in the reply form. May I email you for a check ? Thank you very much.</p>

---

## Post #7 by @lassoan (2023-07-06 14:02 UTC)

<p>You can upload the files anywhere (dropbox, onedrive, google drive, etc.) and post the link here.</p>

---

## Post #8 by @Sakuranezumi (2023-07-06 14:24 UTC)

<p>Hello sir, here is the OneDrive link ,<a href="https://1drv.ms/u/s!AkmRJUo5DbDriy_v0bhoMvrKlFWY" class="inline-onebox" rel="noopener nofollow ugc">Microsoft OneDrive - Access files anywhere. Create docs with free Office Online.</a> . Thank you for your information</p>

---

## Post #9 by @lassoan (2023-07-06 15:48 UTC)

<p>The data set is invalid. See the output of David Clunie’s dciodvfy tool:</p>
<pre><code class="lang-txt">(0x0040,0x1008) LO Confidentiality Code  - Warning - Explicit value representation doesn't match data dictionary; Explicit &lt;ST&gt; Dictionary &lt;LO&gt;
(0x07a3,0x10ca)  ?  - Warning - Unrecognized tag - assuming explicit value representation OK
Warning - Value dubious for this VR - (0x0010,0x0010) PN Patient's Name  PN [1] = &lt;Anonymous&gt; - Retired Person Name form
MRImage
Error - Empty attribute (no value) Type 1 Required Element=&lt;ReferencedSOPClassUID&gt; Module=&lt;SOPInstanceReferenceMacro&gt;
Error - Empty attribute (no value) Type 1 Required Element=&lt;ReferencedSOPInstanceUID&gt; Module=&lt;SOPInstanceReferenceMacro&gt;
Error - Empty attribute (no value) Type 1C Conditional Element=&lt;CodeValue&gt; Module=&lt;BasicCodeSequenceMacro&gt;
Error - Empty attribute (no value) Type 1C Conditional Element=&lt;CodingSchemeDesignator&gt; Module=&lt;BasicCodeSequenceMacro&gt;
Error - Empty attribute (no value) Type 1 Required Element=&lt;CodeMeaning&gt; Module=&lt;BasicCodeSequenceMacro&gt;
Error - Attribute present when condition unsatisfied (which may not be present otherwise) Type 2C Conditional Element=&lt;Laterality&gt; Module=&lt;GeneralSeries&gt;
Warning - is only permitted to be empty when actually unknown; should be absent (not empty) if an unpaired body part, and have a value if a paired body part - attribute &lt;Laterality&gt;
Error - Empty attribute (no value) Type 1C Conditional Element=&lt;CodeValue&gt; Module=&lt;BasicCodeSequenceMacro&gt;
Error - Empty attribute (no value) Type 1C Conditional Element=&lt;CodingSchemeDesignator&gt; Module=&lt;BasicCodeSequenceMacro&gt;
Error - Empty attribute (no value) Type 1 Required Element=&lt;CodeMeaning&gt; Module=&lt;BasicCodeSequenceMacro&gt;
Warning - Unrecognized defined term &lt;M&gt; for value 3 of attribute &lt;Image Type&gt;
Warning - Non-identity Modality LUT Module (RescaleSlope and RescaleIntercept) not expected to be present in standard MR IOD - may cause windowing problems - attribute &lt;RescaleIntercept&gt; = &lt;32768&gt;
Warning - Non-identity Modality LUT Module (RescaleSlope and RescaleIntercept) not expected to be present in standard MR IOD - may cause windowing problems - attribute &lt;RescaleSlope&gt; = &lt;1&gt;
Warning - Attribute is not present in standard DICOM IOD - (0x0008,0x0061) CS Modalities in Study 
Warning - Attribute is not present in standard DICOM IOD - (0x0008,0x9208) CS Complex Image Component 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x1061) LO Trigger Source or Type 
Warning - Attribute is not present in standard DICOM IOD - (0x0018,0x9073) FD Acquisition Duration 
Warning - Attribute is not present in standard DICOM IOD - (0x0020,0x1208) IS Number of Study Related Instances 
Warning - Attribute is not present in standard DICOM IOD - (0x0028,0x1052) DS Rescale Intercept 
Warning - Attribute is not present in standard DICOM IOD - (0x0028,0x1053) DS Rescale Slope 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1032) PN Requesting Physician 
Warning - Attribute is not present in standard DICOM IOD - (0x0032,0x1060) LO Requested Procedure Description 
Warning - Attribute is not present in standard DICOM IOD - (0x0040,0x1008) LO Confidentiality Code 
Warning - Attribute is not present in standard DICOM IOD - (0x0054,0x0081) US Number of Slices 
Warning - Dicom dataset contains attributes not present in standard DICOM IOD - this is a Standard Extended SOP Class 
</code></pre>
<p>The invalid tag value that causes the load failure is <code>&lt;RescaleIntercept&gt; = &lt;32768&gt;</code>. Probably ITK complains because if this rescaling was applied then values stored in the image may not fit in the 16-bit voxel type.</p>
<p>If this value is not introduced by post-processing/anonymization then report the error to the manufacturer.</p>
<p>In the meantime, you can patch the files using DCMTK’s dcmodify tool by running it on each file like this:</p>
<pre><code class="lang-auto">dcmodify.exe -i RescaleIntercept=0 I1000000
</code></pre>

---

## Post #11 by @Sakuranezumi (2023-07-07 11:35 UTC)

<p>thank you for your help manager , I successfully open the file, love u. I will go try to tell the engineer to fix the trouble <img src="https://emoji.discourse-cdn.com/twitter/smiling_face_with_three_hearts.png?v=12" title=":smiling_face_with_three_hearts:" class="emoji" alt=":smiling_face_with_three_hearts:" loading="lazy" width="20" height="20"></p>

---
