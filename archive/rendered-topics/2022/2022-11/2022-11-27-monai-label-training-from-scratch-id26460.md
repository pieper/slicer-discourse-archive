# MONAI Label - Training from Scratch

**Topic ID**: 26460
**Date**: 2022-11-27
**URL**: https://discourse.slicer.org/t/monai-label-training-from-scratch/26460

---

## Post #1 by @chendong9416 (2022-11-27 14:49 UTC)

<div class="youtube-onebox lazy-video-container" data-video-id="3HTh2dqZqew" data-video-title="MONAI Label - Training from Scratch" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=3HTh2dqZqew" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/3HTh2dqZqew/maxresdefault.jpg" title="MONAI Label - Training from Scratch" width="" height="">
  </a>
</div>

<p>Currently, i am training my own dataset as the video showed. I wonder,  after i trained about 10-20 cases, how can i use the trained model? Does a simple click on auto-segmentation works (it does not work in low cases trained model-report error)?</p>

---

## Post #2 by @diazandr3s (2022-11-29 01:29 UTC)

<p>Hi <a class="mention" href="/u/chendong9416">@chendong9416</a>,</p>
<p>Yes, you should be able to get a prediction by clicking the auto-segmentation button.</p>
<blockquote>
<p>(it does not work in low cases trained model-report error)?</p>
</blockquote>
<p>I’m not sure I understand this. Have you trained the model?</p>

---

## Post #3 by @chendong9416 (2022-11-30 14:36 UTC)

<p>Hi, Andres,</p>
<p>There is problem in my training.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b48674cf79e7d25db89332c555cb5181d11341e.jpeg" data-download-href="/uploads/short-url/8srigmmOBETs0MyEvzn0TKwXET4.jpeg?dl=1" title="00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b48674cf79e7d25db89332c555cb5181d11341e_2_517x258.jpeg" alt="00" data-base62-sha1="8srigmmOBETs0MyEvzn0TKwXET4" width="517" height="258" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b48674cf79e7d25db89332c555cb5181d11341e_2_517x258.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b48674cf79e7d25db89332c555cb5181d11341e_2_775x387.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b48674cf79e7d25db89332c555cb5181d11341e_2_1034x516.jpeg 2x" data-dominant-color="B8B9CA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">00</span><span class="informations">1920×959 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After manual segmentation of 5 cases with infra-renal abdominal aortic aneurysm and submit label in the monai label module in 3D slicer, i click on the “Train” button, but no accuracy was seen, below is the code in Anaconda Prompt</p>
<pre><code class="lang-auto">(base) C:\Users\xgzxe&gt;conda activate monailabel

