# TotalSegmentator - Failed to compute results

**Topic ID**: 39876
**Date**: 2024-10-27
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-compute-results/39876

---

## Post #1 by @yk_Chen (2024-10-27 04:22 UTC)

<p>Operating system: Windows 10<br>
Slicer version:5.6.2<br>
Hi,<br>
When I ran totalsegmentator in batch yesterday, the computer reported an error and flashed back. The following error occurred when refocusing on automatic segmentation today.<br>
And here is the detail:</p>
<pre><code class="lang-auto">Requirement already satisfied: pillow&lt;10.1 in c:\users\administrator\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (10.0.1)
[Python] Failed to compute results.
[Python] Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
    self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
  File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1002, in process
    self.processVolume(inputFile, inputVolume,
  File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1076, in processVolume
    self.logProcessOutput(proc)
  File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 848, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\
</code></pre>
<p>The following is more detailed info from “report a bug”</p>
<pre><code class="lang-auto">[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Session start time .......: 20241027_121401
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19041, Code Page 65001) - 64-bit
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Memory ...................: 64665 MB physical, 130201 MB virtual
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen 9 7900X 12-Core Processor            , 24 cores, 24 logical processors
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Application path .........: C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin
[DEBUG][Qt] 27.10.2024 12:14:01 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/AirwaySegmentation/lib/Slicer-5.6/cli-modules, slicer.org/Extensions-32448/AirwaySegmentation/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/HDBrainExtraction/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules
[DEBUG][Python] 27.10.2024 12:14:03 [Python] (C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 27.10.2024 12:14:03 [Python] (C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 27.10.2024 12:14:03 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 27.10.2024 12:14:17 [] (unknown:0) - "Volume" Reader has successfully read the file "D:/gastric nii/240242.nii.gz" "[1.41s]"
[DEBUG][Qt] 27.10.2024 12:14:21 [] (unknown:0) - Switch to module:  "TotalSegmentator"
[INFO][Stream] 27.10.2024 12:14:23 [] (unknown:0) - Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
[INFO][Stream] 27.10.2024 12:14:23 [] (unknown:0) - Requirement already satisfied: pillow&lt;10.1 in c:\users\administrator\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (10.0.1)
[INFO][Python] 27.10.2024 12:14:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch...
[INFO][Python] 27.10.2024 12:14:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.4.0+cu118 imported successfully
[INFO][Python] 27.10.2024 12:14:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: True
[INFO][Python] 27.10.2024 12:14:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Processing started
[INFO][Python] 27.10.2024 12:14:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Writing input file to C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/total-segmentator-input.nii
[INFO][Python] 27.10.2024 12:14:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Creating segmentations with TotalSegmentator AI...
[INFO][Python] 27.10.2024 12:14:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Total Segmentator arguments: ['-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/segmentation', '--ml', '--task', 'total']
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Traceback (most recent call last):
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return _run_code(code, main_globals, None,
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     exec(code, run_globals)
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 141, in main
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 119, in totalsegmentator
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     setup_totalseg()
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\config.py", line 60, in setup_totalseg
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     config = json.load(f)
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\__init__.py", line 293, in load
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return loads(fp.read(),
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\__init__.py", line 346, in loads
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return _default_decoder.decode(s)
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py", line 337, in decode
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py", line 355, in raw_decode
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     raise JSONDecodeError("Expecting value", s, err.value) from None
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - If you use this tool please cite: https://pubs.rsna.org/doi/10.1148/ryai.230024
[INFO][Python] 27.10.2024 12:14:27 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -
[ERROR][Python] 27.10.2024 12:14:27 [Python] (C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Failed to compute results.

Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1002, in process
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) -     self.processVolume(inputFile, inputVolume,
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1076, in processVolume
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) -     self.logProcessOutput(proc)
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 848, in logProcessOutput
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 27.10.2024 12:14:29 [] (unknown:0) - subprocess.CalledProcessError: Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+14+25.418/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
[INFO][Python] 27.10.2024 12:16:22 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch...
[INFO][Python] 27.10.2024 12:16:23 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.4.0+cu118 imported successfully
[INFO][Python] 27.10.2024 12:16:23 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: True
[INFO][Python] 27.10.2024 12:16:23 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Processing started
[INFO][Python] 27.10.2024 12:16:23 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Writing input file to C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+16+23.034/total-segmentator-input.nii
[INFO][Python] 27.10.2024 12:16:23 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Creating segmentations with TotalSegmentator AI...
[INFO][Python] 27.10.2024 12:16:23 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Total Segmentator arguments: ['-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+16+23.034/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+16+23.034/segmentation', '--ml', '--task', 'total']
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Traceback (most recent call last):
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return _run_code(code, main_globals, None,
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     exec(code, run_globals)
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 141, in main
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 119, in totalsegmentator
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     setup_totalseg()
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\config.py", line 60, in setup_totalseg
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     config = json.load(f)
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\__init__.py", line 293, in load
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return loads(fp.read(),
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\__init__.py", line 346, in loads
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return _default_decoder.decode(s)
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py", line 337, in decode
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py", line 355, in raw_decode
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     raise JSONDecodeError("Expecting value", s, err.value) from None
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - If you use this tool please cite: https://pubs.rsna.org/doi/10.1148/ryai.230024
[INFO][Python] 27.10.2024 12:16:25 [Python] (C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -
[ERROR][Python] 27.10.2024 12:16:25 [Python] (C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Failed to compute results.

Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+16+23.034/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+16+23.034/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1002, in process
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) -     self.processVolume(inputFile, inputVolume,
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1076, in processVolume
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) -     self.logProcessOutput(proc)
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) -   File "C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 848, in logProcessOutput
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 27.10.2024 12:16:52 [] (unknown:0) - subprocess.CalledProcessError: Command '['C:/Users/Administrator/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\Administrator\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+16+23.034/total-segmentator-input.nii', '-o', 'C:/Users/Administrator/AppData/Local/Temp/Slicer/__SlicerTemp__2024-10-27_12+16+23.034/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
When I run the bulk code in pythonslicer.exe, I get the following error:
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 10, in &lt;module&gt;
  File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 119, in totalsegmentator
    setup_totalseg()
  File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\config.py", line 60, in setup_totalseg
    config = json.load(f)
  File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\__init__.py", line 293, in load
    return loads(fp.read(),
  File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Users\Administrator\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
</code></pre>

---

## Post #2 by @lassoan (2024-10-27 17:54 UTC)

<p>Your TotalSegmentator configuration file got corrupted or was not created correctly. See instructions for resolving the issue <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/README.md#jsondecoderjsondecodeerror-expecting-value-line-1-column-1-char-0">here</a>.</p>

---
