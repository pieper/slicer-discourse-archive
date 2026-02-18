# Problems with modules installation

**Topic ID**: 11036
**Date**: 2020-04-08
**URL**: https://discourse.slicer.org/t/problems-with-modules-installation/11036

---

## Post #1 by @doc-xie (2020-04-08 02:12 UTC)

<p>The 3D Slicer of preview release (4.11.0,revision28931) can be installed successfully in my Macbook pro, but after some modules were downloaded from “Extentions manager” and the software was reopenned again, the modules can not be shown in the menu. The error informations are bellows:<br>
QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>QPixmap::scaled: Pixmap is a null pixmap</p>
<p>Remote debugging server started successfully. Try pointing a Chromium-based browser to <a href="http://127.0.0.1:1337" rel="nofollow noopener">http://127.0.0.1:1337</a></p>
<p>Best wishes,<br>
Xie</p>

---

## Post #2 by @pieper (2020-04-08 14:28 UTC)

<p>Hi <a class="mention" href="/u/doc-xie">@doc-xie</a> - I don’t see anything in the log there to indicate what’s going on.  Could you try the following:</p>
<ul>
<li>
<p>look in the logs from past runs (they are in the Help -&gt; report a bug menu)</p>
</li>
<li>
<p>try deleting all your slicer files and starting fresh, installing one extension at a time.  Let us know if you can isolate the specific extension or combination that breaks things.</p>
</li>
</ul>
<p>Best,<br>
Steve</p>

---

## Post #3 by @lassoan (2020-04-08 22:00 UTC)

<p><a class="mention" href="/u/doc-xie">@doc-xie</a> don’t forget to delete (or temporary move elsewhere) the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ApplicationSettings#Settings_file_location">application settings (.ini files)</a>.</p>

---

## Post #4 by @doc-xie (2020-04-09 02:47 UTC)

