# Landmark Registration transform resampling

**Topic ID**: 23243
**Date**: 2022-05-02
**URL**: https://discourse.slicer.org/t/landmark-registration-transform-resampling/23243

---

## Post #1 by @giovform (2022-05-02 17:42 UTC)

<p>Hello, I am using the <strong>Landmark Registration</strong> module to register a labelmap image onto another vector image. The registration is done with success, but I want to harden this transformation. Since it is a labelmap, using “Harden transform” causes the appearance of extra labels, because it is using an interpolation of order &gt; 0.</p>
<p>To solve this, I tried to use the modules <strong>Resample Image (BRAINS)</strong> and the <strong>Resample Scalar/Vector/DWI Volume</strong> but I am getting the following error messages when using the transform node:</p>
<p><strong>Resample Image (BRAINS)</strong> output:</p>
<pre><code class="lang-auto">Resample Image (BRAINS) standard error:

[FAILED]
Error while reading the the file C:/Work/GeoSlicer-1.6.0-2022-04-12-win-amd64/LTrace/temp/BCCCE_vtkMRMLTransformNodeB.h5

itk::ExceptionObject (0000009D1B5CC0E0)
Location: "unknown" 
File: C:\gs1\ITK\Modules\IO\TransformBase\src\itkTransformIOBase.cxx
Line: 62
Description: itk::ERROR: itk::ERROR: HDF5TransformIOTemplate(000001BEEEF8AC30): Could not create an instance of "InverseThinPlateSplineKernelTransform_double_3_3"
The usual cause of this error is not registering the transform with TransformFactory
Currently registered Transforms: 
	"AffineTransform_double_2_2"
	"AffineTransform_double_3_3"
	"AffineTransform_double_4_4"
	"AffineTransform_float_2_2"
	"AffineTransform_float_3_3"
	"AffineTransform_float_4_4"
	"AzimuthElevationToCartesianTransform_double_3_3"
	"AzimuthElevationToCartesianTransform_float_3_3"
	"BSplineDeformableTransform_double_2_2"
	"BSplineDeformableTransform_double_3_3"
	"BSplineDeformableTransform_float_2_2"
	"BSplineDeformableTransform_float_3_3"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_double_2_2"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_double_3_3"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_float_2_2"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_float_3_3"
	"BSplineTransform_double_2_2"
	"BSplineTransform_double_3_3"
	"BSplineTransform_float_2_2"
	"BSplineTransform_float_3_3"
	"CenteredAffineTransform_double_2_2"
	"CenteredAffineTransform_double_3_3"
	"CenteredAffineTransform_float_2_2"
	"CenteredAffineTransform_float_3_3"
	"CenteredEuler3DTransform_double_3_3"
	"CenteredEuler3DTransform_float_3_3"
	"CenteredRigid2DTransform_double_2_2"
	"CenteredRigid2DTransform_float_2_2"
	"CenteredSimilarity2DTransform_double_2_2"
	"CenteredSimilarity2DTransform_float_2_2"
	"CompositeTransform_double_2_2"
	"CompositeTransform_double_3_3"
	"CompositeTransform_double_4_4"
	"CompositeTransform_float_2_2"
	"CompositeTransform_float_3_3"
	"CompositeTransform_float_4_4"
	"ConstantVelocityFieldTransform_double_2_2"
	"ConstantVelocityFieldTransform_double_3_3"
	"ConstantVelocityFieldTransform_float_2_2"
	"ConstantVelocityFieldTransform_float_3_3"
	"DisplacementFieldTransform_double_2_2"
	"DisplacementFieldTransform_double_3_3"
	"DisplacementFieldTransform_float_2_2"
	"DisplacementFieldTransform_float_3_3"
	"Euler2DTransform_double_2_2"
	"Euler2DTransform_float_2_2"
	"Euler3DTransform_double_3_3"
	"Euler3DTransform_float_3_3"
	"FixedCenterOfRotationAffineTransform_double_3_3"
	"FixedCenterOfRotationAffineTransform_float_3_3"
	"GaussianExponentialDiffeomorphicTransform_double_2_2"
	"GaussianExponentialDiffeomorphicTransform_double_3_3"
	"GaussianExponentialDiffeomorphicTransform_float_2_2"
	"GaussianExponentialDiffeomorphicTransform_float_3_3"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_double_2_2"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_double_3_3"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_float_2_2"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_float_3_3"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_double_2_2"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_double_3_3"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_float_2_2"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_float_3_3"
	"IdentityTransform_double_2_2"
	"IdentityTransform_double_3_3"
	"IdentityTransform_double_4_4"
	"IdentityTransform_float_2_2"
	"IdentityTransform_float_3_3"
	"IdentityTransform_float_4_4"
	"QuaternionRigidTransform_double_3_3"
	"QuaternionRigidTransform_float_3_3"
	"Rigid2DTransform_double_2_2"
	"Rigid2DTransform_float_2_2"
	"Rigid3DPerspectiveTransform_double_3_2"
	"Rigid3DPerspectiveTransform_float_3_2"
	"Rigid3DTransform_double_3_3"
	"Rigid3DTransform_float_3_3"
	"ScalableAffineTransform_double_3_3"
	"ScalableAffineTransform_float_3_3"
	"ScaleLogarithmicTransform_double_3_3"
	"ScaleLogarithmicTransform_float_3_3"
	"ScaleSkewVersor3DTransform_double_3_3"
	"ScaleSkewVersor3DTransform_float_3_3"
	"ScaleTransform_double_2_2"
	"ScaleTransform_double_3_3"
	"ScaleTransform_double_4_4"
	"ScaleTransform_float_2_2"
	"ScaleTransform_float_3_3"
	"ScaleTransform_float_4_4"
	"ScaleVersor3DTransform_double_3_3"
	"ScaleVersor3DTransform_float_3_3"
	"Similarity2DTransform_double_2_2"
	"Similarity2DTransform_float_2_2"
	"Similarity3DTransform_double_3_3"
	"Similarity3DTransform_float_3_3"
	"TimeVaryingBSplineVelocityFieldTransform_double_2_2"
	"TimeVaryingBSplineVelocityFieldTransform_double_3_3"
	"TimeVaryingBSplineVelocityFieldTransform_float_2_2"
	"TimeVaryingBSplineVelocityFieldTransform_float_3_3"
	"TimeVaryingVelocityFieldTransform_double_2_2"
	"TimeVaryingVelocityFieldTransform_double_3_3"
	"TimeVaryingVelocityFieldTransform_float_2_2"
	"TimeVaryingVelocityFieldTransform_float_3_3"
	"TranslationTransform_double_2_2"
	"TranslationTransform_double_3_3"
	"TranslationTransform_double_4_4"
	"TranslationTransform_float_2_2"
	"TranslationTransform_float_3_3"
	"TranslationTransform_float_4_4"
	"VelocityFieldTransform_double_2_2"
	"VelocityFieldTransform_double_3_3"
	"VelocityFieldTransform_float_2_2"
	"VelocityFieldTransform_float_3_3"
	"VersorRigid3DTransform_double_3_3"
	"VersorRigid3DTransform_float_3_3"
	"VersorTransform_double_3_3"
	"VersorTransform_float_3_3"




