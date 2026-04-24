---
topic_id: 46820
title: "Totalsegmentator Keeps Returning Non Zero Exit Status 1"
date: 2026-04-24
url: https://discourse.slicer.org/t/46820
---

# TotalSegmentator keeps returning non-zero exit status 1

**Topic ID**: 46820
**Date**: 2026-04-24
**URL**: https://discourse.slicer.org/t/totalsegmentator-keeps-returning-non-zero-exit-status-1/46820

---

## Post #1 by @its-charliem (2026-04-24 01:24 UTC)

<p>Problem report for 3D Slicer 5.10.0 win-amd64: [please describe expected and actual behavior]</p>
<p>Command ‘[‘C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../bin\\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘monai[fire,pyyaml,nibabel,pynrrd,psutil,tensorboard,skimage,itk,tqdm]&gt;=1.3’, ‘–upgrade’]’ returned non-zero exit status 1.</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - Traceback (most recent call last):</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - File “C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/MONAIAuto3DSeg/lib/Slicer-5.10/qt-scripted-modules/MONAIAuto3DSeg.py”, line 775, in onPackageUpgrade</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - restartRequired = self.logic.setupPythonRequirements(upgrade=True)</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - File “C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/MONAIAuto3DSeg/lib/Slicer-5.10/qt-scripted-modules/MONAIAuto3DSeg.py”, line 1099, in setupPythonRequirements</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - self.DEPENDENCY_HANDLER.setupPythonRequirements(upgrade)</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\slicer.org\Extensions-34045\MONAIAuto3DSeg\lib\Slicer-5.10\qt-scripted-modules\MONAIAuto3DSegLib\dependency_handler.py”, line 92, in setupPythonRequirements</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - slicer.util.pip_install(monaiInstallString)</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\bin\Python\slicer\util.py”, line 4034, in pip_install</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - _executePythonModule(“pip”, args)</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\bin\Python\slicer\util.py”, line 3988, in _executePythonModule</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - logProcessOutput(proc)</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\bin\Python\slicer\util.py”, line 3954, in logProcessOutput</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>[CRITICAL][Stream] 23.04.2026 09:04:48 [] (unknown:0) - subprocess.CalledProcessError: Command ‘[‘C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../bin\\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘monai[fire,pyyaml,nibabel,pynrrd,psutil,tensorboard,skimage,itk,tqdm]&gt;=1.3’, ‘–upgrade’]’ returned non-zero exit status 1.</p>
<p>[DEBUG][Qt] 23.04.2026 09:04:52 [] (unknown:0) - Switch to module: “TotalSegmentator”</p>
<p>[INFO][Python] 23.04.2026 09:05:02 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch…</p>
<p>[INFO][Python] 23.04.2026 09:05:03 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.9.1+cu126 imported successfully</p>
<p>[INFO][Python] 23.04.2026 09:05:03 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/PyTorch/lib/Slicer-5.10/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: True</p>
<p>[INFO][Python] 23.04.2026 09:05:03 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - Processing started</p>
<p>[INFO][Python] 23.04.2026 09:05:03 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - Writing input file to C:/Users/DiMO 3D 1/AppData/Local/Temp/Slicer/__SlicerTemp__2026-04-23_09+05+03.721/total-segmentator-input.nii</p>
<p>[INFO][Python] 23.04.2026 09:05:04 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - Creating segmentations with TotalSegmentator AI…</p>
<p>[INFO][Python] 23.04.2026 09:05:04 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - Total Segmentator arguments: [‘-i’, ‘C:/Users/DiMO 3D 1/AppData/Local/Temp/Slicer/__SlicerTemp__2026-04-23_09+05+03.721/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/DiMO 3D 1/AppData/Local/Temp/Slicer/__SlicerTemp__2026-04-23_09+05+03.721/segmentation’, ‘–device’, ‘gpu’, ‘–ml’, ‘–task’, ‘total’]</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - Traceback (most recent call last):</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - File “”, line 198, in _run_module_as_main</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - File “”, line 88, in _run_code</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Python\Scripts\TotalSegmentator.exe\_<em>main</em>_.py”, line 7, in </p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 201, in main</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 156, in totalsegmentator</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - from totalsegmentator.nnunet import nnUNet_predict_image # this has to be after setting new env vars</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</p>
<p>[INFO][Python] 23.04.2026 09:05:08 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 28, in </p>
<p>[INFO][Python] 23.04.2026 09:05:09 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - from nnunetv2.utilities.find_class_by_name import recursive_find_python_class</p>
<p>[INFO][Python] 23.04.2026 09:05:09 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - File “C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\lib\Python\Lib\site-packages\nnunetv2\utilities\find_class_by_name.py”, line 4, in </p>
<p>[INFO][Python] 23.04.2026 09:05:09 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - from batchgenerators.utilities.file_and_folder_operations import *</p>
<p>[INFO][Python] 23.04.2026 09:05:09 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - ModuleNotFoundError: No module named ‘batchgenerators’</p>
<p>[INFO][Python] 23.04.2026 09:05:09 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) -</p>
<p>[INFO][Python] 23.04.2026 09:05:09 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) - If you use this tool please cite: <a href="https://pubs.rsna.org/doi/10.1148/ryai.230024" rel="noopener nofollow ugc">https://pubs.rsna.org/doi/10.1148/ryai.230024</a></p>
<p>[INFO][Python] 23.04.2026 09:05:09 [Python] (C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py:687) -</p>
<p>[ERROR][Python] 23.04.2026 09:05:09 [Python] (C:\Users\DiMO 3D 1\AppData\Local\slicer.org\3D Slicer 5.10.0\bin\Python\slicer\util.py:3146) - Failed to compute results.</p>
<p>Command ‘[‘C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../bin\\PythonSlicer.EXE’, ‘C:\\Users\\DiMO 3D 1\\AppData\\Local\\slicer.org\\3D Slicer 5.10.0\\lib\\Python\\Scripts\\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/DiMO 3D 1/AppData/Local/Temp/Slicer/__SlicerTemp__2026-04-23_09+05+03.721/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/DiMO 3D 1/AppData/Local/Temp/Slicer/__SlicerTemp__2026-04-23_09+05+03.721/segmentation’, ‘–device’, ‘gpu’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - Traceback (most recent call last):</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - File “C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py”, line 360, in onApplyButton</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - File “C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py”, line 1132, in process</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - self.processVolume(inputFile, inputVolume,</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - File “C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py”, line 1216, in processVolume</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - self.logProcessOutput(proc)</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - File “C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/slicer.org/Extensions-34045/TotalSegmentator/lib/Slicer-5.10/qt-scripted-modules/TotalSegmentator.py”, line 964, in logProcessOutput</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>[CRITICAL][Stream] 23.04.2026 09:05:27 [] (unknown:0) - subprocess.CalledProcessError: Command ‘[‘C:/Users/DiMO 3D 1/AppData/Local/slicer.org/3D Slicer 5.10.0/bin/../bin\\PythonSlicer.EXE’, ‘C:\\Users\\DiMO 3D 1\\AppData\\Local\\slicer.org\\3D Slicer 5.10.0\\lib\\Python\\Scripts\\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/DiMO 3D 1/AppData/Local/Temp/Slicer/__SlicerTemp__2026-04-23_09+05+03.721/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/DiMO 3D 1/AppData/Local/Temp/Slicer/__SlicerTemp__2026-04-23_09+05+03.721/segmentation’, ‘–device’, ‘gpu’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 1.</p>

---
