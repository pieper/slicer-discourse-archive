---
topic_id: 31603
title: "Problem With General Registration Elastix"
date: 2023-09-07
url: https://discourse.slicer.org/t/31603
---

# Problem with General Registration (Elastix)

**Topic ID**: 31603
**Date**: 2023-09-07
**URL**: https://discourse.slicer.org/t/problem-with-general-registration-elastix/31603

---

## Post #1 by @xiangchaodong1 (2023-09-07 12:04 UTC)

<p>For example, when I want to use this tool for registration, there is an error. I have tried many cases and the data are the same. Could someone please help me solve it? The error code is as follows:<br>
`Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/bin/Python/slicer/util.py”, line 3146, in tryWithErrorDisplay<br>
yield<br>
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 241, in onApplyButton<br>
self.logic.registerVolumesUsingParameterNode(self._parameterNode)<br>
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 518, in registerVolumesUsingParameterNode<br>
self.registerVolumes(<br>
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 564, in registerVolumes<br>
self.logProcessOutput(elastixProcess)<br>
File “/Applications/Slicer.app/Contents/Extensions-32158/SlicerElastix/lib/Slicer-5.5/qt-scripted-modules/Elastix.py”, line 499, in logProcessOutput<br>
raise subprocess.CalledProcessError(return_code, “elastix”)<br>
subprocess.CalledProcessError: Command ‘elastix’ died with &lt;Signals.SIGABRT: 6&gt;.</p>
<p>I am MAC version 5.50, and the elastix plug-in version is the latest.`</p>

---

## Post #2 by @lassoan (2023-09-08 04:20 UTC)

<p><a class="mention" href="/u/xiangchaodong1">@xiangchaodong1</a> Does registration work with default settings on the <code>MRBrainTumor1</code> and <code>MRBrainTumor2</code> data sets?</p>
<p><a class="mention" href="/u/pieper">@pieper</a>, <a class="mention" href="/u/jcfr">@jcfr</a> or others who have access to a mac: could you check that Elastix (and in general, C++ modules in extensions) work well in Slicer-5.4/5.5 on macOS?<br>
Today I helped someone on a macOS computer and there were a number of errors about some shared libraries in extensions could not be loaded.</p>

---

## Post #3 by @pieper (2023-09-08 16:01 UTC)

<p>Yes, I’ve confirmed VMTK is broken too.</p>
<aside class="quote quote-modified" data-post="1" data-topic="31535">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/6de8d8/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-extensions-can-not-work-on-slicer-5-4-0-on-macos/31535">New extensions can not work on Slicer 5.4.0 on MacOS</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I have just updated Slicer VMTK to 144582e (2023-08-22). It showed the following error: 
dlopen(/Applications/Slicer 5.4.0.app/Contents/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/qt-loadable-modules/qSlicerBranchClipperModuleWidgetsPythonQt.so, 0x0002): Library not loaded: /Users/svc-dashboard/D/S/A/ITK-build/lib/libitkgdcmjpeg8-5.3.1.dylib
  Referenced from: &lt;8228E9E9-AE1B-31B6-BEEB-4F916BF21B91&gt; /Applications/Slicer 5.4.0.app/Contents/Extensions-31938/SlicerVMTK/lib/Slicer-5.4/libitkgdc…
  </blockquote>
</aside>


---

## Post #4 by @lassoan (2023-09-08 22:03 UTC)

<p>This is a very significant issue with the 5.4 release then.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you have a look at this?</p>

---

## Post #5 by @xiangchaodong1 (2023-09-09 01:58 UTC)

<p>Yes, the default registration: General Registration (BRIAN) can be used, but I am not skilled in using it.</p>

---
