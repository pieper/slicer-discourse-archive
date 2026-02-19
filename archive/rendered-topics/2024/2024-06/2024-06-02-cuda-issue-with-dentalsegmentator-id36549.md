---
topic_id: 36549
title: "Cuda Issue With Dentalsegmentator"
date: 2024-06-02
url: https://discourse.slicer.org/t/36549
---

# Cuda issue with dentalsegmentator

**Topic ID**: 36549
**Date**: 2024-06-02
**URL**: https://discourse.slicer.org/t/cuda-issue-with-dentalsegmentator/36549

---

## Post #1 by @mohammed_alshakhas (2024-06-02 10:05 UTC)

<p>i installed cuda on mu PC and still whenever i run detalsegmentaror it says cuda not available on your system .<br>
any idea what to do ?<br>
thanks</p>

---

## Post #2 by @mohammed_alshakhas (2024-06-02 12:48 UTC)

<p>correction<br>
i installed cuda on  PC and still whenever i run dentalsegmentor but  it says cuda not available on your system</p>

---

## Post #3 by @Thibault_Pelletier (2024-06-03 07:27 UTC)

<p>Hi <a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> ,</p>
<p>Thank you for your interest in our extension.<br>
For CUDA related problems, please have a look at this doc : <a href="https://github.com/gaudot/SlicerDentalSegmentator?tab=readme-ov-file#torch-cuda-not-properly-installed" class="inline-onebox" rel="noopener nofollow ugc">GitHub - gaudot/SlicerDentalSegmentator: 3D Slicer extension for fully-automatic segmentation of CT and CBCT dental volumes.</a></p>
<p>To summarize, you can use the <a href="https://github.com/fepegar/SlicerPyTorch" rel="noopener nofollow ugc">PyTorch slicer extension</a> to manually set the pytorch + CUDA version which best suits your system.</p>
<p>Let me know if that helps.<br>
Best,<br>
Thibault</p>

---

## Post #4 by @mohammed_alshakhas (2024-06-03 09:48 UTC)

<p>let me take the chance to congratulate you and thank you for the amazing work. this extension is mindblowing.</p>

---

## Post #5 by @1546161 (2024-06-14 04:47 UTC)

