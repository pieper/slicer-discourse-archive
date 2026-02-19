---
topic_id: 45235
title: "Specific Reason For Using Winmain Instead Of Main"
date: 2025-11-26
url: https://discourse.slicer.org/t/45235
---

# Specific reason for using WinMain instead of main?

**Topic ID**: 45235
**Date**: 2025-11-26
**URL**: https://discourse.slicer.org/t/specific-reason-for-using-winmain-instead-of-main/45235

---

## Post #1 by @codeling (2025-11-26 10:56 UTC)

<p>I just discovered that Slicer is using <code>int __stdcall WinMain(…)</code> on Windows (basically since forever, as far as I can tell).</p>
<p>From what I can tell, WinMain is just a wrapper making it easier <em>for Windows-targeted development</em>; one could just as well use the standard <code>int main(…)</code>instead, such as <a href="https://code.qt.io/cgit/qt/qtbase.git/tree/examples/widgets/mainwindows/menus/main.cpp?h=6.10" rel="noopener nofollow ugc">the official Qt examples do</a>. Since this would simplify code quite a bit - basically <a href="https://github.com/Slicer/Slicer/blob/main/Base/QTApp/qSlicerApplicationMainWrapper.cxx#L24-L51" rel="noopener nofollow ugc">all Windows-specific code in qSlicerApplicationMainWrapper.cxx</a> could be removed - is there a specific reason why <code>WinMain</code> should be kept?</p>

---
