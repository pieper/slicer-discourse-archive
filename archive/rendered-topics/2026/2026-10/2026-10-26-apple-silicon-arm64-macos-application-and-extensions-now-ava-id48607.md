---
topic_id: 48607
title: "Apple Silicon (arm64 macOS) application and extensions now available"
date: 2026-10-26
url: https://discourse.slicer.org/t/48607
last_bumped: 2026-10-28T02:48:46.806Z
---

# Apple Silicon (arm64 macOS) application and extensions now available

**Topic ID**: 48607
**Date**: 2026-10-26
**URL**: https://discourse.slicer.org/t/apple-silicon-arm64-macos-application-and-extensions-now-available/48607

---

## Post #1 by @Sam_Horvath (2026-10-26 16:25 UTC)

<p>The Apple Silicon installer for 3D Slicer is now available for preview builds on <a href="https://download.slicer.org/">https://download.slicer.org/</a>. A stable arm64 package will be available in the next release.</p>
<p>Please give it a try and report any issues!</p>

---

## Post #2 by @Philipp_G (2026-10-27 20:34 UTC)

<p>I installed it on m1 mac mini macos 27.2, Rosetta installed. I as far as allowing the app to run through privacy settings, entering password, but after that the app crashes. launching again shows the splash screen, a couple of things load, then again crash. I useful I can post the crash report.</p>

---

## Post #3 by @Sam_Horvath (2026-10-27 20:57 UTC)

<p>Yes, please post the crash report.</p>

---

## Post #4 by @russellmiller49 (2026-10-28 02:48 UTC)

<p>I’m experiencing what appears to be the same issue with the new native Apple Silicon preview build.</p>
<p><strong>System:</strong></p>
<ul>
<li>
<p>3D Slicer: 5.13.0 (2026-10-26), ARM64 native</p>
</li>
<li>
<p>macOS: 27.2 (build 26B118)</p>
</li>
<li>
<p>Mac hardware identifier: Mac17,6</p>
</li>
<li>
<p>Bundled Qt version: 6.11.1</p>
</li>
</ul>
<p>Slicer displays its splash screen and begins loading, but crashes consistently before the main window appears.</p>
<p><strong>Crash report:</strong></p>
<ul>
<li>
<p>Exception: <code>EXC_BREAKPOINT (SIGTRAP)</code></p>
</li>
<li>
<p>Crashed thread: 0 (main thread)</p>
</li>
<li>
<p>Error: <code>pointer authentication trap DA</code></p>
</li>
</ul>
<p>Relevant stack trace:</p>
<pre><code class="lang-auto">CoreFoundation  __CF_IS_OBJC
CoreFoundation  CFGetTypeID
CoreGraphics   CGColorSpaceGetType
CoreGraphics   valid_image_colorspace
CoreGraphics   verify_image_parameters
CoreGraphics   CGImageCreate
QtGui          QImage::toCGImage()
QtGui          imageFromQIcon
libqcocoa      QCocoaMenuItem::sync()
QtWidgets      QMenu::actionEvent()
Slicer         qSlicerMainWindowPrivate::setupUi()
</code></pre>
<p>I investigated the crash and found that it closely matches <strong>QTBUG-147602</strong>, a use-after-free bug in Qt 6.11.1 affecting <code>QImage::toCGImage()</code> on macOS. The same failure has been reported in other Qt applications, including OBS Studio, on macOS 27.2.</p>
<p>The upstream Qt issue was reportedly fixed in Qt 6.11.2 and 6.12.0.</p>
<p>Since this Slicer preview bundles Qt 6.11.1, I suspect the same issue is responsible for the crash. Would it be possible to incorporate the upstream Qt fix or update the bundled Qt version in the next ARM64 preview?</p>
<p>I’ve attached my complete macOS crash report for reference as Gist here: <a href="https://gist.github.com/russellmiller49/f4c0d0871139561384afbc61828a5d0f#file-slicer-arm64-crash-2026-10-27" class="inline-onebox" rel="noopener nofollow ugc">slicer-arm64-crash-2026-10-27 · GitHub</a></p>
<p>Thanks for making the native Apple Silicon build available!</p>

---
