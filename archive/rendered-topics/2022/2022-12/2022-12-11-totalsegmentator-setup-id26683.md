# TotalSegmentator setup

**Topic ID**: 26683
**Date**: 2022-12-11
**URL**: https://discourse.slicer.org/t/totalsegmentator-setup/26683

---

## Post #1 by @Chuns_SS (2022-12-11 13:53 UTC)

<p>I keep getting errors trying to run totalsegmenter. I suspect it has to do with pyTorch not being installed properly on my system. Linux Ubuntu 22.04. To install pyTorch seems a bit tricky and most sites recommend using anaconda. Any advice? error message included:<br>
Traceback (most recent call last):<br>
File “/home/samuel/Slicer-5.2.1-linux-amd64/bin/Python/slicer/util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “/home/samuel/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 248, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “/home/samuel/Slicer-5.2.1-linux-amd64/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 531, in setupPythonRequirements<br>
slicer.util.pip_install(totalSegmentatorPackage + " --no-deps" + (" --upgrade" if upgrade else “”))<br>
File “/home/samuel/Slicer-5.2.1-linux-amd64/bin/Python/slicer/util.py”, line 3571, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “/home/samuel/Slicer-5.2.1-linux-amd64/bin/Python/slicer/util.py”, line 3533, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “/home/samuel/Slicer-5.2.1-linux-amd64/bin/Python/slicer/util.py”, line 3502, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/home/samuel/Slicer-5.2.1-linux-amd64/bin/…/bin/PythonSlicer’, ‘-m’, ‘pip’, ‘install’, ‘git+https://github.com/wasserth/TotalSegmentator.git’, ‘–no-deps’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @rbumm (2022-12-11 14:31 UTC)

<p>There is a new 3D Slicer extension available for installing and running TotalSegmentator within 3D Slicer.<br>
Highly recommended.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac1a2858154e1aee0d1d7b11a34e1a7c309f3259.png" data-download-href="/uploads/short-url/oyuan7egF2iUEnGDHKDvASw7CtP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac1a2858154e1aee0d1d7b11a34e1a7c309f3259_2_316x500.png" alt="image" data-base62-sha1="oyuan7egF2iUEnGDHKDvASw7CtP" width="316" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac1a2858154e1aee0d1d7b11a34e1a7c309f3259_2_316x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac1a2858154e1aee0d1d7b11a34e1a7c309f3259.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac1a2858154e1aee0d1d7b11a34e1a7c309f3259.png 2x" data-dominant-color="D8DEDA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">349×552 75.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Sources on GitHub: <a href="https://github.com/lassoan/SlicerTotalSegmentator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerTotalSegmentator: Fully automatic total body segmentation in 3D Slicer using "TotalSegmentator" AI model</a></p>
<p>You will also need to install PyTorch by using the PyTorch extension:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce52cf236f8bbc41891c1ea4ee6dd22ed57bbbd2.png" alt="image" data-base62-sha1="trdM9uYzj1zVIyAuvneeZO6bs1s" width="244" height="496"></p>

---

## Post #3 by @Chuns_SS (2022-12-14 01:41 UTC)

<p>Thank-you, I installed newer version and also GIT which I overlooked previously. Now running fine. Is there a version for the Mac OS platform?</p>

---

## Post #4 by @pieper (2022-12-14 02:50 UTC)

<p>Yes, the TotalSegmentator extenstion works on a mac (tested on an M2 mac book air) but the GPU version is not available and I didn’t see an option to run the high-res version (but the faster low-res version did work).</p>

---

## Post #5 by @Chuns_SS (2022-12-14 05:11 UTC)

<p>Thanks I updated my mac version and was able to load the extension but as you said I couldn’t get the hi res version to compile.</p>

---

## Post #6 by @lassoan (2022-12-14 06:46 UTC)

<p>The full-resolution model works fine on CPU (at least on Windows). Tested on two computers. Even completes successfully on an 8th-generation Intel i5 with 8GB RAM (it takes 30-40 minutes, which is long, but still much shorter than doing the segmentation manually).</p>
<p>What error did you get on macOS when you attempted to segment with “fast” mode disabled?</p>

---

## Post #7 by @philippepellerin (2022-12-14 12:44 UTC)

<p>I does not see the totalsegmentation plug-in in the list when I open the extension manager.I am working with3D slicer 5-1-0-2022-11-12</p>

---

## Post #8 by @rbumm (2022-12-14 13:15 UTC)

<p>Please update Slicer to the recent stable version 5.2.1.</p>
<p>You should find the extension here after installation:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/205568a7e0271a56a26ef049267b99890843f33d.png" alt="image" data-base62-sha1="4C2gwLGhDvC5A1O6QSpZh11KWkZ" width="445" height="103"></p>

---

## Post #9 by @lassoan (2022-12-14 13:18 UTC)

