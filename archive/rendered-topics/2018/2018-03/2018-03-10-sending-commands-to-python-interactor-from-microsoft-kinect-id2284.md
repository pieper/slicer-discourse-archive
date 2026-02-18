# Sending commands to python interactor from Microsoft kinect

**Topic ID**: 2284
**Date**: 2018-03-10
**URL**: https://discourse.slicer.org/t/sending-commands-to-python-interactor-from-microsoft-kinect/2284

---

## Post #1 by @Ahmed_Soufane (2018-03-10 22:29 UTC)

<p>I’m trying to use the sendmessage() command to send the python code to manipulate the 3-D Slicer from the Kinect c# code. Currently the code to do so is:</p>
<pre><code class="lang-auto">Process notepadProccess = Process.GetProcessesByName("NEED NAME")[0];
IntPtr notepadTextbox = FindWindowEx(notepadProccess.MainWindowHandle, IntPtr.Zero, "Edit", null);

SendMessage(notepadTextbox, WM_SETTEXT, 0, "ENTER PYTHON COMMAND");
</code></pre>
<p>What would the name be for the python interactor that would be needed to entered in the processor element to get it to send the commands to the interactor?</p>

---

## Post #2 by @lassoan (2018-03-10 23:12 UTC)

<p>I don’t think you can or should try to control one application from another like this. There are many inter-process communication techniques,  you should be able to find one that is easily accessible from both Slicer and your application. If you don’t want to build Slicer yourself then you can either use OpenIGTLink (<a href="http://www.openigtlink.org">www.openigtlink.org</a>, there are C# implementations for sending/receiving transforms, which should be more than enough) or something native Python based library.</p>

---

## Post #3 by @Ahmed_Soufane (2018-03-13 21:50 UTC)

<p>Im currently trying to set up a OpenIGTLinkIf connection between the Windows terminal/command prompt and the 3-D Slicer. The set up on the 3-d slicer runs correctly but following the instructions on the OpenIGTLinkIf page for the terminal (using the ./TrackerServer 18944 10) does not work simply throwing a ./TrackerServer is not recognized as an internal or external command, operable program or batch file. How can I fix this so the connect to the server is complete? Is there a plugin-in that has to be installed or is the command outdated now?</p>

---

## Post #4 by @lassoan (2018-03-14 16:28 UTC)

<p>You need to implement OpenIGTLink communication in your software. What programming language do you use?</p>

---

## Post #5 by @Ahmed_Soufane (2018-03-14 16:35 UTC)

<p>I am using C sharp (C#)</p>

---

## Post #6 by @lassoan (2018-03-15 04:32 UTC)

<p>You may be able to use this OpenIGTLink client:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/IGSIO/UWPOpenIGTLink">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/IGSIO/UWPOpenIGTLink" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/44b49ef26abf7f72f6c2dd2d201dd60695d067c6a0d96d7d02ce27305c33db5b/IGSIO/UWPOpenIGTLink" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/IGSIO/UWPOpenIGTLink" target="_blank" rel="noopener">GitHub - IGSIO/UWPOpenIGTLink: A client for OpenIGTLink implemented for the...</a></h3>

  <p>A client for OpenIGTLink implemented for the Universal Windows Platform - GitHub - IGSIO/UWPOpenIGTLink: A client for OpenIGTLink implemented for the Universal Windows Platform</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @zulex (2020-11-03 09:57 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, Sorry to bring this topic up again.</p>
<p>I’ve been looking thoroughly for C# solutions to connect to openIGTLink. (Mainly to use in unity and receive transforms/position/rotation).</p>
<p>I’ve been trying the following solution which is referred in most topics: <a href="https://github.com/franklinwk/OpenIGTLink-Unity" rel="noopener nofollow ugc">https://github.com/franklinwk/OpenIGTLink-Unity</a>. Unfortunately it is based on a deprecated SteamVR dependency, which doesn’t work on unity 2018.3 or higher.</p>
<p>The link you post above is written in C#. Do you advice trying to convert this to a DLL to use in unity, or do you know of any repositories having a working solution for recent unity version?</p>

---

## Post #8 by @kareem_abdelaziz (2025-10-22 21:03 UTC)

<p>Hello Iam a Senior Biomedical Engineering student Working on a similar project using kinect and I want to Integerate it with 3D slicer, have you found a solution to the Bridge problem between IGT and Kinect?</p>

---

## Post #9 by @lassoan (2025-10-25 14:36 UTC)

<p><a href="https://plustoolkit.org">Plus toolkit</a> can acquire surface scans using azure kinect, revopoint, and intel realsense surface devices and stream them into Slicer via OpenIGTLink.</p>

---
