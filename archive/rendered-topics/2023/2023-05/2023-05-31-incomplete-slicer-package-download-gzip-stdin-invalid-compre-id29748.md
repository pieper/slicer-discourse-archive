# Incomplete Slicer package download - `gzip: stdin: invalid compressed data--format violated`

**Topic ID**: 29748
**Date**: 2023-05-31
**URL**: https://discourse.slicer.org/t/incomplete-slicer-package-download-gzip-stdin-invalid-compressed-data-format-violated/29748

---

## Post #1 by @Tanuki (2023-05-31 13:40 UTC)

<p>Downloaded the tar file repeatedly but each one has the same error. The unpacked tar only has the bin and lib directories.</p>
<pre><code class="lang-auto">gzip: stdin: invalid compressed data--format violated
tar: Unexpected EOF in archive
tar: Error is not recoverable: exiting now
</code></pre>

---

## Post #2 by @lassoan (2023-05-31 13:41 UTC)

<p>Please check if the downloaded file’s checksum matches the <a href="https://download.slicer.org/#checksums">checksum on the download site</a>.</p>

---

## Post #3 by @Tanuki (2023-05-31 14:52 UTC)

<p>The chechsums don’t match. It’s the same for the preview.</p>

---

## Post #4 by @pearsonm (2023-05-31 22:17 UTC)

<p>You might need to use a tool that allows you to retry a failed download such as DownThemAll. I am in Australia and have similar issues with Slicer downloads.</p>

---

## Post #5 by @lassoan (2023-06-01 00:16 UTC)

<p>Thanks for the reports. I don’t recall hearing any problems about interrupted downloads. Do you connect through VPN or proxy server? How long does it take to download the installer package? If you repeat the download multiple times, are all the download attempts result in exactly the same file size?</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> do you see anything in the server logs?</p>

---

## Post #6 by @pearsonm (2023-06-01 01:42 UTC)

<p>I think in my case it might be ISP related as my downloads from home rarely fail. The work connection is directly to our ISP without any proxy etc. and I am the network admin. All downloads are different sizes so there is no common failure point.</p>
<p>Here is a typical download attempt. The connection keeps failing until interrupted.</p>
<blockquote>
<p>wget <a href="https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7" rel="noopener nofollow ugc">https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7</a><br>
–2023-06-01 11:09:36--  <a href="https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7" rel="noopener nofollow ugc">https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7</a><br>
Resolving <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a> (<a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a>)… 66.162.65.219<br>
Connecting to <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a> (<a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a>)|66.162.65.219|:443… connected.<br>
HTTP request sent, awaiting response… 302 FOUND<br>
Location: <a href="https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download</a> [following]<br>
–2023-06-01 11:09:37--  <a href="https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download</a><br>
Resolving <a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a> (<a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a>)… 216.136.40.52<br>
Connecting to <a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a> (<a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a>)|216.136.40.52|:443… connected.<br>
HTTP request sent, awaiting response… 200 OK<br>
Length: 373537536 (356M) [application/octet-stream]<br>
Saving to: ‘63f5bee68939577d9867b4c7’</p>
<p>63f5bee68939577d9867b4c7           9%[====&gt;                                                     ]  35.06M  1.50MB/s    in 83s</p>
<p>2023-06-01 11:11:02 (431 KB/s) - Connection closed at byte 36765696. Retrying.</p>
<p>–2023-06-01 11:11:03--  (try: 2)  <a href="https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download</a><br>
Connecting to <a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a> (<a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a>)|216.136.40.52|:443… connected.<br>
HTTP request sent, awaiting response… 206 Partial Content<br>
Retrying.</p>
<p>–2023-06-01 11:11:05--  (try: 3)  <a href="https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download</a><br>
Connecting to <a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a> (<a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a>)|216.136.40.52|:443… connected.<br>
HTTP request sent, awaiting response… 206 Partial Content<br>
Retrying.</p>
<p>–2023-06-01 11:11:09--  (try: 4)  <a href="https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download</a><br>
Connecting to <a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a> (<a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a>)|216.136.40.52|:443… connected.<br>
HTTP request sent, awaiting response… 206 Partial Content<br>
Retrying.</p>
</blockquote>
<p>A second attempt about 10 minutes later worked.</p>
<blockquote>
<p>wget <a href="https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7" rel="noopener nofollow ugc">https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7</a><br>
–2023-06-01 11:29:19--  <a href="https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7" rel="noopener nofollow ugc">https://download.slicer.org/bitstream/63f5bee68939577d9867b4c7</a><br>
Resolving <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a> (<a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a>)… 66.162.65.219<br>
Connecting to <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a> (<a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a>)|66.162.65.219|:443… connected.<br>
HTTP request sent, awaiting response… 302 FOUND<br>
Location: <a href="https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download</a> [following]<br>
–2023-06-01 11:29:20--  <a href="https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download</a><br>
Resolving <a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a> (<a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a>)… 216.136.40.52<br>
Connecting to <a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a> (<a href="http://slicer-packages.kitware.com" rel="noopener nofollow ugc">slicer-packages.kitware.com</a>)|216.136.40.52|:443… connected.<br>
HTTP request sent, awaiting response… 200 OK<br>
Length: 373537536 (356M) [application/octet-stream]<br>
Saving to: ‘63f5bee68939577d9867b4c7.1’</p>
<p>63f5bee68939577d9867b4c7.1       100%[=========================================================&gt;] 356.23M  1.34MB/s    in 3m 50s</p>
<p>2023-06-01 11:33:10 (1.55 MB/s) - ‘63f5bee68939577d9867b4c7.1’ saved [373537536/373537536]</p>
</blockquote>
<blockquote>
<p>sha512sum 63f5bee68939577d9867b4c7.1<br>
aed98e0b800054d69ca5636e13c39e11a1c633b15e3b6faafade505c04867ed5e285446f4be210073fec6a9e501089ec76f3fe82edbb57d40d72b38c2796b67b  63f5bee68939577d9867b4c7.1</p>
</blockquote>

