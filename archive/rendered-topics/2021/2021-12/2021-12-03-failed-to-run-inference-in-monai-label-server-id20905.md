---
topic_id: 20905
title: "Failed To Run Inference In Monai Label Server"
date: 2021-12-03
url: https://discourse.slicer.org/t/20905
---

# Failed to run inference in MONAI Label Server

**Topic ID**: 20905
**Date**: 2021-12-03
**URL**: https://discourse.slicer.org/t/failed-to-run-inference-in-monai-label-server/20905

---

## Post #1 by @Fluvio_Lobo (2021-12-03 19:04 UTC)

<p>Hello,</p>
<p>We are trying to use MONAI Label to train an AI on our own dataset.<br>
I have installed MONAI Label following the <a href="https://github.com/Project-MONAI/MONAILabel" rel="noopener nofollow ugc">instructions in GitHub</a>, but I get the;</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/WS000039/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-13/NA-MIC/Extensions-30181/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabel.py", line 1532, in onClickSegmentation
    result_file, params = self.logic.infer(model, image_file, self.getParamsFromConfig("infer", model))
  File "C:/Users/WS000039/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-13/NA-MIC/Extensions-30181/MONAILabel/lib/Slicer-4.13/qt-scripted-modules/MONAILabel.py", line 1815, in infer
    result_file, params = client.infer(model, image_in, params, label_in)
  File "C:\Users\WS000039\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-13\NA-MIC\Extensions-30181\MONAILabel\lib\Slicer-4.13\qt-scripted-modules\MONAILabelLib\client.py", line 111, in infer
    "Status: {}; Response: {}".format(status, form),
MONAILabelLib.client.MONAILabelException: (2, "Status: 500; Response: b'Internal Server Error'")
</code></pre>
<p>Even when running one of the spleen example datasets</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85808066e48b3a662d9581bc039fee9a7fb3cd9f.png" data-download-href="/uploads/short-url/j30OEdqalAAWlGG82XqNYFb0XUj.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85808066e48b3a662d9581bc039fee9a7fb3cd9f_2_690x373.png" alt="error" data-base62-sha1="j30OEdqalAAWlGG82XqNYFb0XUj" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85808066e48b3a662d9581bc039fee9a7fb3cd9f_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85808066e48b3a662d9581bc039fee9a7fb3cd9f_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85808066e48b3a662d9581bc039fee9a7fb3cd9f_2_1380x746.png 2x" data-dominant-color="414248"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1920×1040 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @diazandr3s (2021-12-06 00:40 UTC)

<p>Hi <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a>,</p>
<p>Can you please also add the server logs? You can get them from <a href="https://127.0.0.1:8000/logs" rel="noopener nofollow ugc">https://127.0.0.1:8000/logs</a> or in the folder App (deepedit/logs).</p>
<p>Thanks!</p>
<p>Andres</p>

---