Resample Image (BRAINS) standard output:

=====================================================
Input Volume:     C:/Work/GeoSlicer-1.6.0-2022-04-12-win-amd64/LTrace/temp/BCCCE_vtkMRMLLabelMapVolumeNodeB.nrrd
Reference Volume: 
Output Volume:    C:/Work/GeoSlicer-1.6.0-2022-04-12-win-amd64/LTrace/temp/BCCCE_vtkMRMLLabelMapVolumeNodeE.nrrd
Pixel Type:       short
Interpolation:    NearestNeighbor
Background Value: 0
Warp By Transform: C:/Work/GeoSlicer-1.6.0-2022-04-12-win-amd64/LTrace/temp/BCCCE_vtkMRMLTransformNodeB.h5
=====================================================
Warning:  missing Reference Volume defaulted to inputVolume
Read ITK transform from file: C:/Work/GeoSlicer-1.6.0-2022-04-12-win-amd64/LTrace/temp/BCCCE_vtkMRMLTransformNodeB.h5
******* HERE *******C:\gs1\BRAINSTools\BRAINSResample\BRAINSResample.cxx 195
itk::ExceptionObject (0000009D1B5CC0E0)
Location: "unknown" 
File: C:\gs1\ITK\Modules\IO\TransformBase\src\itkTransformIOBase.cxx
Line: 62
Description: itk::ERROR: itk::ERROR: HDF5TransformIOTemplate(000001BEEEF8AC30): Could not create an instance of "InverseThinPlateSplineKernelTransform_double_3_3"
The usual cause of this error is not registering the transform with TransformFactory
Currently registered Transforms: 
	"AffineTransform_double_2_2"
	"AffineTransform_double_3_3"
	"AffineTransform_double_4_4"
	"AffineTransform_float_2_2"
	"AffineTransform_float_3_3"
	"AffineTransform_float_4_4"
	"AzimuthElevationToCartesianTransform_double_3_3"
	"AzimuthElevationToCartesianTransform_float_3_3"
	"BSplineDeformableTransform_double_2_2"
	"BSplineDeformableTransform_double_3_3"
	"BSplineDeformableTransform_float_2_2"
	"BSplineDeformableTransform_float_3_3"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_double_2_2"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_double_3_3"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_float_2_2"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_float_3_3"
	"BSplineTransform_double_2_2"
	"BSplineTransform_double_3_3"
	"BSplineTransform_float_2_2"
	"BSplineTransform_float_3_3"
	"CenteredAffineTransform_double_2_2"
	"CenteredAffineTransform_double_3_3"
	"CenteredAffineTransform_float_2_2"
	"CenteredAffineTransform_float_3_3"
	"CenteredEuler3DTransform_double_3_3"
	"CenteredEuler3DTransform_float_3_3"
	"CenteredRigid2DTransform_double_2_2"
	"CenteredRigid2DTransform_float_2_2"
	"CenteredSimilarity2DTransform_double_2_2"
	"CenteredSimilarity2DTransform_float_2_2"
	"CompositeTransform_double_2_2"
	"CompositeTransform_double_3_3"
	"CompositeTransform_double_4_4"
	"CompositeTransform_float_2_2"
	"CompositeTransform_float_3_3"
	"CompositeTransform_float_4_4"
	"ConstantVelocityFieldTransform_double_2_2"
	"ConstantVelocityFieldTransform_double_3_3"
	"ConstantVelocityFieldTransform_float_2_2"
	"ConstantVelocityFieldTransform_float_3_3"
	"DisplacementFieldTransform_double_2_2"
	"DisplacementFieldTransform_double_3_3"
	"DisplacementFieldTransform_float_2_2"
	"DisplacementFieldTransform_float_3_3"
	"Euler2DTransform_double_2_2"
	"Euler2DTransform_float_2_2"
	"Euler3DTransform_double_3_3"
	"Euler3DTransform_float_3_3"
	"FixedCenterOfRotationAffineTransform_double_3_3"
	"FixedCenterOfRotationAffineTransform_float_3_3"
	"GaussianExponentialDiffeomorphicTransform_double_2_2"
	"GaussianExponentialDiffeomorphicTransform_double_3_3"
	"GaussianExponentialDiffeomorphicTransform_float_2_2"
	"GaussianExponentialDiffeomorphicTransform_float_3_3"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_double_2_2"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_double_3_3"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_float_2_2"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_float_3_3"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_double_2_2"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_double_3_3"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_float_2_2"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_float_3_3"
	"IdentityTransform_double_2_2"
	"IdentityTransform_double_3_3"
	"IdentityTransform_double_4_4"
	"IdentityTransform_float_2_2"
	"IdentityTransform_float_3_3"
	"IdentityTransform_float_4_4"
	"QuaternionRigidTransform_double_3_3"
	"QuaternionRigidTransform_float_3_3"
	"Rigid2DTransform_double_2_2"
	"Rigid2DTransform_float_2_2"
	"Rigid3DPerspectiveTransform_double_3_2"
	"Rigid3DPerspectiveTransform_float_3_2"
	"Rigid3DTransform_double_3_3"
	"Rigid3DTransform_float_3_3"
	"ScalableAffineTransform_double_3_3"
	"ScalableAffineTransform_float_3_3"
	"ScaleLogarithmicTransform_double_3_3"
	"ScaleLogarithmicTransform_float_3_3"
	"ScaleSkewVersor3DTransform_double_3_3"
	"ScaleSkewVersor3DTransform_float_3_3"
	"ScaleTransform_double_2_2"
	"ScaleTransform_double_3_3"
	"ScaleTransform_double_4_4"
	"ScaleTransform_float_2_2"
	"ScaleTransform_float_3_3"
	"ScaleTransform_float_4_4"
	"ScaleVersor3DTransform_double_3_3"
	"ScaleVersor3DTransform_float_3_3"
	"Similarity2DTransform_double_2_2"
	"Similarity2DTransform_float_2_2"
	"Similarity3DTransform_double_3_3"
	"Similarity3DTransform_float_3_3"
	"TimeVaryingBSplineVelocityFieldTransform_double_2_2"
	"TimeVaryingBSplineVelocityFieldTransform_double_3_3"
	"TimeVaryingBSplineVelocityFieldTransform_float_2_2"
	"TimeVaryingBSplineVelocityFieldTransform_float_3_3"
	"TimeVaryingVelocityFieldTransform_double_2_2"
	"TimeVaryingVelocityFieldTransform_double_3_3"
	"TimeVaryingVelocityFieldTransform_float_2_2"
	"TimeVaryingVelocityFieldTransform_float_3_3"
	"TranslationTransform_double_2_2"
	"TranslationTransform_double_3_3"
	"TranslationTransform_double_4_4"
	"TranslationTransform_float_2_2"
	"TranslationTransform_float_3_3"
	"TranslationTransform_float_4_4"
	"VelocityFieldTransform_double_2_2"
	"VelocityFieldTransform_double_3_3"
	"VelocityFieldTransform_float_2_2"
	"VelocityFieldTransform_float_3_3"
	"VersorRigid3DTransform_double_3_3"
	"VersorRigid3DTransform_float_3_3"
	"VersorTransform_double_3_3"
	"VersorTransform_float_3_3"



