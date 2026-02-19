---
topic_id: 13197
title: "Build Failure Windows"
date: 2020-08-27
url: https://discourse.slicer.org/t/13197
---

# Build Failure (Windows)

**Topic ID**: 13197
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/build-failure-windows/13197

---

## Post #1 by @jrl (2020-08-27 16:31 UTC)

<p>I am having trouble with the initial build. I think Qt, CMake, and Git are installed correctly. However, with Visual Studio, the instructions provided say “when configuring the installer, enable installation of Visual Studio 2019 (v142) toolset and component Programming languages / Visual C++ / Common Tools for Visual C++ (in some distributions, this option is not enabled by default)”. However, I do not see any option to select/install “component Programming languages / Visual C++ / Common Tools for Visual C++”, and I haven’t discovered anything online. I am unsure if this is related to my build failure but wanted to address this issue first.</p>

---

## Post #2 by @jamesobutler (2020-08-27 16:53 UTC)

<p>The toolsets are optional things to install as part of the Visual Studio installation. In the Visual Studio Installer it looks like the following. I’ve highlighted the areas where you can select various toolkits.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43d5ae5808f5aac95201be8083d8fef6d7416f74.png" data-download-href="/uploads/short-url/9G5NBguUaat0YaE0QjII0n1VwiM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43d5ae5808f5aac95201be8083d8fef6d7416f74_2_690x373.png" alt="image" data-base62-sha1="9G5NBguUaat0YaE0QjII0n1VwiM" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43d5ae5808f5aac95201be8083d8fef6d7416f74_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43d5ae5808f5aac95201be8083d8fef6d7416f74_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43d5ae5808f5aac95201be8083d8fef6d7416f74_2_1380x746.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @jrl (2020-08-27 18:16 UTC)

<p>Okay I included that one item checked off (MSVC v142 -VS 2019…) at the top in the installation process.</p>
<p>I am able to run this command without error -<br>
“C:\Program Files\CMake\bin\cmake.exe” -G “Visual Studio 16 2019” -A x64 -DQt5_DIR:PATH=C:\Qt\5.15.0\msvc2019_64\lib\cmake\Qt5 “C:\D\S4”</p>
<p>The output is “Build files have been written to :C/D/S4D”</p>
<p>However, the second command yields errors and large output<br>
“C:\Program Files\CMake\bin\cmake.exe” --build . --config Debug"</p>
<p>This isn’t the full output but some of the errors include:</p>
<ol>
<li>
</li></ol>
<p>" Cloning into ‘DCMTK’…<br>
fatal: unable to look up <a href="http://git.dcmtk.org" rel="nofollow noopener">git.dcmtk.org</a> (port 9418) (No such host is known. )"</p>
<ol start="2">
<li>
</li></ol>
<p>“C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(234,5): error MSB6006: “cmd.exe” exited with code 1. [C:\D\S4D\DCMTK.vcxproj]”</p>
<ol start="3">
<li>
</li></ol>
<p>"CUSTOMBUILD : error : downloading ‘<a href="https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz" rel="nofollow noopener">https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz</a>’ failed [C:\D\S4D\CTKResEdit.vcxproj]<br>
status_code: 6<br>
status_string: “Couldn’t resolve host name”<br>
log:<br>
— LOG BEGIN —<br>
timeout on name lookup is not supported</p>
<pre><code>getaddrinfo(3) failed for github.com:443

Couldn't resolve host 'github.com'

Closing connection 0"
</code></pre>
<ol start="4">
<li>
</li></ol>
<p>" Check for working CXX compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.27.29110/bin/Hostx64/x64/cl.exe - skipped"</p>
<hr>
<p>I thought perhaps it was a proxy issue given that “no such host is known”. However, I don’t believe that to be the case. Thanks.</p>

---

## Post #4 by @jamesobutler (2020-08-27 18:23 UTC)

<p>Try again. <a href="https://git.dcmtk.org/" rel="nofollow noopener">https://git.dcmtk.org/</a> might’ve been temporarily down.</p>

---

## Post #6 by @jrl (2020-08-28 18:33 UTC)

