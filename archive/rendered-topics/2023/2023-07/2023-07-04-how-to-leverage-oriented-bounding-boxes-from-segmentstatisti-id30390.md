---
topic_id: 30390
title: "How To Leverage Oriented Bounding Boxes From Segmentstatisti"
date: 2023-07-04
url: https://discourse.slicer.org/t/30390
---

# How to leverage oriented bounding boxes from SegmentStatistics to crop scans within python numpy

**Topic ID**: 30390
**Date**: 2023-07-04
**URL**: https://discourse.slicer.org/t/how-to-leverage-oriented-bounding-boxes-from-segmentstatistics-to-crop-scans-within-python-numpy/30390

---

## Post #1 by @tomek1911 (2023-07-04 12:49 UTC)

<p>Intro:<br>
I need to crop teeth instances in the CBCT scan. I have to do it in Python with numpy because I need to be able to crop data during code runs and experiments - e.g., by changing the crop margin along the z-axis) - in short, it has to be done outside the Slicer. To crop instances with slicing that are not aligned with array axes, I need to rotate them first. Inverse rotation does not work as I expect it to; something is missing I need to understand.</p>
<p>Current process:</p>
<ul>
<li>In Slicer: I generate oriented bounding boxes (OBBs) based on segmentation using Slicer (I created a simple extension for it that uses class SegmentStatistics). In the end, I have an LPS JSON file per each segment with parameters like center, size, and orientation.</li>
<li>Outside Slicer: I read nifti files to numpy (nibabel). I generate a matrix based on nifti affine to transform from LPS to IJK. I calculate inverse transform and apply it to bounding box vertices and CBCT scan.</li>
</ul>
<p><strong>PROBLEM</strong>: I expect to obtain scan oriented in the same way as the oriented bounding box - so axes of instance are now new scan axes, so I can easily crop it using array slicing. However, I cannot get these results. Inverse rotation does not generate proper results.</p>
<p>Details:<br>
I read image data from nifti file and OBBs data from JSON. The JSON file is saved in LPS, but I transform it to RAS like in <a href="https://discourse.slicer.org/t/transformation-matrix-ras-to-lps/19352">here</a>. I calculate inverse transform based on the affine matrix embedded in the nii.gz file to convert data from RAS2IJK (by IJK, I mean data space in pixels/voxels). Finally, I calculate the inverse transform of rotation in IJK. Now I can align the scan with OBB. I translate the instance center to the origin (precisely, it is in the rotation center at the beginning because of dimensions normalization and grid resampling, but I do not want to overcomplicate here), apply inverse rotation, and translate back with vector from box center to the scan center. I do the same with OBB vertices. Based on transformed vertices, I calculate slices to crop scan.</p>
<p>Resampling details:<br>
I apply an affine matrix using Pytorch and MONAI. Grid resampling requires additional operation of normalizing dimensions and aligning image corners - doc: <a href="https://docs.monai.io/en/stable/networks.html#monai.networks.utils.normalize_transform" rel="noopener nofollow ugc">here</a>.</p>
<p>Experiments and <strong>magic</strong>:<br>
To make the transformation work, I do a bizarre and unintuitive thing. I calculate intrinsic Euler angles (‘xyz’). I change the sign of rotation around the x and y-axis. I multiply rotation matrices based on angles in proper order zyx. The magic rotation matrix constructed in this way works correctly for the scan but not for OBB vertex coordinates.</p>
<p>Example when it works (affine with <strong>magic</strong>):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/76d07c3f90ee3a7070d3de967c45cfe8351cb4a4.jpeg" data-download-href="/uploads/short-url/gX51ccNlOgOVa5FEilDJaupC8Re.jpeg?dl=1" title="Screenshot 2023-07-04 at 12.35.05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76d07c3f90ee3a7070d3de967c45cfe8351cb4a4_2_690x284.jpeg" alt="Screenshot 2023-07-04 at 12.35.05" data-base62-sha1="gX51ccNlOgOVa5FEilDJaupC8Re" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76d07c3f90ee3a7070d3de967c45cfe8351cb4a4_2_690x284.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76d07c3f90ee3a7070d3de967c45cfe8351cb4a4_2_1035x426.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/76d07c3f90ee3a7070d3de967c45cfe8351cb4a4_2_1380x568.jpeg 2x" data-dominant-color="8C8C8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-04 at 12.35.05</span><span class="informations">1920×793 53.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Example when it doesn’t work (np.linalg.inv(rotationMatrixRAS)):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c268c46f2bc777f701996bad59b2a0b5296b6c.jpeg" data-download-href="/uploads/short-url/rvec2zvUc90R7wfmkvUagIUpwE4.jpeg?dl=1" title="Screenshot 2023-07-04 at 12.33.58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0c268c46f2bc777f701996bad59b2a0b5296b6c_2_690x283.jpeg" alt="Screenshot 2023-07-04 at 12.33.58" data-base62-sha1="rvec2zvUc90R7wfmkvUagIUpwE4" width="690" height="283" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0c268c46f2bc777f701996bad59b2a0b5296b6c_2_690x283.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0c268c46f2bc777f701996bad59b2a0b5296b6c_2_1035x424.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0c268c46f2bc777f701996bad59b2a0b5296b6c_2_1380x566.jpeg 2x" data-dominant-color="8B8B8B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-04 at 12.33.58</span><span class="informations">1920×788 49.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Slicer OBBs:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2925f7f3df41792e905be1cc2d2e17594bf37e88.jpeg" data-download-href="/uploads/short-url/5S0Vgb4xjezNYGptuVi748PA8fS.jpeg?dl=1" title="Screenshot 2023-07-04 at 13.33.21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2925f7f3df41792e905be1cc2d2e17594bf37e88_2_690x462.jpeg" alt="Screenshot 2023-07-04 at 13.33.21" data-base62-sha1="5S0Vgb4xjezNYGptuVi748PA8fS" width="690" height="462" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2925f7f3df41792e905be1cc2d2e17594bf37e88_2_690x462.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2925f7f3df41792e905be1cc2d2e17594bf37e88_2_1035x693.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/2925f7f3df41792e905be1cc2d2e17594bf37e88_2_1380x924.jpeg 2x" data-dominant-color="95889C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-04 at 13.33.21</span><span class="informations">1872×1254 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ed59f02e79a3f46fa161807d370fd09aadc0747.jpeg" data-download-href="/uploads/short-url/dwWyVHVG26kR5KlOiIioxi1ib2v.jpeg?dl=1" title="Screenshot 2023-07-04 at 13.33.42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ed59f02e79a3f46fa161807d370fd09aadc0747_2_431x500.jpeg" alt="Screenshot 2023-07-04 at 13.33.42" data-base62-sha1="dwWyVHVG26kR5KlOiIioxi1ib2v" width="431" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ed59f02e79a3f46fa161807d370fd09aadc0747_2_431x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ed59f02e79a3f46fa161807d370fd09aadc0747_2_646x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ed59f02e79a3f46fa161807d370fd09aadc0747_2_862x1000.jpeg 2x" data-dominant-color="8D91BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-04 at 13.33.42</span><span class="informations">920×1066 25.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am aware that some more explanations and details may be necessary, so please ask questions and I will try to answer them to make things clear.</p>
<p>*Data I am working with are publicly available.</p>
<p>Code:</p>
<pre><code class="lang-auto">import numpy as np
import nibabel as nib
from scipy.spatial.transform import Rotation as R
from monai.transforms import Affine 
from monai.networks.utils import normalize_transform

