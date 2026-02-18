# Monaibundle testing

**Topic ID**: 29564
**Date**: 2023-05-21
**URL**: https://discourse.slicer.org/t/monaibundle-testing/29564

---

## Post #1 by @rbumm (2023-05-21 16:11 UTC)

<p>Hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>
<p>Referring to this page:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/monaibundle#supported-models">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/monaibundle#supported-models" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/monaibundle#supported-models" target="_blank" rel="noopener">MONAILabel/sample-apps/monaibundle at main · Project-MONAI/MONAILabel - Supported Models</a></h3>

  <p><a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/monaibundle#supported-models" target="_blank" rel="noopener">main/sample-apps/monaibundle</a></p>

  <p><span class="label1">MONAI Label is an intelligent open source image labeling and learning tool.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>is this supposed to be working?<br>
Freshly installed MONAILabel and issued the command</p>
<pre><code class="lang-auto">PS C:\Users\rudol&gt; monailabel start_server --app apps/monaibundle --studies datasets/Task06_Lung/imagesTr --conf models lung_nodule_ct_detection

</code></pre>
<p>from a powershell</p>
<pre><code class="lang-auto">PYTHONPATH=C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages;C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\
""
[2023-05-21 18:07:59,854] [29820] [MainThread] [INFO] (__main__:276) - USING:: version = False
[2023-05-21 18:07:59,855] [29820] [MainThread] [INFO] (__main__:276) - USING:: app = C:\Users\rudol\apps\monaibundle
[2023-05-21 18:07:59,856] [29820] [MainThread] [INFO] (__main__:276) - USING:: studies = C:\Users\rudol\datasets\Task06_Lung\imagesTr
[2023-05-21 18:07:59,856] [29820] [MainThread] [INFO] (__main__:276) - USING:: verbose = INFO
[2023-05-21 18:07:59,857] [29820] [MainThread] [INFO] (__main__:276) - USING:: conf = [['models', 'lung_nodule_ct_detection']]
[2023-05-21 18:07:59,858] [29820] [MainThread] [INFO] (__main__:276) - USING:: host = 0.0.0.0
[2023-05-21 18:07:59,858] [29820] [MainThread] [INFO] (__main__:276) - USING:: port = 8000
[2023-05-21 18:07:59,859] [29820] [MainThread] [INFO] (__main__:276) - USING:: uvicorn_app = monailabel.app:app
[2023-05-21 18:07:59,861] [29820] [MainThread] [INFO] (__main__:276) - USING:: ssl_keyfile = None
[2023-05-21 18:07:59,862] [29820] [MainThread] [INFO] (__main__:276) - USING:: ssl_certfile = None
[2023-05-21 18:07:59,862] [29820] [MainThread] [INFO] (__main__:276) - USING:: ssl_keyfile_password = None
[2023-05-21 18:07:59,863] [29820] [MainThread] [INFO] (__main__:276) - USING:: ssl_ca_certs = None
[2023-05-21 18:07:59,863] [29820] [MainThread] [INFO] (__main__:276) - USING:: workers = None
[2023-05-21 18:07:59,864] [29820] [MainThread] [INFO] (__main__:276) - USING:: limit_concurrency = None
[2023-05-21 18:07:59,864] [29820] [MainThread] [INFO] (__main__:276) - USING:: access_log = False
[2023-05-21 18:07:59,864] [29820] [MainThread] [INFO] (__main__:276) - USING:: log_config = None
[2023-05-21 18:07:59,865] [29820] [MainThread] [INFO] (__main__:276) - USING:: dryrun = False
[2023-05-21 18:07:59,865] [29820] [MainThread] [INFO] (__main__:276) - USING:: action = start_server
[2023-05-21 18:07:59,866] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_API_STR =
[2023-05-21 18:07:59,866] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_PROJECT_NAME = MONAILabel
[2023-05-21 18:07:59,866] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_APP_DIR =
[2023-05-21 18:07:59,866] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_STUDIES =
[2023-05-21 18:07:59,868] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_AUTH_ENABLE = False
[2023-05-21 18:07:59,869] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_AUTH_DB =
[2023-05-21 18:07:59,869] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_APP_CONF = '{}'
[2023-05-21 18:07:59,869] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_TRAIN = True
[2023-05-21 18:07:59,870] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_STRATEGY = True
[2023-05-21 18:07:59,870] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_SCORING = True
[2023-05-21 18:07:59,870] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_BATCH_INFER = True
[2023-05-21 18:07:59,871] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE =
[2023-05-21 18:07:59,872] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_URL =
[2023-05-21 18:07:59,873] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_USERNAME =
[2023-05-21 18:07:59,874] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PASSWORD =
[2023-05-21 18:07:59,874] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_API_KEY =
[2023-05-21 18:07:59,874] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_CACHE_PATH =
[2023-05-21 18:07:59,874] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PROJECT =
[2023-05-21 18:07:59,875] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_ASSET_PATH =
[2023-05-21 18:07:59,875] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_DSA_ANNOTATION_GROUPS =
[2023-05-21 18:07:59,875] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_USERNAME =
[2023-05-21 18:07:59,876] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PASSWORD =
[2023-05-21 18:07:59,876] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_PATH =
[2023-05-21 18:07:59,877] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_QIDO_PREFIX = None
[2023-05-21 18:07:59,877] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_WADO_PREFIX = None
[2023-05-21 18:07:59,878] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_STOW_PREFIX = None
[2023-05-21 18:07:59,878] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_FETCH_BY_FRAME = False
[2023-05-21 18:07:59,878] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CONVERT_TO_NIFTI = True
[2023-05-21 18:07:59,879] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_SEARCH_FILTER = '{"Modality": "CT"}'
[2023-05-21 18:07:59,879] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_EXPIRY = 180
[2023-05-21 18:07:59,879] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PROXY_TIMEOUT = 30.0
[2023-05-21 18:07:59,880] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_READ_TIMEOUT = 5.0
[2023-05-21 18:07:59,880] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_AUTO_RELOAD = True
[2023-05-21 18:07:59,881] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_READ_ONLY = False
[2023-05-21 18:07:59,881] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_FILE_EXT = '["*.nii.gz", "*.nii", "*.nrrd", "*.jpg", "*.png", "*.tif", "*.svs", "*.xml"]'
[2023-05-21 18:07:59,882] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_SERVER_PORT = 8000
[2023-05-21 18:07:59,882] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_CORS_ORIGINS = '[]'
[2023-05-21 18:07:59,882] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_SESSIONS = True
[2023-05-21 18:07:59,882] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_SESSION_PATH =
[2023-05-21 18:07:59,885] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_SESSION_EXPIRY = 3600
[2023-05-21 18:07:59,885] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_INFER_CONCURRENCY = -1
[2023-05-21 18:07:59,886] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_INFER_TIMEOUT = 600
[2023-05-21 18:07:59,889] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TRACKING_ENABLED = True
[2023-05-21 18:07:59,889] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TRACKING_URI =
[2023-05-21 18:07:59,890] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_ZOO_SOURCE = github
[2023-05-21 18:07:59,890] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_ZOO_REPO = Project-MONAI/model-zoo/hosting_storage_v1
[2023-05-21 18:07:59,891] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_ZOO_AUTH_TOKEN =
[2023-05-21 18:07:59,891] [29820] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_AUTO_UPDATE_SCORING = True
[2023-05-21 18:07:59,892] [29820] [MainThread] [INFO] (__main__:281) -
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\main.py", line 342, in &lt;module&gt;
    Main().run()
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\main.py", line 133, in run
    self.action_start_server(args)
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\main.py", line 234, in action_start_server
    uvicorn.run(
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\main.py", line 568, in run
    server.run()
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\server.py", line 59, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\asyncio\runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\asyncio\base_events.py", line 647, in run_until_complete
    return future.result()
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\server.py", line 66, in serve
    config.load()
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\config.py", line 471, in load
    self.loaded_app = import_from_string(self.app)
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\importer.py", line 24, in import_from_string
    raise exc from None
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "&lt;frozen importlib._bootstrap&gt;", line 1030, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 1007, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 986, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 680, in _load_unlocked
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\app.py", line 23, in &lt;module&gt;
    from monailabel.endpoints import (
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\endpoints\activelearning.py", line 19, in &lt;module&gt;
    from monailabel.interfaces.app import MONAILabelApp
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\interfaces\app.py", line 38, in &lt;module&gt;
    from monailabel.datastore.dicom import DICOMwebClientX, DICOMWebDatastore
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\datastore\dicom.py", line 26, in &lt;module&gt;
    from monailabel.datastore.utils.convert import binary_to_image, dicom_to_nifti, nifti_to_dicom_seg
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\datastore\utils\convert.py", line 23, in &lt;module&gt;
    from monai.data import write_nifti
ImportError: cannot import name 'write_nifti' from 'monai.data' (C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monai\data\__init__.py)
PS C:\Users\rudol&gt;
PS C:\Users\rudol&gt; monailabel start_server --app apps/monaibundle --studies datasets/Task06_Lung/imagesTr --conf models lung_nodule_ct_detection
Using PYTHONPATH=C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages;C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\
""
[2023-05-21 18:08:59,845] [35816] [MainThread] [INFO] (__main__:276) - USING:: version = False
[2023-05-21 18:08:59,845] [35816] [MainThread] [INFO] (__main__:276) - USING:: app = C:\Users\rudol\apps\monaibundle
[2023-05-21 18:08:59,845] [35816] [MainThread] [INFO] (__main__:276) - USING:: studies = C:\Users\rudol\datasets\Task06_Lung\imagesTr
[2023-05-21 18:08:59,846] [35816] [MainThread] [INFO] (__main__:276) - USING:: verbose = INFO
[2023-05-21 18:08:59,847] [35816] [MainThread] [INFO] (__main__:276) - USING:: conf = [['models', 'lung_nodule_ct_detection']]
[2023-05-21 18:08:59,847] [35816] [MainThread] [INFO] (__main__:276) - USING:: host = 0.0.0.0
[2023-05-21 18:08:59,848] [35816] [MainThread] [INFO] (__main__:276) - USING:: port = 8000
[2023-05-21 18:08:59,848] [35816] [MainThread] [INFO] (__main__:276) - USING:: uvicorn_app = monailabel.app:app
[2023-05-21 18:08:59,848] [35816] [MainThread] [INFO] (__main__:276) - USING:: ssl_keyfile = None
[2023-05-21 18:08:59,849] [35816] [MainThread] [INFO] (__main__:276) - USING:: ssl_certfile = None
[2023-05-21 18:08:59,849] [35816] [MainThread] [INFO] (__main__:276) - USING:: ssl_keyfile_password = None
[2023-05-21 18:08:59,850] [35816] [MainThread] [INFO] (__main__:276) - USING:: ssl_ca_certs = None
[2023-05-21 18:08:59,850] [35816] [MainThread] [INFO] (__main__:276) - USING:: workers = None
[2023-05-21 18:08:59,852] [35816] [MainThread] [INFO] (__main__:276) - USING:: limit_concurrency = None
[2023-05-21 18:08:59,852] [35816] [MainThread] [INFO] (__main__:276) - USING:: access_log = False
[2023-05-21 18:08:59,852] [35816] [MainThread] [INFO] (__main__:276) - USING:: log_config = None
[2023-05-21 18:08:59,853] [35816] [MainThread] [INFO] (__main__:276) - USING:: dryrun = False
[2023-05-21 18:08:59,853] [35816] [MainThread] [INFO] (__main__:276) - USING:: action = start_server
[2023-05-21 18:08:59,854] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_API_STR =
[2023-05-21 18:08:59,855] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_PROJECT_NAME = MONAILabel
[2023-05-21 18:08:59,855] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_APP_DIR =
[2023-05-21 18:08:59,856] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_STUDIES =
[2023-05-21 18:08:59,857] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_AUTH_ENABLE = False
[2023-05-21 18:08:59,857] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_AUTH_DB =
[2023-05-21 18:08:59,858] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_APP_CONF = '{}'
[2023-05-21 18:08:59,858] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_TRAIN = True
[2023-05-21 18:08:59,858] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_STRATEGY = True
[2023-05-21 18:08:59,859] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_SCORING = True
[2023-05-21 18:08:59,859] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TASKS_BATCH_INFER = True
[2023-05-21 18:08:59,860] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE =
[2023-05-21 18:08:59,860] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_URL =
[2023-05-21 18:08:59,861] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_USERNAME =
[2023-05-21 18:08:59,861] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PASSWORD =
[2023-05-21 18:08:59,861] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_API_KEY =
[2023-05-21 18:08:59,861] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_CACHE_PATH =
[2023-05-21 18:08:59,862] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PROJECT =
[2023-05-21 18:08:59,862] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_ASSET_PATH =
[2023-05-21 18:08:59,863] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_DSA_ANNOTATION_GROUPS =
[2023-05-21 18:08:59,863] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_USERNAME =
[2023-05-21 18:08:59,864] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PASSWORD =
[2023-05-21 18:08:59,864] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_PATH =
[2023-05-21 18:08:59,865] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_QIDO_PREFIX = None
[2023-05-21 18:08:59,865] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_WADO_PREFIX = None
[2023-05-21 18:08:59,865] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_STOW_PREFIX = None
[2023-05-21 18:08:59,866] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_FETCH_BY_FRAME = False
[2023-05-21 18:08:59,866] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CONVERT_TO_NIFTI = True
[2023-05-21 18:08:59,867] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_SEARCH_FILTER = '{"Modality": "CT"}'
[2023-05-21 18:08:59,869] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_EXPIRY = 180
[2023-05-21 18:08:59,869] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PROXY_TIMEOUT = 30.0
[2023-05-21 18:08:59,870] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_READ_TIMEOUT = 5.0
[2023-05-21 18:08:59,874] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_AUTO_RELOAD = True
[2023-05-21 18:08:59,874] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_READ_ONLY = False
[2023-05-21 18:08:59,875] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_DATASTORE_FILE_EXT = '["*.nii.gz", "*.nii", "*.nrrd", "*.jpg", "*.png", "*.tif", "*.svs", "*.xml"]'
[2023-05-21 18:08:59,875] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_SERVER_PORT = 8000
[2023-05-21 18:08:59,876] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_CORS_ORIGINS = '[]'
[2023-05-21 18:08:59,876] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_SESSIONS = True
[2023-05-21 18:08:59,876] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_SESSION_PATH =
[2023-05-21 18:08:59,877] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_SESSION_EXPIRY = 3600
[2023-05-21 18:08:59,877] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_INFER_CONCURRENCY = -1
[2023-05-21 18:08:59,877] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_INFER_TIMEOUT = 600
[2023-05-21 18:08:59,878] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TRACKING_ENABLED = True
[2023-05-21 18:08:59,878] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_TRACKING_URI =
[2023-05-21 18:08:59,879] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_ZOO_SOURCE = github
[2023-05-21 18:08:59,879] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_ZOO_REPO = Project-MONAI/model-zoo/hosting_storage_v1
[2023-05-21 18:08:59,880] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_ZOO_AUTH_TOKEN =
[2023-05-21 18:08:59,880] [35816] [MainThread] [INFO] (__main__:280) - ENV SETTINGS:: MONAI_LABEL_AUTO_UPDATE_SCORING = True
[2023-05-21 18:08:59,880] [35816] [MainThread] [INFO] (__main__:281) -
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\main.py", line 342, in &lt;module&gt;
    Main().run()
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\main.py", line 133, in run
    self.action_start_server(args)
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\main.py", line 234, in action_start_server
    uvicorn.run(
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\main.py", line 568, in run
    server.run()
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\server.py", line 59, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\asyncio\runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\asyncio\base_events.py", line 647, in run_until_complete
    return future.result()
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\server.py", line 66, in serve
    config.load()
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\config.py", line 471, in load
    self.loaded_app = import_from_string(self.app)
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\importer.py", line 24, in import_from_string
    raise exc from None
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\uvicorn\importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.9_3.9.3568.0_x64__qbz5n2kfra8p0\lib\importlib\__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "&lt;frozen importlib._bootstrap&gt;", line 1030, in _gcd_import
  File "&lt;frozen importlib._bootstrap&gt;", line 1007, in _find_and_load
  File "&lt;frozen importlib._bootstrap&gt;", line 986, in _find_and_load_unlocked
  File "&lt;frozen importlib._bootstrap&gt;", line 680, in _load_unlocked
  File "&lt;frozen importlib._bootstrap_external&gt;", line 850, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 228, in _call_with_frames_removed
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\app.py", line 23, in &lt;module&gt;
    from monailabel.endpoints import (
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\endpoints\activelearning.py", line 19, in &lt;module&gt;
    from monailabel.interfaces.app import MONAILabelApp
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\interfaces\app.py", line 38, in &lt;module&gt;
    from monailabel.datastore.dicom import DICOMwebClientX, DICOMWebDatastore
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\datastore\dicom.py", line 26, in &lt;module&gt;
    from monailabel.datastore.utils.convert import binary_to_image, dicom_to_nifti, nifti_to_dicom_seg
  File "C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monailabel\datastore\utils\convert.py", line 23, in &lt;module&gt;
    from monai.data import write_nifti
ImportError: cannot import name 'write_nifti' from 'monai.data' (C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\monai\data\__init__.py)
</code></pre>

---

## Post #2 by @Yucheng_Tang (2023-05-22 13:30 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a> , thanks for trying the monailabel. This issue should be caused by the version consistent between monai and monailabel, The “write_nifti” is deprecated in recent update. Can you try reinstall monai by using:</p>
<p>“pip install monai==1.2.0rc6”</p>

---

## Post #3 by @rbumm (2023-05-24 15:46 UTC)

<p>I am now on a different computer, installed 1.2.0rc6, but get:</p>
<pre><code class="lang-auto">PS C:\Users\rudol\MONAILABEL&gt; monailabel apps --download --name monaibundle --output workspace
Using PYTHONPATH=C:\Users\rudol\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages;
App monaibundle =&gt; C:\Users\rudol\MONAILabel\sample-apps\monaibundle not exists
</code></pre>

---

## Post #4 by @diazandr3s (2023-05-26 04:40 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a>,</p>
<p>This is strange. How did you install the monailabel library? Did you use the GitHub repo? If yes, you don’t need to download the monaibundle app - it is already there.<br>
If not, can I ask you what’s the MONAI Label version you are using?</p>
<p>Another option is to download the monaibundle app folder directly from the GitHub repository: <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/sample-apps/monaibundle" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/sample-apps/monaibundle at main · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Please let us know</p>

---

## Post #5 by @rbumm (2023-05-26 11:55 UTC)

<p>I am pleased to confirm that we’ve successfully implemented the MONAILabel monaibundle setup. Here’s an overview of the steps I undertook to achieve this:</p>
<p>Firstly, I began by uninstalling the existing MONAILabel and Monai installations. This was accomplished by running the following commands in the terminal:</p>
<pre><code class="lang-auto">pip uninstall monailabel
pip uninstall monai
</code></pre>
<p>Subsequently, I adhered to our outlined procedures for setting up MONAILabel from scratch. For those who need to refer to these instructions, they can be found on our <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">Project Week webpage</a>.</p>
<p>I followed these guidelines until I reached the command to set the MONAILabel script paths:</p>
<pre><code class="lang-auto">$Env:PATH += ";C:\Users\yourname\MONAILabel\monailabel\scripts"
</code></pre>
<p>After setting the paths, the next step was to installed Monai as recommended above:</p>
<pre><code class="lang-auto">pip install monai==1.2.0rc6
</code></pre>
<p>After a “cd $home”, where my MONAILabel folder is located, the start_server command was issued:</p>
<pre><code class="lang-auto">monailabel start_server --app MONAILabel/sample-apps/monaibundle --studies c:/Data/Task06_Lung/imagesTr --conf models lung_nodule_ct_detection
</code></pre>
<p>After this command, the correct and requested model was automatically loaded from the <a href="https://monai.io/model-zoo.html">Monai Model Zoo</a>, which is a highly commendable feature.</p>
<p>I then proceeded to test our setup with the 3D Slicer and the MONAILabel extension using the CT Chest dataset. It was great to see that the AI successfully detected some nodules!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/214cd0998d510e3b6c2da426c1b3e957ae530c3c.jpeg" data-download-href="/uploads/short-url/4KAkyxGZyxVLmcmuPIfE6n6UyTy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/214cd0998d510e3b6c2da426c1b3e957ae530c3c_2_690x358.jpeg" alt="image" data-base62-sha1="4KAkyxGZyxVLmcmuPIfE6n6UyTy" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/214cd0998d510e3b6c2da426c1b3e957ae530c3c_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/214cd0998d510e3b6c2da426c1b3e957ae530c3c_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/214cd0998d510e3b6c2da426c1b3e957ae530c3c_2_1380x716.jpeg 2x" data-dominant-color="A7A6AB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1876×976 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I want to express my enthusiasm for this significant monaibundle achievement. The ease of implementation lets me hope that there will be a promising future for integrating a variety of models from the Zoo into 3D Slicer setups and extensions.</p>
<p>Great work, <span class="mention">@zephyrie</span>, <a class="mention" href="/u/diazandr3s">@diazandr3s</a> everyone @ NVIDIA!</p>
<p>Sidenote: The process was implemented on an AWS EC2 Windows server instance with an A10G GPU (23 GB dedicated video RAM).</p>
<p>Best,</p>
<p>Rudolf</p>

---

## Post #6 by @diazandr3s (2023-05-29 16:13 UTC)

<p>Many thanks for reporting back, <a class="mention" href="/u/rbumm">@rbumm</a><br>
I’m glad to hear this <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
