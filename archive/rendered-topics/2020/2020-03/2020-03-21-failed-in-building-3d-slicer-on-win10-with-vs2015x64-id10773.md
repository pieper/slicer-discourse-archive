---
topic_id: 10773
title: "Failed In Building 3D Slicer On Win10 With Vs2015X64"
date: 2020-03-21
url: https://discourse.slicer.org/t/10773
---

# Failed in building 3D Slicer on win10 with vs2015x64

**Topic ID**: 10773
**Date**: 2020-03-21
**URL**: https://discourse.slicer.org/t/failed-in-building-3d-slicer-on-win10-with-vs2015x64/10773

---

## Post #1 by @sunshine_boycn (2020-03-21 15:25 UTC)

<p>Dear everybody:</p>
<p>I am building 3D Slicer 4.11.0 on windows10 for a whole week. But still I met lots of problems and failed. My building process is as follows:</p>
<ol>
<li>System: win10x64</li>
<li>CMake: 3.16.5, self-build with openssl ( both self-built and downloaded from official website have been tried.)</li>
<li>git. version 2.25.1. windows.1</li>
<li>svn. 1.13.0 (r1867053)</li>
<li>qt: version 5.10.1 from official website</li>
<li>vs2015x64.</li>
<li>My source directotry is D:\S\S4 and my binary directory is D:\S\SD</li>
</ol>
<p>When 3D Slicer is built, Qt5_DIR is correctly selected. The Option Slicer_USE_PYTHONQT_WITH_OPENSSL is selected to ON and OFF both. Neither of them works for me.</p>
<p>The build error is as follows:</p>
<ol>
<li>
<p>Slicer_USE_PYTHONQT_WITH_OPENSSL is set to ON<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13fa8cccdd1a4c1c651d43680ab4ded6c37045c3.png" data-download-href="/uploads/short-url/2QJS7cbQXjvwh7gYuMIjfkh4gjV.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13fa8cccdd1a4c1c651d43680ab4ded6c37045c3.png" alt="error" data-base62-sha1="2QJS7cbQXjvwh7gYuMIjfkh4gjV" width="690" height="278" data-dominant-color="F7F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1356×547 30.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>Slicer_USE_PYTHONQT_WITH_OPENSSL is set to OFF<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5932216e85404eb44cfc137eacc05d184a14fa41.png" data-download-href="/uploads/short-url/cJ3TKpf60UgHoN27oatcN7yaeo9.png?dl=1" title="error_nossl" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5932216e85404eb44cfc137eacc05d184a14fa41.png" alt="error_nossl" data-base62-sha1="cJ3TKpf60UgHoN27oatcN7yaeo9" width="690" height="203" data-dominant-color="F7F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error_nossl</span><span class="informations">1335×394 20.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>It seems the errors are related to OpenSSL and no matter whether I switch the option Slicer_USE_PYTHONQT_WITH_OPENSSL ON or OFF, the building errors are still there. I can’t solve it. Could anyone help ?</p>
<p>The addition error information is as follows:</p>
<ol>
<li>If I built the python-setuptools project separately, the building error is as follows:</li>
</ol>
<pre><code class="lang-auto">1&gt;------ 已启动生成: 项目: python-setuptools, 配置: Debug x64 ------
1&gt;  Creating directories for 'python-setuptools'
1&gt;  Building Custom Rule D:/S/S4/CMakeLists.txt
1&gt;  No download step for 'python-setuptools'
1&gt;  No update step for 'python-setuptools'
1&gt;  No patch step for 'python-setuptools'
1&gt;  Generate version-python-setuptools.txt and license-python-setuptools.txt
1&gt;  fatal: not a git repository (or any of the parent directories): .git
1&gt;  CMake Warning (dev) at D:/S/SD/CMakeFiles/python-setuptools-generate-project-description.cmake:68 (message):
1&gt;    python-setuptools: Could not find a license file
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.
1&gt;
1&gt;  No configure step for 'python-setuptools'
1&gt;  No build step for 'python-setuptools'
1&gt;  Performing install step for 'python-setuptools'
1&gt;  CMake Error at D:/S/SD/python-setuptools-prefix/src/python-setuptools-stamp/python-setuptools-install-Debug.cmake:49 (message):
1&gt;    Command failed: 1
1&gt;
1&gt;     'D:/S/SD/python-install/bin/SlicerPython.exe' '-m' 'pip' 'install' '--require-hashes' '-r' 'D:/S/SD/python-setuptools-requirements.txt'
1&gt;
1&gt;    See also
1&gt;
1&gt;      D:/S/SD/python-setuptools-prefix/src/python-setuptools-stamp/python-setuptools-install-*.log
1&gt;
1&gt;
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(171,5): error MSB6006: “cmd.exe”已退出，代码为 1。
</code></pre>
<p>If I looked into the error log, the file shows:</p>
<pre><code class="lang-auto">pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
  Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError("Can't connect to HTTPS URL because the SSL module is not available.",)': /simple/setuptools/
  Could not find a version that satisfies the requirement setuptools==41.6.0 (from -r D:/S/SD/python-setuptools-requirements.txt (line 1)) (from versions: )