(monailabel) C:\Users\xgzxe&gt;monailabel start_server --app radiology --studies my_dataset --conf models segmentation
Using PYTHONPATH=C:\Users\xgzxe\anaconda3\envs;
""
2022-11-30 19:50:17,217 - USING:: version = False
2022-11-30 19:50:17,217 - USING:: app = C:\Users\xgzxe\radiology
2022-11-30 19:50:17,217 - USING:: studies = C:\Users\xgzxe\my_dataset
2022-11-30 19:50:17,217 - USING:: verbose = INFO
2022-11-30 19:50:17,217 - USING:: conf = [['models', 'segmentation']]
2022-11-30 19:50:17,217 - USING:: host = 0.0.0.0
2022-11-30 19:50:17,217 - USING:: port = 8000
2022-11-30 19:50:17,217 - USING:: uvicorn_app = monailabel.app:app
2022-11-30 19:50:17,217 - USING:: ssl_keyfile = None
2022-11-30 19:50:17,217 - USING:: ssl_certfile = None
2022-11-30 19:50:17,217 - USING:: ssl_keyfile_password = None
2022-11-30 19:50:17,217 - USING:: ssl_ca_certs = None
2022-11-30 19:50:17,217 - USING:: workers = None
2022-11-30 19:50:17,217 - USING:: limit_concurrency = None
2022-11-30 19:50:17,217 - USING:: access_log = False
2022-11-30 19:50:17,217 - USING:: log_config = None
2022-11-30 19:50:17,217 - USING:: dryrun = False
2022-11-30 19:50:17,217 - USING:: action = start_server
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_API_STR =
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_PROJECT_NAME = MONAILabel
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_APP_DIR =
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_STUDIES =
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_AUTH_ENABLE = False
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_AUTH_DB =
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_APP_CONF = '{}'
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_TASKS_TRAIN = True
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_TASKS_STRATEGY = True
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_TASKS_SCORING = True
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_TASKS_BATCH_INFER = True
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_DATASTORE =
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_URL =
2022-11-30 19:50:17,217 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_USERNAME =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PASSWORD =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_API_KEY =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_CACHE_PATH =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PROJECT =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_ASSET_PATH =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_DSA_ANNOTATION_GROUPS =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_USERNAME =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PASSWORD =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_PATH =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_QIDO_PREFIX = None
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_WADO_PREFIX = None
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_STOW_PREFIX = None
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_FETCH_BY_FRAME = False
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CONVERT_TO_NIFTI = True
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_SEARCH_FILTER = '{"Modality": "CT"}'
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_EXPIRY = 180
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PROXY_TIMEOUT = 30.0
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_READ_TIMEOUT = 5.0
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_AUTO_RELOAD = True
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_READ_ONLY = False
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_FILE_EXT = '["*.nii.gz", "*.nii", "*.nrrd", "*.jpg", "*.png", "*.tif", "*.svs", "*.xml"]'
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_SERVER_PORT = 8000
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_CORS_ORIGINS = '[]'
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_SESSIONS = True
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_SESSION_PATH =
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_SESSION_EXPIRY = 3600
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_INFER_CONCURRENCY = -1
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_INFER_TIMEOUT = 600
2022-11-30 19:50:17,233 - ENV SETTINGS:: MONAI_LABEL_AUTO_UPDATE_SCORING = True
2022-11-30 19:50:17,233 -
Allow Origins: ['*']
[2022-11-30 19:50:18,272] [12856] [MainThread] [INFO] (uvicorn.error:75) - Started server process [12856]
[2022-11-30 19:50:18,284] [12856] [MainThread] [INFO] (uvicorn.error:45) - Waiting for application startup.
[2022-11-30 19:50:18,300] [12856] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: C:\Users\xgzxe\radiology; studies: C:\Users\xgzxe\my_dataset; conf: {'models': 'segmentation'}
[2022-11-30 19:50:18,440] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2022-11-30 19:50:18,455] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepedit.DeepEdit'&gt;
[2022-11-30 19:50:18,455] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepgrow_2d.Deepgrow2D'&gt;
[2022-11-30 19:50:18,471] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepgrow_3d.Deepgrow3D'&gt;
[2022-11-30 19:50:18,472] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.localization_spine.LocalizationSpine'&gt;
[2022-11-30 19:50:18,472] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.localization_vertebra.LocalizationVertebra'&gt;
[2022-11-30 19:50:18,487] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation.Segmentation'&gt;
[2022-11-30 19:50:18,518] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation_spleen.SegmentationSpleen'&gt;
[2022-11-30 19:50:18,518] [12856] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation_vertebra.SegmentationVertebra'&gt;
[2022-11-30 19:50:18,518] [12856] [MainThread] [INFO] (main:93) - +++ Adding Model: segmentation =&gt; lib.configs.segmentation.Segmentation
[2022-11-30 19:50:18,581] [12856] [MainThread] [INFO] (main:96) - +++ Using Models: ['segmentation']
[2022-11-30 19:50:18,581] [12856] [MainThread] [INFO] (monailabel.interfaces.app:129) - Init Datastore for: C:\Users\xgzxe\my_dataset
[2022-11-30 19:50:18,581] [12856] [MainThread] [INFO] (monailabel.datastore.local:129) - Auto Reload: True; Extensions: ['*.nii.gz', '*.nii', '*.nrrd', '*.jpg', '*.png', '*.tif', '*.svs', '*.xml']
[2022-11-30 19:50:18,612] [12856] [MainThread] [INFO] (monailabel.datastore.local:576) - Invalidate count: 0
[2022-11-30 19:50:18,612] [12856] [MainThread] [INFO] (monailabel.datastore.local:150) - Start observing external modifications on datastore (AUTO RELOAD)
[2022-11-30 19:50:18,628] [12856] [MainThread] [INFO] (main:126) - +++ Adding Inferer:: segmentation =&gt; &lt;lib.infers.segmentation.Segmentation object at 0x000001B03C4BCD00&gt;
[2022-11-30 19:50:18,628] [12856] [MainThread] [INFO] (main:191) - {'segmentation': &lt;lib.infers.segmentation.Segmentation object at 0x000001B03C4BCD00&gt;, 'Histogram+GraphCut': &lt;monailabel.scribbles.infer.HistogramBasedGraphCut object at 0x000001B03D18CB20&gt;, 'GMM+GraphCut': &lt;monailabel.scribbles.infer.GMMBasedGraphCut object at 0x000001B03D18CAF0&gt;}
[2022-11-30 19:50:18,628] [12856] [MainThread] [INFO] (main:206) - +++ Adding Trainer:: segmentation =&gt; &lt;lib.trainers.segmentation.Segmentation object at 0x000001B03D452A00&gt;
[2022-11-30 19:50:18,644] [12856] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: C:\Users\xgzxe\.cache\monailabel\sessions
[2022-11-30 19:50:18,644] [12856] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2022-11-30 19:50:18,644] [12856] [MainThread] [INFO] (monailabel.interfaces.app:468) - App Init - completed
[2022-11-30 19:50:18,644] [timeloop] [INFO] Starting Timeloop..
[2022-11-30 19:50:18,644] [12856] [MainThread] [INFO] (timeloop:60) - Starting Timeloop..
[2022-11-30 19:50:18,644] [timeloop] [INFO] Registered job &lt;function MONAILabelApp.on_init_complete.&lt;locals&gt;.run_scheduler at 0x000001B03C528F70&gt;
[2022-11-30 19:50:18,644] [12856] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete.&lt;locals&gt;.run_scheduler at 0x000001B03C528F70&gt;
[2022-11-30 19:50:18,644] [timeloop] [INFO] Timeloop now started. Jobs will run based on the interval set
[2022-11-30 19:50:18,644] [12856] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set
[2022-11-30 19:50:18,659] [12856] [MainThread] [INFO] (uvicorn.error:59) - Application startup complete.
[2022-11-30 19:50:18,675] [12856] [MainThread] [INFO] (uvicorn.error:206) - Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
[2022-11-30 19:53:26,485] [12856] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {'strategy': 'random', 'client_id': 'user-xyz'}
[2022-11-30 19:53:26,488] [12856] [MainThread] [INFO] (monailabel.tasks.activelearning.random:47) - Random: Selected Image: image7; Weight: 152398
[2022-11-30 19:53:26,497] [12856] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {'id': 'image7', 'weight': 152398, 'path': 'C:\\Users\\xgzxe\\my_dataset\\image7.nii.gz', 'ts': 1669639040, 'name': 'image7.nii.gz', 'strategy': {'random': {'ts': 1669809206, 'client_id': 'user-xyz'}}}
[2022-11-30 21:30:56,492] [12856] [MainThread] [INFO] (monailabel.endpoints.datastore:100) - Saving Label for image7 for tag: final by admin
[2022-11-30 21:30:56,494] [12856] [MainThread] [INFO] (monailabel.endpoints.datastore:111) - Save Label params: {"label_info": [{"name": "aorta", "idx": 1}], "client_id": "user-xyz"}
[2022-11-30 21:30:56,494] [12856] [MainThread] [INFO] (monailabel.datastore.local:485) - Saving Label for Image: image7; Tag: final; Info: {'label_info': [{'name': 'aorta', 'idx': 1}], 'client_id': 'user-xyz'}
[2022-11-30 21:30:56,495] [12856] [MainThread] [INFO] (monailabel.datastore.local:493) - Adding Label: image7 =&gt; final =&gt; C:\Users\xgzxe\AppData\Local\Temp\tmpyobzgp06.nii.gz
[2022-11-30 21:30:56,506] [12856] [MainThread] [INFO] (monailabel.datastore.local:509) - Label Info: {'label_info': [{'name': 'aorta', 'idx': 1}], 'client_id': 'user-xyz', 'ts': 1669815056, 'checksum': 'SHA256:debba0c8b04ddc732a1a3f7708564cee6b180b49c56fd1312dae5e74f2748c68', 'name': 'image7.nii.gz'}
[2022-11-30 21:30:56,507] [12856] [MainThread] [INFO] (monailabel.interfaces.app:492) - New label saved for: image7 =&gt; image7
[2022-11-30 21:30:56,575] [12856] [Thread-1] [INFO] (monailabel.datastore.local:576) - Invalidate count: 0
[2022-11-30 21:31:11,929] [12856] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {'strategy': 'random', 'client_id': 'user-xyz'}
[2022-11-30 21:31:11,930] [12856] [MainThread] [INFO] (monailabel.tasks.activelearning.random:47) - Random: Selected Image: image10; Weight: 158263
[2022-11-30 21:31:11,933] [12856] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {'id': 'image10', 'weight': 158263, 'path': 'C:\\Users\\xgzxe\\my_dataset\\image10.nii.gz', 'ts': 1669639040, 'name': 'image10.nii.gz', 'strategy': {'random': {'ts': 1669815071, 'client_id': 'user-xyz'}}}
[2022-11-30 22:23:43,614] [12856] [MainThread] [INFO] (monailabel.endpoints.datastore:100) - Saving Label for image10 for tag: final by admin
[2022-11-30 22:23:43,616] [12856] [MainThread] [INFO] (monailabel.endpoints.datastore:111) - Save Label params: {"label_info": [{"name": "aorta", "idx": 1}], "client_id": "user-xyz"}
[2022-11-30 22:23:43,616] [12856] [MainThread] [INFO] (monailabel.datastore.local:485) - Saving Label for Image: image10; Tag: final; Info: {'label_info': [{'name': 'aorta', 'idx': 1}], 'client_id': 'user-xyz'}
[2022-11-30 22:23:43,617] [12856] [MainThread] [INFO] (monailabel.datastore.local:493) - Adding Label: image10 =&gt; final =&gt; C:\Users\xgzxe\AppData\Local\Temp\tmpmdhw3xxx.nii.gz
[2022-11-30 22:23:43,630] [12856] [MainThread] [INFO] (monailabel.datastore.local:509) - Label Info: {'label_info': [{'name': 'aorta', 'idx': 1}], 'client_id': 'user-xyz', 'ts': 1669818223, 'checksum': 'SHA256:b2d81b61049ebcca4087ee825f266ba4fa20684383cc176da4c5b8b233ca779c', 'name': 'image10.nii.gz'}
[2022-11-30 22:23:43,632] [12856] [MainThread] [INFO] (monailabel.interfaces.app:492) - New label saved for: image10 =&gt; image10
[2022-11-30 22:23:43,686] [12856] [Thread-1] [INFO] (monailabel.datastore.local:576) - Invalidate count: 0
[2022-11-30 22:24:47,694] [12856] [MainThread] [INFO] (monailabel.utils.async_tasks.task:36) - Train request: {'model': 'segmentation', 'name': 'train_01', 'pretrained': True, 'device': 'cuda', 'max_epochs': 50, 'early_stop_patience': -1, 'val_split': 0.2, 'train_batch_size': 1, 'val_batch_size': 1, 'multi_gpu': True, 'gpus': 'all', 'dataset': 'SmartCacheDataset', 'dataloader': 'ThreadDataLoader', 'client_id': 'user-xyz'}
[2022-11-30 22:24:47,696] [12856] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:59) - COMMAND:: C:\Users\xgzxe\anaconda3\envs\monailabel\python.exe -m monailabel.interfaces.utils.app -m train -r {"model":"segmentation","name":"train_01","pretrained":true,"device":"cuda","max_epochs":50,"early_stop_patience":-1,"val_split":0.2,"train_batch_size":1,"val_batch_size":1,"multi_gpu":true,"gpus":"all","dataset":"SmartCacheDataset","dataloader":"ThreadDataLoader","client_id":"user-xyz"}
[2022-11-30 22:24:47,909] [3788] [MainThread] [INFO] (__main__:38) - Initializing App from: C:\Users\xgzxe\radiology; studies: C:\Users\xgzxe\my_dataset; conf: {'models': 'segmentation'}
[2022-11-30 22:24:51,224] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2022-11-30 22:24:51,234] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepedit.DeepEdit'&gt;
[2022-11-30 22:24:51,235] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepgrow_2d.Deepgrow2D'&gt;
[2022-11-30 22:24:51,236] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepgrow_3d.Deepgrow3D'&gt;
[2022-11-30 22:24:51,236] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.localization_spine.LocalizationSpine'&gt;
[2022-11-30 22:24:51,237] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.localization_vertebra.LocalizationVertebra'&gt;
[2022-11-30 22:24:51,237] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation.Segmentation'&gt;
[2022-11-30 22:24:51,238] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation_spleen.SegmentationSpleen'&gt;
[2022-11-30 22:24:51,239] [3788] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation_vertebra.SegmentationVertebra'&gt;
[2022-11-30 22:24:51,239] [3788] [MainThread] [INFO] (main:93) - +++ Adding Model: segmentation =&gt; lib.configs.segmentation.Segmentation
[2022-11-30 22:24:51,271] [3788] [MainThread] [INFO] (main:96) - +++ Using Models: ['segmentation']
[2022-11-30 22:24:51,271] [3788] [MainThread] [INFO] (monailabel.interfaces.app:129) - Init Datastore for: C:\Users\xgzxe\my_dataset
[2022-11-30 22:24:51,271] [3788] [MainThread] [INFO] (monailabel.datastore.local:129) - Auto Reload: False; Extensions: ['*.nii.gz', '*.nii', '*.nrrd', '*.jpg', '*.png', '*.tif', '*.svs', '*.xml']
[2022-11-30 22:24:51,283] [3788] [MainThread] [INFO] (monailabel.datastore.local:576) - Invalidate count: 0
[2022-11-30 22:24:51,283] [3788] [MainThread] [INFO] (main:126) - +++ Adding Inferer:: segmentation =&gt; &lt;lib.infers.segmentation.Segmentation object at 0x000001EB31E36790&gt;
[2022-11-30 22:24:51,284] [3788] [MainThread] [INFO] (main:191) - {'segmentation': &lt;lib.infers.segmentation.Segmentation object at 0x000001EB31E36790&gt;, 'Histogram+GraphCut': &lt;monailabel.scribbles.infer.HistogramBasedGraphCut object at 0x000001EB341C2940&gt;, 'GMM+GraphCut': &lt;monailabel.scribbles.infer.GMMBasedGraphCut object at 0x000001EB341C2910&gt;}
[2022-11-30 22:24:51,284] [3788] [MainThread] [INFO] (main:206) - +++ Adding Trainer:: segmentation =&gt; &lt;lib.trainers.segmentation.Segmentation object at 0x000001EB341C29D0&gt;
[2022-11-30 22:24:51,284] [3788] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: C:\Users\xgzxe\.cache\monailabel\sessions
[2022-11-30 22:24:51,284] [3788] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2022-11-30 22:24:51,284] [3788] [MainThread] [INFO] (monailabel.tasks.train.basic_train:390) - Train Request (input): {'model': 'segmentation', 'name': 'train_01', 'pretrained': True, 'device': 'cuda', 'max_epochs': 50, 'early_stop_patience': -1, 'val_split': 0.2, 'train_batch_size': 1, 'val_batch_size': 1, 'multi_gpu': True, 'gpus': 'all', 'dataset': 'SmartCacheDataset', 'dataloader': 'ThreadDataLoader', 'client_id': 'user-xyz', 'local_rank': 0}
[2022-11-30 22:24:51,284] [3788] [MainThread] [INFO] (monailabel.tasks.train.basic_train:400) - CUDA_VISIBLE_DEVICES: None
[2022-11-30 22:24:51,285] [3788] [MainThread] [INFO] (monailabel.tasks.train.basic_train:405) - Distributed/Multi GPU is limited
[2022-11-30 22:24:51,285] [3788] [MainThread] [INFO] (monailabel.tasks.train.basic_train:420) - Distributed Training = FALSE
[2022-11-30 22:24:51,285] [3788] [MainThread] [INFO] (monailabel.tasks.train.basic_train:447) - 0 - Train Request (final): {'name': 'train_01', 'pretrained': True, 'device': 'cuda', 'max_epochs': 50, 'early_stop_patience': -1, 'val_split': 0.2, 'train_batch_size': 1, 'val_batch_size': 1, 'multi_gpu': False, 'gpus': 'all', 'dataset': 'SmartCacheDataset', 'dataloader': 'ThreadDataLoader', 'model': 'segmentation', 'client_id': 'user-xyz', 'local_rank': 0, 'run_id': '20221130_2224'}
[2022-11-30 22:24:51,285] [3788] [MainThread] [INFO] (monailabel.tasks.train.basic_train:555) - 0 - Using Device: cpu; IDX: None
[2022-11-30 22:24:51,285] [3788] [MainThread] [INFO] (monailabel.tasks.train.basic_train:368) - Total Records for Training: 4
[2022-11-30 22:24:51,285] [3788] [MainThread] [INFO] (monailabel.tasks.train.basic_train:369) - Total Records for Validation: 1
Loading dataset:   0%|          | 0/1 [00:00&lt;?, ?it/s]
Loading dataset:   0%|          | 0/1 [00:10&lt;?, ?it/s]
Traceback (most recent call last):
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\transforms\transform.py", line 91, in apply_transform
    return _apply_transform(transform, data, unpack_items)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\transforms\transform.py", line 55, in _apply_transform
    return transform(parameters)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\transforms\io\dictionary.py", line 154, in __call__
    data = self._loader(d[key], reader)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\transforms\io\array.py", line 271, in __call__
    meta_data = switch_endianness(meta_data, "&lt;")
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\transforms\io\array.py", line 84, in switch_endianness
    data = {k: switch_endianness(v, new) for k, v in data.items()}
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\transforms\io\array.py", line 84, in &lt;dictcomp&gt;
    data = {k: switch_endianness(v, new) for k, v in data.items()}
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\transforms\io\array.py", line 86, in switch_endianness
    raise RuntimeError(f"Unknown type: {type(data).__name__}")
