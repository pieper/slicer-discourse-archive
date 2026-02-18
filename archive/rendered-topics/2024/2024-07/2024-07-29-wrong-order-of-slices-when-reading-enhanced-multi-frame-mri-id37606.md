# Wrong order of slices when reading enhanced multi-frame MRI containing 3 image stacks

**Topic ID**: 37606
**Date**: 2024-07-29
**URL**: https://discourse.slicer.org/t/wrong-order-of-slices-when-reading-enhanced-multi-frame-mri-containing-3-image-stacks/37606

---

## Post #1 by @winter (2024-07-29 09:11 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.6.2.</p>
<p>When loading slice packages (respiratory gated T2) to 3D Slicer, the slices get represented in a wrong order. When I open the DICOM file in ImageJ, the representation of the slices is normal.<br>
Is there any way to reorganize the slices in 3D Slicer? Please find an image attached.</p>
<p>Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93c439765e5529dabd3a9b32c41a71cc05b2a11e.jpeg" data-download-href="/uploads/short-url/l5cB1mhhhCexsvyDXvPbb3hK46q.jpeg?dl=1" title="Slice package" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93c439765e5529dabd3a9b32c41a71cc05b2a11e_2_690x418.jpeg" alt="Slice package" data-base62-sha1="l5cB1mhhhCexsvyDXvPbb3hK46q" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93c439765e5529dabd3a9b32c41a71cc05b2a11e_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93c439765e5529dabd3a9b32c41a71cc05b2a11e_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93c439765e5529dabd3a9b32c41a71cc05b2a11e_2_1380x836.jpeg 2x" data-dominant-color="535450"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slice package</span><span class="informations">1459×885 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-07-29 09:21 UTC)

<p>Have you loaded the image using the DICOM browser?</p>

---

## Post #3 by @winter (2024-07-29 09:33 UTC)

<p>Thank you for your reply Anras, yes, I did.</p>

---

## Post #4 by @lassoan (2024-07-29 09:38 UTC)

<p>Could you share the dataset (after anonymization) so that we can investigate? You can upload to onedrive/dropbox/google drive and post the link here.</p>

---

## Post #5 by @winter (2024-07-29 09:56 UTC)

<p>I am sending now only one sequence of the dicome file, please tell me, if you need the whole DICOM file.</p>
<p>Thank you for your help.</p>
<p><a href="https://1drv.ms/u/c/099b754dec08494e/EXlNrxN86S5AkYwJQycPfzkBERp_0oRkbbgF2kJ8wz3zOw?e=SFNeHo" rel="noopener nofollow ugc">ENIM1</a></p>

---

## Post #6 by @lassoan (2024-07-29 10:01 UTC)

<p>We would need all the slices, so it would be great if you could send those.</p>

---

## Post #7 by @winter (2024-07-29 10:10 UTC)

<p><a href="https://1drv.ms/f/c/099b754dec08494e/EonY8jjKSedKqux4OYK4VlMBS6IE9D1fbOYC7Xn0y42zIw?e=QwFTwG" rel="noopener nofollow ugc">DICOM</a></p>

---

## Post #8 by @lassoan (2024-07-29 23:50 UTC)

<p>This is probably a valid DICOM image but a very special one, as it is an enhanced multi-frame MRI containing 3 image stacks. I don’t think we’ll update the default DICOM image reader plugin in Slicer to handle these kind of images and checked a few other DICOM image readers and they were not able to load these images correctly either.</p>
<p>I’ve <a href="https://github.com/rordenlab/dcm2niix/issues/839">filed an issue to @Chris_Rorden’s dcm2niix DICOM converter tool</a>. If he manages to update his converter to handle this images then you’ll be able to load images like this into Slicer by installing the SlicerDcm2nii extension.</p>

---

## Post #9 by @winter (2024-07-30 06:45 UTC)

<p>Thank you for your kind help.<br>
There is an other issue in the same file, I can´t solve. I already sent a post, but I did not get response yet. I have a DCE image there with 3 layers in a time resolution of 1 sec during 9 minutes. When you open the image set the order of images displayed is : time 1 - frame 1; time 1 - frame 2; time 1 - frame 3;  time 2 - frame 1; time 2 - frame 2; time 2 - frame 3; and so on. I would prefere to have first ordered by frame and second to time. I would like to analyse the DCE in 3D Slicer but I did not find the right way yet. The image is not recognised as multiframe object but as scalar volume (The images are then arranged firstly in the order of time and secondly in order of Frames). This is why it won’t be recognised in the MultiVolumeExplorer as an input multivolume.</p>
<p>Could you maybe check this out, too? Thank you very much.</p>

