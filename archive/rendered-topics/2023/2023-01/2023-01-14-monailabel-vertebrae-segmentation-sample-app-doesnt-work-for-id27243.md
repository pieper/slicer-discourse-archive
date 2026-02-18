# MonaiLabel vertebrae segmentation sample-app doesn't work for sample data

**Topic ID**: 27243
**Date**: 2023-01-14
**URL**: https://discourse.slicer.org/t/monailabel-vertebrae-segmentation-sample-app-doesnt-work-for-sample-data/27243

---

## Post #1 by @mau_igna_06 (2023-01-14 21:11 UTC)

<p>After clicking Run Auto Segmentation, the segments of the segmentationNode are still empty.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/084cdcbc9f21b6f20a6655b28424db88989b0b6e.jpeg" data-download-href="/uploads/short-url/1bquM5Bdyi4XLPBaWQArtAJITIW.jpeg?dl=1" title="Captura desde 2023-01-14 18-05-19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/084cdcbc9f21b6f20a6655b28424db88989b0b6e_2_690x388.jpeg" alt="Captura desde 2023-01-14 18-05-19" data-base62-sha1="1bquM5Bdyi4XLPBaWQArtAJITIW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/084cdcbc9f21b6f20a6655b28424db88989b0b6e_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/084cdcbc9f21b6f20a6655b28424db88989b0b6e_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/084cdcbc9f21b6f20a6655b28424db88989b0b6e_2_1380x776.jpeg 2x" data-dominant-color="9D9DA5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura desde 2023-01-14 18-05-19</span><span class="informations">1920×1080 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Another CT I tried only segmented half a vertebrae.</p>
<p>If I try segmentation_vertebrae model instead the monai-label server crashes</p>
<p>Here is the console output for localization_spine</p>
<pre><code class="lang-auto">~$ monailabel start_server --app /home/user1/Escritorio/Monai/apps/radiology --studies /home/user1/Escritorio/Monai/datasets/vertebrae/imagesTr --conf models "localization_spine,localization_vertebra,segmentation_vertebra"
Using PYTHONPATH=/home/user1:

