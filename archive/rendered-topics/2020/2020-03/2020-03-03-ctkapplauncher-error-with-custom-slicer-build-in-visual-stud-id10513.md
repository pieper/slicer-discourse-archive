---
topic_id: 10513
title: "Ctkapplauncher Error With Custom Slicer Build In Visual Stud"
date: 2020-03-03
url: https://discourse.slicer.org/t/10513
---

# CTKAPPLAUNCHER error with custom Slicer build in Visual Studio

**Topic ID**: 10513
**Date**: 2020-03-03
**URL**: https://discourse.slicer.org/t/ctkapplauncher-error-with-custom-slicer-build-in-visual-studio/10513

---

## Post #1 by @aptirumalai (2020-03-03 08:25 UTC)

<p>I am getting failures with a custom Slicer application that Kitware had helped us develop 3 years ago. Most of the projects build fine. The issue is with the CTKAPPLAUNCHER project.</p>
<p>From what I can tell, it appears to have to do with a failure to download CTKAppLauncher-0.1.14-win-i386.tar.gz from <a href="http://packages.kitware.com" rel="nofollow noopener">packages.kitware.com</a>. This used to work fine. This application is built in Visual Studio 2013 Community Edition.</p>
<p>Here’s the relevant build output:<br>
InitializeBuildStatus:<br>
Touching “x64\Release\CTKAPPLAUNCHER\CTKAPPLAUNCHER.tlog\unsuccessfulbuild”.<br>
CustomBuild:<br>
Building Custom Rule C:/D/SPMTR-rel/Slicer/CMakeLists.txt<br>
CMake does not need to re-run because C:\D\SPMTR-rel\S-bld\CMakeFiles\generate.stamp is up-to-date.<br>
Creating directories for ‘CTKAPPLAUNCHER’<br>
Performing download step (download, verify and extract) for ‘CTKAPPLAUNCHER’<br>
– downloading…<br>
src=‘<a href="http://packages.kitware.com/api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz" rel="nofollow noopener">http://packages.kitware.com/api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz</a>’<br>
dst=‘C:/D/SPMTR-rel/S-bld/CTKAPPLAUNCHER-prefix/src/method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz’<br>
timeout=‘none’<br>
– [download 100% complete]<br>
CMake Error at CTKAPPLAUNCHER-prefix/src/CTKAPPLAUNCHER-stamp/download-CTKAPPLAUNCHER.cmake:27 (message):<br>
CUSTOMBUILD : error : downloading [C:\D\SPMTR-rel\S-bld\CTKAPPLAUNCHER.vcxproj]<br>
‘<a href="http://packages.kitware.com/api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz" rel="nofollow noopener">http://packages.kitware.com/api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz</a>’<br>
failed</p>
<pre><code>    status_code: 22
    status_string: "HTTP response code said error"
    log: timeout on name lookup is not supported

  Hostname was NOT found in DNS cache

    Trying 66.194.253.18...

  Connected to packages.kitware.com (66.194.253.18) port 80 (#0)

  GET
  /api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz
  HTTP/1.1


  User-Agent: curl/7.38.0


  Host: packages.kitware.com


  Accept: */*


  


  HTTP/1.1 301 Moved Permanently


  Date: Mon, 02 Mar 2020 21:28:05 GMT


  Server Apache is not blacklisted

  Server: Apache


  X-Frame-Options: SAMEORIGIN


  Location:
  https://packages.kitware.com/api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz



  Content-Length: 332


  Content-Type: text/html; charset=iso-8859-1


  


  Ignoring the response-body

  &lt;!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN"&gt;

  &lt;html&gt;&lt;head&gt;

  &lt;title&gt;301 Moved Permanently&lt;/title&gt;

  &lt;/head&gt;&lt;body&gt;

  &lt;h1&gt;Moved Permanently&lt;/h1&gt;

  &lt;p&gt;The document has moved &lt;a
  href="https://packages.kitware.com/api/rest?method=midas.item.download&amp;amp;id=7565&amp;amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz"&gt;here&lt;/a&gt;.&lt;/p&gt;


  &lt;/body&gt;&lt;/html&gt;

  Connection #0 to host packages.kitware.com left intact

  Issue another request to this URL:
  'https://packages.kitware.com/api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz'


  Found bundle for host packages.kitware.com: 0x2677a30

  timeout on name lookup is not supported

  Hostname was NOT found in DNS cache

    Trying 66.194.253.18...

  Connected to packages.kitware.com (66.194.253.18) port 443 (#1)

  schannel: SSL/TLS connection with packages.kitware.com port 443 (step 1/3)

  schannel: disable server certificate revocation checks

  schannel: sending initial handshake data: sending 176 bytes...

  schannel: sent initial handshake data: sent 176 bytes

  schannel: SSL/TLS connection with packages.kitware.com port 443 (step 2/3)

  schannel: failed to receive handshake, need more data

  schannel: SSL/TLS connection with packages.kitware.com port 443 (step 2/3)

  schannel: encrypted data buffer: offset 2988 length 4096

  schannel: sending next handshake data: sending 126 bytes...

  schannel: SSL/TLS connection with packages.kitware.com port 443 (step 2/3)

  schannel: encrypted data buffer: offset 274 length 4096

  schannel: SSL/TLS handshake complete

  schannel: SSL/TLS connection with packages.kitware.com port 443 (step 3/3)

  schannel: incremented credential handle refcount = 1

  schannel: stored credential handle in session cache

  GET
  /api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz
  HTTP/1.1


  User-Agent: curl/7.38.0


  Host: packages.kitware.com


  Accept: */*

  schannel: client wants to read 16384 bytes

  schannel: encrypted data buffer: offset 0 length 16384

  schannel: encrypted data got 521

  schannel: encrypted data buffer: offset 521 length 16384

  schannel: decrypted data length: 492

  schannel: decrypted data added: 492

  schannel: decrypted data cached: offset 492 length 16384

  schannel: decrypted data buffer: offset 492 length 16384

  schannel: decrypted data returned 492

  schannel: decrypted data buffer: offset 0 length 16384
</code></pre>
<p>CUSTOMBUILD : The requested URL returned error : 403 Forbidden [C:\D\SPMTR-rel\S-bld\CTKAPPLAUNCHER.vcxproj]</p>
<pre><code>  Closing connection 1

  schannel: shutting down SSL/TLS connection with packages.kitware.com port
  443

  schannel: clear security context handle

  schannel: decremented credential handle refcount = 0
</code></pre>
<p>Done Building Project “C:\D\SPMTR-rel\S-bld\CTKAPPLAUNCHER.vcxproj” (default targets) – FAILED.</p>

---

## Post #2 by @Sam_Horvath (2020-03-03 15:45 UTC)

<p>Hi:</p>
<p>I am looking at this and will get back to you.</p>

---

## Post #3 by @aptirumalai (2020-03-07 22:37 UTC)

<p>Sam,<br>
I have been looking into this too - just trying to get it to build to make some progress. This is what I have discovered so far.</p>
<ul>
<li>
<p>The issue is with the CTKAPPLAUNCHER project</p>
</li>
<li>
<p>CTKAPPLAUNCHER-prefix\src\CTKAPPLAUNCHER-stamp\download-CTKAPPLAUNCHER.cmake is where the issue originates. There is a file download command here:</p>
</li>
</ul>
<pre><code class="lang-auto">file(DOWNLOAD
  "http://packages.kitware.com/api/rest?method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz"
  "C:/W/SPMTR-rel/S-bld/CTKAPPLAUNCHER-prefix/src/method=midas.item.download&amp;id=7565&amp;dummy=CTKAppLauncher-0.1.14-win-i386.tar.gz"
  SHOW_PROGRESS
  # no TIMEOUT
  STATUS status
  LOG log)
</code></pre>
<ul>
<li>
<p>This download fails - apparently this tar.gz file does not exist on <a href="http://packages.kitware.com" rel="nofollow noopener">packages.kitware.com</a> any more.</p>
</li>
<li>
<p>I was able to find this tar.gz file at: <a href="https://github.com/commontk/AppLauncher/releases/tag/v0.1.14" rel="nofollow noopener">https://github.com/commontk/AppLauncher/releases/tag/v0.1.14</a></p>
</li>
<li>
<p>I downloaded this file.</p>
</li>
<li>
<p>I then modified the following files to use this downloaded file instead:<br>
download-CTKAPPLAUNCHER.cmake<br>
verify-CTKAPPLAUNCHER.cmake<br>
extract-CTKAPPLAUNCHER.cmake<br>
This hack appears to at least successfully build CTKAPPLAUNCHER</p>
</li>
</ul>
<p>Just wanted to share this with you.</p>
<p>Regards,<br>
Arun</p>
<p>PS: JC was our principal consultant at Kitware when we worked on this about 3 years back. So he might be worth asking. We had a contract with Kitware for this work.</p>

---
