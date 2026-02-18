# Qt5 build recompiles on Linux?

**Topic ID**: 1542
**Date**: 2017-11-27
**URL**: https://discourse.slicer.org/t/qt5-build-recompiles-on-linux/1542

---

## Post #1 by @chir.set (2017-11-27 18:26 UTC)

<p>[split from <a href="https://discourse.slicer.org/t/nightly-binaries-qt5-vtk9/1531">Nightly binaries Qt5/VTK9?</a>]</p>
<hr>
<p>How would Qt5 library version be managed on Linux ? From 5.9.2 to 5.9.3, I had to recompile, Qt says ‘mismatch version’ otherwise. This was not a problem for no longer developed Qt4.</p>

---

## Post #2 by @lassoan (2017-11-28 03:24 UTC)

<aside class="quote no-group quote-modified" data-username="chir.set" data-post="2" data-topic="1531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"><a href="https://discourse.slicer.org/t/nightly-binaries-qt5-vtk9/1531/2">Nightly binaries Qt5/VTK9?</a></div>
<blockquote>
<p>How would Qt5 library version be managed on Linux ? From 5.9.2 to 5.9.3, I had to recompile,</p>
</blockquote>
</aside>
<p>What do you mean?<br>
What did you have to recompile?</p>

---

## Post #3 by @chir.set (2017-11-28 11:20 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="4" data-topic="1531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/nightly-binaries-qt5-vtk9/1531/4">Nightly binaries Qt5/VTK9?</a></div>
<blockquote>
<p>What did you have to recompile?</p>
</blockquote>
</aside>
<p>On switching from Qt 5.9.1 to 5.9.2, and from 5.9.2 to 5.9.3 through system upgrade on Arch Linux, I had to recompile Slicer. Slicer compiled with one version of Qt won’t run with the next version. AFAICT, Slicer does not ship Qt binaries, but relies on system Qt libraries on Linux. The Qt4 libraries have been stable for years, Qt5 is ongoing development. It seems to me that Slicer may have to include Qt binaries against which it was compiled. I don’t know if there are special configuration switches that would allow cross-version application execution.</p>

---

## Post #4 by @lassoan (2017-11-28 12:23 UTC)

<p>Slicer install package includes Qt libraries. You only need to rebuild Slicer if you’ve built it yourself and chose to use system Qt for the build.</p>

---

## Post #5 by @chir.set (2017-11-28 13:40 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="6" data-topic="1531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/nightly-binaries-qt5-vtk9/1531/6">Nightly binaries Qt5/VTK9?</a></div>
<blockquote>
<p>Slicer install package includes Qt libraries.</p>
</blockquote>
</aside>
<p>OK. Just found they are in lib/Slicer-4.9/ from the downloaded package, and also in  the self compiled one. Just added a working LD_LIBRARY_PATH in my startup script. Nice hint, thanks.</p>

---

## Post #6 by @lassoan (2017-11-28 13:53 UTC)

<p>If you start the application with the Slicer executable (the “launcher”) then it should set up LD_LIBRARY_PATH to include all necessary folders and then it starts SlicerApp-real executable.</p>

---

## Post #7 by @chir.set (2017-11-28 14:25 UTC)

<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="8" data-topic="1531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/nightly-binaries-qt5-vtk9/1531/8">Nightly binaries Qt5/VTK9?</a></div>
<blockquote>
<p>start the application with the Slicer executable (the “launcher”)</p>
</blockquote>
</aside>
<p>That’s what I do since years :</p>
<blockquote>
<p>export LC_NUMERIC=C<br>
$HOME/bin/Slicer4/Slicer</p>
</blockquote>
<p>where Slicer4 is a symlink.</p>
<p>I booted on a partition with Qt5 5.9.1 and Failed to run Slicer built with 5.9.3 :</p>
<blockquote>
<p>#[user@vasc2 ~][0]$ export LC_NUMERIC=C<br>
#[user@vasc2 ~][0]$ bin/Slicer4/Slicer<br>
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
Qt WebEngine ICU data not found at /usr/share/qt/resources. Trying parent directory…<br>
Qt WebEngine ICU data not found at /usr/share/qt. Trying application directory…<br>
Qt WebEngine ICU data not found at /home/user/bin/Slicer-4.9.0-2017-11-23-linux-amd64/bin. Trying fallback directory… The application MAY NOT work.<br>
Path override failed for key base::DIR_QT_LIBRARY_DATA and path ‘/home/user/.Slicer’<br>
[1128/151322.965258:ERROR:icu_util.cc(178)] Invalid file descriptor to ICU data received.<br>
error: [/home/user/bin/Slicer4/bin/SlicerApp-real] exit abnormally - Report the problem.<br>
#[user@vasc2 ~][1]$ export LD_LIBRARY_PATH=/home/user/bin/Slicer4/lib/Slicer-4.9<br>
#[user@vasc2 ~][0]$ bin/Slicer4/Slicer<br>
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.<br>
Qt WebEngine ICU data not found at /usr/share/qt/resources. Trying parent directory…<br>
Qt WebEngine ICU data not found at /usr/share/qt. Trying application directory…<br>
Qt WebEngine ICU data not found at /home/user/bin/Slicer-4.9.0-2017-11-23-linux-amd64/bin. Trying fallback directory… The application MAY NOT work.<br>
Path override failed for key base::DIR_QT_LIBRARY_DATA and path ‘/home/user/.Slicer’<br>
[1128/151443.117284:ERROR:icu_util.cc(178)] Invalid file descriptor to ICU data received.<br>
error: [/home/user/bin/Slicer4/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>

---

## Post #8 by @lassoan (2017-11-28 20:53 UTC)

<p>If you build Slicer using system Qt then you need to rebuild Slicer if you update system Qt (maybe not needed for some small patch updates). If you build using your own Qt or use a pre-built binary package then upgrading system Qt has no effect on your Slicer builds. If you find that you build your own Qt and Slicer still uses system Qt then it’s probably a launcher configuration error and it will be addressed when Slicer nightly will switch to Qt5 (in a few weeks).</p>

---