def cropOBB(self, obbCenterLPS, obbOrientationLPS, obbSize, volumeArray, labelArray, affineRAS) -&gt; Tuple[torch.tensor, torch.tensor, np.array, int]:
 
        #LPS
        directionLPSx = obbOrientationLPS[0::3]
        directionLPSy = obbOrientationLPS[1::3]
        directionLPSz = obbOrientationLPS[2::3]
        obbCenterLPS4 = np.append(obbCenterLPS, 1)
        rotationMatrixLPS33 = np.column_stack((directionLPSx, directionLPSy, directionLPSz))
        
        #RAS
        ras2LPS44 = np.diag([-1, -1, 1, 1]) 
        ras2LPS33 = np.diag([-1, -1, 1])
        ras2IJKinv44 = np.linalg.inv(affineRAS)
        #center
        obbCenterRAS4 = ras2LPS44 @ obbCenterLPS4
        #rotation
        rotationMatrixRAS33 = ras2LPS33 @ rotationMatrixLPS33
        rotationMatrixRAS44 = np.eye(4)
        rotationMatrixRAS44[:3,:3] = rotationMatrixRAS33
        rotationMatrixLPS44 = np.eye(4)
        rotationMatrixLPS44[:3,:3] = rotationMatrixLPS33
        #obb dimensions
        obbTopLeftNearRASVec3 = obbCenterRAS4[:3] - 0.5 * rotationMatrixRAS33 @ obbSize
        obbBottomRightFarRASVec3 = obbCenterRAS4[:3] + 0.5 * rotationMatrixRAS33 @ obbSize

        #IJK - volume data coordinates (voxels)
        obbsCenterIJKVec4 = ras2IJKinv44 @ obbCenterRAS4
        obbTopLeftNearIJKVec4 = ras2IJKinv44 @ np.append(obbTopLeftNearRASVec3, 1)
        obbBottomRightFarIJKVec4 = ras2IJKinv44 @ np.append(obbBottomRightFarRASVec3, 1)

        #transforms obb coordinates
        translationOBBOriginIJK44 = np.eye(4)
        translationOBBOriginIJK44[:3,3] = -obbsCenterIJKVec4[:3]

        translationBack2OriginOBB= np.eye(4)
        translationBack2OriginOBB[:,3] = obbsCenterIJKVec4

        #translations to origin - rotation center
        translation_2 = np.eye(4)
        scanOriginVec3 = obbsCenterIJKVec4[:3]
        translation_2[:,3] = np.append(scanOriginVec3,1) # centers tooth of interest in the screen
        
        translation_3 = np.eye(4)
        translation_4 = np.eye(4)
        obbOriginVec3 = obbsCenterIJKVec4[:3] - np.array(volumeArray.shape)//2
        translation_3[:,3] = np.append(-scanOriginVec3,1)
        translation_4[:,3] = np.append(-obbOriginVec3,1)


        #affine matrices
		# norm transform - data dimensions to grid resamlt dimensions [
        normTransformNonZeroCentered44 = normalize_transform(volumeArray.shape, align_corners=False, zero_centered=False)[0]

        #some kind of magic
        angles = R.from_matrix(np.linalg.inv(rotationMatrixLPS33)).as_euler('xyz', degrees=True)
        anglesAdjusted = angles * [-1,-1,1]
        rotationAdjusted = rot(anglesAdjusted[0], 'x') @ rot(anglesAdjusted[1],'y') @ rot(anglesAdjusted[2],'z')
        experimental_rotation = np.eye(4)
        
        affineMatrixNormalised44 = normTransformNonZeroCentered44 @ translation_2 @ rotationAdjusted
        obbCoordinatesAffineMatrix44 = translation_4 @ translation_2 @ np.linalg.inv(rotationMatrixLPS44) @ translation_3

        #apply affine obb
        obbTopLeftNearIJKOriginVec4 = obbCoordinatesAffineMatrix44 @ obbTopLeftNearIJKVec4
        obbBottomRightFarIJKOriginVec4 = obbCoordinatesAffineMatrix44 @ obbBottomRightFarIJKVec4
        obbsCenterIJKOriginVec4 = obbCoordinatesAffineMatrix44 @ obbsCenterIJKVec4
        obbCropSlices = tuple(map(lambda a, b: slice(int(np.floor(min(a,b))), int(np.ceil(max(a,b)))), obbTopLeftNearIJKOriginVec4[:3], obbBottomRightFarIJKOriginVec4[:3]))

        #apply affine on volume and label and resample
        volumeArray4ch= np.expand_dims(volumeArray, 0)
        labelArray4ch= np.expand_dims(labelArray, 0)
        transformedVolumeArray, _ = Affine(affine=affineMatrixNormalised44, normalized=True, mode='bilinear', padding_mode='zeros', image_only=False)(volumeArray4ch)
        transformedLabelArray, _ = Affine(affine=affineMatrixNormalised44, normalized=True, mode='nearest', padding_mode='zeros', image_only=False)(labelArray4ch)

        #crop transformed arrays
        croppedToothID = transformedLabelArray[0][tuple(map(lambda a: a//2, volumeArray.shape))].int().item()
        croppedVolume = transformedVolumeArray[0][obbCropSlices]
        croppedLabels = transformedLabelArray[0][obbCropSlices]
		
		#visualise results
        self.visualiseResults(croppedVolume, filename=f"{croppedToothID:02d}_croppedTooth")
        self.visualiseResults(transformedVolumeArray[0], filename=f"{croppedToothID:02d}_rectifiedTooth", bbox=obbCropSlices)
        self.visualiseSlices(volumeArray, obbTopLeftNearIJKVec4, obbBottomRightFarIJKVec4, obbsCenterIJKVec4,
                             obbTopLeftNearIJKOriginVec4, obbBottomRightFarIJKOriginVec4, obbsCenterIJKOriginVec4,
                             transformedVolumeArray[0], transformedLabelArray[0], croppedToothID)

        #delete labels of neighboring tooth
        croppedLabels[croppedLabels!=croppedToothID]=0

        cropAffine =  np.eye(4)
        cropAffine[:3,:3]=affineRAS[:3,:3]
        cropAffine[:,3] = obbsCenterIJKVec4

        return croppedVolume, croppedLabels, cropAffine, croppedToothID
</code></pre>

---

## Post #2 by @lassoan (2023-07-04 13:04 UTC)

<aside class="quote no-group" data-username="tomek1911" data-post="1" data-topic="30390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tomek1911/48/66603_2.png" class="avatar"> tomek1911:</div>
<blockquote>
<p>I need to crop teeth instances in the CBCT scan. I have to do it in Python with numpy because I need to be able to crop data during code runs and experiments - e.g., by changing the crop margin along the z-axis) - in short, it has to be done outside the Slicer.</p>
</blockquote>
</aside>
<p>Slicer’s Python environment should work as any other Python environment, but it offers some more built-in libraries and an optional desktop application GUI. Anything that you can do using the GUI you can do using Python scripting without relying on the GUI.</p>
<p>Therefore, I would recommend to simply use Crop volume module using Python scripting. You can reimplement all Slicer features using lower-level libraries (Slicer ultimately relies on VTK and ITK for most of its processing) but that’s up to you to figure out. If you need help for using lower-level libraries, you can ask on the forum of those libraries.</p>
<p>If you decide to reimplement cropping, here are some hints:</p>
<ul>
<li>I don’t think you can resample an image using numpy, but instead you can use ITK, SimpleITK, or VTK filters.</li>
<li>Euler angles is a not suitable for representing image orientation in medical image computing due to ambiguity and instability (gimbal lock).</li>
<li>You can solve all linear transforms related tasks, such as computing the transformation between any coordinate systems, using a homogeneous transformations. Always work with the compete transform - it should never be necessary to separate the translation and rotation parts.</li>
</ul>

---