<p>2024/06/14 11:20:00.892 :: nnUNet is already installed (2.4.2) and compatible with requested version (nnunetv2).<br>
2024/06/14 11:20:09.816 :: Transferring volume to nnUNet in C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs<br>
2024/06/14 11:20:20.152 :: Starting nnUNet with the following parameters:<br>
2024/06/14 11:20:20.152 ::<br>
2024/06/14 11:20:20.152 :: C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs/input -o C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cuda -chk checkpoint_final.pth --disable_tta<br>
2024/06/14 11:20:20.152 ::<br>
2024/06/14 11:20:20.152 :: JSON parameters :<br>
2024/06/14 11:20:20.152 :: {<br>
2024/06/14 11:20:20.152 ::     “folds”: “0”,<br>
2024/06/14 11:20:20.152 ::     “device”: “cuda”,<br>
2024/06/14 11:20:20.152 ::     “stepSize”: 0.5,<br>
2024/06/14 11:20:20.152 ::     “disableTta”: true,<br>
2024/06/14 11:20:20.152 ::     “nProcessPreprocessing”: 1,<br>
2024/06/14 11:20:20.152 ::     “nProcessSegmentationExport”: 1,<br>
2024/06/14 11:20:20.152 ::     “checkPointName”: “”,<br>
2024/06/14 11:20:20.152 ::     “modelPath”: {<br>
2024/06/14 11:20:20.152 ::         “_path”: “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\slicer.org\Extensions-32886\DentalSegmentator\lib\Slicer-5.7\qt-scripted-modules\Resources\ML”<br>
2024/06/14 11:20:20.152 ::     }<br>
2024/06/14 11:20:20.152 :: }<br>
2024/06/14 11:20:20.159 :: nnUNet preprocessing…<br>
2024/06/14 11:20:21.429 :: Traceback (most recent call last):<br>
2024/06/14 11:20:21.429 ::   File “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
2024/06/14 11:20:21.430 :: return _run_code(code, main_globals, None,<br>
2024/06/14 11:20:21.430 ::   File “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
2024/06/14 11:20:21.430 ::     exec(code, run_globals)<br>
2024/06/14 11:20:21.430 ::   File "C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Scripts\nnUNetv2_predict.exe_<em>main</em></em>.py", line 4, in <br>
2024/06/14 11:20:21.430 ::   File “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 12, in <br>
2024/06/14 11:20:21.430 ::     from batchgenerators.dataloading.multi_threaded_augmenter import MultiThreadedAugmenter<br>
2024/06/14 11:20:21.430 ::   File “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\site-packages\batchgenerators\dataloading\multi_threaded_augmenter.py”, line 26, in <br>
2024/06/14 11:20:21.435 :: from threadpoolctl import threadpool_limits<br>
2024/06/14 11:20:21.435 :: ModuleNotFoundError: No module named ‘threadpoolctl’<br>
2024/06/14 11:20:21.613 :: Loading inference results…<br>
2024/06/14 11:20:25.688 :: Error loading results :<br>
2024/06/14 11:20:25.688 :: Failed to load the segmentation.<br>
2024/06/14 11:20:25.688 :: Check the inference folder content C:\Users\DELL\AppData\Local\Temp\Slicer-bFASSs\output</p>
<p>Dear developer, I am a newcomer from China, please can you tell me the way to solve the problem, the detailed process, thank you, thank you</p>

---

## Post #6 by @1546161 (2024-06-14 04:53 UTC)

<p>2024/06/14 11:20:00.892 :: nnUNet is already installed (2.4.2) and compatible with requested version (nnunetv2).<br>
2024/06/14 11:20:09.816 :: Transferring volume to nnUNet in C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs<br>
2024/06/14 11:20:20.152 :: Starting nnUNet with the following parameters:<br>
2024/06/14 11:20:20.152 ::<br>
2024/06/14 11:20:20.152 :: C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs/input -o C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cuda -chk checkpoint_final.pth --disable_tta<br>
2024/06/14 11:20:20.152 ::<br>
2024/06/14 11:20:20.152 :: JSON parameters :<br>
2024/06/14 11:20:20.152 :: {<br>
2024/06/14 11:20:20.152 ::     “folds”: “0”,<br>
2024/06/14 11:20:20.152 ::     “device”: “cuda”,<br>
2024/06/14 11:20:20.152 ::     “stepSize”: 0.5,<br>
2024/06/14 11:20:20.152 ::     “disableTta”: true,<br>
2024/06/14 11:20:20.152 ::     “nProcessPreprocessing”: 1,<br>
2024/06/14 11:20:20.152 ::     “nProcessSegmentationExport”: 1,<br>
2024/06/14 11:20:20.152 ::     “checkPointName”: “”,<br>
2024/06/14 11:20:20.152 ::     “modelPath”: {<br>
2024/06/14 11:20:20.152 ::         “_path”: “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\slicer.org\Extensions-32886\DentalSegmentator\lib\Slicer-5.7\qt-scripted-modules\Resources\ML”<br>
2024/06/14 11:20:20.152 ::     }<br>
2024/06/14 11:20:20.152 :: }<br>
2024/06/14 11:20:20.159 :: nnUNet preprocessing…<br>
2024/06/14 11:20:21.429 :: Traceback (most recent call last):<br>
2024/06/14 11:20:21.429 ::   File “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
2024/06/14 11:20:21.430 :: return _run_code(code, main_globals, None,<br>
2024/06/14 11:20:21.430 ::   File “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
2024/06/14 11:20:21.430 ::     exec(code, run_globals)<br>
2024/06/14 11:20:21.430 ::   File "C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Scripts\nnUNetv2_predict.exe_<em>main</em></em>.py", line 4, in <br>
2024/06/14 11:20:21.430 ::   File “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 12, in <br>
2024/06/14 11:20:21.430 ::     from batchgenerators.dataloading.multi_threaded_augmenter import MultiThreadedAugmenter<br>
2024/06/14 11:20:21.430 ::   File “C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\site-packages\batchgenerators\dataloading\multi_threaded_augmenter.py”, line 26, in <br>
2024/06/14 11:20:21.435 :: from threadpoolctl import threadpool_limits<br>
2024/06/14 11:20:21.435 :: ModuleNotFoundError: No module named ‘threadpoolctl’<br>
2024/06/14 11:20:21.613 :: Loading inference results…<br>
2024/06/14 11:20:25.688 :: Error loading results :<br>
2024/06/14 11:20:25.688 :: Failed to load the segmentation.<br>
2024/06/14 11:20:25.688 :: Check the inference folder content C:\Users\DELL\AppData\Local\Temp\Slicer-bFASSs\output</p>
<p>Dear developer, I am a newcomer from China, please can you tell me the solution, the detailed process so that we can recommend you in the Chinese market, thank you, thank you</p>

---

## Post #7 by @Marce (2024-06-14 07:31 UTC)

<aside class="quote no-group quote-modified" data-username="1546161" data-post="5" data-topic="36549">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/1/d07c76/48.png" class="avatar"> 1546161:</div>
<blockquote>
<p>ModuleNotFoundError: Ningún módulo llamado ‘threadpoolctl’<br>
2024 /06/14 11:20:21.613 :: Cargando resultados de inferencia…</p>
</blockquote>
</aside>
<p>Hello, dowload:<br>
<a href="https://slicer-packages.kitware.com/api/v1/item/665d6717c8a295ea328461ef/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/665d6717c8a295ea328461ef/download </a></p>
<p>This is slicer package “Slicer-5.7.0-2024-06-01-win-amd64”. this work.</p>

---

## Post #8 by @1546161 (2024-06-14 07:56 UTC)

<p>Downloading and installing still doesn’t work</p>

---

## Post #9 by @Thibault_Pelletier (2024-06-14 08:24 UTC)

<p><a class="mention" href="/u/1546161">@1546161</a> Thank you for your interest in our extension.</p>
<p>The error you are providing seems to indicate something went wrong when installing the nnUNet python dependencies.</p>
<p>When first launching the Dental Segmentator, you should have multiple logs with printed “Installing …”, you also have console logs in the Python console.</p>
<p>Could you try checking if you have any errors at this step so we can investigate further? (you will have to install a clean 3D Slicer version / remove the 3D Slicer directory).</p>
<p>If you want to manually solve this problem, you can also try installing the dependency manually using <code>slicer.util.pip_install("threadpoolctl")</code> in the python console.</p>

---