---

## Post #7 by @Tanuki (2023-06-02 08:28 UTC)

<p>The downloads are never interrupted and all have the same size. I can’t recall the download times but they were roughly the same. I do not connect through a VPN or Proxy server.</p>

---

## Post #8 by @lassoan (2023-06-02 23:44 UTC)

<p>Thanks for the additional info. Hopefully <a class="mention" href="/u/jcfr">@jcfr</a> will be able to look at the server logs and we can learn something from there.</p>
<p><a class="mention" href="/u/tanuki">@Tanuki</a> please provide exact time when your download failed (including timezone) and the download URL.</p>

---

## Post #9 by @Tanuki (2023-06-04 16:52 UTC)

<p>The downloads are never interrupted nor do they fail. My last download was on 31-05-2023.</p>
<p>Time zone: Africa/Accra (GMT, +0000)</p>
<p><a href="https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download</a></p>

---

## Post #10 by @lassoan (2023-06-04 19:33 UTC)

<p>Thanks for the information. Do all your downloads have the same size? Could you upload somewhere an incomplete downloaded file?</p>

---

## Post #11 by @Tanuki (2023-06-04 20:10 UTC)

<p>Thanks for the help so far. All the downloads have the same file size and all completed downloading without interruption.</p>
<p>link to the upload</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://mega.nz/file/KlgFEY7K#Qx7hHO6QWugRU3EFUtUriPCtPG2iFKdPsL4P5aN0b7U">
  <header class="source">
      <img src="https://mega.nz/favicon.ico?v=3" class="site-icon" width="32" height="32">

      <a href="https://mega.nz/file/KlgFEY7K#Qx7hHO6QWugRU3EFUtUriPCtPG2iFKdPsL4P5aN0b7U" target="_blank" rel="noopener nofollow ugc">mega.nz</a>
  </header>

  <article class="onebox-body">
    <img src="https://mega.nz/rich-file.png" class="thumbnail onebox-avatar" width="500" height="500">

<h3><a href="https://mega.nz/file/KlgFEY7K#Qx7hHO6QWugRU3EFUtUriPCtPG2iFKdPsL4P5aN0b7U" target="_blank" rel="noopener nofollow ugc">356.23 MB file on MEGA</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @lassoan (2023-06-05 01:22 UTC)

<p>Thank you, the file that you got was interesting. The file has the correct size (373537536 bytes). The first 43883184 bytes were correctly downloaded. After that point, the file content restarts from the beginning.</p>
<p>This indicates that the download was interrupted (it can happen for example if the server loses its patience because your network connection is slow) and then your download client thought that it could resume the interrupted download from where it was left off, but the server did not support this and just just provided the bytes from the beginning.</p>
<p>With some help from bing-chat, I checked if the Slicer download server supports resume:</p>
<pre><code class="lang-auto">import requests

