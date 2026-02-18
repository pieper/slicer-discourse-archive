# QAccessibleTable warnings in preview release clean install

**Topic ID**: 12953
**Date**: 2020-08-11
**URL**: https://discourse.slicer.org/t/qaccessibletable-warnings-in-preview-release-clean-install/12953

---

## Post #1 by @mikebind (2020-08-11 23:04 UTC)

<p>Problem report for Slicer 4.11.0-2020-08-10 win-amd64:<br>
Expected behavior: Clean install of preview release should not generate warnings/errors on startup<br>
Actual behavior: Many instances of the warning<br>
<code>QAccessibleTable:: child: Invalid index at: 0 0</code><br>
on Slicer startup.</p>
<p>I had noticed these warnings on prior preview installs (my most recent one before today was 2020-05-27), but was never sure whether they might be due to problems with modules I wrote.  So, when I upgraded today to 2020-08-10, before I installed any of my modules or any extensions, I checked to see if there were any warnings and found these, so they can’t be due to any of my code or any extension code.  Here is the full log file on the first opening of 2020-08-10 today:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Session start time .......: 2020-08-11 15:44:03
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Slicer version ...........: 4.11.0-2020-08-10 (revision 29263 / 6afabbc) win-amd64 - installed release
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Operating system .........: Windows /  Professional / (Build 19041, Code Page 65001) - 64-bit
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Memory ...................: 32499 MB physical, 52979 MB virtual
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - CPU ......................: GenuineIntel , 12 cores, 12 logical processors
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Qt configuration .........: version 5.15.0, with SSL, requested OpenGL 3.2 (compatibility profile)
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Developer mode enabled ...: yes
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Application path .........: C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.11.0-2020-08-10/bin
[DEBUG][Qt] 11.08.2020 15:44:03 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 11.08.2020 15:44:05 [Python] (C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword...
[WARNING][Qt] 11.08.2020 15:44:06 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:06 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:06 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:06 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:06 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:06 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[DEBUG][Python] 11.08.2020 15:44:08 [Python] (C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:08 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[DEBUG][Python] 11.08.2020 15:44:09 [Python] (C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 11.08.2020 15:44:09 [Python] (C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2020-08-10\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[WARNING][Qt] 11.08.2020 15:44:09 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[WARNING][Qt] 11.08.2020 15:44:09 [] (unknown:0) - QAccessibleTable::child: Invalid index at: 0 0
[DEBUG][Qt] 11.08.2020 15:44:09 [] (unknown:0) - Switch to module:  "Welcome"
</code></pre>
<p>Note that the emoji’s are not in the log, it is replacing “:”+“child”+":" with <img src="https://emoji.discourse-cdn.com/twitter/child.png?v=9" title=":child:" class="emoji" alt=":child:"></p>

---

## Post #2 by @lassoan (2020-08-11 23:16 UTC)

<p>Thanks for reporting this. The warning seems harmless but is surely distracting and may mask other errors and warnings. I’ve added a ticket to make sure it gets addressed before Slicer5: <a href="https://github.com/Slicer/Slicer/issues/5094" class="inline-onebox">Warnings at startup: QAccessibleTable::child: Invalid index at: 0 0 · Issue #5094 · Slicer/Slicer · GitHub</a></p>
<p>To include source code or text, use triple-backtick before and after the text. For example:</p>
<p>Source:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9ffd7140427239d6c043098bbb217578cfe30a35.png" alt="image" data-base62-sha1="mPkULBGyiHLacc0zx8MtQNh9HyB" width="405" height="172"></p>
<p>Result:</p>
<blockquote>
<p>This will be displayed as emoji: <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
</blockquote>
<pre><code class="lang-auto">This will not be displayed as emoji: :)
</code></pre>

---

## Post #3 by @Sam_Horvath (2020-08-12 01:05 UTC)

<p>What is the OS build version number of your Windows 10 install?  I have the same issues occurring on a newer version (Version 2004, OS build 192628.1) but not on an older one (Version 1909, OS build 18363.959).</p>

---

## Post #4 by @mikebind (2020-08-12 15:10 UTC)

<p>My OS build is 19041.388, (version 2004) updated last week.  I had the warnings before the update, but I’m not sure what build number I was running at that point. I think the version number was in the 1800 range, I sort of remember feeling like the jump to 2004 was a big one.</p>

---

## Post #5 by @lassoan (2020-08-12 15:15 UTC)

<p>I’ve pushed a <a href="https://github.com/Slicer/Slicer/pull/5095">fix</a>.</p>
<p>The difference might not be the OS version but accessibility settings, as the warning is logged when the accessibility plugin cannot retrieve info about the currently selected item in a node selection combobox.</p>

---