2023-01-14 17:57:49,144 - USING:: version = False
2023-01-14 17:57:49,144 - USING:: app = /home/user1/Escritorio/Monai/apps/radiology
2023-01-14 17:57:49,144 - USING:: studies = /home/user1/Escritorio/Monai/datasets/vertebrae/imagesTr
2023-01-14 17:57:49,144 - USING:: verbose = INFO
2023-01-14 17:57:49,144 - USING:: conf = [['models', 'localization_spine,localization_vertebra,segmentation_vertebra']]
2023-01-14 17:57:49,144 - USING:: host = 0.0.0.0
2023-01-14 17:57:49,144 - USING:: port = 8000
2023-01-14 17:57:49,144 - USING:: uvicorn_app = monailabel.app:app
2023-01-14 17:57:49,144 - USING:: ssl_keyfile = None
2023-01-14 17:57:49,144 - USING:: ssl_certfile = None
2023-01-14 17:57:49,144 - USING:: ssl_keyfile_password = None
2023-01-14 17:57:49,144 - USING:: ssl_ca_certs = None
2023-01-14 17:57:49,144 - USING:: workers = None
2023-01-14 17:57:49,144 - USING:: limit_concurrency = None
2023-01-14 17:57:49,144 - USING:: access_log = False
2023-01-14 17:57:49,144 - USING:: log_config = None
2023-01-14 17:57:49,144 - USING:: dryrun = False
2023-01-14 17:57:49,144 - USING:: action = start_server
2023-01-14 17:57:49,144 - ENV SETTINGS:: MONAI_LABEL_API_STR = 
2023-01-14 17:57:49,144 - ENV SETTINGS:: MONAI_LABEL_PROJECT_NAME = MONAILabel
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_APP_DIR = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_STUDIES = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_AUTH_ENABLE = False
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_AUTH_DB = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_APP_CONF = '{}'
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_TASKS_TRAIN = True
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_TASKS_STRATEGY = True
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_TASKS_SCORING = True
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_TASKS_BATCH_INFER = True
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_URL = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_USERNAME = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PASSWORD = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_API_KEY = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_CACHE_PATH = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PROJECT = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_ASSET_PATH = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_DSA_ANNOTATION_GROUPS = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_USERNAME = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PASSWORD = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_PATH = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_QIDO_PREFIX = None
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_WADO_PREFIX = None
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_STOW_PREFIX = None
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_FETCH_BY_FRAME = False
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CONVERT_TO_NIFTI = True
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_SEARCH_FILTER = '{"Modality": "CT"}'
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_EXPIRY = 180
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PROXY_TIMEOUT = 30.0
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_READ_TIMEOUT = 5.0
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_AUTO_RELOAD = True
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_READ_ONLY = False
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_FILE_EXT = '["*.nii.gz", "*.nii", "*.nrrd", "*.jpg", "*.png", "*.tif", "*.svs", "*.xml"]'
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_SERVER_PORT = 8000
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_CORS_ORIGINS = '[]'
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_SESSIONS = True
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_SESSION_PATH = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_SESSION_EXPIRY = 3600
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_INFER_CONCURRENCY = -1
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_INFER_TIMEOUT = 600
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_TRACKING_ENABLED = True
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_TRACKING_URI = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_ZOO_SOURCE = github
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_ZOO_REPO = Project-MONAI/model-zoo/hosting_storage_v1
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_ZOO_AUTH_TOKEN = 
2023-01-14 17:57:49,145 - ENV SETTINGS:: MONAI_LABEL_AUTO_UPDATE_SCORING = True
2023-01-14 17:57:49,145 - 
Allow Origins: ['*']
[2023-01-14 17:57:49,432] [850291] [MainThread] [INFO] (uvicorn.error:75) - Started server process [850291]
[2023-01-14 17:57:49,432] [850291] [MainThread] [INFO] (uvicorn.error:45) - Waiting for application startup.
[2023-01-14 17:57:49,432] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: /home/user1/Escritorio/Monai/apps/radiology; studies: /home/user1/Escritorio/Monai/datasets/vertebrae/imagesTr; conf: {'models': 'localization_spine,localization_vertebra,segmentation_vertebra'}
[2023-01-14 17:57:49,455] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2023-01-14 17:57:49,458] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepgrow_3d.Deepgrow3D'&gt;
[2023-01-14 17:57:49,459] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepedit.DeepEdit'&gt;
[2023-01-14 17:57:49,459] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.localization_vertebra.LocalizationVertebra'&gt;
[2023-01-14 17:57:49,459] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation_spleen.SegmentationSpleen'&gt;
[2023-01-14 17:57:49,459] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepgrow_2d.Deepgrow2D'&gt;
[2023-01-14 17:57:49,459] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation_vertebra.SegmentationVertebra'&gt;
[2023-01-14 17:57:49,459] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation.Segmentation'&gt;
[2023-01-14 17:57:49,460] [850291] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.localization_spine.LocalizationSpine'&gt;
[2023-01-14 17:57:49,460] [850291] [MainThread] [INFO] (main:93) - +++ Adding Model: localization_spine =&gt; lib.configs.localization_spine.LocalizationSpine
[2023-01-14 17:57:49,564] [850291] [MainThread] [INFO] (main:93) - +++ Adding Model: localization_vertebra =&gt; lib.configs.localization_vertebra.LocalizationVertebra
[2023-01-14 17:57:49,648] [850291] [MainThread] [INFO] (main:93) - +++ Adding Model: segmentation_vertebra =&gt; lib.configs.segmentation_vertebra.SegmentationVertebra
[2023-01-14 17:57:49,733] [850291] [MainThread] [INFO] (main:96) - +++ Using Models: ['localization_spine', 'localization_vertebra', 'segmentation_vertebra']
[2023-01-14 17:57:49,733] [850291] [MainThread] [INFO] (monailabel.interfaces.app:135) - Init Datastore for: /home/user1/Escritorio/Monai/datasets/vertebrae/imagesTr
[2023-01-14 17:57:49,733] [850291] [MainThread] [INFO] (monailabel.datastore.local:129) - Auto Reload: True; Extensions: ['*.nii.gz', '*.nii', '*.nrrd', '*.jpg', '*.png', '*.tif', '*.svs', '*.xml']
[2023-01-14 17:57:49,734] [850291] [MainThread] [INFO] (monailabel.datastore.local:593) - Adding New Image: CTChest =&gt; CTChest.nii.gz
[2023-01-14 17:57:49,734] [850291] [MainThread] [INFO] (monailabel.datastore.local:576) - Invalidate count: 1
[2023-01-14 17:57:49,735] [850291] [MainThread] [INFO] (monailabel.datastore.local:150) - Start observing external modifications on datastore (AUTO RELOAD)
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (main:126) - +++ Adding Inferer:: localization_spine =&gt; &lt;lib.infers.localization_spine.LocalizationSpine object at 0x7fb1700a5f30&gt;
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (main:126) - +++ Adding Inferer:: localization_vertebra =&gt; &lt;lib.infers.localization_vertebra.LocalizationVertebra object at 0x7fb16cb0d480&gt;
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (main:126) - +++ Adding Inferer:: segmentation_vertebra =&gt; &lt;lib.infers.segmentation_vertebra.SegmentationVertebra object at 0x7fb16cb0d4b0&gt;
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (main:191) - {'localization_spine': &lt;lib.infers.localization_spine.LocalizationSpine object at 0x7fb1700a5f30&gt;, 'localization_vertebra': &lt;lib.infers.localization_vertebra.LocalizationVertebra object at 0x7fb16cb0d480&gt;, 'segmentation_vertebra': &lt;lib.infers.segmentation_vertebra.SegmentationVertebra object at 0x7fb16cb0d4b0&gt;, 'Histogram+GraphCut': &lt;monailabel.scribbles.infer.HistogramBasedGraphCut object at 0x7fb16cb0e560&gt;, 'GMM+GraphCut': &lt;monailabel.scribbles.infer.GMMBasedGraphCut object at 0x7fb16cb0e590&gt;, 'vertebra_pipeline': &lt;lib.infers.vertebra_pipeline.InferVertebraPipeline object at 0x7fb16cb0e5f0&gt;}
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (main:206) - +++ Adding Trainer:: localization_spine =&gt; &lt;lib.trainers.localization_spine.LocalizationSpine object at 0x7fb16cb0d8d0&gt;
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (main:206) - +++ Adding Trainer:: localization_vertebra =&gt; &lt;lib.trainers.localization_vertebra.LocalizationVertebra object at 0x7fb16cb0d780&gt;
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (main:206) - +++ Adding Trainer:: segmentation_vertebra =&gt; &lt;lib.trainers.segmentation_vertebra.SegmentationVertebra object at 0x7fb16cb0d7e0&gt;
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /home/user1/.cache/monailabel/sessions
[2023-01-14 17:57:49,736] [850291] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2023-01-14 17:57:49,737] [850291] [MainThread] [INFO] (monailabel.interfaces.app:475) - App Init - completed
[2023-01-14 17:57:49,737] [timeloop] [INFO] Starting Timeloop..
[2023-01-14 17:57:49,737] [850291] [MainThread] [INFO] (timeloop:60) - Starting Timeloop..
[2023-01-14 17:57:49,737] [timeloop] [INFO] Registered job &lt;function MONAILabelApp.on_init_complete.&lt;locals&gt;.run_scheduler at 0x7fb16d05cc10&gt;
[2023-01-14 17:57:49,737] [850291] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete.&lt;locals&gt;.run_scheduler at 0x7fb16d05cc10&gt;
[2023-01-14 17:57:49,737] [timeloop] [INFO] Timeloop now started. Jobs will run based on the interval set
[2023-01-14 17:57:49,737] [850291] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set
[2023-01-14 17:57:49,737] [850291] [MainThread] [INFO] (uvicorn.error:59) - Application startup complete.
[2023-01-14 17:57:49,737] [850291] [MainThread] [INFO] (uvicorn.error:206) - Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
[2023-01-14 17:58:05,865] [850291] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {'strategy': 'random', 'client_id': 'user-xyz'}
[2023-01-14 17:58:05,865] [850291] [MainThread] [INFO] (monailabel.tasks.activelearning.random:47) - Random: Selected Image: CTChest; Weight: 6180
[2023-01-14 17:58:05,865] [850291] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {'id': 'CTChest', 'weight': 6180, 'path': '/home/user1/Escritorio/Monai/datasets/vertebrae/imagesTr/CTChest.nii.gz', 'ts': 1673729869, 'name': 'CTChest.nii.gz'}
[2023-01-14 17:58:13,440] [850291] [MainThread] [INFO] (monailabel.endpoints.infer:160) - Infer Request: {'model': 'localization_spine', 'image': 'CTChest', 'device': 'cpu', 'result_extension': '.nrrd', 'result_dtype': 'uint8', 'client_id': 'user-xyz'}
[2023-01-14 17:58:13,440] [850291] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:279) - Infer Request (final): {'device': 'cpu', 'model': 'localization_spine', 'image': '/home/user1/Escritorio/Monai/datasets/vertebrae/imagesTr/CTChest.nii.gz', 'result_extension': '.nrrd', 'result_dtype': 'uint8', 'client_id': 'user-xyz', 'description': 'A pre-trained model for volumetric (3D) spine localization from CT image'}
[2023-01-14 17:58:13,441] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:76) - PRE - Run Transform(s)
[2023-01-14 17:58:13,441] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - PRE - Input Keys: ['device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path']
[2023-01-14 17:58:15,869] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (LoadImaged): Time: 2.4272; image: torch.Size([512, 512, 139])(torch.float32)
[2023-01-14 17:58:15,870] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (EnsureTyped): Time: 0.0009; image: torch.Size([512, 512, 139])(torch.float32)
[2023-01-14 17:58:15,870] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (EnsureChannelFirstd): Time: 0.0001; image: torch.Size([1, 512, 512, 139])(torch.float32)
[2023-01-14 17:58:15,884] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (CacheObjectd): Time: 0.0134; image: torch.Size([1, 512, 512, 139])(torch.float32)
[2023-01-14 17:58:16,779] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (Spacingd): Time: 0.8947; image: torch.Size([1, 300, 300, 266])(torch.float32)
[2023-01-14 17:58:16,836] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (ScaleIntensityRanged): Time: 0.0569; image: torch.Size([1, 300, 300, 266])(torch.float32)
[2023-01-14 17:58:17,448] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (GaussianSmoothd): Time: 0.6115; image: torch.Size([1, 300, 300, 266])(torch.float32)
[2023-01-14 17:58:17,494] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (ScaleIntensityd): Time: 0.0461; image: torch.Size([1, 300, 300, 266])(torch.float32)
[2023-01-14 17:58:17,494] [850291] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:471) - Inferer:: cpu =&gt; SlidingWindowInferer =&gt; {'roi_size': (96, 96, 96), 'sw_batch_size': 2, 'overlap': 0.4, 'mode': gaussian, 'sigma_scale': 0.125, 'padding_mode': 'replicate', 'cval': 0.0, 'sw_device': None, 'device': None, 'progress': False, 'cpu_thresh': None, 'roi_weight_map': None}
[2023-01-14 17:58:17,494] [850291] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:420) - Infer model path: /home/user1/Escritorio/Monai/apps/radiology/model/pretrained_localization_spine.pt
[2023-01-14 18:00:39,455] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:76) - POST - Run Transform(s)
[2023-01-14 18:00:39,455] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - POST - Input Keys: ['device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path', 'image_meta_dict', 'latencies', 'image_cached', 'pred']
[2023-01-14 18:00:39,455] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (EnsureTyped): Time: 0.0001; image: torch.Size([1, 300, 300, 266])(torch.float32); pred: torch.Size([25, 300, 300, 266])(torch.float32)
[2023-01-14 18:00:39,759] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (Activationsd): Time: 0.3031; image: torch.Size([1, 300, 300, 266])(torch.float32); pred: torch.Size([25, 300, 300, 266])(torch.float32)
[2023-01-14 18:00:42,576] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (AsDiscreted): Time: 2.8175; image: torch.Size([1, 300, 300, 266])(torch.float32); pred: torch.Size([1, 300, 300, 266])(torch.float32)
[2023-01-14 18:00:42,839] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (KeepLargestConnectedComponentd): Time: 0.2623; image: torch.Size([1, 300, 300, 266])(torch.float32); pred: torch.Size([1, 300, 300, 266])(torch.float32)
[2023-01-14 18:00:42,844] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (BinaryMaskd): Time: 0.0051; image: torch.Size([1, 300, 300, 266])(torch.float32); pred: torch.Size([1, 300, 300, 266])(torch.float32)
[2023-01-14 18:00:42,938] [850291] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (Restored): Time: 0.094; image: torch.Size([1, 300, 300, 266])(torch.float32); pred: torch.Size([512, 512, 139])(torch.float32)
[2023-01-14 18:00:43,013] [850291] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:571) - Writing Result...
[2023-01-14 18:00:43,014] [850291] [MainThread] [INFO] (monailabel.transform.writer:189) - Result ext: .nrrd; write_to_file: True; dtype: uint8
[2023-01-14 18:00:43,213] [850291] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:334) - ++ Latencies =&gt; Total: 149.7728; Pre: 4.0537; Inferer: 141.9601; Invert: 0.0000; Post: 3.5590; Write: 0.1997
[2023-01-14 18:00:43,213] [850291] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:358) - Result File: /tmp/tmpt87i1c7f.nrrd
[2023-01-14 18:00:43,213] [850291] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:359) - Result Json Keys: ['label_names', 'latencies']
</code></pre>
<p>Thanks for the help</p>

