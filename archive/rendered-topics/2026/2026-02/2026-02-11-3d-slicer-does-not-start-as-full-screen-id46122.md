# 3D Slicer does not start as full screen

**Topic ID**: 46122
**Date**: 2026-02-11
**URL**: https://discourse.slicer.org/t/3d-slicer-does-not-start-as-full-screen/46122

---

## Post #1 by @strider_hunter (2026-02-11 08:39 UTC)

<p>When I startup up 3D Slicer, instead of occupying the full screen, it only occupies a smaller section (as seen in the screenshot below). I have a multi-monitor setup.</p>
<p>I looked at a `.ini` files like</p>
<ul>
<li><a href="http://slicer.org" rel="noopener nofollow ugc">slicer.org</a>\Slicer-34045.ini</li>
<li>bin\SlicerLauncherSettings.ini</li>
<li>bin\SlicerDesignerLauncherSettings.ini</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2d4bc833bc9a1f72a507737879555cc6ac7579e.png" data-download-href="/uploads/short-url/net8q0NDeXjwnVo1VUqh8HMPX4O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2d4bc833bc9a1f72a507737879555cc6ac7579e_2_690x377.png" alt="image" data-base62-sha1="net8q0NDeXjwnVo1VUqh8HMPX4O" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2d4bc833bc9a1f72a507737879555cc6ac7579e_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2d4bc833bc9a1f72a507737879555cc6ac7579e_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a2d4bc833bc9a1f72a507737879555cc6ac7579e_2_1380x754.png 2x" data-dominant-color="959495"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1914×1048 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e73e45fcefb8e3c140084b766cf0262ee7383c4b.png" data-download-href="/uploads/short-url/wZFInwJ8pEPnki8mBjRoT4UGCSL.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e73e45fcefb8e3c140084b766cf0262ee7383c4b.png" alt="image" data-base62-sha1="wZFInwJ8pEPnki8mBjRoT4UGCSL" width="690" height="286" data-dominant-color="202B33"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">952×395 6.01 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Side note: I do have a custom extension(<code>ScriptedLoadableModuleWidget</code>) that when activated gives me errors lke this</p>
<pre><code class="lang-auto">QWindowsWindow::setGeometry: Unable to set geometry 1970x1009+1280-26 (frame: 1986x1048+1272-57) on QWidgetWindow/"qSlicerMainWindowWindow" on "\\\\.\\DISPLAY1". Resulting geometry: 1920x1009+1280-26 (frame: 1936x1048+1272-57) margins: 8, 31, 8, 8 minimum size: 1970x393 MINMAXINFO maxSize=0,0 maxpos=0,0 mintrack=1986,432 maxtrack=0,0)
</code></pre>
<p>I even got a suggestion to look at <code>HKEY_CURRENT_USER\Software\slicer.org\slicer.org\</code>, but I did not find anything there.</p>
<p>Finally, I have noticed that ever since I have this small window, my Slicer also crashes unexpectedly and there is nothing in the logs (<code>AppData\Local\Temp\Slicer\*.log</code>) that indicates why.</p>

---
