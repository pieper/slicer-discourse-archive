---
topic_id: 38484
title: "Error When Using Brain Tumor Segmentation Gli Model In Monai"
date: 2024-09-22
url: https://discourse.slicer.org/t/38484
---

# Error when using Brain Tumor Segmentation(GLI)" model in MONAI Auto3DSeg

**Topic ID**: 38484
**Date**: 2024-09-22
**URL**: https://discourse.slicer.org/t/error-when-using-brain-tumor-segmentation-gli-model-in-monai-auto3dseg/38484

---

## Post #1 by @clam_keep (2024-09-22 14:04 UTC)

<p>I was try to use the “Brain Tumor Segmentation(GLI)” model in the MONAI Auto3DSEG to create segmentations on my own MRdata. It do worked once and then keep failing.<br>
These are error messages:</p>
<p>Processing started<br>
Writing input file to C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/input-volume0.nrrd<br>
Writing input file to C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/input-volume1.nrrd<br>
Writing input file to C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/input-volume2.nrrd<br>
Writing input file to C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/input-volume3.nrrd<br>
Creating segmentations with MONAIAuto3DSeg AI…<br>
Auto3DSeg command: [‘C:/Users/zcs/AppData/Local/slicer.org/Slicer 5.7.0-2024-09-19/bin/…/bin\PythonSlicer.EXE’, ‘C:/Users/zcs/AppData/Local/slicer.org/Slicer 5.7.0-2024-09-19/slicer.org/Extensions-33018/MONAIAuto3DSeg/lib/Slicer-5.7/qt-scripted-modules\Scripts\auto3dseg_segresnet_inference.py’, ‘–model-file’, ‘C:\Users\zcs\.MONAIAuto3DSeg\models\brats-gli-v1.0.0\model.pt’, ‘–image-file’, ‘C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/input-volume0.nrrd’, ‘–result-file’, ‘C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/output-segmentation.nrrd’, ‘–image-file-2’, ‘C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/input-volume1.nrrd’, ‘–image-file-3’, ‘C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/input-volume2.nrrd’, ‘–image-file-4’, ‘C:/Users/zcs/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-21_23+21+09.704/input-volume3.nrrd’]<br>
You are using <code>torch.load</code> with <code>weights_only=False</code> (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See <a href="https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models" class="inline-onebox" rel="noopener nofollow ugc">pytorch/SECURITY.md at main · pytorch/pytorch · GitHub</a> for more details). In a future release, the default value for <code>weights_only</code> will be flipped to <code>True</code>. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via <code>torch.serialization.add_safe_globals</code>. We recommend you start setting <code>weights_only=True</code> for any use case where you don’t have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.<br>
<code>apex.normalization.InstanceNorm3dNVFuser</code> is not installed properly, use nn.InstanceNorm3d instead.<br>
Model epoch 262 metric 0.8930580615997314<br>
Using crop_foreground<br>
Using resample with  resample_resolution [1.0, 1.0, 1.0]<br>
Traceback (most recent call last):<br>
File “C:\Users\zcs\AppData\Local\slicer.org\Slicer 5.7.0-2024-09-19\lib\Python\Lib\site-packages\monai\transforms\transform.py”, line 140, in apply_transform<br>
return [_apply_transform(transform, item, unpack_items, lazy, overrides, log_stats) for item in data]<br>
File “C:\Users\zcs\AppData\Local\slicer.org\Slicer 5.7.0-2024-09-19\lib\Python\Lib\site-packages\monai\transforms\transform.py”, line 140, in <br>
return [_apply_transform(transform, item, unpack_items, lazy, overrides, log_stats) for item in data]<br>
File “C:\Users\zcs\AppData\Local\slicer.org\Slicer 5.7.0-2024-09-19\lib\Python\Lib\site-packages\monai\transforms\transform.py”, line 98, in _apply_transform<br>
return transform(data, lazy=lazy) if isinstance(transform, LazyTrait) else transform(data)<br>
File “C:\Users\zcs\AppData\Local\slicer.org\Slicer 5.7.0-2024-09-19\lib\Python\Lib\site-packages\monai\transforms\io\dictionary.py”, line 162, in <strong>call</strong><br>
data = self._loader(d[key], reader)<br>
File “C:\Users\zcs\AppData\Local\slicer.org\Slicer 5.7.0-2024-09-19\lib\Python\Lib\site-packages\monai\transforms\io\array.py”, line 282, in <strong>call</strong><br>
img_array, meta_data = reader.get_data(img)<br>
File “C:\Users\zcs\AppData\Local\slicer.org\Slicer 5.7.0-2024-09-19\lib\Python\Lib\site-packages\monai\data\image_reader.py”, line 1343, in get_data<br>
_copy_compatible_dict(header, compatible_meta)<br>
File “C:\Users\zcs\AppData\Local\slicer.org\Slicer 5.7.0-2024-09-19\lib\Python\Lib\site-packages\monai\data\image_reader.py”, line 129, in _copy_compatible_dict<br>
raise RuntimeError(<br>
RuntimeError: affine matrix of all images should be the same for channel-wise concatenation. Got [[-4.57198656e-01 -1.03385621e-01  2.71376017e-03  1.41867333e+02]<br>
[-1.01093522e-01  4.44159679e-01 -1.10584093e-01 -1.02964030e+02]<br>
[ 3.02560651e-01 -1.50380787e+00 -6.31662069e+00  3.36919582e+01]<br>
[ 0.00000000e+00  0.00000000e+00  0.00000000e+00  1.00000000e+00]] and [[-4.57248575e-01 -1.03391612e-01  2.71345400e-03  1.41872669e+02]<br>
[-1.01099258e-01  4.44208168e-01 -1.10596074e-01 -1.02986774e+02]<br>
[ 3.02538236e-01 -1.50374134e+00 -6.31632356e+00  3.36796764e+01]<br>
[ 0.00000000e+00  0.00000000e+00  0.00000000e+00  1.00000000e+00]].</p>
<p>The above exception was the direct cause of the following exception:</p>
<p>Traceback (most recent call last):<br>
Processing failed with return code 1<br>
Cleaning up temporary folder.<br>
Processing failed after 4.64 seconds.</p>
<p>Processing finished.</p>

---

## Post #2 by @pieper (2024-09-22 16:14 UTC)

<p>Probably you just need to resample them to the same geometry using the Resample Image (BRAINS) module under registration.  Use one of the volumes as the reference (probably the highest res one).</p>

---

## Post #3 by @clam_keep (2024-09-23 07:40 UTC)

<p>Thank you very much for the help. Your suggestions were very effective！</p>

---
