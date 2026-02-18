# V5.10 crash on startup (Splash Screen)

**Topic ID**: 45515
**Date**: 2025-12-16
**URL**: https://discourse.slicer.org/t/v5-10-crash-on-startup-splash-screen/45515

---

## Post #1 by @GaryPlayer (2025-12-16 20:14 UTC)

<p>I have a grader that when starting slicer, gets the splash screen and then nothing.<br>
(Windows 11)</p>
<p>We uninstalled, reinstalled, upgraded to 5.10</p>
<p>Tried to reinstall in a simple directory (no spaces)</p>
<p>I tried to run the –disable-settings and the same problem occurs.  Is there a log somewhere that we can troubleshoot was the problem is?</p>

---

## Post #2 by @muratmaga (2025-12-17 01:36 UTC)

<p>Logs should be under <code>C:\Users\&lt;YourUsername&gt;\AppData\Roaming\slicer.org\</code></p>
<p>Do you see any error when you launch from the command prompt?</p>

---

## Post #3 by @GaryPlayer (2025-12-17 16:54 UTC)

<p>We got 0 errors when running from command line.</p>
<p>In the windows event log we got the following (I commented out the users name):  I’ll start running this down as I just was working with the individual.</p>
<p>Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x6911bf2c<br>
Faulting module name: vtkOpenGL-9.5.dll, version: 0.0.0.0, time stamp: 0x6911a4fc<br>
Exception code: 0xc0000005<br>
Fault offset: 0x0000000000008ca3<br>
Faulting process id: 0x70EC<br>
Faulting application start time: 0x1DC6F74D65EA22E<br>
Faulting application path: C:\Users\username\3D Slicer 5.10.0\bin\SlicerApp-real.exe<br>
Faulting module path: C:\Users\username\vtkOpenGL-9.5.dll<br>
Report Id: 0a556c76-1b13-4af5-ac66-5fed2b610368<br>
Faulting package full name:<br>
Faulting package-relative application ID:</p>

---

## Post #4 by @GaryPlayer (2025-12-17 17:41 UTC)

<p>Also we could not find any logs in the designated location, there were older logs from previous versions, but we could not find any from the 2 most recent (5.8 and 5.10) installed.  The slicer folder was empty in %AppData\Local\Temp and \Roaming\Temp</p>

---

## Post #5 by @pieper (2025-12-17 17:46 UTC)

<p>This is the wrong path and is probably the problem.  You can try removing or renaming this file.<br>
<code>: C:\Users\username\vtkOpenGL-9.5.dll</code></p>

---

## Post #6 by @GaryPlayer (2025-12-17 18:15 UTC)

<p>Thats my fault, when I edited out the username, the path got deleted.</p>
<p>Faulting application path: C:\Users\user\3D Slicer 5.10.0\bin\SlicerApp-real.exe<br>
Faulting module path: C:\Users\user\3D Slicer 5.10.0\bin\vtkOpenGL-9.5.dll</p>
<p>ANd somehow I deleted my previous post….ugh been a day</p>

---

## Post #7 by @GaryPlayer (2025-12-17 18:17 UTC)

<p>Full error since I deleted it somehow earlier</p>
<p>Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x6911bf2c</p>
<p>Faulting module name: vtkOpenGL-9.5.dll, version: 0.0.0.0, time stamp: 0x6911a4fc</p>
<p>Exception code: 0xc0000005</p>
<p>Fault offset: 0x0000000000008ca3</p>
<p>Faulting process id: 0x70EC</p>
<p>Faulting application start time: 0x1DC6F74D65EA22E</p>
<p>Faulting application path: C:\Users\user\3D Slicer 5.10.0\bin\SlicerApp-real.exe</p>
<p>Faulting module path: C:\Users\user\3D Slicer 5.10.0\bin\vtkOpenGL-9.5.dll</p>
<p>Report Id: 0a556c76-1b13-4af5-ac66-5fed2b610368</p>
<p>Faulting package full name:</p>
<p>Faulting package-relative application ID:</p>

---

## Post #8 by @muratmaga (2025-12-17 18:51 UTC)

<aside class="quote no-group" data-username="GaryPlayer" data-post="7" data-topic="45515">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/garyplayer/48/66653_2.png" class="avatar"> GaryPlayer:</div>
<blockquote>
<p>vtkOpenGL-9.5.dll, version: 0.0.0.0, time stamp: 0x6911a4fc</p>
</blockquote>
</aside>
<p>There is not much to go there, but given the error and it is nature, I would suggest checking that the GPU on this sytem is a modern GPU that Slicer supports and that the driver is the latest.</p>

---

## Post #9 by @GaryPlayer (2025-12-17 23:55 UTC)

<p>Thanks.  Unfortuantly we are strapped by IT and the computer in question is quite old and resource poor.  No GPU.</p>
<p>I’m still puzzled by the lack of log files.</p>

---

## Post #10 by @pieper (2025-12-18 00:01 UTC)

<p>We typically try to support any computer from the past 5 years or so.  Anything older than that is very hard to keep running.</p>
<p>You can try older versions that might be compatible:</p>
<p><a href="https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482" class="onebox" target="_blank" rel="noopener">https://slicer-packages.kitware.com/#collection/5f4474d0e1d8c75dfc70547e/folder/5f4474d0e1d8c75dfc705482</a></p>

---