## Post #3 by @Fluvio_Lobo (2021-12-06 02:52 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a>,</p>
<p>Sorry for the delay, I had to set-up MONAI-Label in my home computer.<br>
I do get the same issue and here is the logfile;</p>
<pre><code class="lang-auto">[2021-12-05 21:39:03,625] [25408] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:39:14,539] [24708] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:40:22,041] [17392] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:41:40,682] [24228] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:43:03,432] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:43:03,483] [8820] [MainThread] [INFO] (monailabel.utils.others.class_utils:35) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2021-12-05 21:43:04,219] [8820] [MainThread] [INFO] (main:104) - Pretrained Model Path: https://github.com/Project-MONAI/MONAILabel/releases/download/data/deepedit_dynunet_spleen.pt
[2021-12-05 21:43:04,220] [8820] [MainThread] [INFO] (monailabel.interfaces.app:527) - Downloading resource: C:\Users\WOLF512\apps\deepedit\model\pretrained_dynunet.pt from https://github.com/Project-MONAI/MONAILabel/releases/download/data/deepedit_dynunet_spleen.pt
[2021-12-05 21:43:34,967] [8820] [MainThread] [INFO] (main:109) - EPISTEMIC Enabled: 0; Samples: 5
[2021-12-05 21:43:34,968] [8820] [MainThread] [INFO] (main:113) - TTA Enabled: 0; Samples: 5
[2021-12-05 21:43:34,971] [8820] [MainThread] [INFO] (monailabel.interfaces.app:115) - Init Datastore for: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr
[2021-12-05 21:43:34,973] [8820] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: ['*.nii.gz', '*.nii', '*.nrrd']
[2021-12-05 21:43:34,989] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_10 =&gt; spleen_10.nii.gz
[2021-12-05 21:43:35,086] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_12 =&gt; spleen_12.nii.gz
[2021-12-05 21:43:35,217] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_13 =&gt; spleen_13.nii.gz
[2021-12-05 21:43:35,287] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_14 =&gt; spleen_14.nii.gz
[2021-12-05 21:43:35,337] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_16 =&gt; spleen_16.nii.gz
[2021-12-05 21:43:35,402] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_17 =&gt; spleen_17.nii.gz
[2021-12-05 21:43:35,482] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_18 =&gt; spleen_18.nii.gz
[2021-12-05 21:43:35,606] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_19 =&gt; spleen_19.nii.gz
[2021-12-05 21:43:35,655] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_2 =&gt; spleen_2.nii.gz
[2021-12-05 21:43:35,735] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_20 =&gt; spleen_20.nii.gz
[2021-12-05 21:43:35,858] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_21 =&gt; spleen_21.nii.gz
[2021-12-05 21:43:35,932] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_22 =&gt; spleen_22.nii.gz
[2021-12-05 21:43:36,049] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_24 =&gt; spleen_24.nii.gz
[2021-12-05 21:43:36,145] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_25 =&gt; spleen_25.nii.gz
[2021-12-05 21:43:36,222] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_26 =&gt; spleen_26.nii.gz
[2021-12-05 21:43:36,281] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_27 =&gt; spleen_27.nii.gz
[2021-12-05 21:43:36,391] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_28 =&gt; spleen_28.nii.gz
[2021-12-05 21:43:36,433] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_29 =&gt; spleen_29.nii.gz
[2021-12-05 21:43:36,520] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_3 =&gt; spleen_3.nii.gz
[2021-12-05 21:43:36,560] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_31 =&gt; spleen_31.nii.gz
[2021-12-05 21:43:36,620] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_32 =&gt; spleen_32.nii.gz
[2021-12-05 21:43:36,715] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_33 =&gt; spleen_33.nii.gz
[2021-12-05 21:43:36,785] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_38 =&gt; spleen_38.nii.gz
[2021-12-05 21:43:36,870] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_40 =&gt; spleen_40.nii.gz
[2021-12-05 21:43:36,960] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_41 =&gt; spleen_41.nii.gz
[2021-12-05 21:43:37,049] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_44 =&gt; spleen_44.nii.gz
[2021-12-05 21:43:37,122] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_45 =&gt; spleen_45.nii.gz
[2021-12-05 21:43:37,212] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_46 =&gt; spleen_46.nii.gz
[2021-12-05 21:43:37,300] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_47 =&gt; spleen_47.nii.gz
[2021-12-05 21:43:37,390] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_49 =&gt; spleen_49.nii.gz
[2021-12-05 21:43:37,457] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_52 =&gt; spleen_52.nii.gz
[2021-12-05 21:43:37,582] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_53 =&gt; spleen_53.nii.gz
[2021-12-05 21:43:37,742] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_56 =&gt; spleen_56.nii.gz
[2021-12-05 21:43:37,776] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_59 =&gt; spleen_59.nii.gz
[2021-12-05 21:43:37,824] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_6 =&gt; spleen_6.nii.gz
[2021-12-05 21:43:37,945] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_60 =&gt; spleen_60.nii.gz
[2021-12-05 21:43:38,042] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_61 =&gt; spleen_61.nii.gz
[2021-12-05 21:43:38,130] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_62 =&gt; spleen_62.nii.gz
[2021-12-05 21:43:38,201] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_63 =&gt; spleen_63.nii.gz
[2021-12-05 21:43:38,260] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_8 =&gt; spleen_8.nii.gz
[2021-12-05 21:43:38,295] [8820] [MainThread] [INFO] (monailabel.datastore.local:551) - Adding New Image: spleen_9 =&gt; spleen_9.nii.gz
[2021-12-05 21:43:38,344] [8820] [MainThread] [INFO] (monailabel.datastore.local:534) - Invalidate count: 41
[2021-12-05 21:43:38,347] [8820] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)
[2021-12-05 21:43:40,676] [8820] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: C:\Users\WOLF512\.cache\monailabel\sessions
[2021-12-05 21:43:40,676] [8820] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2021-12-05 21:43:40,678] [8820] [MainThread] [INFO] (monailabel.interfaces.app:396) - App Init - completed
[2021-12-05 21:43:40,679] [8820] [MainThread] [INFO] (monailabel.utils.async_tasks.task:36) - Scoring request: {'method': 'dice'}
[2021-12-05 21:43:40,680] [8820] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:57) - COMMAND:: C:\Users\WOLF512\AppData\Local\Programs\Python\Python39\python.exe -m monailabel.interfaces.utils.app -m scoring -r {"method":"dice","gpus":"all"}
[2021-12-05 21:43:40,681] [8820] [MainThread] [INFO] (monailabel.utils.async_tasks.task:36) - Scoring request: {'method': 'sum'}
[2021-12-05 21:43:40,681] [8820] [MainThread] [INFO] (timeloop:60) - Starting Timeloop..
[2021-12-05 21:43:40,682] [8820] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete.&lt;locals&gt;.run_scheduler at 0x000002318F0A3D30&gt;
[2021-12-05 21:43:40,683] [8820] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set
[2021-12-05 21:43:40,883] [4956] [MainThread] [INFO] (__main__:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:43:43,699] [4956] [MainThread] [INFO] (monailabel.utils.others.class_utils:35) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2021-12-05 21:43:44,601] [4956] [MainThread] [INFO] (main:104) - Pretrained Model Path: https://github.com/Project-MONAI/MONAILabel/releases/download/data/deepedit_dynunet_spleen.pt
[2021-12-05 21:43:44,602] [4956] [MainThread] [INFO] (main:109) - EPISTEMIC Enabled: 0; Samples: 5
[2021-12-05 21:43:44,602] [4956] [MainThread] [INFO] (main:113) - TTA Enabled: 0; Samples: 5
[2021-12-05 21:43:44,602] [4956] [MainThread] [INFO] (monailabel.interfaces.app:115) - Init Datastore for: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr
[2021-12-05 21:43:44,602] [4956] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: ['*.nii.gz', '*.nii', '*.nrrd']
[2021-12-05 21:43:44,633] [4956] [MainThread] [INFO] (monailabel.datastore.local:534) - Invalidate count: 0
[2021-12-05 21:43:44,633] [4956] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)
[2021-12-05 21:43:44,665] [4956] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: C:\Users\WOLF512\.cache\monailabel\sessions
[2021-12-05 21:43:44,665] [4956] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2021-12-05 21:43:44,666] [4956] [MainThread] [INFO] (__main__:62) - Result: {}
[2021-12-05 21:43:45,227] [8820] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:75) - Return code: 0
[2021-12-05 21:43:45,229] [8820] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:57) - COMMAND:: C:\Users\WOLF512\AppData\Local\Programs\Python\Python39\python.exe -m monailabel.interfaces.utils.app -m scoring -r {"method":"sum","gpus":"all"}
[2021-12-05 21:43:45,426] [4628] [MainThread] [INFO] (__main__:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:43:48,267] [4628] [MainThread] [INFO] (monailabel.utils.others.class_utils:35) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2021-12-05 21:43:49,008] [4628] [MainThread] [INFO] (main:104) - Pretrained Model Path: https://github.com/Project-MONAI/MONAILabel/releases/download/data/deepedit_dynunet_spleen.pt
[2021-12-05 21:43:49,008] [4628] [MainThread] [INFO] (main:109) - EPISTEMIC Enabled: 0; Samples: 5
[2021-12-05 21:43:49,009] [4628] [MainThread] [INFO] (main:113) - TTA Enabled: 0; Samples: 5
[2021-12-05 21:43:49,009] [4628] [MainThread] [INFO] (monailabel.interfaces.app:115) - Init Datastore for: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr
[2021-12-05 21:43:49,009] [4628] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: ['*.nii.gz', '*.nii', '*.nrrd']
[2021-12-05 21:43:49,030] [4628] [MainThread] [INFO] (monailabel.datastore.local:534) - Invalidate count: 0
[2021-12-05 21:43:49,030] [4628] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)
[2021-12-05 21:43:49,059] [4628] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: C:\Users\WOLF512\.cache\monailabel\sessions
[2021-12-05 21:43:49,059] [4628] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2021-12-05 21:43:49,060] [4628] [MainThread] [INFO] (__main__:62) - Result: {}
[2021-12-05 21:43:49,535] [8820] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:75) - Return code: 0
[2021-12-05 21:43:57,697] [8820] [MainThread] [INFO] (monailabel.endpoints.activelearning:42) - Active Learning Request: {'strategy': 'random'}
[2021-12-05 21:43:57,706] [8820] [MainThread] [INFO] (monailabel.tasks.activelearning.random:44) - Random: Images: ['spleen_10', 'spleen_12', 'spleen_13', 'spleen_14', 'spleen_16', 'spleen_17', 'spleen_18', 'spleen_19', 'spleen_2', 'spleen_20', 'spleen_21', 'spleen_22', 'spleen_24', 'spleen_25', 'spleen_26', 'spleen_27', 'spleen_28', 'spleen_29', 'spleen_3', 'spleen_31', 'spleen_32', 'spleen_33', 'spleen_38', 'spleen_40', 'spleen_41', 'spleen_44', 'spleen_45', 'spleen_46', 'spleen_47', 'spleen_49', 'spleen_52', 'spleen_53', 'spleen_56', 'spleen_59', 'spleen_6', 'spleen_60', 'spleen_61', 'spleen_62', 'spleen_63', 'spleen_8', 'spleen_9']; Weight: [1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637, 1638758637]
[2021-12-05 21:43:57,706] [8820] [MainThread] [INFO] (monailabel.tasks.activelearning.random:45) - Random: Selected Image: spleen_52
[2021-12-05 21:43:57,707] [8820] [MainThread] [INFO] (monailabel.utils.async_tasks.task:36) - Scoring request: {'method': 'dice'}
[2021-12-05 21:43:57,708] [8820] [MainThread] [INFO] (monailabel.utils.async_tasks.task:36) - Scoring request: {'method': 'sum'}
[2021-12-05 21:43:57,709] [8820] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:57) - COMMAND:: C:\Users\WOLF512\AppData\Local\Programs\Python\Python39\python.exe -m monailabel.interfaces.utils.app -m scoring -r {"method":"dice","gpus":"all"}
[2021-12-05 21:43:57,715] [8820] [MainThread] [INFO] (monailabel.endpoints.activelearning:58) - Next sample: {'id': 'spleen_52', 'ts': 1638758617, 'checksum': 'SHA256:689d690d0fc10324c2a5ef3b0c883d07a9412619f69e0475b0b8cbabb75fd5cb', 'name': 'spleen_52.nii.gz', 'path': 'C:\\Users\\WOLF512\\datasets\\Task09_Spleen\\imagesTr\\spleen_52.nii.gz'}
[2021-12-05 21:43:57,882] [22940] [MainThread] [INFO] (__main__:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:43:59,150] [8820] [MainThread] [INFO] (monailabel.endpoints.infer:147) - Infer Request: {'model': 'deepedit_seg', 'image': 'spleen_52'}
[2021-12-05 21:43:59,152] [8820] [MainThread] [INFO] (monailabel.interfaces.app:224) - Image =&gt; C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr\spleen_52.nii.gz
[2021-12-05 21:43:59,152] [8820] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:218) - Infer Request (final): {'model': 'deepedit_seg', 'image': 'C:\\Users\\WOLF512\\datasets\\Task09_Spleen\\imagesTr\\spleen_52.nii.gz'}
[2021-12-05 21:43:59,155] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:61) - PRE - Run Transform
[2021-12-05 21:43:59,155] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:62) - PRE - Input Keys: dict_keys(['model', 'image', 'image_path'])
[2021-12-05 21:43:59,965] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (LoadImaged): Time: 0.8081; image: (512, 512, 112)(float32)
[2021-12-05 21:43:59,966] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (SingleLabelSingleModalityd): Time: 0.0000; image: (512, 512, 112)(float32)
[2021-12-05 21:43:59,967] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (AddChanneld): Time: 0.0000; image: (1, 512, 512, 112)(float32)
[2021-12-05 21:44:02,089] [22940] [MainThread] [INFO] (monailabel.utils.others.class_utils:35) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2021-12-05 21:44:04,430] [22940] [MainThread] [INFO] (main:104) - Pretrained Model Path: https://github.com/Project-MONAI/MONAILabel/releases/download/data/deepedit_dynunet_spleen.pt
[2021-12-05 21:44:04,430] [22940] [MainThread] [INFO] (main:109) - EPISTEMIC Enabled: 0; Samples: 5
[2021-12-05 21:44:04,430] [22940] [MainThread] [INFO] (main:113) - TTA Enabled: 0; Samples: 5
[2021-12-05 21:44:04,430] [22940] [MainThread] [INFO] (monailabel.interfaces.app:115) - Init Datastore for: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr
[2021-12-05 21:44:04,431] [22940] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: ['*.nii.gz', '*.nii', '*.nrrd']
[2021-12-05 21:44:04,470] [22940] [MainThread] [INFO] (monailabel.datastore.local:534) - Invalidate count: 0
[2021-12-05 21:44:04,470] [22940] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)
[2021-12-05 21:44:04,503] [22940] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: C:\Users\WOLF512\.cache\monailabel\sessions
[2021-12-05 21:44:04,503] [22940] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2021-12-05 21:44:04,503] [22940] [MainThread] [INFO] (__main__:62) - Result: {}
[2021-12-05 21:44:05,158] [8820] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:75) - Return code: 0
[2021-12-05 21:44:05,159] [8820] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:57) - COMMAND:: C:\Users\WOLF512\AppData\Local\Programs\Python\Python39\python.exe -m monailabel.interfaces.utils.app -m scoring -r {"method":"sum","gpus":"all"}
[2021-12-05 21:44:05,336] [24840] [MainThread] [INFO] (__main__:38) - Initializing App from: C:\Users\WOLF512\apps\deepedit; studies: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr; conf: {}
[2021-12-05 21:44:08,168] [24840] [MainThread] [INFO] (monailabel.utils.others.class_utils:35) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2021-12-05 21:44:08,800] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (Spacingd): Time: 8.8329; image: (1, 412, 412, 445)(float32)
[2021-12-05 21:44:08,802] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (Orientationd): Time: 0.0020; image: (1, 412, 412, 445)(float32)
[2021-12-05 21:44:09,212] [24840] [MainThread] [INFO] (main:104) - Pretrained Model Path: https://github.com/Project-MONAI/MONAILabel/releases/download/data/deepedit_dynunet_spleen.pt
[2021-12-05 21:44:09,212] [24840] [MainThread] [INFO] (main:109) - EPISTEMIC Enabled: 0; Samples: 5
[2021-12-05 21:44:09,213] [24840] [MainThread] [INFO] (main:113) - TTA Enabled: 0; Samples: 5
[2021-12-05 21:44:09,213] [24840] [MainThread] [INFO] (monailabel.interfaces.app:115) - Init Datastore for: C:\Users\WOLF512\datasets\Task09_Spleen\imagesTr
[2021-12-05 21:44:09,213] [24840] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: True; Extensions: ['*.nii.gz', '*.nii', '*.nrrd']
[2021-12-05 21:44:09,236] [24840] [MainThread] [INFO] (monailabel.datastore.local:534) - Invalidate count: 0
[2021-12-05 21:44:09,236] [24840] [MainThread] [INFO] (monailabel.datastore.local:145) - Start observing external modifications on datastore (AUTO RELOAD)
[2021-12-05 21:44:09,265] [24840] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: C:\Users\WOLF512\.cache\monailabel\sessions
[2021-12-05 21:44:09,265] [24840] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2021-12-05 21:44:09,266] [24840] [MainThread] [INFO] (__main__:62) - Result: {}
[2021-12-05 21:44:09,929] [8820] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:75) - Return code: 0
[2021-12-05 21:44:10,948] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (NormalizeIntensityd): Time: 2.1451; image: (1, 412, 412, 445)(float32)
[2021-12-05 21:44:11,347] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (Resized): Time: 0.3982; image: (1, 256, 256, 128)(float32)
[2021-12-05 21:44:11,432] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (DiscardAddGuidanced): Time: 0.0828; image: (3, 256, 256, 128)(float32)
[2021-12-05 21:44:11,432] [8820] [MainThread] [INFO] (monailabel.interfaces.utils.transform:98) - PRE - Transform (ToTensord): Time: 0.0000; image: torch.Size([3, 256, 256, 128])(torch.float32)
[2021-12-05 21:44:11,433] [8820] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:341) - Running Inferer:: SimpleInferer
[2021-12-05 21:44:11,433] [8820] [MainThread] [INFO] (monailabel.interfaces.tasks.infer:294) - Infer model path: C:\Users\WOLF512\apps\deepedit\model\pretrained_dynunet.pt
</code></pre>

