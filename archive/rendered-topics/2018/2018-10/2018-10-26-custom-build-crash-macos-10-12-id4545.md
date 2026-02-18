# Custom build crash - MacOS 10.12

**Topic ID**: 4545
**Date**: 2018-10-26
**URL**: https://discourse.slicer.org/t/custom-build-crash-macos-10-12/4545

---

## Post #1 by @dominicwhite (2018-10-26 16:07 UTC)

<p>I’ve been trying to build Slicer from source, but I keep running into the following error when running the build:</p>
<pre><code>2018-10-26 11:18:42.097 Slicer[1559:9595646] *** WARNING: Method userSpaceScaleFactor in class NSView is deprecated on 10.7 and later. It should not be used in new applications. Use convertRectToBacking: instead. 
Switch to module:  "Welcome"
Switch to module:  "Volumes"
ASSERT: "this-&amp;gt;Table-&amp;gt;rowHeight(i) == newHeight" in file /opt/S/CTK/Libs/Widgets/ctkMatrixWidget.cpp, line 252
error: [/opt/S/Slicer-build/bin/Slicer.app/Contents/MacOS/./Slicer] exit abnormally - Report the problem.
</code></pre>
<p>This happens whenever I switch to the Volumes module (with or without data loaded).</p>
<p>OS: MacOS Sierra 10.12.6<br>
XCode: Version 9.2 (9C40b)<br>
clang: Apple LLVM version 9.0.0 (clang-900.0.39.2)<br>
QT: 5.11.2<br>
Cmake: 3.12.3</p>
<p>Slicer: Nightly-master branch (4.11.0 2018-10-23)</p>
<p>My cmake command is<br>
cmake <br>
-DCMAKE_BUILD_TYPE:STRING=Debug <br>
-DQt5_DIR:PATH=/Users/whitede/Applications/Qt/5.11.2/clang_64/lib/cmake/Qt5 <br>
-DCMAKE_OSX_DEPLOYMENT_TARGET=10.12 <br>
-DSlicer_USE_GIT_PROTOCOL=OFF <br>
-DSlicer_USE_PYTHONQT_WITH_TCL=OFF <br>
/Users/whitede/MyProjects/Slicer</p>
<p>I’ve been trying various combinations of this all week without success. Is there a likely cause of this problem? Wrong version of QT? When I try to compile the master-48 branch, I get this error:</p>
<pre><code>In file included from /opt/Slicer/CTK-build/CTK-build/Libs/Widgets/moc_ctkPathListButtonsWidget_p.cpp:9:
/opt/Slicer/CTK/Libs/Widgets/ctkPathListButtonsWidget_p.h:60:49: error: unknown type name 'QItemSelection'
  void on_PathListWidget_selectionChanged(const QItemSelection&amp; selected, const QItemSelection&amp; deselected);</code></pre>

---

## Post #2 by @jcfr (2018-10-26 16:56 UTC)

<p>Thanks for detailed report. Could you create an issue report on: <a href="http://issues.slicer.org/">http://issues.slicer.org/</a> ? Summarizing the problem and including a link to this post will be enough.</p>
<p>Also waiting we address the issue, you could do a Release build and you shouldn’t have problem.</p>
<p>You can do a release build passing the following option to <code>cmake</code> when  configuring Slicer <code>-DCMAKE_BUILD_TYPE:STRING=Release</code>.</p>

---

## Post #3 by @leochan2009 (2019-10-31 20:17 UTC)

<p>The same issue happen to MacOS 10.15 SDK again</p>

---

## Post #4 by @lassoan (2019-11-01 02:48 UTC)

<p>The issue is fixed in recent CTK versions. Either build latest Slicer master or backport the <a href="https://github.com/commontk/CTK/commit/0e1d94593d900fd144f50af38e3240063ab30484">CTK fix</a> into CTK in your build tree.</p>

---