<p>Hi Steve,<br>
The log message shows as following:</p>
<p>[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2020-04-09 10:37:06<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.0-2020-04-06 (revision 28931 / 526e73f) macosx-amd64 - installed release<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Mac OS X / 10.15.4 / 19E266 - 64-bit<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 16384 MB physical, 2048 MB virtual<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i7-8850H CPU @ 2.60GHz, 6 cores, 12 logical processors<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.10.0, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: yes<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: /Applications/Slicer4_11.app/Contents/MacOS<br>
[DEBUG][Qt] 09.04.2020 10:37:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 09.04.2020 10:37:09 [Python] (/Applications/Slicer4_11.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 09.04.2020 10:37:10 [Python] (/Applications/Slicer4_11.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 09.04.2020 10:37:10 [Python] (/Applications/Slicer4_11.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 09.04.2020 10:37:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 09.04.2020 10:37:15 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[INFO][VTK] 09.04.2020 10:37:26 [vtkMRMLVolumeArchetypeStorageNode (0x7ffed4104d40)] (/Volumes/Dashboards/Preview/Slicer-0/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:471) - Loaded volume from file: /Users/dr.xie/Desktop/data for training.nrrd. Dimensions: 512x512x247. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 09.04.2020 10:37:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “/Users/dr.xie/Desktop/data for training.nrrd” “[0.89s]”<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QPixmap::scaled: Pixmap is a null pixmap<br>
[WARNING][Qt] 09.04.2020 10:37:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Remote debugging server started successfully. Try pointing a Chromium-based browser to <a href="http://127.0.0.1:1337" rel="noopener nofollow ugc">http://127.0.0.1:1337</a><br>
[CRITICAL][Qt] 09.04.2020 10:38:14 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “{81c54703-cc56-4ddd-8bd1-da2840f4f0a5}: 5: Operation canceled”</p>
<p>The modules which I installed can be found in the Extentions manager, but they are not shown in the modules menu.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78dd4bed1e65f44ccb94c16435bb69d84ed26e88.png" data-download-href="/uploads/short-url/hfdqaXbYDKqBqOnN67M3VM7zedi.png?dl=1" title="Screen Shot 2020-04-09 at 10.42.29 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78dd4bed1e65f44ccb94c16435bb69d84ed26e88_2_690x418.png" alt="Screen Shot 2020-04-09 at 10.42.29 AM" data-base62-sha1="hfdqaXbYDKqBqOnN67M3VM7zedi" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78dd4bed1e65f44ccb94c16435bb69d84ed26e88_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78dd4bed1e65f44ccb94c16435bb69d84ed26e88_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/78dd4bed1e65f44ccb94c16435bb69d84ed26e88_2_1380x836.png 2x" data-dominant-color="E8E9F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-04-09 at 10.42.29 AM</span><span class="informations">3350×2032 674 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have the stable and the preview release versions in my computer. Do you mean I should uninstall all the files about Slicer?</p>
<p>Best wishes,<br>
Xie</p>

---

## Post #5 by @lassoan (2020-04-09 03:08 UTC)

<aside class="quote no-group" data-username="doc-xie" data-post="4" data-topic="11036">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/c77e96/48.png" class="avatar"> doc-xie:</div>
<blockquote>
<p>Additional module paths …: (none)</p>
</blockquote>
</aside>
<p>This indicates that the extensions have not been actually installed. Have you tried to uninstall and reinstall the modules? Make sure you wait for the “Restart” button to be enabled and click that (do not click the “Close” button if you want to install extensions).</p>

---

## Post #6 by @doc-xie (2020-04-09 06:16 UTC)

<p>Hi Lasson,<br>
The issue have been solved after the modules were uninstalled and reinstalled. I think the reason is the modules have not been downloaded and installed completely.<br>
Best wishes,<br>
Xie</p>

---

## Post #7 by @pieper (2020-04-09 20:37 UTC)

<p>Hi <a class="mention" href="/u/doc-xie">@doc-xie</a> - you might try this command on the mac on the nightly builds:</p>
<p><code>codesign --force --deep -s - /Applications/Slicer.app/Contents/MacOS/Slicer</code></p>
<p>It seems to really speed up application startup time and extension manager dialog operations.</p>
<p>More info here:</p>
<aside class="quote quote-modified" data-post="37" data-topic="7881">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/extension-wizard-file-open-dialogs-hang-ui-for-several-seconds/7881/37">Extension Wizard - file open dialogs hang UI for several seconds</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Andras and I did some more digging into this issue. 
Logged tccd using this command: 

log stream --debug --predicate ‘subsystem == “com.apple.TCC”’ 

During startup, there is a 50sec window where tccd is presumably checking the application signature: 

2019-11-13 12:41:30.733517-0500 0x7694f    Info        0xa9379              199    0    tccd: [com.apple.TCC:access] adhoc signed StaticCode :0x7fa6d33950e0 START 
2019-11-13 12:42:23.224389-0500 0x7694f    Info        0xa9379              199   …
  </blockquote>
</aside>


---

## Post #8 by @doc-xie (2020-04-11 02:32 UTC)

<p>Hi Steve,<br>
The modules in Slicer are working normally now. So I think the modules have not been installed completely. By the way, where should the command you give me to run?<br>
In terminal: No such files or dictionary;<br>
In Python interactor window in Slicer: invalid syntax.<br>
Best wishes,<br>
Xie</p>

---

## Post #9 by @pieper (2020-04-11 15:43 UTC)

<p>Hi Xie -</p>
<p>Yes, that <code>codesign</code> command should be run in a terminal.  Since it says <code>No such file</code> it means you need to install it.  I didn’t find the specific instructions, but I believe it comes if you install Xcode, which you can get from the Apple App Store.</p>
<p>Best,<br>
Steve</p>

---

## Post #10 by @doc-xie (2020-04-12 05:14 UTC)

<p>Hi Steve,<br>
Actually Xcode had been installed in my computer several months ago. But after the modules were uninstalled and reinstalled, they were shown in the Modules menu normally and works well for me.<br>
Thanks,<br>
Best wishes,<br>
Xie</p>

---
