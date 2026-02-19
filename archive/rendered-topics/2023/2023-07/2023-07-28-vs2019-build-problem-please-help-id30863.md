---
topic_id: 30863
title: "Vs2019 Build Problem Please Help"
date: 2023-07-28
url: https://discourse.slicer.org/t/30863
---

# vs2019 build problem, please help

**Topic ID**: 30863
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/vs2019-build-problem-please-help/30863

---

## Post #1 by @zswin (2023-07-28 19:31 UTC)

<ul>
<li>Operating system: windows10 professional</li>
<li>Slicer version: 5.2 I think</li>
<li>Expected behavior:</li>
<li>Actual behavior: got 8 errors while building(debug x64)</li>
<li>BUILD WITH VS2019</li>
<li>cmake :3.26.4</li>
<li>Qt: 5.15.2</li>
</ul>
<h3><a name="p-98330-err-msg-1" class="anchor" href="#p-98330-err-msg-1" aria-label="Heading link"></a>Err Msg</h3>
<pre><code class="lang-auto">Error	MSB8066	“D:\R\CMakeFiles\2a00df8f2ee7b3e66170519024eabeb5\ITK-mkdir.rule;D:\R\CMakeFiles\2a00df8f2ee7b3e66170519024eabeb5\ITK-download.rule;D:\R\CMakeFiles\2a00df8f2ee7b3e66170519024eabeb5\ITK-update.rule;D:\R\CMakeFiles\2a00df8f2ee7b3e66170519024eabeb5\ITK-patch.rule;D:\R\CMakeFiles\2a00df8f2ee7b3e66170519024eabeb5\ITK-configure.rule;D:\R\CMakeFiles\2a00df8f2ee7b3e66170519024eabeb5\ITK-build.rule;D:\R\CMakeFiles\2a00df8f2ee7b3e66170519024eabeb5\ITK-generate_project_description.rule;D:\R\CMakeFiles\2a00df8f2ee7b3e66170519024eabeb5\ITK-install.rule;D:\R\CMakeFiles\685585194e4f07a5284e025cc2950b86\ITK-complete.rule;D:\R\CMakeFiles\b953c46a80b9fa9421ab3b55ff57190e\ITK.rule;D:\S\CMakeLists.txt”custom generation exited, code 1	ITK	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
Error	MSB8066	“D:\R\CMakeFiles\56963f57fba68e2964c1355ce9fb4c7b\SimpleITK-mkdir.rule;D:\R\CMakeFiles\56963f57fba68e2964c1355ce9fb4c7b\SimpleITK-download.rule;D:\R\CMakeFiles\56963f57fba68e2964c1355ce9fb4c7b\SimpleITK-update.rule;D:\R\CMakeFiles\56963f57fba68e2964c1355ce9fb4c7b\SimpleITK-patch.rule;D:\R\CMakeFiles\56963f57fba68e2964c1355ce9fb4c7b\SimpleITK-configure.rule;D:\R\CMakeFiles\56963f57fba68e2964c1355ce9fb4c7b\SimpleITK-build.rule;D:\R\CMakeFiles\56963f57fba68e2964c1355ce9fb4c7b\SimpleITK-install.rule;D:\R\CMakeFiles\685585194e4f07a5284e025cc2950b86\SimpleITK-complete.rule;D:\R\CMakeFiles\b953c46a80b9fa9421ab3b55ff57190e\SimpleITK.rule;D:\S\CMakeLists.txt”custom generation exited, code 1	SimpleITK	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
Error	MSB8066	“D:\R\CMakeFiles\a919682ba9a9b7a9c4eff3108a0c2533\SlicerExecutionModel-mkdir.rule;D:\R\CMakeFiles\a919682ba9a9b7a9c4eff3108a0c2533\SlicerExecutionModel-download.rule;D:\R\CMakeFiles\a919682ba9a9b7a9c4eff3108a0c2533\SlicerExecutionModel-update.rule;D:\R\CMakeFiles\a919682ba9a9b7a9c4eff3108a0c2533\SlicerExecutionModel-patch.rule;D:\R\CMakeFiles\a919682ba9a9b7a9c4eff3108a0c2533\SlicerExecutionModel-configure.rule;D:\R\CMakeFiles\a919682ba9a9b7a9c4eff3108a0c2533\SlicerExecutionModel-build.rule;D:\R\CMakeFiles\a919682ba9a9b7a9c4eff3108a0c2533\SlicerExecutionModel-generate_project_description.rule;D:\R\CMakeFiles\a919682ba9a9b7a9c4eff3108a0c2533\SlicerExecutionModel-install.rule;D:\R\CMakeFiles\685585194e4f07a5284e025cc2950b86\SlicerExecutionModel-complete.rule;D:\R\CMakeFiles\b953c46a80b9fa9421ab3b55ff57190e\SlicerExecutionModel.rule;D:\S\CMakeLists.txt”custom generation exited, code 1	SlicerExecutionModel	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
Error	MSB8066	“D:\R\CMakeFiles\8de523c90162fa6ec802ee5ccd4a8903\python-dicom-requirements-mkdir.rule;D:\R\CMakeFiles\8de523c90162fa6ec802ee5ccd4a8903\python-dicom-requirements-download.rule;D:\R\CMakeFiles\8de523c90162fa6ec802ee5ccd4a8903\python-dicom-requirements-update.rule;D:\R\CMakeFiles\8de523c90162fa6ec802ee5ccd4a8903\python-dicom-requirements-patch.rule;D:\R\CMakeFiles\8de523c90162fa6ec802ee5ccd4a8903\python-dicom-requirements-configure.rule;D:\R\CMakeFiles\8de523c90162fa6ec802ee5ccd4a8903\python-dicom-requirements-build.rule;D:\R\CMakeFiles\8de523c90162fa6ec802ee5ccd4a8903\python-dicom-requirements-generate_project_description.rule;D:\R\CMakeFiles\8de523c90162fa6ec802ee5ccd4a8903\python-dicom-requirements-install.rule;D:\R\CMakeFiles\685585194e4f07a5284e025cc2950b86\python-dicom-requirements-complete.rule;D:\R\CMakeFiles\b953c46a80b9fa9421ab3b55ff57190e\python-dicom-requirements.rule;D:\S\CMakeLists.txt”custom generation exited, code 1	python-dicom-requirements	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
Error	MSB8066	“D:\R\CTK-build\CMakeFiles\47b96cb8080aec385a18ae8753d6f6a1\CTK-mkdir.rule;D:\R\CTK-build\CMakeFiles\47b96cb8080aec385a18ae8753d6f6a1\CTK-download.rule;D:\R\CTK-build\CMakeFiles\47b96cb8080aec385a18ae8753d6f6a1\CTK-update.rule;D:\R\CTK-build\CMakeFiles\47b96cb8080aec385a18ae8753d6f6a1\CTK-patch.rule;D:\R\CTK-build\CMakeFiles\47b96cb8080aec385a18ae8753d6f6a1\CTK-configure.rule;D:\R\CTK-build\CMakeFiles\47b96cb8080aec385a18ae8753d6f6a1\CTK-build.rule;D:\R\CTK-build\CMakeFiles\47b96cb8080aec385a18ae8753d6f6a1\CTK-forceconfigure.rule;D:\R\CTK-build\CMakeFiles\47b96cb8080aec385a18ae8753d6f6a1\CTK-install.rule;D:\R\CTK-build\CMakeFiles\2417c1e6ecc37b5c6621b44acea10d7e\CTK-complete.rule;D:\R\CTK-build\CMakeFiles\b3a155c1c60e235b2cd6682b7a62e794\CTK.rule;D:\R\CTK\CMakeLists.txt”custom generation exited, code 1 [D:\R\CTK-build\CTK.vcxproj]	CTK	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
Error	MSB8066	“D:\R\CMakeFiles\affded9edbdd4b0823de4937f9352d02\CTK-mkdir.rule;D:\R\CMakeFiles\affded9edbdd4b0823de4937f9352d02\CTK-download.rule;D:\R\CMakeFiles\affded9edbdd4b0823de4937f9352d02\CTK-update.rule;D:\R\CMakeFiles\affded9edbdd4b0823de4937f9352d02\CTK-patch.rule;D:\R\CMakeFiles\affded9edbdd4b0823de4937f9352d02\CTK-configure.rule;D:\R\CMakeFiles\affded9edbdd4b0823de4937f9352d02\CTK-build.rule;D:\R\CMakeFiles\affded9edbdd4b0823de4937f9352d02\CTK-generate_project_description.rule;D:\R\CMakeFiles\affded9edbdd4b0823de4937f9352d02\CTK-install.rule;D:\R\CMakeFiles\685585194e4f07a5284e025cc2950b86\CTK-complete.rule;D:\R\CMakeFiles\b953c46a80b9fa9421ab3b55ff57190e\CTK.rule;D:\S\CMakeLists.txt”custom generation exited, code 1	CTK	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
Error	MSB8066	“D:\R\CMakeFiles\e0d658c0435eb240d058300f3ecfeea6\python-scipy-mkdir.rule;D:\R\CMakeFiles\e0d658c0435eb240d058300f3ecfeea6\python-scipy-download.rule;D:\R\CMakeFiles\e0d658c0435eb240d058300f3ecfeea6\python-scipy-update.rule;D:\R\CMakeFiles\e0d658c0435eb240d058300f3ecfeea6\python-scipy-patch.rule;D:\R\CMakeFiles\e0d658c0435eb240d058300f3ecfeea6\python-scipy-configure.rule;D:\R\CMakeFiles\e0d658c0435eb240d058300f3ecfeea6\python-scipy-build.rule;D:\R\CMakeFiles\e0d658c0435eb240d058300f3ecfeea6\python-scipy-generate_project_description.rule;D:\R\CMakeFiles\e0d658c0435eb240d058300f3ecfeea6\python-scipy-install.rule;D:\R\CMakeFiles\685585194e4f07a5284e025cc2950b86\python-scipy-complete.rule;D:\R\CMakeFiles\b953c46a80b9fa9421ab3b55ff57190e\python-scipy.rule;D:\S\CMakeLists.txt”custom generation exited, code 1	python-scipy	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
Error	MSB8066	“D:\R\CMakeFiles\4dc4d65868ae7c14fe3a4b6ad207d8ee\Slicer-mkdir.rule;D:\R\CMakeFiles\4dc4d65868ae7c14fe3a4b6ad207d8ee\Slicer-download.rule;D:\R\CMakeFiles\4dc4d65868ae7c14fe3a4b6ad207d8ee\Slicer-update.rule;D:\R\CMakeFiles\4dc4d65868ae7c14fe3a4b6ad207d8ee\Slicer-patch.rule;D:\R\CMakeFiles\4dc4d65868ae7c14fe3a4b6ad207d8ee\Slicer-configure.rule;D:\R\CMakeFiles\4dc4d65868ae7c14fe3a4b6ad207d8ee\Slicer-build.rule;D:\R\CMakeFiles\4dc4d65868ae7c14fe3a4b6ad207d8ee\Slicer-forceconfigure.rule;D:\R\CMakeFiles\4dc4d65868ae7c14fe3a4b6ad207d8ee\Slicer-install.rule;D:\R\CMakeFiles\685585194e4f07a5284e025cc2950b86\Slicer-complete.rule;D:\R\CMakeFiles\b953c46a80b9fa9421ab3b55ff57190e\Slicer.rule;D:\S\CMakeLists.txt”custom generation exited, code 1	Slicer	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
</code></pre>

