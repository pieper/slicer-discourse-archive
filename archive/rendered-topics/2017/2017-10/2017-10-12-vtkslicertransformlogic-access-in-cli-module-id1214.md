---
topic_id: 1214
title: "Vtkslicertransformlogic Access In Cli Module"
date: 2017-10-12
url: https://discourse.slicer.org/t/1214
---

# vtkSlicerTransformLogic access in CLI module

**Topic ID**: 1214
**Date**: 2017-10-12
**URL**: https://discourse.slicer.org/t/vtkslicertransformlogic-access-in-cli-module/1214

---

## Post #1 by @danielbr (2017-10-12 18:36 UTC)

<p>Having a small issue that is driving me crazy and I can’t figure it out.  It is such a simple problem, but I can’t seem to remedy the problem.</p>
<p>I am writing a CLI module and need access to the transform module logic.  I try to get access to it by doing the following:</p>
<p><span class="hashtag">#include</span> “qSlicerAbstractModule.h”<br>
<span class="hashtag">#include</span> “qSlicerCoreApplication.h”<br>
<span class="hashtag">#include</span> “qSlicerModuleManager.h”<br>
<span class="hashtag">#include</span> “vtkSlicerTransformLogic.h”<br>
<span class="hashtag">#include</span> &lt;vtkMRMLTransformNode.h&gt;</p>
<p>vtkSlicerTransformLogic* transformLogic= vtkSlicerTransformLogic::SafeDownCast(qSlicerCoreApplication::application()-&gt;moduleManager()-&gt;module(“transforms”)-&gt;logic());</p>
<p>When I try to compile I get this error message “Error	1	error LNK2019: unresolved external symbol “__declspec(dllimport) public: static class vtkSlicerTransformLogic * __cdecl vtkSlicerTransformLogic::SafeDownCast(class vtkObjectBase *)” (_<em>imp</em>?SafeDownCast@vtkSlicerTransformLogic@<span class="mention">@SAPEAV1</span>@PEAVvtkObjectBase@@<span class="mention">@Z</span>)”</p>
<p>I have been able to access other module logic doing the exact same thing but I just can’t seem to do it for the transform module.  What am I missing here?</p>

---

## Post #2 by @lassoan (2017-10-12 18:37 UTC)

<p>You need to add transforms logic library to the list of libraries in your CMakeLists.txt.</p>

---

## Post #3 by @danielbr (2017-10-12 19:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1214">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>transforms logic library</p>
</blockquote>
</aside>
<p>Duh.  Thanks.  Haven’t edited my cmake file in awhile in this module.  Didn’t even cross my mind.  Works now!</p>

---
