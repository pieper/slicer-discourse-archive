---
topic_id: 15310
title: "Failed To Execute In Centos 8 3 2011"
date: 2021-01-01
url: https://discourse.slicer.org/t/15310
---

# Failed to execute in CentOS 8.3.2011

**Topic ID**: 15310
**Date**: 2021-01-01
**URL**: https://discourse.slicer.org/t/failed-to-execute-in-centos-8-3-2011/15310

---

## Post #1 by @endi (2021-01-01 20:12 UTC)

<p>I downloaded the latest stable release and was not able to get Slicer to execute. The error message received was</p>
<p>/u/software/slicer/Slicer-4.11.20200930-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libnsl.so.1: cannot open shared object file: No such file or directory</p>
<p>I was not able to download libnsl.slo.1 from the Centos 8 repos.</p>
<p>Does anyone on the list have Centos 8.3.2011 that might be able to help.</p>
<p>Thanks ahead of time!!!</p>
<p>Greg Ennis</p>

---

## Post #2 by @endi (2021-01-01 20:51 UTC)

<p>The same results occurred with downloading the unstable release.<br>
/u/software/slicer/Slicer-4.13.0-2020-12-31-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libnsl.so.1: cannot open shared object file: No such file or directory</p>

---

## Post #3 by @endi (2021-01-01 21:07 UTC)

<aside class="quote no-group" data-username="endi" data-post="2" data-topic="15310">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/65b543/48.png" class="avatar"> endi:</div>
<blockquote>
<p>libnsl.so.1</p>
</blockquote>
</aside>
<p>I found  BUG # 1814151<br>
<a href="https://bugzilla.redhat.com/show_bug.cgi?id=1814151" class="onebox" target="_blank" rel="noopener nofollow ugc">https://bugzilla.redhat.com/show_bug.cgi?id=1814151</a></p>
<p>After installing libnsl via<br>
dnf install libnsl</p>
<p>I was still unable to use Slice<br>
u/software/slicer/Slicer-4.13.0-2020-12-31-linux-amd64/bin/SlicerApp-real: symbol lookup error:/lib64/libk5crypto.so.3: undefined symbol: EVP_KDF_ctrl, version OPENSSL_1_1_1b</p>

---

## Post #4 by @endi (2021-01-01 22:14 UTC)

<p>Additional research identified the problem</p><aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://bugzilla.redhat.com/show_bug.cgi/extensions/RedHat/web/css/favicons/production.ico?v=0" class="site-icon" width="16" height="16">
      <a href="https://bugzilla.redhat.com/show_bug.cgi?id=1829790" target="_blank" rel="noopener nofollow ugc">bugzilla.redhat.com</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://bugzilla.redhat.com/show_bug.cgi?id=1829790" target="_blank" rel="noopener nofollow ugc">1829790 – libk5crypto.so.3: undefined symbol: EVP_KDF_ctrl, version...</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<p>
I deleted the libcrypto.so.1.1.s in the Slicer subdirectory and was able to get ./Slicer to execute.</p>
<p>Hope this is helpful to other Centos 8 users.</p>
<p>Greg</p>

---

## Post #5 by @lassoan (2021-01-02 00:49 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Is there anything we can do about this or we should just document this in linux install instructions as a workaround? Is there any better way of packaging than what we do now? Should we choose a few linux distributions that we officially support and let users build from source on all others?</p>

---