---

## Post #2 by @mau_igna_06 (2023-01-20 15:55 UTC)

<p>Hi</p>
<p>The server does work for sample radiology app “segmentation_spleen” on the same virtualenviroment</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c87b95d9bd26bba21d0cc21e26757e780fcb68ad.jpeg" data-download-href="/uploads/short-url/sByh18ouQhdh2JthsL56ySowe0R.jpeg?dl=1" title="Captura desde 2023-01-20 12-16-22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c87b95d9bd26bba21d0cc21e26757e780fcb68ad_2_690x388.jpeg" alt="Captura desde 2023-01-20 12-16-22" data-base62-sha1="sByh18ouQhdh2JthsL56ySowe0R" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c87b95d9bd26bba21d0cc21e26757e780fcb68ad_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c87b95d9bd26bba21d0cc21e26757e780fcb68ad_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c87b95d9bd26bba21d0cc21e26757e780fcb68ad_2_1380x776.jpeg 2x" data-dominant-color="8F8F97"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura desde 2023-01-20 12-16-22</span><span class="informations">1920×1080 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">~/Escritorio/Monai$ monailabel start_server --app apps/radiology --studies datasets/Task09_Spleen/imagesTr --conf models segmentation_spleen
Using PYTHONPATH=/home/user1:

