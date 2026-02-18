# MONAI Label Server error

**Topic ID**: 26300
**Date**: 2022-11-18
**URL**: https://discourse.slicer.org/t/monai-label-server-error/26300

---

## Post #1 by @platanus (2022-11-18 09:34 UTC)

<p>Dear all members in 3D-Slicer</p>
<p>I’m working auto segmentation with brats_mri_segmentation_v0.2.1 in 3D-Slicer.</p>
<p>When I conduct server start, I used command that is ‘monailabel start_server --app apps/monaibundle --studies datasets/Task01_BrainTumour/imagesTr --conf models brats_mri_segmentation_v0.2.1’.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1252afd06fa8f52395f07b6604c85ec37dbf500.png" data-download-href="/uploads/short-url/mZyvhSrhnM2scEoKFWP386kV13a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1252afd06fa8f52395f07b6604c85ec37dbf500_2_690x291.png" alt="image" data-base62-sha1="mZyvhSrhnM2scEoKFWP386kV13a" width="690" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1252afd06fa8f52395f07b6604c85ec37dbf500_2_690x291.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1252afd06fa8f52395f07b6604c85ec37dbf500_2_1035x436.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1252afd06fa8f52395f07b6604c85ec37dbf500_2_1380x582.png 2x" data-dominant-color="94959B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2560×1080 379 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I added code that is ’ “ensure_channel_first”: true ’ in “preprocessing” part in Inference.json of monaibundle.</p>
<p>But it occurs error that is ‘Failed to run Inference in MONAI Label Server’. Does it have solution?</p>
<p>Train.json also need to edit, but I don’t know where it adds code.</p>
<p>please, let me know how to solve error that is Failed to run interence in MONAI Label Server.</p>
<ul>
<li>monai.config.print_debug_info() -<br>
================================<br>
Printing MONAI config…<br>
================================<br>
MONAI version: 1.0.1<br>
Numpy version: 1.23.4<br>
Pytorch version: 1.12.1+cu113<br>
MONAI flags: HAS_EXT = False, USE_COMPILED = False, USE_META_DICT = False<br>
MONAI rev id: 8271a193229fe4437026185e218d5b06f7c8ce69<br>
MONAI <strong>file</strong>: C:\Users\AA\AppData\Local\Programs\Python\Python39\lib\site-packages\monai_<em>init</em>_.py</li>
</ul>
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
transformers version: NOT INSTALLED or UNKNOWN VERSION.<br>
mlflow version: NOT INSTALLED or UNKNOWN VERSION.<br>
pynrrd version: 0.4.3</p>
<p>For details about installing the optional dependencies, please visit:<br>
<a href="https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies" rel="noopener nofollow ugc">https://docs.monai.io/en/latest/installation.html#installing-the-recommended-dependencies</a></p>
<h1><a name="p-86261-printing-system-config-1" class="anchor" href="#p-86261-printing-system-config-1" aria-label="Heading link"></a>================================<br>
Printing system config…</h1>
<p>System: Windows<br>
Win32 version: (‘10’, ‘10.0.22000’, ‘SP0’, ‘Multiprocessor Free’)<br>
Win32 edition: Core<br>
Platform: Windows-10-10.0.22000-SP0<br>
Processor: AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD<br>
Machine: AMD64<br>
Python version: 3.9.13<br>
Process name: python.exe<br>
Command: [‘C:\Users\AA\AppData\Local\Programs\Python\Python39\python.exe’, ‘-c’, ‘import monai; monai.config.print_debug_info()’]<br>
Open files: [popenfile(path=‘C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackko-KR_22000.29.134.0_neutral__8wekyb3d8bbwe\Windows\System32\ko-KR\a7c1941e6709c10ab525083b61805316\KernelBase.dll.mui’, fd=-1), popenfile(path=‘C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackko-KR_22000.29.134.0_neutral__8wekyb3d8bbwe\Windows\System32\ko-KR\39386f74d1967f5c37a5b4171f81c8f3\kernel32.dll.mui’, fd=-1), popenfile(path=‘C:\Program Files\WindowsApps\Microsoft.LanguageExperiencePackko-KR_22000.29.134.0_neutral__8wekyb3d8bbwe\Windows\System32\ko-KR\fe441ef3ed396a241e46f9f354057863\tzres.dll.mui’, fd=-1)]<br>
Num physical CPUs: 8<br>
Num logical CPUs: 16<br>
Num usable CPUs: 16<br>
CPU usage (%): [10.8, 3.2, 13.1, 3.8, 7.6, 3.9, 4.5, 0.6, 3.9, 0.0, 1.9, 1.9, 8.3, 8.4, 4.5, 45.3]<br>
CPU freq. (MHz): 2652<br>
Load avg. in last 1, 5, 15 mins (%): [0.0, 0.0, 0.0]<br>
Disk usage (%): 57.4<br>
Avg. sensor temp. (Celsius): UNKNOWN for given OS<br>
Total physical memory (GB): 15.4<br>
Available memory (GB): 7.2<br>
Used memory (GB): 8.2</p>
<h1><a name="p-86261-printing-gpu-config-2" class="anchor" href="#p-86261-printing-gpu-config-2" aria-label="Heading link"></a>================================<br>
Printing GPU config…</h1>
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

## Post #2 by @platanus (2022-11-19 02:04 UTC)

<p>I completed to solve error that is ‘Failed to run Inference in MONAI Label Server’ occurred in MONAI Label server.</p>

---

## Post #3 by @diazandr3s (2022-11-22 22:57 UTC)

<p>This is being discussed here: <a href="https://github.com/Project-MONAI/MONAILabel/issues/1051" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/issues/1051</a></p>

---