<p>I have noticed other failures in regards to git. Here is some of the output.</p>
<hr>
<p>Completed ‘zlib’<br>
Building Custom Rule C:/D/S4/CMakeLists.txt<br>
Creating directories for ‘DCMTK’<br>
Performing download step (git clone) for ‘DCMTK’<br>
Cloning into ‘DCMTK’…<br>
fatal: unable to look up <a href="http://git.dcmtk.org" rel="nofollow noopener">git.dcmtk.org</a> (port 9418) (No such host is known. )<br>
…<br>
– Had to git clone more than once:<br>
3 times.<br>
CMake Error at DCMTK-prefix/tmp/DCMTK-gitclone.cmake:31 (message):<br>
Failed to clone repository: ‘git://git.dcmtk.org/dcmtk’</p>
<p>C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(234,5): error MSB6006: “cmd.exe” exited with code 1. [C:\D\S4D\DCMTK.vcxproj]<br>
Creating directories for ‘CTKResEdit’<br>
Performing download step (download, verify and extract) for ‘CTKResEdit’<br>
– Downloading…<br>
dst=‘C:/D/S4D/CTKResEdit-0.1.0-gc157-win-i386.tar.gz’<br>
timeout=‘none’<br>
– Using src=‘<a href="https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz" rel="nofollow noopener">https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz</a>’<br>
– Retrying…<br>
…<br>
– Retry after 60 seconds (attempt <span class="hashtag">#5</span>) …<br>
– Using src=‘<a href="https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz" rel="nofollow noopener">https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz</a>’<br>
CMake Error at CTKResEdit-prefix/src/CTKResEdit-stamp/download-CTKResEdit.cmake:159 (message):<br>
Each download failed!</p>
<p>CUSTOMBUILD : error : downloading ‘<a href="https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz" rel="nofollow noopener">https://github.com/jcfr/ResEdit/releases/download/v0.1.0-20140331-c157b7c/CTKResEdit-0.1.0-gc157-win-i386.tar.gz</a>’ failed [C:\D\S4D\CTKResEdit.vcxproj]<br>
status_code: 6<br>
status_string: “Couldn’t resolve host name”<br>
log:<br>
— LOG BEGIN —<br>
timeout on name lookup is not supported</p>
<hr>
<p>In addition, here is a line from the output regarding skipping the compiler and not sure if this is relevant.<br>
– Check for working C compiler: C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC/14.27.29110/bin/Hostx64/x64/cl.exe - skipped</p>
<hr>
<p>(Edited to remove some links for potential spam flags)<br>
If anyone has any suggestions or insight into what the issue could be, I would appreciate it.<br>
Thanks again.</p>

---

## Post #7 by @lassoan (2020-08-29 15:11 UTC)

<aside class="quote no-group" data-username="jrl" data-post="6" data-topic="13197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/fbc32d/48.png" class="avatar"> jrl:</div>
<blockquote>
<p>status_string: “Couldn’t resolve host name”</p>
</blockquote>
</aside>
<p>These are all networking errors. Do you use VPN or corporate or hospital firewall to connect to the internet? If yes, follow <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/common_errors.html#firewall-is-blocking-git-protocol">these instructions</a>.</p>

---

## Post #8 by @jrl (2020-09-03 05:41 UTC)

<p>I’ve moved past the networking errors (I believe). However, there is no “slicer.exe” file in my Slicer-build folder. Was the build not successful or am I missing something? I noticed there is a “SlicerPython.exe” in the “python-install\bin” folder</p>

---

## Post #9 by @jrl (2020-09-03 16:04 UTC)

<p>Note - there is a “slicer.exe” file in the “Program Files/Slicer 4.10.2” folder</p>

---

## Post #10 by @lassoan (2020-09-03 16:18 UTC)

<p>Yes, you are expected to have a <code>c:\D\S4R\Slicer-build\Slicer.exe</code> file, which launches Slicer. If you don’t have it then it means that the build failed. Restart the top-level build and check for build errors.</p>

---

## Post #12 by @jrl (2020-09-03 16:34 UTC)

<ol>
<li>Are these below actual errors? And if so, what is their significance?</li>
</ol>
<p>"Cloning into ‘JsonCpp’…<br>
Note: switching to ‘73b8e172d6615251ef851d883ef02f163e7075b2’.</p>
<p>You are in ‘detached HEAD’ state. You can look around, make experimental<br>
changes and commit them, and you can discard any commits you make in this<br>
state without impacting any branches by switching back to a branch.</p>
<p>If you want to create a new branch to retain commits you create, you may<br>
do so (now or later) by using -c with the switch command. Example:</p>
<pre><code>git switch -c &lt;new-branch-name&gt;
</code></pre>
<p>Or undo this operation with:</p>
<pre><code>git switch -
</code></pre>
<p>Turn off this advice by setting config variable advice.detachedHead to false</p>
<p>HEAD is now at 73b8e17 COMP: Update json_(reader|writer).cpp to fix gcc6 build <strong>error</strong>"</p>
<p>" Cloning into ‘curl’…<br>
Note: switching to ‘ca5fe8e63df7faea0bfb988ef3fe58f538e6950b’.</p>
<p>You are in ‘detached HEAD’ state. You can look around, make experimental<br>
changes and commit them, and you can discard any commits you make in this<br>
state without impacting any branches by switching back to a branch.</p>
<p>If you want to create a new branch to retain commits you create, you may<br>
do so (now or later) by using -c with the switch command. Example:</p>
<pre><code>git switch -c &lt;new-branch-name&gt;
</code></pre>
<p>Or undo this operation with:</p>
<pre><code>git switch -
</code></pre>
<p>Turn off this advice by setting config variable advice.detachedHead to false</p>
<p>HEAD is now at ca5fe8e63 [slicer] Fix windows link <strong>error</strong> explicitly defining CURL_STATICLIB"</p>
<ol start="2">
<li>
<p>Also - it appears that I am getting LibArchive errors that are also present in a post that another individual had been receiving. So I can try that approach listed there.</p>
</li>
<li>
<p>Throughout the output I am seeing a lot of “not found” (below are just some of the few to give an example) and also some failed tests.<br>
"<br>
– Looking for strerror_r - <strong>not found</strong><br>
– Looking for strftime<br>
– Looking for strftime - found<br>
– Looking for vprintf<br>
– Looking for vprintf - <strong>not found</strong><br>
– Looking for wmemcmp<br>
– Looking for wmemcmp - <strong>not found</strong><br>
– Looking for wmemcpy<br>
– Looking for wmemcpy - <strong>not found</strong><br>
– Looking for wmemmove<br>
– Looking for wmemmove - not found<br>
– Performing Test HAVE_STRUCT_VFSCONF<br>
– Performing Test HAVE_STRUCT_VFSCONF - <strong>Failed</strong><br>
– Performing Test HAVE_STRUCT_XVFSCONF<br>
– Performing Test HAVE_STRUCT_XVFSCONF - <strong>Failed</strong><br>
– Performing Test HAVE_READDIR_R<br>
– Performing Test HAVE_READDIR_R - <strong>Failed</strong><br>
– Performing Test HAVE_DIRFD<br>
– Performing Test HAVE_DIRFD - <strong>Failed</strong><br>
– Performing Test HAVE_READLINKAT<br>
– Performing Test HAVE_READLINKAT - <strong>Failed</strong><br>
– Performing Test MAJOR_IN_MKDEV<br>
– Performing Test MAJOR_IN_MKDEV - <strong>Failed</strong><br>
– Performing Test MAJOR_IN_SYSMACROS<br>
– Performing Test MAJOR_IN_SYSMACROS - <strong>Failed</strong><br>
– Performing Test HAVE_LZMA_STREAM_ENCODER_MT<br>
– Performing Test HAVE_LZMA_STREAM_ENCODER_MT - <strong>Failed</strong><br>
– Looking for EFTYPE<br>
– Looking for EFTYPE - <strong>not found</strong><br>
– Looking for EILSEQ<br>
– Looking for EILSEQ - found<br>
– Looking for D_MD_ORDER<br>
– Looking for D_MD_ORDER - <strong>not found</strong><br>
"<br>
Are these “not found” indicative of a problem? Should there be zero “not founds” during the build? Or are they akin to warnings as opposed to errors?</p>
</li>
</ol>
<p>Thanks again</p>

---

## Post #13 by @lassoan (2020-09-03 16:40 UTC)

<p>None of these are errors. The <code>Failed</code> and <code>not found</code> messages are results of compile tests, which test features of the build environment. Errors are those that Visual Studio compiler reports as errors. You can show list of errors in Visual Studio menu: View / Error list.</p>

---

## Post #14 by @jrl (2020-09-03 16:44 UTC)

<p>Should I be opening the solution file in Visual Studio and building from there? I haven’t opened Visual Studio yet for this.</p>
<p>I was using the command line steps from the instructions:<br>
“C:\Program Files\CMake\bin\cmake.exe” -G “Visual Studio 16 2019 Win64” -DQt5_DIR:PATH=C:\Qt\5.15.0\msvc2019_64\lib\cmake\Qt5 C:\D\S4<br>
“C:\Program Files\CMake\bin\cmake.exe” --build . --config Debug</p>

---

## Post #15 by @jamesobutler (2020-09-03 17:26 UTC)

<p><a class="mention" href="/u/jrl">@jrl</a> What are your plans for development using Slicer? Are you planning to develop a new module? Customize a current module? Or just use python to code some commonly repeated steps in a workflow?</p>

---

## Post #16 by @jrl (2020-09-03 17:44 UTC)

<p>Develop a new module</p>

---

## Post #17 by @jamesobutler (2020-09-03 17:50 UTC)

<p>A C++ based module or python? Have you tried out some python coding of various Slicer actions in the Slicer python interactor yet?</p>

---