2023-01-20 12:13:57,337 - USING:: version = False
2023-01-20 12:13:57,337 - USING:: app = /home/user1/Escritorio/Monai/apps/radiology
2023-01-20 12:13:57,337 - USING:: studies = /home/user1/Escritorio/Monai/datasets/Task09_Spleen/imagesTr
2023-01-20 12:13:57,337 - USING:: verbose = INFO
2023-01-20 12:13:57,337 - USING:: conf = [['models', 'segmentation_spleen']]
2023-01-20 12:13:57,337 - USING:: host = 0.0.0.0
2023-01-20 12:13:57,337 - USING:: port = 8000
2023-01-20 12:13:57,337 - USING:: uvicorn_app = monailabel.app:app
2023-01-20 12:13:57,337 - USING:: ssl_keyfile = None
2023-01-20 12:13:57,337 - USING:: ssl_certfile = None
2023-01-20 12:13:57,337 - USING:: ssl_keyfile_password = None
2023-01-20 12:13:57,337 - USING:: ssl_ca_certs = None
2023-01-20 12:13:57,337 - USING:: workers = None
2023-01-20 12:13:57,337 - USING:: limit_concurrency = None
2023-01-20 12:13:57,337 - USING:: access_log = False
2023-01-20 12:13:57,337 - USING:: log_config = None
2023-01-20 12:13:57,337 - USING:: dryrun = False
2023-01-20 12:13:57,337 - USING:: action = start_server
2023-01-20 12:13:57,337 - ENV SETTINGS:: MONAI_LABEL_API_STR = 
2023-01-20 12:13:57,337 - ENV SETTINGS:: MONAI_LABEL_PROJECT_NAME = MONAILabel
2023-01-20 12:13:57,337 - ENV SETTINGS:: MONAI_LABEL_APP_DIR = 
2023-01-20 12:13:57,337 - ENV SETTINGS:: MONAI_LABEL_STUDIES = 
2023-01-20 12:13:57,337 - ENV SETTINGS:: MONAI_LABEL_AUTH_ENABLE = False
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_AUTH_DB = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_APP_CONF = '{}'
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_TASKS_TRAIN = True
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_TASKS_STRATEGY = True
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_TASKS_SCORING = True
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_TASKS_BATCH_INFER = True
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_URL = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_USERNAME = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PASSWORD = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_API_KEY = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_CACHE_PATH = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PROJECT = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_ASSET_PATH = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_DSA_ANNOTATION_GROUPS = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_USERNAME = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PASSWORD = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_PATH = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_QIDO_PREFIX = None
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_WADO_PREFIX = None
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_STOW_PREFIX = None
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_FETCH_BY_FRAME = False
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CONVERT_TO_NIFTI = True
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_SEARCH_FILTER = '{"Modality": "CT"}'
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_EXPIRY = 180
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PROXY_TIMEOUT = 30.0
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_READ_TIMEOUT = 5.0
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_AUTO_RELOAD = True
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_READ_ONLY = False
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_FILE_EXT = '["*.nii.gz", "*.nii", "*.nrrd", "*.jpg", "*.png", "*.tif", "*.svs", "*.xml"]'
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_SERVER_PORT = 8000
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_CORS_ORIGINS = '[]'
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_SESSIONS = True
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_SESSION_PATH = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_SESSION_EXPIRY = 3600
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_INFER_CONCURRENCY = -1
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_INFER_TIMEOUT = 600
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_TRACKING_ENABLED = True
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_TRACKING_URI = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_ZOO_SOURCE = github
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_ZOO_REPO = Project-MONAI/model-zoo/hosting_storage_v1
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_ZOO_AUTH_TOKEN = 
2023-01-20 12:13:57,338 - ENV SETTINGS:: MONAI_LABEL_AUTO_UPDATE_SCORING = True
2023-01-20 12:13:57,338 - 
Allow Origins: ['*']
[2023-01-20 12:13:57,611] [1927570] [MainThread] [INFO] (uvicorn.error:75) - Started server process [1927570]
[2023-01-20 12:13:57,611] [1927570] [MainThread] [INFO] (uvicorn.error:45) - Waiting for application startup.
[2023-01-20 12:13:57,611] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: /home/user1/Escritorio/Monai/apps/radiology; studies: /home/user1/Escritorio/Monai/datasets/Task09_Spleen/imagesTr; conf: {'models': 'segmentation_spleen'}
[2023-01-20 12:13:57,636] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for MONAILabelApp Found: &lt;class 'main.MyApp'&gt;
[2023-01-20 12:13:57,638] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepgrow_3d.Deepgrow3D'&gt;
[2023-01-20 12:13:57,639] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepedit.DeepEdit'&gt;
[2023-01-20 12:13:57,639] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.localization_vertebra.LocalizationVertebra'&gt;
[2023-01-20 12:13:57,640] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation_spleen.SegmentationSpleen'&gt;
[2023-01-20 12:13:57,640] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.deepgrow_2d.Deepgrow2D'&gt;
[2023-01-20 12:13:57,640] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation_vertebra.SegmentationVertebra'&gt;
[2023-01-20 12:13:57,640] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.segmentation.Segmentation'&gt;
[2023-01-20 12:13:57,640] [1927570] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class 'lib.configs.localization_spine.LocalizationSpine'&gt;
[2023-01-20 12:13:57,640] [1927570] [MainThread] [INFO] (main:93) - +++ Adding Model: segmentation_spleen =&gt; lib.configs.segmentation_spleen.SegmentationSpleen
[2023-01-20 12:13:57,640] [1927570] [MainThread] [INFO] (monailabel.utils.others.generic:185) - Downloading resource: /home/user1/Escritorio/Monai/apps/radiology/model/pretrained_segmentation_spleen.pt from https://github.com/Project-MONAI/MONAILabel/releases/download/pretrained/radiology_segmentation_unet_spleen.pt
pretrained_segmentation_spleen.pt: 18.4MB [00:06, 3.09MB/s]                                                                                                                                                              
2023-01-20 12:14:03,890 - INFO - Downloaded: /home/user1/Escritorio/Monai/apps/radiology/model/pretrained_segmentation_spleen.pt
2023-01-20 12:14:03,890 - INFO - Expected md5 is None, skip md5 check for file /home/user1/Escritorio/Monai/apps/radiology/model/pretrained_segmentation_spleen.pt.
[2023-01-20 12:14:04,938] [1927570] [MainThread] [INFO] (lib.configs.segmentation_spleen:75) - EPISTEMIC Enabled: False; Samples: 5
[2023-01-20 12:14:04,938] [1927570] [MainThread] [INFO] (main:96) - +++ Using Models: ['segmentation_spleen']
[2023-01-20 12:14:04,938] [1927570] [MainThread] [INFO] (monailabel.interfaces.app:135) - Init Datastore for: /home/user1/Escritorio/Monai/datasets/Task09_Spleen/imagesTr
[2023-01-20 12:14:04,939] [1927570] [MainThread] [INFO] (monailabel.datastore.local:129) - Auto Reload: True; Extensions: ['*.nii.gz', '*.nii', '*.nrrd', '*.jpg', '*.png', '*.tif', '*.svs', '*.xml']
[2023-01-20 12:14:04,943] [1927570] [MainThread] [INFO] (monailabel.datastore.local:576) - Invalidate count: 0
[2023-01-20 12:14:04,943] [1927570] [MainThread] [INFO] (monailabel.datastore.local:150) - Start observing external modifications on datastore (AUTO RELOAD)
[2023-01-20 12:14:04,943] [1927570] [MainThread] [INFO] (main:126) - +++ Adding Inferer:: segmentation_spleen =&gt; &lt;lib.infers.segmentation_spleen.SegmentationSpleen object at 0x7f3ed429dfc0&gt;
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (main:191) - {'segmentation_spleen': &lt;lib.infers.segmentation_spleen.SegmentationSpleen object at 0x7f3ed429dfc0&gt;, 'Histogram+GraphCut': &lt;monailabel.scribbles.infer.HistogramBasedGraphCut object at 0x7f3ed3d1e6b0&gt;, 'GMM+GraphCut': &lt;monailabel.scribbles.infer.GMMBasedGraphCut object at 0x7f3ed3d1e6e0&gt;}
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (main:206) - +++ Adding Trainer:: segmentation_spleen =&gt; &lt;lib.trainers.segmentation_spleen.SegmentationSpleen object at 0x7f3ed3d982e0&gt;
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /home/user1/.cache/monailabel/sessions
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (monailabel.interfaces.app:475) - App Init - completed
[2023-01-20 12:14:04,944] [timeloop] [INFO] Starting Timeloop..
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (timeloop:60) - Starting Timeloop..
[2023-01-20 12:14:04,944] [timeloop] [INFO] Registered job &lt;function MONAILabelApp.on_init_complete.&lt;locals&gt;.run_scheduler at 0x7f3ed3d0ee60&gt;
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (timeloop:42) - Registered job &lt;function MONAILabelApp.on_init_complete.&lt;locals&gt;.run_scheduler at 0x7f3ed3d0ee60&gt;
[2023-01-20 12:14:04,944] [timeloop] [INFO] Timeloop now started. Jobs will run based on the interval set
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (timeloop:63) - Timeloop now started. Jobs will run based on the interval set
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (uvicorn.error:59) - Application startup complete.
[2023-01-20 12:14:04,944] [1927570] [MainThread] [INFO] (uvicorn.error:206) - Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
[2023-01-20 12:14:40,865] [1927570] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {'strategy': 'first', 'client_id': 'user-xyz'}
[2023-01-20 12:14:40,865] [1927570] [MainThread] [INFO] (monailabel.tasks.activelearning.first:38) - First: Selected Image: spleen_10
[2023-01-20 12:14:40,868] [1927570] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {'id': 'spleen_10', 'path': '/home/user1/Escritorio/Monai/datasets/Task09_Spleen/imagesTr/spleen_10.nii.gz', 'ts': 1673700860, 'name': 'spleen_10.nii.gz', 'strategy': {'first': {'ts': 1674227680, 'client_id': 'user-xyz'}}}
[2023-01-20 12:14:53,752] [1927570] [MainThread] [INFO] (monailabel.endpoints.activelearning:43) - Active Learning Request: {'strategy': 'first', 'client_id': 'user-xyz'}
[2023-01-20 12:14:53,752] [1927570] [MainThread] [INFO] (monailabel.tasks.activelearning.first:38) - First: Selected Image: spleen_10
[2023-01-20 12:14:53,754] [1927570] [MainThread] [INFO] (monailabel.endpoints.activelearning:59) - Next sample: {'id': 'spleen_10', 'path': '/home/user1/Escritorio/Monai/datasets/Task09_Spleen/imagesTr/spleen_10.nii.gz', 'ts': 1673700860, 'name': 'spleen_10.nii.gz', 'strategy': {'first': {'ts': 1674227693, 'client_id': 'user-xyz'}}}
[2023-01-20 12:15:01,791] [1927570] [MainThread] [INFO] (monailabel.endpoints.infer:160) - Infer Request: {'model': 'segmentation_spleen', 'image': 'spleen_10', 'device': 'cpu', 'result_extension': '.nrrd', 'result_dtype': 'uint8', 'client_id': 'user-xyz'}
[2023-01-20 12:15:01,791] [1927570] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:279) - Infer Request (final): {'device': 'cpu', 'model': 'segmentation_spleen', 'image': '/home/user1/Escritorio/Monai/datasets/Task09_Spleen/imagesTr/spleen_10.nii.gz', 'result_extension': '.nrrd', 'result_dtype': 'uint8', 'client_id': 'user-xyz', 'description': 'A pre-trained model for volumetric (3D) segmentation of the spleen from CT image'}
[2023-01-20 12:15:01,792] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:76) - PRE - Run Transform(s)
[2023-01-20 12:15:01,792] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - PRE - Input Keys: ['device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path']
[2023-01-20 12:15:02,083] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (LoadImaged): Time: 0.2906; image: torch.Size([512, 512, 55])(torch.float32)
[2023-01-20 12:15:02,084] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (EnsureTyped): Time: 0.0002; image: torch.Size([512, 512, 55])(torch.float32)
[2023-01-20 12:15:02,084] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (EnsureChannelFirstd): Time: 0.0001; image: torch.Size([1, 512, 512, 55])(torch.float32)
[2023-01-20 12:15:04,614] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (Spacingd): Time: 2.53; image: torch.Size([1, 500, 500, 271])(torch.float32)
[2023-01-20 12:15:04,797] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (ScaleIntensityRanged): Time: 0.1831; image: torch.Size([1, 500, 500, 271])(torch.float32)
[2023-01-20 12:15:04,798] [1927570] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:471) - Inferer:: cpu =&gt; SlidingWindowInferer =&gt; {'roi_size': (160, 160, 160), 'sw_batch_size': 1, 'overlap': 0.25, 'mode': constant, 'sigma_scale': 0.125, 'padding_mode': constant, 'cval': 0.0, 'sw_device': None, 'device': None, 'progress': False, 'cpu_thresh': None, 'roi_weight_map': None}
[2023-01-20 12:15:04,798] [1927570] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:420) - Infer model path: /home/user1/Escritorio/Monai/apps/radiology/model/pretrained_segmentation_spleen.pt
[2023-01-20 12:15:17,355] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:76) - POST - Run Transform(s)
[2023-01-20 12:15:17,355] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - POST - Input Keys: ['device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path', 'image_meta_dict', 'latencies', 'pred']
[2023-01-20 12:15:17,356] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (EnsureTyped): Time: 0.0001; image: torch.Size([1, 500, 500, 271])(torch.float32); pred: torch.Size([2, 500, 500, 271])(torch.float32)
[2023-01-20 12:15:17,420] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (Activationsd): Time: 0.0644; image: torch.Size([1, 500, 500, 271])(torch.float32); pred: torch.Size([2, 500, 500, 271])(torch.float32)
[2023-01-20 12:15:22,801] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (AsDiscreted): Time: 5.3802; image: torch.Size([1, 500, 500, 271])(torch.float32); pred: torch.Size([1, 500, 500, 271])(torch.float32)
[2023-01-20 12:15:22,858] [1927570] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (Restored): Time: 0.0571; image: torch.Size([1, 500, 500, 271])(torch.float32); pred: torch.Size([512, 512, 55])(torch.float32)
[2023-01-20 12:15:22,885] [1927570] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:571) - Writing Result...
[2023-01-20 12:15:22,886] [1927570] [MainThread] [INFO] (monailabel.transform.writer:189) - Result ext: .nrrd; write_to_file: True; dtype: uint8
[2023-01-20 12:15:24,913] [1927570] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:334) - ++ Latencies =&gt; Total: 23.1218; Pre: 3.0060; Inferer: 12.5575; Invert: 0.0000; Post: 5.5303; Write: 2.0278
[2023-01-20 12:15:24,913] [1927570] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:358) - Result File: /tmp/tmpq5s1_hsr.nrrd
[2023-01-20 12:15:24,913] [1927570] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:359) - Result Json Keys: ['label_names', 'latencies']

