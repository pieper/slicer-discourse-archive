# Unable to download 3D SLICER 5.2.2 for windows

**Topic ID**: 28886
**Date**: 2023-04-13
**URL**: https://discourse.slicer.org/t/unable-to-download-3d-slicer-5-2-2-for-windows/28886

---

## Post #1 by @zahra (2023-04-13 13:42 UTC)

<p>Hello<br>
For a week I’ve been trying to download the software from this page : <a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a><br>
the download starts and stops suddenly and shows me “unable to download”<br>
Any solution that can help me ?<br>
Thanks in advance</p>

---

## Post #2 by @pieper (2023-04-13 13:44 UTC)

<p>It sounds like a network issue between you and the server.  Downloading works for me both on my local workstation and from various cloud compute instances.</p>

---

## Post #3 by @ripburger (2023-04-14 12:39 UTC)

<p>I have run into this issue myself several times with attempting to download Slicer, even earlier this week. Whenever I tried to download from Windows (various Browsers and at command line with PowerShell) I noticed the same thing, goes for a bit at high speed, throttles down, then quits.</p>
<p>I was eventually able to download on my Mac (from the same network), so I’m wondering if it’s something on Slicer’s server side, or something else with its geophysical hosting. I’m downloading from North America if that helps, over standard residential internet.</p>

---

## Post #4 by @pieper (2023-04-14 13:22 UTC)

<p>Thanks for reporting.  If others have the same problem please report and maybe we can get to the bottom of the issue.</p>

---

## Post #5 by @lassoan (2023-04-15 00:54 UTC)

<p>I’ve tried from Eastern Canada when I saw the post, the download was completed in about 30 seconds.</p>
<p>Please write here if you encounter any problem again (with the exact time when it happened) and we’ll test immediately.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> can you see errors in the server logs?</p>

---

## Post #6 by @jcfr (2023-04-15 03:32 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="28886">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>can you see errors in the server logs?</p>
</blockquote>
</aside>
<p>We will be reviewing the log and follow up.</p>

---

## Post #7 by @jcfr (2023-04-15 21:50 UTC)

<h3><a name="p-93569-server-downloadslicerorg-server-1" class="anchor" href="#p-93569-server-downloadslicerorg-server-1" aria-label="Heading link"></a>server: <code>download.slicer.org</code> server</h3>
<p>Based on the access and error logs associated with <code>download.slicer.org</code> for the period of April 8th to April 14th.</p>
<p>We couldn’t identify any outstanding issues.</p>
<p>That said, reviewing the <code>500</code> errors helped identify some interesting attempts to gain privileged access, we will follow up with details.</p>
<p><strong>Details:</strong></p>
<pre><code class="lang-auto">$ cat access.txt.* | cut -d '"' -f3 | cut -d ' ' -f2 | sort | uniq -c | sort -rn
 107416 200
  11365 302
  10406 404
    511 400
    139 502
    122 499
     64 405
     58 301
     49 206
     24 304
     13 500
</code></pre>
<pre><code class="lang-auto">$ cat error.txt.* | wc -l
194
</code></pre>
<pre><code class="lang-auto">$ cat error.txt.* | ack "SSL_do_handshake\(\) failed" | wc -l
55
</code></pre>
<pre><code class="lang-auto">$ cat error.txt.* | ack "Connection refused" | wc -l
139
</code></pre>
<h3><a name="p-93569-server-slicer-packageskitwarecom-2" class="anchor" href="#p-93569-server-slicer-packageskitwarecom-2" aria-label="Heading link"></a>server: <code>slicer-packages.kitware.com</code></h3>
<p>This is the server from which both application and extension packages are effectively downloaded from.</p>
<p>The downloads may be originate from the <code>download.slicer.org</code> site or from the <code>extensions.slicer.org</code> presented to the user through the <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html">extensions manager</a>.</p>
<p>We will shortly provide a report.</p>

---
