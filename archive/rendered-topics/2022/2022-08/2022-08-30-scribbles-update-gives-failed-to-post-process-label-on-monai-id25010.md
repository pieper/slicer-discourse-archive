---
topic_id: 25010
title: "Scribbles Update Gives Failed To Post Process Label On Monai"
date: 2022-08-30
url: https://discourse.slicer.org/t/25010
---

# Scribbles update gives "Failed to post process label on MONAI Label Server using Histogram+GraphCut" error

**Topic ID**: 25010
**Date**: 2022-08-30
**URL**: https://discourse.slicer.org/t/scribbles-update-gives-failed-to-post-process-label-on-monai-label-server-using-histogram-graphcut-error/25010

---

## Post #1 by @lukasvanderstricht (2022-08-30 17:51 UTC)

<p>Hi,</p>
<p>I am working in Windows and I was able to install MONAILabel and run the exemplary server with the radiology app and the Task09_Spleen dataset.</p>
<p>I am able to see the images in 3D Slicer and everything seems normal.<br>
When I draw some scribbles and click <em>Update</em> in the Scribbles tab, I get the following error:</p>
<p><strong>Failed to post process label on MONAI Label Server using Histogram+GraphCut</strong> (see below)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c5b0f3ea51864dca0f85055d243940c636e9454a.png" alt="image" data-base62-sha1="scRbeSPRG5FCRTqQ9klZNBlgGvM" width="496" height="113"></p>
<p>The details of this error are as follows:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “C:/Users/lukas/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabel.py”, line 1867, in onUpdateScribbles<br>
result_file, params = self.logic.infer(<br>
File “C:/Users/lukas/AppData/Local/NA-MIC/Slicer 5.0.3/NA-MIC/Extensions-30893/MONAILabel/lib/Slicer-5.0/qt-scripted-modules/MONAILabel.py”, line 2152, in infer<br>
result_file, params = client.infer(model, image_in, params, label_in, file, session_id)<br>
File “C:\Users\lukas\AppData\Local\NA-MIC\Slicer 5.0.3\NA-MIC\Extensions-30893\MONAILabel\lib\Slicer-5.0\qt-scripted-modules\MONAILabelLib\client.py”, line 192, in infer<br>
raise MONAILabelException(<br>
MONAILabelLib.client.MONAILabelException: (2, “Status: 500; Response: b’Internal Server Error’”)</p>
</blockquote>
<p>The logs are included below:</p>
<blockquote>
<p>[2022-08-30 06:45:27,691] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: /home/lukas/radiology; studies: /home/lukas/Task09_Spleen/imagesTr; conf: {‘models’: ‘deepedit’}<br>
[2022-08-30 06:45:27,752] [8015] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for MONAILabelApp Found: &lt;class ‘main.MyApp’&gt;<br>
[2022-08-30 06:45:27,778] [8015] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation.Segmentation’&gt;<br>
[2022-08-30 06:45:27,779] [8015] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_3d.Deepgrow3D’&gt;<br>
[2022-08-30 06:45:27,790] [8015] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepedit.DeepEdit’&gt;<br>
[2022-08-30 06:45:27,792] [8015] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation_spleen.SegmentationSpleen’&gt;<br>
[2022-08-30 06:45:27,794] [8015] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_2d.Deepgrow2D’&gt;<br>
[2022-08-30 06:45:27,794] [8015] [MainThread] [INFO] (main:83) - +++ Adding Model: deepedit =&gt; lib.configs.deepedit.DeepEdit<br>
[2022-08-30 06:45:27,794] [8015] [MainThread] [INFO] (monailabel.utils.others.generic:171) - Downloading resource: /home/lukas/radiology/model/pretrained_deepedit_dynunet.pt from <a href="https://github.com/Project-MONAI/MONAILabel/releases/download/data/deepedit_dynunet_multilabel.pt" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/releases/download/data/deepedit_dynunet_multilabel.pt</a><br>
[2022-08-30 06:45:42,148] [8015] [MainThread] [INFO] (lib.configs.deepedit:144) - EPISTEMIC Enabled: 0; Samples: 5<br>
[2022-08-30 06:45:42,149] [8015] [MainThread] [INFO] (lib.configs.deepedit:148) - TTA Enabled: 0; Samples: 5<br>
[2022-08-30 06:45:42,150] [8015] [MainThread] [INFO] (main:87) - +++ Using Models: [‘deepedit’]<br>
[2022-08-30 06:45:42,151] [8015] [MainThread] [INFO] (monailabel.interfaces.app:128) - Init Datastore for: /home/lukas/Task09_Spleen/imagesTr<br>
[2022-08-30 06:45:42,151] [8015] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: [‘<em>.nii.gz’, '</em>.nii’, ‘<em>.nrrd’, '</em>.jpg’, ‘<em>.png’, '</em>.tif’, ‘<em>.svs’, '</em>.xml’]<br>
[2022-08-30 06:45:42,153] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_63 =&gt; spleen_63.nii.gz<br>
[2022-08-30 06:45:42,153] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_8 =&gt; spleen_8.nii.gz<br>
[2022-08-30 06:45:42,153] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_20 =&gt; spleen_20.nii.gz<br>
[2022-08-30 06:45:42,154] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_22 =&gt; spleen_22.nii.gz<br>
[2022-08-30 06:45:42,154] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_25 =&gt; spleen_25.nii.gz<br>
[2022-08-30 06:45:42,154] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_28 =&gt; spleen_28.nii.gz<br>
[2022-08-30 06:45:42,154] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_56 =&gt; spleen_56.nii.gz<br>
[2022-08-30 06:45:42,154] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_6 =&gt; spleen_6.nii.gz<br>
[2022-08-30 06:45:42,155] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_40 =&gt; spleen_40.nii.gz<br>
[2022-08-30 06:45:42,155] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_41 =&gt; spleen_41.nii.gz<br>
[2022-08-30 06:45:42,155] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_33 =&gt; spleen_33.nii.gz<br>
[2022-08-30 06:45:42,155] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_45 =&gt; spleen_45.nii.gz<br>
[2022-08-30 06:45:42,155] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_31 =&gt; spleen_31.nii.gz<br>
[2022-08-30 06:45:42,156] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_60 =&gt; spleen_60.nii.gz<br>
[2022-08-30 06:45:42,156] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_3 =&gt; spleen_3.nii.gz<br>
[2022-08-30 06:45:42,156] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_16 =&gt; spleen_16.nii.gz<br>
[2022-08-30 06:45:42,156] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_52 =&gt; spleen_52.nii.gz<br>
[2022-08-30 06:45:42,157] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_12 =&gt; spleen_12.nii.gz<br>
[2022-08-30 06:45:42,157] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_19 =&gt; spleen_19.nii.gz<br>
[2022-08-30 06:45:42,157] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_26 =&gt; spleen_26.nii.gz<br>
[2022-08-30 06:45:42,157] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_47 =&gt; spleen_47.nii.gz<br>
[2022-08-30 06:45:42,157] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_32 =&gt; spleen_32.nii.gz<br>
[2022-08-30 06:45:42,158] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_29 =&gt; spleen_29.nii.gz<br>
[2022-08-30 06:45:42,158] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_14 =&gt; spleen_14.nii.gz<br>
[2022-08-30 06:45:42,158] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_17 =&gt; spleen_17.nii.gz<br>
[2022-08-30 06:45:42,158] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_49 =&gt; spleen_49.nii.gz<br>
[2022-08-30 06:45:42,158] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_21 =&gt; spleen_21.nii.gz<br>
[2022-08-30 06:45:42,159] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_38 =&gt; spleen_38.nii.gz<br>
[2022-08-30 06:45:42,159] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_59 =&gt; spleen_59.nii.gz<br>
[2022-08-30 06:45:42,159] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_10 =&gt; spleen_10.nii.gz<br>
[2022-08-30 06:45:42,159] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_13 =&gt; spleen_13.nii.gz<br>
[2022-08-30 06:45:42,159] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_2 =&gt; spleen_2.nii.gz<br>
[2022-08-30 06:45:42,160] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_44 =&gt; spleen_44.nii.gz<br>
[2022-08-30 06:45:42,160] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_61 =&gt; spleen_61.nii.gz<br>
[2022-08-30 06:45:42,160] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_62 =&gt; spleen_62.nii.gz<br>
[2022-08-30 06:45:42,160] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_53 =&gt; spleen_53.nii.gz<br>
[2022-08-30 06:45:42,160] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_9 =&gt; spleen_9.nii.gz<br>
[2022-08-30 06:45:42,161] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_24 =&gt; spleen_24.nii.gz<br>
[2022-08-30 06:45:42,161] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_18 =&gt; spleen_18.nii.gz<br>
[2022-08-30 06:45:42,161] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_27 =&gt; spleen_27.nii.gz<br>
[2022-08-30 06:45:42,161] [8015] [MainThread] [INFO] (monailabel.datastore.local:557) - Adding New Image: spleen_46 =&gt; spleen_46.nii.gz<br>
[2022-08-30 06:45:42,163] [8015] [MainThread] [INFO] (monailabel.datastore.local:540) - Invalidate count: 41<br>
[2022-08-30 06:45:42,165] [8015] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)<br>
[2022-08-30 06:45:42,166] [8015] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7f9a7410ac50&gt;<br>
[2022-08-30 06:45:42,166] [8015] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit_seg =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7f9a630226d0&gt;<br>
[2022-08-30 06:45:42,167] [8015] [MainThread] [INFO] (main:161) - +++ Adding Trainer:: deepedit =&gt; &lt;lib.trainers.deepedit.DeepEdit object at 0x7f9a63022850&gt;<br>
[2022-08-30 06:45:42,167] [8015] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /home/lukas/.cache/monailabel/sessions<br>
[2022-08-30 06:45:42,167] [8015] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600<br>
[2022-08-30 06:45:42,167] [8015] [MainThread] [INFO] (monailabel.interfaces.app:460) - App Init - completed<br>
[2022-08-30 06:45:42,168] [8015] [MainThread] [INFO] (timeloop:60) - Starting Timeloop…<br>
[2022-08-30 06:45:42,168] [8015] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete..run_scheduler at 0x7f9a74059950&gt;<br>
[2022-08-30 06:45:42,168] [8015] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set<br>
[2022-08-30 06:47:34,447] [8015] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘random’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 06:47:34,449] [8015] [MainThread] [INFO] (monailabel.tasks.activelearning.random:44) - Random: Images: [‘spleen_63’, ‘spleen_8’, ‘spleen_20’, ‘spleen_22’, ‘spleen_25’, ‘spleen_28’, ‘spleen_56’, ‘spleen_6’, ‘spleen_40’, ‘spleen_41’, ‘spleen_33’, ‘spleen_45’, ‘spleen_31’, ‘spleen_60’, ‘spleen_3’, ‘spleen_16’, ‘spleen_52’, ‘spleen_12’, ‘spleen_19’, ‘spleen_26’, ‘spleen_47’, ‘spleen_32’, ‘spleen_29’, ‘spleen_14’, ‘spleen_17’, ‘spleen_49’, ‘spleen_21’, ‘spleen_38’, ‘spleen_59’, ‘spleen_10’, ‘spleen_13’, ‘spleen_2’, ‘spleen_44’, ‘spleen_61’, ‘spleen_62’, ‘spleen_53’, ‘spleen_9’, ‘spleen_24’, ‘spleen_18’, ‘spleen_27’, ‘spleen_46’]; Weight: [1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054, 1661842054]<br>
[2022-08-30 06:47:34,450] [8015] [MainThread] [INFO] (monailabel.tasks.activelearning.random:45) - Random: Selected Image: spleen_41<br>
[2022-08-30 06:47:34,454] [8015] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_41’, ‘ts’: 1661841942, ‘name’: ‘spleen_41.nii.gz’, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_41.nii.gz’}<br>
[2022-08-30 06:50:17,167] [8015] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘first’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 06:50:17,167] [8015] [MainThread] [INFO] (lib.activelearning.first:36) - First: Selected Image: spleen_10<br>
[2022-08-30 06:50:17,171] [8015] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_10’, ‘ts’: 1661841942, ‘name’: ‘spleen_10.nii.gz’, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_10.nii.gz’}<br>
[2022-08-30 06:50:30,760] [8015] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘first’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 06:50:30,760] [8015] [MainThread] [INFO] (lib.activelearning.first:36) - First: Selected Image: spleen_10<br>
[2022-08-30 06:50:30,763] [8015] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_10’, ‘ts’: 1661841942, ‘name’: ‘spleen_10.nii.gz’, ‘strategy’: {‘first’: {‘ts’: 1661842230, ‘client_id’: ‘user-xyz’}}, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_10.nii.gz’}<br>
[2022-08-30 06:50:36,629] [8015] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘first’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 06:50:36,630] [8015] [MainThread] [INFO] (lib.activelearning.first:36) - First: Selected Image: spleen_10<br>
[2022-08-30 06:50:36,633] [8015] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_10’, ‘ts’: 1661841942, ‘name’: ‘spleen_10.nii.gz’, ‘strategy’: {‘first’: {‘ts’: 1661842236, ‘client_id’: ‘user-xyz’}}, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_10.nii.gz’}<br>
[2022-08-30 06:52:46,679] [8015] [MainThread] [INFO] (monailabel.endpoints.infer:160) - Infer Request: {‘model’: ‘Histogram+GraphCut’, ‘image’: ‘spleen_10’, ‘label’: ‘/tmp/tmp1j82ejpz.nii.gz’, ‘num_bins’: 64, ‘lamda’: 1.0, ‘sigma’: 0.1, ‘roi’: <span class="chcklst-box fa fa-square-o fa-fw"></span>, ‘label_info’: [{‘name’: ‘background’, ‘id’: 1}, {‘name’: ‘spleen’, ‘id’: 2}, {‘name’: ‘right kidney’, ‘id’: 3}, {‘name’: ‘left kidney’, ‘id’: 4}, {‘name’: ‘liver’, ‘id’: 5}, {‘name’: ‘stomach’, ‘id’: 6}, {‘name’: ‘aorta’, ‘id’: 7}, {‘name’: ‘inferior vena cava’, ‘id’: 8}, {‘name’: ‘background_scribbles’, ‘id’: 9}, {‘name’: ‘foreground_scribbles’, ‘id’: 10}], ‘selected_label_name’: ‘spleen’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 06:52:46,680] [8015] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:265) - Infer Request (final): {‘num_bins’: 64, ‘lamda’: 1.0, ‘sigma’: 0.1, ‘model’: ‘Histogram+GraphCut’, ‘image’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_10.nii.gz’, ‘label’: ‘/tmp/tmp1j82ejpz.nii.gz’, ‘roi’: <span class="chcklst-box fa fa-square-o fa-fw"></span>, ‘label_info’: [{‘name’: ‘background’, ‘id’: 1}, {‘name’: ‘spleen’, ‘id’: 2}, {‘name’: ‘right kidney’, ‘id’: 3}, {‘name’: ‘left kidney’, ‘id’: 4}, {‘name’: ‘liver’, ‘id’: 5}, {‘name’: ‘stomach’, ‘id’: 6}, {‘name’: ‘aorta’, ‘id’: 7}, {‘name’: ‘inferior vena cava’, ‘id’: 8}, {‘name’: ‘background_scribbles’, ‘id’: 9}, {‘name’: ‘foreground_scribbles’, ‘id’: 10}], ‘selected_label_name’: ‘spleen’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’, ‘description’: ‘A post processing step with histogram-based GraphCut for Generic segmentation’, ‘device’: ‘cpu’}<br>
[2022-08-30 06:52:46,682] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:63) - PRE - Run Transform(s)<br>
[2022-08-30 06:52:46,682] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:64) - PRE - Input Keys: [‘num_bins’, ‘lamda’, ‘sigma’, ‘model’, ‘image’, ‘label’, ‘roi’, ‘label_info’, ‘selected_label_name’, ‘result_extension’, ‘result_dtype’, ‘client_id’, ‘description’, ‘device’, ‘image_path’]<br>
[2022-08-30 06:52:47,495] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (LoadImaged): Time: 0.8118; image: (512, 512, 55)(torch.float32); label: (512, 512, 55)(torch.float32)<br>
[2022-08-30 06:52:47,617] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (EnsureChannelFirstd): Time: 0.1213; image: (1, 512, 512, 55)(torch.float32); label: (1, 512, 512, 55)(torch.float32)<br>
[2022-08-30 06:52:47,617] [8015] [MainThread] [INFO] (root:74) - Loading background scribbles labels from: background_scribbles with index: 9<br>
[2022-08-30 06:52:47,617] [8015] [MainThread] [INFO] (root:79) - Loading foreground scribbles labels from: foreground_scribbles with index: 10<br>
[2022-08-30 06:52:47,623] [8015] [MainThread] [INFO] (monailabel.scribbles.transforms:111) - Scribbles: (1, 512, 512, 55)<br>
[2022-08-30 06:52:47,623] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (AddBackgroundScribblesFromROId): Time: 0.0063; image: (1, 512, 512, 55)(torch.float32); label: (1, 512, 512, 55)(float32)<br>
[2022-08-30 06:52:48,808] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (Spacingd): Time: 1.1842; image: (1, 201, 201, 55)(torch.float32); label: (1, 205, 205, 12)(torch.float32)<br>
[2022-08-30 06:52:48,852] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (ScaleIntensityRanged): Time: 0.0432; image: (1, 201, 201, 55)(torch.float32); label: (1, 205, 205, 12)(torch.float32)<br>
[2022-08-30 06:52:48,853] [8015] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:400) - Inferer:: cpu =&gt; Compose =&gt; {‘transforms’: (&lt;monailabel.scribbles.transforms.MakeLikelihoodFromScribblesHistogramd object at 0x7f9a60f396d0&gt;,), ‘map_items’: True, ‘unpack_items’: False, ‘log_stats’: False, ‘R’: RandomState(MT19937) at 0x7F9AAD53D8D0}<br>
[2022-08-30 06:52:48,853] [8015] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:352) - Infer model path: None<br>
[2022-08-30 06:52:48,853] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:63) - INF - Run Inferer(s)<br>
[2022-08-30 06:52:48,854] [8015] [MainThread] [INFO] (monailabel.interfaces.utils.transform:64) - INF - Input Keys: [‘num_bins’, ‘lamda’, ‘sigma’, ‘model’, ‘image’, ‘label’, ‘roi’, ‘label_info’, ‘selected_label_name’, ‘result_extension’, ‘result_dtype’, ‘client_id’, ‘description’, ‘device’, ‘image_path’, ‘image_meta_dict’, ‘label_meta_dict’, ‘latencies’]<br>
[2022-08-30 06:52:48,854] [8015] [MainThread] [INFO] (root:74) - Loading background scribbles labels from: background_scribbles with index: 9<br>
[2022-08-30 06:52:48,854] [8015] [MainThread] [INFO] (root:79) - Loading foreground scribbles labels from: foreground_scribbles with index: 10<br>
[2022-08-30 06:58:29,521] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: /home/lukas/radiology; studies: /home/lukas/Task09_Spleen/imagesTr; conf: {‘models’: ‘deepedit’}<br>
[2022-08-30 06:58:29,525] [15129] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for MONAILabelApp Found: &lt;class ‘main.MyApp’&gt;<br>
[2022-08-30 06:58:29,529] [15129] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation.Segmentation’&gt;<br>
[2022-08-30 06:58:29,530] [15129] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_3d.Deepgrow3D’&gt;<br>
[2022-08-30 06:58:29,532] [15129] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepedit.DeepEdit’&gt;<br>
[2022-08-30 06:58:29,532] [15129] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation_spleen.SegmentationSpleen’&gt;<br>
[2022-08-30 06:58:29,533] [15129] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_2d.Deepgrow2D’&gt;<br>
[2022-08-30 06:58:29,533] [15129] [MainThread] [INFO] (main:83) - +++ Adding Model: deepedit =&gt; lib.configs.deepedit.DeepEdit<br>
[2022-08-30 06:58:30,511] [15129] [MainThread] [INFO] (lib.configs.deepedit:144) - EPISTEMIC Enabled: 0; Samples: 5<br>
[2022-08-30 06:58:30,511] [15129] [MainThread] [INFO] (lib.configs.deepedit:148) - TTA Enabled: 0; Samples: 5<br>
[2022-08-30 06:58:30,511] [15129] [MainThread] [INFO] (main:87) - +++ Using Models: [‘deepedit’]<br>
[2022-08-30 06:58:30,512] [15129] [MainThread] [INFO] (monailabel.interfaces.app:128) - Init Datastore for: /home/lukas/Task09_Spleen/imagesTr<br>
[2022-08-30 06:58:30,512] [15129] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: [‘<em>.nii.gz’, '</em>.nii’, ‘<em>.nrrd’, '</em>.jpg’, ‘<em>.png’, '</em>.tif’, ‘<em>.svs’, '</em>.xml’]<br>
[2022-08-30 06:58:30,518] [15129] [MainThread] [INFO] (monailabel.datastore.local:540) - Invalidate count: 0<br>
[2022-08-30 06:58:30,518] [15129] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)<br>
[2022-08-30 06:58:30,519] [15129] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7fc616be5610&gt;<br>
[2022-08-30 06:58:30,519] [15129] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit_seg =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7fc61d7ae650&gt;<br>
[2022-08-30 06:58:30,519] [15129] [MainThread] [INFO] (main:161) - +++ Adding Trainer:: deepedit =&gt; &lt;lib.trainers.deepedit.DeepEdit object at 0x7fc6101b7190&gt;<br>
[2022-08-30 06:58:30,520] [15129] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /home/lukas/.cache/monailabel/sessions<br>
[2022-08-30 06:58:30,520] [15129] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600<br>
[2022-08-30 06:58:30,520] [15129] [MainThread] [INFO] (monailabel.interfaces.app:460) - App Init - completed<br>
[2022-08-30 06:58:30,520] [15129] [MainThread] [INFO] (timeloop:60) - Starting Timeloop…<br>
[2022-08-30 06:58:30,520] [15129] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete..run_scheduler at 0x7fc6119b27a0&gt;<br>
[2022-08-30 06:58:30,521] [15129] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set<br>
[2022-08-30 06:59:05,474] [15129] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘random’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 06:59:05,478] [15129] [MainThread] [INFO] (monailabel.tasks.activelearning.random:44) - Random: Images: [‘spleen_63’, ‘spleen_8’, ‘spleen_20’, ‘spleen_22’, ‘spleen_25’, ‘spleen_28’, ‘spleen_56’, ‘spleen_6’, ‘spleen_40’, ‘spleen_41’, ‘spleen_33’, ‘spleen_45’, ‘spleen_31’, ‘spleen_60’, ‘spleen_3’, ‘spleen_16’, ‘spleen_52’, ‘spleen_12’, ‘spleen_19’, ‘spleen_26’, ‘spleen_47’, ‘spleen_32’, ‘spleen_29’, ‘spleen_14’, ‘spleen_17’, ‘spleen_49’, ‘spleen_21’, ‘spleen_38’, ‘spleen_59’, ‘spleen_10’, ‘spleen_13’, ‘spleen_2’, ‘spleen_44’, ‘spleen_61’, ‘spleen_62’, ‘spleen_53’, ‘spleen_9’, ‘spleen_24’, ‘spleen_18’, ‘spleen_27’, ‘spleen_46’]; Weight: [1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 691, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745, 1661842745]<br>
[2022-08-30 06:59:05,478] [15129] [MainThread] [INFO] (monailabel.tasks.activelearning.random:45) - Random: Selected Image: spleen_16<br>
[2022-08-30 06:59:05,484] [15129] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_16’, ‘ts’: 1661841942, ‘name’: ‘spleen_16.nii.gz’, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_16.nii.gz’}<br>
[2022-08-30 07:00:29,907] [15129] [MainThread] [INFO] (monailabel.endpoints.infer:160) - Infer Request: {‘model’: ‘Histogram+GraphCut’, ‘image’: ‘spleen_16’, ‘label’: ‘/tmp/tmpr6wyzmqn.nii.gz’, ‘num_bins’: 64, ‘lamda’: 1.0, ‘sigma’: 0.1, ‘roi’: [88, 190, 254, 431, 25, 39], ‘label_info’: [{‘name’: ‘background’, ‘id’: 1}, {‘name’: ‘spleen’, ‘id’: 2}, {‘name’: ‘right kidney’, ‘id’: 3}, {‘name’: ‘left kidney’, ‘id’: 4}, {‘name’: ‘liver’, ‘id’: 5}, {‘name’: ‘stomach’, ‘id’: 6}, {‘name’: ‘aorta’, ‘id’: 7}, {‘name’: ‘inferior vena cava’, ‘id’: 8}, {‘name’: ‘background_scribbles’, ‘id’: 9}, {‘name’: ‘foreground_scribbles’, ‘id’: 10}], ‘selected_label_name’: ‘spleen’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 07:00:29,908] [15129] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:265) - Infer Request (final): {‘num_bins’: 64, ‘lamda’: 1.0, ‘sigma’: 0.1, ‘model’: ‘Histogram+GraphCut’, ‘image’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_16.nii.gz’, ‘label’: ‘/tmp/tmpr6wyzmqn.nii.gz’, ‘roi’: [88, 190, 254, 431, 25, 39], ‘label_info’: [{‘name’: ‘background’, ‘id’: 1}, {‘name’: ‘spleen’, ‘id’: 2}, {‘name’: ‘right kidney’, ‘id’: 3}, {‘name’: ‘left kidney’, ‘id’: 4}, {‘name’: ‘liver’, ‘id’: 5}, {‘name’: ‘stomach’, ‘id’: 6}, {‘name’: ‘aorta’, ‘id’: 7}, {‘name’: ‘inferior vena cava’, ‘id’: 8}, {‘name’: ‘background_scribbles’, ‘id’: 9}, {‘name’: ‘foreground_scribbles’, ‘id’: 10}], ‘selected_label_name’: ‘spleen’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’, ‘description’: ‘A post processing step with histogram-based GraphCut for Generic segmentation’, ‘device’: ‘cpu’}<br>
[2022-08-30 07:00:29,910] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:63) - PRE - Run Transform(s)<br>
[2022-08-30 07:00:29,910] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:64) - PRE - Input Keys: [‘num_bins’, ‘lamda’, ‘sigma’, ‘model’, ‘image’, ‘label’, ‘roi’, ‘label_info’, ‘selected_label_name’, ‘result_extension’, ‘result_dtype’, ‘client_id’, ‘description’, ‘device’, ‘image_path’]<br>
[2022-08-30 07:00:30,815] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (LoadImaged): Time: 0.9036; image: (512, 512, 61)(torch.float32); label: (512, 512, 61)(torch.float32)<br>
[2022-08-30 07:00:30,816] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (EnsureChannelFirstd): Time: 0.0005; image: (1, 512, 512, 61)(torch.float32); label: (1, 512, 512, 61)(torch.float32)<br>
[2022-08-30 07:00:30,816] [15129] [MainThread] [INFO] (root:74) - Loading background scribbles labels from: background_scribbles with index: 9<br>
[2022-08-30 07:00:30,816] [15129] [MainThread] [INFO] (root:79) - Loading foreground scribbles labels from: foreground_scribbles with index: 10<br>
[2022-08-30 07:00:30,816] [15129] [MainThread] [INFO] (monailabel.scribbles.transforms:111) - Scribbles: (1, 512, 512, 61)<br>
[2022-08-30 07:00:30,873] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (AddBackgroundScribblesFromROId): Time: 0.0568; image: (1, 512, 512, 61)(torch.float32); label: (1, 512, 512, 61)(float32)<br>
[2022-08-30 07:00:31,192] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (Spacingd): Time: 0.3187; image: (1, 163, 163, 97)(torch.float32); label: (1, 205, 205, 13)(torch.float32)<br>
[2022-08-30 07:00:31,203] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (ScaleIntensityRanged): Time: 0.0101; image: (1, 163, 163, 97)(torch.float32); label: (1, 205, 205, 13)(torch.float32)<br>
[2022-08-30 07:00:31,205] [15129] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:400) - Inferer:: cpu =&gt; Compose =&gt; {‘transforms’: (&lt;monailabel.scribbles.transforms.MakeLikelihoodFromScribblesHistogramd object at 0x7fc61d6a1150&gt;,), ‘map_items’: True, ‘unpack_items’: False, ‘log_stats’: False, ‘R’: RandomState(MT19937) at 0x7FC61D6AB490}<br>
[2022-08-30 07:00:31,205] [15129] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:352) - Infer model path: None<br>
[2022-08-30 07:00:31,205] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:63) - INF - Run Inferer(s)<br>
[2022-08-30 07:00:31,205] [15129] [MainThread] [INFO] (monailabel.interfaces.utils.transform:64) - INF - Input Keys: [‘num_bins’, ‘lamda’, ‘sigma’, ‘model’, ‘image’, ‘label’, ‘roi’, ‘label_info’, ‘selected_label_name’, ‘result_extension’, ‘result_dtype’, ‘client_id’, ‘description’, ‘device’, ‘image_path’, ‘image_meta_dict’, ‘label_meta_dict’, ‘latencies’]<br>
[2022-08-30 07:00:31,206] [15129] [MainThread] [INFO] (root:74) - Loading background scribbles labels from: background_scribbles with index: 9<br>
[2022-08-30 07:00:31,207] [15129] [MainThread] [INFO] (root:79) - Loading foreground scribbles labels from: foreground_scribbles with index: 10<br>
[2022-08-30 07:05:59,582] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: /home/lukas/radiology; studies: /home/lukas/Task09_Spleen/imagesTr; conf: {‘models’: ‘deepedit’}<br>
[2022-08-30 07:05:59,586] [19017] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for MONAILabelApp Found: &lt;class ‘main.MyApp’&gt;<br>
[2022-08-30 07:05:59,591] [19017] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation.Segmentation’&gt;<br>
[2022-08-30 07:05:59,591] [19017] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_3d.Deepgrow3D’&gt;<br>
[2022-08-30 07:05:59,593] [19017] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepedit.DeepEdit’&gt;<br>
[2022-08-30 07:05:59,594] [19017] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation_spleen.SegmentationSpleen’&gt;<br>
[2022-08-30 07:05:59,594] [19017] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_2d.Deepgrow2D’&gt;<br>
[2022-08-30 07:05:59,595] [19017] [MainThread] [INFO] (main:83) - +++ Adding Model: deepedit =&gt; lib.configs.deepedit.DeepEdit<br>
[2022-08-30 07:06:00,586] [19017] [MainThread] [INFO] (lib.configs.deepedit:144) - EPISTEMIC Enabled: 0; Samples: 5<br>
[2022-08-30 07:06:00,587] [19017] [MainThread] [INFO] (lib.configs.deepedit:148) - TTA Enabled: 0; Samples: 5<br>
[2022-08-30 07:06:00,587] [19017] [MainThread] [INFO] (main:87) - +++ Using Models: [‘deepedit’]<br>
[2022-08-30 07:06:00,587] [19017] [MainThread] [INFO] (monailabel.interfaces.app:128) - Init Datastore for: /home/lukas/Task09_Spleen/imagesTr<br>
[2022-08-30 07:06:00,587] [19017] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: [‘<em>.nii.gz’, '</em>.nii’, ‘<em>.nrrd’, '</em>.jpg’, ‘<em>.png’, '</em>.tif’, ‘<em>.svs’, '</em>.xml’]<br>
[2022-08-30 07:06:00,593] [19017] [MainThread] [INFO] (monailabel.datastore.local:540) - Invalidate count: 0<br>
[2022-08-30 07:06:00,593] [19017] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)<br>
[2022-08-30 07:06:00,595] [19017] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7f39ef5a46d0&gt;<br>
[2022-08-30 07:06:00,595] [19017] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit_seg =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7f39e53b4190&gt;<br>
[2022-08-30 07:06:00,595] [19017] [MainThread] [INFO] (main:161) - +++ Adding Trainer:: deepedit =&gt; &lt;lib.trainers.deepedit.DeepEdit object at 0x7f39e53b42d0&gt;<br>
[2022-08-30 07:06:00,595] [19017] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /home/lukas/.cache/monailabel/sessions<br>
[2022-08-30 07:06:00,595] [19017] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600<br>
[2022-08-30 07:06:00,595] [19017] [MainThread] [INFO] (monailabel.interfaces.app:460) - App Init - completed<br>
[2022-08-30 07:06:00,596] [19017] [MainThread] [INFO] (timeloop:60) - Starting Timeloop…<br>
[2022-08-30 07:06:00,596] [19017] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete..run_scheduler at 0x7f39e576d320&gt;<br>
[2022-08-30 07:06:00,596] [19017] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set<br>
[2022-08-30 07:06:25,853] [19017] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘random’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 07:06:25,855] [19017] [MainThread] [INFO] (monailabel.tasks.activelearning.random:44) - Random: Images: [‘spleen_63’, ‘spleen_8’, ‘spleen_20’, ‘spleen_22’, ‘spleen_25’, ‘spleen_28’, ‘spleen_56’, ‘spleen_6’, ‘spleen_40’, ‘spleen_41’, ‘spleen_33’, ‘spleen_45’, ‘spleen_31’, ‘spleen_60’, ‘spleen_3’, ‘spleen_16’, ‘spleen_52’, ‘spleen_12’, ‘spleen_19’, ‘spleen_26’, ‘spleen_47’, ‘spleen_32’, ‘spleen_29’, ‘spleen_14’, ‘spleen_17’, ‘spleen_49’, ‘spleen_21’, ‘spleen_38’, ‘spleen_59’, ‘spleen_10’, ‘spleen_13’, ‘spleen_2’, ‘spleen_44’, ‘spleen_61’, ‘spleen_62’, ‘spleen_53’, ‘spleen_9’, ‘spleen_24’, ‘spleen_18’, ‘spleen_27’, ‘spleen_46’]; Weight: [1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1131, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 440, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185, 1661843185]<br>
[2022-08-30 07:06:25,855] [19017] [MainThread] [INFO] (monailabel.tasks.activelearning.random:45) - Random: Selected Image: spleen_27<br>
[2022-08-30 07:06:25,860] [19017] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_27’, ‘ts’: 1661841942, ‘name’: ‘spleen_27.nii.gz’, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_27.nii.gz’}<br>
[2022-08-30 07:06:39,936] [19017] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘random’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 07:06:39,938] [19017] [MainThread] [INFO] (monailabel.tasks.activelearning.random:44) - Random: Images: [‘spleen_63’, ‘spleen_8’, ‘spleen_20’, ‘spleen_22’, ‘spleen_25’, ‘spleen_28’, ‘spleen_56’, ‘spleen_6’, ‘spleen_40’, ‘spleen_41’, ‘spleen_33’, ‘spleen_45’, ‘spleen_31’, ‘spleen_60’, ‘spleen_3’, ‘spleen_16’, ‘spleen_52’, ‘spleen_12’, ‘spleen_19’, ‘spleen_26’, ‘spleen_47’, ‘spleen_32’, ‘spleen_29’, ‘spleen_14’, ‘spleen_17’, ‘spleen_49’, ‘spleen_21’, ‘spleen_38’, ‘spleen_59’, ‘spleen_10’, ‘spleen_13’, ‘spleen_2’, ‘spleen_44’, ‘spleen_61’, ‘spleen_62’, ‘spleen_53’, ‘spleen_9’, ‘spleen_24’, ‘spleen_18’, ‘spleen_27’, ‘spleen_46’]; Weight: [1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1145, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 454, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 1661843199, 14, 1661843199]<br>
[2022-08-30 07:06:39,938] [19017] [MainThread] [INFO] (monailabel.tasks.activelearning.random:45) - Random: Selected Image: spleen_49<br>
[2022-08-30 07:06:39,941] [19017] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_49’, ‘ts’: 1661841942, ‘name’: ‘spleen_49.nii.gz’, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_49.nii.gz’}<br>
[2022-08-30 07:07:42,923] [19017] [MainThread] [INFO] (monailabel.endpoints.infer:160) - Infer Request: {‘model’: ‘Histogram+GraphCut’, ‘image’: ‘spleen_49’, ‘label’: ‘/tmp/tmp2n85sm6p.nii.gz’, ‘num_bins’: 64, ‘lamda’: 1.0, ‘sigma’: 0.1, ‘roi’: [24, 137, 124, 306, 6, 53], ‘label_info’: [{‘name’: ‘background’, ‘id’: 1}, {‘name’: ‘spleen’, ‘id’: 2}, {‘name’: ‘right kidney’, ‘id’: 3}, {‘name’: ‘left kidney’, ‘id’: 4}, {‘name’: ‘liver’, ‘id’: 5}, {‘name’: ‘stomach’, ‘id’: 6}, {‘name’: ‘aorta’, ‘id’: 7}, {‘name’: ‘inferior vena cava’, ‘id’: 8}, {‘name’: ‘background_scribbles’, ‘id’: 9}, {‘name’: ‘foreground_scribbles’, ‘id’: 10}], ‘selected_label_name’: ‘spleen’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 07:07:42,924] [19017] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:265) - Infer Request (final): {‘num_bins’: 64, ‘lamda’: 1.0, ‘sigma’: 0.1, ‘model’: ‘Histogram+GraphCut’, ‘image’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_49.nii.gz’, ‘label’: ‘/tmp/tmp2n85sm6p.nii.gz’, ‘roi’: [24, 137, 124, 306, 6, 53], ‘label_info’: [{‘name’: ‘background’, ‘id’: 1}, {‘name’: ‘spleen’, ‘id’: 2}, {‘name’: ‘right kidney’, ‘id’: 3}, {‘name’: ‘left kidney’, ‘id’: 4}, {‘name’: ‘liver’, ‘id’: 5}, {‘name’: ‘stomach’, ‘id’: 6}, {‘name’: ‘aorta’, ‘id’: 7}, {‘name’: ‘inferior vena cava’, ‘id’: 8}, {‘name’: ‘background_scribbles’, ‘id’: 9}, {‘name’: ‘foreground_scribbles’, ‘id’: 10}], ‘selected_label_name’: ‘spleen’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’, ‘description’: ‘A post processing step with histogram-based GraphCut for Generic segmentation’, ‘device’: ‘cpu’}<br>
[2022-08-30 07:07:42,926] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:63) - PRE - Run Transform(s)<br>
[2022-08-30 07:07:42,926] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:64) - PRE - Input Keys: [‘num_bins’, ‘lamda’, ‘sigma’, ‘model’, ‘image’, ‘label’, ‘roi’, ‘label_info’, ‘selected_label_name’, ‘result_extension’, ‘result_dtype’, ‘client_id’, ‘description’, ‘device’, ‘image_path’]<br>
[2022-08-30 07:07:43,825] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (LoadImaged): Time: 0.8985; image: (512, 512, 61)(torch.float32); label: (512, 512, 61)(torch.float32)<br>
[2022-08-30 07:07:43,827] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (EnsureChannelFirstd): Time: 0.0007; image: (1, 512, 512, 61)(torch.float32); label: (1, 512, 512, 61)(torch.float32)<br>
[2022-08-30 07:07:43,827] [19017] [MainThread] [INFO] (root:74) - Loading background scribbles labels from: background_scribbles with index: 9<br>
[2022-08-30 07:07:43,827] [19017] [MainThread] [INFO] (root:79) - Loading foreground scribbles labels from: foreground_scribbles with index: 10<br>
[2022-08-30 07:07:43,828] [19017] [MainThread] [INFO] (monailabel.scribbles.transforms:111) - Scribbles: (1, 512, 512, 61)<br>
[2022-08-30 07:07:43,889] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (AddBackgroundScribblesFromROId): Time: 0.0618; image: (1, 512, 512, 61)(torch.float32); label: (1, 512, 512, 61)(float32)<br>
[2022-08-30 07:07:44,233] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (Spacingd): Time: 0.3435; image: (1, 175, 175, 49)(torch.float32); label: (1, 205, 205, 13)(torch.float32)<br>
[2022-08-30 07:07:44,238] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (ScaleIntensityRanged): Time: 0.0042; image: (1, 175, 175, 49)(torch.float32); label: (1, 205, 205, 13)(torch.float32)<br>
[2022-08-30 07:07:44,239] [19017] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:400) - Inferer:: cpu =&gt; Compose =&gt; {‘transforms’: (&lt;monailabel.scribbles.transforms.MakeLikelihoodFromScribblesHistogramd object at 0x7f39e42f2090&gt;,), ‘map_items’: True, ‘unpack_items’: False, ‘log_stats’: False, ‘R’: RandomState(MT19937) at 0x7F39F28B6380}<br>
[2022-08-30 07:07:44,239] [19017] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:352) - Infer model path: None<br>
[2022-08-30 07:07:44,239] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:63) - INF - Run Inferer(s)<br>
[2022-08-30 07:07:44,239] [19017] [MainThread] [INFO] (monailabel.interfaces.utils.transform:64) - INF - Input Keys: [‘num_bins’, ‘lamda’, ‘sigma’, ‘model’, ‘image’, ‘label’, ‘roi’, ‘label_info’, ‘selected_label_name’, ‘result_extension’, ‘result_dtype’, ‘client_id’, ‘description’, ‘device’, ‘image_path’, ‘image_meta_dict’, ‘label_meta_dict’, ‘latencies’]<br>
[2022-08-30 07:07:44,240] [19017] [MainThread] [INFO] (root:74) - Loading background scribbles labels from: background_scribbles with index: 9<br>
[2022-08-30 07:07:44,240] [19017] [MainThread] [INFO] (root:79) - Loading foreground scribbles labels from: foreground_scribbles with index: 10<br>
[2022-08-30 07:16:57,278] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: /home/lukas/radiology; studies: /home/lukas/Task09_Spleen/imagesTr; conf: {‘models’: ‘deepedit’}<br>
[2022-08-30 07:16:57,282] [25061] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for MONAILabelApp Found: &lt;class ‘main.MyApp’&gt;<br>
[2022-08-30 07:16:57,286] [25061] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation.Segmentation’&gt;<br>
[2022-08-30 07:16:57,287] [25061] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_3d.Deepgrow3D’&gt;<br>
[2022-08-30 07:16:57,289] [25061] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepedit.DeepEdit’&gt;<br>
[2022-08-30 07:16:57,290] [25061] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation_spleen.SegmentationSpleen’&gt;<br>
[2022-08-30 07:16:57,290] [25061] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_2d.Deepgrow2D’&gt;<br>
[2022-08-30 07:16:57,290] [25061] [MainThread] [INFO] (main:83) - +++ Adding Model: deepedit =&gt; lib.configs.deepedit.DeepEdit<br>
[2022-08-30 07:16:58,278] [25061] [MainThread] [INFO] (lib.configs.deepedit:144) - EPISTEMIC Enabled: 0; Samples: 5<br>
[2022-08-30 07:16:58,279] [25061] [MainThread] [INFO] (lib.configs.deepedit:148) - TTA Enabled: 0; Samples: 5<br>
[2022-08-30 07:16:58,279] [25061] [MainThread] [INFO] (main:87) - +++ Using Models: [‘deepedit’]<br>
[2022-08-30 07:16:58,279] [25061] [MainThread] [INFO] (monailabel.interfaces.app:128) - Init Datastore for: /home/lukas/Task09_Spleen/imagesTr<br>
[2022-08-30 07:16:58,279] [25061] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: [‘<em>.nii.gz’, '</em>.nii’, ‘<em>.nrrd’, '</em>.jpg’, ‘<em>.png’, '</em>.tif’, ‘<em>.svs’, '</em>.xml’]<br>
[2022-08-30 07:16:58,285] [25061] [MainThread] [INFO] (monailabel.datastore.local:540) - Invalidate count: 0<br>
[2022-08-30 07:16:58,285] [25061] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)<br>
[2022-08-30 07:16:58,287] [25061] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7fa70d2d1610&gt;<br>
[2022-08-30 07:16:58,287] [25061] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit_seg =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7fa7045f91d0&gt;<br>
[2022-08-30 07:16:58,287] [25061] [MainThread] [INFO] (main:161) - +++ Adding Trainer:: deepedit =&gt; &lt;lib.trainers.deepedit.DeepEdit object at 0x7fa7045f9310&gt;<br>
[2022-08-30 07:16:58,287] [25061] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /home/lukas/.cache/monailabel/sessions<br>
[2022-08-30 07:16:58,288] [25061] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600<br>
[2022-08-30 07:16:58,288] [25061] [MainThread] [INFO] (monailabel.interfaces.app:460) - App Init - completed<br>
[2022-08-30 07:16:58,288] [25061] [MainThread] [INFO] (timeloop:60) - Starting Timeloop…<br>
[2022-08-30 07:16:58,288] [25061] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete..run_scheduler at 0x7fa7049b2320&gt;<br>
[2022-08-30 07:16:58,289] [25061] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set<br>
[2022-08-30 07:17:32,947] [25061] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘random’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 07:17:32,949] [25061] [MainThread] [INFO] (monailabel.tasks.activelearning.random:44) - Random: Images: [‘spleen_63’, ‘spleen_8’, ‘spleen_20’, ‘spleen_22’, ‘spleen_25’, ‘spleen_28’, ‘spleen_56’, ‘spleen_6’, ‘spleen_40’, ‘spleen_41’, ‘spleen_33’, ‘spleen_45’, ‘spleen_31’, ‘spleen_60’, ‘spleen_3’, ‘spleen_16’, ‘spleen_52’, ‘spleen_12’, ‘spleen_19’, ‘spleen_26’, ‘spleen_47’, ‘spleen_32’, ‘spleen_29’, ‘spleen_14’, ‘spleen_17’, ‘spleen_49’, ‘spleen_21’, ‘spleen_38’, ‘spleen_59’, ‘spleen_10’, ‘spleen_13’, ‘spleen_2’, ‘spleen_44’, ‘spleen_61’, ‘spleen_62’, ‘spleen_53’, ‘spleen_9’, ‘spleen_24’, ‘spleen_18’, ‘spleen_27’, ‘spleen_46’]; Weight: [1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1798, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1107, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 653, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 1661843852, 667, 1661843852]<br>
[2022-08-30 07:17:32,949] [25061] [MainThread] [INFO] (monailabel.tasks.activelearning.random:45) - Random: Selected Image: spleen_26<br>
[2022-08-30 07:17:32,953] [25061] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_26’, ‘ts’: 1661841942, ‘name’: ‘spleen_26.nii.gz’, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_26.nii.gz’}<br>
[2022-08-30 07:17:47,731] [25061] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {‘strategy’: ‘random’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 07:17:47,732] [25061] [MainThread] [INFO] (monailabel.tasks.activelearning.random:44) - Random: Images: [‘spleen_63’, ‘spleen_8’, ‘spleen_20’, ‘spleen_22’, ‘spleen_25’, ‘spleen_28’, ‘spleen_56’, ‘spleen_6’, ‘spleen_40’, ‘spleen_41’, ‘spleen_33’, ‘spleen_45’, ‘spleen_31’, ‘spleen_60’, ‘spleen_3’, ‘spleen_16’, ‘spleen_52’, ‘spleen_12’, ‘spleen_19’, ‘spleen_26’, ‘spleen_47’, ‘spleen_32’, ‘spleen_29’, ‘spleen_14’, ‘spleen_17’, ‘spleen_49’, ‘spleen_21’, ‘spleen_38’, ‘spleen_59’, ‘spleen_10’, ‘spleen_13’, ‘spleen_2’, ‘spleen_44’, ‘spleen_61’, ‘spleen_62’, ‘spleen_53’, ‘spleen_9’, ‘spleen_24’, ‘spleen_18’, ‘spleen_27’, ‘spleen_46’]; Weight: [1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1813, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1122, 1661843867, 1661843867, 1661843867, 15, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 668, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 1661843867, 682, 1661843867]<br>
[2022-08-30 07:17:47,733] [25061] [MainThread] [INFO] (monailabel.tasks.activelearning.random:45) - Random: Selected Image: spleen_14<br>
[2022-08-30 07:17:47,736] [25061] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {‘id’: ‘spleen_14’, ‘ts’: 1661841942, ‘name’: ‘spleen_14.nii.gz’, ‘path’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_14.nii.gz’}<br>
[2022-08-30 07:18:21,299] [25061] [MainThread] [INFO] (monailabel.endpoints.infer:160) - Infer Request: {‘model’: ‘Histogram+GraphCut’, ‘image’: ‘spleen_14’, ‘label’: ‘/tmp/tmp4nz9wtc4.nii.gz’, ‘num_bins’: 64, ‘lamda’: 1.0, ‘sigma’: 0.1, ‘roi’: <span class="chcklst-box fa fa-square-o fa-fw"></span>, ‘label_info’: [{‘name’: ‘background’, ‘id’: 1}, {‘name’: ‘spleen’, ‘id’: 2}, {‘name’: ‘right kidney’, ‘id’: 3}, {‘name’: ‘left kidney’, ‘id’: 4}, {‘name’: ‘liver’, ‘id’: 5}, {‘name’: ‘stomach’, ‘id’: 6}, {‘name’: ‘aorta’, ‘id’: 7}, {‘name’: ‘inferior vena cava’, ‘id’: 8}, {‘name’: ‘background_scribbles’, ‘id’: 9}, {‘name’: ‘foreground_scribbles’, ‘id’: 10}], ‘selected_label_name’: ‘spleen’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’}<br>
[2022-08-30 07:18:21,299] [25061] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:265) - Infer Request (final): {‘num_bins’: 64, ‘lamda’: 1.0, ‘sigma’: 0.1, ‘model’: ‘Histogram+GraphCut’, ‘image’: ‘/home/lukas/Task09_Spleen/imagesTr/spleen_14.nii.gz’, ‘label’: ‘/tmp/tmp4nz9wtc4.nii.gz’, ‘roi’: <span class="chcklst-box fa fa-square-o fa-fw"></span>, ‘label_info’: [{‘name’: ‘background’, ‘id’: 1}, {‘name’: ‘spleen’, ‘id’: 2}, {‘name’: ‘right kidney’, ‘id’: 3}, {‘name’: ‘left kidney’, ‘id’: 4}, {‘name’: ‘liver’, ‘id’: 5}, {‘name’: ‘stomach’, ‘id’: 6}, {‘name’: ‘aorta’, ‘id’: 7}, {‘name’: ‘inferior vena cava’, ‘id’: 8}, {‘name’: ‘background_scribbles’, ‘id’: 9}, {‘name’: ‘foreground_scribbles’, ‘id’: 10}], ‘selected_label_name’: ‘spleen’, ‘result_extension’: ‘.nrrd’, ‘result_dtype’: ‘uint8’, ‘client_id’: ‘user-xyz’, ‘description’: ‘A post processing step with histogram-based GraphCut for Generic segmentation’, ‘device’: ‘cpu’}<br>
[2022-08-30 07:18:21,302] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:63) - PRE - Run Transform(s)<br>
[2022-08-30 07:18:21,303] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:64) - PRE - Input Keys: [‘num_bins’, ‘lamda’, ‘sigma’, ‘model’, ‘image’, ‘label’, ‘roi’, ‘label_info’, ‘selected_label_name’, ‘result_extension’, ‘result_dtype’, ‘client_id’, ‘description’, ‘device’, ‘image_path’]<br>
[2022-08-30 07:18:22,043] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (LoadImaged): Time: 0.7396; image: (512, 512, 54)(torch.float32); label: (512, 512, 54)(torch.float32)<br>
[2022-08-30 07:18:22,044] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (EnsureChannelFirstd): Time: 0.0005; image: (1, 512, 512, 54)(torch.float32); label: (1, 512, 512, 54)(torch.float32)<br>
[2022-08-30 07:18:22,044] [25061] [MainThread] [INFO] (root:74) - Loading background scribbles labels from: background_scribbles with index: 9<br>
[2022-08-30 07:18:22,044] [25061] [MainThread] [INFO] (root:79) - Loading foreground scribbles labels from: foreground_scribbles with index: 10<br>
[2022-08-30 07:18:22,045] [25061] [MainThread] [INFO] (monailabel.scribbles.transforms:111) - Scribbles: (1, 512, 512, 54)<br>
[2022-08-30 07:18:22,045] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (AddBackgroundScribblesFromROId): Time: 0.0006; image: (1, 512, 512, 54)(torch.float32); label: (1, 512, 512, 54)(float32)<br>
[2022-08-30 07:18:22,334] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (Spacingd): Time: 0.2885; image: (1, 175, 175, 54)(torch.float32); label: (1, 205, 205, 12)(torch.float32)<br>
[2022-08-30 07:18:22,339] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:108) - PRE - Transform (ScaleIntensityRanged): Time: 0.0049; image: (1, 175, 175, 54)(torch.float32); label: (1, 205, 205, 12)(torch.float32)<br>
[2022-08-30 07:18:22,341] [25061] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:400) - Inferer:: cpu =&gt; Compose =&gt; {‘transforms’: (&lt;monailabel.scribbles.transforms.MakeLikelihoodFromScribblesHistogramd object at 0x7fa701d37690&gt;,), ‘map_items’: True, ‘unpack_items’: False, ‘log_stats’: False, ‘R’: RandomState(MT19937) at 0x7FA711AFB380}<br>
[2022-08-30 07:18:22,341] [25061] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:352) - Infer model path: None<br>
[2022-08-30 07:18:22,342] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:63) - INF - Run Inferer(s)<br>
[2022-08-30 07:18:22,342] [25061] [MainThread] [INFO] (monailabel.interfaces.utils.transform:64) - INF - Input Keys: [‘num_bins’, ‘lamda’, ‘sigma’, ‘model’, ‘image’, ‘label’, ‘roi’, ‘label_info’, ‘selected_label_name’, ‘result_extension’, ‘result_dtype’, ‘client_id’, ‘description’, ‘device’, ‘image_path’, ‘image_meta_dict’, ‘label_meta_dict’, ‘latencies’]<br>
[2022-08-30 07:18:22,343] [25061] [MainThread] [INFO] (root:74) - Loading background scribbles labels from: background_scribbles with index: 9<br>
[2022-08-30 07:18:22,343] [25061] [MainThread] [INFO] (root:79) - Loading foreground scribbles labels from: foreground_scribbles with index: 10</p>
</blockquote>
<p>I have a numpy version that is 1.21.6 and the SimpleCRF package is installed.</p>
<p>Any ideas on how to fix this?</p>
<p>Thank you in advance!</p>
<p>Lukas</p>

---
