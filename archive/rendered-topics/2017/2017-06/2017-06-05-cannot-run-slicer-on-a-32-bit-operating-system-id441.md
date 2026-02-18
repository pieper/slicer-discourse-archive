# Cannot run Slicer on a 32-bit operating system

**Topic ID**: 441
**Date**: 2017-06-05
**URL**: https://discourse.slicer.org/t/cannot-run-slicer-on-a-32-bit-operating-system/441

---

## Post #1 by @LilyLJ (2017-06-05 02:26 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.6.2 (also tried 4.5.0-1, same behavior)<br>
Expected behavior: Installation of Slicer, and run it by double clicking Slicer.exe<br>
Actual behavior: Installation seems done, but nothing happens when I double click on Slicer.exe</p>
<p>Hi guys,<br>
This is the first time I’m trying to use 3D Slicer. I’m stuck at the installation step. Could you please give me a hand?<br>
Thanks a lot !<br>
Lily</p>

---

## Post #2 by @lassoan (2017-06-05 02:49 UTC)

<p>See instructions for solving this issue here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Troubleshooting#Debugging_Slicer_application_startup_issues</a></p>
<p>Write here what was the solution. If the problem persists then provide additional information as described.</p>

---

## Post #3 by @LilyLJ (2017-06-05 19:02 UTC)

<p>Hi,</p>
<p>Thank you very much for your answer.</p>
<p>This was my mistake actually, I installed and tried to run versions for Windows 64 bits, whereas I was using a 32 bits. Sorry about that. I could run the Slicer-4.3.0-win-i386.</p>
<p>I would like to show some results at a presentation. I will have my work prepared on an external hard drive, but I cannot know if the system there will be a 32 or 64 bits. Any chance the i386 version can also run on a 64 bits?</p>

---

## Post #4 by @lassoan (2017-06-06 00:14 UTC)

<p>We stopped providing 32-bit Slicer packages several years ago, because memory space of 32-bit applications is very small and so you can only manipulate relatively small data sets and you can perform very limited processing.</p>
<p>You can still build a 32-bit Slicer - follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions">these build instructions</a>, but I would strongly recommend to switch to a 64-bit operating system.</p>

---

## Post #5 by @timeanddoctor (2018-03-18 00:08 UTC)

<p>For some reasons, the navigation device only support 32, I must have a 32 bits slicer running on my win7*32.<br>
However, I installed a 4.3 slicer successfully but there was no extension. I just went the IGTslicer extension, so what can I do? Can I load it just as many modules not a extension.<br>
I also try to build one followwing these build instructions mentioned above, but get many fails because<br>
I am a newable to code. I also think if there is a building-video could be very usefull to one like me.</p>

---

## Post #6 by @lassoan (2018-03-18 01:22 UTC)

<p>I would suggest to use a 32-bit release of Plus toolkit on the navigation device. Run Slicer on another computer, running an up-to-date operating system. Plus can stream navigation data to Slicer using OpenIGTLink.</p>

---
