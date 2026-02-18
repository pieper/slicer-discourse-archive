# Error messages indicating 4 missing files

**Topic ID**: 14839
**Date**: 2020-12-02
**URL**: https://discourse.slicer.org/t/error-messages-indicating-4-missing-files/14839

---

## Post #1 by @Poul_Andersson (2020-12-02 02:00 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc7dab40c7cb1c55d336400579ad88e7d31981bf.jpeg" alt="Slicer_error2" data-base62-sha1="A1Dz9KqNEW6HKV5xgJPdZRyQHyT" width="423" height="183"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1b7a67e43b20f5df92f46825adc55a4d3e3ab52.jpeg" alt="Slicer_error3" data-base62-sha1="wcMTNngKF9qUoPfsZxoGnJI12XE" width="422" height="183"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e32e379640a5154e5e7ba73c796af43569bf85f9.jpeg" alt="Slicer_error4" data-base62-sha1="wpJp8VVIalgRGYTxXSCV2O33dVv" width="435" height="185"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3eb1e090204eac26b5468d51f6c8b1c8923f208.jpeg" alt="Slicer_error1" data-base62-sha1="ueItVVcqiR4BdERFkzerp97LUDu" width="425" height="170"></p>
<p>I have installed the module for the jupyter kernel to use 3DSlicer in notebooks but am now facing two problems: firstly, the 3DSlicer app keeps restarting automatically after proper exit; and secondly, I get the above error messages indicating that some files are missing: CTKWidgets.dll, CTKVisualizationVTCore.dll, qMRMLWidgets.dll, and CTKQtTesting.dll. Suggestions would be much appreciated. Best, Poul</p>

---

## Post #2 by @lassoan (2020-12-02 02:03 UTC)

<p>I could not reproduce this issue.</p>
<p>What Slicer version do you use?<br>
How did you start Slicer?<br>
What Slicer version do you use?<br>
What operating system version do you use?<br>
What extensions have you installed?<br>
Have you added any additional module paths manually?</p>

---

## Post #3 by @Poul_Andersson (2020-12-02 09:24 UTC)

<p>Hi Andras,</p>
<p>I believe that the problem is associated with the Jupyter Notebook extension/module which I added to Slicer. Let me describe the auto start problem in some detail.</p>
<p>The automatic restart of Slicer does not happen when I start my PC. Nor does it happen when I start Slicer from Windows start menu and close it again.</p>
<p>When I use Slicer from a Jupyter Notebook in Anaconda (attached), the Slicer function in the Noteboo works perfectly, and at the same time the Slicer app starts with the Welcome screen as module. After closing this Slicer instance (subsequent to closing the Jupyter Notebook and Anaconda), Slicer restarts automatically some 10-15 seconds later. This pattern repeats until the PC is restarted.</p>
<p>I noticed that the Slicer icon in the Windows Task bar shows the following contextual menu:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6b3a6b493ae9927fa8014d04091742ee2024e6c.png" alt="image001.png" data-base62-sha1="slNrhzjv3eKzGXL22EZRROXJ7Hu" width="284" height="149"></p>
<p>When I tried to activate “SlicerApp-real”, I received the missing files error messages previously sent.</p>
<p>To your questions:</p>
<p>Latest Slicer download from your home page 4.11.20****</p>
<p>Slicer start: see description above</p>
<p>Windows 10 Pro 10.0.19041</p>
<p>Only new extension added to any program since start of the problem: SlicerJupyter module.</p>
<p>No new paths added to any program since start of the problem</p>
<p>Best regards,</p>
<p>Poul</p>
<p>(Attachment Poul_3DSlicer1.ipynb is missing)</p>

---

## Post #4 by @lassoan (2020-12-03 06:24 UTC)

<aside class="quote no-group" data-username="Poul_Andersson" data-post="3" data-topic="14839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/poul_andersson/48/8979_2.png" class="avatar"> Poul_Andersson:</div>
<blockquote>
<p>After closing this Slicer instance (subsequent to closing the Jupyter Notebook and Anaconda), Slicer restarts automatically some 10-15 seconds later. This pattern repeats until the PC is restarted.</p>
</blockquote>
</aside>
<p>This is the correct behavior. Slicer is a Jupyter notebook kernel. Kernels are managed by the Jupyter notebook server. If the kernel dies (e.g., because you close the application) then the Jupyter notebook server detects this an automatically restarts the kernel (the application). You can manage (start/stop/restart) kernels in the Jupyter server GUI in your browser.</p>
<aside class="quote no-group" data-username="Poul_Andersson" data-post="3" data-topic="14839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/poul_andersson/48/8979_2.png" class="avatar"> Poul_Andersson:</div>
<blockquote>
<p>When I tried to activate “SlicerApp-real”, I received the missing files error messages previously sent.</p>
</blockquote>
</aside>
<p>SlicerApp-real must be launched using the Slicer.exe launcher, which sets up all the required paths. Otherwise you will end up getting error messages that DLLs are not found - these are the messages that you show on your screenshots above. Why did you try to launch SlicerApp-real?</p>
<p>So, as far as I can tell, everything works as expected.</p>

---

## Post #5 by @Poul_Andersson (2020-12-03 10:33 UTC)

<p>Hi Andras,</p>
<p>Thank you for your explanation. And Slicer kernel shutdown from the Jupyter GUI cured my problem.</p>
<p>Best regards,</p>
<p>Poul</p>

---
