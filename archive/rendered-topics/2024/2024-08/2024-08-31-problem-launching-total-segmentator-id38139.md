---
topic_id: 38139
title: "Problem Launching Total Segmentator"
date: 2024-08-31
url: https://discourse.slicer.org/t/38139
---

# Problem launching total segmentator

**Topic ID**: 38139
**Date**: 2024-08-31
**URL**: https://discourse.slicer.org/t/problem-launching-total-segmentator/38139

---

## Post #1 by @MikeSala (2024-08-31 11:00 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abbedd4053037fdcd41f7aa13c5e1435d582741f.jpeg" data-download-href="/uploads/short-url/ovkztHIPBVhTm4io8Pj8zvCrJgz.jpeg?dl=1" title="problem total segmentator" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbedd4053037fdcd41f7aa13c5e1435d582741f_2_690x201.jpeg" alt="problem total segmentator" data-base62-sha1="ovkztHIPBVhTm4io8Pj8zvCrJgz" width="690" height="201" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbedd4053037fdcd41f7aa13c5e1435d582741f_2_690x201.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbedd4053037fdcd41f7aa13c5e1435d582741f_2_1035x301.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abbedd4053037fdcd41f7aa13c5e1435d582741f_2_1380x402.jpeg 2x" data-dominant-color="888587"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">problem total segmentator</span><span class="informations">1920×560 97 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello,</p>
<p>I am a radiologist and I use total segmentator a lot.<br>
I have a problem with my total segmentator.<br>
When I run it on a CT scan of the abdomen, it displays an error message.<br>
Can anyone help me please.<br>
I have version 5.6.2 of 3D slicer and the latest update of total segmentator.<br>
Total segmentator has always worked very well so far.<br>
Thanks for your help,</p>
<p>Mike</p>

---

## Post #2 by @pieper (2024-08-31 14:17 UTC)

<p>Use the “Help-&gt;Report a bug” menu to get the full log file for a failed run and look at it for more diagnostic info.  If you still need help, post the log here (make sure it doesn’t have patient information in it).</p>

---

## Post #3 by @MikeSala (2024-09-08 13:35 UTC)

