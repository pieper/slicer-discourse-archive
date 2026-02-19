---
topic_id: 22587
title: "Segfault With In Qslicerapplicationprivate Only With Slicerc"
date: 2022-03-18
url: https://discourse.slicer.org/t/22587
---

# SegFault with in `~qSlicerApplicationPrivate` only with SlicerCAT

**Topic ID**: 22587
**Date**: 2022-03-18
**URL**: https://discourse.slicer.org/t/segfault-with-in-qslicerapplicationprivate-only-with-slicercat/22587

---

## Post #1 by @keri (2022-03-18 15:27 UTC)

<p>Hi,</p>
<p>When I updated the Slicer commit in my SlicerCAT I started to get Segmentation Fault in <a href="https://github.com/Slicer/Slicer/blob/5d334fd3885d0a717dbc7e38772edc5db8838ffb/Base/QTGUI/qSlicerApplication.cxx#L181" rel="noopener nofollow ugc">qSlicerApplicationPrivate destructor</a></p>
<p>This happens only with SlicerCAT (clean Slicer app works fine) even when all the modules are disabled ie SlicerCAT is launched with  <code>--disable-modules</code></p>
<p>Here are the steps that leads to this:</p>
<ol>
<li>launch SlicerCAT</li>
<li>open <code>Application Settings</code>
</li>
<li>close <code>Application Settings</code>
</li>
<li>close SlicerCAT</li>
</ol>
<p>It seems that <code>this-&gt;SettingsDialog</code> is already somehow unavailable by the time setting <code>setParent(nullptr)</code><br>
I’ve tried to rebuild it, debug but without success. Even though the idea behind creating/deleting <code>SettingsDialog</code> is pretty clear.</p>
<p>If somebody uses SlicerCAT with recent commits (after 26 february) I would appreciate for testing that.</p>

---

## Post #2 by @keri (2022-03-18 15:56 UTC)

<p>Oh it seems I understand the root of a problem:</p>
<p>At first <code>Settings</code> has <a href="https://github.com/Slicer/Slicer/blob/5d334fd3885d0a717dbc7e38772edc5db8838ffb/Base/QTGUI/qSlicerApplication.cxx#L274" rel="noopener nofollow ugc">no parent at the initilization time</a></p>
<p>When we click on <code>Application Settings</code> the <code>Settings</code> object gets <a href="https://github.com/Slicer/Slicer/blob/5d334fd3885d0a717dbc7e38772edc5db8838ffb/Base/QTGUI/qSlicerApplication.cxx#L745" rel="noopener nofollow ugc"><code>MainWindow</code> parent</a>. That means <code>MainWindow</code> destructor will delete <code>Settings</code>.</p>
<p>Then in <code>~qSlicerApplicationPrivate()</code> destructor we are trying to set <a href="https://github.com/Slicer/Slicer/blob/5d334fd3885d0a717dbc7e38772edc5db8838ffb/Base/QTGUI/qSlicerApplication.cxx#L181-L182" rel="noopener nofollow ugc"><code>Settings</code> parent to <code>nullptr</code> and explicitely delete <code>Settings</code></a>.</p>
<p>But what if <code>~MainWindow</code> destructor is called before <code>~qSlicerApplicationPrivate</code> destructor? Then in <code>~qSlicerApplicationPrivate</code> we will try to access deleted <code>Settings</code> object.</p>
<p>I added <code>cout</code> to these destructors to see who is deleted first and the output is:</p>
<pre><code class="lang-auto">$ ./Colada --disable-modules
QXcbConnection: XCB error: 3 (BadWindow), sequence: 1157, resource id: 14779307, major code: 40 (TranslateCoords), minor code: 0
MainWindow destructor is called
Switch to module:  ""
qSlicerApplicationPrivate destructor is called
error: [~/Documents/Colada/d/Slicer-build/bin/./ColadaApp-real] exit abnormally - Report the problem.
</code></pre>
<p>That means in my SlicerCAT (I suspect in others too) <code>~MainWindow</code> is deleted first so there is no need to explicitely delete <code>Settings</code> in <code>~qSlicerApplicationPrivate</code> destructor.</p>
<p>Please take a look at this</p>

---

## Post #3 by @lassoan (2022-03-19 00:25 UTC)

<p>The same issue is solved for the Python console, by using a <code>QPointer</code>. It would be great if you could submit a pull request that passes the ownership of the settings dialog similarly to how it is done for the Python console.</p>

---

## Post #4 by @keri (2022-03-19 00:44 UTC)

<p>Could please show where can I find Python console <code>QPointer</code> solution?<br>
I have an idea how to solve this with <code>QPointer</code> but don’t know anything about python console implementation yet.</p>

---

## Post #5 by @lassoan (2022-03-19 01:17 UTC)

<p>Search for <code>QPointer</code> and <code>PythonConsole</code> in the source and header files of the Slicer application classes.</p>

---

## Post #6 by @keri (2022-03-19 13:23 UTC)

<p>The <a href="https://github.com/Slicer/Slicer/pull/6275" rel="noopener nofollow ugc">PR is ready</a></p>

---
