---
topic_id: 13831
title: "Truncated Gzip Input On The New Stable Version On Linux"
date: 2020-10-02
url: https://discourse.slicer.org/t/13831
---

# Truncated gzip input on the new Stable version (on Linux)

**Topic ID**: 13831
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/truncated-gzip-input-on-the-new-stable-version-on-linux/13831

---

## Post #1 by @agporto (2020-10-02 20:55 UTC)

<p>When downloading the new stable version (Slicer-4.11.20200930-linux-amd64) for Linux, I am getting ‘truncated gzip input’ when trying to extract the contents. It is happening in multiple machines, so I assume it is problem with the file itself.</p>

---

## Post #2 by @muratmaga (2020-10-02 20:59 UTC)

<p>Same here:</p>
<p>Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/<strong>pycache</strong>/sysconfig.cpython-36.opt-1.pyc</p>
<p>gzip: stdin: unexpected end of file<br>
Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/<strong>pycache</strong>/operator.cpython-36.pyc<br>
tar: Unexpected EOF in archive<br>
tar: Unexpected EOF in archive<br>
tar: Error is not recoverable: exiting now</p>

---

## Post #3 by @lassoan (2020-10-03 02:53 UTC)

<p>Confirmed. <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> it would be great if you could upload the file again.</p>

---

## Post #4 by @muratmaga (2020-10-04 15:59 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> the download link still brings the corrupted file.</p>

---

## Post #5 by @Sam_Horvath (2020-10-05 14:18 UTC)

<p>Can you try the original package here:<br>
</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="http://slicer.cdash.org/viewFiles.php/favicon.ico" class="site-icon" width="16" height="16">
      <a href="http://slicer.cdash.org/viewFiles.php?buildid=2025692" target="_blank" rel="noopener nofollow ugc">slicer.cdash.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="http://slicer.cdash.org/viewFiles.php?buildid=2025692" target="_blank" rel="noopener nofollow ugc">CDash - Uploaded files</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @muratmaga (2020-10-05 14:51 UTC)

<p>Yes, the file in the link is working for me.</p>

---

## Post #7 by @Sam_Horvath (2020-10-05 15:37 UTC)

<p>Package has been re-uploaded, downloads fine on my end.  Give it a try!</p>

---
