---
topic_id: 3165
title: "Dicom Image Volume Loaded As A Single Slice"
date: 2018-06-13
url: https://discourse.slicer.org/t/3165
---

# DICOM image volume loaded as a single slice

**Topic ID**: 3165
**Date**: 2018-06-13
**URL**: https://discourse.slicer.org/t/dicom-image-volume-loaded-as-a-single-slice/3165

---

## Post #1 by @Ash_Alarfaj (2018-06-13 11:09 UTC)

<p>Problem report for Slicer 4.9.0-2018-05-09 win-amd64: [please describe expected and actual behavior]</p>
<p>after I load data and open segment editor, it shows only one slice?! after pressing the thresould</p>

---

## Post #2 by @Sam_Horvath (2018-06-13 14:00 UTC)

<p>Hi!</p>
<p>Can you provide a screenshot of the error?  What kind of data are you using?</p>
<p>Thanks1</p>

---

## Post #3 by @Ash_Alarfaj (2018-06-13 14:54 UTC)

<p>I use MRI T1 W Images actually. when I download version4.8 the problem is solved. after spending time on version4.9, I think I will choose the stable version hopefully the errors will don’t exist. thank you and sorry I have not screenshot for the error.</p>

---

## Post #4 by @lassoan (2018-06-13 17:57 UTC)

<p>Slicer-4.8 will soon be replaced by the current nightly version, so it is important for us to know if there are any remaining issues. Can you explain what you mean by “it shows only one slice”? Only one of the slice viewers show an image, all the others are black? Is it reproducible with different data sets or just one? What is the file format (DICOM, nrrd, nii, …)?</p>

---

## Post #5 by @Ash_Alarfaj (2018-06-14 15:21 UTC)

<p>this error I have faced when I tried to download data many times. in both 4.9 and 4.8 versions</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad5ce36aefd386f960c20250def08b4fa018355.png" data-download-href="/uploads/short-url/1xQQKWFsuew1e26ebZUhTB3tLjn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad5ce36aefd386f960c20250def08b4fa018355_2_690x387.png" alt="image" data-base62-sha1="1xQQKWFsuew1e26ebZUhTB3tLjn" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad5ce36aefd386f960c20250def08b4fa018355_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/a/0ad5ce36aefd386f960c20250def08b4fa018355_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0ad5ce36aefd386f960c20250def08b4fa018355.png 2x" data-dominant-color="777982"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2018-06-14 15:36 UTC)

<p>A possibility for this problem is that you use the Add Data dialog to load DICOM data, instead of the DICOM browser, where you need to import the DICOM folder and then load the series.</p>

---

## Post #7 by @fedorov (2018-06-14 17:11 UTC)

<p>I think <a class="mention" href="/u/cpinter">@cpinter</a> guess is the right one.</p>
<p>As I looked over the FAQ, it struck me that we don’t have any basic information on what DICOM is, and how to deal with it. Looking at the <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">DICOM section of FAQ</a>, it assumes users know a lot already. I will make the time later today to edit that section to add a bit of introduction and basic information on how to get started with DICOM data in Slicer.</p>

---

## Post #8 by @Ash_Alarfaj (2018-06-15 14:15 UTC)

<p>Yes Actually I know Dicom is medical image formate but I am a bit confused when I load many studies and I need to distanguish them. Which one Is under process.</p>

---

## Post #9 by @cpinter (2018-06-15 15:26 UTC)

<p>The Subject hierarchy view in the Data module shows you the patient/study/series tree of the loaded DICOM objects. Let us know if you have specific questions.</p>

---

## Post #10 by @fedorov (2018-06-15 15:35 UTC)

<p>I added two new entries here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a>. Comments/edits are welcome. <a class="mention" href="/u/ash_alarfaj">@Ash_Alarfaj</a> if you could review the added entry for how to load DICOM data, and let us know if you followed those steps, it might help investigate what is going on in your case.</p>

---

## Post #11 by @lassoan (2025-02-09 23:19 UTC)

<p>A post was split to a new topic: <a href="/t/cannot-view-ultrasound-dicom-files/41595">Cannot view ultrasound DICOM files</a></p>

---
