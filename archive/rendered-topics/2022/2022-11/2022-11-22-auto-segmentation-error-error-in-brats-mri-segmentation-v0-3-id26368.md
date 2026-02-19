---
topic_id: 26368
title: "Auto Segmentation Error Error In Brats Mri Segmentation V0 3"
date: 2022-11-22
url: https://discourse.slicer.org/t/26368
---

# Auto Segmentation error error in 'brats_mri_segmentation_v0.3.8'

**Topic ID**: 26368
**Date**: 2022-11-22
**URL**: https://discourse.slicer.org/t/auto-segmentation-error-error-in-brats-mri-segmentation-v0-3-8/26368

---

## Post #1 by @platanus (2022-11-22 02:19 UTC)

<p>Dear all members in 3d slicer</p>
<p><strong>Describe the bug</strong><br>
[2022-11-22 10:24:37,281] [19036] [MainThread] [ERROR] (uvicorn.error:119) - Traceback (most recent call last):<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\starlette\routing.py”, line 635, in lifespan<br>
async with self.lifespan_context(app):<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\starlette\routing.py”, line 530, in <strong>aenter</strong><br>
await self.<em>router.startup()<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\starlette\routing.py”, line 612, in startup<br>
await handler()<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\monailabel\app.py”, line 106, in startup_event<br>
instance = app_instance()<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\monailabel\interfaces\utils\app.py”, line 51, in app_instance<br>
app = c(app_dir=app_dir, studies=studies, conf=conf)<br>
File “C:\Users\AA\apps\monaibundle\main.py”, line 90, in <strong>init</strong><br>
super().<strong>init</strong>(<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\monailabel\interfaces\app.py”, line 96, in <strong>init</strong><br>
self.<em>trainers = self.init_trainers() if settings.MONAI_LABEL_TASKS_TRAIN else {}<br>
File “C:\Users\AA\apps\monaibundle\main.py”, line 116, in init_trainers<br>
t = BundleTrainTask(b, self.conf)<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\monailabel\tasks\train\bundle.py”, line 83, in <strong>init</strong><br>
self.bundle_config.read_config(self.bundle_config_path)<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\monai\bundle\config_parser.py”, line 300, in read_config<br>
content.update(self.load_config_files(f, **kwargs))<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\monai\bundle\config_parser.py”, line 403, in load_config_files<br>
for k, v in (cls.load_config_file(i, **kwargs)).items():<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\monai\bundle\config_parser.py”, line 382, in load_config_file<br>
return json.load(f, **kwargs)<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\json_<em>init</em></em>.py”, line 293, in load<br>
return loads(fp.read(),<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\json_<em>init</em></em>.py”, line 346, in loads<br>
return _default_decoder.decode(s)<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\json\decoder.py”, line 337, in decode<br>
obj, end = self.raw_decode(s, idx=_w(s, 0).end())<br>
File “C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\json\decoder.py”, line 353, in raw_decode<br>
obj, end = self.scan_once(s, idx)<br>
json.decoder.JSONDecodeError: Expecting ‘,’ delimiter: line 63 column 43 (char 1947)</p>
<p>[2022-11-22 10:24:37,282] [19036] [MainThread] [ERROR] (uvicorn.error:56) - Application startup failed. Exiting.</p>
<p><strong>To Reproduce</strong><br>
Steps to reproduce the behavior:</p>
<ol>
<li>‘in_channel’ value edited 4 into 1 and added 'ensure_channel_first": ture in train.json as following.</li>
</ol>

<p>“<em>target</em>”: “SegResNet”,<br>
“blocks_down”: [<br>
1,<br>
2,<br>
2,<br>
4<br>
],<br>
“blocks_up”: [<br>
1,<br>
1,<br>
1<br>
],<br>
“init_filters”: 16,<br>
“in_channels”: 1,<br>
“out_channels”: 3,<br>
“dropout_prob”: 0.2<br>
},<br>
“network”: “$@network_def.to(<a href="https://github.com/device" rel="noopener nofollow ugc">@device</a>)”,<br>
“preprocessing”: {<br>
“<em>target</em>”: “Compose”,<br>
“transforms”: [<br>
{<br>
“<em>target</em>”: “LoadImaged”,<br>
“keys”: “image”,<br>
“ensure_channel_first”: true<br>
},</p>
<ol start="2">
<li>‘in_channel’ value edited 4 into 1 and added 'ensure_channel_first": ture in train.json as following.</li>
</ol>
<blockquote>
<p>edited train.json code&gt;</p>
</blockquote>
<p>“<em>target</em>”: “SegResNet”,<br>
“blocks_down”: [<br>
1,<br>
2,<br>
2,<br>
4<br>
],<br>
“blocks_up”: [<br>
1,<br>
1,<br>
1<br>
],<br>
“init_filters”: 16,<br>
“in_channels”: 1,<br>
“out_channels”: 3,<br>
“dropout_prob”: 0.2<br>
},<br>
.<br>
.<br>
.<br>
“train”: {<br>
“preprocessing_transforms”: [<br>
{<br>
“<em>target</em>”: “LoadImaged”,<br>
“keys”: [<br>
“image”,<br>
“label”,<br>
“ensure_channel_first”: true<br>
]<br>
},</p>
<ol start="3">
<li>‘(“inputs”) num_channel’ value edits 4 into 1 train.json as following.</li>
</ol>

<p>“network_data_format”: {<br>
“inputs”: {<br>
“image”: {<br>
“type”: “image”,<br>
“format”: “magnitude”,<br>
“modality”: “MR”,<br>
“num_channels”: 1,<br>
“spatial_shape”: [<br>
“8<em>n”,<br>
“8</em>n”,<br>
“8*n”<br>
],</p>
<p><strong>Expected behavior</strong><br>
I can expect result when I press ‘run’ button in Auto Segmentation option, after I edited and added inference.json, train.josn and metadata.json.<br>
<a href="https://user-images.githubusercontent.com/67679322/203200004-2f7e1187-4ec7-46a8-bb90-f7862d9a78ef.png" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/67679322/203200004-2f7e1187-4ec7-46a8-bb90-f7862d9a78ef.png" alt="image" width="612" height="168"></a></p>
<p><a href="https://user-images.githubusercontent.com/67679322/203198584-98b80bb9-f404-4c0a-9731-e7a80b9d47ff.png" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/67679322/203198584-98b80bb9-f404-4c0a-9731-e7a80b9d47ff.png" alt="image" width="690" height="470"></a></p>
<p><strong>Screenshots</strong><br>
But I can’t extract brain tumor as following figure.</p>
<p><a href="https://user-images.githubusercontent.com/67679322/203199021-29678f2d-fb3f-4f2d-a328-7bd52f93127d.png" rel="noopener nofollow ugc"><img src="https://user-images.githubusercontent.com/67679322/203199021-29678f2d-fb3f-4f2d-a328-7bd52f93127d.png" alt="image" width="690" height="429"></a></p>
<h1><a name="p-86384-environment-1" class="anchor" href="#p-86384-environment-1" aria-label="Heading link"></a><strong>Environment</strong></h1>
<h1><a name="p-86384-printing-monai-config-2" class="anchor" href="#p-86384-printing-monai-config-2" aria-label="Heading link"></a>Printing MONAI config…</h1>
<p>MONAI version: 1.0.1<br>
Numpy version: 1.23.4<br>
Pytorch version: 1.12.1+cu113<br>
MONAI flags: HAS_EXT = False, USE_COMPILED = False, USE_META_DICT = False<br>
MONAI rev id: 8271a193229fe4437026185e218d5b06f7c8ce69<br>
MONAI <strong>file</strong>: C:\Users\TRL 3D\AppData\Local\Programs\Python\Python39\lib\site-packages\monai_<em>init</em>_.py</p>
<p>Optional dependencies:<br>
Pytorch Ignite version: 0.4.10<br>
Nibabel version: 4.0.2<br>
scikit-image version: 0.19.3<br>
Pillow version: 9.3.0<br>
Tensorboard version: 2.10.1<br>
gdown version: 4.5.3<br>
TorchVision version: 0.13.1+cu113<br>
tqdm version: 4.64.1<br>
lmdb version: 1.3.0<br>
psutil version: 5.9.4<br>
pandas version: 1.5.1<br>
einops version: 0.6.0<br>
transformers version: 4.24.0<br>
mlflow version: 2.0.1<br>
pynrrd version: 0.4.3</p>
<p>For details about installing the optional dependencies, please visit:<br>
<a href="https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies" class="onebox" target="_blank" rel="noopener nofollow ugc">https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies</a></p>
<h1><a name="p-86384-h-3" class="anchor" href="#p-86384-h-3" aria-label="Heading link"></a>================================</h1>
<p>Printing system config…</p>
<p>System: Windows<br>
Win32 version: (‘10’, ‘10.0.22000’, ‘SP0’, ‘Multiprocessor Free’)<br>
Win32 edition: Core<br>
Platform: Windows-10-10.0.22000-SP0<br>
Processor: AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD<br>
Machine: AMD64<br>
Python version: 3.9.13<br>
Process name: python.exe<br>
Command: [‘C:\Users\TRL 3D\AppData\Local\Programs\Python\Python39\python.exe’, ‘-c’, ‘import monai; monai.config.print_debug_info()’]<br>
Open files: [popenfile(path=‘C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackko-KR_22000.29.134.0_neutral__8wekyb3d8bbwe\Windows\System32\ko-KR\39386f74d1967f5c37a5b4171f81c8f3\kernel32.dll.mui’, fd=-1), popenfile(path=‘C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackko-KR_22000.29.134.0_neutral__8wekyb3d8bbwe\Windows\System32\ko-KR\fe441ef3ed396a241e46f9f354057863\tzres.dll.mui’, fd=-1), popenfile(path=‘C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackko-KR_22000.29.134.0_neutral__8wekyb3d8bbwe\Windows\System32\ko-KR\a7c1941e6709c10ab525083b61805316\KernelBase.dll.mui’, fd=-1)]<br>
Num physical CPUs: 8<br>
Num logical CPUs: 16<br>
Num usable CPUs: 16<br>
CPU usage (%): [10.3, 9.4, 6.9, 3.8, 4.4, 0.6, 1.9, 2.2, 6.6, 15.2, 7.8, 3.2, 2.2, 0.9, 6.0, 41.1]<br>
CPU freq. (MHz): 3301<br>
Load avg. in last 1, 5, 15 mins (%): [0.0, 0.0, 0.0]<br>
Disk usage (%): 60.3<br>
Avg. sensor temp. (Celsius): UNKNOWN for given OS<br>
Total physical memory (GB): 15.4<br>
Available memory (GB): 7.1<br>
Used memory (GB): 8.3</p>
<h1><a name="p-86384-h-4" class="anchor" href="#p-86384-h-4" aria-label="Heading link"></a>================================</h1>
<p>Printing GPU config…</p>
<p>Num GPUs: 1<br>
Has CUDA: True<br>
CUDA version: 11.3<br>
cuDNN enabled: True<br>
cuDNN version: 8302<br>
Current device: 0<br>
Library compiled for CUDA architectures: [‘sm_37’, ‘sm_50’, ‘sm_60’, ‘sm_61’, ‘sm_70’, ‘sm_75’, ‘sm_80’, ‘sm_86’, ‘compute_37’]<br>
GPU 0 Name: NVIDIA GeForce RTX 3070 Laptop GPU<br>
GPU 0 Is integrated: False<br>
GPU 0 Is multi GPU board: False<br>
GPU 0 Multi processor count: 40<br>
GPU 0 Total memory (GB): 8.0<br>
GPU 0 CUDA capability (maj.min): 8.6</p>

---

## Post #2 by @rbumm (2022-11-22 11:33 UTC)

<p>Sorry, please understand that I do not respond to this via discourse direct mail, <a class="mention" href="/u/platanus">@platanus</a></p>
<p>You need to bring this into a readable and structured form, preferably with a native English speaker, to expect answers from the community. And it is not good to spam this forum with questions, even if they do not get answered.</p>

---

## Post #3 by @platanus (2022-11-22 22:16 UTC)

<p>Dear <a class="mention" href="/u/rbumm">@rbumm</a></p>
<p>Thank you for answering.</p>

---

## Post #4 by @lassoan (2022-11-23 00:18 UTC)

<p>This seems to be a MONAILabel core question that MONAI community members may be able to help with - see how to contact them here: <a href="https://monai.io/community.html" class="inline-onebox">MONAI - Community</a></p>

---

## Post #5 by @diazandr3s (2022-11-29 01:31 UTC)

<p>Many thanks, <a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/lassoan">@lassoan</a><br>
This question is being addressed here: <a href="https://github.com/Project-MONAI/model-zoo/issues/239#issuecomment-1327094860" class="inline-onebox" rel="noopener nofollow ugc">Auto Segmentation error in 'brats_segmentation_v0.3.3' model · Issue #239 · Project-MONAI/model-zoo · GitHub</a></p>
<p>and here: <a href="https://github.com/Project-MONAI/MONAILabel/issues/1051" class="inline-onebox" rel="noopener nofollow ugc">RuntimeError when "brats_mri_segmentation_v0.2.1" from monaibundle is used. · Issue #1051 · Project-MONAI/MONAILabel · GitHub</a></p>

---