<aside class="quote no-group" data-username="philippepellerin" data-post="7" data-topic="26683" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>I does not see the totalsegmentation plug-in in the list when I open the extension manager.I am working with3D slicer 5-1-0-2022-11-12</p>
</blockquote>
</aside>
<p>This is a new extension. It is not available in older Slicer Preview Releases.</p>
<p>I would recommend to use the latest Slicer Stable Release (currently Slicer-5.2.1), as it allows you to easily update the extensions as we make improvements/fixes.</p>

---

## Post #10 by @philippepellerin (2022-12-14 14:36 UTC)

<p>Thank you so much, I missed the latest release! I will do that.<br>
Very best regards</p>
<p>Pr Philippe Pellerin.<br>
Former coordinator of the French National Reference Center for rare craniofacial malformations.<br>
Departement of Plastic Surgery.<br>
Lille University Hospital.<br>
France</p>

---

## Post #11 by @philippepellerin (2022-12-14 16:50 UTC)

<p>I have downloaded Slicer 5-3 and the total segmentation extension, tried it at once: great result, I can’t believe how you did that but this is for me as a miracle!<br>
Bravo and thanks again for the incredible tool that you provided.<br>
Happy X’mas</p>

---

## Post #12 by @lassoan (2022-12-14 20:09 UTC)

<p>Thanks for the kind words. TotalSegmentator is indeed amazing, and it is still in early stage. It is expected to become much better - more accurate and more comprehensive. Credits go to DKFZ for releasing this AI segmentation tool (including training method and data sets) for public use without restrictions (see <a href="https://github.com/wasserth/TotalSegmentator" class="inline-onebox">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of 104 important anatomical structures in CT images</a> for details).</p>

---

## Post #13 by @philippepellerin (2023-01-18 14:51 UTC)

<p>Dear Andras, I am trying to work with Bale’s team to implement face segmentation in Totalsegmentator. I am asked to send the CT data as Nifti files, I am OK with this, but they ask as well a Nifti or NRRD for the segmentation. I can’t find a way to export the segmentation this way. Is it one that I could use?<br>
Thanks for your time and help.</p>

---

## Post #14 by @rbumm (2023-01-18 15:15 UTC)

<aside class="quote no-group quote-modified" data-username="philippepellerin" data-post="13" data-topic="26683">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/philippepellerin/48/16062_2.png" class="avatar"> philippepellerin:</div>
<blockquote>
<p>way to export the segmentation?</p>
</blockquote>
</aside>
<p>This is quite hidden: You can find it in “Segmentations”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc122f9647f131b11e34bd63fa20df7b2dbe39eb.png" data-download-href="/uploads/short-url/zXVhHZ4koHQBc8KTj2KyiM1VbwT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc122f9647f131b11e34bd63fa20df7b2dbe39eb_2_620x500.png" alt="image" data-base62-sha1="zXVhHZ4koHQBc8KTj2KyiM1VbwT" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fc122f9647f131b11e34bd63fa20df7b2dbe39eb_2_620x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc122f9647f131b11e34bd63fa20df7b2dbe39eb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc122f9647f131b11e34bd63fa20df7b2dbe39eb.png 2x" data-dominant-color="BCBABA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">815×657 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @philippepellerin (2023-01-18 15:52 UTC)

<p>Super, thank you, in the meantime, Jakob has been happy with the .nrrb file in the saved bundle. But this way, I could select what he is specifically interested in.<br>
Thanks a lot for your fast answer.<br>
All the best.</p>

---

## Post #16 by @linda_varghese (2023-06-04 17:39 UTC)

<p>Hi, I am trying to run TotalSegmentor,but its showing error.pyTorch has already been installed on my system Windows 64 bit.<br>
Traceback (most recent call last):<br>
File “C:\Users\lvarghese\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/lvarghese/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/lvarghese/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 799, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/lvarghese/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 692, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/lvarghese/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\lvarghese\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/lvarghese/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-04_19+38+07.977/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/lvarghese/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-04_19+38+07.977/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>I am not that good with coding,can someone help me where I am doing wrong,is there anyother extensions for support I have to install?</p>

---

## Post #17 by @lassoan (2023-06-04 19:29 UTC)

<p>Please go to Pytorch Utils module and copy here the displayed version of Pytorch and cuda.</p>

---

## Post #18 by @linda_varghese (2023-06-04 20:21 UTC)

<p>I had installed the latest version.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce4cd5ea1d52e0a64385a4334af5bbcd1ff48ca.png" data-download-href="/uploads/short-url/A5cwNHMIPcPelmzbm7i54ba3OdQ.png?dl=1" title="Screenshot (5)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce4cd5ea1d52e0a64385a4334af5bbcd1ff48ca_2_690x336.png" alt="Screenshot (5)" data-base62-sha1="A5cwNHMIPcPelmzbm7i54ba3OdQ" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce4cd5ea1d52e0a64385a4334af5bbcd1ff48ca_2_690x336.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce4cd5ea1d52e0a64385a4334af5bbcd1ff48ca_2_1035x504.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce4cd5ea1d52e0a64385a4334af5bbcd1ff48ca_2_1380x672.png 2x" data-dominant-color="F2F0EE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (5)</span><span class="informations">1892×922 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #19 by @lassoan (2023-06-04 20:26 UTC)

