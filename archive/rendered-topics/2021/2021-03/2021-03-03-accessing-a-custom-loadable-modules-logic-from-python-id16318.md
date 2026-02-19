---
topic_id: 16318
title: "Accessing A Custom Loadable Modules Logic From Python"
date: 2021-03-03
url: https://discourse.slicer.org/t/16318
---

# Accessing a custom loadable module's logic from python

**Topic ID**: 16318
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/accessing-a-custom-loadable-modules-logic-from-python/16318

---

## Post #1 by @hphalen (2021-03-03 02:07 UTC)

<p>Hello, I am working with an existing custom loadable module (written in C++) and was hoping to be able to access functions from the module’s logic in the python interface and/or within a scripted python module.</p>
<p>For the existing modules that come with Slicer, I typically do this as recommended here <a href="https://discourse.slicer.org/t/how-to-call-a-function-from-the-logic/6433/2" class="inline-onebox">How to call a function from the logic - #2 by pieper</a></p>
<p>e.g.</p>
<pre><code class="lang-auto">slicer.modules.screencapture.widgetRepresentation().self().logic
</code></pre>
<p>However, for the loadable module that was developed in my group, the widgetRepresentation does not have a ‘self’. I was wondering if it is even possible to access the logic of C++ loadable modules in this way?</p>

---

## Post #2 by @lassoan (2021-03-03 02:11 UTC)

<p>For Python scripted modules, you need to call <code>self()</code> to get the Python implementation of the generic C++ widget representation, an call <code>logic</code> because in scripted modules it makes dynamic reloading of the module much easier if the widget owns the logic. In C++ you don’t need any of these, so you can simply call <code>logic()</code> method of the module class, for example: <code>slicer.modules.volumerendering.logic()</code>.</p>
<p>This and many other useful concepts are described in the PerkLab developer tutorial: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials" class="inline-onebox">Documentation/Nightly/Training - Slicer Wiki</a></p>

---

## Post #3 by @pll_llq (2021-03-03 11:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16318">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>it makes dynamic reloading of the module much easier if the widget owns the logic</p>
</blockquote>
</aside>
<p>This is the answer to a question I had after I went through the tutorials after the call on Tuesday=)<br>
Thanks for the advice to revisit the PerkLab presentations. It really is an iterative process.</p>

---

## Post #4 by @hphalen (2021-03-03 18:16 UTC)

<p>Thank you for your response! The distinction is clear - I had not seen this PerkLab tutorial before so thank you for the link.</p>
<p>I tried the <code>slicer.modules.modulename.logic()</code> route previously, but did not get access to any of the logic methods from the module, just standard ones (e.g. <code>AddObserver()</code>, <code>BreakOnError()</code>, etc.) so I thought it was the wrong approach. Instead, it seems there must be an implementation issue with the loadable module I am using such that it isn’t exposing these methods correctly.</p>
<p>I wanted to make sure that my assumption/understanding is correct as I try to hunt down the issue. If things are done correctly, should I be able to call all of the public methods of <code>vtkSlicer[ModuleName]Logic</code> from Python using the method we discussed of</p>
<pre><code class="lang-auto">logic = slicer.modules.modulename.logic()
logic.method() 
</code></pre>
<p>?</p>
<p>To be (hopefully) more clear, the setup is as follows:<br>
There is a module which in the top-level directory has <code>qSlicerUniversalRobotModule.cxx(/h)</code> and <code>qSlicerUniversalRobotModuleWidget.cxx(/h)</code>. The module has a <code>createLogic()</code> method which creates a new instance of <code>vtkSlicerUniversalRobotLogic</code>, which is derived from <code>vtkSlicerModuleLogic</code>. Basically, my questions i, if everything was set up correctly, should I be able to access the public methods of this <code>vtkSlicerUniversalRobotLogic</code>?</p>
<p>Thanks again!</p>

---

## Post #5 by @lassoan (2021-03-03 18:37 UTC)

<aside class="quote no-group quote-modified" data-username="hphalen" data-post="4" data-topic="16318">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/c6cbf5/48.png" class="avatar"> hphalen:</div>
<blockquote>
<p>should I be able to call all of the public methods of ‘vtkSlicer[ModuleName]Logic’ from Python using the method we discussed of<br>
logic = slicer.modules.modulename.logic()<br>
logic.method() ?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="hphalen" data-post="4" data-topic="16318">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/c6cbf5/48.png" class="avatar"> hphalen:</div>
<blockquote>
<p>if everything was set up correctly, should I be able to access the public methods of this vtkSlicerUniversalRobotLogic?</p>
</blockquote>
</aside>
<p>Yes.<br>
The first thing to check is the class name that is displayed when you call <code>slicer.modules.modulename.logic()</code>. If that’s correct then you can call <code>help(slicer.modules.modulename.logic())</code> to see what methods are visible from Python.</p>

---

## Post #6 by @hphalen (2021-03-03 18:41 UTC)

<p>Thanks - for me it says the following when I call <code>slicer.modules.modulename.logic()</code>:<br>
vtkCommonCorePython.vtkSlicerModuleLogic.</p>
<p>I imagine if this was working correctly it would say vtkSlicerUniversalRobotModuleLogic? If so, I at least know my problem now <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #7 by @lassoan (2021-03-03 19:36 UTC)

<p>There is either something unusual in the logic class header file (e.g., you have included some headers from a third-party library - those should be all just included in the implementation cxx file), or maybe there is something wrong with the export declaration (between <code>class</code> keyword and class name in the header file). You can make a verbatim copy of a loadable module from an extension and see if you see the logic methods. If yes, then you can start modifying it step by step and see what change causes failure of the Python wrapping.</p>

---

## Post #8 by @hphalen (2021-03-03 20:13 UTC)

<blockquote>
<p>There is either something unusual in the logic class header file (e.g., you have included some headers from a third-party library</p>
</blockquote>
<p>This is exactly the problem, and it is done quite liberally. Many of the variables are of types defined by headers outside of Slicer (from internal code developed in our group). Basically, I think previous developers have baked in a lot of extraneous things into this logic code that should be elsewhere if done correctly. I don’t see a straightforward way of moving that over to the implementation, so unfortunately I will either have to do a large refactoring of this or find some other approach…</p>
<p>Thank you for you help - figuring out the issue here has been very helpful.</p>

---

## Post #9 by @lassoan (2021-03-03 20:55 UTC)

<p>No redesign should be needed. You can use the private implementation (PIMPL) pattern, it is used many places (search for <code>vtkInternal</code>).</p>
<p>In general, logic should encapsulate libraries: classes from third-party libraries should not leak out to public interface of a logic class.</p>

---

## Post #10 by @hphalen (2021-03-04 21:23 UTC)

<p>Thanks you Andras. This was very helpful. I was able to implement this and it seems to be working!</p>
<p>I just wanted to leave a note here in case someone runs into the same problem in the future. While I needed to do what was described above, I also found that there was the following line ‘DISABLE_WRAP_PYTHON’ in the CMakeLists in the Logic folder of the Loadable Module (see below). Unsurprisingly(!), if this is here, no matter how clean your logic headers are, the python wrapping will be skipped.</p>
<pre><code class="lang-auto">  NAME ${KIT}
  EXPORT_DIRECTIVE ${${KIT}_EXPORT_DIRECTIVE}
  INCLUDE_DIRECTORIES ${${KIT}_INCLUDE_DIRECTORIES}
  SRCS ${${KIT}_SRCS}
  TARGET_LIBRARIES ${${KIT}_TARGET_LIBRARIES}
  DISABLE_WRAP_PYTHON
  )
</code></pre>
<p>Thanks again!</p>

---