url = 'https://slicer-packages.kitware.com/api/v1/item/63f5bee68939577d9867b4c7/download'
headers = {'Range': 'bytes=0-4'}
res = requests.head(url, headers=headers)

if res.status_code == 206:
    print('Resume download is supported')
else:
    print('Resume download is not supported')
</code></pre>
<p>The result was: <code>Resume download is supported</code></p>
<p>Just to confirm, I’ve printed the header:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; res.headers
{'Server': 'nginx',
'Date': 'Mon, 05 Jun 2023 00:48:28 GMT',
'Content-Type': 'application/octet-stream',
'Content-Length': '373537536',
'Connection': 'keep-alive',
'Allow': 'DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT',
'Girder-Request-Uid': '93225529-db4f-4337-8055-363bcc8e7bb9',
'Accept-Ranges': 'bytes',
'Content-Disposition': 'attachment; filename="Slicer-5.2.2-linux-amd64.tar.gz"',
'Content-Range': 'bytes 0-373537535/373537536',
'Strict-Transport-Security': 'max-age=63072000'}
</code></pre>
<p>Again, <code>'Accept-Ranges': 'bytes'</code> confirmed that the server can resume a download.</p>
<p>After this, I’ve tested if the server can actually accepts a range, by requesting file content in the range of byte 10-20:</p>
<pre><code class="lang-auto">headers = {'Range': 'bytes=10-20'}
res = requests.get(url, headers=headers)
with open('c:/tmp/slicerpackage.bin', 'wb') as f:
    f.write(res.content)
</code></pre>
<p>This script downloaded the entire Slicer package and wrote it to file - from byte 0!</p>
<p>The response header tells that the server actually did not respect the range request  (see <code>Content-range</code>):</p>
<pre><code class="lang-auto">&gt;&gt;&gt; res.headers
{'Server': 'nginx', 'Date': 'Mon, 05 Jun 2023 00:56:57 GMT', 'Content-Type': 'application/octet-stream', 'Content-Length': '373537536', 'Connection': 'keep-alive', 'Allow': 'DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT', 'Girder-Request-Uid': '9bbfbc0b-c732-4ee7-a057-975401fd5fcb', 'Accept-Ranges': 'bytes', 'Content-Disposition': 'attachment; filename="Slicer-5.2.2-linux-amd64.tar.gz"', 'Content-Range': 'bytes 0-373537535/373537536', 'Strict-Transport-Security': 'max-age=63072000'}
&gt;&gt;&gt; res.status_code
206
</code></pre>
<p>Arguably, the download client should have known better that it did not get what it asked for and use the received bytes appropriately, but I think overall the server behavior is confusing and probably incorrect. Even more so because the server returned status code of 206 = “partial content”, which is again wrong, as it provided the full content again.</p>
<p>Therefore, it seems that the problem is that the Slicer download server states that it supports resume, but then it ignores the requested content range information in the header and provides the full file content.</p>

---

## Post #13 by @lassoan (2023-06-05 01:22 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Could you please configure the Slicer download server so that it either states that it does not accept range requests; or fix it so that it actually respects range requests?</p>
<p>This will probably solve the download issues that users occasionally reported over slow/unreliable network connections.</p>

---

## Post #14 by @Tanuki (2023-06-05 09:30 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> for your help. I guess I’'l and check back to see if it is fixed.</p>

---

## Post #15 by @jcfr (2023-06-06 15:37 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the detailed analysis <img src="https://emoji.discourse-cdn.com/twitter/100.png?v=12" title=":100:" class="emoji" alt=":100:" loading="lazy" width="20" height="20"></p>
<p>Issue is now tracked in <a href="https://github.com/Slicer/slicer_download/issues/28" class="inline-onebox">Download backend: Disable or add support for HTTP range requests · Issue #28 · Slicer/slicer_download · GitHub</a></p>

---

## Post #16 by @lassoan (2023-08-23 08:22 UTC)

<p>2 posts were split to a new topic: <a href="/t/white-screen-when-launching-slicer-on-older-laptop/31310">White screen when launching Slicer on older laptop</a></p>

---
