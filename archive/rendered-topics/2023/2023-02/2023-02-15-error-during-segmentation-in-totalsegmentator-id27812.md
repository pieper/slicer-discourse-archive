---
topic_id: 27812
title: "Error During Segmentation In Totalsegmentator"
date: 2023-02-15
url: https://discourse.slicer.org/t/27812
---

# Error during segmentation in TotalSegmentator

**Topic ID**: 27812
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/error-during-segmentation-in-totalsegmentator/27812

---

## Post #1 by @Luo_Dr (2023-02-15 01:08 UTC)

<p>raceback (most recent call last):<br>
File “/home/ubuntu/Slicer-5.3.0-2023-02-08-linux-amd64/bin/Python/slicer/util.py”, line 2973, in tryWithErrorDisplay<br>
yield<br>
File “/home/ubuntu/Slicer-5.3.0-2023-02-08-linux-amd64/NA-MIC/Extensions-31564/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 264, in onApplyButton<br>
self.logic.process(self.ui.inputVolumeSelector.currentNode(), self.ui.outputSegmentationSelector.currentNode(),<br>
File “/home/ubuntu/Slicer-5.3.0-2023-02-08-linux-amd64/NA-MIC/Extensions-31564/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 749, in process<br>
self.logProcessOutput(proc)<br>
File “/home/ubuntu/Slicer-5.3.0-2023-02-08-linux-amd64/NA-MIC/Extensions-31564/TotalSegmentator/lib/Slicer-5.3/qt-scripted-modules/TotalSegmentator.py”, line 656, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/home/ubuntu/Slicer-5.3.0-2023-02-08-linux-amd64/bin/…/bin/PythonSlicer’, ‘/home/ubuntu/Slicer-5.3.0-2023-02-08-linux-amd64/lib/Python/bin/TotalSegmentator’, ‘-i’, ‘/tmp/Slicer-ubuntu/__SlicerTemp__2023-02-15_08+53+07.525/total-segmentator-input.nii’, ‘-o’, ‘/tmp/Slicer-ubuntu/__SlicerTemp__2023-02-15_08+53+07.525/segmentation’, ‘–ml’, ‘–task’, ‘total’]’ returned non-zero exit status 120.</p>

---

## Post #2 by @lassoan (2023-02-15 05:24 UTC)

<p>This usually means that CUDA version is incorrect. See more details here:</p>
<aside class="quote" data-post="1" data-topic="27130">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lipteck_chew/48/13519_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/totalsegmentator-fails-with-error-120/27130">TotalSegmentator fails with error 120</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi Lassoan 
I have tried the cpu without fast option selected. It exited with status 120 after predicting part 1/5. Is there a workaround? 
Thank you. 
Regards 
Lip Teck
  </blockquote>
</aside>


---

## Post #3 by @Luo_Dr (2023-02-15 07:05 UTC)

<p>I used CUDA 11.6,it could not work.But,when i changed the version to 11.7, the results were the same.</p>

---

## Post #4 by @lassoan (2023-02-15 07:11 UTC)

<p>Both CUDA 11.6 and 11.7 work on Windows an Linux. Remove your Slicer installation and reinstall Slicer from scratch, then install the TotalSegmentator extension, following the <a href="https://github.com/lassoan/SlicerTotalSegmentator#setup">TotalSegmentaor setup instructions</a> word by word.</p>

---

## Post #5 by @Luo_Dr (2023-02-15 08:21 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> sorry,there was some trouble with me. I could not unintall 3dslicer in my computer which operation system was ubantu.I had try to remove it by using some progames,such as ‘sudo apt-get remove ’，sudo apt-get purge .But all of these i have done ended in failure.</p>

---

## Post #6 by @lassoan (2023-02-15 20:55 UTC)

<p>On Linux, Slicer is installed by simply unpacking the installation package into a folder. You can uninstall Slicer by deleting all the files in that folder.</p>

---

## Post #7 by @Luo_Dr (2023-03-02 01:48 UTC)

<p>It still could not work, <img src="https://emoji.discourse-cdn.com/twitter/hot_face.png?v=12" title=":hot_face:" class="emoji" alt=":hot_face:" loading="lazy" width="20" height="20"><br>
Can you remotely control my computer to solve this problem? I found out that this extension doesn’t work in China<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/961b6b8f75bb67cfc585850cd56f0d713fcf3dfc.png" data-download-href="/uploads/short-url/lpUmOwZRouahFlXB8NKPloIvw84.png?dl=1" title="2023-03-02 08-41-16屏幕截图" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/961b6b8f75bb67cfc585850cd56f0d713fcf3dfc.png" alt="2023-03-02 08-41-16屏幕截图" data-base62-sha1="lpUmOwZRouahFlXB8NKPloIvw84" width="677" height="500" data-dominant-color="3A182F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-03-02 08-41-16屏幕截图</span><span class="informations">732×540 62.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @muratmaga (2023-03-02 03:16 UTC)

