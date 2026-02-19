---
topic_id: 45090
title: "Totalsegmentator And Monai Segmentation"
date: 2025-11-15
url: https://discourse.slicer.org/t/45090
---

# Totalsegmentator and monai segmentation

**Topic ID**: 45090
**Date**: 2025-11-15
**URL**: https://discourse.slicer.org/t/totalsegmentator-and-monai-segmentation/45090

---

## Post #1 by @alex_He (2025-11-15 06:37 UTC)

<p>Hi I just updated to ed slicer 5.10.0 but I found that it is not compatible with totalsegmentator 2 and monai. May iknow why</p>

---

## Post #2 by @Andinet_Enquobahrie (2025-11-15 12:38 UTC)

<p>I installed Slicer 5.10 and the TotalSegmentator extension module on Windows, and successfully ran whole-body segmentation. Everything appears to be working fine.</p>
<p>Could you please provide more details about the issues you are experiencing? Specifically, what operating system are you using, and what kind of failure are you encountering?</p>

---

## Post #3 by @alex_He (2025-11-18 11:02 UTC)

<p>the error is pythonslice.exe “-m”,”pip”,”install”,”pandas” return non_zero exit status 1</p>

---

## Post #4 by @MaxVs (2025-11-18 18:43 UTC)

<p>What graphic cards do you use guys? What VRAM do you have?</p>

---

## Post #5 by @alex_He (2025-11-19 07:59 UTC)

<p>Nvidia mx20, it runs 5.8.0 without any problem, just a little bit slow</p>

---

## Post #6 by @jamesobutler (2025-11-19 11:55 UTC)

<p>It appears that starting with CUDA 12.8, support of Nvidia Pascal cards such as your MX250 was dropped. You would have to make sure the install is grabbing a torch version with an earlier CUDA. It looks like latest torch 2.9.0 is still shipping a CUDA 12.6 variant.</p>
<p>However the Nvidia MX250 only has 4GB of VRAM and for totalsegmentator inference on GPU is really only supported or will work with cards that have at least 8GB of VRAM. Otherwise it will run with CPU inference.</p>

---

## Post #7 by @alex_He (2025-11-22 08:37 UTC)

<p>Hi</p>
<p>Thx for your advise, however I was not running gpu, I used cpu, slicer 5.8 was running with cpu although it is slow, but for slicer 5.10, totalsegmentater 2 not working, can totalsegmentater 2 run on cpu? I think yes, but it is not running and return with error about pandas.(I was using cpu option)</p>

---

## Post #8 by @jamesobutler (2025-11-22 17:33 UTC)

<p>I’m on Windows and using Slicer 5.10.0 I installed TotalSegmentator and ran it on the CTChest sample dataset successfully using just CPU.</p>
<ul>
<li>What operating systems are you using?</li>
<li>Did you install the TotalSegmentator extension directly from the ExtensionManager or did you install from a file that you manually downloaded?</li>
<li>Do you have a strong internet connection that does not have restrictions about what Python packages you can download?</li>
<li>Can you provide the full output displayed in the python console which includes the failure when it attempts to install the required python packages to run TotalSegmentator?</li>
</ul>

---

## Post #9 by @Romulo_Alfaro (2025-11-24 14:36 UTC)

<p>I use an NVIDIA GeForce RTX 4070 8GB, an i9-14900HX 2.20 GHz processor, and 16 GB of RAM, and DentalSegmentator isn’t working for me in the new version 5.10.0.</p>
<p>Is there any solution?</p>

---

## Post #10 by @alex_He (2025-11-26 01:49 UTC)

<p>I am using windows 11 and rtx 250 I run totalsegmentator in slicer5.8 with cpu ok but not 5.10. I installed totalsegmentator using extension manager from slicer. May be i need to reinstall 5.10 all over again.</p>

---

## Post #11 by @jamesobutler (2025-11-26 03:09 UTC)

<p>Can you provide the output when you paste the following into the Slicer python console?</p>
<pre data-code-wrap="python"><code class="lang-python">print(slicer.app.applicationFilePath())
sys_info = slicer.vtkSystemInformation()
sys_info.RunMemoryCheck()
print(sys_info.GetTotalPhysicalMemory())
slicer.util.pip_install("pandas")
</code></pre>

---

## Post #13 by @Alex_Vergara (2025-12-08 19:38 UTC)

<p>I have solved the exact same issue by doing this</p>
<pre><code class="lang-auto">slicer.util.pip_install("platformdirs")
</code></pre>

---

## Post #14 by @jamesobutler (2025-12-08 21:32 UTC)

<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> <code>platformdirs</code> is a dependency of which Python package? You observed an import error when running TotalSegmentator?</p>

---

## Post #15 by @Alex_Vergara (2025-12-09 08:26 UTC)

<aside class="quote no-group" data-username="alex_He" data-post="3" data-topic="45090" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/alex_he/48/67616_2.png" class="avatar"> alex_He:</div>
<blockquote>
<p>the error is pythonslice.exe “-m”,”pip”,”install”,”pandas” return non_zero exit status 1</p>
</blockquote>
</aside>
<p>I got this error before installing platformdirs and it runs perfectly fine after installing it.</p>
<p>I repeat, this is only valid starting with Slicer5.10. None of these was present in 5.8</p>
<p>More details about the error here <a href="https://gitlab.com/opendose/opendose3d/-/issues/118#note_2940327629" rel="noopener nofollow ugc">About Total Sementator (#118) · Issue · opendose/opendose3d</a></p>

---

## Post #16 by @Alex_Vergara (2025-12-09 14:42 UTC)

<p>No errors but just exit code 1 from totalsegmentator. plaformdirs fix the error without touching anything else, IDK why. Anyways, we have added it to the python dependencies.</p>
<p>Our latest build is running in Slicer 5.10 <a href="https://gitlab.com/opendose/opendose3d/-/merge_requests/304" rel="noopener nofollow ugc">Develop (!304) · Merge requests · OpenDose / SlicerOpenDose3D · GitLab</a></p>
<p>Tomorrow it will be available again after the module builds</p>

---