******* HERE *******C:\gs1\BRAINSTools\BRAINSResample\BRAINSResample.cxx 475

itk::ExceptionObject (0000009D1B5CD488)
Location: "unknown" 
File: C:\gs1\ITK\Modules\IO\TransformBase\src\itkTransformIOBase.cxx
Line: 62
Description: itk::ERROR: itk::ERROR: HDF5TransformIOTemplate(000001BEEEF8AC30): Could not create an instance of "InverseThinPlateSplineKernelTransform_double_3_3"
The usual cause of this error is not registering the transform with TransformFactory
Currently registered Transforms: 
	"AffineTransform_double_2_2"
	"AffineTransform_double_3_3"
	"AffineTransform_double_4_4"
	"AffineTransform_float_2_2"
	"AffineTransform_float_3_3"
	"AffineTransform_float_4_4"
	"AzimuthElevationToCartesianTransform_double_3_3"
	"AzimuthElevationToCartesianTransform_float_3_3"
	"BSplineDeformableTransform_double_2_2"
	"BSplineDeformableTransform_double_3_3"
	"BSplineDeformableTransform_float_2_2"
	"BSplineDeformableTransform_float_3_3"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_double_2_2"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_double_3_3"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_float_2_2"
	"BSplineSmoothingOnUpdateDisplacementFieldTransform_float_3_3"
	"BSplineTransform_double_2_2"
	"BSplineTransform_double_3_3"
	"BSplineTransform_float_2_2"
	"BSplineTransform_float_3_3"
	"CenteredAffineTransform_double_2_2"
	"CenteredAffineTransform_double_3_3"
	"CenteredAffineTransform_float_2_2"
	"CenteredAffineTransform_float_3_3"
	"CenteredEuler3DTransform_double_3_3"
	"CenteredEuler3DTransform_float_3_3"
	"CenteredRigid2DTransform_double_2_2"
	"CenteredRigid2DTransform_float_2_2"
	"CenteredSimilarity2DTransform_double_2_2"
	"CenteredSimilarity2DTransform_float_2_2"
	"CompositeTransform_double_2_2"
	"CompositeTransform_double_3_3"
	"CompositeTransform_double_4_4"
	"CompositeTransform_float_2_2"
	"CompositeTransform_float_3_3"
	"CompositeTransform_float_4_4"
	"ConstantVelocityFieldTransform_double_2_2"
	"ConstantVelocityFieldTransform_double_3_3"
	"ConstantVelocityFieldTransform_float_2_2"
	"ConstantVelocityFieldTransform_float_3_3"
	"DisplacementFieldTransform_double_2_2"
	"DisplacementFieldTransform_double_3_3"
	"DisplacementFieldTransform_float_2_2"
	"DisplacementFieldTransform_float_3_3"
	"Euler2DTransform_double_2_2"
	"Euler2DTransform_float_2_2"
	"Euler3DTransform_double_3_3"
	"Euler3DTransform_float_3_3"
	"FixedCenterOfRotationAffineTransform_double_3_3"
	"FixedCenterOfRotationAffineTransform_float_3_3"
	"GaussianExponentialDiffeomorphicTransform_double_2_2"
	"GaussianExponentialDiffeomorphicTransform_double_3_3"
	"GaussianExponentialDiffeomorphicTransform_float_2_2"
	"GaussianExponentialDiffeomorphicTransform_float_3_3"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_double_2_2"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_double_3_3"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_float_2_2"
	"GaussianSmoothingOnUpdateDisplacementFieldTransform_float_3_3"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_double_2_2"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_double_3_3"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_float_2_2"
	"GaussianSmoothingOnUpdateTimeVaryingVelocityFieldTransform_float_3_3"
	"IdentityTransform_double_2_2"
	"IdentityTransform_double_3_3"
	"IdentityTransform_double_4_4"
	"IdentityTransform_float_2_2"
	"IdentityTransform_float_3_3"
	"IdentityTransform_float_4_4"
	"QuaternionRigidTransform_double_3_3"
	"QuaternionRigidTransform_float_3_3"
	"Rigid2DTransform_double_2_2"
	"Rigid2DTransform_float_2_2"
	"Rigid3DPerspectiveTransform_double_3_2"
	"Rigid3DPerspectiveTransform_float_3_2"
	"Rigid3DTransform_double_3_3"
	"Rigid3DTransform_float_3_3"
	"ScalableAffineTransform_double_3_3"
	"ScalableAffineTransform_float_3_3"
	"ScaleLogarithmicTransform_double_3_3"
	"ScaleLogarithmicTransform_float_3_3"
	"ScaleSkewVersor3DTransform_double_3_3"
	"ScaleSkewVersor3DTransform_float_3_3"
	"ScaleTransform_double_2_2"
	"ScaleTransform_double_3_3"
	"ScaleTransform_double_4_4"
	"ScaleTransform_float_2_2"
	"ScaleTransform_float_3_3"
	"ScaleTransform_float_4_4"
	"ScaleVersor3DTransform_double_3_3"
	"ScaleVersor3DTransform_float_3_3"
	"Similarity2DTransform_double_2_2"
	"Similarity2DTransform_float_2_2"
	"Similarity3DTransform_double_3_3"
	"Similarity3DTransform_float_3_3"
	"TimeVaryingBSplineVelocityFieldTransform_double_2_2"
	"TimeVaryingBSplineVelocityFieldTransform_double_3_3"
	"TimeVaryingBSplineVelocityFieldTransform_float_2_2"
	"TimeVaryingBSplineVelocityFieldTransform_float_3_3"
	"TimeVaryingVelocityFieldTransform_double_2_2"
	"TimeVaryingVelocityFieldTransform_double_3_3"
	"TimeVaryingVelocityFieldTransform_float_2_2"
	"TimeVaryingVelocityFieldTransform_float_3_3"
	"TranslationTransform_double_2_2"
	"TranslationTransform_double_3_3"
	"TranslationTransform_double_4_4"
	"TranslationTransform_float_2_2"
	"TranslationTransform_float_3_3"
	"TranslationTransform_float_4_4"
	"VelocityFieldTransform_double_2_2"
	"VelocityFieldTransform_double_3_3"
	"VelocityFieldTransform_float_2_2"
	"VelocityFieldTransform_float_3_3"
	"VersorRigid3DTransform_double_3_3"
	"VersorRigid3DTransform_float_3_3"
	"VersorTransform_double_3_3"
	"VersorTransform_float_3_3"



