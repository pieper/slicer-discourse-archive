---
topic_id: 11355
title: "Cannot Found Attribute Vtkmrmlsegmenteditornode"
date: 2020-04-29
url: https://discourse.slicer.org/t/11355
---

# Cannot found attribute 'vtkMRMLSegmentEditorNode'

**Topic ID**: 11355
**Date**: 2020-04-29
**URL**: https://discourse.slicer.org/t/cannot-found-attribute-vtkmrmlsegmenteditornode/11355

---

## Post #1 by @quabug (2020-04-29 20:54 UTC)

<p>I’ve compile and running the latest version “06e327” of slicer on Mac.<br>
But there’s always an error when I ‘Switch to module:  “SegmentEditor”’, and no tool icons show’s up under panel of “Help &amp; Acknowlegement”.<br>
Traceback (most recent call last):<br>
File “/Users/quabug/proj/slicer/cmake-build-debug/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/SegmentEditor.py”, line 130, in enter<br>
self.selectParameterNode()<br>
File “/Users/quabug/proj/slicer/cmake-build-debug/Slicer-build/lib/Slicer-4.11/qt-scripted-modules/SegmentEditor.py”, line 86, in selectParameterNode<br>
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
AttributeError: module ‘slicer’ has no attribute ‘vtkMRMLSegmentEditorNode’</p>
<p>Is there something I’m missing during compile?<br>
mac 10.15.4<br>
qt 5.14.2 from brew</p>

---

## Post #2 by @lassoan (2020-04-29 20:55 UTC)

<p>It seems that your build did not succeed. Start a build in Slicer-build folder and see if there are any error messages.</p>

---

## Post #3 by @quabug (2020-04-30 12:12 UTC)

<p>There’s no error while building slicer in <code>Slicer-build</code>.<br>
And just few irrelevant warnings on building the whole project.</p>
<p>I’ve tested 3 different cmake config today, they all have this issue.</p>
<pre><code class="lang-auto"># CLion debug
cmake -DCMAKE_BUILD_TYPE=Debug -DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 -DQt5_DIR=/usr/local/Cellar/qt/5.14.2/lib/cmake/Qt5 -G "CodeBlocks - Unix Makefiles" /Users/quabug/proj/slicer
</code></pre>
<pre><code class="lang-auto"># CLion release
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 -DQt5_DIR=/usr/local/Cellar/qt/5.14.2/lib/cmake/Qt5 -G "CodeBlocks - Unix Makefiles" /Users/quabug/proj/slicer
</code></pre>
<pre><code class="lang-auto"># ccmake
ccmake -DCMAKE_OSX_DEPLOYMENT_TARGET=10.15 -DQt5_DIR=/usr/local/Cellar/qt/5.14.2/lib/cmake/Qt5 ../
</code></pre>
<pre><code class="lang-auto"># build command
SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk cmake --build . --target Slicer -- -j 16
</code></pre>
<p>cmake 3.17.1</p>
<p>I am gonna test recommend version of QT next, and will update the result after testing.</p>

---

## Post #4 by @quabug (2020-05-05 12:08 UTC)

<p>Nevermind, I am able to build windows version without any issue, and my target platform is windows, so would not bother mac anymore.</p>

---