---

## Post #2 by @lassoan (2023-07-28 19:33 UTC)

<p>You need to use 64-bit <code>Visual Studio 2022 v143 toolset</code> as described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">build instructions</a>.</p>

---

## Post #3 by @zswin (2023-08-03 04:36 UTC)

<p>dear Andras Loass, I have installed vs2022, but there were still some problems, can I send you e-mal, coz the err message is kind of too big to post</p>

---

## Post #4 by @lassoan (2023-08-03 04:37 UTC)

<p>You can upload the build log somewhere and post the link here.</p>

---

## Post #5 by @zswin (2023-08-03 05:00 UTC)

<p><a href="https://hotfile.io/Jb85c96az8/err0803_txt" class="onebox" target="_blank" rel="noopener nofollow ugc">https://hotfile.io/Jb85c96az8/err0803_txt</a><br>
please check if you can download the log file</p>

---

## Post #6 by @jcfr (2023-08-03 05:07 UTC)

<p>Thanks for uploading the log, this was helpful.</p>
<p>After inspecting it, the first error is related to the download of the Python sources:</p>
<pre><code class="lang-plaintext">[...]
Performing download step (download, verify and extract) for 'python-source'
-- Downloading...
   dst='D:/R/Python-3.9.10.tgz'
   timeout='none'
   inactivity timeout='none'