<pre><code class="lang-auto">DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Session start time .......: 20240908_153253
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Slicer version ...........: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Operating system .........: Windows /  Personal / (Build 22631, Code Page 65001) - 64-bit
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Memory ...................: 65369 MB physical, 75097 MB virtual
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - CPU ......................: GenuineIntel , 32 cores, 32 logical processors
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Developer mode ...........: disabled
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Application path .........: C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/bin
[DEBUG][Qt] 08.09.2024 15:32:53 [] (unknown:0) - Additional module paths ..: slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/MONAILabel/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/NvidiaAIAssistedAnnotation/lib/Slicer-5.6/qt-scripted-modules, slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules
[DEBUG][Python] 08.09.2024 15:32:54 [Python] (C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 08.09.2024 15:32:54 [Python] (C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 08.09.2024 15:32:54 [] (unknown:0) - Switch to module:  "Welcome"
[INFO][Python] 08.09.2024 15:32:54 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/NvidiaAIAssistedAnnotation/lib/Slicer-5.6/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/NvidiaAIAssistedAnnotation/lib/Slicer-5.6/qt-scripted-modules
[DEBUG][Qt] 08.09.2024 15:32:56 [] (unknown:0) - Switch to module:  "DICOM"
[INFO][Python] 08.09.2024 15:33:00 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:446) - Loading with imageIOName: GDCM
[INFO][Python] 08.09.2024 15:33:03 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/bin/../lib/Slicer-5.6/qt-scripted-modules/DICOMScalarVolumePlugin.py:525) - Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 3: Abdomen Veneus
[DEBUG][Qt] 08.09.2024 15:33:07 [] (unknown:0) - Switch to module:  "TotalSegmentator"
[INFO][Stream] 08.09.2024 15:33:15 [] (unknown:0) - Requirement already satisfied: pillow&lt;10.1 in c:\users\salav\appdata\local\slicer.org\slicer 5.6.2\lib\python\lib\site-packages (10.0.1)
[INFO][Python] 08.09.2024 15:33:17 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch...
[INFO][Python] 08.09.2024 15:33:17 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.3.1+cu118 imported successfully
[INFO][Python] 08.09.2024 15:33:17 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/PyTorch/lib/Slicer-5.6/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: True
[INFO][Python] 08.09.2024 15:33:17 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Processing started
[INFO][Python] 08.09.2024 15:33:17 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Writing input file to C:/Users/salav/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-08_15+33+17.326/total-segmentator-input.nii
[INFO][Python] 08.09.2024 15:33:17 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Creating segmentations with TotalSegmentator AI...
[INFO][Python] 08.09.2024 15:33:17 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Total Segmentator arguments: ['-i', 'C:/Users/salav/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-08_15+33+17.326/total-segmentator-input.nii', '-o', 'C:/Users/salav/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-08_15+33+17.326/segmentation', '--ml', '--task', 'total']
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - Traceback (most recent call last):
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 197, in _run_module_as_main
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return _run_code(code, main_globals, None,
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\runpy.py", line 87, in _run_code
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     exec(code, run_globals)
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Scripts\TotalSegmentator.exe\__main__.py", line 7, in &lt;module&gt;
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py", line 141, in main
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\python_api.py", line 119, in totalsegmentator
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     setup_totalseg()
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\site-packages\totalsegmentator\config.py", line 60, in setup_totalseg
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     config = json.load(f)
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\__init__.py", line 293, in load
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return loads(fp.read(),
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\__init__.py", line 346, in loads
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     return _default_decoder.decode(s)
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py", line 337, in decode
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -   File "C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\lib\Python\Lib\json\decoder.py", line 355, in raw_decode
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -     raise JSONDecodeError("Expecting value", s, err.value) from None
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) - If you use this tool please cite: https://pubs.rsna.org/doi/10.1148/ryai.230024
[INFO][Python] 08.09.2024 15:33:19 [Python] (C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py:595) -
[ERROR][Python] 08.09.2024 15:33:19 [Python] (C:\Users\salav\AppData\Local\slicer.org\Slicer 5.6.2\bin\Python\slicer\util.py:3009) - Failed to compute results.

Command '['C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\salav\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/salav/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-08_15+33+17.326/total-segmentator-input.nii', '-o', 'C:/Users/salav/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-08_15+33+17.326/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) -   File "C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 307, in onApplyButton
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) -   File "C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1001, in process
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) -     self.processVolume(inputFile, inputVolume,
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) -   File "C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 1075, in processVolume
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) -     self.logProcessOutput(proc)
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) -   File "C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/slicer.org/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py", line 847, in logProcessOutput
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
[CRITICAL][Stream] 08.09.2024 15:33:24 [] (unknown:0) - subprocess.CalledProcessError: Command '['C:/Users/salav/AppData/Local/slicer.org/Slicer 5.6.2/bin/../bin\\PythonSlicer.EXE', 'C:\\Users\\salav\\AppData\\Local\\slicer.org\\Slicer 5.6.2\\lib\\Python\\Scripts\\TotalSegmentator.exe', '-i', 'C:/Users/salav/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-08_15+33+17.326/total-segmentator-input.nii', '-o', 'C:/Users/salav/AppData/Local/Temp/Slicer/__SlicerTemp__2024-09-08_15+33+17.326/segmentation', '--ml', '--task', 'total']' returned non-zero exit status 1.
</code></pre>

---

## Post #4 by @MikeSala (2024-09-08 13:37 UTC)

<p>How can I get the total segmentator to work again, I really don’t understand. While MonaiAuto3DSeg.<br>
Only there is no head and neck model on Monai Auto 3DSeg. If you could help me thank you.</p>

---

## Post #5 by @pieper (2024-09-08 13:42 UTC)

<p>Maybe you are seeing this issue: <a href="https://discourse.slicer.org/t/i-broke-my-totalsegmentator/32206/5" class="inline-onebox">I broke my totalsegmentator - #5 by lassoan</a></p>

---

## Post #6 by @Matteboo (2024-09-09 09:09 UTC)

<p>Hello,<br>
Have you tried to force reinstall/manually downlaod the weight in the advanced section of the module ?<br>
That’s what fixed it for me last time</p>

---

## Post #7 by @lassoan (2024-09-11 20:06 UTC)

<p>According to the log, an error occurs when TotalSegmentator attempts to read its configuration <code>C:\Users\salav\.totalsegmentator\config.json</code> file. Its content seems to be invalid. Probably the easiest fix is to delete this file.</p>

---

## Post #8 by @MikeSala (2024-09-12 04:28 UTC)

<p>Thank you all, that’s what I did and it’s working now.<br>
…Thank you.<br>
Mike</p>

---
