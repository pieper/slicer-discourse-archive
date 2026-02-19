---
topic_id: 36802
title: "Dentalsegmentator Error Modulenotfounderror No Module Named"
date: 2024-06-15
url: https://discourse.slicer.org/t/36802
---

# DentalSegmentator error: "ModuleNotFoundError: No module named ‘threadpoolctl’"

**Topic ID**: 36802
**Date**: 2024-06-15
**URL**: https://discourse.slicer.org/t/dentalsegmentator-error-modulenotfounderror-no-module-named-threadpoolctl/36802

---

## Post #1 by @1546161 (2024-06-15 05:12 UTC)

<pre><code class="lang-auto">2024/06/14 11:20:00.892 :: nnUNet is already installed (2.4.2) and compatible with requested version (nnunetv2).
2024/06/14 11:20:09.816 :: Transferring volume to nnUNet in C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs
2024/06/14 11:20:20.152 :: Starting nnUNet with the following parameters:
2024/06/14 11:20:20.152 :: 
2024/06/14 11:20:20.152 :: C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs/input -o C:/Users/DELL/AppData/Local/Temp/Slicer-bFASSs/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cuda -chk checkpoint_final.pth --disable_tta
2024/06/14 11:20:20.152 :: 
2024/06/14 11:20:20.152 :: JSON parameters :
2024/06/14 11:20:20.152 :: {
2024/06/14 11:20:20.152 ::     "folds": "0",
2024/06/14 11:20:20.152 ::     "device": "cuda",
2024/06/14 11:20:20.152 ::     "stepSize": 0.5,
2024/06/14 11:20:20.152 ::     "disableTta": true,
2024/06/14 11:20:20.152 ::     "nProcessPreprocessing": 1,
2024/06/14 11:20:20.152 ::     "nProcessSegmentationExport": 1,
2024/06/14 11:20:20.152 ::     "checkPointName": "",
2024/06/14 11:20:20.152 ::     "modelPath": {
2024/06/14 11:20:20.152 ::         "_path": "C:\\Users\\DELL\\AppData\\Local\\slicer.org\\Slicer 5.7.0-2024-06-01\\slicer.org\\Extensions-32886\\DentalSegmentator\\lib\\Slicer-5.7\\qt-scripted-modules\\Resources\\ML"
2024/06/14 11:20:20.152 ::     }
2024/06/14 11:20:20.152 :: }
2024/06/14 11:20:20.159 :: nnUNet preprocessing...
2024/06/14 11:20:21.429 :: Traceback (most recent call last):
2024/06/14 11:20:21.429 ::   File "C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
2024/06/14 11:20:21.430 :: return _run_code(code, main_globals, None,
2024/06/14 11:20:21.430 ::   File "C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\runpy.py", line 87, in _run_code
2024/06/14 11:20:21.430 ::     exec(code, run_globals)
2024/06/14 11:20:21.430 ::   File "C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Scripts\nnUNetv2_predict.exe\__main__.py", line 4, in &lt;module&gt;
2024/06/14 11:20:21.430 ::   File "C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py", line 12, in &lt;module&gt;
2024/06/14 11:20:21.430 ::     from batchgenerators.dataloading.multi_threaded_augmenter import MultiThreadedAugmenter
2024/06/14 11:20:21.430 ::   File "C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01\lib\Python\Lib\site-packages\batchgenerators\dataloading\multi_threaded_augmenter.py", line 26, in &lt;module&gt;
2024/06/14 11:20:21.435 :: from threadpoolctl import threadpool_limits
2024/06/14 11:20:21.435 :: ModuleNotFoundError: No module named 'threadpoolctl'
2024/06/14 11:20:21.613 :: Loading inference results...
2024/06/14 11:20:25.688 :: Error loading results :
2024/06/14 11:20:25.688 :: Failed to load the segmentation.
2024/06/14 11:20:25.688 :: Check the inference folder content C:\Users\DELL\AppData\Local\Temp\Slicer-bFASSs\output
</code></pre>

---

## Post #3 by @muratmaga (2025-04-29 21:21 UTC)

<aside class="quote no-group" data-username="1546161" data-post="1" data-topic="36802">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/1/d07c76/48.png" class="avatar"> 1546161:</div>
<blockquote>
<p>threadpoolctl</p>
</blockquote>
</aside>
<p>in slicer python type<br>
<code>pip_install("threadpoolctl")</code></p>
<p>and then restart and retry. Looks like some libraries are not installed.</p>

---

## Post #4 by @jamesobutler (2025-04-29 21:48 UTC)

<aside class="quote no-group" data-username="1546161" data-post="1" data-topic="36802">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/1/d07c76/48.png" class="avatar"> 1546161:</div>
<blockquote>
<p>C:\Users\DELL\AppData\Local\slicer.org\Slicer 5.7.0-2024-06-01</p>
</blockquote>
</aside>
<p>There were significant updates made in January 2025 to the installation of necessary python packages in the SlicerNNUnet extension which is used by the DentalSegmentator extension. I see that you are using a preview build of Slicer from June 2024. Please download and install latest Slicer Stable (5.8.1) or latest Slicer Preview from <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a> and try using DentalSegmentator. Report back here how it goes for you.</p>
<p>If you run into the following message below, then you have likely run out of system memory as part of running inference.</p>
<blockquote>
<p>RuntimeError: Background workers died. Look for the error message further up! If there is none then your RAM was full and the worker was killed by the OS. Use fewer workers or get more RAM in that case!</p>
</blockquote>

---