-- Using src='https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz'
-- [download 0% complete]
-- [download 1% complete]
[...]
-- [download 89% complete]
-- [download 90% complete]
-- [download 91% complete]
CMake Error at python-source-prefix/src/python-source-stamp/download-python-source.cmake:170 (message):
  Each download failed!

CUSTOMBUILD : error : downloading 'https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz' failed
          status_code: 92
          status_string: "Stream error in the HTTP/2 framing layer"
          log:
          --- LOG BEGIN ---
          timeout on name lookup is not supported
    Trying 151.101.108.223:443...

  Connected to www.python.org (151.101.108.223) port 443 (#0)

  schannel: disabled automatic use of client certificate

  ALPN: offers h2

  ALPN: offers http/1.1

  ALPN: server accepted h2

  Using HTTP2, server supports multiplexing

  Copying HTTP/2 data in stream buffer to connection buffer after upgrade:
  len=0
[...]
  schannel: failed to decrypt data, need more data
[...]
  [2626 bytes data]

  HTTP/2 stream 0 was not closed cleanly: PROTOCOL_ERROR (err 1)

  Connection #0 to host www.python.org left intact
</code></pre>

---

## Post #7 by @jcfr (2023-08-03 05:20 UTC)

<p>It turns out that the download of any archive over https is not working … (e.g download of <code>swigwin-4.0.2.zip</code> is also failing)</p>
<p>Could you try the following ?</p>
<h3><a name="p-98573-h-1-slicercheckcmakehttps-1" class="anchor" href="#p-98573-h-1-slicercheckcmakehttps-1" aria-label="Heading link"></a>(1) SlicerCheckCMakeHTTPS</h3>
<p>Can you run the following command ?</p>
<pre><code class="lang-auto">cmake -P D:/S/CMake/SlicerCheckCMakeHTTPS.cmake
</code></pre>
<p>The following output is expected:</p>
<pre><code class="lang-plaintext">-- Checking if CMake supports https
-- Checking if CMake supports https - ok
</code></pre>
<h3><a name="p-98573-h-2-download-of-files-using-the-web-browser-2" class="anchor" href="#p-98573-h-2-download-of-files-using-the-web-browser-2" aria-label="Heading link"></a>(2) Download of files using the web browser</h3>
<p>Can you download the following files, locally compute their checksum and confirm they match the one reported below ?</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Link</th>
<th>SHA512</th>
</tr>
</thead>
<tbody>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td><a href="https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz">https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz</a></td>
<td><code>3dc9e6a470a0922bad4856db02bc82cc4174f7a94e355fd0ed8cf9bbfd82dcf0b09d854aa482fe70ed441919a526d49e74658222279b5a25b4aa4fa171f65e9c</code></td>
</tr>
<tr>
<td><a href="https://github.com/Slicer/SlicerBinaryDependencies/releases/download/swig/swigwin-4.0.2.zip">https://github.com/Slicer/SlicerBinaryDependencies/releases/download/swig/swigwin-4.0.2.zip</a></td>
<td><code>b8f105f9b9db6acc1f6e3741990915b533cd1bc206eb9645fd6836457fd30789b7229d2e3219d8e35f2390605ade0fbca493ae162ec3b4bc4e428b57155db03d</code></td>
</tr>
</tbody>
</table>
</div><pre><code class="lang-auto"></code></pre>

---

## Post #8 by @jcfr (2023-08-03 05:56 UTC)

<h3><a name="p-98575-h-3-slicercheckcmakehttpsdownload-1" class="anchor" href="#p-98575-h-3-slicercheckcmakehttpsdownload-1" aria-label="Heading link"></a>(3) SlicerCheckCMakeHTTPSDownload</h3>
<p>Finally, you could try running the script <code>SlicerCheckCMakeHTTPSDownload.cmake</code> following the instructions linked below.</p>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/jcfr/e9a281f71b48f52ca6a5ebb903533d62?permalink_comment_id=4650046#gistcomment-4650046">
  <header class="source">

      <a href="https://gist.github.com/jcfr/e9a281f71b48f52ca6a5ebb903533d62?permalink_comment_id=4650046#gistcomment-4650046" target="_blank" rel="noopener">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/jcfr/e9a281f71b48f52ca6a5ebb903533d62?permalink_comment_id=4650046#gistcomment-4650046" target="_blank" rel="noopener">https://gist.github.com/jcfr/e9a281f71b48f52ca6a5ebb903533d62?permalink_comment_id=4650046#gistcomment-4650046</a></h4>

  <h5>SlicerCheckCMakeHTTPSDownload.cmake</h5>
  <pre><code class="CMake"># SPDX-FileCopyrightText: Copyright 2023 Kitware, Inc. and Contributors
# SPDX-License-Identifier: BSD-3-Clause

# Adapted from https://github.com/Kitware/CMake/blob/v3.27.1/Modules/ExternalProject/download.cmake.in
function(check_file_hash filepath expected_value)

  if("${filepath}" STREQUAL "")
    message(FATAL_ERROR "filepath Can't be empty")
  endif()
</code></pre>
   This file has been truncated. <a href="https://gist.github.com/jcfr/e9a281f71b48f52ca6a5ebb903533d62?permalink_comment_id=4650046#gistcomment-4650046" target="_blank" rel="noopener">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The, consider reporting back your findings.</p>

---

## Post #9 by @zswin (2023-08-03 06:19 UTC)

<p>– Checking if CMake supports https<br>
CMake Error at /CMake/SlicerCheckCMakeHTTPS.cmake:33 (message):<br>
error: “Couldn’t resolve host name”<br>
Call Stack (most recent call first):<br>
/CMake/SlicerCheckCMakeHTTPS.cmake:43 (slicer_check_cmake_https)</p>
<p>it didn’t work, I don’t understand, but I can download those packages in browser… what am I suppose to do now?</p>

---

## Post #10 by @zswin (2023-08-03 06:31 UTC)

<p>D:\S\CMake&gt;cmake -P SlicerCheckCMakeHTTPSDownload.cmake<br>
– Checking if CMake https download works for ‘<a href="https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz" rel="noopener nofollow ugc">https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz</a>’<br>
CMake Error at SlicerCheckCMakeHTTPSDownload.cmake:55 (message):<br>
error: “Timeout was reached”<br>
Call Stack (most recent call first):<br>
SlicerCheckCMakeHTTPSDownload.cmake:69 (slicer_check_cmake_https_download)</p>

---

## Post #11 by @jcfr (2023-08-03 07:46 UTC)

<p>It seems there are issues<sup class="footnote-ref"><a href="#footnote-98583-1" id="footnote-ref-98583-1">[1]</a></sup><sup class="footnote-ref"><a href="#footnote-98583-2" id="footnote-ref-98583-2">[2]</a></sup> with newer TLS protocols.</p>
<p>You could try to workaround the issue by downloading these files into the top-level build directory and attempt to resume the build.</p>
<p>Here are the files to download into <code>D:\R</code></p>
<div class="md-table">
<table>
<thead>
<tr>
<th>URL</th>
<th>Checksum</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://github.com/commontk/AppLauncher/releases/download/v$%7Blauncher_version%7D/CTKAppLauncher-0.1.31-win-i386.tar.gz">https://github.com/commontk/AppLauncher/releases/download/v${launcher_version}/CTKAppLauncher-0.1.31-win-i386.tar.gz</a></td>
<td>MD5: 3bbe3823b6950f342dd922fab32d643d</td>
</tr>
<tr>
<td><a href="https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz">https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz</a></td>
<td>MD5: f59547c480420199081b94e96df292ec</td>
</tr>
<tr>
<td><a href="https://github.com/Slicer/Slicer-OpenSSL/releases/download/1.1.1g/OpenSSL_1_1_1g-install-msvc1900-64.tar.gz">https://github.com/Slicer/Slicer-OpenSSL/releases/download/1.1.1g/OpenSSL_1_1_1g-install-msvc1900-64.tar.gz</a></td>
<td>MD5: f89ea6a4fcfb279af30cbe01c1d7f879</td>
</tr>
<tr>
<td><a href="https://github.com/Slicer/SlicerBinaryDependencies/releases/download/swig/swigwin-3.24.zip">https://github.com/Slicer/SlicerBinaryDependencies/releases/download/swig/swigwin-3.24.zip</a></td>
<td>SHA512: b8f105f9b9db6acc1f6e3741990915b533cd1bc206eb9645fd6836457fd30789b7229d2e3219d8e35f2390605ade0fbca493ae162ec3b4bc4e428b57155db03d</td>
</tr>
<tr>
<td><a href="https://github.com/oneapi-src/oneTBB/releases/download/v2021.5.0/oneapi-tbb-2021.5.0-win.zip">https://github.com/oneapi-src/oneTBB/releases/download/v2021.5.0/oneapi-tbb-2021.5.0-win.zip</a></td>
<td>SHA256: 096c004c7079af89fe990bb259d58983b0ee272afa3a7ef0733875bfe09fcd8e</td>
</tr>
<tr>
<td><a href="https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz">https://www.python.org/ftp/python/3.9.10/Python-3.9.10.tgz</a></td>
<td>SHA512 3dc9e6a470a0922bad4856db02bc82cc4174f7a94e355fd0ed8cf9bbfd82dcf0b09d854aa482fe70ed441919a526d49e74658222279b5a25b4aa4fa171f65e9c</td>
</tr>
</tbody>
</table>
</div><hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-98583-1" class="footnote-item"><p><a href="https://www.zdnet.com/article/china-is-now-blocking-all-encrypted-https-traffic-using-tls-1-3-and-esni/" class="inline-onebox">China is now blocking all encrypted HTTPS traffic that uses TLS 1.3 and ESNI | ZDNET</a> <a href="#footnote-ref-98583-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-98583-2" class="footnote-item"><p><a href="https://mailarchive.ietf.org/arch/msg/tls/Dae-cukKMqfzmTT4Ksh1Bzlx7ws/" class="inline-onebox">Re: [TLS] Possible blocking of Encrypted SNI extension in China</a> <a href="#footnote-ref-98583-2" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #12 by @zswin (2023-08-04 03:48 UTC)

<p>(<a href="https://github.com/commontk/AppLauncher/releases/download/v$%7Blauncher_version%7D/CTKAppLauncher-0.1.31-win-i386.tar.gz" rel="noopener nofollow ugc">https://github.com/commontk/AppLauncher/releases/download/v${launcher_version}/CTKAppLauncher-0.1.31-win-i386.tar.gz</a>)<br>
I’m sorry but I can NOT download this file, the browser reads ‘Not Found’, is there any alternative way to download this package?thank you</p>

---

## Post #13 by @jcfr (2023-08-04 04:03 UTC)

<p>Look like I incorrectly composted the URL and forgot to replace <code>${launcher_version}</code> with <code>0.1.31</code>.</p>
<p>In this case, you should use:</p>
<ul>
<li><a href="https://github.com/commontk/AppLauncher/releases/download/v0.1.31/CTKAppLauncher-0.1.31-win-i386.tar.gz">https://github.com/commontk/AppLauncher/releases/download/v0.1.31/CTKAppLauncher-0.1.31-win-i386.tar.gz</a></li>
</ul>
<h2><a name="p-98622-background-1" class="anchor" href="#p-98622-background-1" aria-label="Heading link"></a>Background</h2>
<p>For future reference, the corresponding URLs have been put together looking at the external projects (see <code>External_*.cmake</code> files in <a href="https://github.com/Slicer/Slicer/tree/main/SuperBuild">Slicer/SuperBuild</a>) downloading files.</p>
<p>Note that <code>PCRE</code> archive is not used on Windows. This can be confirmed by inspecting the  <code>External_PCRE.cmake</code> file.</p>
<pre data-code-wrap="bash"><code class="lang-bash">cd /path/to/src/Slicer/SuperBuild

$ ack "\sURL "
External_CTKAPPLAUNCHER.cmake
43:      URL https://github.com/commontk/AppLauncher/releases/download/v${launcher_version}/${CTKAppLauncherFileName}

External_CTKResEdit.cmake
37:    URL ${url}

External_Swig.cmake
32:      URL https://github.com/Slicer/SlicerBinaryDependencies/releases/download/swig/swigwin-${SWIG_TARGET_VERSION}.zip
98:      URL https://github.com/Slicer/SlicerBinaryDependencies/releases/download/swig/swig-${SWIG_TARGET_VERSION}.tar.gz

External_PCRE.cmake
54:    URL https://github.com/Slicer/SlicerBinaryDependencies/releases/download/PCRE/pcre-${_version}.tar.gz

External_OpenSSL.cmake
154:      URL ${OpenSSL_${OPENSSL_DOWNLOAD_VERSION}_URL}
307:      URL ${OpenSSL_${OPENSSL_DOWNLOAD_VERSION}_${MSVC_VERSION}_URL}

External_tbb.cmake
42:  URL https://github.com/oneapi-src/oneTBB/releases/download/v${tbb_ver}/${tbb_file}

External_python.cmake
66:    URL ${_download_${Slicer_REQUIRED_PYTHON_VERSION}_url}
</code></pre>

---

## Post #14 by @zswin (2023-08-07 01:06 UTC)

<p>Dear Jcfr:<br>
I still got problems when doing the ‘ALL_BUILD’, this time it stuck in ‘cloning to VTK…’ ,can you please check the log file, maybe I should download more packages before hand?<br>
<a href="https://hotfile.io/X5bcW665z2/err0806_txt" class="onebox" target="_blank" rel="noopener nofollow ugc">https://hotfile.io/X5bcW665z2/err0806_txt</a></p>

---

## Post #15 by @zswin (2023-08-08 09:22 UTC)

<p><a href="https://hotfile.io/R3s7la7fzf/err0808_txt" class="onebox" target="_blank" rel="noopener nofollow ugc">https://hotfile.io/R3s7la7fzf/err0808_txt</a></p>
<p>please help…</p>

---
