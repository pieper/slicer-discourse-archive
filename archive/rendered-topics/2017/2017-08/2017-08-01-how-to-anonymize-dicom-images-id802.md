# How to anonymize DICOM images?

**Topic ID**: 802
**Date**: 2017-08-01
**URL**: https://discourse.slicer.org/t/how-to-anonymize-dicom-images/802

---

## Post #1 by @doc-xie (2017-08-01 15:24 UTC)

<p>Hello everyone,</p>
<p>I am a beginner of 3D Slicer and i have a simple question:</p>
<p>How to erase the information of patient on the CT or MR scan?</p>

---

## Post #2 by @moselhy (2017-08-01 15:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cf2992b47fc62e22633338f9b26bdc2d11d0fd3.png" data-download-href="/uploads/short-url/dgfGTbYX5RIDzxThtkV1uVyvYMX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf2992b47fc62e22633338f9b26bdc2d11d0fd3_2_690x379.png" alt="image" data-base62-sha1="dgfGTbYX5RIDzxThtkV1uVyvYMX" width="690" height="379" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf2992b47fc62e22633338f9b26bdc2d11d0fd3_2_690x379.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf2992b47fc62e22633338f9b26bdc2d11d0fd3_2_1035x568.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5cf2992b47fc62e22633338f9b26bdc2d11d0fd3_2_1380x758.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1435×790 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2017-08-01 15:56 UTC)

<p>If you want to remove protected health information from DICOM files you could look into DicomCleaner or CTP.</p>
<p><a href="http://www.dclunie.com/pixelmed/software/webstart/DicomCleanerUsage.html" class="onebox" target="_blank">http://www.dclunie.com/pixelmed/software/webstart/DicomCleanerUsage.html</a></p>
<p><a href="http://mircwiki.rsna.org/index.php?title=The_CTP_DICOM_Anonymizer" class="onebox" target="_blank">http://mircwiki.rsna.org/index.php?title=The_CTP_DICOM_Anonymizer</a></p>

---

## Post #4 by @fedorov (2017-08-01 17:05 UTC)

<p>Note that you should always be extra careful, since sometime information that is not obvious must be removed to make the DICOM data de-identified.</p>
<p>One may think that removing patient name and birth date is sufficient, but in reality the process is a lot a lot more complex. Because of this, it is usually a good idea to rely on established and verified tools, like the ones mentioned by <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>If you only care about the image pixel content, you can save the image into a non-DICOM format, which will discard all of the patient-specific metadata. Unless your image has burned-in annotations (and unless you worry about patient’s face or other image features that can uniquely identify the subject), this might be sufficient.</p>

---

## Post #6 by @doc-xie (2017-08-02 02:46 UTC)

<p>Thanks!<br>
Dicomcleaner is a very good software.I want to know whether the procedure can be done with 3d slicer?</p>

---

## Post #7 by @pieper (2017-08-02 13:20 UTC)

<p>Nothing specifically for deidentification in Slicer.  Best to use one of the dedicated tools if you want to be confident in the results (it’s unfortaunately easy for patient identifying information to be left in the files by mistake).</p>

---

## Post #8 by @lassoan (2017-08-02 13:26 UTC)

<p>What you can easily do in Slicer is what <a class="mention" href="/u/fedorov">@fedorov</a> suggested above: save the image file as .nrrd file (menu: File / Save).</p>
<p>You could find ways in Slicer to edit DICOM metadata but you are probably better off using dedicated tools. Why is it important for you to do the anonymization in Slicer?</p>

---

## Post #9 by @doc-xie (2017-08-03 16:53 UTC)

<p>Thanks to everyone!<br>
The best method to solve this problem is using dedicated tools.<br>
The most simple method is saving the image file an non-DICOM format.<br>
Sincerely!</p>

---

## Post #10 by @montamrta (2022-09-12 07:31 UTC)

<p>Adage is a pretty good DICOM Anonymization tool. It is available for free and easily accessible here <a href="https://www.ai-medical.ch/adage" class="inline-onebox" rel="noopener nofollow ugc">Adage - AI Medical</a></p>

---

## Post #11 by @zubmedia (2022-10-12 13:44 UTC)

<p>there is a good program where you can anonymize and change tags in one click. <a href="https://anonymizer.imv-ms.com/" rel="noopener nofollow ugc">https://anonymizer.imv-ms.com/</a>.</p>

---

## Post #12 by @lassoan (2022-10-13 17:30 UTC)

<p>Note that both these above-mentioned tools (Adage and IMV) are very basic, oversimplified tools. They don’t seem to offer essential anonymization techniques (such as randomizing patient birth date, study dates to keep the relative timestamp valid, etc.), and don’t even attempt to make the image content safe (detect and remove burnt-in annotations, remove patient face, etc.).</p>
<p>CTP and DicomCleaner that <a class="mention" href="/u/pieper">@pieper</a> mentioned above are more sophisticated, professional tools (and they are free and open-source). They may be harder to learn, but it is worth the effort if you need proper anonymization.</p>

---

## Post #14 by @sdamirsa (2023-08-13 10:31 UTC)

<p>Thanks, dear Andras, I always found your comments useful.</p>

---

## Post #15 by @sdamirsa (2023-12-20 16:14 UTC)

<p>Hi all,</p>
<p><strong>I wanted to share a no-code solution for pseudonymizing your cases</strong><br>
<strong>The whole code and step by step use-guide is here: <a href="https://github.com/Sdamirsa/PanCanAID/blob/main/Step1_SortingFiles/README.MD" class="inline-onebox" rel="noopener nofollow ugc">PanCanAID/Step1_SortingFiles/README.MD at main · Sdamirsa/PanCanAID · GitHub</a></strong></p>
<p>I know that these days, more people (like me <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> are working with Dicom, and I also noticed how anonymization can disturb your peace. So, I created this no code Python script, you just need to run it and it will identify dicom studies (each with many .dcm files) and extract dicom meta (I tried to extract all useful studies), assign pseudonymized numbers (defined by you), and then anonymize all dicoms while providing an excel that links new pseudonymized numbers with your patient (I call pseudonymized key). If you don’t want to code, use it. And if you know how to code, you can revise it for your project. You can ask doctors involved in your project to pseudonymize cases even before sharing them with you).</p>
<p>The reason behind this is my problems during the PanCanAID project (I have been working on it for three years now), which contains data from many various centres and CT scans with various metadata.</p>

---
