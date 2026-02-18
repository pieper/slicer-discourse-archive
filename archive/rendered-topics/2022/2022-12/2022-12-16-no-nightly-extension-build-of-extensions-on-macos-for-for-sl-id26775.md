# No nightly extension build of extensions on macOS for for Slicer Stable Release

**Topic ID**: 26775
**Date**: 2022-12-16
**URL**: https://discourse.slicer.org/t/no-nightly-extension-build-of-extensions-on-macos-for-for-slicer-stable-release/26775

---

## Post #1 by @muratmaga (2022-12-16 19:34 UTC)

<p>Dashboard doesn’t display any extensions for Mac? Is there something wrong?</p>
<p><a href="https://slicer.cdash.org/index.php?project=SlicerStable" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerStable</a></p>
<p>eg., I can’t update SlicerMorph on Mac</p>

---

## Post #2 by @lassoan (2022-12-16 20:10 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> can you help with this?</p>

---

## Post #3 by @jcfr (2022-12-16 20:34 UTC)

<blockquote>
<p>can you help with this?</p>
</blockquote>
<p>I will follow up shortly with an update.</p>

---

## Post #4 by @Young_Wang (2022-12-16 20:44 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I’m curious about which model of Mac and which version of OS you are running.</p>

---

## Post #5 by @muratmaga (2022-12-16 21:53 UTC)

<p>It is macbook pro from 2019, running macos 12.6.1</p>

---

## Post #6 by @jcfr (2022-12-17 00:43 UTC)

<p>To follow up on this, while <code>Preview</code> extensions are always being built on macOS. There are issues to finalize the build associated with the <code>Preview</code> extensions. See below.</p>
<p>Waiting we understand better, I will restart the machine.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Date</th>
<th>Slicer Preview</th>
<th>Slicer Stable</th>
</tr>
</thead>
<tbody>
<tr>
<td>2022-12-16</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-12-16&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">164</a>
</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/hourglass.png?v=12" title=":hourglass:" class="emoji" alt=":hourglass:" loading="lazy" width="20" height="20">   <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-12-16&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">76</a>
</td>
</tr>
<tr>
<td>2022-12-15</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-12-15&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">164</a>
</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-12-15&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">165</a>
</td>
</tr>
<tr>
<td>2022-12-14</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-12-14&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">164</a>
</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-12-14&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">88</a>
</td>
</tr>
<tr>
<td>2022-12-13</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-12-13&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">164</a>
</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-12-13&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">144</a>
</td>
</tr>
<tr>
<td>2022-12-12</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-12-12&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">164</a>
</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-12-12&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">164</a>
</td>
</tr>
<tr>
<td>2022-12-11</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-12-11&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">164</a>
</td>
<td>
<img src="https://emoji.discourse-cdn.com/twitter/question.png?v=12" title=":question:" class="emoji" alt=":question:" loading="lazy" width="20" height="20">  <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2022-12-11&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=factory-south-macos">156</a>
</td>
</tr>
</tbody>
</table>
</div>

---

## Post #7 by @jcfr (2022-12-17 00:51 UTC)

<p>Looking at the log file associated with the <code>Preview</code> build:</p>
<pre><code class="lang-auto">$ ls -lh /Volumes/D/Logs/factory-south-macos-slicerextensions_preview_nightly.log
...   228K Dec 16 15:50 ....
</code></pre>
<p>we can see it was written at 3:50 pm.</p>
<p>Looking at the list of running process:</p>
<pre><code class="lang-auto">$ $ ps aux  | grep "\-O /Volumes/D/Logs/" 
....    3:50PM   0:25.53 /Volumes/D/Support/CMake-3.22.1.app/Contents/bin/ctest -S /Volumes/D/DashboardScripts/factory-south-macos-slicerextensions_stable_nightly.cmake -VV -O /Volumes/D/Logs/factory-south-macos-slicerextensions_stable_nightly.log
</code></pre>
<p>we can see it started at  3:50 pm.</p>

---

## Post #8 by @jcfr (2022-12-17 00:52 UTC)

<p>To address this, I will disable the tests associated with the Stable build.</p>

---

## Post #9 by @muratmaga (2023-01-06 17:38 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a><br>
this is back, no mac extensions on the stable (at least now shown on dashboard).</p>

---

## Post #10 by @fedorov (2023-01-06 17:58 UTC)

<p>I do not see mac extensions on the preview either. Just downloaded the latest preview.</p>

---

## Post #11 by @lassoan (2023-01-07 00:19 UTC)

<p>Just to clarify: The Extensions Catalog looks good (<a href="https://extensions.slicer.org/catalog/All/31317/macosx">extensions are available for macOS for Slicer 5.2.1</a>). The problems are that extensions were not built last night:</p>
<ul>
<li>on macOS for the <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2023-01-06">Slicer Stable Release</a>
</li>
<li>on macOS and linux for the <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2023-01-06">Slicer Preview Release</a>
</li>
</ul>
<p>A network issue shows up in the linux build in the Slicer Preview Release, so maybe that network outage caused all the issues. Or maybe something else got stuck and the factory computers need a restart. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> or <a class="mention" href="/u/jcfr">@jcfr</a> please have a look.</p>

---

