# Error message when Slicer 4.9 starts

**Topic ID**: 3943
**Date**: 2018-08-30
**URL**: https://discourse.slicer.org/t/error-message-when-slicer-4-9-starts/3943

---

## Post #1 by @Cerezha (2018-08-30 01:23 UTC)

<p>Problem report for Slicer 4.9.0-2018-08-28 linux-amd64:</p>
<p>Hello everyone<br>
New version 4.9 produce the error messages at the start (see below), before loading the data. I am wondering if somebody can read the log (below) and explain what is the problem? Also, may be somebody can comment on following:<br>
I am using Slicer to segment my cell membranes in the tomograms (mrc file). The agreement for my data is that high density is dark. It is my understanding that Slicer agreement is that high density (bone etc) is light (as X-ray). Do I need to change my data-file to reverse densities (making high-density dark)? If so, how I can do it in simple way?<br>
Many thanks in advance! Sergey</p>
<p>Linux: Linux version 3.14.43-desktop-1.mga4 (<a href="mailto:iurt@ecosse.mageia.org">iurt@ecosse.mageia.org</a>) (gcc version 4.8.2 (GCC) ) <span class="hashtag">#1</span> SMP Thu May 21 21:25:55 UTC 2015</p>
<pre><code>[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - Session start time .......: 2018-08-29 13:16:09
[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - Slicer version ...........: 4.9.0-2018-08-28 (revision 27373) linux-amd64 - installed release
[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - Operating system .........: Linux / 3.14.43-desktop-1.mga4 / #1 SMP Thu May 21 21:25:55 UTC 2015 - 64-bit
[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - Memory ...................: 32086 MB physical, 48724 MB virtual
[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - CPU ......................: AuthenticAMD AMD FX(tm)-8350 Eight-Core Processor, 4 cores, 8 logical processors
[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - Prefer executable CLI ....: no
[DEBUG][Qt] 29.08.2018 13:16:09 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 29.08.2018 13:16:10 [Python] (/home/sergey/Slicer-4.9/lib/Python/lib/python2.7/site-packages/git/cmd.py:719) - Popen(['git', 'version'], cwd=/home/sergey/Slicer-4.9, universal_newlines=False, shell=None)
[DEBUG][Python] 29.08.2018 13:16:10 [Python] (/home/sergey/Slicer-4.9/lib/Python/lib/python2.7/site-packages/git/cmd.py:719) - Popen(['git', 'version'], cwd=/home/sergey/Slicer-4.9, universal_newlines=False, shell=None)
[DEBUG][Python] 29.08.2018 13:16:14 [Python] (/home/sergey/Slicer-4.9/lib/Slicer-4.9/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 29.08.2018 13:16:15 [Python] (/home/sergey/Slicer-4.9/lib/Slicer-4.9/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 29.08.2018 13:16:15 [Python] (/home/sergey/Slicer-4.9/lib/Slicer-4.9/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 29.08.2018 13:16:15 [] (unknown:0) - Switch to module:  "Editor"
[WARNING][Qt] 29.08.2018 13:16:16 [] (unknown:0) - "QFormBuilder was unable to create a custom widget of the class 'ctkCollapsibleButton'; defaulting to base class 'QWidget'."
[WARNING][Qt] 29.08.2018 13:16:16 [] (unknown:0) - "QFormBuilder was unable to create a custom widget of the class 'ctkCollapsibleGroupBox'; defaulting to base class 'QGroupBox'."
[WARNING][Qt] 29.08.2018 13:16:16 [] (unknown:0) - "QFormBuilder was unable to create a custom widget of the class 'ctkCollapsibleGroupBox'; defaulting to base class 'QGroupBox'."
[WARNING][Qt] 29.08.2018 13:16:16 [] (unknown:0) - "QFormBuilder was unable to create a custom widget of the class 'ctkCollapsibleGroupBox'; defaulting to base class 'QGroupBox'."
[WARNING][Qt] 29.08.2018 13:16:16 [] (unknown:0) - "QFormBuilder was unable to create a custom widget of the class 'ctkCollapsibleButton'; defaulting to base class 'QWidget'."
[WARNING][Qt] 29.08.2018 13:16:16 [] (unknown:0) - "QFormBuilder was unable to create a custom widget of the class 'ctkCollapsibleGroupBox'; defaulting to base class 'QGroupBox'."
[WARNING][Qt] 29.08.2018 13:16:16 [] (unknown:0) - "QFormBuilder was unable to create a custom widget of the class 'ctkCollapsibleGroupBox'; defaulting to base class 'QGroupBox'."</code></pre>

---

## Post #2 by @lassoan (2018-08-30 02:14 UTC)

<p>Please try to use Segment Editor module instead of the legacy Editor module and let us know if you run into any problem.</p>

---

## Post #3 by @Cerezha (2018-08-30 06:10 UTC)

<p>Hello<br>
I do not understand how the use of segment editor can affect the error message? As I stated above, the error message appeared immediately after launching the program, before loading files.  I am using Segmentation Editor right now and so far I do not see much difference with old Editor (sorry!). Perhaps because my project is very specific - I am segmenting the tomogramm, which is very noisy. Nevertheless, Slicer is so far the best program for my needs. Many thanks for improving it!!!</p>

---

## Post #4 by @lassoan (2018-08-30 11:25 UTC)

<p>You have ‘Switch to module:  “Editor”’ in your log, which means that the Editor module is activated. Maybe it is set as startup module. You can change it in application settings / Modules section.</p>

---

## Post #5 by @pieper (2018-08-30 11:56 UTC)

<aside class="quote no-group" data-username="Cerezha" data-post="1" data-topic="3943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f08c70/48.png" class="avatar"> Cerezha:</div>
<blockquote>
<p>I am wondering if somebody can read the log (below) and explain what is the problem?</p>
</blockquote>
</aside>
<p>Nothing in the log file necessarily indicates and error.  What’s not working as you expect?</p>
<aside class="quote no-group" data-username="Cerezha" data-post="1" data-topic="3943">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f08c70/48.png" class="avatar"> Cerezha:</div>
<blockquote>
<p>The agreement for my data is that high density is dark. It is my understanding that Slicer agreement is that high density (bone etc) is light (as X-ray). Do I need to change my data-file to reverse densities (making high-density dark)? If so, how I can do it in simple way?</p>
</blockquote>
</aside>
<p>It shouldn’t matter if you are trying to segment light or dark areas, things like the threshold effect have both high and low cutoff options.</p>
<p>Maybe you can paste in some screenshots showing what isn’t working for you.</p>

---
