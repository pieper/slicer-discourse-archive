---
topic_id: 28727
title: "Total Segmentator On 5 2 2 Scikit Learn Distribution Not Fou"
date: 2023-04-03
url: https://discourse.slicer.org/t/28727
---

# Total Segmentator on 5.2.2 "scikit-learn" distribution not found

**Topic ID**: 28727
**Date**: 2023-04-03
**URL**: https://discourse.slicer.org/t/total-segmentator-on-5-2-2-scikit-learn-distribution-not-found/28727

---

## Post #1 by @tsehrhardt (2023-04-03 12:07 UTC)

<p>After installing Slicer 5.2.2, Total Segmentator is no longer working. I read through the troubleshooting and uninstalled/reinstalled PyTorch and did a Force reinstall of Total Segmentator, but still can’t run it. I’m just using one of the cardiac sample datasets, so it’s small. The error is saying that the “scikit-learn” distribution is not found.</p>
<pre><code class="lang-auto">Processing started
Writing input file to C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-03_08+02+51.749/total-segmentator-input.nii
Creating segmentations with TotalSegmentator AI...
Total Segmentator arguments: ['-i', 'C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-03_08+02+51.749/total-segmentator-input.nii', '-o', 'C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-03_08+02+51.749/segmentation', '--ml', '--task', 'total']
Traceback (most recent call last):
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator", line 93, in &lt;module&gt;
    main()
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator", line 82, in main
    parser.add_argument('--version', action='version', version=require("TotalSegmentator")[0].version)
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 956, in require
    needed = self.resolve(parse_requirements(requirements))
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 815, in resolve
    dist = self._resolve_dist(
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 856, in _resolve_dist
    raise DistributionNotFound(req, requirers)
pkg_resources.DistributionNotFound: The 'scikit-learn' distribution was not found and is required by batchgenerators, nnunet-customized
</code></pre>

---

## Post #2 by @rbumm (2023-04-03 12:53 UTC)

<p>Hello, on which operating system are you?</p>

---

## Post #3 by @tsehrhardt (2023-04-03 12:55 UTC)

<p>I am using Windows 10.</p>

---

## Post #4 by @rbumm (2023-04-03 13:27 UTC)

<p>Just tested the whole process again (Windows 11, Laptop, GTX 1060 6 GB video RAM)</p>
<ul>
<li>Downloaded Slicer 3.2.2</li>
<li>Installed into a fresh directory</li>
<li>Started 3D Slicer</li>
<li>Installed the Pytorch extension</li>
<li>Restarted</li>
<li>Installed the TotalSegmentator extension</li>
<li>Restarted</li>
<li>Loaded a test dataset</li>
<li>Switched to Totalsegmentator</li>
<li>Pressed “Apply”</li>
<li>Received one error message during the following installation processes (torch etc). This is a known error that happens every time during first installation. We are working to find a solution here.</li>
<li>Restarted Slicer</li>
<li>Switched to Totalsegmentator</li>
<li>Pressed “Apply” (fast mode)</li>
<li>installation continues, then segmentation</li>
<li>Got a good segmentation result.</li>
</ul>

---

## Post #5 by @tsehrhardt (2023-04-03 13:59 UTC)

<p>I went through this a few times and managed to achieve something different if I uninstalled PyTorch, restarted, and let Total Segmentator install it on the first run, restarted, ran TS again and got this:</p>
<pre><code class="lang-auto">Processing started
Writing input file to C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-03_09+56+09.275/total-segmentator-input.nii
Creating segmentations with TotalSegmentator AI...
Total Segmentator arguments: ['-i', 'C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-03_09+56+09.275/total-segmentator-input.nii', '-o', 'C:/Users/starb/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-03_09+56+09.275/segmentation', '--ml', '--task', 'total']
Traceback (most recent call last):
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator", line 93, in &lt;module&gt;
    main()
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator", line 82, in main
    parser.add_argument('--version', action='version', version=require("TotalSegmentator")[0].version)
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 956, in require
    needed = self.resolve(parse_requirements(requirements))
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 815, in resolve
    dist = self._resolve_dist(
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 844, in _resolve_dist
    env = Environment(self.entries)
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 1044, in __init__
    self.scan(search_path)
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 1077, in scan
    self.add(dist)
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 1096, in add
    dists.sort(key=operator.attrgetter('hashcmp'), reverse=True)
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 2631, in hashcmp
    self.parsed_version,
  File "C:\Users\starb\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Lib\site-packages\pkg_resources\__init__.py", line 2685, in parsed_version
    raise packaging.version.InvalidVersion(f"{str(ex)} {info}") from None
pkg_resources.extern.packaging.version.InvalidVersion: Invalid version: 'rch' (package: -)
</code></pre>
<p>This is the PyTorch version installed by TS:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/975be04585bd12ae2a9e63cdeaca9e186f2f0cd1.png" data-download-href="/uploads/short-url/lAYWntkCifb4yQOOBchDFVztD9v.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/975be04585bd12ae2a9e63cdeaca9e186f2f0cd1.png" alt="image" data-base62-sha1="lAYWntkCifb4yQOOBchDFVztD9v" width="690" height="294" data-dominant-color="F4F4F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1105×472 10.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @rbumm (2023-04-03 14:48 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="5" data-topic="28727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p><code>pkg_resources.extern.packaging.version.InvalidVersion: Invalid version: 'rch' (package: -)</code></p>
</blockquote>
</aside>
<p>Had you freshly installed 3D Slicer before that?</p>

---

## Post #7 by @tsehrhardt (2023-04-03 16:14 UTC)

<p>Yes I uninstalled it then reinstalled it. I still have 5.2.1 installed as well–would that matter?</p>

---

## Post #9 by @rbumm (2023-04-03 16:18 UTC)

<p>Not if you newly installed 5.2.2. <a class="mention" href="/u/lassoan">@lassoan</a> do you have any ideas?</p>

---

## Post #10 by @tsehrhardt (2023-04-03 18:37 UTC)

<p>It’s finally working now. I noticed each time I reinstalled 5.2.2 that my extensions were still there, so I uninstalled 5.2.1 and removed all the files that were left in the NA-MIC folder, followed your steps above and it worked.</p>
<p>Thanks so much for your help!</p>

---

## Post #11 by @rbumm (2023-04-03 18:40 UTC)

<p>Excellent, great job.</p>

---

## Post #12 by @lassoan (2023-04-03 21:05 UTC)

<p>Each Slicer installation is independent, so having Slicer-5.2.1 does not affect 5.2.2 at all.</p>
<p>Slicer-5.2.2 has the issue that it has an updated scipy (1.9.2) that scikit-image refuses to work with. I’ve <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/392c53e9f465dca07f0008495a569d077f5630bd">pushed a fix to the TotalSegmentator extension</a> that guides you through how to install a compatible scipy version. This is not the same scikit-learn issue that you described above but maybe they are related.</p>
<p>Please install Slicer-5.2.2 from scratch into a new folder, install the latest TotalSegmentator version (that is available from tomorrow - 2023-04-04 - 10am EST) and see if it starts up correctly. It will ask you to restart the application the first time you use it.</p>

---

## Post #13 by @tsehrhardt (2023-04-04 16:20 UTC)

<p>Thanks! I’ll try today as well to see what happens.</p>

---

## Post #14 by @rbumm (2023-04-04 17:20 UTC)

<p>Fresh installation: It now works as expected and described in your above post. Thank you.</p>

---

## Post #15 by @JulioSansone (2023-04-21 05:36 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="28727" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Each Slicer installation is independent, so having Slicer-5.2.1 does not affect 5.2.2 at all.</p>
<p>Slicer-5.2.2 has the issue that it has an updated scipy (1.9.2) that scikit-image refuses to work with. I’ve <a href="https://github.com/lassoan/SlicerTotalSegmentator/commit/392c53e9f465dca07f0008495a569d077f5630bd" rel="noopener nofollow ugc">pushed a fix to the TotalSegmentator extension </a> that guides you through how to install a compatible scipy version. This is not the same scikit-learn issue that you described above but maybe they are related.</p>
<p>Please install Slicer-5.2.2 from scratch into a new folder, install the latest TotalSegmentator version (that is available from tomorrow - 2023-04-04 - 10am EST) and see if it starts up correctly. It will ask you to restart the application the first time you use it.</p>
</blockquote>
</aside>
<p>Thanks, I will try it.</p>

---

## Post #16 by @whu (2023-04-25 01:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="28727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>u</p>
</blockquote>
</aside>
<p>I installed the Slicer 5.3.0 + TotalSegmentator Apr 24 2023 version, it still ask to restart the slicer again and again , how to solve it ?<br>
thanks.</p>

---

## Post #17 by @whu (2023-04-25 02:04 UTC)

<p>win10  + Slicer 3.3 + Total Segmentator 4.23 , still get the “This module requires installing scipy version &lt;1.9.2,”</p>
<p>thanks.</p>

---

## Post #18 by @lassoan (2023-04-25 02:50 UTC)

<p>What version number is printed if you run this command in the Python console in Slicer?</p>
<pre><code class="lang-auto">import scipy; print(scipy.__version__)
</code></pre>
<p>If it is 1.9.2 then try to restart the computer, because probable some files kept open on your computer (maybe another Slicer instance is running) and restarting your computer is guaranteed to close them. Right after restart, try running TotalSegmentator again. It will ask for Slicer restart and after that then scipy version should be 1.9.1. If it is still not 1.9.1 then restart your computer again (to close all open files) and run this command in a Windows command prompt to install scipy-1.9.1:</p>
<pre><code class="lang-auto">"%localappdata%\NA-MIC\Slicer 5.2.2\bin\PythonSlicer.exe" -m pip install --upgrade pip install scipy==1.9.1
</code></pre>
<p>Please copy the entire output of the command here.</p>

---

## Post #19 by @whu (2023-04-25 05:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="18" data-topic="28727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">"%localappdata%\NA-MIC\Slicer 5.2.2\bin\PythonSlicer.exe" -m pip install --upgrade pip install scipy==1.9.1
</code></pre>
</blockquote>
</aside>
<p>this get help, and latter it will download the pytorch 2.0 again, this was too slow.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61d9a13327c04c9a1eb9466f078498e746d73ae8.png" data-download-href="/uploads/short-url/dXCAdek1Mx2CPCFUuYbPLLG5ETu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61d9a13327c04c9a1eb9466f078498e746d73ae8.png" alt="image" data-base62-sha1="dXCAdek1Mx2CPCFUuYbPLLG5ETu" width="690" height="94" data-dominant-color="FDFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1145×157 7.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
even dead…<br>
I have installed the pytorch extension before the Totalsegmentator.</p>

---

## Post #20 by @whu (2023-04-25 07:54 UTC)

<p>After long time trying, the Totalsegmentator installed.<br>
when using the example dataset from the github code:ct_3mm.nii<br>
the error is as follows:</p>
<p>Traceback (most recent call last):<br>
File “C:\SlicerInstall\Slicer 5.3.0\bin\Python\slicer\util.py”, line 2973, in tryWithErrorDisplay<br>
yield<br>
File “C:/SlicerInstall/Slicer 5.3.0/slicer.org/Extensions-31730/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/SlicerInstall/Slicer 5.3.0/slicer.org/Extensions-31730/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 799, in process<br>
self.logProcessOutput(proc)<br>
File “C:/SlicerInstall/Slicer 5.3.0/slicer.org/Extensions-31730/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 692, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/SlicerInstall/Slicer 5.3.0/bin/…/bin\PythonSlicer.EXE’, ‘C:\SlicerInstall\Slicer 5.3.0\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/wxxx/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-25_15+50+32.050/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/wxxx/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-25_15+50+32.050/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 1.</p>
<p>the same data on the Totalsegmentator online was successful.<br>
so, what is the problem ?<br>
thanks.</p>

---

## Post #21 by @lassoan (2023-04-25 11:09 UTC)

<p>I assumed that you use the current stable version of Slicer, installed in the default location, that’s why I provided this command: <code>"%localappdata%\NA-MIC\Slicer 5.2.2\bin\PythonSlicer.exe" -m pip install --upgrade pip install scipy==1.9.1</code></p>
<p>It seems that you use a preview release installed in a custom location, so you need to use <code>C:\SlicerInstall\Slicer 5.3.0\bin\PythonSlicer.EXE</code> instead.</p>
<p>That said, it seems that your managed to install all prerequisites, because TotalSegmentator was launched. However, I don’t see any specific error messages from TotalSegmentator, only that the final error code was nonzero. To solve the problem, we need more information. Check the module GUI and the application log and copy here all the details. Since you seem to have a very slow and unreliable network connection, the problem is quite likely an inconvenience nolete download of one of the Python packages or the TotalSegmentator model weights.</p>

---

## Post #22 by @whu (2023-04-25 11:23 UTC)

<p>thanks very much.<br>
the output results is as follows:<br>
Processing started<br>
Writing input file to C:/Users/whu/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-25_19+22+09.770/total-segmentator-input.nii<br>
Creating segmentations with TotalSegmentator AI…<br>
Total Segmentator arguments: [‘-i’, ‘C:/Users/whu/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-25_19+22+09.770/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/whu/AppData/Local/Temp/Slicer/__SlicerTemp__2023-04-25_19+22+09.770/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]<br>
Traceback (most recent call last):<br>
File “C:\SlicerInstall\Slicer 5.3.0\lib\Python\Scripts\TotalSegmentator”, line 93, in <br>
main()<br>
File “C:\SlicerInstall\Slicer 5.3.0\lib\Python\Scripts\TotalSegmentator”, line 86, in main<br>
totalsegmentator(args.input, args.output, args.ml, args.nr_thr_resamp, args.nr_thr_saving,<br>
File “C:\SlicerInstall\Slicer 5.3.0\lib\Python\Lib\site-packages\totalsegmentator\python_api.py”, line 173, in totalsegmentator<br>
seg = nnUNet_predict_image(input, output, task_id, model=model, folds=folds,<br>
File “C:\SlicerInstall\Slicer 5.3.0\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 255, in nnUNet_predict_image<br>
nnUNet_predict(tmp_dir, tmp_dir, task_id, model, folds, trainer, tta)<br>
File “C:\SlicerInstall\Slicer 5.3.0\lib\Python\Lib\site-packages\totalsegmentator\nnunet.py”, line 106, in nnUNet_predict<br>
predict_from_folder(model_folder_name, dir_in, dir_out, folds, save_npz, num_threads_preprocessing,<br>
File “C:\SlicerInstall\Slicer 5.3.0\lib\Python\Lib\site-packages\nnunet\inference\predict.py”, line 616, in predict_from_folder<br>
shutil.copy(join(model, ‘plans.pkl’), output_folder)<br>
File “C:\SlicerInstall\Slicer 5.3.0\lib\Python\Lib\shutil.py”, line 427, in copy<br>
copyfile(src, dst, follow_symlinks=follow_symlinks)<br>
File “C:\SlicerInstall\Slicer 5.3.0\lib\Python\Lib\shutil.py”, line 264, in copyfile<br>
with open(src, ‘rb’) as fsrc:<br>
FileNotFoundError: [Errno 2] No such file or directory: ‘C:\Users\whu\.totalsegmentator\nnunet\results\nnUNet\3d_fullres\Task256_TotalSegmentator_3mm_1139subj\nnUNetTrainerV2_ep8000_nomirror__nnUNetPlansv2.1\plans.pkl’<br>
Exception ignored in: &lt;totalsegmentator.libs.DummyFile object at 0x000001D0B7DD8A00&gt;<br>
AttributeError: ‘DummyFile’ object has no attribute ‘flush’</p>
<p>If you use this tool please cite: <a href="https://doi.org/10.48550/arXiv.2208.05868" class="inline-onebox" rel="noopener nofollow ugc">[2208.05868] TotalSegmentator: robust segmentation of 104 anatomical structures in CT images</a></p>
<p>Using ‘fast’ option: resampling to lower resolution (3mm)<br>
Resampling…<br>
Resampled in 0.47s<br>
Predicting…</p>

---

## Post #23 by @lassoan (2023-04-25 11:46 UTC)

<aside class="quote no-group" data-username="whu" data-post="22" data-topic="28727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>FileNotFoundError: [Errno 2] No such file or directory:</p>
</blockquote>
</aside>
<p>Thank you for posting the full output. This message confirms that the issue is that download of the model weights was incomplete. I would recommend to download the weights from Zenodo manually, using your web browser, and place it in the TotalSegmentator folder in your user folder, replacing the incomplete download that is already there.</p>

---

## Post #25 by @whu (2023-04-25 12:44 UTC)

<p>I solved it. thanks <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---
