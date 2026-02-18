# Problem with Segmentation UNet

**Topic ID**: 34923
**Date**: 2024-03-16
**URL**: https://discourse.slicer.org/t/problem-with-segmentation-unet/34923

---

## Post #1 by @LeidyMoraV (2024-03-16 11:39 UTC)

<p>Hello,<br>
I’m new working with PLUS and sliceIGT and I’m trying to follow the tutorial: <a href="https://www.youtube.com/watch?v=l0BcW8c9CnI" rel="noopener nofollow ugc">Tracked ultrasound AI segmentation and 3D reconstruction tutorial - YouTube</a><br>
But after adding the py file the ‘Ultrasound’  &gt; ‘SegmentationUNet’ doesn’t appear in the menu bar of Slicer.</p>

---

## Post #2 by @lassoan (2024-03-17 00:29 UTC)

<p>The tutorial was created 2 years ago. Many things have changed since then, so you might need to make some small changes. What errors appear in the Python console in Slicer?</p>

---

## Post #3 by @LeidyMoraV (2024-03-17 22:10 UTC)

<pre><code class="lang-auto">Python 3.9.10 (main, Dec 12 2023, 02:25:18) [MSC v.1935 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
[Qt] Error #1 while writing setting "Modules/AdditionalPaths"
[Qt] Error #1 while writing setting "Modules/IgnoreModules"
[Qt] Error #1 while writing setting "Extensions/ManagerEnabled"
[Qt] Error #1 while writing setting "Extensions/ServerUrl"
[Qt] Error #1 while writing setting "Extensions/FrontendServerUrl"
[Qt] Error #1 while writing setting "Extensions/InstallPath"
[Qt] QWindowsWindow::setGeometry: Unable to set geometry 1377x705+0+23 (frame: 1393x744-8-8) on QWidgetWindow/"qSlicerMainWindowWindow" on "\\.\DISPLAY1". Resulting geometry: 1366x705+0+23 (frame: 1382x744-8-8) margins: 8, 31, 8, 8 minimum size: 1377x396 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=1393,435 maxtrack=0,0)
[Qt] Error #1 while writing setting "Modules/AdditionalPaths"
[Qt] Error #1 while writing setting "Modules/IgnoreModules"
[Qt] Error #1 while writing setting "Extensions/FrontendServerUrl"
[Qt] Error #1 while writing setting "Extensions/InstallPath"
[Qt] Error #1 while writing setting "Extensions/ManagerEnabled"
[Qt] Error #1 while writing setting "Extensions/ServerUrl"

</code></pre>

---

## Post #5 by @LeidyMoraV (2024-03-18 14:00 UTC)

<p>I’ve used the <code>Ctrl+G</code> command and loaded the py file, but I get this error:</p>
<pre><code class="lang-auto"> Traceback (most recent call last):
  File "&lt;string&gt;", line 303, in &lt;module&gt;
NameError: name 'Process' is not defined
</code></pre>
<p>Also I’ve tried running the 3D Slicer as an administrator but then I can’t drag the py extension file</p>

---
