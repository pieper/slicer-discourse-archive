# `import dicom` resolves differently across platforms

**Topic ID**: 4072
**Date**: 2018-09-11
**URL**: https://discourse.slicer.org/t/import-dicom-resolves-differently-across-platforms/4072

---

## Post #1 by @fedorov (2018-09-11 16:46 UTC)

<p>It appears that <code>import dicom</code> works inconsistently across platforms, perhaps this is due to runtime load ordering issues:</p>
<p>mac (resolves to pydicom):</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import dicom
&gt;&gt;&gt; print dicom
&lt;module 'dicom' from '/Applications/Slicer.app/Contents/lib/Python/lib/python2.7/
  site-packages/dicom/__init__.pyc'&gt;
</code></pre>
<p>linux (resolves to Slicer DICOM module):</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import dicom
&gt;&gt;&gt; print dicom
&lt;module 'dicom' from '/media/psf/Home/Slicer-4.9.0-2018-09-10-linux-amd64/lib/
</code></pre>
<p>Anyone has a workaround for this problem?</p>

---

## Post #2 by @jcfr (2018-09-11 18:05 UTC)

<p>I suspect this happens on case-insensitive filesystem.</p>
<p>If this is the case:</p>
<ul>
<li>switch to case sensistive filesystem<br>
or</li>
<li>rename faulty module to have different name</li>
</ul>

---

## Post #3 by @fedorov (2018-09-11 18:32 UTC)

<p>Thank you JC, this indeed appears to have been the case. I was using Parallels, and installed Slicer on a mounted volume. The file names were not showing up as case-insensitive in the file browser, but apparently this was the issue. After I installed Slicer in a local FS Parallels folder, things returned back to normal.</p>

---

## Post #4 by @pieper (2018-09-11 19:23 UTC)

<p>Do we have documentation anywhere saying that a case sensitive file system is suggested?  Maybe we should have a small test that runs on startup and warns if a case-insensitive file system is detected.</p>

---

## Post #5 by @jcfr (2018-09-11 19:48 UTC)

<blockquote>
<p>a small test that runs on startup and warns if a case-insensitive file system is detected.</p>
</blockquote>
<p>Great idea</p>
<p>For the buildsystem, what about:</p>
<pre><code class="lang-auto">file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/TestCaseSensitiveFileSystem.txt" "1")
file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/Testcasesensitivefilesystem.txt" "0")
file(READ "${CMAKE_CURRENT_BINARY_DIR}/TestCaseSensitiveFileSystem.txt" is_case_sensitive_filesystem)
if(NOT is_case_sensitive_filesystem)
  message(FATAL_ERROR "")
endif()
</code></pre>
<p>and for the runtime, we could do similar test in C++ or python. Or use an existing system call  …</p>

---

## Post #6 by @jcfr (2018-09-11 19:55 UTC)

<p>And to clarify, I would be happy to review a pull-request if someone want to implement such configure and/or runtime test</p>

---

## Post #7 by @jcfr (2018-09-11 21:31 UTC)

<p>For reference, here is the corresponding Slicer issue: <a href="https://issues.slicer.org/view.php?id=4606">https://issues.slicer.org/view.php?id=4606</a></p>

---

## Post #8 by @lassoan (2018-09-11 21:52 UTC)

<p>Windows uses case-insensitive file system, topic. Why it is not a problem there (it imports pydicom)?</p>
<p>Both Slicer’s DICOM module and pydicom is very brave to claim such a generic word as “dicom” for its name, but especially pydicom, as a Python package, it should have chosen a more specific name. Anyway, we cannot expect pydicom to be renamed, so should we change the Slicer module name? Maybe to DICOMBrowser?</p>

---

## Post #9 by @pieper (2018-09-11 22:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="4072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>we cannot expect pydicom to be renamed,</p>
</blockquote>
</aside>
<p>It was <a href="https://pydicom.github.io/pydicom/stable/transition_to_pydicom1.html">just renamed for the 1.0 release</a> - dicom now it’s pydicom.</p>
<p>But the whole thing does seem very fragile.  Isn’t there some other way to namespace these things?  Like what if someone decides to name their python package slicer?  (guess we should grab that one).</p>

---