RuntimeError: Unknown type: itkMatrixF44
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monailabel\interfaces\utils\app.py", line 132, in &lt;module&gt;
    run_main()
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monailabel\interfaces\utils\app.py", line 117, in run_main
    result = a.train(request)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monailabel\interfaces\app.py", line 422, in train
    result = task(request, self.datastore())
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monailabel\tasks\train\basic_train.py", line 421, in __call__
    res = self.train(0, world_size, req, datalist)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monailabel\tasks\train\basic_train.py", line 478, in train
    context.evaluator = self._create_evaluator(context)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monailabel\tasks\train\basic_train.py", line 591, in _create_evaluator
    val_data_loader=self.val_data_loader(context),
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monailabel\tasks\train\basic_train.py", line 295, in val_data_loader
    dataset, datalist = self._dataset(context, context.val_datalist, is_train=False)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monailabel\tasks\train\basic_train.py", line 217, in _dataset
    else SmartCacheDataset(datalist, transforms, replace_rate)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\data\dataset.py", line 979, in __init__
    super().__init__(data, transform, cache_num, cache_rate, num_init_workers, progress, copy_cache, as_contiguous)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\data\dataset.py", line 793, in __init__
    self.set_data(data)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\data\dataset.py", line 1013, in set_data
    super().set_data(data)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\data\dataset.py", line 818, in set_data
    self._cache = _compute_cache()
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\data\dataset.py", line 807, in _compute_cache
    return self._fill_cache()
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\data\dataset.py", line 827, in _fill_cache
    return list(
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\tqdm\std.py", line 1195, in __iter__
    for obj in iterable:
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\multiprocessing\pool.py", line 870, in next
    raise value
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\multiprocessing\pool.py", line 125, in worker
    result = (True, func(*args, **kwds))
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\data\dataset.py", line 847, in _load_cache_item
    item = apply_transform(_xform, item)
  File "C:\Users\xgzxe\anaconda3\envs\monailabel\lib\site-packages\monai\transforms\transform.py", line 118, in apply_transform
    raise RuntimeError(f"applying transform {transform}") from e
RuntimeError: applying transform &lt;monai.transforms.io.dictionary.LoadImaged object at 0x000001EB09410400&gt;
[2022-11-30 22:25:02,068] [12856] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:77) - Return code: 1
</code></pre>
<p>Please tell me how can i solve this problem, thanks.</p>