No matching distribution found for setuptools==41.6.0 (from -r D:/S/SD/python-setuptools-requirements.txt (line 1))
pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
</code></pre>
<p>I serously doubt it is related to OpenSSL option. However, even if I turn the option OFF, still the error jumps out.</p>
<p>And I have some additional doubts here.</p>
<ol>
<li>
<p>Why 3D Slicer need to build VTK, ITK, CTK from scratch all the time? The most inconvenient thing is that I have to redownload about 1GB source files from web each time I failed in building and retry. It costs a lot of time. I noticed that the building process of VTK, ITK, CTK and some other project is OK and cost lots of time.</p>
</li>
<li>
<p>Another trial I have done is to reserve the downloaded github files in the binary directory for the new building, however it still failed during the procedures.<br>
Are there are methods to solve this problems?</p>
</li>
</ol>
<p>Most important, how to successfuly build the Slicer on Windows. I have succeeded on Ubuntu system. It is a great software.</p>
<p>Thank you  very much.</p>
<p>tangtang</p>

---

## Post #2 by @lassoan (2020-03-21 16:01 UTC)

<p>I’ve built Slicer successfully on Windows in Debug mode a few days ago using these commands:</p>
<pre><code class="lang-plaintext">set PATH=%PATH%;C:\Program Files\Git\cmd
set GIT_EXE="c:\Program Files\Git\bin\git.exe"
mkdir C:\D\S4D
cd /d C:\D\S4D
"C:\Program Files\CMake\bin\cmake.exe" -G "Visual Studio 16 2019" -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=ON -DQt5_DIR:PATH=C:\Qt\5.12.7\msvc2017_64\lib\cmake\Qt5 -DSlicer_USE_SimpleITK:BOOL=ON -T "v141" ../S4
"C:\Program Files\CMake\bin\cmake.exe" --build . --config Debug -- /m
</code></pre>
<p>A few weeks ago, I’ve set up debug and release mode builds from scratch based on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows">Slicer build instructions</a>.</p>
<aside class="quote no-group" data-username="sunshine_boycn" data-post="1" data-topic="10773">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed8c4c/48.png" class="avatar"> sunshine_boycn:</div>
<blockquote>
<p>Why 3D Slicer need to build VTK, ITK, CTK from scratch all the time?</p>
</blockquote>
</aside>
<p>You need to build dependencies only once. This is a small price to pay for the time it saves that you don’t need to worry about building all the dependencies manually.</p>

---

## Post #3 by @sunshine_boycn (2020-03-22 09:26 UTC)

