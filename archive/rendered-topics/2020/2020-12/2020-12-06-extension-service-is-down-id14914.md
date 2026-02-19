---
topic_id: 14914
title: "Extension Service Is Down"
date: 2020-12-06
url: https://discourse.slicer.org/t/14914
---

# Extension service is down

**Topic ID**: 14914
**Date**: 2020-12-06
**URL**: https://discourse.slicer.org/t/extension-service-is-down/14914

---

## Post #1 by @pieper (2020-12-06 19:10 UTC)

<p>It looks like midas is half-broken.  The metadata can be retrieved but the downloaded files are empty.</p>
<p>Can someone reboot it?</p>
<pre><code class="lang-auto">"Retrieving extension metadata [ extensionId: 405842]"
"Downloading extension [ itemId: 548410]"
"Archive /tmp/29402-linux-amd64-WindowLevelEffect-git39baeae-2016-07-22.tar.gz.mFmokN doesn't contain any files !"
Uncaught SyntaxError: missing ) after argument list
</code></pre>

---

## Post #2 by @Sam_Horvath (2020-12-07 14:52 UTC)

<p>Looking into it now!</p>

---

## Post #3 by @jcfr (2020-12-07 19:07 UTC)

<p>Updates:</p>
<ul>
<li>We identified the issue and will follow up once it is addressed. In short, the server ran out of disk space.</li>
<li>Once we are done addressing VTK9-Slicer integration <a href="https://github.com/Slicer/Slicer/issues?q=is%3Aissue+is%3Aopen+label%3Adomain%3Avtk9">issues</a>, we will <a href="https://www.slicer.org/wiki/Documentation/Labs/ExtensionsServer#Status">resume</a> work toward integration of the new extension management infrastructure.</li>
</ul>
<p>Thanks for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>

---

## Post #4 by @jcfr (2020-12-08 13:25 UTC)

<p>Update: I confirm increasing the space available on the server addressed the issue (+1TB)</p>

---
