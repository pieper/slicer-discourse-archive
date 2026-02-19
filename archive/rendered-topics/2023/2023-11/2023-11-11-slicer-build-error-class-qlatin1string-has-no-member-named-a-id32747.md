---
topic_id: 32747
title: "Slicer Build Error Class Qlatin1String Has No Member Named A"
date: 2023-11-11
url: https://discourse.slicer.org/t/32747
---

# Slicer build error - ‘class QLatin1String’ has no member named ‘arg’de

**Topic ID**: 32747
**Date**: 2023-11-11
**URL**: https://discourse.slicer.org/t/slicer-build-error-class-qlatin1string-has-no-member-named-arg-de/32747

---

## Post #1 by @Ankit_Mishra (2023-11-11 18:48 UTC)

<p>/home/ankit/Slicer/Base/QTGUI/qSlicerExtensionsLocalWidget.cxx: In member function ‘void {anonymous}::qSlicerExtensionsDescriptionLabel::labelText(const QString&amp;)’:<br>
/home/ankit/Slicer/Base/QTGUI/qSlicerExtensionsLocalWidget.cxx:431:84: error: ‘class QLatin1String’ has no member named ‘arg’<br>
431 | g style="float: left" src=":/Icons/ExtensionIncompatible.svg"/&gt; ").arg(this-&gt;WarningColor) +<br>
|                                                                        ^~~</p>
<p>make[5]: *** [Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/build.make:1269: Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/qSlicerExtensionsLocalWidget.cxx.o] Error 1<br>
make[4]: *** [CMakeFiles/Makefile2:9810: Base/QTGUI/CMakeFiles/qSlicerBaseQTGUI.dir/all] Error 2<br>
make[3]: *** [Makefile:163: all] Error 2<br>
make[2]: *** [CMakeFiles/Slicer.dir/build.make:143: Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2<br>
make[1]: *** [CMakeFiles/Makefile2:196: CMakeFiles/Slicer.dir/all] Error 2<br>
make: *** [Makefile:95: all] Error 2</p>

---

## Post #2 by @pieper (2023-11-11 21:32 UTC)

<aside class="quote no-group" data-username="Ankit_Mishra" data-post="1" data-topic="32747">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ankit_mishra/48/68271_2.png" class="avatar"> Ankit_Mishra:</div>
<blockquote>
<p>QLatin1String</p>
</blockquote>
</aside>
<p>That’s from using an older version of Qt, since <a href="https://doc.qt.io/qt-5/qlatin1string.html#arg">that method</a> was introduced in 5.14.  Updating to 5.15 is recommended.</p>

---