<p>Please make sure you install the pytorch extension first and run the module prior to trying the totalsegmentator.</p>

---

## Post #9 by @lassoan (2023-03-03 06:20 UTC)

<p>Currently, PyTorch is not compatible with CUDA 12.0 (only with 11.6 and 11.7). See compatible versions <a href="https://pytorch.org/get-started/locally/">here</a>.</p>
<p>Delete the entire Slicer installation folder, unpack the Slicer install package, install a compatible CUDA version, then install pytorch manually as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested, for example, like this:</p>
<pre><code>pip_install("torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117")
</code></pre>

---

## Post #10 by @muratmaga (2023-03-03 18:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="27812">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Delete the entire Slicer installation folder, unpack the Slicer install package, install a compatible CUDA version, then install pytorch manually as <a class="mention" href="/u/muratmaga">@muratmaga</a> suggested, for example, like this:</p>
</blockquote>
</aside>
<p>Actually in my experience, with new Nvidia drivers on Ubuntu you do NOT need to install CUDA. Just run the pytorch module, and choose automatic install and see that it bring the CUDA enabled torch. In fact if the CUDA 10.2 installed in the LD_LIBRARY_PATH, that might be interfering with the correct install.</p>

---

## Post #11 by @lassoan (2023-03-03 18:40 UTC)

<p>The code snippet I provided is from the PyTorch website - <a href="https://pytorch.org/get-started/locally/">https://pytorch.org/get-started/locally/</a><br>
I still recommend to follow those instructions if anyone runs into trouble with Slicer’s automatic PyTorch installation. How you get CUDA is another matter, it depends on your operating system and drivers, so it is hard to give exact instructions.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="27812">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Actually in my experience, with new Nvidia drivers on Ubuntu you do NOT need to install CUDA</p>
</blockquote>
</aside>
<p>Agreed. On Linux, <a href="https://stackoverflow.com/a/62361395">PyTorch includes CUDA libraries</a>.</p>
<p>Even if system CUDA is installed, system CUDA is not used. System CUDA should not interfere with PyTorch’s CUDA libraries, but in some edge cases (e.g., incomplete PyTorch installation) having a system CUDA may make things more complicated. Therefore, I agree that it is better not to install system CUDA (if you don’t need it for other purposes).</p>
<hr>
<p><a class="mention" href="/u/luo_dr">@Luo_Dr</a> What is important to use NVIDIA driver on your system that supports the CUDA version compatible with PyTorch. On Linux it is <a href="https://pytorch.org/get-started/locally/">currently CUDA 11.6 or 11.7</a>. It seems that <a href="https://docs.nvidia.com/datacenter/tesla/drivers/index.html#:~:text=The%20CUDA%20driver%20provides%20an%20API%20that%20is,toolkit.%20This%20behavior%20of%20CUDA%20is%20documented%20here.">new NVIDIA drivers always work with older CUDA toolkit</a>, so it may be enough to install “new enough” driver. Since NVIDIA-SMI listed compatibility with CUDA 12.0 for you, it should be compatible with the 11.6 or 11.7 CUDA binaries that are bundled with PyTorch, so I don’t know why you are getting problems. However, this problem is most likely not related to Slicer, so you can search the web on tips for installing PyTorch on Linux.</p>

---

## Post #12 by @Luo_Dr (2023-03-04 02:00 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04e542f84c18e40d3fec09941d0f628b84579ea1.png" alt="2023-03-04 09-59-35屏幕截图" data-base62-sha1="Hj6eH5R4jKajxtOJICKLUMkntv" width="530" height="379"><br>
I had installed the pytorch extension</p>

---

## Post #13 by @muratmaga (2023-03-04 02:43 UTC)

<p>And you still get the error?</p>

---

## Post #14 by @Luo_Dr (2023-03-04 03:25 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/stuck_out_tongue_closed_eyes.png?v=12" title=":stuck_out_tongue_closed_eyes:" class="emoji" alt=":stuck_out_tongue_closed_eyes:" loading="lazy" width="20" height="20">it can work now,thank you!</p>

---
