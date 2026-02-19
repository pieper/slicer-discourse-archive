---
topic_id: 28654
title: "Getting Pointer On Modules Logic And Open Show The Logic Wid"
date: 2023-03-29
url: https://discourse.slicer.org/t/28654
---

# Getting pointer on module's logic and open/show the logic widget

**Topic ID**: 28654
**Date**: 2023-03-29
**URL**: https://discourse.slicer.org/t/getting-pointer-on-modules-logic-and-open-show-the-logic-widget/28654

---

## Post #1 by @adeguet1 (2023-03-29 14:23 UTC)

<p>In python, we can do: <code>slicer.util.getModuleLogic(name)</code> and <code>getModuleLogic</code>.  Is there an equivalent in C++?  For example, when loading a MRML scene, in the UpdateScene callback, I’d like to make sure a module exists and has been properly loaded.  I would also like to know if the GUI for that module is shown.</p>
<p>Since it would be in the Node::UpdateScene, is there a path from the scene pointer to find the application’s logic and from there find the module’s logic?  Or, is there a registry accessible via a static methods to all the loaded modules?</p>

---

## Post #2 by @lassoan (2023-03-29 14:40 UTC)

<aside class="quote no-group" data-username="adeguet1" data-post="1" data-topic="28654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/aeb1de/48.png" class="avatar"> adeguet1:</div>
<blockquote>
<p>In python, we can do: <code>slicer.util.getModuleLogic(name)</code> and <code>getModuleLogic</code>. Is there an equivalent in C++?</p>
</blockquote>
</aside>
<p>You can get a module’s logic from any other module’s logic using the <a href="https://apidocs.slicer.org/main/classvtkSlicerModuleLogic.html#a7d7ca329e0cc60869ed8a20829eaa9ae">GetModuleLogic(moduleName)</a> method. From any GUI class, you can use the application’s <a href="https://apidocs.slicer.org/main/classqSlicerCoreApplication.html#a9aa6380c45c7dae28e933af109d550bf">moduleLogic(moduleName)</a> method.</p>
<aside class="quote no-group" data-username="adeguet1" data-post="1" data-topic="28654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/aeb1de/48.png" class="avatar"> adeguet1:</div>
<blockquote>
<p>I’d like to make sure a module exists and has been properly loaded</p>
</blockquote>
</aside>
<p>If your module depends on a module (the module class returns the list of dependencies in the <code>dependencies()</code> method) then tou don’t need to check if that module exists. Slicer would not initialize your module if any of the dependencies were missing.</p>
<aside class="quote no-group" data-username="adeguet1" data-post="1" data-topic="28654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/aeb1de/48.png" class="avatar"> adeguet1:</div>
<blockquote>
<p>I would also like to know if the GUI for that module is shown.</p>
</blockquote>
</aside>
<p>Whether a module has a GUI, has it been created, or shown yet is a private business of that module. In general, a module should not directly access or manipulate another module’s GUI in any way. Instead, your module can modify the MRML scene and other modules can observe those changes. You can also call methods in any other module’s logic.</p>
<p>Why would you need to know if another module’s GUI is shown?</p>
<aside class="quote no-group" data-username="adeguet1" data-post="1" data-topic="28654">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/aeb1de/48.png" class="avatar"> adeguet1:</div>
<blockquote>
<p>Since it would be in the Node::UpdateScene, is there a path from the scene pointer to find the application’s logic and from there find the module’s logic?</p>
</blockquote>
</aside>
<p>Nodes are only for data storage, so you don’t initiate any module logic operations from there. Instead, your module logic can observe scene changes and perform operations in response.</p>

---
