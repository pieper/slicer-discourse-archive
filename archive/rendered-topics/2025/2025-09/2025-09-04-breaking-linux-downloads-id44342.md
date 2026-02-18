# Breaking Linux downloads

**Topic ID**: 44342
**Date**: 2025-09-04
**URL**: https://discourse.slicer.org/t/breaking-linux-downloads/44342

---

## Post #1 by @abitrolly (2025-09-04 15:16 UTC)

<p>Unable to download 3D Slicer for Linux.</p>
<pre><code class="lang-auto">$ wget -c https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download
Saving 'download'
Just got 32571392 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 32571392.
Saving 'download'
Just got 9109504 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 9109504.
Saving 'download'
Just got 14090240 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 14090240.
Saving 'download'
Just got 6422528 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 6422528.
</code></pre>
<p>The connection is unexpectedly terminated with 200. And resume is not supported. Looks like a bug on server side.</p>

---

## Post #2 by @pieper (2025-09-04 15:36 UTC)

<p>These are working for me:</p>
<p>For the preview:</p>
<p><code>wget  "http://download.slicer.org/download?os=linux&amp;stability=any&amp;offset=0" -O /tmp/slicer.tar.gz</code></p>
<p>For 5.8.1:</p>
<p><code>wget "https://download.slicer.org/bitstream/67c51fc129825655577cfee9" -O /tmp/slicer-stable.tar.gz</code></p>
<p>Maybe you have a proxy or other networking issue?</p>
<p>(edited to replace <code>-o with -O</code>)</p>

---

## Post #3 by @abitrolly (2025-09-04 21:58 UTC)

<p>I moved to another place with another ISP. There is a better speed, about 400KB/s, but the connection breaks too. It looks like I doesn’t reach 50% when it restarts.</p>
<pre><code class="lang-auto">$ wget -c https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download
Saving 'download'
Just got 169148416 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 169148416.
Saving 'download'
Just got 31391744 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 31391744.
Saving 'download'
Just got 153157632 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 153157632.
Saving 'download'
Just got 11272192 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 11272192.
Saving 'download'
Just got 10260480 of 402316524 bytes (https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download)
HTTP response 200 OK [https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download]
Unexpected body length 10260480.

                          [Files: 0  Bytes: 0  [0 B/s] Redirects: 0  Todo: 1  Errors: 0                                                          ]
</code></pre>
<p>I am not sure what is the server configuration, but judging that <a href="https://github.com/Slicer/slicer_download" rel="noopener nofollow ugc">https://github.com/Slicer/slicer_download</a> is Python app, it could be that Nginx breaks the connection under heavy load.</p>
<p>Now I was able to download slicer and the speed is much higher (3MB/s) than few hour ago when the download was broken.</p>
<p>I</p>

---

## Post #4 by @abitrolly (2025-10-12 16:24 UTC)

<p>So to improve the download experience, the Python + uWSGI + Nginx could probably be replaced with Go server that supports resuming downloads out of the box. uWSGI seems dead ( <a href="https://uwsgi-docs.readthedocs.io/en/latest/" class="inline-onebox" rel="noopener nofollow ugc">The uWSGI project — uWSGI 2.0 documentation</a> ) so probably going with <a href="https://pkg.go.dev/net/http#ServeFile" rel="noopener nofollow ugc">Go <code>http.FileServe()</code> </a>is the easiest quick win.</p>
<p>EDIT: code to start <a href="https://eli.thegreenplace.net/2023/static-server-an-http-server-in-go-for-static-content/" class="inline-onebox" rel="noopener nofollow ugc">static-server: an HTTP server in Go for static content - Eli Bendersky's website</a></p>

---

## Post #5 by @lassoan (2025-10-14 03:43 UTC)

<p>Slicer uses girder as storage backend for application packages. Unfortunately, girder has a bug: HTTP range requests are implemented incorrectly It would be OK if the server did not support it, but instead the server claims it can do it, but actually ignores the requested range parameters. The issue is described in detail here:</p>
<aside class="quote quote-modified" data-post="12" data-topic="29748">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/incomplete-slicer-package-download-gzip-stdin-invalid-compressed-data-format-violated/29748/12">Incomplete Slicer package download - `gzip: stdin: invalid compressed data--format violated`</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Thank you, the file that you got was interesting. The file has the correct size (373537536 bytes). The first 43883184 bytes were correctly downloaded. After that point, the file content restarts from the beginning. 
This indicates that the download was interrupted (it can happen for example if the server loses its patience because your network connection is slow) and then your download client thought that it could resume the interrupted download from where it was left off, but the server did not…
  </blockquote>
</aside>

<p>I’ve been downloading Slicer on various computers over various internet connections and usually the speed is between 3 MB/sec and 100 MB/sec. The entire package is downloaded within one minute, there are no interruptions, no need for resumes, so the HTTP range request bug has no impact. If the download speed for some reason is unusually slow (e.g., 0.3MB/sec), then the connection may be interrupted and your download client may then try to use “resume” feature (HTTP range request), which will result in an invalid downloaded file or other failure.</p>
<p>The problem will get higher priority if we get more complaints or we can get significant funding for improving the hosting infrastructure. But for now the approach will remain “watch and wait”.</p>

---

## Post #6 by @abitrolly (2025-10-30 19:34 UTC)

<p>Is it possible to clarify the role of the <a href="https://github.com/girder/girder" class="inline-onebox" rel="noopener nofollow ugc">GitHub - girder/girder: A data management platform for the web, developed by Kitware</a> here?</p>
<p>Is it the handler for <a href="https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/67c51fc129825655577cfee9/download</a> URL? If yes, then how does it relay it to web server?</p>

---
