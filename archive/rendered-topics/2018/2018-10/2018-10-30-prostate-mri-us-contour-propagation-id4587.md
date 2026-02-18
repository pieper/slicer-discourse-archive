# Prostate MRI-US contour propagation

**Topic ID**: 4587
**Date**: 2018-10-30
**URL**: https://discourse.slicer.org/t/prostate-mri-us-contour-propagation/4587

---

## Post #1 by @Felix_Navarro_Guirad (2018-10-30 10:02 UTC)

<p>Dear Slicer users and developers,</p>
<p>I’m using the “prostate MRI-US Contour propagation” module under Slicer 4.10 windows 64 bits. I have scanned a prostate phantom for ultrasound devices using MR and US. I have segmented the region that mimics the prostate on both set of images using the segment editor module.</p>
<p>First of all, I have applied a transformation to the US volume and segmentation in order to resize and center them close to MR image and segmentation.</p>
<p>After that I harden the transformation and launch the registration. Do any of you know why I’m getting the following error that halts the process? (<a href="https://drive.google.com/open?id=1SGB5G9ZX-ir77DQF3jBSQ26MuwDwQ_O1" rel="noopener nofollow ugc">here</a> you can find the data to replicate the error, the transformation performed is also attached)</p>
<blockquote>
<p>[INFO][Python] 30.10.2018 10:19:54 [Python] (C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py:547) - Performing registration workflow<br>
[INFO][Python] 30.10.2018 10:19:54 [Python] (C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py:602) - Cropping MRI volume<br>
[INFO][Python] 30.10.2018 10:19:56 [Python] (C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py:661) - Pre-aligning segmentations<br>
[INFO][Python] 30.10.2018 10:19:56 [Python] (C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py:674) - US prostate bounds: [154.5, 532.5, -443.5, -164.5, 0.5, 10.5]<br>
[INFO][Python] 30.10.2018 10:19:56 [Python] (C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py:683) - MRI prostate bounds: [305.0625, 381.9375, -353.453125, -254.546875, -29.5, 40.5]<br>
[INFO][Python] 30.10.2018 10:19:56 [Python] (C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py:687) - MRI to US prostate translation: [0.0, 0.0, 0.0]<br>
[INFO][Python] 30.10.2018 10:19:56 [Python] (C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py:722) - Resampling US volume<br>
[INFO][Python] 30.10.2018 10:20:35 [Python] (C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py:747) - Creating prostate contour labelmaps<br>
[INFO][Stream] 30.10.2018 10:19:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Performing registration workflow<br>
[INFO][Stream] 30.10.2018 10:19:54 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Cropping MRI volume<br>
[INFO][Stream] 30.10.2018 10:19:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Pre-aligning segmentations<br>
[INFO][Stream] 30.10.2018 10:19:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - US prostate bounds: [154.5, 532.5, -443.5, -164.5, 0.5, 10.5]<br>
[INFO][Stream] 30.10.2018 10:19:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - MRI prostate bounds: [305.0625, 381.9375, -353.453125, -254.546875, -29.5, 40.5]<br>
[INFO][Stream] 30.10.2018 10:19:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - MRI to US prostate translation: [0.0, 0.0, 0.0]<br>
[WARNING][VTK] 30.10.2018 10:19:56 [vtkMRMLLinearTransformNode (0000000DA5111520)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLTransformNode.cxx:1547) - vtkMRMLTransformNode::SetAndObserveMatrixTransformToParent method is deprecated. Use vtkMRMLTransformNode::SetMatrixTransformToParent instead<br>
[INFO][Stream] 30.10.2018 10:19:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Resampling US volume<br>
[DEBUG][Qt] 30.10.2018 10:19:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Found CommandLine Module, target is C:/Program Files/Slicer 4.10.0/bin/…/lib/Slicer-4.10/cli-modules/ResampleScalarVolume.exe<br>
[DEBUG][Qt] 30.10.2018 10:19:56 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 30.10.2018 10:19:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Resample Scalar Volume command line:<br>
C:/Program Files/Slicer 4.10.0/bin/…/lib/Slicer-4.10/cli-modules/ResampleScalarVolume.exe --spacing 1,1,1 --interpolation lanczos C:/Users/BEBIG Variseed/AppData/Local/Temp/Slicer/DIDG_vtkMRMLScalarVolumeNodeC.nrrd C:/Users/BEBIG Variseed/AppData/Local/Temp/Slicer/DIDG_vtkMRMLScalarVolumeNodeBE.nrrd<br>
[DEBUG][Qt] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Resample Scalar Volume completed without errors<br>
[INFO][VTK] 30.10.2018 10:20:35 [vtkMRMLVolumeArchetypeStorageNode (0000000D8A821C00)] (D:\D\S\Slicer-4100\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/BEBIG Variseed/AppData/Local/Temp/Slicer/DIDG_vtkMRMLScalarVolumeNodeBE.nrrd. Dimensions: 240x240x256. Number of components: 1. Pixel type: short.<br>
[INFO][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Creating prostate contour labelmaps<br>
[CRITICAL][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File "C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py", line 336, in onPerformRegistration<br>
[CRITICAL][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - if self.logic.performRegistration():<br>
[CRITICAL][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File "C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py", line 551, in performRegistration<br>
[CRITICAL][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - self.createProstateContourLabelmaps()<br>
[CRITICAL][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - File "C:/Users/BEBIG Variseed/AppData/Roaming/NA-MIC/Extensions-27501/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules/ProstateMRIUSContourPropagation.py", line 756, in createProstateContourLabelmaps<br>
[CRITICAL][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - mrProstateOrientedImageData.DeepCopy(self.mrSegmentationNode.GetSegmentation().GetSegment(self.mrProstateSegmentName).GetRepresentation(slicer.vtkSegmentationConverter.GetSegmentationBinaryLabelmapRepresentationName()))<br>
[CRITICAL][Stream] 30.10.2018 10:20:35 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - AttributeError: ‘NoneType’ object has no attribute ‘GetRepresentation’</p>
</blockquote>
<p>Thank you very much in advance.</p>

---

## Post #2 by @cpinter (2018-10-30 13:36 UTC)

<p>Can you please try to reproduce this with data which does not contain sensitive information? For example doing some fake workflow with the MRHead and CTChest sample datasets.</p>
<p>By the way you don’t need to pre-align anything manually, the module does that as a pre-processing step.</p>

---

## Post #3 by @Felix_Navarro_Guirad (2018-10-31 08:55 UTC)

<p>Dear Csaba, thank you very much for your answer.</p>
<p>The linked images are obtained using a phantom and fake identification data, there is no personal information which may be sensitive. Thank you for the remainder.</p>
<p>Enclosed in the mrb file you can find the MR volume (800: Multiplanar reconstruction), the US volume (201801029000011_0), and segmentations of the prostate part of the phantom on MR images (segmentation RM) and US images (sementation US).</p>
<p>To reproduce the situation just load de prostate MR-US contour propagation module, select the US and MR volumes, select the segmentations and perform the registration.</p>
<p>Best regards.</p>

---

## Post #4 by @Felix_Navarro_Guirad (2018-11-05 21:58 UTC)

<p>Dear users and developers,</p>
<p>Did any of you could find a reason which could cause this module to crash when the shared images are used?</p>
<p>Any help would be appreciated.</p>
<p>Thank you very much.</p>

---

## Post #5 by @cpinter (2018-11-06 14:03 UTC)

<p>Thanks for the reminder. I’ll debug into this, hopefully soon.</p>

---

## Post #6 by @cpinter (2018-11-06 16:44 UTC)

<p>I tried with 4.10, and there was no crash, but I got the same error message that you got.</p>
<p>I see that you scaled the US volume from the original 1x1x1mm to 5x0.2x0.2mm with a transform. Part of the reason the registration didn’t work is that the CropVolume module that ProstateMRIUSContourPropagation uses didn’t consider the parent transform. If you harden the transform, then this will not be a problem. I’ll fix this first issue in the module so that not hardened parent transforms are handled correctly.</p>
<p>By the way how come you needed to do this manual scaling of the US volume?</p>
<p>The main issue is a bug in the module which happens if the segmentation was done in Slicer and not loaded from DICOM. I’ll fix that too. Both of these are pretty simple, so probably I can fix it soon.</p>

---

## Post #7 by @cpinter (2018-11-06 17:30 UTC)

<p>I believe I fixed the issues, but there is one final error. It’s probably because there are artifacts in one of the segmentations. As the segmetnation uses solely the two segmentations, they need to have the same generic shape, so you absolutely need to make sure that such artifacts are removed. The Scissors effect is perfect for such task.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccde9324c5b3aa4677c7bc37078cecbf598c7d23.jpeg" alt="image" data-base62-sha1="temgD6FcN6A2OlqfPLwbIog8iUb" width="335" height="319"></p>

---

## Post #8 by @Felix_Navarro_Guirad (2018-11-06 19:46 UTC)

<p>Thank you very much for your effort and time.</p>
<p>If I remove and reinstall the module will I get the fixed version?</p>
<p>I’ll test it using new segmentations.</p>
<p>Best regards.</p>

---

## Post #9 by @cpinter (2018-11-06 20:01 UTC)

<p>Thanks for the explanation. Still it’s quite strange that even the x,y spacing is incorrect in the US volume. If you’re not tied to Variseed for your experiment I’d probably do the volume reconstruction using SlicerIGT.</p>
<p>I did the necessary fixes and the registration is performed without errors now. The nightly release tomorrow will contain the fixed extension. However, the result with your dataset is not really good, it seems that the distance based registration (provided by SlicerProstate extension) does not find a good minimum. The deformation field is very erratic.</p>
<p>I spent most of today on this but now have to work on my regular things, so I’ll leave you to work on fixing this last part.<br>
What I’d try next is to make sure that the US segmentation is isotropic. There is a small box in Segment Editor at the end of the line of the master volume selector that allows changing the segmentation’s geometry. You can check isotropic there to make the voxels cube shaped. This might not work for the registration because the ultrasound volume’s geometry is used, so in that case you can go to Crop volume and resample the US image so that it is not this coarse (so that a voxel is not 25 times longer along Z then X and Y), and there are way more slices.<br>
Then do the segmentation carefully to not include any artifacts (show in 3D so it’s easier to see). It may also help to fill the hole the probe leaves. You can do that with Fill between slices.</p>

---

## Post #10 by @Felix_Navarro_Guirad (2018-11-06 20:10 UTC)

<p>Thank you very much, I’ll try it using the new version.</p>

---

## Post #11 by @Felix_Navarro_Guirad (2018-11-13 12:57 UTC)

<p>Thank you very much for the modifications made, now the code works fine.</p>
<p>We will try to tune the procedure using images of real patients instead of images from a phantom.</p>

---