<p>Please go to Pytorch Utils module and check what are the Pytorch and cuda versions displayed there.</p>

---

## Post #20 by @linda_varghese (2023-06-04 20:29 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1a0f25439b18d11eef8d32019484e1971cf0e0b.png" data-download-href="/uploads/short-url/wc0fXeOtcqCm0REtjtzJ6JPbKBB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1a0f25439b18d11eef8d32019484e1971cf0e0b.png" alt="image" data-base62-sha1="wc0fXeOtcqCm0REtjtzJ6JPbKBB" width="690" height="248" data-dominant-color="F8F8F8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">918×330 4.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is what it showing</p>

---

## Post #21 by @linda_varghese (2023-06-04 20:31 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f886bb1ed1713e4136f279d6d7339f4b42fef38.png" data-download-href="/uploads/short-url/2dprp8AzpyDLYKphbEk7GojW5bq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f886bb1ed1713e4136f279d6d7339f4b42fef38.png" alt="image" data-base62-sha1="2dprp8AzpyDLYKphbEk7GojW5bq" width="690" height="454" data-dominant-color="F3F3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">733×483 8.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #22 by @lassoan (2023-06-04 23:26 UTC)

<p>Thank you, it seems that by default an old version of pytorch got installed. We have observed this on some computers, but could not figure out why it happens (why not the latest version is installed). Thr good news that the fix is easy:</p>
<ul>
<li>uninstall pytorch (you can use Pytorch Utils module for this)</li>
<li>restart Slicer</li>
<li>install Pytorch-1.12 - by typing this into the Python console in Slicer: <code>pip_install("torch&gt;=1.12")</code>
</li>
</ul>

---

## Post #23 by @linda_varghese (2023-06-13 09:11 UTC)

<p>Thanks for the suggestion, now it worked.But after this updating am getting an error message before starting the slicer. What would be the reason for that?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/680c3004a1109c2b35d7e8c394ce1d3536428aa9.png" alt="image" data-base62-sha1="eQrLEN6c7tKNbBp2FoPoRi4Gke5" width="637" height="349"></p>

---

## Post #24 by @linda_varghese (2023-06-20 08:09 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="22" data-topic="26683">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>pip_install(“torch&gt;=1.12”)</p>
</blockquote>
</aside>
<p>Hi Team, am facing the same error again while running Total Segmentor module, even after installing the 1.12 version pyTorch.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7ccf892f1635c8ecf152ce4b8b548d087c6dcce4.png" alt="image" data-base62-sha1="hO7QH0acE9cKtVyJf5rHVSyBrz6" width="682" height="394"></p>

---

## Post #25 by @lassoan (2023-06-20 11:25 UTC)

<p>Could you copy here the entire message In the details section of the error popup?</p>

---

## Post #26 by @linda_varghese (2023-06-23 07:33 UTC)

<p>Traceback (most recent call last):<br>
File “C:\Users\lvarghese\AppData\Local\NA-MIC\Slicer 5.2.2\bin\Python\slicer\util.py”, line 2967, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/lvarghese/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “C:/Users/lvarghese/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 770, in process<br>
self.logProcessOutput(proc)<br>
File “C:/Users/lvarghese/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 663, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/lvarghese/AppData/Local/NA-MIC/Slicer 5.2.2/bin/…/bin\PythonSlicer.EXE’, ‘C:\Users\lvarghese\AppData\Local\NA-MIC\Slicer 5.2.2\lib\Python\Scripts\TotalSegmentator’, ‘-i’, ‘C:/Users/lvarghese/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-23_09+32+41.573/total-segmentator-input.nii’, ‘-o’, ‘C:/Users/lvarghese/AppData/Local/Temp/Slicer/__SlicerTemp__2023-06-23_09+32+41.573/segmentation’, ‘–ml’, ‘–task’, ‘total’, ‘–fast’]’ returned non-zero exit status 120.</p>
<p>It had worked earlier ,now i was trying to work on Monai and suddelnly this is not working.</p>

---

## Post #27 by @lassoan (2023-06-23 11:27 UTC)

<p>Maybe try to install Slicer from scratch into a new folder and install totalsegmentator but not install monai.</p>

---

## Post #28 by @linda_varghese (2023-06-23 12:14 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96f662ad6c57983980da84a8a9b9953bdee375fc.png" alt="image" data-base62-sha1="lxtuW4sz0DeO83pmsBGxJlqQXwM" width="686" height="269"><br>
I had re installed slicer and didn’t install MONAI and again the total segmentor showing same error.</p>

---
