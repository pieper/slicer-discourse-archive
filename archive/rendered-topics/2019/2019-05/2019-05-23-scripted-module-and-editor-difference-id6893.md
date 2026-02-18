# Scripted Module and editor difference

**Topic ID**: 6893
**Date**: 2019-05-23
**URL**: https://discourse.slicer.org/t/scripted-module-and-editor-difference/6893

---

## Post #1 by @prorai (2019-05-23 09:35 UTC)

<p>Odd behavior when i run my Scriptable Module and when i run same code in Python interactor.<br>
i’m using threshold first to mask the segment and then applying seed grow for making segment, when i run it in python interactor it looks its working as expected , but same code in scripted module is not working as expected and i’m not seeing any difference with and without masking code</p>

---

## Post #2 by @pieper (2019-05-23 11:55 UTC)

<p>The most likely cause is that the GUI gets updated each time you hit return in the python interactor, but it’s blocked when executing a script.  So you might need to call <code>slicer.app.processEvents()</code> in your script or otherwise make it event driven.</p>

---

## Post #3 by @lassoan (2019-05-23 12:48 UTC)

<p>Segment Editor only use asynchronous event processing for display, so if you see difference in processing results then there may be some other trivial mistake (e.g., you have multiple segment editor parameter nodes and you change the wrong one). You can typically find such errors very easily by using a <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" rel="nofollow noopener">Python debugger</a>.</p>

---

## Post #4 by @prorai (2019-05-23 14:30 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
i tried to put <code>slicer.app.processEvents()</code>  this before applying threshold and after <code>effect.self().onUseForPaint()</code><br>
then the seedgrow Code from the example script referred by <a class="mention" href="/u/lassoan">@lassoan</a><br>
and i’m sure that i’ve created Segment editor node once and using that for both the segments (masking and seedgrow )</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a066a5262d275b8b6ba7fed44b1cad88f954eab.png" alt="image" data-base62-sha1="cQoIswQ4n62kqxBJpSpxJu90NXd" width="367" height="274"><br>
this is the effect when i call my scripted module.</p>
<p>and<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85ed568e7dc3927c99b9952a96b4e68c281b56ea.png" alt="image" data-base62-sha1="j6LZSO5eXsMY4TA0juoqFbrXqwa" width="322" height="194"><br>
and this is when i use same code in python interactor<br>
threshold masking is used and seeds grown in that limited area.</p>

---

## Post #5 by @lassoan (2019-05-24 17:40 UTC)

<p>If you show the editor widget, do you see that “Editable intensity range” is enabled?</p>
<p>Put a breakpoint in AbstractScriptedSegmentEditorAutoCompleteEffect.py in <code>preview(self)</code> method. What value <code>intensityBasedMasking</code> is set to?</p>

---

## Post #6 by @prorai (2019-05-29 07:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>intensityBasedMasking</p>
</blockquote>
</aside>
<p>I have 2 scenarios ,</p>
<ol>
<li>when i’m ruining my script in python interarctor , i can able to add breakpoints and i’m getting this value as True, and threshold masking works perfectly as expected .</li>
<li>when i call my script through batch file , i cant set the breakpoints and i cant see the “Editable intensity range” enable  when slicer window pop up. , threshold masking doesn’t seems to be applied here.</li>
</ol>
<p>so the thing is happening here as per my observation is, when i call the script module using batch file it goes in one shot and before the onUseForPaint() finishes the work, seedgrow code already gets executed and it doesn’t get that masking intensity.</p>
<p>i tried to put this code in thread , which doesn’t work , and i cant use the async/await call as i’m getting error for import asyncio. <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2019-05-29 16:18 UTC)

<aside class="quote no-group" data-username="prorai" data-post="6" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>when i call my script through batch file</p>
</blockquote>
</aside>
<p>Do you attempt to run the script without a main window?</p>
<aside class="quote no-group" data-username="prorai" data-post="6" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>when i call my script through batch file , i cant set the breakpoints</p>
</blockquote>
</aside>
<p>You should be able to set breakpoints the same way. To make sure your code runs after the debugger is attached, start you processing with a timer (e.g., after 5-10 seconds the application has started).</p>
<aside class="quote no-group" data-username="prorai" data-post="6" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>i tried to put this code in thread</p>
</blockquote>
</aside>
<p>I don’t think multithreading is relevant here.</p>

---

## Post #8 by @prorai (2019-05-30 10:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>start you processing with a timer</p>
</blockquote>
</aside>
<p>its helped me to debug my code.<br>
and finally i found the cause , its the slicer version.<br>
i have Slicer 4.11.0-2018-11-13 nightly version which was set for batch file process, and i was testing in stable 4.10 editor which was working fine.<br>
so in this nightly build i believe that the masking plus seedgrow has some issue or may be solved in next nightly release.</p>
<p>i’m really thankful to <a class="mention" href="/u/lassoan">@lassoan</a> for all the support .</p>
<p>one last thing</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you attempt to run the script without a main window?</p>
</blockquote>
</aside>
<p>i was using window mode .<br>
now everything is working in window mode but i just tried no-window mode and after crash this is the log i’m seeing</p>
<pre><code class="lang-auto">[CRITICAL][Qt] 30.05.2019 16:10:39 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::onSegmentSelectionChanged(const class QItemSelection &amp;,const class QItemSelection &amp;) : Invalid segment editor parameter set node
[CRITICAL][Qt] 30.05.2019 16:10:39 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::onSegmentationNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node
[CRITICAL][Qt] 30.05.2019 16:10:39 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::onSegmentSelectionChanged(const class QItemSelection &amp;,const class QItemSelection &amp;) : Invalid segment editor parameter set node
[CRITICAL][Qt] 30.05.2019 16:10:39 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::onSegmentationNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node
[CRITICAL][Qt] 30.05.2019 16:10:39 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node
[CRITICAL][Qt] 30.05.2019 16:10:39 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node
[CRITICAL][Qt] 30.05.2019 16:10:39 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::onMasterVolumeNodeChanged(class vtkMRMLNode *) : Invalid segment editor parameter set node
[WARNING][Qt] 30.05.2019 16:10:39 [] (unknown:0) - QObject::connect: Cannot connect (null)::layoutChanged(int) to qMRMLSegmentEditorWidget::onLayoutChanged(int)
[CRITICAL][Qt] 30.05.2019 16:10:39 [] (unknown:0) - void __cdecl qMRMLSegmentEditorWidget::updateWidgetFromMRML(void) : Invalid segment editor parameter set node
</code></pre>

---

## Post #9 by @lassoan (2019-05-30 13:10 UTC)

<aside class="quote no-group" data-username="prorai" data-post="8" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>so in this nightly build i believe that the masking plus seedgrow has some issue or may be solved in next nightly release.</p>
</blockquote>
</aside>
<p>Masking in “Grow from Seeds” effect is available since latest stable (Slicer-4.10.2) and recent preview releases.</p>
<aside class="quote no-group" data-username="prorai" data-post="8" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>i just tried no-window mode</p>
</blockquote>
</aside>
<p>I think Segment Editor currently requires a main application window (it may be possible to remove the dependency but we don’t plan to work on that right now).</p>

---

## Post #10 by @prorai (2019-05-30 13:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="6893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think Segment Editor currently requires a main application window</p>
</blockquote>
</aside>
<p>strange! , cause same script when i was using for seedgrow only (without masking code) , it was running fine with --no-window mode.</p>

---
