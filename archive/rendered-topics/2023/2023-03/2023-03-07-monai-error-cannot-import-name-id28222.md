---
topic_id: 28222
title: "Monai Error Cannot Import Name"
date: 2023-03-07
url: https://discourse.slicer.org/t/28222
---

# MONAI error: cannot import name

**Topic ID**: 28222
**Date**: 2023-03-07
**URL**: https://discourse.slicer.org/t/monai-error-cannot-import-name/28222

---

## Post #1 by @GeneRisi (2023-03-07 15:08 UTC)

<p>When I run (in Windows 10):</p>
<p><em>monailabel start_server --app monaibundle --studies Task09_Spleen/imagesTr --conf models renalStructures_UNEST_segmentation</em></p>
<p>I get:</p>
<p><em>Using PYTHONPATH=C:\Users\Gene\AppData\Local\Programs\Python;C:\Users\Gene\AppData\Local\Programs\Python\Python39;<br>
“”<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: version = False<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: app = C:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monaibundle<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: studies = C:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\Task09_Spleen\imagesTr<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: verbose = INFO<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: conf = [[‘models’, ‘renalStructures_UNEST_segmentation’]]<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: host = 0.0.0.0<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: port = 8000<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: uvicorn_app = monailabel.app:app<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: ssl_keyfile = None<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: ssl_certfile = None<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: ssl_keyfile_password = None<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: ssl_ca_certs = None<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: workers = None<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: limit_concurrency = None<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: access_log = False<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: log_config = None<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: dryrun = False<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:276) - USING:: action = start_server<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_API_STR =<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_PROJECT_NAME = MONAILabel<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_APP_DIR =<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_STUDIES =<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_AUTH_ENABLE = False<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_AUTH_DB =<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_APP_CONF = ‘{}’<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_TRAIN = True<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_STRATEGY = True<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_SCORING = True<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_BATCH_INFER = True<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE =<br>
[2023-03-07 10:49:47,870] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_URL =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_USERNAME =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PASSWORD =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_API_KEY =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_CACHE_PATH =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PROJECT =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_ASSET_PATH =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_DSA_ANNOTATION_GROUPS =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_USERNAME =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PASSWORD =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_PATH =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_QIDO_PREFIX = None<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_WADO_PREFIX = None<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_STOW_PREFIX = None<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_FETCH_BY_FRAME = False<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CONVERT_TO_NIFTI = True<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_SEARCH_FILTER = ‘{“Modality”: “CT”}’<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_EXPIRY = 180<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PROXY_TIMEOUT = 30.0<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_READ_TIMEOUT = 5.0<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_AUTO_RELOAD = True<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_READ_ONLY = False<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_FILE_EXT = '["</em>.nii.gz", “<em>.nii", "</em>.nrrd”, “<em>.jpg", "</em>.png”, “<em>.tif", "</em>.svs”, "<em>.xml"]’<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_SERVER_PORT = 8000<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_CORS_ORIGINS = ‘[]’<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_SESSIONS = True<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_SESSION_PATH =<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_SESSION_EXPIRY = 3600<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_INFER_CONCURRENCY = -1<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_INFER_TIMEOUT = 600<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_TRACKING_ENABLED = True<br>
[2023-03-07 10:49:47,885] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_TRACKING_URI =<br>
[2023-03-07 10:49:47,901] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_ZOO_SOURCE = github<br>
[2023-03-07 10:49:47,901] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_ZOO_REPO = Project-MONAI/model-zoo/hosting_storage_v1<br>
[2023-03-07 10:49:47,901] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_ZOO_AUTH_TOKEN = <br>
[2023-03-07 10:49:47,901] [15316] [MainThread] [INFO] (<strong>main</strong>:280) - ENV SETTINGS:: MONAI_LABEL_AUTO_UPDATE_SCORING = True<br>
[2023-03-07 10:49:47,901] [15316] [MainThread] [INFO] (<strong>main</strong>:281) -<br>
Traceback (most recent call last):<br>
File “C:\Users\Gene\AppData\Local\Programs\python\Python39\lib\runpy.py”, line 197, in _run_module_as_main<br>
return _run_code(code, main_globals, None,<br>
File “C:\Users\Gene\AppData\Local\Programs\python\Python39\lib\runpy.py”, line 87, in <em>run_code<br>
exec(code, run_globals)<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monailabel\main.py”, line 342, in <br>
Main().run()<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monailabel\main.py”, line 133, in run<br>
self.action_start_server(args)<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monailabel\main.py”, line 234, in action_start_server<br>
uvicorn.run(<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\uvicorn\main.py”, line 463, in run<br>
server.run()<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\uvicorn\server.py”, line 60, in run<br>
return asyncio.run(self.serve(sockets=sockets))<br>
File “C:\Users\Gene\AppData\Local\Programs\python\Python39\lib\asyncio\runners.py”, line 44, in run<br>
return loop.run_until_complete(main)<br>
File “C:\Users\Gene\AppData\Local\Programs\python\Python39\lib\asyncio\base_events.py”, line 647, in run_until_complete<br>
return future.result()<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\uvicorn\server.py”, line 67, in serve<br>
config.load()<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\uvicorn\config.py”, line 458, in load<br>
self.loaded_app = import_from_string(self.app)<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\uvicorn\importer.py”, line 24, in import_from_string<br>
raise exc from None<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\uvicorn\importer.py”, line 21, in import_from_string<br>
module = importlib.import_module(module_str)<br>
File "C:\Users\Gene\AppData\Local\Programs\python\Python39\lib\importlib_<em>init</em></em>.py", line 127, in import_module<br>
return _bootstrap._gcd_import(name[level:], package, level)<br>
File “”, line 1030, in _gcd_import<br>
File “”, line 1007, in _find_and_load<br>
File “”, line 986, in _find_and_load_unlocked<br>
File “”, line 680, in _load_unlocked<br>
File “”, line 850, in exec_module<br>
File “”, line 228, in <em>call_with_frames_removed<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monailabel\app.py”, line 23, in <br>
from monailabel.endpoints import (<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monailabel\endpoints\activelearning.py”, line 19, in <br>
from monailabel.interfaces.app import MONAILabelApp<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monailabel\interfaces\app.py”, line 38, in <br>
from monailabel.datastore.dicom import DICOMwebClientX, DICOMWebDatastore<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monailabel\datastore\dicom.py”, line 26, in <br>
from monailabel.datastore.utils.convert import binary_to_image, dicom_to_nifti, nifti_to_dicom_seg<br>
File “c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monailabel\datastore\utils\convert.py”, line 24, in <br>
from monai.data import nifty_writer<br>
ImportError: cannot import name ‘nifty_writer’ from ‘monai.data’ (c:\Users\Gene\AppData\Local\Programs\Python\Python39\Lib\site-packages\monai\data_<em>init</em></em>.py)</em></p>
<p>I don’t know what to do next. I installed monailabel and then monai-weekly to avoid the hardcoded site request issue with running the server in Windows.</p>
<p>Gene</p>

---

## Post #2 by @GeneRisi (2023-03-07 20:37 UTC)

<p>I installed monailabel-weekly…</p>

---

## Post #3 by @rbumm (2023-03-07 22:01 UTC)

<p>Did you install MonaiLabel as <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">described here</a> and which works for most use cases?</p>
<p>What did you do differently?</p>

---

## Post #5 by @GeneRisi (2023-03-08 14:37 UTC)

<p>Thank you for your assistance!</p>
<p>I was following directions from another web site, so I started over and used your directions. It got me this far:</p>
<p><em>requests.exceptions.HTTPError: 404 Client Error: Not Found for url: <a href="https://api.github.com/repos/Project-MONAI%5Cmodel-zoo/releases" rel="noopener nofollow ugc">https://api.github.com/repos/Project-MONAI\model-zoo/releases</a></em></p>
<p>The "" is the problem. I believe I read about this Windows specific error and that the solution was to install monailabel-weekly. I don’t know if this is what I should do and I don’t want to mess up what has gotten me this far. Do you have a suggestion?</p>
<p>Thanks again.</p>
<p>Gene</p>

---

## Post #6 by @rbumm (2023-03-08 19:09 UTC)

<aside class="quote no-group" data-username="GeneRisi" data-post="5" data-topic="28222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/ba8739/48.png" class="avatar"> GeneRisi:</div>
<blockquote>
<p>requests.exceptions.HTTPError: 404 Client Error: Not Found for url: <a href="https://api.github.com/repos/Project-MONAI%5Cmodel-zoo/releases">https://api.github.com/repos/Project-MONAI\model-zoo/releases</a></p>
</blockquote>
</aside>
<p>At which installation stage/command from the script (link above) does this happen?</p>

---

## Post #7 by @GeneRisi (2023-03-08 19:12 UTC)

<p>PS C:\Users\Gene&gt; monailabel datasets --download --name Task09_Spleen --output datasets<br>
Using PYTHONPATH=C:\Users\Gene\MONAILabel;<br>
“”<br>
Directory already exists: datasets\Task09_Spleen<br>
PS C:\Users\Gene&gt; monailabel start_server --app monaibundle --studies Task09_Spleen/imagesTr --conf models renalStructures_UNEST_segmentation<br>
Using PYTHONPATH=C:\Users\Gene\MONAILabel;<br>
“”<br>
2023-03-08 08:56:00,220 - USING:: version = False<br>
2023-03-08 08:56:00,220 - USING:: app = C:\Users\Gene\monaibundle<br>
2023-03-08 08:56:00,221 - USING:: studies = C:\Users\Gene\Task09_Spleen\imagesTr<br>
2023-03-08 08:56:00,222 - USING:: verbose = INFO<br>
2023-03-08 08:56:00,222 - USING:: conf = [[‘models’, ‘renalStructures_UNEST_segmentation’]]<br>
2023-03-08 08:56:00,222 - USING:: host = 0.0.0.0<br>
2023-03-08 08:56:00,223 - USING:: port = 8000<br>
2023-03-08 08:56:00,223 - USING:: uvicorn_app = monailabel.app:app<br>
2023-03-08 08:56:00,223 - USING:: ssl_keyfile = None<br>
2023-03-08 08:56:00,224 - USING:: ssl_certfile = None<br>
2023-03-08 08:56:00,224 - USING:: ssl_keyfile_password = None<br>
2023-03-08 08:56:00,224 - USING:: ssl_ca_certs = None<br>
2023-03-08 08:56:00,225 - USING:: workers = None<br>
2023-03-08 08:56:00,225 - USING:: limit_concurrency = None<br>
2023-03-08 08:56:00,225 - USING:: access_log = False<br>
2023-03-08 08:56:00,226 - USING:: log_config = None<br>
2023-03-08 08:56:00,226 - USING:: dryrun = False<br>
2023-03-08 08:56:00,226 - USING:: action = start_server<br>
2023-03-08 08:56:00,227 - ENV SETTINGS:: MONAI_LABEL_API_STR =<br>
2023-03-08 08:56:00,227 - ENV SETTINGS:: MONAI_LABEL_PROJECT_NAME = MONAILabel<br>
2023-03-08 08:56:00,227 - ENV SETTINGS:: MONAI_LABEL_APP_DIR =<br>
2023-03-08 08:56:00,228 - ENV SETTINGS:: MONAI_LABEL_STUDIES =<br>
2023-03-08 08:56:00,228 - ENV SETTINGS:: MONAI_LABEL_AUTH_ENABLE = False<br>
2023-03-08 08:56:00,229 - ENV SETTINGS:: MONAI_LABEL_AUTH_DB =<br>
2023-03-08 08:56:00,229 - ENV SETTINGS:: MONAI_LABEL_APP_CONF = ‘{}’<br>
2023-03-08 08:56:00,230 - ENV SETTINGS:: MONAI_LABEL_TASKS_TRAIN = True<br>
2023-03-08 08:56:00,230 - ENV SETTINGS:: MONAI_LABEL_TASKS_STRATEGY = True<br>
2023-03-08 08:56:00,230 - ENV SETTINGS:: MONAI_LABEL_TASKS_SCORING = True<br>
2023-03-08 08:56:00,231 - ENV SETTINGS:: MONAI_LABEL_TASKS_BATCH_INFER = True<br>
2023-03-08 08:56:00,231 - ENV SETTINGS:: MONAI_LABEL_DATASTORE =<br>
2023-03-08 08:56:00,231 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_URL =<br>
2023-03-08 08:56:00,231 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_USERNAME =<br>
2023-03-08 08:56:00,232 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PASSWORD =<br>
2023-03-08 08:56:00,232 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_API_KEY =<br>
2023-03-08 08:56:00,232 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_CACHE_PATH =<br>
2023-03-08 08:56:00,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PROJECT =<br>
2023-03-08 08:56:00,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_ASSET_PATH =<br>
2023-03-08 08:56:00,233 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_DSA_ANNOTATION_GROUPS =<br>
2023-03-08 08:56:00,234 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_USERNAME =<br>
2023-03-08 08:56:00,236 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PASSWORD =<br>
2023-03-08 08:56:00,236 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_PATH =<br>
2023-03-08 08:56:00,236 - ENV SETTINGS:: MONAI_LABEL_QIDO_PREFIX = None<br>
2023-03-08 08:56:00,237 - ENV SETTINGS:: MONAI_LABEL_WADO_PREFIX = None<br>
2023-03-08 08:56:00,237 - ENV SETTINGS:: MONAI_LABEL_STOW_PREFIX = None<br>
2023-03-08 08:56:00,237 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_FETCH_BY_FRAME = False<br>
2023-03-08 08:56:00,238 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CONVERT_TO_NIFTI = True<br>
2023-03-08 08:56:00,238 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_SEARCH_FILTER = ‘{“Modality”: “CT”}’<br>
2023-03-08 08:56:00,238 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_EXPIRY = 180<br>
2023-03-08 08:56:00,239 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PROXY_TIMEOUT = 30.0<br>
2023-03-08 08:56:00,239 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_READ_TIMEOUT = 5.0<br>
2023-03-08 08:56:00,239 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_AUTO_RELOAD = True<br>
2023-03-08 08:56:00,239 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_READ_ONLY = False<br>
2023-03-08 08:56:00,239 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_FILE_EXT = ‘[“<em>.nii.gz", "</em>.nii”, “<em>.nrrd", "</em>.jpg”, “<em>.png", "</em>.tif”, “<em>.svs", "</em>.xml”]’<br>
2023-03-08 08:56:00,240 - ENV SETTINGS:: MONAI_LABEL_SERVER_PORT = 8000<br>
2023-03-08 08:56:00,240 - ENV SETTINGS:: MONAI_LABEL_CORS_ORIGINS = ‘<span class="chcklst-box fa fa-square-o fa-fw"></span>’<br>
2023-03-08 08:56:00,240 - ENV SETTINGS:: MONAI_LABEL_SESSIONS = True<br>
2023-03-08 08:56:00,241 - ENV SETTINGS:: MONAI_LABEL_SESSION_PATH =<br>
2023-03-08 08:56:00,241 - ENV SETTINGS:: MONAI_LABEL_SESSION_EXPIRY = 3600<br>
2023-03-08 08:56:00,241 - ENV SETTINGS:: MONAI_LABEL_INFER_CONCURRENCY = -1<br>
2023-03-08 08:56:00,242 - ENV SETTINGS:: MONAI_LABEL_INFER_TIMEOUT = 600<br>
2023-03-08 08:56:00,242 - ENV SETTINGS:: MONAI_LABEL_TRACKING_ENABLED = True<br>
2023-03-08 08:56:00,242 - ENV SETTINGS:: MONAI_LABEL_TRACKING_URI =<br>
2023-03-08 08:56:00,243 - ENV SETTINGS:: MONAI_ZOO_SOURCE = github<br>
2023-03-08 08:56:00,243 - ENV SETTINGS:: MONAI_ZOO_REPO = Project-MONAI/model-zoo/hosting_storage_v1<br>
2023-03-08 08:56:00,243 - ENV SETTINGS:: MONAI_ZOO_AUTH_TOKEN = <br>
2023-03-08 08:56:00,244 - ENV SETTINGS:: MONAI_LABEL_AUTO_UPDATE_SCORING = True<br>
2023-03-08 08:56:00,244 -<br>
Allow Origins: [‘*’]<br>
[2023-03-08 08:56:01,589] [9072] [MainThread] [INFO] (uvicorn.error:75) - Started server process [9072]<br>
[2023-03-08 08:56:01,589] [9072] [MainThread] [INFO] (uvicorn.error:45) - Waiting for application startup.<br>
[2023-03-08 08:56:01,591] [9072] [MainThread] [INFO] (monailabel.interfaces.utils.app:37) - Initializing App from: C:\Users\Gene\monaibundle; studies: C:\Users\Gene\Task09_Spleen\imagesTr; conf: {‘models’: ‘renalStructures_UNEST_segmentation’}<br>
[2023-03-08 08:56:01,660] [9072] [MainThread] [INFO] (monailabel.utils.others.class_utils:57) - Subclass for MONAILabelApp Found: &lt;class ‘main.MyApp’&gt;<br>
[2023-03-08 08:56:05,915] [9072] [MainThread] [INFO] (monailabel.utils.others.generic:303) - +++ Adding Bundle from Zoo: renalStructures_UNEST_segmentation =&gt; C:\Users\Gene\monaibundle\model\renalStructures_UNEST_segmentation<br>
2023-03-08 08:56:05,915 - INFO - — input summary of monai.bundle.scripts.download —<br>
2023-03-08 08:56:05,916 - INFO - &gt; name: ‘renalStructures_UNEST_segmentation’<br>
2023-03-08 08:56:05,917 - INFO - &gt; bundle_dir: ‘C:\Users\Gene\monaibundle\model’<br>
2023-03-08 08:56:05,918 - INFO - &gt; source: ‘github’<br>
2023-03-08 08:56:05,918 - INFO - &gt; repo: ‘Project-MONAI/model-zoo/hosting_storage_v1’<br>
2023-03-08 08:56:05,919 - INFO - &gt; remove_prefix: ‘monai_’<br>
2023-03-08 08:56:05,919 - INFO - &gt; progress: True<br>
2023-03-08 08:56:05,920 - INFO - —</p>
<p>[2023-03-08 08:56:06,060] [9072] [MainThread] [ERROR] (uvicorn.error:119) - Traceback (most recent call last):<br>
File “C:\Users\Gene\AppData\Roaming\Python\Python39\site-packages\starlette\routing.py”, line 635, in lifespan<br>
async with self.lifespan_context(app):<br>
File “C:\Users\Gene\AppData\Roaming\Python\Python39\site-packages\starlette\routing.py”, line 530, in <strong>aenter</strong><br>
await self.<em>router.startup()<br>
File “C:\Users\Gene\AppData\Roaming\Python\Python39\site-packages\starlette\routing.py”, line 612, in startup<br>
await handler()<br>
File “C:\Users\Gene\MONAILabel\monailabel\app.py”, line 106, in startup_event<br>
instance = app_instance()<br>
File “C:\Users\Gene\MONAILabel\monailabel\interfaces\utils\app.py”, line 50, in app_instance<br>
app = c(app_dir=app_dir, studies=studies, conf=conf)<br>
File “C:\Users\Gene\monaibundle\main.py”, line 36, in <strong>init</strong><br>
self.models = get_bundle_models(app_dir, conf)<br>
File “C:\Users\Gene\MONAILabel\monailabel\utils\others\generic.py”, line 307, in get_bundle_models<br>
download(name=name, version=version, bundle_dir=model_dir, source=zoo_source, repo=zoo_repo)<br>
File “C:\Users\Gene\AppData\Roaming\Python\Python39\site-packages\monai\bundle\scripts.py”, line 302, in download<br>
version</em> = <em>get_latest_bundle_version(source=source</em>, name=name_, repo=repo_)<br>
File “C:\Users\Gene\AppData\Roaming\Python\Python39\site-packages\monai\bundle\scripts.py”, line 185, in _get_latest_bundle_version<br>
return get_bundle_versions(name, repo=os.path.join(repo_owner, repo_name), tag=tag_name)[“latest_version”]<br>
File “C:\Users\Gene\AppData\Roaming\Python\Python39\site-packages\monai\bundle\scripts.py”, line 520, in get_bundle_versions<br>
bundles_info = _get_all_bundles_info(repo=repo, tag=tag, auth_token=auth_token)<br>
File “C:\Users\Gene\AppData\Roaming\Python\Python39\site-packages\monai\bundle\scripts.py”, line 434, in _get_all_bundles_info<br>
resp.raise_for_status()<br>
File “C:\Users\Gene\AppData\Roaming\Python\Python39\site-packages\requests\models.py”, line 1021, in raise_for_status<br>
raise HTTPError(http_error_msg, response=self)<br>
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: <a href="https://api.github.com/repos/Project-MONAI%5Cmodel-zoo/releases" rel="noopener nofollow ugc">https://api.github.com/repos/Project-MONAI\model-zoo/releases</a></p>
<p>[2023-03-08 08:56:06,061] [9072] [MainThread] [ERROR] (uvicorn.error:56) - Application startup failed. Exiting.</p>

---

## Post #8 by @rbumm (2023-03-08 19:32 UTC)

<p>I can reproduce that.<br>
Have you tried the radiology apps? Do you rely on monaibundle?</p>

---

## Post #9 by @GeneRisi (2023-03-08 19:36 UTC)

<p>This is where I confess my ignorance… I want to use Slicer3d with a radiology app and was excited when I saw the kidney study because I have kidney cancer and want to learn as much as I can. Is there another way to run this study?</p>
<p>Is there a way to download the models and then refer to them on my PC vs getting them from github ?</p>

---

## Post #10 by @rbumm (2023-03-08 19:51 UTC)

<p>Sorry to hear that. Good luck.</p>
<p>Maybe <a class="mention" href="/u/diazandr3s">@diazandr3s</a> can comment.</p>

---

## Post #11 by @mau_igna_06 (2023-03-08 20:10 UTC)

<p>Give it some time. You should get it going.<br>
I would recommend studying kidney (and related organs/tissues) anatomy.<br>
Also checkout this:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerLiver/">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="" height="">

      <a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerLiver/" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://projectweek.na-mic.org/PW38_2023_GranCanaria/Projects/SlicerLiver/" target="_blank" rel="noopener nofollow ugc">NA-MIC Project Weeks</a></h3>

  <p>Website for NA-MIC Project Weeks</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Best of luck</p>

---

## Post #12 by @GeneRisi (2023-03-08 20:24 UTC)

<p>I figured it out. There are environment variables (MONI_ZOO_SOURCE = ‘’ and MONI_ZOO_REPO =  ) that seems to be working.</p>

---

## Post #13 by @rbumm (2023-03-08 20:39 UTC)

<p>Could you write a short passage that I could add to the installation script? Thank you.</p>

---

## Post #14 by @GeneRisi (2023-03-08 21:05 UTC)

<p>How’s this?</p>
<p><strong>IF</strong></p>
<p>the git api request for a model fails due to an improperly formatted URL</p>
<p>(for example <em><a href="https://api.github.com/repos/Project-MONAI%5Cmodel-zoo/releases" rel="noopener nofollow ugc">https://api.github.com/repos/Project-MONAI\model-zoo/releases</a></em>)</p>
<p><strong>THEN</strong></p>
<p>Step 1: The model “.zip” file can be downloaded  (via web browser, for example) with a properly formatted version of the URL (replace '' with ‘/’) and then expanded into a folder on your PC.</p>
<p>Step 2: Set values for two environment variable the server will use as an override:</p>
<ul>
<li>$Env:MONAI_ZOO_SOURCE = ‘local’</li>
<li>$Env:MONAI_ZOO_REPO = &lt; folder name &gt;</li>
</ul>
<p>Step 3: Start monailabel server</p>

---

## Post #15 by @GeneRisi (2023-03-08 21:11 UTC)

<p>Also, “git” was not installed on my Win 10 pro. “winget install git.git” made it available.</p>

---

## Post #16 by @diazandr3s (2023-03-08 21:49 UTC)

<p>Thanks for the ping <a class="mention" href="/u/rbumm">@rbumm</a><br>
I’d suggest asking questions or reporting any issues on using MONAI Bundle or models from the model Zoo directly on the main GitHub repo (<a href="https://github.com/project-monai/model-zoo" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/model-zoo: MONAI Model Zoo that hosts models in the MONAI Bundle format.</a>). The developers will answer you within hours <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
