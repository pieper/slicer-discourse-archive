---
topic_id: 6738
title: "Build Error Linux Related To Introduction Of Slicer Build We"
date: 2019-05-09
url: https://discourse.slicer.org/t/6738
---

# Build error linux related to introduction of Slicer_BUILD_WEBENGINE_SUPPORT option

**Topic ID**: 6738
**Date**: 2019-05-09
**URL**: https://discourse.slicer.org/t/build-error-linux-related-to-introduction-of-slicer-build-webengine-support-option/6738

---

## Post #1 by @gcsharp (2019-05-09 16:46 UTC)

<p>Build failure in clean build directory.</p>
<pre><code>CMakeFiles/qMRMLWidgets.dir/qMRMLLayoutManager.cxx.o: In function `qMRMLLayoutChartViewFactory::qMRMLLayoutChartViewFactory(QObject*)':
qMRMLLayoutManager.cxx:(.text+0x7b0): undefined reference to `vtable for qMRMLLayoutChartViewFactory'
CMakeFiles/qMRMLWidgets.dir/qMRMLLayoutManager.cxx.o: In function `qMRMLLayoutManager::setMRMLColorLogic(vtkMRMLColorLogic*)':
qMRMLLayoutManager.cxx:(.text+0x4c74): undefined reference to `qMRMLLayoutChartViewFactory::staticMetaObject'
CMakeFiles/qMRMLWidgets.dir/qMRMLLayoutManager.cxx.o: In function `qMRMLLayoutManager::mrmlColorLogic() const':
qMRMLLayoutManager.cxx:(.text+0x4d3f): undefined reference to `qMRMLLayoutChartViewFactory::staticMetaObject'
collect2: error: ld returned 1 exit status
Libs/MRML/Widgets/CMakeFiles/qMRMLWidgets.dir/build.make:3695: recipe for target 'bin/libqMRMLWidgets.so' failed
</code></pre>
<p>Looking at qMRMLWidgetsConfigure.h, I get:</p>
<pre><code>#define MRML_WIDGETS_HAVE_QT5
#define MRML_WIDGETS_HAVE_WEBGINE_SUPPORT</code></pre>

---

## Post #2 by @brhoom (2019-05-09 17:45 UTC)

<p>Please provide more information. What Linux are you using and which version? which Slicer version are you building? Did you install all required dependencies?</p>

---

## Post #3 by @lassoan (2019-05-09 18:04 UTC)

<p>Does your Qt have WebEngine component enabled?</p>

---

## Post #4 by @gcsharp (2019-05-09 19:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  Yes.  The following are installed: qtwebengin5-dev, libqt5webengine-data, libqt5webengine5, libqt5webenginewidgets5, libqt5webenginecore5.<br>
<a class="mention" href="/u/brhoom">@brhoom</a> This is debian stable, and HEAD.</p>

---

## Post #5 by @lassoan (2019-05-09 19:21 UTC)

<p>Is this the latest master version? There were a few days recently when there were build similar errors but <a class="mention" href="/u/jcfr">@jcfr</a> fixed those. You can also try disabling <code>Slicer_BUILD_WEBENGINE_SUPPORT</code> to skip all webengine related components (extension manager and the legacy chart view will not be available, but everything else should work; and the Slicer package will be 100-150MB smaller).</p>

---

## Post #6 by @jcfr (2019-05-09 19:45 UTC)

<p>If you are toggled <code>Slicer_BUILD_WEBENGINE_SUPPORT</code> ON and OFF in an existing build tree, you may have to delete the following files from the inner build tree, reconfigure and build the inner project:</p>
<pre><code class="lang-auto">./Libs/MRML/Widgets/moc_qMRMLLayoutManager.cpp_parameters
./Libs/MRML/Widgets/moc_qMRMLLayoutManager_p.cpp
./Libs/MRML/Widgets/moc_qMRMLLayoutManager.cpp
./Libs/MRML/Widgets/moc_qMRMLLayoutManager_p.cpp_parameters
</code></pre>

---

## Post #7 by @gcsharp (2019-05-09 20:16 UTC)

<p>Yes, I am at HEAD of master branch.  Disabling <code>Slicer_BUILD_WEBENGINE_SUPPORT</code> allows the build to complete, thank you.</p>
<p>I looked through the source a bit, but did not find any obvious difference between, say, qMRMLLayoutChartViewFactory and qMRMLLayoutThreeDViewFactory.  But it seems only the former is giving undefined symbols.</p>

---

## Post #8 by @jcfr (2019-05-09 20:27 UTC)

<p>This should help address the issue. See <a href="https://github.com/Slicer/Slicer/pull/1137" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/1137</a></p>

---

## Post #9 by @jcfr (2019-05-23 02:17 UTC)

<p>To follow up, fixes have been integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28262" rel="nofollow noopener">r28262</a> and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28263" rel="nofollow noopener">r28263</a></p>

---

## Post #10 by @gcsharp (2019-05-28 17:25 UTC)

<p>Fix confirmed.  Thanks Jc!</p>

---