---

## Post #4 by @diazandr3s (2022-11-30 18:53 UTC)

<aside class="quote no-group" data-username="chendong9416" data-post="3" data-topic="26460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c2a13f/48.png" class="avatar"> chendong9416:</div>
<blockquote>
<p><code>RuntimeError: Unknown type: itkMatrixF44</code></p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/chendong9416">@chendong9416</a>,</p>
<p>Which Python version are you using? Can you please make sure you’re using 3.7/3.8/3.9 python versions?</p>
<p>It seems there are some issues with Python 3.10 support. Not everything is compatible with itk or some other libraries.</p>

---

## Post #5 by @chendong9416 (2022-11-30 22:37 UTC)

<p>i am using python 3.9</p>

---

## Post #6 by @diazandr3s (2022-12-01 03:20 UTC)

<aside class="quote no-group" data-username="chendong9416" data-post="3" data-topic="26460">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/c2a13f/48.png" class="avatar"> chendong9416:</div>
<blockquote>
<p>RuntimeError: Unknown type: itkMatrixF44</p>
</blockquote>
</aside>
<p>We’ve seen this issue before and it was solved by creating a python virtual env with Python 3.9 version. Please see here: <a href="https://github.com/Project-MONAI/MONAILabel/issues/1064#issuecomment-1277232006" class="inline-onebox" rel="noopener nofollow ugc">RuntimeError: Unknown type: itkMatrixF44 · Issue #1064 · Project-MONAI/MONAILabel · GitHub</a></p>

---

## Post #7 by @chendong9416 (2022-12-03 01:45 UTC)

<p>Ok, i will try this way</p>

---
