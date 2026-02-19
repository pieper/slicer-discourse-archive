---
topic_id: 12200
title: "Save A Dicom Data As A Nifti"
date: 2020-06-24
url: https://discourse.slicer.org/t/12200
---

# Save a DICOM Data as a Nifti

**Topic ID**: 12200
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/save-a-dicom-data-as-a-nifti/12200

---

## Post #1 by @radio123 (2020-06-24 14:58 UTC)

<p>Hi guys,</p>
<p>at the moment I try to segment DICOM MR pictures. Before Slicer I used ITK Snap. Now I have the problem when I try to save my DICOM as a nifti (.nii) it is not possible. There are just the options .nrrd and other. Same problem when I try to save my Segmentation as a .nii.gz data. Can you please help me?</p>
<p>Thank you very much!</p>

---

## Post #2 by @Andinet_Enquobahrie (2020-06-24 15:01 UTC)

<p>Hello <a class="mention" href="/u/radio123">@radio123</a></p>
<p>What version of Slicer are using?</p>
<p>In the Save dialog box, if you click on the drop down menu for File format, you should get .nii and .nii.gz formats</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/461a1fbaab162ef98a6fb5ff749d514a331d5279.png" data-download-href="/uploads/short-url/a09onx9d5YK5bP4QKKy9DMy2CaB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/461a1fbaab162ef98a6fb5ff749d514a331d5279_2_690x234.png" alt="image" data-base62-sha1="a09onx9d5YK5bP4QKKy9DMy2CaB" width="690" height="234" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/461a1fbaab162ef98a6fb5ff749d514a331d5279_2_690x234.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/461a1fbaab162ef98a6fb5ff749d514a331d5279_2_1035x351.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/461a1fbaab162ef98a6fb5ff749d514a331d5279.png 2x" data-dominant-color="F4F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1225×417 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Andinet</p>

---

## Post #3 by @radio123 (2020-06-24 15:02 UTC)

<p>Hi!<br>
Thanks for your response! I use 4.10.2<br>
Yes I tried this but there are no .nii or .nii.gz options. Is my version too old?</p>

---

## Post #4 by @Andinet_Enquobahrie (2020-06-24 16:12 UTC)

<p>No, it should still work. Have you scrolled all the way down using the drop down menu for the File Format option? What file formats do you get?</p>

---

## Post #5 by @pieper (2020-06-24 16:49 UTC)

<p><a class="mention" href="/u/radio123">@radio123</a> -  did you export your segmentation to a labelmap first? (Use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#panels-and-their-use">Export in the segmentations module</a>).  Nii format can’t save a full segmentation so it’s not a save option.</p>

---

## Post #6 by @eleanor (2022-09-18 17:16 UTC)

<p>hello, i am having the same problem…did you find a solution? thank you .</p>

---

## Post #7 by @lassoan (2022-09-21 13:46 UTC)

<p>You can find step-by-step instructions for exporting segmentation to NIFTI format in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">Segmentations module documentation</a>.</p>

---
