# Registration of two DICOM-Sets from MRI

**Topic ID**: 23475
**Date**: 2022-05-18
**URL**: https://discourse.slicer.org/t/registration-of-two-dicom-sets-from-mri/23475

---

## Post #1 by @Leon_Dosendepp (2022-05-18 19:46 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Two DICOM-Sets of different size are registered with landmark registration and one DICOM-Set with both combined is exported.<br>
Actual behavior:<br>
I have one DICOM-Set of a Calf and one of a Foot. They have different resolutions and sizes (Foot 512x512, calf 384x384). If i use landmark registration it first seems perfect in the preview. I used Affine registration and the rigid registration mode. Then i go to resample image (BRAINS) select the image to warp and the reference image, with the pixel type im unsure so i left it at float. Next i select under warping parameters the transform file transform, which is the only one i get, interpolation mode to linear and apply. But now it dosent look like the preview anymore, the warped DICOM seems like randomly thrown on the reference DICOM and everthing of the warped DICOM which is not in the dimensions of the reference DICOM just gets cut. Please help me on how to get the DICOM like it is shown in the preview of the registration or if you have any different approach let me know, i would be happy to learn. Thank you in advance!</p>

---

## Post #2 by @pieper (2022-05-18 20:34 UTC)

<p>Hi -</p>
<p>What you can try is CropVolume to make a new volume that’s big enough to hold both the foot and the calf.  Then harden the transform you on the volume from Landmark Registration and use the Add Volumes to make a new composite.  If there’s overlap you can trim one volume or the other with CropVolume.</p>

---

## Post #3 by @Leon_Dosendepp (2022-06-08 11:47 UTC)

<p>Hey piper,</p>
<p>first of all thank you! I had the project on hold so please excuse my late response. To harden the transform was the missing step i was looking for.<br>
For anybody else who has a similar problem, here is how i did it:<br>
Change one volume to be larger and so accommodate for second DICOM-Set</p>
<p>Volume Rendering – create new ROI-&gt;save</p>
<p>Converters-&gt;Crop volume-&gt;newROI as input ROI-&gt;save</p>
<p><a href="https://youtu.be/2gWv4f-2zrA" class="inline-onebox" rel="noopener nofollow ugc">3D Slicer: Volume Rendering and ROI's - YouTube</a>, <a href="https://discourse.slicer.org/t/merge-dicom-or-nrrd-or-nii-images/1566" class="inline-onebox">Merge dicom or nrrd or nii images</a>, <a href="https://discourse.slicer.org/t/padding-a-volume-with-cropvolume-requires-interpolated-cropping/8750" class="inline-onebox">Padding a volume with CropVolume requires "Interpolated Cropping"</a></p>
<p>Landmark registration fixed volume is new enlarged volume, moving volume is the other DICOM</p>
<p>Use as few landmarks as possible. The last row is a live preview of the transformation.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="rBeh692v7kI" data-video-title="Landmark registration with 3DSlicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=rBeh692v7kI" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/rBeh692v7kI/maxresdefault.jpg" title="Landmark registration with 3DSlicer" width="" height="">
  </a>
</div>

<p>Harden transform with Transforms module</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html</a></p>
<p>Combine volumes of transformed and enlarged DICOMs with Add Scalar Volumes module</p>
<p>thanks again Piper</p>

---
