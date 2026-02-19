---
topic_id: 123
title: "Ext Manager And View Controller Broke"
date: 2017-04-14
url: https://discourse.slicer.org/t/123
---

# Ext manager and view controller broke

**Topic ID**: 123
**Date**: 2017-04-14
**URL**: https://discourse.slicer.org/t/ext-manager-and-view-controller-broke/123

---

## Post #1 by @mrjeffs (2017-04-14 23:04 UTC)

<p>Operating system: ubuntu 16.04<br>
Slicer version: 4.7.0-2017-3-12 and 4.7.0-2017-4-13<br>
Expected behavior: extension manager opens &amp; view controller shows red/yellow/green slice controls<br>
Actual behavior: invoking extension manger crashes slicer.<br>
tried clearing old configs etc but no love.<br>
also when slicer does load without invoking ext mngr only red slice controller appears in view controller.<br>
yellow and green only accessible via layout controls.<br>
turning off/on module panel doesn’t clear it.</p>

---

## Post #2 by @lassoan (2017-04-15 01:16 UTC)

<p>For me Extension manager works without problems in latest nightly version on a Ubuntu 16.04 virtual machine on HyperV.</p>
<p>It is normal that you select view layout (which viewers are displayed, where) using the layout toolbar button. You can enable saving of current layout in menu: Edit / Application settings / Appearance / Save user interface… checkbox. It only saves the selection if you exit Slicer, not if it crashes.</p>
<p>Could you attach the application log of a crashed session? (menu: Help / Report a bug, choose the previous session in the “Recent log files” listbox).</p>

---

## Post #3 by @mrjeffs (2017-04-17 17:03 UTC)

<p>it crashes with todays version 4-15-2017:</p>
<pre><code class="lang-nohighlight">toddr@redshirt:~/Software/Slicer-4.7.0-2017-04-15-linux-amd64$ ./Slicer &amp;
[1] 32736
toddr@redshirt:~/Software/Slicer-4.7.0-2017-04-15-linux-amd64$ Number of registered modules: 140 
Number of instantiated modules: 140 
When loading module  "CLIEventTest" , the dependency "CLI4Test" failed to be loaded. 
Initializing terminology mapping for map file /home/toddr/Software/Slicer-4.7.0-2017-04-15-linux-amd64/share/Slicer-4.7/ColorFiles/Terminology//GenericAnatomyColors-SNOMED.csv
288 terms were read for Slicer LUT GenericAnatomyColors
When loading module  "TwoCLIsInARowTest" , the dependency "CLI4Test" failed to be loaded. 
When loading module  "TwoCLIsInParallelTest" , the dependency "CLI4Test" failed to be loaded. 
Number of loaded modules: 137 
Switch to module:  "Welcome" 
error: [/home/toddr/Software/Slicer-4.7.0-2017-04-15-linux-amd64/./bin/SlicerApp-real] exit abnormally - Report the problem.

