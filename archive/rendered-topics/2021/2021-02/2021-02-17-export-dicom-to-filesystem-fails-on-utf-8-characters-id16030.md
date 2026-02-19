---
topic_id: 16030
title: "Export Dicom To Filesystem Fails On Utf 8 Characters"
date: 2021-02-17
url: https://discourse.slicer.org/t/16030
---

# Export DICOM to filesystem fails on UTF-8 characters

**Topic ID**: 16030
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/export-dicom-to-filesystem-fails-on-utf-8-characters/16030

---

## Post #1 by @chir.set (2021-02-17 09:55 UTC)

<p>Hi,</p>
<p>My environment’s locale is fr_FR.UTF-8, which does not always plays well with Slicer, rarely though.</p>
<p>While exporting DICOM series that have accented characters to filesystem, it fails on non-ascii characters as such:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80ad090f5c5b4dab68960637672673dc2ee2d595.png" alt="Screenshot_20210217_104325" data-base62-sha1="imjQfQuY1Wtpy9fe4gC5Smxs4p7" width="290" height="334"></p>
<blockquote>
<p>Failed to copy</p>
<source>
to
/tmp/Slicer/A10000711888-PATIENT_NAME/20210210-ANGIOSCANNER MEMBRE INF/201-Images trait�es/000000.dcm
Halting export
</blockquote>
<p>The directory &lt;201-Images traitées&gt; is created on storage.</p>
<p>I fear it’s an issue that can’t be resolved as it relates deeply to Slicer’s internals.</p>
<p>I’m posting here for any magic solution.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2021-02-17 11:33 UTC)

<p>Since you use UTF8 and latest Slicer Stable Release (or preview releases) uses UTF8 everywhere, there should be no problems with special characters.</p>
<p>What Slicer version and operating system do you use? Can you send the full application log?</p>

---

## Post #3 by @chir.set (2021-02-17 13:29 UTC)

<p>I have the same failure on self built and factory built Slicer on Arch Linux. Here is the application log from factory built :</p>
<blockquote>
<p>Session start time …: 2021-02-17 14:21:33<br>
Slicer version …: 4.13.0-2021-02-16 (revision 29713 / b691c46) linux-amd64 - installed release<br>
Operating system …: Linux / 5.10.15-arch1-1 / <span class="hashtag-raw">#1</span> SMP PREEMPT Wed, 10 Feb 2021 18:32:40 +0000 - 64-bit<br>
Memory …: 16006 MB physical, 16383 MB virtual<br>
CPU …: AuthenticAMD AMD Phenom™ II X6 1100T Processor, 6 cores, 6 logical processors<br>
VTK configuration …: OpenGL2 rendering, Sequential threading<br>
Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
Developer mode enabled …: yes<br>
Prefer executable CLI …: yes<br>
Application path …: /home/user/programs/Test/Slicer-4.13.0-2021-02-16-linux-amd64/bin<br>
Additional module paths …: (none)<br>
Reversing DICOM dictionary so can look up tag from a keyword…<br>
Scripted subject hierarchy plugin registered: Annotations<br>
Scripted subject hierarchy plugin registered: SegmentEditor<br>
Scripted subject hierarchy plugin registered: SegmentStatistics<br>
Switch to module:  “Volumes”<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
Assertion <code>this-&gt;Table-&gt;columnWidth(j) == newWidth</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  242<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  /work/Preview/Slicer-0-build/CTK/Libs/Widgets/ctkMatrixWidget.cpp  line  253<br>
Loading Slicer RC file [/home/user/.slicerrc.py]<br>
Switch to module:  “DICOM”</p>
</blockquote>
<p>Not much informative about the failure.</p>
<p>Anyway, I can do without this being fixed. AFAIK, core libraries like VTK, CTK, ITK and others do not expect non-asciii characters.</p>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2021-02-17 13:51 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="16030">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Anyway, I can do without this being fixed. AFAIK, core libraries like VTK, CTK, ITK and others do not expect non-asciii characters.</p>
</blockquote>
</aside>
<p>We build Slicer with UTF8 application code page on Windows, and UTF8 encoding is used on Linux and macOS by default already. So everything, including VTK, CTK, ITK works well with non-ASCII characters.</p>
<p>If your Linux or macOS system is set to a non-UTF8 locale then you need to restrict yourself to ASCII characters or switch the locale in the environment where you launch Slicer.</p>
<p>There is still an issue in Windows passing command-line arguments from a non-UTF8 terminal to a UTF8 application, but this should be resolved as Windows is gradually moving towards UTF8 everywhere.</p>
<p><strong>What is the output of <code>locale</code> command on your system (in a terminal)?</strong></p>
<p><strong>What is the output of this command in Slicer’s Python console?</strong></p>
<pre data-code-wrap="python"><code class="lang-python">localeCodec = qt.QTextCodec().codecForLocale()
print(localeCodec.toUnicode(localeCodec.name()))
</code></pre>
<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="16030">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>Not much informative about the failure.</p>
</blockquote>
</aside>
<p>I meant the application log of a failed DICOM export. It may contain useful information - most importantly what and where exactly logged the error.</p>

---

## Post #5 by @lassoan (2021-02-17 20:38 UTC)

<p><strong>Update:</strong> I’ve found that there is an intentional stripping of special characters in the CTK DICOM exporter:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/f670e1d0e513bae9d08257b883aaf669f546053d/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L1338" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/f670e1d0e513bae9d08257b883aaf669f546053d/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L1338" target="_blank" rel="noopener">commontk/CTK/blob/f670e1d0e513bae9d08257b883aaf669f546053d/Libs/DICOM/Widgets/ctkDICOMBrowser.cpp#L1338</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="1328" style="counter-reset: li-counter 1327 ;">
<li>destinationDir += sep + seriesNumber;</li><li>if (!seriesDescription.isEmpty())</li><li>{</li><li>  destinationDir += nameSep + seriesDescription;</li><li>}</li><li>destinationDir += sep;</li><li></li><li>// make sure only ascii characters are in the directory path</li><li>// (while special characters may be used on an internal hard disk, it may not be possible</li><li>// to use special characters on file systems of an external drive or network storage)</li><li class="selected">destinationDir = QString::fromLatin1(destinationDir.toLatin1());</li><li>// replace any question marks that were used as replacements for non ascii</li><li>// characters with underscore</li><li>destinationDir.replace("?", "_");</li><li></li><li>// create the destination directory if necessary</li><li>if (!QDir().exists(destinationDir))</li><li>{</li><li>  if (!QDir().mkpath(destinationDir))</li><li>  {</li><li>    QString errorString =</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>While the intent is good (you don’t want to create a folder that you may not be able to write to a DVD or USB stick later), but may lead to other complications. I’ve pushed a few fixes, you can try if it works better in the Slicer Preview Release that you download tomorrow or later.</p>

---

## Post #6 by @chir.set (2021-02-18 09:39 UTC)

<p>Yes, this fixes the issue. Slicer-4.13.0-2021-02-17 can now export the series, stripping special characters with ‘_’.</p>
<p>Thank you.</p>

---

## Post #7 by @lassoan (2023-03-21 02:36 UTC)



---
