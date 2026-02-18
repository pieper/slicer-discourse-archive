# Cannot start_server for MONAILABEL

**Topic ID**: 27406
**Date**: 2023-01-22
**URL**: https://discourse.slicer.org/t/cannot-start-server-for-monailabel/27406

---

## Post #1 by @Bor_Antolic (2023-01-22 19:28 UTC)

<p>Hi! I hope someone could help me with my problem. I successfully installed Monailabel on my home (Mac)computer, started the server, and it works inside 3D Slicer. I followed same steps to install it on my work Windows computer - which is more powerful - but I cannot seem to start the server.<br>
Can anyone please look at the output bellow and suggest a solution?</p>
<p>(monailabel-env) C:\Users\EchoPac&gt;monailabel start_server --app apps/radiology --studies datasets/Task02_Heart/ImagesTr --conf models deepedit<br>
Using PYTHONPATH=C:\Users\EchoPac.conda\envs;<br>
“”<br>
2023-01-20 17:48:12,913 - USING:: version = False<br>
2023-01-20 17:48:12,913 - USING:: app = C:\Users\EchoPac\apps\radiology<br>
2023-01-20 17:48:12,913 - USING:: studies = C:\Users\EchoPac\datasets\Task02_Heart\imagesTr<br>
2023-01-20 17:48:12,913 - USING:: verbose = INFO<br>
2023-01-20 17:48:12,913 - USING:: conf = [[‘models’, ‘deepedit’]]<br>
2023-01-20 17:48:12,913 - USING:: host = 0.0.0.0<br>
2023-01-20 17:48:12,913 - USING:: port = 8000<br>
2023-01-20 17:48:12,913 - USING:: uvicorn_app = monailabel.app:app<br>
2023-01-20 17:48:12,913 - USING:: ssl_keyfile = None<br>
2023-01-20 17:48:12,913 - USING:: ssl_certfile = None<br>
2023-01-20 17:48:12,913 - USING:: ssl_keyfile_password = None<br>
2023-01-20 17:48:12,913 - USING:: ssl_ca_certs = None<br>
2023-01-20 17:48:12,913 - USING:: workers = None<br>
2023-01-20 17:48:12,913 - USING:: limit_concurrency = None<br>
2023-01-20 17:48:12,913 - USING:: access_log = False<br>
2023-01-20 17:48:12,913 - USING:: log_config = None<br>
2023-01-20 17:48:12,913 - USING:: dryrun = False<br>
2023-01-20 17:48:12,913 - USING:: action = start_server<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_API_STR =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_PROJECT_NAME = MONAILabel<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_APP_DIR =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_STUDIES =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_AUTH_ENABLE = False<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_AUTH_DB =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_APP_CONF = ‘{}’<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_TASKS_TRAIN = True<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_TASKS_STRATEGY = True<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_TASKS_SCORING = True<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_TASKS_BATCH_INFER = True<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_URL =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_USERNAME =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PASSWORD =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_API_KEY =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_CACHE_PATH =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_PROJECT =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_ASSET_PATH =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_DSA_ANNOTATION_GROUPS =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_USERNAME =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PASSWORD =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_PATH =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_QIDO_PREFIX = None<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_WADO_PREFIX = None<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_STOW_PREFIX = None<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_FETCH_BY_FRAME = False<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CONVERT_TO_NIFTI = True<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_SEARCH_FILTER = ‘{“Modality”: “CT”}’<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_CACHE_EXPIRY = 180<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_PROXY_TIMEOUT = 30.0<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DICOMWEB_READ_TIMEOUT = 5.0<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_AUTO_RELOAD = True<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_READ_ONLY = False<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_DATASTORE_FILE_EXT = ‘[“<em>.nii.gz", "</em>.nii”, “<em>.nrrd", "</em>.jpg”, “<em>.png", "</em>.tif”, “<em>.svs", "</em>.xml”]’<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_SERVER_PORT = 8000<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_CORS_ORIGINS = ‘<span class="chcklst-box fa fa-square-o fa-fw"></span>’<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_SESSIONS = True<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_SESSION_PATH =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_SESSION_EXPIRY = 3600<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_INFER_CONCURRENCY = -1<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_INFER_TIMEOUT = 600<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_TRACKING_ENABLED = True<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_TRACKING_URI =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_ZOO_SOURCE = github<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_ZOO_REPO = Project-MONAI/model-zoo/hosting_storage_v1<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_ZOO_AUTH_TOKEN =<br>
2023-01-20 17:48:12,913 - ENV SETTINGS:: MONAI_LABEL_AUTO_UPDATE_SCORING = True<br>
2023-01-20 17:48:12,913 -<br>
Allow Origins: [‘*’]<br>
[2023-01-20 17:48:14,147] [11612] [MainThread] [INFO] (uvicorn.error:75) - Started server process [11612]<br>
[2023-01-20 17:48:14,147] [11612] [MainThread] [INFO] (uvicorn.error:45) - Waiting for application startup.<br>
[2023-01-20 17:48:14,147] [11612] [MainThread] [INFO] (monailabel.interfaces.utils.app:38) - Initializing App from: C:\Users\EchoPac\apps\radiology; studies: C:\Users\EchoPac\datasets\Task02_Heart\imagesTr; conf: {‘models’: ‘deepedit’}<br>
[2023-01-20 17:48:14,584] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for MONAILabelApp Found: &lt;class ‘main.MyApp’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepedit.DeepEdit’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_2d.Deepgrow2D’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_3d.Deepgrow3D’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.localization_spine.LocalizationSpine’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.localization_vertebra.LocalizationVertebra’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation.Segmentation’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation_spleen.SegmentationSpleen’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.class_utils:37) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation_vertebra.SegmentationVertebra’&gt;<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (main:93) - +++ Adding Model: deepedit =&gt; lib.configs.deepedit.DeepEdit<br>
[2023-01-20 17:48:14,600] [11612] [MainThread] [INFO] (monailabel.utils.others.generic:185) - Downloading resource: C:\Users\EchoPac\apps\radiology\model\pretrained_deepedit_dynunet.pt from <a href="https://github.com/Project-MONAI/MONAILabel/releases/download/pretrained/radiology_deepedit_dynunet_multilabel.pt" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/releases/download/pretrained/radiology_deepedit_dynunet_multilabel.pt</a><br>
pretrained_deepedit_dynunet.pt: 0.00B [00:00, ?B/s]<br>
2023-01-20 17:48:14,727 - ERROR - Download failed from <a href="https://github.com/Project-MONAI/MONAILabel/releases/download/pretrained/radiology_deepedit_dynunet_multilabel.pt" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/releases/download/pretrained/radiology_deepedit_dynunet_multilabel.pt</a> to C:\Users\EchoPac\AppData\Local\Temp\tmp6fkuh0c8\pretrained_deepedit_dynunet.pt.<br>
[2023-01-20 17:48:14,806] [11612] [MainThread] [ERROR] (uvicorn.error:119) - Traceback (most recent call last):<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\urllib\request.py”, line 1346, in do_open<br>
h.request(req.get_method(), req.selector, req.data, headers,<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\http\client.py”, line 1285, in request<br>
self._send_request(method, url, body, headers, encode_chunked)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\http\client.py”, line 1331, in _send_request<br>
self.endheaders(body, encode_chunked=encode_chunked)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\http\client.py”, line 1280, in endheaders<br>
self._send_output(message_body, encode_chunked=encode_chunked)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\http\client.py”, line 1040, in _send_output<br>
self.send(msg)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\http\client.py”, line 980, in send<br>
self.connect()<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\http\client.py”, line 1454, in connect<br>
self.sock = self._context.wrap_socket(self.sock,<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\ssl.py”, line 501, in wrap_socket<br>
return self.sslsocket_class._create(<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\ssl.py”, line 1041, in _create<br>
self.do_handshake()<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\ssl.py”, line 1310, in do_handshake<br>
self._sslobj.do_handshake()<br>
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\starlette\routing.py”, line 635, in lifespan<br>
async with self.lifespan_context(app):<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\starlette\routing.py”, line 530, in <strong>aenter</strong><br>
await self._router.startup()<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\starlette\routing.py”, line 612, in startup<br>
await handler()<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\monailabel\app.py”, line 106, in startup_event<br>
instance = app_instance()<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\monailabel\interfaces\utils\app.py”, line 51, in app_instance<br>
app = c(app_dir=app_dir, studies=studies, conf=conf)<br>
File “C:\Users\EchoPac\apps\radiology\main.py”, line 95, in <strong>init</strong><br>
self.models[k].init(k, self.model_dir, conf, self.planner)<br>
File “C:\Users\EchoPac\apps\radiology\lib\configs\deepedit.py”, line 74, in init<br>
download_file(url, self.path[0])<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\monailabel\utils\others\generic.py”, line 187, in download_file<br>
download_url(url, path)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\monai\apps\utils.py”, line 203, in download_url<br>
_download_with_progress(url, tmp_name, progress=progress)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\monai\apps\utils.py”, line 114, in _download_with_progress<br>
raise e<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\site-packages\monai\apps\utils.py”, line 107, in _download_with_progress<br>
urlretrieve(url, filepath, reporthook=t.update_to)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\urllib\request.py”, line 239, in urlretrieve<br>
with contextlib.closing(urlopen(url, data)) as fp:<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\urllib\request.py”, line 214, in urlopen<br>
return opener.open(url, data, timeout)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\urllib\request.py”, line 517, in open<br>
response = self._open(req, data)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\urllib\request.py”, line 534, in _open<br>
result = self._call_chain(self.handle_open, protocol, protocol +<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\urllib\request.py”, line 494, in _call_chain<br>
result = func(*args)<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\urllib\request.py”, line 1389, in https_open<br>
return self.do_open(http.client.HTTPSConnection, req,<br>
File “C:\Users\EchoPac.conda\envs\monailabel-env\lib\urllib\request.py”, line 1349, in do_open<br>
raise URLError(err)<br>
urllib.error.URLError: &lt;urlopen error [WinError 10054] An existing connection was forcibly closed by the remote host&gt;</p>
<p>[2023-01-20 17:48:14,806] [11612] [MainThread] [ERROR] (uvicorn.error:56) - Application startup failed. Exiting.</p>

---

## Post #2 by @rbumm (2023-01-23 10:39 UTC)

<p>Hi Bor,<br>
Please make sure that you install MONIALabel on Windows as <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">outlined here</a>.<br>
From the error messages I vaguely assume this could be Firewall / Network / Admin rights problems, maybe ports that are not open, but I would like to ask <a class="mention" href="/u/diazandr3s">@diazandr3s</a> to have a look at this. Thank you, Andres. We have never tried to use MONAILabel within our hospital network yet.</p>

---

## Post #3 by @Bor_Antolic (2023-01-23 11:06 UTC)

<p>Thank you for your reply. I managed to solve this problem, thanks to <a class="mention" href="/u/sachidanandalle">@SachidanandAlle</a>(<a href="https://github.com/SachidanandAlle" class="inline-onebox" rel="noopener nofollow ugc">SachidanandAlle (SACHIDANAND ALLE) · GitHub</a>). It’s more of a workaround - I manually downloaded the file that couldn’t be downloaded and added it to the specified folder.</p>

---

## Post #4 by @natachavalador (2025-01-27 18:11 UTC)

<p>Hi,<br>
It seems I am facing the same problem with the server.</p>
<p>. Running on my own pc (Windows 11)<br>
. 3D Slicer installed with MonaiLabel plug-in working<br>
. Tryed Anaconda, Python 3.11 and Visual Studio Code as an interface<br>
. Followed precisely all tutorials from Andres Pinto and the server remains not working<br>
. Tried to mix my personal IP with the Port :8000 and the error remains</p>
<p>Could you please help me?</p>
<p>Natacha Valador</p>

---
