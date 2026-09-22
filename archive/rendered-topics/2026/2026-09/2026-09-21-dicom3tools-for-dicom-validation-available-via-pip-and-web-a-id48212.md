---
topic_id: 48212
title: "Dicom3tools for DICOM validation available via pip and web app"
date: 2026-09-21
url: https://discourse.slicer.org/t/48212
last_bumped: 2026-09-21T16:00:24.260Z
---

# Dicom3tools for DICOM validation available via pip and web app

**Topic ID**: 48212
**Date**: 2026-09-21
**URL**: https://discourse.slicer.org/t/dicom3tools-for-dicom-validation-available-via-pip-and-web-app/48212

---

## Post #1 by @fedorov (2026-09-21 14:45 UTC)

<p><em>Reposted (with edits) from <a href="https://discourse.canceridc.dev/t/dicom3tools-binaries-are-now-available-via-a-pypi-package/802" class="inline-onebox">Dicom3tools binaries are now available via a PyPI package - Announcements - Imaging Data Commons</a></em></p>
<hr>
<p>Those of us who work with DICOM a lot (by desire or by necessity) know what <code>dciodvfy</code> is. The ultimate DICOM validator. One of the many tools offered by the <a href="https://www.dclunie.com/dicom3tools.html"><code>dicom3tools</code> software</a> maintained by the one and only David Clunie. Open source, but not on GitHub. Written in C++, but with prebuilt binaries available only for Mac and Windows.</p>
<p>We at Imaging Data Commons want to make it easier to access those tools, with the release of the three companion repositories:</p>
<ul>
<li>
<p><a href="https://github.com/ImagingDataCommons/dicom3tools:">https://github.com/ImagingDataCommons/dicom3tools:</a> github mirror of the <code>dicom3tools</code> source code, synchronized automatically from the source packages published by David Clunie, release-tagged, and accompanied by binaries for Windows, Linux and Mac</p>
</li>
<li>
<p><a href="https://github.com/ImagingDataCommons/dicom3tools-python-distributions:">https://github.com/ImagingDataCommons/dicom3tools-python-distributions:</a> python distribution of the dicom3tools binaries, published on PyPI: pip install dicom3tools will install <code>dciodvfy</code>, <code>dcentvfy</code>, <code>dcdump</code> and other <code>dicom3tools</code> binaries in the path of your environment - and callable from Python</p>
</li>
<li>
<p><a href="https://github.com/ImagingDataCommons/dicom3tools-web-distributions">https://github.com/ImagingDataCommons/dicom3tools-web-distributions</a> WebAssembly packaging) + <a href="https://imagingdatacommons.github.io/dicom3tools-web-distributions/">https://imagingdatacommons.github.io/dicom3tools-web-distributions/</a> web page interface where you can validate your DICOM files directly in the browser (contribution by Alireza Sedghi)</p>
</li>
</ul>
<p>You can now easily incorporate DICOM validation into your CI workflows, add these binaries to your Dockerfile or a Colab notebook, check conformance of suspected problematic files without installing anything!</p>
<p>See any issues? If you notice tools are not agreeing with the standard - contact David Clunie. If you have problems with the packaging - open an issue in one of the repos above!</p>
<p>We hope this small improvement will make it easier for you to identify problems in the DICOM files you are working with, and will help you improve standard compliance for the new content you create!</p>

---

## Post #2 by @pieper (2026-09-21 15:01 UTC)

<p>Thanks for posting <a class="mention" href="/u/fedorov">@fedorov</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>I confirm the following works for me on Slicer 5.12.4 on mac (intel)</p>
<pre><code class="lang-auto">&gt;&gt;&gt; pip_install("dicom3tools")
Collecting dicom3tools
  Downloading dicom3tools-20260901-py3-none-macosx_10_9_x86_64.whl.metadata (18 kB)
Downloading dicom3tools-20260901-py3-none-macosx_10_9_x86_64.whl (37.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 37.3/37.3 MB 21.7 MB/s  0:00:01
Installing collected packages: dicom3tools
Successfully installed dicom3tools-20260901
&gt;&gt;&gt; dicom3tools.run("dciodvfy", ["/tmp/x.dcm"])
0
[FD] Warning - Missing attribute or value that would be needed to build DICOMDIR - Study ID
[FD] Warning - Value dubious for this VR - (0x0010,0x0010) PN Patient's Name  PN [1] = &lt;13800&gt; - Retired Person Name form
[FD] CTImage
</code></pre>
<p>Any plans to make this more pythonic?  I.e. capture the output as an array of strings for example or make <code>dicom3tools.dciodvfy</code> take a file path as an argument.</p>

---

## Post #3 by @fedorov (2026-09-21 15:06 UTC)

<p>No immediate plans, but if you have any ideas like that, please open an issue in the most appropriate repo from those mentioned so we can consider in the future!</p>

---

## Post #4 by @pieper (2026-09-21 16:00 UTC)

<p>done!</p><aside class="onebox githubissue" data-onebox-src="https://github.com/ImagingDataCommons/dicom3tools-python-distributions/issues/4">
  <header class="source">

      <a href="https://github.com/ImagingDataCommons/dicom3tools-python-distributions/issues/4" target="_blank" rel="noopener">github.com/ImagingDataCommons/dicom3tools-python-distributions</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/ImagingDataCommons/dicom3tools-python-distributions/issues/4" target="_blank" rel="noopener">Make interface more pythonic</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2026-09-21" data-time="16:00:06" data-timezone="UTC">04:00PM - 21 Sep 26 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/pieper" target="_blank" rel="noopener">
          <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Make it possible to run `results = dicom3tools.dciodvfy(file_path)` where `resul<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ts` is either a list of strings of analysis results or an instance of a class that gives higher level parsed output, like `results.warnings_only()` 

https://discourse.slicer.org/t/dicom3tools-for-dicom-validation-available-via-pip-and-web-app/48212</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