---

## Post #4 by @Fluvio_Lobo (2021-12-06 03:19 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a>,</p>
<p>Quick Update!<br>
While the <code>log</code> does not show it, the terminal had a message saying something in line with <code>running as a CPU system only</code></p>
<p>I looked over the <a href="https://docs.monai.io/projects/label/en/latest/installation.html" rel="noopener nofollow ugc">installation prerequisites</a> and saw that I missed the actual installation of Pytorch with CUDA.</p>
<p>Now I get this however;</p>
<pre><code class="lang-auto">RuntimeError: CUDA out of memory. Tried to allocate 1024.00 MiB (GPU 0; 4.00 GiB total capacity; 2.21 GiB already allocated; 481.27 MiB free; 2.25 GiB reserved in total by PyTorch)
</code></pre>

---

## Post #5 by @diazandr3s (2021-12-06 12:07 UTC)

<p>Thanks for the update, <a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a><br>
Can you please run in a terminal the nvidia-smi command to check which GPU card and memory is available on your PC?<br>
By default, the DeepEdit App uses 256x256x128 as the image size to train and do inference (<a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/deepedit/main.py#L94" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/main.py at main · Project-MONAI/MONAILabel · GitHub</a>). I think the available GPU is not enough for this image size. My recommendation is to train a model using an image size of 128x128x128 or another that fits in the available GPU memory.</p>
<p>Please let me know,</p>

---

## Post #6 by @Fluvio_Lobo (2021-12-06 13:01 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a>,</p>
<p>I will test this at work today. I think this is a reminder that I need an upgrade at home <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=10" title=":sweat_smile:" class="emoji" alt=":sweat_smile:"></p>
<p>I do have more questions regarding these limits;</p>
<ul>
<li>
<p>What is the relationship between image dimensions (or overall number of voxels) and memory size required?</p>
</li>
<li>
<p><code>main.py</code> also has a line for “target spacing”…these are just default values that get updated with the new image, correct? The image size is still the limiting factor</p>
</li>
</ul>
<pre><code class="lang-auto">   spatial_size = json.loads(conf.get("spatial_size", "[256, 256, 128]"))
   target_spacing = json.loads(conf.get("target_spacing", "[1.0, 1.0, 1.0]"))
</code></pre>
<p>Thank you!</p>

---

## Post #7 by @diazandr3s (2021-12-06 13:53 UTC)

<p><a class="mention" href="/u/fluvio_lobo">@Fluvio_Lobo</a>,</p>
<p><strong>What is the relationship between image dimensions (or overall number of voxels) and memory size required?</strong></p>
<p>This is not easy to tell as it also depends on the network hyperparameters and the transformations (data augmentation) you apply to the images. For instance, you can check here (<a href="https://tinyurl.com/tableGPUMemory" rel="noopener nofollow ugc">https://tinyurl.com/tableGPUMemory</a>) an empirical relation between image size and the DynUNet (<a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/deepedit/main.py#L54" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/main.py at main · Project-MONAI/MONAILabel · GitHub</a>).</p>
<p><strong><code>main.py</code> also has a line for “target spacing”…these are just default values that get updated with the new image, correct? The image size is still the limiting factor</strong></p>
<p>“Target spacing” is the spatial resolution we use to train and do inference. This is the default value and it does not change once you start the training process.<br>
For understanding purposes, you may want to check how the spatial resolution varies among the dataset. Otherwise, you can think of this as a sort of normalization.</p>
<p>Best,</p>

---

## Post #8 by @Fluvio_Lobo (2021-12-06 14:16 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a>,</p>
<p>Thanks for the clarification!</p>
<p><strong><code>main.py</code> also has a line for “target spacing”…these are just default values that get updated with the new image, correct? The image size is still the limiting factor</strong></p>
<blockquote>
<p>“Target spacing” is the spatial resolution we use to train and do inference. This is the default value and it does not change once you start the training process.<br>
For understanding purposes, you may want to check how the spatial resolution varies among the dataset. Otherwise, you can think of this as a sort of normalization.</p>
</blockquote>
<p>If we had a dataset with a spatial resolution below 1.00 mm. Or, perhaps, we resample the data to below 1.00 mm, do we then update this value before running the training?</p>

---

## Post #9 by @diazandr3s (2021-12-06 21:40 UTC)

<p>That’s right. This is the argument you should update with the desired spatial resolution before training.</p>

---