## Post #10 by @jcfr (2018-09-11 22:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="4072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe to DICOMBrowser?</p>
</blockquote>
</aside>
<p>That makes sense. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #11 by @jcfr (2018-09-11 23:47 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="4072">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Windows uses case-insensitive file system, topic. Why it is not a problem there (it imports pydicom)?</p>
</blockquote>
</aside>
<p>Good point. There are no problem on windows. See experiment below.</p>
<p>That said, the path containing <code>DICOM.py</code> is indeed listed first in <code>sys.path</code></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd.png" data-download-href="/uploads/short-url/sUa6GKbqSu82etuyk1AhUZDNuQB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd_2_690x217.png" alt="image" data-base62-sha1="sUa6GKbqSu82etuyk1AhUZDNuQB" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd_2_690x217.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd.png 2x" data-dominant-color="EBF5EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">921×290 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I suspect that the function listing files in a directory on a case insensitive macOS always return lower case files whereas on windows the case is maintained in the listing.</p>
<p>Also worth noting that <code>~/.local/lib/python2.7</code> is  listed … more on that below.</p>
<h2><a name="p-15451-import-of-dicom-vs-dicom-macos-linux-window-installed-slicer-from-sept-11-r27399-1" class="anchor" href="#p-15451-import-of-dicom-vs-dicom-macos-linux-window-installed-slicer-from-sept-11-r27399-1" aria-label="Heading link"></a>import of dicom vs DICOM / macOS, Linux, Window / Installed Slicer from Sept 11 (r27399)</h2>
<h3><a name="p-15451-windows-2" class="anchor" href="#p-15451-windows-2" aria-label="Heading link"></a>Windows</h3>
<p>Here is what happen using the latest windows nightly build:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7da425ac94f5033bcdc893b230671a54633506a7.png" data-download-href="/uploads/short-url/hVtmMBPlzhxqQEZ5s0FU8JRXOx9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7da425ac94f5033bcdc893b230671a54633506a7_2_690x72.png" alt="image" data-base62-sha1="hVtmMBPlzhxqQEZ5s0FU8JRXOx9" width="690" height="72" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7da425ac94f5033bcdc893b230671a54633506a7_2_690x72.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7da425ac94f5033bcdc893b230671a54633506a7_2_1035x108.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7da425ac94f5033bcdc893b230671a54633506a7.png 2x" data-dominant-color="F3F8F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1345×142 57.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The two paths are:</p>
<ul>
<li><code>lib/Python/Lib/site-packages/dicom</code>  (which contains <code>__init__.py</code>)</li>
<li><code>lib/Slicer-4.9/qt-scripted-modules</code>   (which contains <code>DICOM.py</code>)</li>
</ul>
<h3><a name="p-15451-linux-3" class="anchor" href="#p-15451-linux-3" aria-label="Heading link"></a>Linux</h3>
<p>On linux, using the latest nightly, we have:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import dicom
&gt;&gt;&gt; dicom.__file__
'/home/jcfr/Downloads/Slicer-4.9.0-2018-09-10-linux-amd64/lib/Python/lib/python2.7/site-packages/dicom/__init__.pyc'
&gt;&gt;&gt; import DICOM
&gt;&gt;&gt; DICOM.__file__
'/home/jcfr/Downloads/Slicer-4.9.0-2018-09-10-linux-amd64/bin/../lib/Slicer-4.9/qt-scripted-modules/DICOM.pyc'
</code></pre>
<p>The two paths are also:</p>
<ul>
<li><code>lib/Python/lib/python2.7/site-packages/dicom</code></li>
<li><code>lib/Slicer-4.9/qt-scripted-modules</code></li>
</ul>
<h3><a name="p-15451-macos-4" class="anchor" href="#p-15451-macos-4" aria-label="Heading link"></a>macOS</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/716f40e06be509d57dda9498c34d096488ad98e9.png" data-download-href="/uploads/short-url/gbujrbmpwaJI1eX7dvUak1LpPNT.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/716f40e06be509d57dda9498c34d096488ad98e9_2_690x121.png" alt="image" data-base62-sha1="gbujrbmpwaJI1eX7dvUak1LpPNT" width="690" height="121" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/716f40e06be509d57dda9498c34d096488ad98e9_2_690x121.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/716f40e06be509d57dda9498c34d096488ad98e9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/716f40e06be509d57dda9498c34d096488ad98e9.png 2x" data-dominant-color="F1F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">717×126 39.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The two paths are also:</p>
<ul>
<li><code>lib/Python/lib/python2.7/site-packages/dicom</code></li>
<li><code>lib/Slicer-4.9/qt-scripted-modules</code></li>
</ul>
<p>Not sure what is happening .. it may be worth doing more experiment in that setup.</p>
<h2><a name="p-15451-pythonnousersite-seems-to-be-ignored-on-macos-5" class="anchor" href="#p-15451-pythonnousersite-seems-to-be-ignored-on-macos-5" aria-label="Heading link"></a>PYTHONNOUSERSITE seems to be ignored on macOS</h2>
<p>While looking at the issue, I printed the <code>sys.path</code> and we can see that the one containing <code>DICOM</code> is first.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd.png" data-download-href="/uploads/short-url/sUa6GKbqSu82etuyk1AhUZDNuQB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd_2_690x217.png" alt="image" data-base62-sha1="sUa6GKbqSu82etuyk1AhUZDNuQB" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd_2_690x217.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca96221859dbb26981ab8805e6fa1beadde45efd.png 2x" data-dominant-color="EBF5EB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">921×290 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @pieper (2018-09-12 12:41 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="11" data-topic="4072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Not sure what is happening … it may be worth doing more experiment in that setup.</p>
</blockquote>
</aside>
<p>Does that mac have a case-sensitive filesystem?</p>

---
