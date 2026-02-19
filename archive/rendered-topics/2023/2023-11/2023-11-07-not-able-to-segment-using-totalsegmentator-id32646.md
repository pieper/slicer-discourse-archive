---
topic_id: 32646
title: "Not Able To Segment Using Totalsegmentator"
date: 2023-11-07
url: https://discourse.slicer.org/t/32646
---

# Not able to segment using TotalSegmentator

**Topic ID**: 32646
**Date**: 2023-11-07
**URL**: https://discourse.slicer.org/t/not-able-to-segment-using-totalsegmentator/32646

---

## Post #1 by @Jaroslav_Ptacek (2023-11-07 18:24 UTC)

<p>I tried every possible step I was able to find here, still it doesn’t work for me. This is what I receive:</p>
<p>Importing torch…<br>
PyTorch 2.1.0+cpu imported successfully<br>
CUDA available: False<br>
Processing started<br>
Writing input file to C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-07_16+05+03.035/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-07_16+05+03.035/total-segmentator-input.nii’, ‘-o’, 'C:/Users/jaros/AppData/Local/Temp/Slicer/_<em>SlicerTemp__2023-11-07_16+05+03.035/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator:5: DeprecationWarning: pkg_resources is deprecated as an API. See <a href="https://setuptools.pypa.io/en/latest/pkg_resources.html" class="inline-onebox" rel="noopener nofollow ugc">Package Discovery and Resource Access using pkg_resources - setuptools 68.2.2.post20231016 documentation</a><br>
from pkg_resources import require<br>
C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\requests_<em>init</em></em>.py:102: RequestsDependencyWarning: urllib3 (1.26.18) or chardet (5.1.0)/charset_normalizer (2.0.12) doesn’t match a supported version!<br>
warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn’t match a supported "</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" class="inline-onebox" rel="noopener nofollow ugc">[2208.05868] TotalSegmentator: robust segmentation of 104 anatomical structures in CT images</a></p>
<p>No GPU detected. Running on CPU. This can be very slow. The ‘–fast’ option can help to some extend.<br>
Using ‘fast’ option: resampling to lower resolution (3mm)<br>
Using ‘fast’ option: resampling to lower resolution (3mm)<br>
ERROR: Failed to compute results.</p>
<p>Command ‘[‘C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.4.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-07_16+05+03.035/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-07_16+05+03.035/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.<br>
Traceback (most recent call last):<br>
File “C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 271, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 781, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.4.0/slicer.org/Extensions-31938/TotalSegmentator/lib/Slicer-5.4/qt-scripted-modules/TotalSegmentator.py”, line 614, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.4.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-07_16+05+03.035/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-07_16+05+03.035/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>
<p>Thanks for help.</p>

---

## Post #2 by @mau_igna_06 (2023-11-07 18:31 UTC)

<aside class="quote no-group" data-username="Jaroslav_Ptacek" data-post="1" data-topic="32646">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaroslav_ptacek/48/68203_2.png" class="avatar"> Jaroslav_Ptacek:</div>
<blockquote>
<p>CUDA available: False</p>
</blockquote>
</aside>
<p>It appears you don’t have CUDA installed. Please try to solve that then try to use the TotalSegmentator module again</p>
<p>Hope it helps</p>

---

## Post #3 by @rbumm (2023-11-08 12:26 UTC)

<p>What are your system specifications ?  Do you have a GPU installed ? Which brand and model ?</p>

---

## Post #4 by @Jaroslav_Ptacek (2023-11-08 14:06 UTC)

<p>Dear Maoro, Rudolf,</p>
<p>in fact I didn’t want to use GPU on purpose for it doesn’t have enough RAM. So I wanted to force use CPU. The segmentation works on my desktop, but is rather slow since it’s an office computer. I’d like to run TotalSegmentator on laptop:</p>
<ul>
<li>HP Victus</li>
<li>AMD Ryzen7 5800H with Radeon Graphics / 16GB RAM</li>
<li>Windows 11</li>
<li>Nvidia GeForce RTX 3060 Laptop GPU (6GB RAM)</li>
</ul>
<p>I had no luck. In this case I’m just a normal user, so the installation became too difficult. I updated the whole system including all drivers.</p>
<p>Thank you for any advice.</p>

---

## Post #5 by @lassoan (2023-11-08 14:49 UTC)

<blockquote>
<p>C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.4.0\lib\Python\Lib\site-packages\requests_<em>init</em>* .py:102: RequestsDependencyWarning: urllib3 (1.26.18) or chardet (5.1.0)/charset_normalizer (2.0.12) doesn’t match a supported version!</p>
</blockquote>
<p>This is the root cause of the error. Package installation fails because some unnecessary requirements specified by nnunet. Probably you have tried to install previous versions of TotalSegmentator in this Slicer installation tree or the Python environment was messed up by some other extensions.</p>
<p>You can fix the issue by uninstalling Slicer and completely wiping off the content of the <code>C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.4.0</code> folder and then installing Slicer again.</p>
<p>I would recommend to install the latest Slicer Preview Release (currently Slicer-5.5), as it installs the new TotalSegmentator version that can segment more structures and has a couple of other improvements.</p>

---

## Post #7 by @rbumm (2023-11-08 14:51 UTC)

<p>Yes, and install Pytorch via the extension, in CPU mode</p>

---

## Post #8 by @linda_varghese (2023-11-09 07:18 UTC)

<p>Hi ,</p>
<p>After the new Updation for Total Segmentator I am also facing similar issues. Even if I change the classes for total or any other.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1c206571a5734945458a0a46f52f9b630150a9b.png" data-download-href="/uploads/short-url/tVBudPx3CMpfI4lZDRLsFwXMtMn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1c206571a5734945458a0a46f52f9b630150a9b_2_690x218.png" alt="image" data-base62-sha1="tVBudPx3CMpfI4lZDRLsFwXMtMn" width="690" height="218" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1c206571a5734945458a0a46f52f9b630150a9b_2_690x218.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1c206571a5734945458a0a46f52f9b630150a9b_2_1035x327.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1c206571a5734945458a0a46f52f9b630150a9b.png 2x" data-dominant-color="E4E3E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1180×373 42.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can anyone help me this?</p>
<p>Thanks &amp; Regards,<br>
Linda</p>

---

## Post #9 by @Jaroslav_Ptacek (2023-11-09 13:55 UTC)

<p>Dear Rudolf and Andras,</p>
<p>I wiped all files repeatedly before and nothing worked. I did again, used the Preview version and installed Pytorch CPU. At first it looked good, it even started to download data (weights?) but than it failed again. The next tries are even worse.</p>
<p>As far as I can see from the log, there’s a memory issue. But this machine has 16GB RAM, and the problem is with allocating 1.14GB?</p>
<p>[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-11-09 14:48:38<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.5.0-2023-11-07 (revision 32301 / 17d23da) win-amd64 - installed release<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 22631, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 15713 MB physical, 16225 MB virtual<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 7 5800H with Radeon Graphics         , 16 cores, 16 logical processors<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/bin<br>
[DEBUG][Qt] 09.11.2023 14:48:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-32301/PyTorch/lib/Slicer-5.5/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32301/PyTorch/lib/Slicer-5.5/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules</a><br>
[DEBUG][Python] 09.11.2023 14:48:43 [Python] (C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Slicer-5.5\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 09.11.2023 14:48:43 [Python] (C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Slicer-5.5\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 09.11.2023 14:48:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 09.11.2023 14:48:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading Slicer RC file [C:/Users/jaros/.slicerrc.py]<br>
[DEBUG][Qt] 09.11.2023 14:48:48 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “DICOM”<br>
[INFO][Python] 09.11.2023 14:48:54 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/bin/…/lib/Slicer-5.5/qt-scripted-modules/DICOMScalarVolumePlugin.py:400) - Loading with imageIOName: GDCM<br>
[INFO][Python] 09.11.2023 14:48:55 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/bin/…/lib/Slicer-5.5/qt-scripted-modules/DICOMScalarVolumePlugin.py:479) - Window/level found in DICOM tags (center=40.0, width=400.0) has been applied to volume 2: Planovani Hrudnik MULAZ POD PRSEM 1,00 Qr40 S3<br>
[DEBUG][Qt] 09.11.2023 14:49:00 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “TotalSegmentator”<br>
[INFO][Stream] 09.11.2023 14:49:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - WARNING: Ignoring invalid distribution -illow (c:\users\jaros\appdata\local\slicer.org\slicer 5.5.0-2023-11-07\lib\python\lib\site-packages)<br>
[INFO][Stream] 09.11.2023 14:49:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Requirement already satisfied: pillow&lt;10.1 in c:\users\jaros\appdata\local\slicer.org\slicer 5.5.0-2023-11-07\lib\python\lib\site-packages (10.0.1)<br>
[INFO][Stream] 09.11.2023 14:49:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - WARNING: Ignoring invalid distribution -illow (c:\users\jaros\appdata\local\slicer.org\slicer 5.5.0-2023-11-07\lib\python\lib\site-packages)<br>
[INFO][Stream] 09.11.2023 14:49:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - WARNING: There was an error checking the latest version of pip.<br>
[INFO][Python] 09.11.2023 14:49:08 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/PyTorch/lib/Slicer-5.5/qt-scripted-modules/PyTorchUtils.py:153) - Importing torch…<br>
[INFO][Python] 09.11.2023 14:49:08 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/PyTorch/lib/Slicer-5.5/qt-scripted-modules/PyTorchUtils.py:190) - PyTorch 2.1.0+cpu imported successfully<br>
[INFO][Python] 09.11.2023 14:49:08 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/PyTorch/lib/Slicer-5.5/qt-scripted-modules/PyTorchUtils.py:191) - CUDA available: False<br>
[INFO][Python] 09.11.2023 14:49:08 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - Processing started<br>
[CRITICAL][Stream] 09.11.2023 14:49:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:880: UserWarning: ‘has_cuda’ is deprecated, please use ‘torch.backends.cuda.is_built()’<br>
[CRITICAL][Stream] 09.11.2023 14:49:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   cuda = torch.cuda if torch.has_cuda and torch.cuda.is_available() else None<br>
[INFO][Python] 09.11.2023 14:49:10 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - Writing input file to C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-09_14+49+08.273/total-segmentator-input.nii<br>
[INFO][Python] 09.11.2023 14:49:10 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - Creating segmentations with TotalSegmentator AI…<br>
[INFO][Python] 09.11.2023 14:49:10 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - Total Segmentator arguments: [‘-i’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-09_14+49+08.273/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-09_14+49+08.273/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - multiprocessing.pool.RemoteTraceback:<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - “”"<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - Traceback (most recent call last):<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\multiprocessing\pool.py”, line 125, in worker<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     result = (True, func(*args, **kwds))<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\multiprocessing\pool.py”, line 51, in starmapstar<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     return list(itertools.starmap(args[0], args[1]))<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\nnunetv2\inference\export_prediction.py”, line 39, in export_prediction_from_softmax<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     segmentation = label_manager.convert_logits_to_segmentation(predicted_array_or_file)<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\nnunetv2\utilities\label_handling\label_handling.py”, line 182, in convert_logits_to_segmentation<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     return self.convert_probabilities_to_segmentation(probabilities)<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\nnunetv2\utilities\label_handling\label_handling.py”, line 175, in convert_probabilities_to_segmentation<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     segmentation = predicted_probabilities.argmax(0)<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.14 GiB for an array with shape (65, 200, 200, 118) and data type float32<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - “”"<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - The above exception was the direct cause of the following exception:<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - Traceback (most recent call last):<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\runpy.py”, line 197, in _run_module_as_main<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     return _run_code(code, main_globals, None,<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\runpy.py”, line 87, in <em>run_code<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     exec(code, run_globals)<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File "C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Scripts\TotalSegmentator.exe_<em>main</em></em>.py", line 7, in <br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\totalsegmentator\bin\TotalSegmentator.py”, line 127, in main<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 293, in totalsegmentator<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     seg_img, ct_img = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 395, in nnUNet_predict_image<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     nnUNetv2_predict(tmp_dir, tmp_dir, task_id, model, folds, trainer, tta,<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 178, in nnUNetv2_predict<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     predict_from_raw_data(dir_in,<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 347, in predict_from_raw_data<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     [i.get() for i in r]<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\site-packages\nnunetv2\inference\predict_from_raw_data.py”, line 347, in <br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     [i.get() for i in r]<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Lib\multiprocessing\pool.py”, line 771, in get<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) -     raise self._value<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.14 GiB for an array with shape (65, 200, 200, 118) and data type float32<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x00000239DBB96040&gt;<br>
[INFO][Python] 09.11.2023 14:50:15 [Python] (C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py:544) - AttributeError: ‘DummyFile’ object has no attribute ‘flush’<br>
[ERROR][Python] 09.11.2023 14:50:16 [Python] (C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\bin\Python\slicer\util.py:2909) - Failed to compute results.</p>
<p>Command ‘[‘C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-09_14+49+08.273/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-09_14+49+08.273/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.<br>
[CRITICAL][Stream] 09.11.2023 14:50:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 09.11.2023 14:50:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 292, in onApplyButton<br>
[CRITICAL][Stream] 09.11.2023 14:50:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
[CRITICAL][Stream] 09.11.2023 14:50:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 967, in process<br>
[CRITICAL][Stream] 09.11.2023 14:50:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.logProcessOutput(proc)<br>
[CRITICAL][Stream] 09.11.2023 14:50:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 787, in logProcessOutput<br>
[CRITICAL][Stream] 09.11.2023 14:50:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
[CRITICAL][Stream] 09.11.2023 14:50:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - subprocess.CalledProcessError: Command ‘[‘C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Python\Scripts\TotalSegmentator.exe’, ‘-i’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-09_14+49+08.273/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/jaros/AppData/Local/Temp/Slicer/__SlicerTemp__2023-11-09_14+49+08.273/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>Do you have any ideas what could be the issue?</p>
<p>Thank you.</p>

---

## Post #10 by @rbumm (2023-11-09 17:52 UTC)

<p>Invest in better hardware with a decent GPU (NVIDIA, 24GB GPU memory)<br>
Good look</p>

---

## Post #11 by @Jaroslav_Ptacek (2023-11-10 09:36 UTC)

<p>Dear Rudolf,</p>
<p>will probably do. On the other hand, TotalSegmenter runs smoothly on my desktop:</p>
<ul>
<li>Intel i5-9600</li>
<li>8GB RAM + Intel graphics (no GPU)</li>
<li>Win11</li>
</ul>
<p>Thus I guess the problem is also somewhere else.</p>

---

## Post #12 by @Jaroslav_Ptacek (2023-11-10 14:10 UTC)

<p>Couldn’t the problem be caused by:</p>
<p>[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2023-11-10 14:51:02<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.5.0-2023-11-07 (revision 32301 / 17d23da) win-amd64 - installed release<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Personal / (Build 22631, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 15713 MB physical, 16225 MB virtual<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 7 5800H with Radeon Graphics         , 16 cores, 16 logical processors<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/bin<br>
[DEBUG][Qt] 10.11.2023 14:51:02 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-32301/PyTorch/lib/Slicer-5.5/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32301/PyTorch/lib/Slicer-5.5/qt-scripted-modules</a>, <a href="http://slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules</a><br>
[DEBUG][Python] 10.11.2023 14:51:05 [Python] (C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Slicer-5.5\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 10.11.2023 14:51:05 [Python] (C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\lib\Slicer-5.5\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:38) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 10.11.2023 14:51:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 10.11.2023 14:51:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading Slicer RC file [C:/Users/jaros/.slicerrc.py]<br>
[DEBUG][Qt] 10.11.2023 14:51:21 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “TotalSegmentator”<br>
[INFO][Stream] 10.11.2023 14:51:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Collecting pandas<br>
[INFO][Stream] 10.11.2023 14:51:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Obtaining dependency information for pandas from <a href="https://files.pythonhosted.org/packages/3f/7a/8ecafdb6a6990ad90f0366a8d7356e9d62118ce832c38ca4fe6136a5e207/pandas-2.1.2-cp39-cp39-win_amd64.whl.metadata" rel="noopener nofollow ugc">https://files.pythonhosted.org/packages/3f/7a/8ecafdb6a6990ad90f0366a8d7356e9d62118ce832c38ca4fe6136a5e207/pandas-2.1.2-cp39-cp39-win_amd64.whl.metadata</a><br>
[INFO][Stream] 10.11.2023 14:51:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Using cached pandas-2.1.2-cp39-cp39-win_amd64.whl.metadata (18 kB)<br>
[INFO][Stream] 10.11.2023 14:51:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Requirement already satisfied: numpy&lt;2,&gt;=1.22.4 in c:\users\jaros\appdata\local\slicer.org\slicer 5.5.0-2023-11-07\lib\python\lib\site-packages (from pandas) (1.26.1)<br>
[INFO][Stream] 10.11.2023 14:51:28 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\jaros\appdata\local\slicer.org\slicer 5.5.0-2023-11-07\lib\python\lib\site-packages (from pandas) (2.8.2)<br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Collecting pytz&gt;=2020.1 (from pandas)<br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Obtaining dependency information for pytz&gt;=2020.1 from <a href="https://files.pythonhosted.org/packages/32/4d/aaf7eff5deb402fd9a24a1449a8119f00d74ae9c2efa79f8ef9994261fc2/pytz-2023.3.post1-py2.py3-none-any.whl.metadata" rel="noopener nofollow ugc">https://files.pythonhosted.org/packages/32/4d/aaf7eff5deb402fd9a24a1449a8119f00d74ae9c2efa79f8ef9994261fc2/pytz-2023.3.post1-py2.py3-none-any.whl.metadata</a><br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Using cached pytz-2023.3.post1-py2.py3-none-any.whl.metadata (22 kB)<br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Collecting tzdata&gt;=2022.1 (from pandas)<br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)<br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Requirement already satisfied: six&gt;=1.5 in c:\users\jaros\appdata\local\slicer.org\slicer 5.5.0-2023-11-07\lib\python\lib\site-packages (from python-dateutil&gt;=2.8.2-&gt;pandas) (1.16.0)<br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Using cached pandas-2.1.2-cp39-cp39-win_amd64.whl (10.8 MB)<br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Using cached pytz-2023.3.post1-py2.py3-none-any.whl (502 kB)<br>
[INFO][Stream] 10.11.2023 14:51:29 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Installing collected packages: pytz, tzdata, pandas<br>
[INFO][Stream] 10.11.2023 14:51:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Successfully installed pandas-2.1.2 pytz-2023.3.post1 tzdata-2023.3<br>
[INFO][Stream] 10.11.2023 14:51:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - WARNING: There was an error checking the latest version of pip.<br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Collecting pillow&lt;10.1<br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Obtaining dependency information for pillow&lt;10.1 from <a href="https://files.pythonhosted.org/packages/a8/fd/ce5fab4a15f4e38c5f6b86377f2c2ef6c92ec9a48e7296048251057a58ec/Pillow-10.0.1-cp39-cp39-win_amd64.whl.metadata" rel="noopener nofollow ugc">https://files.pythonhosted.org/packages/a8/fd/ce5fab4a15f4e38c5f6b86377f2c2ef6c92ec9a48e7296048251057a58ec/Pillow-10.0.1-cp39-cp39-win_amd64.whl.metadata</a><br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Using cached Pillow-10.0.1-cp39-cp39-win_amd64.whl.metadata (9.6 kB)<br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Using cached Pillow-10.0.1-cp39-cp39-win_amd64.whl (2.5 MB)<br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Installing collected packages: pillow<br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Attempting uninstall: pillow<br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     Found existing installation: Pillow 10.1.0<br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     Uninstalling Pillow-10.1.0:<br>
[INFO][Stream] 10.11.2023 14:51:39 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -       Successfully uninstalled Pillow-10.1.0<br>
[INFO][Stream] 10.11.2023 14:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -<br>
[INFO][Stream] 10.11.2023 14:51:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - WARNING: There was an error checking the latest version of pip.<br>
[ERROR][Python] 10.11.2023 14:51:43 [Python] (C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\bin\Python\slicer\util.py:2909) - Failed to upgrade TotalSegmentator</p>
<p>Command ‘[‘C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pillow&lt;10.1’]’ returned non-zero exit status 1.<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 304, in onPackageUpgrade<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     self.logic.setupPythonRequirements(upgrade=True)<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/slicer.org/Extensions-32301/TotalSegmentator/lib/Slicer-5.5/qt-scripted-modules/TotalSegmentator.py”, line 680, in setupPythonRequirements<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     slicer.util.pip_install(“pillow&lt;10.1”)<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\bin\Python\slicer\util.py”, line 3759, in pip_install<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     _executePythonModule(“pip”, args)<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\bin\Python\slicer\util.py”, line 3721, in _executePythonModule<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     logProcessOutput(proc)<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:\Users\jaros\AppData\Local\slicer.org\Slicer 5.5.0-2023-11-07\bin\Python\slicer\util.py”, line 3690, in logProcessOutput<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
[CRITICAL][Stream] 10.11.2023 14:54:33 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - subprocess.CalledProcessError: Command ‘[‘C:/Users/jaros/AppData/Local/slicer.org/Slicer 5.5.0-2023-11-07/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pillow&lt;10.1’]’ returned non-zero exit status 1.</p>
<p>There seems to be some problem with Pillow installation, but I’m not able to solve that.</p>

---