</code></pre>
<p>Could someone help? or give pointers?</p>
<p>Thanks a lot</p>

---

## Post #3 by @rbumm (2023-01-21 23:55 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> can maybe comment and will present vertrebrae segmentation with 3D Slicer sample datasets in the upcoming <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/MONAILabel_Workshop.html">MONAILabel workshop</a> on <strong>Wednesday January 25th  9-11am EST</strong></p>

---

## Post #4 by @diazandr3s (2023-01-22 01:32 UTC)

<p>Thanks for the ping, <a class="mention" href="/u/rbumm">@rbumm</a>.</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>:</p>
<p>The vertebra segmentation model has been trained on a portion of the VerSe dataset. This means the model may need training to work on other datasets.</p>
<p>Can you try the <strong>localization_vertebra</strong> or <strong>vertebra_pipeline</strong>? It should be under the list of Auto Segmentation models.</p>
<p>You may also be interested on the whole-body CT segmentation model that includes vertebra segmentation. This model was trained on the Total Segmentator dataset.</p>
<p>Here you can find the app folder: <a href="https://drive.google.com/drive/folders/17eJan-8_oNCnZyJk8B9zLQpwaOjtDuKi?usp=share_link" class="inline-onebox" rel="noopener nofollow ugc">radiology_full_ct-upgraded-HYBRID - Google Drive</a></p>
<p>Please let us know how that goes.</p>