<p>Thank you very much for your building information. Could I know which Slicer branch do you build from the github? The latest 4.11.0?</p>
<p>I noticed that the reason that I didn’t succeed probably came from my network. A stable network which could support downloading more than 1GB data from web is important.</p>
<p>Althought I have built Slicer.ext on windows, I still have problems with the building solution. Some projects which related to python didn’t work. The error message from the VS2015 is as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/023b20c7647ad3c3e6f66aa5ee580648b68e1e65.png" data-download-href="/uploads/short-url/jJDrvkW3czThwRN3epThvN2rpb.png?dl=1" title="error_python" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/023b20c7647ad3c3e6f66aa5ee580648b68e1e65.png" alt="error_python" data-base62-sha1="jJDrvkW3czThwRN3epThvN2rpb" width="690" height="147" data-dominant-color="F7F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error_python</span><span class="informations">1352×289 14.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I check the error information and the requirement. I noticed that the python which is downloaded by the Slicer solution offers the python-setuptools 39.0.1 and the requirement for python-setuptools from python-setuptools-requirements.txt is 41.6.0. Would this be the reasons that I can’t build the above python-based projects in my solutions? and how could I solve it?</p>
<p>I noticed that if I choose branch 4.10.2, then the python would choose 2.17.x, and there is no requirements for python-setuptools. However since I choose branch 4.11.0, the python version is 3.6.7, and there exist the python requirement which triggled the error.</p>
<p>I am not sure about the problems, and I would like to know the solution to this problem.</p>
<p>Thank you.</p>
<p>tangtang</p>

---

## Post #4 by @lassoan (2020-03-22 13:45 UTC)

<aside class="quote no-group" data-username="sunshine_boycn" data-post="3" data-topic="10773">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed8c4c/48.png" class="avatar"> sunshine_boycn:</div>
<blockquote>
<p>Could I know which Slicer branch do you build from the github?</p>
</blockquote>
</aside>
<p>Latest master branch.</p>
<aside class="quote no-group" data-username="sunshine_boycn" data-post="3" data-topic="10773">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed8c4c/48.png" class="avatar"> sunshine_boycn:</div>
<blockquote>
<p>I noticed that the reason that I didn’t succeed probably came from my network.</p>
</blockquote>
</aside>
<p>If anything fails due to slow network then you just need to restart the build (without deleting anything that has been already downloaded or built).</p>

---

## Post #5 by @jamesobutler (2020-03-22 13:46 UTC)

<aside class="quote no-group" data-username="sunshine_boycn" data-post="3" data-topic="10773">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/ed8c4c/48.png" class="avatar"> sunshine_boycn:</div>
<blockquote>
<p>which Slicer branch do you build from the github?</p>
</blockquote>
</aside>
<p>The master branch. <a href="https://github.com/Slicer/Slicer/tree/master" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>. Fetch the latest as recent Slicer versions use a version of setuptools that’s newer than 41.6.0.</p>
<p>Just doing a google search on the original errors you had, might you have any version of Anaconda installed on your Windows machine? This might be causing problems.</p>
<p>Others have seemingly done the following with success (<a href="https://github.com/pypa/virtualenv/issues/1139#issuecomment-481847818" rel="noopener nofollow ugc">source</a>):</p>
<blockquote>
<p>Removing both libssl-1_1-x64.dll and  <strong>libcrypto-1_1-x64.dll</strong>  in C:/Windows/System32/ fixed the problem for me.</p>
</blockquote>

---

## Post #6 by @sunshine_boycn (2020-03-22 15:06 UTC)

<p>Thank you very much.</p>
<p>If I reconfigure the project using CMake with different options, it seems that I have to download the files again. That is what troubles me.</p>

---

## Post #7 by @sunshine_boycn (2020-03-22 15:26 UTC)

<p>You are quiet right. I have installed both python3.7 and anaconda on my win10 operation system.</p>
<p>And I have tried your solution which delete two files from windows fold and add three anaconda path to the system PATH. Both of them failed to solve the problem.</p>

---

## Post #8 by @jamesobutler (2020-03-22 20:16 UTC)

<p>I would actually suggest to remove the anaconda install and rebuild. Want to make sure SlicerPython and the pip for that is being used and not being interrupted by some other system pip.</p>
<p>There’s going to be inevitably some redownloading of files necessary to get it to build correctly.</p>

---

## Post #9 by @sunshine_boycn (2020-03-26 02:50 UTC)

<p>Thank you very much for you advice. I have tried to build slicer on a computer without Anaconda and it does succeed. It costs me three days to complete the download.</p>
<p>And I have tried to remove the anaconda path from the system PATH, it seems useless.</p>

---

## Post #10 by @Yang_Li (2022-02-08 10:13 UTC)

<p>Hi, I also have the same issue. After I closed the proxy the python related projects are compiled correctly. And at the same time the annaconda is uninstalled completly from my desktop.</p>

---
