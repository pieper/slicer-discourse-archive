---
topic_id: 48375
title: "DentalSegmentator : error loading results : failt to load the segmentation. "
date: 2026-10-01
url: https://discourse.slicer.org/t/48375
last_bumped: 2026-10-02T07:48:34.260Z
---

# DentalSegmentator : error loading results : failt to load the segmentation. 

**Topic ID**: 48375
**Date**: 2026-10-01
**URL**: https://discourse.slicer.org/t/dentalsegmentator-error-loading-results-failt-to-load-the-segmentation/48375

---

## Post #1 by @samzou974 (2026-10-01 14:52 UTC)

<p>Operating system:Windows 11 PRO<br>
Slicer version: 5.12.4<br>
Expected behavior: Segmentation of Cone-Beam using DentalSegmentator extension<br>
Actual behavior: error</p>
<p>2026/10/01 12:32:47.256 :: nnUNet is already installed (2.8.1) and compatible with requested version (nnunetv2).</p>
<p>2026/10/01 12:32:50.322 :: Transferring volume to nnUNet in C:/Users/Bureau01/AppData/Local/Temp/Slicer-WlePvN</p>
<p>2026/10/01 12:32:59.229 :: Starting nnUNet with the following parameters:</p>
<p>2026/10/01 12:32:59.229 ::</p>
<p>2026/10/01 12:32:59.229 :: C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/Bureau01/AppData/Local/Temp/Slicer-WlePvN/input -o C:/Users/Bureau01/AppData/Local/Temp/Slicer-WlePvN/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cuda -chk checkpoint_final.pth --disable_tta</p>
<p>2026/10/01 12:32:59.229 ::</p>
<p>2026/10/01 12:32:59.229 :: JSON parameters :</p>
<p>2026/10/01 12:32:59.229 :: {</p>
<p>2026/10/01 12:32:59.229 ::     “folds”: “0”,</p>
<p>2026/10/01 12:32:59.229 ::     “device”: “cuda”,</p>
<p>2026/10/01 12:32:59.229 ::     “stepSize”: 0.5,</p>
<p>2026/10/01 12:32:59.229 ::     “disableTta”: true,</p>
<p>2026/10/01 12:32:59.229 ::     “nProcessPreprocessing”: 1,</p>
<p>2026/10/01 12:32:59.229 ::     “nProcessSegmentationExport”: 1,</p>
<p>2026/10/01 12:32:59.229 ::     “checkPointName”: “”,</p>
<p>2026/10/01 12:32:59.229 ::     “modelPath”: {</p>
<p>2026/10/01 12:32:59.229 ::         “_path”: “C:\\ProgramData\\slicer.org\\3D Slicer 5.12.4\\slicer.org\\Extensions-34645\\DentalSegmentator\\lib\\Slicer-5.12\\qt-scripted-modules\\Resources\\ML”</p>
<p>2026/10/01 12:32:59.229 ::     }</p>
<p>2026/10/01 12:32:59.229 :: }</p>
<p>2026/10/01 12:32:59.248 :: nnUNet preprocessing…</p>
<p>2026/10/01 12:33:02.363 :: Traceback (most recent call last):</p>
<p>2026/10/01 12:33:02.363 ::   File “”, line 198, in _run_module_as_main</p>
<p>2026/10/01 12:33:02.363 ::   File “”, line 88, in _run_code</p>
<p>2026/10/01 12:33:02.363 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Scripts\nnUNetv2_predict.exe\_<em>main</em>_.py”, line 2, in </p>
<p>2026/10/01 12:33:02.365 :: File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 23, in </p>
<p>2026/10/01 12:33:02.365 ::     from nnunetv2.configuration import default_num_processes</p>
<p>2026/10/01 12:33:02.365 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\site-packages\nnunetv2\configuration.py”, line 10, in </p>
<p>2026/10/01 12:33:02.365 ::     default_n_proc_DA = get_allowed_n_proc_DA()</p>
<p>2026/10/01 12:33:02.365 ::                         ^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/01 12:33:02.365 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\site-packages\nnunetv2\utilities\default_n_proc_DA.py”, line 23, in get_allowed_n_proc_DA</p>
<p>2026/10/01 12:33:02.365 ::     hostname = subprocess.getoutput([‘hostname’])</p>
<p>2026/10/01 12:33:02.365 ::                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/01 12:33:02.365 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\subprocess.py”, line 691, in getoutput</p>
<p>2026/10/01 12:33:02.365 ::     return getstatusoutput(cmd, encoding=encoding, errors=errors)[1]</p>
<p>2026/10/01 12:33:02.365 ::            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/01 12:33:02.365 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\subprocess.py”, line 671, in getstatusoutput</p>
<p>2026/10/01 12:33:02.365 ::     data = check_output(cmd, shell=True, text=True, stderr=STDOUT,</p>
<p>2026/10/01 12:33:02.365 ::            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/01 12:33:02.365 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\subprocess.py”, line 466, in check_output</p>
<p>2026/10/01 12:33:02.365 ::     return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,</p>
<p>2026/10/01 12:33:02.365 ::            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/01 12:33:02.365 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\subprocess.py”, line 550, in run</p>
<p>2026/10/01 12:33:02.365 ::     stdout, stderr = process.communicate(input, timeout=timeout)</p>
<p>2026/10/01 12:33:02.365 ::                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/01 12:33:02.365 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.12.4\lib\Python\Lib\subprocess.py”, line 1196, in communicate</p>
<p>2026/10/01 12:33:02.366 :: stdout = self.stdout.read()</p>
<p>2026/10/01 12:33:02.366 ::              ^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/01 12:33:02.366 ::   File “”, line 322, in decode</p>
<p>2026/10/01 12:33:02.366 :: UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0x82 in position 86: invalid start byte</p>
<p>2026/10/01 12:33:02.881 :: Loading inference results…</p>
<p>2026/10/01 12:33:07.035 :: Error loading results :</p>
<p>2026/10/01 12:33:07.035 :: Failed to load the segmentation.</p>
<p>2026/10/01 12:33:07.035 :: Something went wrong during the nnUNet processing.</p>
<p>2026/10/01 12:33:07.035 :: Please check the logs for potential errors and contact the library maintainers.</p>
<p>Thank you for your help !! Have a nice day !</p>

---

## Post #2 by @samzou974 (2026-10-02 05:17 UTC)

<p>I tried with the 5.13.0 on an other computer, and it work well… no error.<br>
So i uninstall everything (3d Slicer 5.12 and extensions) on the 1st computer, then I installed 5.13 version and extension (DentalSegmentator) : still the same error :</p>
<blockquote>
<p>2026/10/02 09:06:53.981 :: PyTorch Python package is required. Installing… (it may take several minutes)2026/10/02 09:09:04.957 :: nnUNet installation completed successfully.</p>
<p>2026/10/02 09:09:04.961 :: Downloading model weights…</p>
<p>2026/10/02 09:09:29.570 :: Transferring volume to nnUNet in C:/Users/Bureau01/AppData/Local/Temp/Slicer-DKvOSY</p>
<p>2026/10/02 09:09:41.372 :: Starting nnUNet with the following parameters:</p>
<p>2026/10/02 09:09:41.372 ::</p>
<p>2026/10/02 09:09:41.372 :: C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Scripts\nnUNetv2_predict.exe -i C:/Users/Bureau01/AppData/Local/Temp/Slicer-DKvOSY/input -o C:/Users/Bureau01/AppData/Local/Temp/Slicer-DKvOSY/output -d Dataset111_453CT -tr nnUNetTrainer -p nnUNetPlans -c 3d_fullres -f 0 -npp 1 -nps 1 -step_size 0.5 -device cuda -chk checkpoint_final.pth --disable_tta</p>
<p>2026/10/02 09:09:41.372 ::</p>
<p>2026/10/02 09:09:41.372 :: JSON parameters :</p>
<p>2026/10/02 09:09:41.372 :: {</p>
<p>2026/10/02 09:09:41.372 ::     “folds”: “0”,</p>
<p>2026/10/02 09:09:41.372 ::     “device”: “cuda”,</p>
<p>2026/10/02 09:09:41.372 ::     “stepSize”: 0.5,</p>
<p>2026/10/02 09:09:41.372 ::     “disableTta”: true,</p>
<p>2026/10/02 09:09:41.372 ::     “nProcessPreprocessing”: 1,</p>
<p>2026/10/02 09:09:41.372 ::     “nProcessSegmentationExport”: 1,</p>
<p>2026/10/02 09:09:41.372 ::     “checkPointName”: “”,</p>
<p>2026/10/02 09:09:41.372 ::     “modelPath”: {</p>
<p>2026/10/02 09:09:41.372 ::         “_path”: “C:\\ProgramData\\slicer.org\\3D Slicer 5.13.0-2026-09-30\\slicer.org\\Extensions-35317\\DentalSegmentator\\lib\\Slicer-5.13\\qt-scripted-modules\\Resources\\ML”</p>
<p>2026/10/02 09:09:41.372 ::     }</p>
<p>2026/10/02 09:09:41.372 :: }</p>
<p>2026/10/02 09:09:41.398 :: nnUNet preprocessing…</p>
<p>2026/10/02 09:09:44.911 :: Traceback (most recent call last):</p>
<p>2026/10/02 09:09:44.911 ::   File “”, line 198, in _run_module_as_main</p>
<p>2026/10/02 09:09:44.911 ::   File “”, line 88, in _run_code</p>
<p>2026/10/02 09:09:44.911 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Scripts\nnUNetv2_predict.exe\_<em>main</em>_.py”, line 2, in </p>
<p>2026/10/02 09:09:44.919 :: File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 23, in </p>
<p>2026/10/02 09:09:44.919 ::     from nnunetv2.configuration import default_num_processes</p>
<p>2026/10/02 09:09:44.919 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Lib\site-packages\nnunetv2\configuration.py”, line 10, in </p>
<p>2026/10/02 09:09:44.919 ::     default_n_proc_DA = get_allowed_n_proc_DA()</p>
<p>2026/10/02 09:09:44.919 ::                         ^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/02 09:09:44.919 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Lib\site-packages\nnunetv2\utilities\default_n_proc_DA.py”, line 23, in get_allowed_n_proc_DA</p>
<p>2026/10/02 09:09:44.919 ::     hostname = subprocess.getoutput([‘hostname’])</p>
<p>2026/10/02 09:09:44.919 ::                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/02 09:09:44.919 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Lib\subprocess.py”, line 691, in getoutput</p>
<p>2026/10/02 09:09:44.919 ::     return getstatusoutput(cmd, encoding=encoding, errors=errors)[1]</p>
<p>2026/10/02 09:09:44.919 ::            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/02 09:09:44.919 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Lib\subprocess.py”, line 671, in getstatusoutput</p>
<p>2026/10/02 09:09:44.919 ::     data = check_output(cmd, shell=True, text=True, stderr=STDOUT,</p>
<p>2026/10/02 09:09:44.919 ::            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/02 09:09:44.919 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Lib\subprocess.py”, line 466, in check_output</p>
<p>2026/10/02 09:09:44.919 ::     return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,</p>
<p>2026/10/02 09:09:44.919 ::            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/02 09:09:44.919 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Lib\subprocess.py”, line 550, in run</p>
<p>2026/10/02 09:09:44.919 ::     stdout, stderr = process.communicate(input, timeout=timeout)</p>
<p>2026/10/02 09:09:44.919 ::                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/02 09:09:44.919 ::   File “C:\ProgramData\slicer.org\3D Slicer 5.13.0-2026-09-30\lib\Python\Lib\subprocess.py”, line 1196, in communicate</p>
<p>2026/10/02 09:09:44.919 ::     stdout = self.stdout.read()</p>
<p>2026/10/02 09:09:44.919 ::              ^^^^^^^^^^^^^^^^^^</p>
<p>2026/10/02 09:09:44.919 ::   File “”, line 322, in decode</p>
<p>2026/10/02 09:09:44.919 :: UnicodeDecodeError: ‘utf-8’ codec can’t decode byte 0x82 in position 86: invalid start byte</p>
<p>2026/10/02 09:09:45.449 :: Loading inference results…</p>
<p>2026/10/02 09:09:50.156 :: Error loading results :</p>
<p>2026/10/02 09:09:50.156 :: Failed to load the segmentation.</p>
<p>2026/10/02 09:09:50.156 :: Something went wrong during the nnUNet processing.</p>
<p>2026/10/02 09:09:50.156 :: Please check the logs for potential errors and contact the library maintainers.</p>
</blockquote>
<p>Let me know if you can help me ! Thank you !</p>

---

## Post #3 by @Thibault_Pelletier (2026-10-02 07:08 UTC)

<p>Hi <a class="mention" href="/u/samzou974">@samzou974</a>,</p>
<p>Thanks for reporting this error.<br>
I’m investigating where the problem may come from and I’ll get back to you if I have a solution to test.</p>

---

## Post #4 by @Thibault_Pelletier (2026-10-02 07:48 UTC)

<p>Hi <a class="mention" href="/u/samzou974">@samzou974</a>,</p>
<p>Looking at the nnUNet code, it seems to be accessing the hostname at some given time which will yield problems depending on the host local langage.</p>
<p>Can you try defining the following env variables in your console and running the inference:</p>
<pre data-code-wrap="python"><code class="lang-python">import os

cpu_count = os.cpu_count() or 1
os.environ["nnUNet_n_proc_DA"] = str(min(12, cpu_count))
os.environ["nnUNet_def_n_proc"] = str(min(8, cpu_count))
</code></pre>

---
