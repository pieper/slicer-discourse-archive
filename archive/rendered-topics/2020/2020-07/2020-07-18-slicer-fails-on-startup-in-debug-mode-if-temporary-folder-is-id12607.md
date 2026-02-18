# Slicer fails on startup in debug mode if temporary folder is set to empty

**Topic ID**: 12607
**Date**: 2020-07-18
**URL**: https://discourse.slicer.org/t/slicer-fails-on-startup-in-debug-mode-if-temporary-folder-is-set-to-empty/12607

---

## Post #1 by @sogo (2020-07-18 00:05 UTC)

<p>I’m working on an loadable application where I’m changing the temporary directory path to work in my own application directory. I’m changing the directory path by using qSlicerCoreApplication::application-&gt;setTemporaryPath(d-&gt;folderPath) and I’m using it to create Dicom database in that directory. The “d-&gt;folderPath” variable is the temporary directory selected by user using QFileDialog.<br>
It has been working fine for sometime but recently I got an error and slicer fails to load at startup. The error is:</p>
<blockquote>
<p>“[100%] Built target qSlicerDAFSModuleGenericCxxTests<br>
ASSERT: “!d-&gt;TempDirectory.isEmpty()” in file /home/simtiaz/Myproject/Slicer-build/slicersources-src/Base/QTCLI/qSlicerCLIModule.cxx, line 78”.</p>
</blockquote>
<p>I’m not sure why this error is generated and why slicer crashes on startup but it happens randomly after some amount of tries. I think potential issue is sometimes slicer exits abnormally and when it starts, it can not find temporary directory path. I have to rebuild slicer to fix this issue. Is changing temporary path causing this issue?</p>

---

## Post #2 by @lassoan (2020-07-18 02:08 UTC)

<p><code>Q_ASSERT(!d-&gt;TempDirectory.isEmpty());</code> is just a debug-mode assertion, warning you that the temporary folder is not set (or set to an invalid empty string) by the time the module is being set up. Assertions supposed to work like this - crashing the application in debug mode to make sure developer notice them. In general we prefer replacing them with logging a warning message, so if you want to change this then send us a pull request.</p>
<p>Nevertheless, you need to fix the root cause of the error, which is most likely that you set the temp folder to an empty (or maybe invalid?) folder somewhere. Since you cannot achieve anything with setting the temporary folder to a particular location (you can only break things by not setting it to a writeable folder), I would suggest not to mess with it. Leave it at the default.</p>
<p>If you want to create the DICOM database somewhere else then just create it somewhere else by specifying the desired location: <code>DICOMUtils.TemporaryDICOMDatabase(mytempfolder)</code>. But the fact that you actually care about where this folder resides indicates that is actually not a temporary database, so probably you should just use the application’s default DICOM database.</p>

---

## Post #3 by @sogo (2020-07-18 04:59 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@Lassoan</a>,<br>
Thanks for your response, I looked into DICOMUtils.py and see there is option to set absolute path as tempDatabaseDir. Before I was just giving directory name and changing temporary directory path. I should have checked this option earlier as this way I don’t need to change slicer’s default temporary path. Let me test this and see if I run into any issues.<br>
I’m not sure if this should be warning as it could affect other modules or if any invalid path set or no path set as per your reasoning, but is there any way to find root cause to it. I did try setting temporary path using slicer.app.temporaryPath= “Path” in  .slicerrc.py and re-run slicer but issue persisted.</p>
<p>Thanks for the support.<br>
Regards</p>

---

## Post #4 by @lassoan (2020-07-18 15:05 UTC)

<p>I would recommend to set a valid temporary path in the GUI (menu: Edit / Application settings / Modules / Temporary directory) and then don’t modify it from scripts.</p>

---

## Post #5 by @sogo (2020-07-19 01:11 UTC)

<p>Actually the slicer crashes on initialization screen so there is no way to go to toolbar options. If there is any external file or option which sets the temporaryPath, that could be tested. I have rebuilt slicer and changed my code, now it is working fine but I’ll be testing it more to see if this issue comes again, I doubt it will. Thanks for the help, closing this topic.</p>

---

## Post #6 by @lassoan (2020-07-19 03:37 UTC)

<aside class="quote no-group" data-username="sogo" data-post="5" data-topic="12607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/779978/48.png" class="avatar"> sogo:</div>
<blockquote>
<p>there is no way to go to toolbar options. If there is any external file or option which sets the temporaryPath</p>
</blockquote>
</aside>
<p>Temporary path is stored in <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#settings-file-location">Slicer.ini settings file</a>, you can view/change it by editing that file.</p>

---

## Post #7 by @sogo (2020-07-19 05:14 UTC)

<p>Yes, I checked and the temporary path field was empty in Slicer.ini file. Adding temporary path has fixed the issue. Thanks</p>

---