---

## Post #5 by @diazandr3s (2023-01-22 02:44 UTC)

<p>Forgot to add the command to start the server:</p>
<p>monailabel start_server --app radiology_full_ct-upgraded-HYBRID/ --studies PATH_TO_IMAGES/ --conf models segmentation_full_ct</p>

---

## Post #6 by @mau_igna_06 (2023-01-22 18:51 UTC)

<p>Hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>
<p>Thank you for your answer</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="4" data-topic="27243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>Can you try the <strong>localization_vertebra</strong> or <strong>vertebra_pipeline</strong>? It should be under the list of Auto Segmentation models.</p>
</blockquote>
</aside>
<p>None of them worked, one gave an empty result and the other an error of mismatching tensor size on the server</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="5" data-topic="27243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>monailabel start_server --app radiology_full_ct-upgraded-HYBRID/ --studies PATH_TO_IMAGES/ --conf models segmentation_full_ct</p>
</blockquote>
</aside>
<p>This one worked. Thank you</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd6377955019558d68be2954dbff91096f00dc0f.jpeg" data-download-href="/uploads/short-url/A9zUfQS1ya0Lvii0DeZkMWCbW9N.jpeg?dl=1" title="Captura desde 2023-01-22 14-30-25" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd6377955019558d68be2954dbff91096f00dc0f_2_690x388.jpeg" alt="Captura desde 2023-01-22 14-30-25" data-base62-sha1="A9zUfQS1ya0Lvii0DeZkMWCbW9N" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd6377955019558d68be2954dbff91096f00dc0f_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd6377955019558d68be2954dbff91096f00dc0f_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd6377955019558d68be2954dbff91096f00dc0f_2_1380x776.jpeg 2x" data-dominant-color="9AA3CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura desde 2023-01-22 14-30-25</span><span class="informations">1920×1080 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The original CT had 0.65mm spacing, but the automatic segmentation result looks much rougher than when I do a manual threshold. Please see the picture below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/440467d90cd21c6380f58c13d955ad11a62e1bfe.jpeg" data-download-href="/uploads/short-url/9HHUeKOyKW1pZXSelsnmKaotQT4.jpeg?dl=1" title="Captura desde 2023-01-22 15-49-56" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/440467d90cd21c6380f58c13d955ad11a62e1bfe_2_690x388.jpeg" alt="Captura desde 2023-01-22 15-49-56" data-base62-sha1="9HHUeKOyKW1pZXSelsnmKaotQT4" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/440467d90cd21c6380f58c13d955ad11a62e1bfe_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/440467d90cd21c6380f58c13d955ad11a62e1bfe_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/440467d90cd21c6380f58c13d955ad11a62e1bfe_2_1380x776.jpeg 2x" data-dominant-color="A7AD96"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura desde 2023-01-22 15-49-56</span><span class="informations">1920×1080 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can this be corrected?</p>

