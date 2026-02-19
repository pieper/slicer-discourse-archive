---
topic_id: 34866
title: "Totalsegmentator License Activation Issues"
date: 2024-03-13
url: https://discourse.slicer.org/t/34866
---

# TotalSegmentator License Activation Issues

**Topic ID**: 34866
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/totalsegmentator-license-activation-issues/34866

---

## Post #1 by @KewilB (2024-03-13 13:28 UTC)

<p>I recently obtained a license in order to use the heartchambers highres option. I am unable to activate my license. When I put the code sent to my email in the python console, I get a syntax error. Not sure if this is the correct place to activate the license and I cannot find any help online</p>

---

## Post #2 by @Matteboo (2024-03-13 13:40 UTC)

<p>if you use slicer 5.6, you can do it directly form the totalsegmentator extension<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e945e5dbe8fec5b70e277adfd9c33bfd6242a33.png" data-download-href="/uploads/short-url/fMeoNMsLOpccP12n5WPf56GmyMr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e945e5dbe8fec5b70e277adfd9c33bfd6242a33_2_506x500.png" alt="image" data-base62-sha1="fMeoNMsLOpccP12n5WPf56GmyMr" width="506" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e945e5dbe8fec5b70e277adfd9c33bfd6242a33_2_506x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e945e5dbe8fec5b70e277adfd9c33bfd6242a33.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e945e5dbe8fec5b70e277adfd9c33bfd6242a33.png 2x" data-dominant-color="3C3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">686×677 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Camille_Guillerminet (2025-04-01 15:43 UTC)

<p>Hello,</p>
<p>Could you tell me how to obtain a licence activation in order to segment the CT with the model tissue.</p>
<p>Tx in advance,<br>
Camille</p>

---

## Post #4 by @Matteboo (2025-04-01 16:52 UTC)

<p>For non-commercial license you can go there <a href="https://backend.totalsegmentator.com/license-academic/" class="inline-onebox" rel="noopener nofollow ugc">Streamlit</a></p>
<p>For a commercial license contact <a href="mailto:jakob.wasserthal@usb.ch">jakob.wasserthal@usb.ch</a>)</p>

---

## Post #5 by @doc-xie (2025-04-09 02:43 UTC)