</code></pre>
<p><strong>Resample Scalar/Vector/DWI Volume</strong> output:</p>
<pre><code class="lang-auto">Resample Scalar/Vector/DWI Volume standard error:


itk::ExceptionObject (0000009A75CFA940)
Location: "unknown" 
File: C:\gs1\ITK\Modules\IO\TransformBase\src\itkTransformIOBase.cxx
Line: 62
Description: itk::ERROR: itk::ERROR: HDF5TransformIOTemplate(00000283F074E500): Could not create an instance of "InverseThinPlateSplineKernelTransform_double_3_3"
The usual cause of this error is not registering the transform with TransformFactory
Currently registered Transforms: 




</code></pre>

---

## Post #2 by @pieper (2022-05-02 17:50 UTC)

<p>Yes, probably the ITK code doesn’t work with the thin plate spline.</p>
<p>A couple options: (1) you could export the transform as a grid transform using the button in the Landmark Registration interface or (2) you could import the labelmap into a segmentation and the it should harden using nearest neighbor.  Probably the second option is less lossy, but either should work.</p>

---

## Post #3 by @giovform (2022-05-02 20:25 UTC)

<p>Used the second solution and it worked. Thanks <a class="mention" href="/u/pieper">@pieper</a> .</p>

---

## Post #4 by @lassoan (2022-05-04 01:30 UTC)

<p>FYI, this error occurs because unlike VTK, ITK unfortunately does not support inverse transforms. <code>InverseThinPlateSplineKernelTransform</code> is an inverse transform type that Slicer introduced so that ITK transform file can store an inverse transform (so that you can load an ITK transform, invert it in Transforms module, then save it, without any data loss). ITK cannot do anything else with this file other than read/write it.</p>
<p>If you want to ITK to apply an inverse transform, you can convert it to a grid transform in Transforms module. It is a lossy conversion, because the displacement values are computed on a specific voxel grid.</p>

---