---

## Post #7 by @pieper (2023-01-22 19:05 UTC)

<p>Yes, this is expected - <a class="mention" href="/u/diazandr3s">@diazandr3s</a> has told me that this model is only trained at 1.5mm and another at 2mm which is the same as TotalSegmentator.  In my experience the MONAI Label ct_full and TotalSegmentator give comparable results, just with different resource requirements (MONAI can be faster but uses more memory).  I understand either could be trained to run inference at higher resolution but I don’t believe that has happened yet.  We plan to do some spine-specific higher resolution models with <a class="mention" href="/u/ron">@Ron</a> Alkalay.</p>

---

## Post #8 by @Ron (2023-01-22 19:17 UTC)

<p>Thanks.  flying out today, will have internet by 9 or 10 est tomorrow</p>
<p>Ron N Alkalay<br>
Associate Professor,<br>
Dept of Orthopedic Surgery, Harvard Medical School<br>
Center for Advanced<br>
Orthopedic Studies<br>
Beth Israel<br>
Deaconess Medical Center<br>
1 Overland Street<br>
Boston, MA, 02215<br>
Tel. 617-667-5185<br>
Fax. 617-667-7175<br>
email:<br>
rn_alkalay@bidmc.harvard.edu</p>

---

## Post #9 by @diazandr3s (2023-01-22 21:14 UTC)