---

## Post #10 by @lassoan (2024-07-31 10:37 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> has implemented a quick workaround in his dcm2niix tool. It will be available for latest Slicer Preview Release and in the latest Slicer Stable Release from tomorrow. You need to disable the default DICOM scalar volume reader plugin to make the dcm2niix plugin used by default:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d91646df3ea73efbfd86d0a2eb62edb839d59798.png" data-download-href="/uploads/short-url/uYrl18uPh4aosc6VxSRaeZPukty.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d91646df3ea73efbfd86d0a2eb62edb839d59798_2_482x499.png" alt="image" data-base62-sha1="uYrl18uPh4aosc6VxSRaeZPukty" width="482" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d91646df3ea73efbfd86d0a2eb62edb839d59798_2_482x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d91646df3ea73efbfd86d0a2eb62edb839d59798_2_723x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d91646df3ea73efbfd86d0a2eb62edb839d59798_2_964x998.png 2x" data-dominant-color="3D3737"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1070×1108 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The change in the dcm2niix tool may not be permanent, so please report the DICOM non-conformance error to your scanner manufacturer (sending them the <a href="https://github.com/rordenlab/dcm2niix/issues/839" class="inline-onebox">Incorrect 3D reconstruction for enhanced multi-frame MRI · Issue #839 · rordenlab/dcm2niix · GitHub</a> link should be sufficient).</p>
<p>I’ll comment on the DCE-MRI loading in <a href="https://discourse.slicer.org/t/dce-time-series-recognised-as-scalar-volume/33198">that topic</a>. In both cases the issue is that the new enhanced mult-frame MRI format is used, which is not well supported by most tools, including Slicer, as we have not encountered such images before. The issue is further complicated by Bruker’s implementation not fully following the DICOM standard.</p>

---

## Post #11 by @winter (2024-08-02 08:53 UTC)

<p>Thank you for your help, but for me it does not function perfectly. This way for me it loads only the first slice package with 14 slices.<br>
I am going to contact the manufacturer considering the DICOM non-conformance problem.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bfa94b0e72948ed167674e05b197e035d41006f.jpeg" data-download-href="/uploads/short-url/fpdXhVRqkdPAGhxVuu4tQ1twrwj.jpeg?dl=1" title="Screenshot_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bfa94b0e72948ed167674e05b197e035d41006f_2_690x418.jpeg" alt="Screenshot_1" data-base62-sha1="fpdXhVRqkdPAGhxVuu4tQ1twrwj" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bfa94b0e72948ed167674e05b197e035d41006f_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bfa94b0e72948ed167674e05b197e035d41006f_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6bfa94b0e72948ed167674e05b197e035d41006f_2_1380x836.jpeg 2x" data-dominant-color="45444E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_1</span><span class="informations">1459×885 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2024-08-02 09:18 UTC)

<p>This was the old behavior. You don’t have the new version of dcm2niix yet.</p>
<p>What operating system and Slicer version do you use?</p>

---

## Post #13 by @winter (2024-08-02 11:35 UTC)

<p>Windows 10 Enterprise<br>
Slicer 5.7.0</p>

---

## Post #14 by @lassoan (2024-08-03 22:32 UTC)

<p>Each day there is a new version of Slicer-5.7.0. Could you test with the very latest version (that you have just downloaded)?</p>

---

## Post #15 by @saaussan (2024-08-07 17:20 UTC)

<p>Hi,<br>
Can you please email Bruker application<br>
<a href="mailto:application.mri.americas@bruker.com">application.mri.americas@bruker.com</a><br>
We will send  you instructions to upload the data to troubleshoot the problem.<br>
Kind Regards,</p>

---

## Post #16 by @winter (2024-08-15 10:49 UTC)

<p>Dear Saaussaan, thank you for your reply, I have sent an e-mail there.</p>
<p>Kind Regards</p>

---

## Post #17 by @winter (2024-08-15 12:48 UTC)

<p>Dear Andras,<br>
I downloaded today the actual version of Slicer - 5.7.0, there Dcm2niixPlugin indeed opened the image in the right way. Thank you for your help.</p>

---