<p>Hi,everyone,<br>
The error information during TotalSegmentator installing as below:<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3255, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 334, in onSetLicense<br>
self.logic.setupPythonRequirements()<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 806, in setupPythonRequirements<br>
skippedRequirements = self.pipInstallSelective(<br>
File “/Applications/Slicer.app/Contents/Extensions-32448/TotalSegmentator/lib/Slicer-5.6/qt-scripted-modules/TotalSegmentator.py”, line 708, in pipInstallSelective<br>
slicer.util.pip_install(requirement)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3887, in pip_install<br>
_executePythonModule(“pip”, args)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3848, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3814, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[’/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer’, ‘-m’, ‘pip’, ‘install’, ‘dicom2nifti’]’ returned non-zero exit status 2.<br>
What is the reason about this and how to solve the issue?<br>
Thanksm</p>

---

## Post #6 by @bulala (2025-09-29 09:09 UTC)

<p>Have you solved it? I encountered the same problem and the license setting failed.</p>
<details>
<summary>
Original message</summary>
<p>请问您解决了吗，我遇到了相同问题，license设置失败</p>
</details>

---

## Post #7 by @lassoan (2025-09-29 17:50 UTC)

<p>See more details here: <a href="https://discourse.slicer.org/t/totalsegmentator-extra-task-license-not-saved-in-slicer-6-2/35622/14" class="inline-onebox">TotalSegmentator Extra Task License Not Saved in Slicer 6.2 - #14 by bulala</a></p>
<p><a class="mention" href="/u/bulala">@bulala</a> Please give a chance for people to respond before posting the same question at multiple places. In exceptional cases, if you are desperate to get an answer as soon as possible from as many people as possible at the same time, then it might be acceptable to post to several topics at once, but then at least add a link to all other places where you asked to make people aware of this.</p>

---

## Post #8 by @doc-xie (2025-09-30 03:43 UTC)

<p>The problem has not been solved until now.</p>

---

## Post #9 by @Romulo_Alfaro (2025-10-01 00:47 UTC)

<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1GUVRDZbyZJZtoQERImdVhWro7T6MdhWy/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1GUVRDZbyZJZtoQERImdVhWro7T6MdhWy/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1GUVRDZbyZJZtoQERImdVhWro7T6MdhWy/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1GUVRDZbyZJZtoQERImdVhWro7T6MdhWy/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">TotalSegmentator.py</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><strong>First, replace the following Python file in the directory (you can make a backup copy if you wish):</strong><br>
<code>C:\Users\XXXXX\AppData\Local\slicer.org\Slicer 5.8.1\slicer.org\Extensions-33241\TotalSegmentator\lib\Slicer-5.8\qt-scripted-modules</code><br>
<strong>Then try entering your license number again.<br>
Please let me know if it worked for you.</strong></p>

---

## Post #11 by @bulala (2025-10-10 08:35 UTC)

<aside class="quote no-group quote-modified" data-username="bulala" data-post="10" data-topic="34866">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/df788c/48.png" class="avatar"> bulala:</div>
<blockquote>
<p>I have completed the replacement, but it still failed. Could you please help me figure out what the reason might be?</p>
</blockquote>
</aside>
<p>I have completed the replacement, but it still failed. Could you please help me figure out what the reason might be?</p>
<p>Failed to set TotalSegmentator license.</p>
<p>Command ‘[‘C:/Users/localadmin/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE’, ‘C:\\Users\\localadmin\\AppData\\Local\\slicer.org\\Slicer 5.8.1\\lib\\Python\\Scripts\\totalseg_set_license.exe’, ‘-l’, ‘aca_L3S919KUQIFOHA’]’ returned non-zero exit status 1.</p>
<p>Failed to set TotalSegmentator license.</p>
<p>Command ‘[‘C:/Users/localadmin/AppData/Local/slicer.org/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE’, ‘C:\\Users\\localadmin\\AppData\\Local\\slicer.org\\Slicer 5.8.1\\lib\\Python\\Scripts\\totalseg_set_license.exe’, ‘-l’, ‘aca_L3S919KUQIFOHA’]’ returned non-zero exit status 1.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03f99d0ffdc6b57c33e80aab5de5886500274125.png" data-download-href="/uploads/short-url/zae4i32XVBTDnvHQX3AFWNz6p7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03f99d0ffdc6b57c33e80aab5de5886500274125_2_690x210.png" alt="image" data-base62-sha1="zae4i32XVBTDnvHQX3AFWNz6p7" width="690" height="210" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03f99d0ffdc6b57c33e80aab5de5886500274125_2_690x210.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03f99d0ffdc6b57c33e80aab5de5886500274125_2_1035x315.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03f99d0ffdc6b57c33e80aab5de5886500274125_2_1380x420.png 2x" data-dominant-color="E6E0E0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1892×577 94.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>Could you kindly confirm whether the connection failure is network-related?</p>
<p>When I run the license tool from the command line:“C:\Users\localadmin\AppData\Local\slicer.org\Slicer 5.8.1\bin\PythonSlicer.EXE”<br>
“C:\Users\localadmin\AppData\Local\slicer.org\Slicer 5.8.1\lib\Python\Scripts\totalseg_set_license.exe” -l aca_L3S919KUQIFOHA</p>
<p>t times out while attempting to reach <code>backend.totalsegmentator.com:80</code>.</p>
<p>My security team is willing to open outbound access.<br>
Should I allow <strong>TCP 443 (HTTPS)</strong> to <code>https://backend.totalsegmentator.com/</code> for the validation to succeed?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d626638764806d9c4a3042f653c84da604eeb93.png" data-download-href="/uploads/short-url/mshMvuAtIcpqpSm3cHYQxzI1dZ1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d626638764806d9c4a3042f653c84da604eeb93.png" alt="image" data-base62-sha1="mshMvuAtIcpqpSm3cHYQxzI1dZ1" width="690" height="90" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1099×144 8.18 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2025-10-10 12:47 UTC)

<p>You need to allow network connectivity for license check and model downloads. From what you describe it seems that you need to allow connection to port 80 at <a href="http://backend.totalsegmentator.com">backend.totalsegmentator.com</a>, but you may need to enable some more for model download.</p>

---

## Post #13 by @bulala (2025-10-11 01:29 UTC)

<p>Thank you very much for your reply. May I ask if the license tab is grayed out after a successful setup? I’m using version <strong>3D Slicer 5.8.1, win11</strong>. When I enter the license, it prompts me to restart 3D Slicer. However, when I open the software again and check the license setup tab, it becomes empty again. I don’t know if the setup was successful. Please see the screenshot below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29828041646ffc49b2970dc2c15b75fb278e5cfe.png" data-download-href="/uploads/short-url/5VdaKuUwJXpTk1Z70a8Jxf81ObQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29828041646ffc49b2970dc2c15b75fb278e5cfe_2_690x381.png" alt="image" data-base62-sha1="5VdaKuUwJXpTk1Z70a8Jxf81ObQ" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29828041646ffc49b2970dc2c15b75fb278e5cfe_2_690x381.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29828041646ffc49b2970dc2c15b75fb278e5cfe_2_1035x571.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/9/29828041646ffc49b2970dc2c15b75fb278e5cfe_2_1380x762.png 2x" data-dominant-color="B5B5B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1437×794 38.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d65a0971878c09841b40d9b74c2d793375a0b28.png" data-download-href="/uploads/short-url/6tBdK5INVQMiRbMhoApNxVv4uSI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d65a0971878c09841b40d9b74c2d793375a0b28_2_690x437.png" alt="image" data-base62-sha1="6tBdK5INVQMiRbMhoApNxVv4uSI" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d65a0971878c09841b40d9b74c2d793375a0b28_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d65a0971878c09841b40d9b74c2d793375a0b28_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d65a0971878c09841b40d9b74c2d793375a0b28.png 2x" data-dominant-color="B2B1B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1188×754 48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>Name: TotalSegmentator</p>
<p>Version: 2.10.0</p>
<p>Summary: Robust segmentation of 104 classes in CT images.</p>
<p>Home-page: <a href="https://github.com/wasserth/TotalSegmentator" class="inline-onebox" rel="noopener nofollow ugc">GitHub - wasserth/TotalSegmentator: Tool for robust segmentation of &gt;100 important anatomical structures in CT and MR images</a></p>
<p>Author: Jakob Wasserthal</p>
<p>Author-email: jakob.wasserthal@usb.ch</p>
<p>License: Apache 2.0</p>
<p>Location: d:\3d_slicer\lib\python\lib\site-packages</p>
<p>Requires: dicom2nifti, nibabel, nnunetv2, numpy, pyarrow, requests, SimpleITK, torch, tqdm, xvfbwrapper</p>
<p>Required-by:</p>
<p>When I enter the license on <strong>another computer (Windows 11, 3D Slicer 5.8.1)</strong>,3d slicer log：</p>
<p>[Python] Failed to set TotalSegmentator license. [Python] Command ‘[‘C:/3D_Slicer_package/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE’, ‘C:\\3D_Slicer_package\\Slicer 5.8.1\\lib\\Python\\Scripts\\totalseg_set_license.exe’, ‘-l’, ‘aca_FU8HUMWANYM6K5’]’ returned non-zero exit status 1. [Qt] A cookie associated with a cross-site resource at <a href="http://www.nitrc.org/" rel="noopener nofollow ugc">http://www.nitrc.org/</a>   was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at <a href="https://www.chromestatus.com/feature/5088147346030592" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a>   and <a href="https://www.chromestatus.com/feature/5633521622188032" class="inline-onebox" rel="noopener nofollow ugc">Chrome Platform Status</a>  . Traceback (most recent call last):   File “C:/3D_Slicer_package/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 337, in onSetLicense     self.logic.setLicense(licenseText)   File “C:/3D_Slicer_package/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 944, in setLicense     licenseToolOutput = self.logProcessOutput(proc, returnOutput=True)   File “C:/3D_Slicer_package/Slicer 5.8.1/slicer.org/Extensions-33241/TotalSegmentator/lib/Slicer-5.8/qt-scripted-modules/TotalSegmentator.py”, line 900, in logProcessOutput     raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr) subprocess.CalledProcessError: Command ‘[‘C:/3D_Slicer_package/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE’, ‘C:\\3D_Slicer_package\\Slicer 5.8.1\\lib\\Python\\Scripts\\totalseg_set_license.exe’, ‘-l’, ‘aca_FU8HUMWANYM6K5’]’ returned non-zero exit status</p>

---

## Post #14 by @lassoan (2025-10-11 02:43 UTC)

<aside class="quote no-group" data-username="bulala" data-post="13" data-topic="34866">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/df788c/48.png" class="avatar"> bulala:</div>
<blockquote>
<p>However, when I open the software again and check the license setup tab, it becomes empty again</p>
</blockquote>
</aside>
<p>That’s the correct behavior: the license key input box should always appear empty. This is because we don’t store the license number in Slicer (it is passed to TotalSegmentator, which authenticates with the server and stores the authentication result).</p>
<p>The screenshot shows that the license is successfully authenticated:</p>
<blockquote>
<p>License has been successfully saved.<br>
License has been successfully set.</p>
</blockquote>
<p>After that you included some logs that showed an error. Maybe your firewall or proxy server interfered with the authentication. But if you have already set the license successfully once then you don’t need to worry about it, it should work well.</p>

---

## Post #15 by @bulala (2025-10-11 08:23 UTC)

<p>Thank you so much for your generous and prompt responses! I have successfully resolved the issue and can now use the software normally. I truly appreciate all your help—thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you, thank you！</p>

---
