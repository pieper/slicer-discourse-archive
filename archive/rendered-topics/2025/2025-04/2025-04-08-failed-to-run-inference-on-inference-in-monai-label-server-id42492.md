---
topic_id: 42492
title: "Failed To Run Inference On Inference In Monai Label Server"
date: 2025-04-08
url: https://discourse.slicer.org/t/42492
---

# Failed to run inference on inference in MONAI Label Server

**Topic ID**: 42492
**Date**: 2025-04-08
**URL**: https://discourse.slicer.org/t/failed-to-run-inference-on-inference-in-monai-label-server/42492

---

## Post #1 by @e.baldelomar (2025-04-08 20:09 UTC)

<p>Hello,</p>
<p>I’ve been trying to get acquainted with MONAI Label. I got it installed and running. I’m trying to test out the case 2 example in the Quickstart documentation (<a href="https://docs.monai.io/projects/label/en/latest/quickstart.html#use-case-2-bundle-with-customized-scripts-for-renal-substructure-segmentation" class="inline-onebox" rel="noopener nofollow ugc">Quickstart — MONAI Label 0.8.5 Documentation</a>).</p>
<p>I’m apparently able to connect; load the test data up to the server; and select the specific model/bundle (renalStructures_UNEST_segmentation). When I click ‘Run’ I get an error of</p>
<blockquote>
<p>‘Failed to run inference in MONAI Label Server. Message: Status: 500; Response: Internal Server Error’</p>
</blockquote>
<p>Below are1) details from the error and 2) Log. Any help is greatly appreciated!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cb10916cc8e0ffac949f4e78e9f3f4052e8b546.jpeg" data-download-href="/uploads/short-url/8ETWAKKeGCEN9y2nR26RvGFnPHU.jpeg?dl=1" title="Screenshot 2025-04-08 at 2.40.02 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cb10916cc8e0ffac949f4e78e9f3f4052e8b546_2_690x337.jpeg" alt="Screenshot 2025-04-08 at 2.40.02 PM" data-base62-sha1="8ETWAKKeGCEN9y2nR26RvGFnPHU" width="690" height="337" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cb10916cc8e0ffac949f4e78e9f3f4052e8b546_2_690x337.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cb10916cc8e0ffac949f4e78e9f3f4052e8b546_2_1035x505.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cb10916cc8e0ffac949f4e78e9f3f4052e8b546_2_1380x674.jpeg 2x" data-dominant-color="9C9BA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-04-08 at 2.40.02 PM</span><span class="informations">1920×939 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol>
<li></li>
</ol>
<blockquote>
<p>Traceback (most recent call last):<br>
File “/bmrc-homes/nmrgrp/nmr141/Slicer-5.8.1-linux-amd64/slicer.org/Extensions-33241/MONAILabel/lib/Slicer-5.8/qt-scripted-modules/MONAILabel.py”, line 1565, in onClickSegmentation<br>
result_file, params = self.logic.infer(model, image_file, params, session_id=self.getSessionId())<br>
File “/bmrc-homes/nmrgrp/nmr141/Slicer-5.8.1-linux-amd64/slicer.org/Extensions-33241/MONAILabel/lib/Slicer-5.8/qt-scripted-modules/MONAILabel.py”, line 2397, in infer<br>
result_file, params = client.infer(model, image_in, params, label_in, file, session_id)<br>
File “/bmrc-homes/nmrgrp/nmr141/Slicer-5.8.1-linux-amd64/slicer.org/Extensions-33241/MONAILabel/lib/Slicer-5.8/qt-scripted-modules/MONAILabelLib/client.py”, line 344, in infer<br>
raise MONAILabelClientException(<br>
MONAILabelLib.client.MONAILabelClientException: (1, ‘Status: 500; Response: Internal Server Error’)</p>
</blockquote>
<ol start="2">
<li></li>
</ol>
<blockquote>
<p>[nmr141@bmrs117 ~]$ monailabel start_server --app monaibundle --studies Task09_Spleen/imagesTr --conf models renalStructures_UNEST_segmentation<br>
Using PYTHONPATH=/bmr207/nmrgrp/nmr141:</p>
<p>/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/ignite/handlers/checkpoint.py:17: DeprecationWarning: <code>TorchScript</code> support for functional optimizers is deprecated and will be removed in a future PyTorch release. Consider using the <code>torch.compile</code> optimizer instead.<br>
from torch.distributed.optim import ZeroRedundancyOptimizer<br>
[2025-04-08 14:35:32,524] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: version = False<br>
[2025-04-08 14:35:32,524] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: app = /bmrc-homes/nmrgrp/nmr141/monaibundle<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: studies = /bmrc-homes/nmrgrp/nmr141/Task09_Spleen/imagesTr<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: verbose = INFO<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: conf = [[‘models’, ‘renalStructures_UNEST_segmentation’]]<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: host = 0.0.0.0<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: port = 8000<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: uvicorn_app = monailabel.app:app<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: ssl_keyfile = None<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: ssl_certfile = None<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: ssl_keyfile_password = None<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: ssl_ca_certs = None<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: workers = None<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: limit_concurrency = None<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: access_log = False<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: root_path = /<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: log_level = info<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: log_config = None<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: dryrun = False<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:285) - USING:: action = start_server<br>
[2025-04-08 14:35:32,525] [2026107] [MainThread] [INFO] (<strong>main</strong>:296) -<br>
Allow Origins: [‘<em>‘]<br>
[2025-04-08 14:35:33,599] [2026107] [MainThread] [INFO] (uvicorn.error:82) - Started server process [2026107]<br>
[2025-04-08 14:35:33,599] [2026107] [MainThread] [INFO] (uvicorn.error:48) - Waiting for application startup.<br>
[2025-04-08 14:35:33,599] [2026107] [MainThread] [INFO] (monailabel.interfaces.utils.app:37) - Initializing App from: /bmrc-homes/nmrgrp/nmr141/monaibundle; studies: /bmrc-homes/nmrgrp/nmr141/Task09_Spleen/imagesTr; conf: {‘models’: ‘renalStructures_UNEST_segmentation’}<br>
[2025-04-08 14:35:33,656] [2026107] [MainThread] [INFO] (monailabel.utils.others.class_utils:57) - Subclass for MONAILabelApp Found: &lt;class ‘main.MyApp’&gt;<br>
[2025-04-08 14:36:35,828] [2026107] [MainThread] [INFO] (monailabel.utils.others.generic:315) - +++ Adding Bundle from Zoo: renalStructures_UNEST_segmentation =&gt; /bmrc-homes/nmrgrp/nmr141/monaibundle/model/renalStructures_UNEST_segmentation<br>
[2025-04-08 14:36:35,829] [2026107] [MainThread] [INFO] (monailabel.utils.others.generic:375) - +++ Using Bundle Models: [‘renalStructures_UNEST_segmentation’]<br>
[2025-04-08 14:36:35,829] [2026107] [MainThread] [INFO] (monailabel.interfaces.app:135) - Init Datastore for: /bmrc-homes/nmrgrp/nmr141/Task09_Spleen/imagesTr<br>
[2025-04-08 14:36:35,829] [2026107] [MainThread] [INFO] (monailabel.datastore.local:130) - Auto Reload: True; Extensions: [’</em>.nii.gz’, ‘<em>.nii’, '</em>.nrrd’, ‘<em>.jpg’, '</em>.png’, ‘<em>.tif’, '</em>.svs’, ‘*.xml’]<br>
[2025-04-08 14:36:35,837] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_56 =&gt; spleen_56.nii.gz<br>
[2025-04-08 14:36:35,837] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_6 =&gt; spleen_6.nii.gz<br>
[2025-04-08 14:36:35,837] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_62 =&gt; spleen_62.nii.gz<br>
[2025-04-08 14:36:35,837] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_2 =&gt; spleen_2.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_3 =&gt; spleen_3.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_31 =&gt; spleen_31.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_24 =&gt; spleen_24.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_13 =&gt; spleen_13.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_14 =&gt; spleen_14.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_44 =&gt; spleen_44.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_27 =&gt; spleen_27.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_52 =&gt; spleen_52.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_17 =&gt; spleen_17.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_46 =&gt; spleen_46.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_26 =&gt; spleen_26.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_9 =&gt; spleen_9.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_16 =&gt; spleen_16.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_21 =&gt; spleen_21.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_49 =&gt; spleen_49.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_22 =&gt; spleen_22.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_41 =&gt; spleen_41.nii.gz<br>
[2025-04-08 14:36:35,838] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_40 =&gt; spleen_40.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_29 =&gt; spleen_29.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_38 =&gt; spleen_38.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_32 =&gt; spleen_32.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_28 =&gt; spleen_28.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_60 =&gt; spleen_60.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_45 =&gt; spleen_45.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_10 =&gt; spleen_10.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_33 =&gt; spleen_33.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_19 =&gt; spleen_19.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_25 =&gt; spleen_25.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_61 =&gt; spleen_61.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_53 =&gt; spleen_53.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_20 =&gt; spleen_20.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_12 =&gt; spleen_12.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_47 =&gt; spleen_47.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_18 =&gt; spleen_18.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_8 =&gt; spleen_8.nii.gz<br>
[2025-04-08 14:36:35,839] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_63 =&gt; spleen_63.nii.gz<br>
[2025-04-08 14:36:35,840] [2026107] [MainThread] [INFO] (monailabel.datastore.local:594) - Adding New Image: spleen_59 =&gt; spleen_59.nii.gz<br>
[2025-04-08 14:36:35,844] [2026107] [MainThread] [INFO] (monailabel.datastore.local:577) - Invalidate count: 41<br>
[2025-04-08 14:36:35,848] [2026107] [MainThread] [INFO] (monailabel.datastore.local:151) - Start observing external modifications on datastore (AUTO RELOAD)<br>
[2025-04-08 14:36:39,154] [2026107] [MainThread] [INFO] (main:63) - +++ Adding Inferer:: renalStructures_UNEST_segmentation =&gt; &lt;monailabel.tasks.infer.bundle.BundleInferTask object at 0x7f8ba763fe50&gt;<br>
[2025-04-08 14:36:39,155] [2026107] [MainThread] [INFO] (main:77) - +++ Adding Trainer:: renalStructures_UNEST_segmentation =&gt; &lt;monailabel.tasks.train.bundle.BundleTrainTask object at 0x7f8ba7ab65b0&gt;<br>
[2025-04-08 14:36:39,155] [2026107] [MainThread] [INFO] (main:87) - Active Learning Strategies:: [‘random’, ‘first’]<br>
[2025-04-08 14:36:39,155] [2026107] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /bmr207/nmrgrp/nmr141/.cache/monailabel/sessions<br>
[2025-04-08 14:36:39,156] [2026107] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600<br>
[2025-04-08 14:36:39,156] [2026107] [MainThread] [INFO] (monailabel.interfaces.app:469) - App Init - completed<br>
[2025-04-08 14:36:39,156] [timeloop] [INFO] Starting Timeloop..<br>
[2025-04-08 14:36:39,156] [2026107] [MainThread] [INFO] (timeloop:60) - Starting Timeloop..<br>
[2025-04-08 14:36:39,157] [timeloop] [INFO] Registered job &lt;function MONAILabelApp.on_init_complete..run_scheduler at 0x7f8ba5f35a60&gt;<br>
[2025-04-08 14:36:39,157] [2026107] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete..run_scheduler at 0x7f8ba5f35a60&gt;<br>
[2025-04-08 14:36:39,157] [timeloop] [INFO] Timeloop now started. Jobs will run based on the interval set<br>
[2025-04-08 14:36:39,157] [2026107] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set<br>
[2025-04-08 14:36:39,157] [2026107] [MainThread] [INFO] (uvicorn.error:62) - Application startup complete.<br>
[2025-04-08 14:36:39,157] [2026107] [MainThread] [INFO] (uvicorn.error:214) - Uvicorn running on <a href="http://0.0.0.0:8000" rel="noopener nofollow ugc">http://0.0.0.0:8000</a> (Press CTRL+C to quit)<br>
Switch to module:  “MONAILabel”<br>
“Volume” Reader has successfully read the file “/bmrc-homes/nmrgrp/nmr141/Task09_Spleen/imagesTr/spleen_10.nii.gz” “[0.65s]”<br>
“Text file” Reader has successfully read the file “/bmrc-homes/nmrgrp/nmr141/Task09_Spleen/imagesTr/datastore_v2.json” “[0.00s]”<br>
[2025-04-08 14:39:32,205] [2026107] [MainThread] [INFO] (monailabel.endpoints.datastore:68) - Image: spleen_10; File: UploadFile(filename=‘/tmp/Slicer-nmr141/slicer-monai-label2025-04-08_14+38+59.980/tmp4i5jkyde.nii.gz’, size=15682060, headers=Headers({‘content-disposition’: ‘form-data; name=“file”; filename=“/tmp/Slicer-nmr141/slicer-monai-label2025-04-08_14+38+59.980/tmp4i5jkyde.nii.gz”’, ‘content-type’: ‘application/octet-stream’})); params: {“client_id”: “user-xyz”}<br>
[2025-04-08 14:39:32,217] [2026107] [MainThread] [INFO] (monailabel.datastore.local:439) - Adding Image: spleen_10 =&gt; /tmp/tmp8j3am7z9.nii.gz<br>
[2025-04-08 14:39:41,855] [2026107] [MainThread] [INFO] (monailabel.endpoints.infer:161) - Infer Request: {‘model’: ‘renalStructures_UNEST_segmentation’, ‘image’: ‘spleen_10’, ‘device’: ‘Tesla V100S-PCIE-32GB:0’, ‘model_filename’: ‘model.pt’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’}<br>
[2025-04-08 14:39:41,856] [2026107] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:277) - Infer Request (final): {‘device’: ‘cuda:0’, ‘model_filename’: ‘model.pt’, ‘model’: ‘renalStructures_UNEST_segmentation’, ‘image’: ‘/bmrc-homes/nmrgrp/nmr141/Task09_Spleen/imagesTr/spleen_10.nii.gz’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’, ‘description’: ‘A transformer-based model for renal segmentation from CT image’}<br>
[2025-04-08 14:39:41,861] [2026107] [MainThread] [INFO] (monailabel.utils.others.class_utils:33) - Remove/Reload previous Modules: [‘scripts’, ‘scripts.networks’, ‘scripts.networks.nest’, ‘scripts.networks.nest.utils’, ‘scripts.networks.nest_transformer_3D’, ‘scripts.networks.patchEmbed3D’, ‘scripts.networks.unest’, ‘scripts.networks.unest_block’]<br>
[2025-04-08 14:39:41,862] [2026107] [MainThread] [ERROR] (uvicorn.error:412) - Exception in ASGI application<br>
Traceback (most recent call last):<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/uvicorn/protocols/http/h11_impl.py”, line 407, in run_asgi<br>
result = await app(  # type: ignore[func-returns-value]<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/uvicorn/middleware/proxy_headers.py”, line 69, in <strong>call</strong><br>
return await self.app(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/fastapi/applications.py”, line 1054, in <strong>call</strong><br>
await super().<strong>call</strong>(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/applications.py”, line 123, in <strong>call</strong><br>
await self.middleware_stack(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/middleware/errors.py”, line 186, in <strong>call</strong><br>
raise exc<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/middleware/errors.py”, line 164, in <strong>call</strong><br>
await self.app(scope, receive, _send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/middleware/cors.py”, line 85, in <strong>call</strong><br>
await self.app(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/middleware/exceptions.py”, line 65, in <strong>call</strong><br>
await wrap_app_handling_exceptions(self.app, conn)(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/_exception_handler.py”, line 64, in wrapped_app<br>
raise exc<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/_exception_handler.py”, line 53, in wrapped_app<br>
await app(scope, receive, sender)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/routing.py”, line 756, in <strong>call</strong><br>
await self.middleware_stack(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/routing.py”, line 776, in app<br>
await route.handle(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/routing.py”, line 297, in handle<br>
await self.app(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/routing.py”, line 77, in app<br>
await wrap_app_handling_exceptions(app, request)(scope, receive, send)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/_exception_handler.py”, line 64, in wrapped_app<br>
raise exc<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/_exception_handler.py”, line 53, in wrapped_app<br>
await app(scope, receive, sender)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/starlette/routing.py”, line 72, in app<br>
response = await func(request)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/fastapi/routing.py”, line 278, in app<br>
raw_response = await run_endpoint_function(<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/fastapi/routing.py”, line 191, in run_endpoint_function<br>
return await dependant.call(**values)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monailabel/endpoints/infer.py”, line 180, in api_run_inference<br>
return run_inference(background_tasks, model, image, session_id, params, file, label, output)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monailabel/endpoints/infer.py”, line 162, in run_inference<br>
result = instance.infer(request)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monailabel/interfaces/app.py”, line 307, in infer<br>
result_file_name, result_json = task(request)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monailabel/tasks/infer/basic_infer.py”, line 294, in <strong>call</strong><br>
pre_transforms = self.pre_transforms(data)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monailabel/tasks/infer/bundle.py”, line 193, in pre_transforms<br>
c = self.bundle_config.get_parsed_content(k, instantiate=True)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monai/bundle/config_parser.py”, line 290, in get_parsed_content<br>
return self.ref_resolver.get_resolved_content(id=id, **kwargs)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monai/bundle/reference_resolver.py”, line 193, in get_resolved_content<br>
return self._resolve_one_item(id=id, **kwargs)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monai/bundle/reference_resolver.py”, line 163, in _resolve_one_item<br>
self._resolve_one_item(id=d, waiting_list=waiting_list, **kwargs)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monai/bundle/reference_resolver.py”, line 171, in _resolve_one_item<br>
self.resolved_content[id] = item.instantiate() if kwargs.get(“instantiate”, True) else item<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monai/bundle/config_item.py”, line 292, in instantiate<br>
return instantiate(modname, mode, **args)<br>
File “/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monai/utils/module.py”, line 251, in instantiate<br>
raise ModuleNotFoundError(f"Cannot locate class or function path: ‘{__path}’.")<br>
ModuleNotFoundError: Cannot locate class or function path: ‘AddChanneld’.</p>
</blockquote>

---

## Post #2 by @e.baldelomar (2025-04-09 14:40 UTC)

<p>Since I have searched both the monai/ and monailabel/ folders for ‘AddChanneld’ and only things I find are commented. So I’m really lost on how to get this up and running.</p>
<blockquote>
<p>grep --include=*.{py} -rnw ‘/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/’ -e “AddChanneld”</p>
<p>/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monailabel/tasks/infer/basic_infer.py:171:                    monai.transforms.AddChanneld(keys=‘image’),<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monailabel/tasks/infer/basic_infer.py:211:                    monai.transforms.AddChanneld(keys=‘pred’),<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/tests/unit/deepedit/test_deepedit_transforms.py:16:from monai.transforms import AddChanneld<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/tests/unit/deepedit/test_deepedit_transforms.py:184:        add_ch = AddChanneld(keys=[“image”, “label”])(input_data)<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/tests/unit/deepedit/test_deepedit_transforms.py:193:        add_ch = AddChanneld(keys=[“image”, “label”])(input_data)<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/tests/unit/deepedit/test_deepedit_transforms.py:202:        add_ch = AddChanneld(keys=[“image”, “label”])(input_data)<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/tests/unit/deepedit/test_deepedit_transforms.py:211:        add_ch = AddChanneld(keys=[“image”, “label”])(input_data)<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/tests/unit/activelearning/test_epistemic.py:24:    AddChanneld,<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/tests/unit/activelearning/test_epistemic.py:73:                AddChanneld(keys),<br>
/bmr207/nmrgrp/nmr141/.local/lib/python3.8/site-packages/monai/transforms/transform.py:443:             except for example: <code>AddChanneld</code> expects (spatial_dim_1[, spatial_dim_2, …])</p>
</blockquote>
<p>The only two files that actually use ‘AddChanneld’ (not commented out) are:</p>
<ul>
<li>tests/unit/activelearning/test_epistemic.py:73</li>
<li>tests/unit/deepedit/test_deepedit_transforms.py</li>
</ul>
<p>I found this thread (<a href="https://github.com/Project-MONAI/tutorials/discussions/1686" class="inline-onebox" rel="noopener nofollow ugc">module 'monai.transforms' has no attribute 'AddChannel' · Project-MONAI/tutorials · Discussion #1686 · GitHub</a>) that talked about this AddChannel issue before but it’s not clear to me how one goes about properly editing it.</p>
<p>When checking version of things using:</p>
<blockquote>
<p>python -c “import monai; monai.config.print_config()”</p>
</blockquote>
<p>I get the following output if helpful:</p>
<blockquote>
<p>MONAI version: 1.3.2<br>
Numpy version: 1.23.4<br>
Pytorch version: 2.4.1+cu121<br>
MONAI flags: HAS_EXT = False, USE_COMPILED = False, USE_META_DICT = False<br>
MONAI rev id: 59a7211070538586369afd4a01eca0a7fe2e742e<br>
MONAI <strong>file</strong>: /bmr207/nmrgrp//.local/lib/python3.8/site-packages/monai/<strong>init</strong>.py</p>
<p>Optional dependencies:<br>
Pytorch Ignite version: 0.4.11<br>
ITK version: 5.4.3<br>
Nibabel version: 4.0.2<br>
scikit-image version: 0.21.0<br>
scipy version: 1.10.1<br>
Pillow version: 9.3.0<br>
Tensorboard version: 2.14.0<br>
gdown version: 5.2.0<br>
TorchVision version: 0.19.1+cu121<br>
tqdm version: 4.64.1<br>
lmdb version: 1.6.2<br>
psutil version: 7.0.0<br>
pandas version: 1.5.1<br>
einops version: 0.7.0<br>
transformers version: NOT INSTALLED or UNKNOWN VERSION.<br>
mlflow version: 2.17.2<br>
pynrrd version: 1.0.0<br>
clearml version: NOT INSTALLED or UNKNOWN VERSION.</p>
</blockquote>
<p>(<em>A separate question I had was that, even though I just installed this week, I thought the most stable release would be version 1.4? I’m using the ‘pip install monai’</em>)</p>

---