[1]+  Exit 1                  ./Slicer
</code></pre>
<p>and the previous log shows the load but not the crash. see below:</p>
<pre><code class="lang-nohighlight">[DEBUG][Qt] 17.04.2017 09:52:10 [] (unknown:0) - Session start time .......: 2017-04-17 09:52:10
[DEBUG][Qt] 17.04.2017 09:52:10 [] (unknown:0) - Slicer version ...........: 4.7.0-2017-04-15 (revision 25933) linux-amd64 - installed
[DEBUG][Qt] 17.04.2017 09:52:10 [] (unknown:0) - Operating system .........: Linux / 4.4.0-71-generic / #92-Ubuntu SMP Fri Mar 24 12:59:01 UTC 2017 - 64-bit
[DEBUG][Qt] 17.04.2017 09:52:10 [] (unknown:0) - Memory ...................: 128907 MB physical, 131036 MB virtual
[DEBUG][Qt] 17.04.2017 09:52:10 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Xeon(R) CPU E5-2667 v2 @ 3.30GHz, 16 cores, 32 logical processors
[DEBUG][Qt] 17.04.2017 09:52:10 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 17.04.2017 09:52:10 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 17.04.2017 09:52:10 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 17.04.2017 09:52:15 '[Python]' (/home/toddr/Software/Slicer-4.7.0-2017-04-15-linux-amd64/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 17.04.2017 09:52:16 [Python] (/home/toddr/Software/Slicer-4.7.0-2017-04-15-linux-amd64/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 17.04.2017 09:52:16 [Python] (/home/toddr/Software/Slicer-4.7.0-2017-04-15-linux-amd64/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 17.04.2017 09:52:11 [] (unknown:0) - Number of registered modules: 140
[DEBUG][Qt] 17.04.2017 09:52:12 [] (unknown:0) - Number of instantiated modules: 140
[WARNING][Qt] 17.04.2017 09:52:15 [] (unknown:0) - When loading module  "CLIEventTest" , the dependency "CLI4Test" failed to be loaded.
[INFO][Stream] 17.04.2017 09:52:15 [] (unknown:0) - Initializing terminology mapping for map file /home/toddr/Software/Slicer-4.7.0-2017-04-15-linux-amd64/share/Slicer-4.7/ColorFiles/Terminology//GenericAnatomyColors-SNOMED.csv
[INFO][Stream] 17.04.2017 09:52:15 [] (unknown:0) - 288 terms were read for Slicer LUT GenericAnatomyColors
[WARNING][Qt] 17.04.2017 09:52:16 [] (unknown:0) - When loading module  "TwoCLIsInARowTest" , the dependency "CLI4Test" failed to be loaded.
[WARNING][Qt] 17.04.2017 09:52:16 [] (unknown:0) - When loading module  "TwoCLIsInParallelTest" , the dependency "CLI4Test" failed to be loaded.
[DEBUG][Qt] 17.04.2017 09:52:16 [] (unknown:0) - Number of loaded modules: 137
[DEBUG][Qt] 17.04.2017 09:52:16 [] (unknown:0) - Switch to module:  "Welcome"
</code></pre>

---

## Post #4 by @mrjeffs (2017-04-17 22:08 UTC)

<p>tried with mac version on laptop got same result. here is the bug report:</p>
<pre><code class="lang-nohighlight">[DEBUG][Qt] 17.04.2017 15:05:04 [] (unknown:0) - Session start time .......: 2017-04-17 15:05:04
[DEBUG][Qt] 17.04.2017 15:05:04 [] (unknown:0) - Slicer version ...........: 4.7.0-2017-04-15 (revision 25933) macosx-amd64 - installed
[DEBUG][Qt] 17.04.2017 15:05:04 [] (unknown:0) - Operating system .........: Mac OS X / 10.10.5 / 14F2315 - 64-bit
[DEBUG][Qt] 17.04.2017 15:05:04 [] (unknown:0) - Memory ...................: 16384 MB physical, 8192 MB virtual
[DEBUG][Qt] 17.04.2017 15:05:04 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-4960HQ CPU @ 2.60GHz, 4 cores, 8 logical processors
[DEBUG][Qt] 17.04.2017 15:05:04 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 17.04.2017 15:05:04 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 17.04.2017 15:05:04 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 17.04.2017 15:05:12 '[Python]' (/Applications/Slicer_dev4p7_4-15-2017.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 17.04.2017 15:05:13 [Python] (/Applications/Slicer_dev4p7_4-15-2017.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 17.04.2017 15:05:13 [Python] (/Applications/Slicer_dev4p7_4-15-2017.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 17.04.2017 15:05:07 [] (unknown:0) - Number of registered modules: 140
[DEBUG][Qt] 17.04.2017 15:05:08 [] (unknown:0) - Number of instantiated modules: 140
[WARNING][Qt] 17.04.2017 15:05:12 [] (unknown:0) - When loading module  "CLIEventTest" , the dependency "CLI4Test" failed to be loaded.
[INFO][Stream] 17.04.2017 15:05:12 [] (unknown:0) - Initializing terminology mapping for map file /Applications/Slicer_dev4p7_4-15-2017.app/Contents/share/Slicer-4.7/ColorFiles/Terminology//GenericAnatomyColors-SNOMED.csv
[INFO][Stream] 17.04.2017 15:05:12 [] (unknown:0) - 288 terms were read for Slicer LUT GenericAnatomyColors
[WARNING][Qt] 17.04.2017 15:05:13 [] (unknown:0) - When loading module  "TwoCLIsInARowTest" , the dependency "CLI4Test" failed to be loaded.
[WARNING][Qt] 17.04.2017 15:05:13 [] (unknown:0) - When loading module  "TwoCLIsInParallelTest" , the dependency "CLI4Test" failed to be loaded.
[DEBUG][Qt] 17.04.2017 15:05:13 [] (unknown:0) - Number of loaded modules: 137
[DEBUG][Qt] 17.04.2017 15:05:13 [] (unknown:0) - Switch to module:  "Welcome"
</code></pre>
<p>clicking on download plugins causes crash.</p>

---

## Post #5 by @ihnorton (2017-04-17 22:22 UTC)

<p>A post was split to a new topic: <a href="/t/new-user-link-limit/137">New user link limit?</a></p>

---

## Post #6 by @lassoan (2017-04-17 23:22 UTC)

<p>Thank you for your reports. There is nothing suspicious in the logs.</p>
<p>Could you send a backtrace of the crash?<br>
(<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Analyze_a_segmentation_fault">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Analyze_a_segmentation_fault</a>)</p>
<p>Are there other ways you can crash Slicer (loading data, running CLI modules, etc)?</p>
<p>Does a web browser appear if you run the following code in the Slicer Python console (Ctrl + 3)?<br>
<code>w=qt.QWebView(); w.setUrl(qt.QUrl('http://www.google.com')); w.show()</code></p>

---

## Post #7 by @mrjeffs (2017-04-21 20:17 UTC)

<p>before i do all that, are we sure this is not related to thread 168<br>
NA-MIC site down?<br>
j</p>

---

## Post #8 by @lassoan (2017-04-21 20:31 UTC)

<p>The appstore is not related to the NA-MIC wiki, so you can go ahead with your testing.</p>

---

## Post #9 by @mrjeffs (2017-05-08 14:19 UTC)

<p>i found the problem, i deleted the .config/NA-MIC directory and started fresh and now everything works again.<br>
seems there was a conflict with something in the .ini or past extensions… thats as far as i got. j</p>

---
