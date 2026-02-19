---
topic_id: 41357
title: "No Extensions Are Being Built For Linux Stable 5 8"
date: 2025-01-29
url: https://discourse.slicer.org/t/41357
---

# No extensions are being built for Linux stable (5.8)

**Topic ID**: 41357
**Date**: 2025-01-29
**URL**: https://discourse.slicer.org/t/no-extensions-are-being-built-for-linux-stable-5-8/41357

---

## Post #1 by @muratmaga (2025-01-29 14:59 UTC)

<p>Cdash does not show any Linux extensions for couple days now…</p>

---

## Post #2 by @muratmaga (2025-02-03 21:28 UTC)

<p>Following up on this. There are no extension rebuild for Linux since 1/25. Cdash shows the extension list for latest stable as empty.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #3 by @jcfr (2025-02-03 22:56 UTC)

<p>Reviewing CDash, we can confirm that yesterday extensions were built for both:</p>
<ul>
<li>Stable:
<ul>
<li>CDash: <a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex">https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex</a></li>
<li>Extensions: <a href="https://extensions.slicer.org/catalog/All/33216/linux">https://extensions.slicer.org/catalog/All/33216/linux</a></li>
</ul>
</li>
<li>Preview (aka Nightly):
<ul>
<li>CDash: <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex">https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex</a></li>
<li>Extensions: <a href="https://extensions.slicer.org/catalog/All/33455/linux">https://extensions.slicer.org/catalog/All/33455/linux</a></li>
</ul>
</li>
</ul>
<hr>
<p>That said, we can indeed see missing builds.</p>
<p>To summarize:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>01/25</th>
<th>01/26</th>
<th>01/27</th>
<th>01/28</th>
<th>01/29</th>
<th>01/30</th>
<th>01/31</th>
<th>02/01</th>
<th>02/02</th>
<th>02/03</th>
</tr>
</thead>
<tbody>
<tr>
<td>Preview</td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-25&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-26&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-27&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-28&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-29&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-30&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-01-31&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-01&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2025-02-03&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
</tr>
<tr>
<td>Stable</td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-01-25&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-01-26&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-01-27&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-01-28&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-01-29&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-01-30&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-01-31&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-01&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-02&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji only-emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"></a></td>
<td><a href="https://slicer.cdash.org/index.php?project=SlicerStable&amp;date=2025-02-03&amp;filtercount=1&amp;showfilters=1&amp;field1=site&amp;compare1=63&amp;value1=metroplex"><img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji only-emoji" alt=":x:" loading="lazy" width="20" height="20"></a></td>
</tr>
</tbody>
</table>
</div><p><em><strong>Note:</strong> Clicking on either <img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=12" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  or <img src="https://emoji.discourse-cdn.com/twitter/x.png?v=12" title=":x:" class="emoji" alt=":x:" loading="lazy" width="20" height="20">  will open the corresponding CDash page for either Preview or Stable build.</em></p>

---

## Post #4 by @jcfr (2025-02-03 23:02 UTC)

<p>Notes:</p>
<ul>
<li>Following the failed builds reported between 01/27 and 01/29, we performed cleanup of orphan and unused docker images along with setting up daily restart of the system to ensure there are no lingering docker builds.</li>
<li>We are still investigating the failures of 02/01 and 02/03.</li>
</ul>

---

## Post #5 by @jcfr (2025-02-04 00:03 UTC)

<blockquote>
<p>re: We are still investigating the build failures from 02/01 and 02/03.</p>
</blockquote>
<p>Now that Slicer 5.8 has been released, we will proceed with backing up the relevant build trees in preparation for updating the underlying operating system and transitioning to a more recent Docker engine. Our goal is to minimize disruption while improving system reliability.</p>
<p>The current Docker engine version has been unstable and frequently encounters the following error:</p>
<pre><code class="lang-auto">2025/02/03 01:49:09 grpc: Server.processUnaryRPC failed to write status stream error: code = 4 desc = "context deadline exceeded"
</code></pre>
<p>To address this, we will schedule a system upgrade. A dedicated post will follow to coordinate the required downtime.</p>

---