<p>Thanks for sharing the results, <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>.</p>
<p>As <a class="mention" href="/u/pieper">@pieper</a> said, we’ve trained two models on the Total Segmentator dataset: one using 1.5mm and the other using 2mm.</p>
<p>Just to check how it goes, could you try running inference after changing the <strong>self.target_spacing</strong> values to (0.6, 0.6, 0.6) in the file <em>lib/configs/segmentation_full_ct</em>?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5863a17b2f3e2bab57203d1a3900c7a3790d1837.png" alt="Screenshot from 2023-01-22 21-09-11" data-base62-sha1="cBVttkTDh6zinbMoaIHaveTGDaf" width="569" height="261"></p>
<p>Retraining the model on better resolution shouldn’t be difficult at all. You just need to change the <strong>self.target_spacing</strong> values to (0.6, 0.6, 0.6), or the one that fits on your GPU/CPU, in the file <em>lib/configs/segmentation_full_ct</em> and trigger training.</p>

---

## Post #10 by @mau_igna_06 (2023-01-22 21:39 UTC)

<p>Hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>
<p>Thank you for your answer</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="9" data-topic="27243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>Just to check how it goes, could you try running inference after changing the <strong>self.target_spacing</strong> values to (0.6, 0.6, 0.6) in the file <em>lib/configs/segmentation_full_ct</em>?</p>
</blockquote>
</aside>
<p>I’ll do</p>
<p>I wonder if we could train a preliminar stage of a bone segmentation model using just binary thresholds (then they could be separated by connected components by another stage or a human) or create an expert threshold limit chooser for bones segmentation using the training data from totalSegmentator.<br>
On our application, making anatomic surgical guide bases, only surface of cortical bone is important (considering other geometric restrictions). Currently we create them with the segment editor.</p>

---

## Post #11 by @diazandr3s (2023-01-22 21:46 UTC)

<p>Definitely! that can be done. This is a good question/topic to talk about during the workshop this Wednesday <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #12 by @mau_igna_06 (2023-01-23 17:00 UTC)

<p>Hi</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="9" data-topic="27243">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>Just to check how it goes, could you try running inference after changing the <strong>self.target_spacing</strong> values to (0.6, 0.6, 0.6) in the file <em>lib/configs/segmentation_full_ct</em>?</p>
</blockquote>
</aside>
<p>My laptop could not allocate 58GB of RAM</p>
<p>Thank you anyway, I’ll keep exploring in the near future with better (cloud?) hardware</p>

---

## Post #13 by @diazandr3s (2023-01-23 17:05 UTC)

<p>I suspected this is the challenge with high-resolution images</p>

---