## Post #12 by @jcfr (2023-01-07 02:02 UTC)

<blockquote>
<p>I will disable the tests associated with the Stable build.</p>
</blockquote>
<p>This has just been done in <a href="https://github.com/Slicer/DashboardScripts/commit/2280c47d6633b9cc155fa412cf6f647afc083717">Slicer/DashboardScripts@2280c47d6</a></p>

---

## Post #13 by @jcfr (2023-01-07 02:18 UTC)

<blockquote>
<p>re: Connection timed out / <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2904982">metroplex / Slicer Preview Release</a></p>
</blockquote>
<p>SSH’ing to <code>metroplex</code> and attempting to build the <code>OpenSSL</code> target confirm this was a temporary network failure.</p>
<pre><details><summary>ninja OpenSSL</summary>

[6/15] Performing download step (download, verify and extract) for 'OpenSSL'
-- verifying file...
       file='/work/Preview/Slicer-0-build/openssl-1.1.1g-pr12238.tar.gz'
-- MD5 hash of
    /work/Preview/Slicer-0-build/openssl-1.1.1g-pr12238.tar.gz
  does not match expected value
    expected: '4765dcd60bcbed784c59ad7c2ca2b841'
      actual: 'd41d8cd98f00b204e9800998ecf8427e'
-- File already exists but hash mismatch. Removing...
-- Downloading...
   dst='/work/Preview/Slicer-0-build/openssl-1.1.1g-pr12238.tar.gz'
   timeout='none'
   inactivity timeout='none'
-- Using src='https://github.com/Slicer/Slicer-OpenSSL/releases/download/sources/openssl-1.1.1g-pr12238.tar.gz'
-- [download 0% complete]
-- ...
-- [download 100% complete]
-- verifying file...
       file='/work/Preview/Slicer-0-build/openssl-1.1.1g-pr12238.tar.gz'
-- Downloading... done
-- extracting...
     src='/work/Preview/Slicer-0-build/openssl-1.1.1g-pr12238.tar.gz'
     dst='/work/Preview/Slicer-0-build/OpenSSL'
-- extracting... [tar xfz]
-- extracting... [analysis]
-- extracting... [rename]
-- extracting... [clean up]
-- extracting... done
...
[15/15] Completed 'OpenSSL'
</details>
</pre>
<p>Since no incident are reported in <a href="https://www.githubstatus.com/history">GitHub Status history</a>, I will check with Kitware monitoring.</p>

---

## Post #14 by @jcfr (2023-01-07 23:06 UTC)

<p>Follow up:</p>
<ul>
<li>
<code>metroplex</code> dashboard <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">
</li>
<li>
<code>factory-south-macos</code> <img src="https://emoji.discourse-cdn.com/twitter/hourglass_flowing_sand.png?v=12" title=":hourglass_flowing_sand:" class="emoji" alt=":hourglass_flowing_sand:" loading="lazy" width="20" height="20">
<ul>
<li>testing of the preview package was “stuck” due to a zombie process, this has been resumed and build &amp; test of extensions should follow up</li>
<li>Note that build of preview macos packages are being reinstated on <code>computron</code>  factory that is now running macOS 13 (Ventura). See <a href="https://github.com/Slicer/DashboardScripts/issues/52">Slicer/DashboardScripts#52</a>
</li>
</ul>
</li>
</ul>

---

## Post #15 by @fedorov (2023-01-13 14:41 UTC)

<p>Extension manager for a preview release is blank again today.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a23b1ef88d6f5bb65ad9465dbdfe02dde5a17b79.jpeg" data-download-href="/uploads/short-url/n9a10LwITNDbiKM9JMpRWl5aGil.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a23b1ef88d6f5bb65ad9465dbdfe02dde5a17b79_2_690x452.jpeg" alt="image" data-base62-sha1="n9a10LwITNDbiKM9JMpRWl5aGil" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a23b1ef88d6f5bb65ad9465dbdfe02dde5a17b79_2_690x452.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a23b1ef88d6f5bb65ad9465dbdfe02dde5a17b79_2_1035x678.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a23b1ef88d6f5bb65ad9465dbdfe02dde5a17b79_2_1380x904.jpeg 2x" data-dominant-color="EFF1F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2106×1382 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #16 by @jcfr (2023-01-13 15:48 UTC)

<p>Based on your screenshot, it is associated with <code>2023.01.05</code> which seems to correspond to the preview release for which one you already reported an issue, see <a href="https://discourse.slicer.org/t/no-nightly-extension-build-of-extensions-on-macos-for-for-slicer-stable-release/26775/10">here</a>.</p>
<p>I suggest you download a more recent preview build.</p>

---

## Post #17 by @fedorov (2023-01-13 16:27 UTC)

<p>I see. I mistakenly assumed that dashboard fix will recover extensions for the problematic past releases. Thank you for the clarification.</p>

---

## Post #18 by @mau_igna_06 (2023-01-13 16:37 UTC)

<p>I think this should work on ubuntu:</p>
<pre><code class="lang-auto">QTWEBENGINE_DISABLE_SANDBOX=1 ./Slicer
</code></pre>
<p>The extensions manager is empty for me if I don’t set that variable</p>
<p>Hope it helps</p>

---
