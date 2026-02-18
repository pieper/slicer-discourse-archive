# How to fetch dicom file as next sample in MONAI Label extension in 3D Slicer

**Topic ID**: 30131
**Date**: 2023-06-20
**URL**: https://discourse.slicer.org/t/how-to-fetch-dicom-file-as-next-sample-in-monai-label-extension-in-3d-slicer/30131

---

## Post #1 by @Arpan_Gyawali (2023-06-20 02:38 UTC)

<p>Hello,<br>
I have a brain CTA dataset for the task of brain extraction. The dataset contains both nifty as well as dicom format data. I have fetched all the nifty file and trained them. But i am not able to fetch dicom files using next sample button. But it supports dicom files right?<br>
How can i fetch next dicom file so that i can train them without converting them into nifty as most of the data we receive are in dicom format.<br>
I still have dicom data in the dataset folder but it shows 100% in active learning section.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b018a1d24c1ddc1b6345bb2c7f707316266d551e.png" alt="Screenshot 2023-06-20 080653" data-base62-sha1="p7OO9gxk0Bwrus5t2Gq5AluSqYu" width="540" height="95"></p>

---

## Post #2 by @rbumm (2023-06-20 05:19 UTC)

<p><a href="https://github.com/Project-MONAI/MONAILabel/discussions/1008">This thread</a> may get you started.</p>

---

## Post #3 by @diazandr3s (2023-06-27 12:16 UTC)

<p>Hi <a class="mention" href="/u/arpan_gyawali">@Arpan_Gyawali</a>,</p>
<p>Good question.<br>
As suggested by <a class="mention" href="/u/rbumm">@rbumm</a>, you could consider the solution proposed here: <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1008#discussioncomment-3685380" class="inline-onebox" rel="noopener nofollow ugc">Using DICOM folders of data instead of nifti files for image volumes. · Project-MONAI/MONAILabel · Discussion #1008 · GitHub</a></p>
<p>Another way is by using a DICOMWeb such as Orthanc. For this and start the MONAI Label server pointing to that server instead of a local folder: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/ohif#installing-orthanc-dicomweb" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/plugins/ohif at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Otherwise, you could continue using the MONAI Label server pointing to a folder, manually load the DICOM image, and push them one by one to the server.</p>
<p>Hope this helps,</p>

---

## Post #4 by @Arpan_Gyawali (2023-07-06 08:46 UTC)

<p>Thank you so much <a class="mention" href="/u/diazandr3s">@diazandr3s</a> .<br>
Sorry for late reply</p>

---
