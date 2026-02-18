# Extensions not showing anything

**Topic ID**: 23432
**Date**: 2022-05-14
**URL**: https://discourse.slicer.org/t/extensions-not-showing-anything/23432

---

## Post #1 by @sodium83 (2022-05-14 19:36 UTC)

<p>Using Ubuntu 22.04 and Slicer 4.11.20210226. Also tried on the preview release.</p>
<p>Loading Extensions Manager shows 100% at bottom but nothing appears. I am just using this on a home computer with no firewalls etc. My internet connection otherwise works fine.</p>
<p>Desperately trying to install the VMTK.</p>
<p>Any help appreciated.</p>
<p>Kind regards,</p>
<p>Jeremy.</p>
<p>LOG:<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Session start time …: 2022-05-14 09:33:30<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) linux-amd64 - installed release<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Operating system …: Linux / 5.15.0-27-generic / <span class="hashtag">#28-Ubuntu</span> SMP Thu Apr 14 04:55:28 UTC 2022 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Memory …: 15788 MB physical, 2047 MB virtual<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - CPU …: GenuineIntel 12th Gen Intel(R) Core™ i5-12600K, 10 cores, 16 logical processors<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Application path …: /home/jeremy/.var/app/Slicer/bin<br>
[DEBUG][Qt] 14.05.2022 09:33:30 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 14.05.2022 09:33:31 [Python] (/home/jeremy/.var/app/Slicer/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 14.05.2022 09:33:33 [Python] (/home/jeremy/.var/app/Slicer/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 14.05.2022 09:33:33 [Python] (/home/jeremy/.var/app/Slicer/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 14.05.2022 09:33:33 [Python] (/home/jeremy/.var/app/Slicer/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 14.05.2022 09:33:33 [] (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 14.05.2022 09:33:34 [] (unknown:0) - An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
[WARNING][Qt] 14.05.2022 09:33:39 [] (unknown:0) - QXcbConnection: XCB error: 3 (BadWindow), sequence: 2096, resource id: 13383320, major code: 40 (TranslateCoords), minor code: 0<br>
[WARNING][Qt] 14.05.2022 09:34:28 [] (unknown:0) - QXcbConnection: XCB error: 3 (BadWindow), sequence: 4651, resource id: 13387921, major code: 40 (TranslateCoords), minor code: 0</p>

---

## Post #2 by @lassoan (2022-05-14 21:04 UTC)

<p>Check out these troubleshooting instructions and let us know if they help:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extensions-manager-does-not-show-any-extensions" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html#extensions-manager-does-not-show-any-extensions</a></p>

---

## Post #3 by @Davide_Cester (2022-05-17 10:17 UTC)

<p>Hi,</p>
<p>I am having a similar issue. The Extension list only reports “All (0)”. This happens both via Slicer and by manually visiting the URL <a href="http://slicer.kitware.com/midas3/slicerappstore" class="inline-onebox" rel="noopener nofollow ugc">@KitwareMedical/slicer-extensions-webapp</a></p>
<p>EDIT: Slicer version 4.11.0-2020-06-12 r29143 / 95c7682<br>
I am using Ubuntu, my kernel is recent (5.13), the file ‘/proc/sys/kernel/unprivileged_userns_clone’ contains 1 and --no-sandbox has no effect, as well as QTWEBENGINE_DISABLE_SANDBOX=1 ./Slicer.</p>
<p>Any hint? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @cpinter (2022-05-17 10:39 UTC)

<p>The Midas backend of the older Slicer versions has been replaced by a new one, and so extensions for those versions are not available.</p>
<p>You’ll need to use a more recent Slicer. 5.0 will be released imminently, and the 5.1 preview version is virtually identical to the coming stable.</p>

---

## Post #5 by @RyanZurrin (2022-09-12 18:01 UTC)

<p>I am using Ubuntu 22.04 and was having the same issue.<br>
This is the step that worked for me, using this flag before launching Slicer: <code>QTWEBENGINE_DISABLE_SANDBOX=1</code>.</p>
<p>Thanks for pointing me in the right direction.</p>

---

## Post #6 by @Gonzalo_Rojas_Costa (2023-01-19 20:28 UTC)

<p>Where should I put <code>QTWEBENGINE_DISABLE_SANDBOX=1</code> ?</p>

---

## Post #7 by @muratmaga (2023-01-19 20:32 UTC)

<p>in the terminal window, before you start Slicer. So this will be shell command like<br>
<code>export QTWEBENGINE_DISABLE_SANDBOX=1</code><br>
then you can invoke<br>
./Slicer<br>
and extension manager should be available to you.</p>

---

## Post #8 by @RafaelPalomar (2023-01-20 05:49 UTC)

<p>This issue was recently addressed (<a href="https://github.com/Slicer/Slicer/pull/6744#event-8096626953" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix blank Extensions manager for Linux package due to Chromium sandboxing by jcfr · Pull Request #6744 · Slicer/Slicer · GitHub</a>). In the current preview release there is no need to set this variable.</p>

---
