# Error Using nVIDIA AIAA - Prostate Model 

**Topic ID**: 20367
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/error-using-nvidia-aiaa-prostate-model/20367

---

## Post #1 by @mario.boccia1992 (2021-10-26 18:55 UTC)

<p>Dear all,</p>
<p>Unfortunately I’m facing issue using nVIDIA AIAA module: prostate MRI segmentation.</p>
<p>Running the AI I get this error:</p>
<p>" Traceback (most recent call last):</p>
<p>File “C:/Users/M/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 410, in onClickSegmentation</p>
<p>extreme_points, result_file = self.logic.segmentation(in_file, session_id, model)</p>
<p>File “C:/Users/M/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py”, line 1092, in segmentation</p>
<p>session_id=session_id,</p>
<p>File “C:\Users\M\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\NvidiaAIAssistedAnnotation\lib\Slicer-4.11\qt-scripted-modules\NvidiaAIAAClientAPI\client_api.py”, line 389, in inference</p>
<p>raise AIAAException(AIAAError.SERVER_ERROR, ‘Status: {}; Response: {}’.format(status, form))</p>
<p>NvidiaAIAAClientAPI.client_api.AIAAException: (3, ‘Status: 500; Response: b’{“error”:{“message”:[],“type”:“InferenceServerException”},“success”:false}\n’’) "</p>
<p>Please, do you have any clues?</p>
<p>Thank you very much!</p>
<p>M.</p>

---

## Post #2 by @lassoan (2021-10-28 04:33 UTC)

<p>You can find more detailed server logs here: <a href="http://perklabseg.asuscomm.com:5000/logs/">http://perklabseg.asuscomm.com:5000/logs/</a></p>
<pre><code class="lang-auto">[2021-10-28 04:20:36] [INFO] (aiaa.www.api.api_v1) - ===============================================================================
[2021-10-28 04:20:36] [INFO] (aiaa.www.api.api_v1) - API_v1:: /v1/inference (model: clara_pt_prostate_mri_segmentation)
[2021-10-28 04:20:36] [INFO] (aiaa.www.api.api_v1) - ===============================================================================
[2021-10-28 04:20:37] [INFO] (aiaa.inference.inference_utils) - PRE - Run Transforms
[2021-10-28 04:20:37] [INFO] (aiaa.inference.inference_utils) - PRE - Input Keys: dict_keys(['image', 'image_path', 'params', 'transform_meta'])
[2021-10-28 04:20:37] [INFO] (aiaa.inference.inference_utils) - PRE - Transform (LoadImaged): Time: 0.0883; image: (512, 512, 27)
[2021-10-28 04:20:37] [INFO] (aiaa.inference.inference_utils) - PRE - Transform (AddChanneld): Time: 0.0000; image: (1, 512, 512, 27)
[2021-10-28 04:20:37] [INFO] (aiaa.inference.inference_utils) - PRE - Transform (Spacingd): Time: 0.1367; image: (1, 161, 161, 79)
[2021-10-28 04:20:37] [INFO] (aiaa.inference.inference_utils) - PRE - Transform (ScaleIntensityRanged): Time: 0.0055; image: (1, 161, 161, 79)
[2021-10-28 04:20:37] [INFO] (aiaa.inference.triton_inference) - Input  Shape: (1, 1, 161, 161, 79), Type: ndarray
[2021-10-28 04:20:37] [ERROR] (aiaa.www.api.api_v1) - unexpected shape for input 'INPUT__0' for model 'clara_pt_prostate_mri_segmentation'. Expected [-1,2,192,192,64], got [1,1,192,192,64]
[2021-10-28 04:20:37] Traceback (most recent call last):
[2021-10-28 04:20:37]   File "/opt/conda/lib/python3.8/site-packages/flask/app.py", line 1950, in full_dispatch_request
[2021-10-28 04:20:37]     rv = self.dispatch_request()
[2021-10-28 04:20:37]   File "/opt/conda/lib/python3.8/site-packages/flask/app.py", line 1936, in dispatch_request
[2021-10-28 04:20:37]     return self.view_functions[rule.endpoint](**req.view_args)
[2021-10-28 04:20:37]   File "www/api/api_v1.py", line 368, in api_v1_inference
[2021-10-28 04:20:37]   File "www/api/api_v1.py", line 255, in run_inference
[2021-10-28 04:20:37]   File "www/api/api_v1.py", line 168, in run_infer
[2021-10-28 04:20:37]   File "actions/inference_engine.py", line 80, in run
[2021-10-28 04:20:37]   File "actions/inference_engine.py", line 141, in _run_inference
[2021-10-28 04:20:37]   File "inference/triton_inference.py", line 74, in inference
[2021-10-28 04:20:37]   File "inference/triton/inference.py", line 260, in sw_inference
[2021-10-28 04:20:37]   File "/opt/conda/lib/python3.8/site-packages/tritonclient/http/__init__.py", line 1286, in get_result
[2021-10-28 04:20:37]     _raise_if_error(response)
[2021-10-28 04:20:37]   File "/opt/conda/lib/python3.8/site-packages/tritonclient/http/__init__.py", line 63, in _raise_if_error
[2021-10-28 04:20:37]     raise error
[2021-10-28 04:20:37] tritonclient.utils.InferenceServerException: unexpected shape for input 'INPUT__0' for model 'clara_pt_prostate_mri_segmentation'. Expected [-1,2,192,192,64], got [1,1,192,192,64]
</code></pre>
<p>The prostate model probably fails because <a href="https://ngc.nvidia.com/catalog/models/nvidia:med:clara_pt_prostate_mri_segmentation">it requires two input images (T2 and ADC)</a> and most likely the AIAA client that NVidia developers created for Slicer does not support this yet.</p>
<p>Please submit a feature request to NVidia developers at <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues" class="inline-onebox">Issues · NVIDIA/ai-assisted-annotation-client · GitHub</a> and copy the link here.</p>

---

## Post #3 by @mario.boccia1992 (2021-10-28 12:31 UTC)

<p>Dear Andras,</p>
<p>I successfully created a new issue regarding this topic on the Github project.</p>
<p>Here you can find the link to the issue raised: <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/issues/92" rel="noopener nofollow ugc">Slicer 3D - Error Using nVIDIA AIAA - Prostate Model · Issue #92 · NVIDIA/ai-assisted-annotation-client (github.com)</a>.</p>

---
