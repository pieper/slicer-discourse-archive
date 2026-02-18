# Is there a way to register 2D+t cines?

**Topic ID**: 27510
**Date**: 2023-01-27
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-register-2d-t-cines/27510

---

## Post #1 by @Gening_Dong (2023-01-27 23:35 UTC)

<p>Hi,</p>
<p>I’ve been using sequence registration to register image stacks and it works well! Now I have a series of 2D+t ultrasound cines (DICOM files). Since it’s 2D+t, I’m not able to import those files as volumes and perform sequence registration. I was wondering if there’s a way to register 2D+t images so I can get a 4D dataset.</p>
<p>Thanks in advance!<br>
Gening</p>

---

## Post #2 by @lassoan (2023-01-28 17:35 UTC)

<p>Is the ultrasound image loaded as a volume sequence (can you play/pause it it using the sequence browser toolbar)?</p>
<p>If yes, then most likely the issue is that you are using a registration preset that is developed for 3D volumes. It may be also an issue that most ultrasound images are stored in DICOM as screenshots, therefore they are RGB color images.</p>
<p>You can try registering just two slices first and then if it works then go back and make it work in Sequence registration.</p>
<p>We also had some success in using ANTs and SynthMorph/VoxelMorph for 3D+t ultrasound registration. You can give them a try, too.</p>

---

## Post #3 by @Gening_Dong (2023-01-28 18:00 UTC)

<p>Hi Andras,</p>
<p>Thanks for the reply! However, the images cannot be uploaded as a volume sequence. When I uploaded the DICOM files and clicked “Examine”, there wasn’t one with the reader “MultiVolume”. I think it’s because each file is a 2D+t image, so each one of them is not a volume at all. To get a volume, several slices are supposed to be registered so those slices together become a 3D+t.</p>
<p>Best,<br>
Gening</p>

---

## Post #4 by @lassoan (2023-01-28 18:05 UTC)

<p>Recent Slicer versions load ultrasound images as volume sequence (it does not matter that the volume contains a single slice, it is still a 3D object, located in 3D physical space).</p>
<p>MultiVolume module is being phased out. The volume sequence should appear in the scene as a sequence node and a sequence browser node. Unfortunately, ultrasound images in DICOM are quite messy and complicated, so it is possible that your images are not recognized as an image sequence. If you use the latest Slicer release and you cannotoad them as volume sequence then ease share a phantom/animal/anonymized study so that we can investigate.</p>

---

## Post #5 by @Gening_Dong (2023-02-03 19:55 UTC)

<p>Hi Andras,</p>
<p>Thanks for the information! I’ve updated the Slicer to the latest version (5.2.1) and tried to load DICOM files (little endian) again. They were loaded as Sequence Node and Vector Volume Node. And you are right about the RGB color, the ultrasound images are stored in DICOM as screenshots. I’ll try to process those DICOM files into 32-bit 3D+t first and then try the registration.</p>
<p>Best,</p>
<p>Gening</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de15464ce986b9f30c01d733793f8ad9780ab6b6.png" data-download-href="/uploads/short-url/vGDzTZRK5A8tonKZ8ifiTwieAMm.png?dl=1" title="4B93809A07804FC4A62D9BA08FC0503B.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de15464ce986b9f30c01d733793f8ad9780ab6b6.png" alt="4B93809A07804FC4A62D9BA08FC0503B.png" data-base62-sha1="vGDzTZRK5A8tonKZ8ifiTwieAMm" width="690" height="1" data-dominant-color="000000"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4B93809A07804FC4A62D9BA08FC0503B.png</span><span class="informations">698×2 68 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
