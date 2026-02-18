# Voxel-based radiomics crash

**Topic ID**: 19385
**Date**: 2021-08-27
**URL**: https://discourse.slicer.org/t/voxel-based-radiomics-crash/19385

---

## Post #1 by @Guglielmo_Baccani (2021-08-27 08:59 UTC)

<p>Hi everyone,</p>
<p>I would like extract voxel-based features from a CT volume within a labelmap.<br>
I am able to extract segment-based feature but when when I try to compute voxel-based ones 3D Slicer crashes.</p>
<p>To reproduce the problem I load the CT volume and the labelmap downloadable from the following link.<br>
<a href="https://drive.google.com/drive/folders/1y6eD2EAsd8guWLX6QJkJgClTHDGCpY-q?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1y6eD2EAsd8guWLX6QJkJgClTHDGCpY-q?usp=sharing</a><br>
Then I copy the following code directly in the python interactor</p>
<pre><code class="lang-auto">from radiomics.featureextractor import RadiomicsFeatureExtractor
import six
import sitkUtils

inputVolumeNode = getNode('/path/to/CT_volume.nrrd')
inputImage = sitkUtils.PullVolumeFromSlicer(inputVolumeNode)
inputLabelMaskNode = getNode('/path/to/Candidate_lesions-label.nrrd')
inputMask = sitkUtils.PullVolumeFromSlicer(inputLabelMaskNode)

parameter_file = '/path/to/param_sk_modif.yaml'
extractor = RadiomicsFeatureExtractor(parameter_file)

"""
the following works but is not what I need
"""
result = extractor.execute(inputImage, inputMask)
for key, val in six.iteritems(result):
  print("\t%s: %s" %(key, val))

"""
the following crashes at the next line
"""
result = extractor.execute(inputImage, inputMask, voxelBased=True)
for key, val in six.iteritems(result):
  if isinstance(val, sitk.Image):  # Feature map
    sitk.WriteImage(val, key + '.nrrd', True)
    print("Stored feature %s in %s" % (key, key + ".nrrd"))
  else:  # Diagnostic information
    print("\t%s: %s" %(key, val))</code></pre>
<p>Any suggestion for the reason of the crash? I tried to check the log file but no errors were reported.<br>
Thanks!</p>

---

## Post #2 by @lassoan (2021-09-01 04:36 UTC)

<p>The application does not crash, just voxel-based computation seem to take much longer. If you wait a couple of minutes then it completes and you can get the results without any problems:</p>
<pre><code class="lang-python">&gt;&gt;&gt; result = extractor.execute(inputImage, inputMask, voxelBased=True)
&gt;&gt;&gt; import SimpleITK as sitk
&gt;&gt;&gt; for key, val in six.iteritems(result):
...   if isinstance(val, sitk.Image):  # Feature map
...     sitk.WriteImage(val, key + '.nrrd', True)
...     print("Stored feature %s in %s" % (key, key + ".nrrd"))
...   else:  # Diagnostic information
...     print("\t%s: %s" %(key, val))
... 
	diagnostics_Versions_PyRadiomics: v3.0.1.post4+gad5b2de
	diagnostics_Versions_Numpy: 1.19.5
	diagnostics_Versions_SimpleITK: 2.1.0
	diagnostics_Versions_PyWavelet: 1.1.1
	diagnostics_Versions_Python: 3.6.7
	diagnostics_Configuration_Settings: {'minimumROIDimensions': 2, 'minimumROISize': None, 'normalize': False, 'normalizeScale': 1, 'removeOutliers': None, 'resampledPixelSpacing': None, 'interpolator': 'sitkBSpline', 'preCrop': False, 'padDistance': 5, 'distances': [1], 'force2D': True, 'force2Ddimension': 0, 'resegmentRange': None, 'label': 1, 'additionalInfo': True, 'binWidth': 25, 'kernelRadius': 3, 'maskedKernel': True, 'voxelBatch': 10000, 'voxelBased': True}
	diagnostics_Configuration_EnabledImageTypes: {'Original': {}}
	diagnostics_Image-original_Hash: 44656800db89afe17c288db37945e97bb623edb9
	diagnostics_Image-original_Dimensionality: 3D
	diagnostics_Image-original_Spacing: (0.7519531249999999, 0.7519531249999999, 3.000000000000002)
	diagnostics_Image-original_Size: (512, 512, 99)
	diagnostics_Image-original_Mean: -555.9123982901525
	diagnostics_Image-original_Minimum: -1024.0
	diagnostics_Image-original_Maximum: 2650.0
	diagnostics_Mask-original_Hash: dc1569ae1b492c8be8a5b67588c693b33e32b3af
	diagnostics_Mask-original_Spacing: (0.7519531249999999, 0.7519531249999999, 3.000000000000002)
	diagnostics_Mask-original_Size: (512, 512, 99)
	diagnostics_Mask-original_BoundingBox: (65, 89, 8, 397, 289, 85)
	diagnostics_Mask-original_VoxelNum: 4001652
	diagnostics_Mask-original_VolumeNum: 1697
	diagnostics_Mask-original_CenterOfMassIndex: (268.67997716942904, 241.2958982940046, 37.42047634327023)
	diagnostics_Mask-original_CenterOfMass: (10.910725019980845, -135.68081866564106, -453.23857097018913)
Stored feature original_firstorder_Skewness in original_firstorder_Skewness.nrrd
&gt;&gt;&gt; 
</code></pre>

---
