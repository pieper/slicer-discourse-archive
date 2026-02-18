# Slicer Build error:MSB8066  in Win10

**Topic ID**: 17443
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/slicer-build-error-msb8066-in-win10/17443

---

## Post #1 by @gylucy (2021-05-04 13:17 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.10<br>
Expected behavior:Build slicer successfully<br>
Actual behavior:Build error occured</p>
<p><strong>the error is:</strong><br>
50&gt;D:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(240,5): error MSB8066: “D:\S4R\a1\CMakeFiles\d6c65a9bb95612b23b9f7dfd2809760b\Slicer-mkdir.rule;D:\S4R\a1\CMakeFiles\d6c65a9bb95612b23b9f7dfd2809760b\Slicer-download.rule;D:\S4R\a1\CMakeFiles\d6c65a9bb95612b23b9f7dfd2809760b\Slicer-update.rule;D:\S4R\a1\CMakeFiles\d6c65a9bb95612b23b9f7dfd2809760b\Slicer-patch.rule;D:\S4R\a1\CMakeFiles\d6c65a9bb95612b23b9f7dfd2809760b\Slicer-configure.rule;D:\S4R\a1\CMakeFiles\d6c65a9bb95612b23b9f7dfd2809760b\Slicer-build.rule;D:\S4R\a1\CMakeFiles\d6c65a9bb95612b23b9f7dfd2809760b\Slicer-forceconfigure.rule;D:\S4R\a1\CMakeFiles\d6c65a9bb95612b23b9f7dfd2809760b\Slicer-install.rule;D:\S4R\a1\CMakeFiles\81bb6dc9211ca64d8deb9e385f10b1b4\Slicer-complete.rule;D:\S4R\a1\CMakeFiles\7a1ce418cc5f93f32cda57dd5b58d729\Slicer.rule”的自定义生成已退出，代码为 1。<br>
50&gt;已完成生成项目“Slicer.vcxproj”的操作 - 失败。<br>
51&gt;------ 已跳过全部重新生成: 项目: ALL_BUILD, 配置: Debug x64 ------<br>
51&gt;没有为此解决方案配置选中要生成的项目<br>
========== 全部重新生成: 成功 47 个，失败 1 个，跳过 3 个 ==========<br>
the file is:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c1f68887fc19146c250c1ff81f82a9434483485.jpeg" alt="CppCommon.targets" data-base62-sha1="fquRfqhQooGWhDxaeXMz5LWMsp7" width="621" height="142"></p>
<p>please help me ,I have no solution for it.  thanks!</p>

---

## Post #2 by @lassoan (2021-05-21 18:38 UTC)

<p>Can you build latest Slicer master version using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html">these build instructions</a>?</p>

---

## Post #3 by @kimble (2021-08-11 04:20 UTC)

<p>Hi gylucy<br>
I got MSB8066 error too. Did you solve this problem?</p>

---

## Post #4 by @kimble (2021-08-11 04:35 UTC)

<p>HI Lassoan<br>
When I build slicer follwoing above guide, I get this MSB8066 error too. May you help to check what is wrong?<br>
The log file could be found with following link</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/shutuzhice/CT">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/shutuzhice/CT" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/88470bf9d7e8e3d294a62ebd7732ef8f3afb2a22fd85e1a61e05f79086aaaad4/shutuzhice/CT" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/shutuzhice/CT" target="_blank" rel="noopener nofollow ugc">GitHub - shutuzhice/CT</a></h3>

  <p>Contribute to shutuzhice/CT development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>thanks</p>

---

## Post #5 by @lassoan (2021-08-11 04:45 UTC)

<p>Which Slicer version are you trying to build?<br>
What is your CPU model?</p>
<p>What build outputs do you get if you start the build again?</p>

---

## Post #6 by @kimble (2021-08-11 05:37 UTC)

<p>Slicer:4.13.0 (debug)<br>
CPU:  Xeon Gold 6128<br>
The 2nd outputs are:<br>
4<em>7&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for ‘C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-configure.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-build.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-forceconfigure.rule;C:\D\S4R\CMakeFiles\26b24c13142eddf123c97e3494499225\Slicer-install.rule;C:\D\S4R\CMakeFiles\d0fbb327fb5d8976f542b004b1325aa2\Slicer-complete.rule;C:\D\S4R\CMakeFiles\dbe9d635f197b17f63b9c895eaab2164\Slicer.rule’ exited with code 1.</em><br>
The whole outputs are uploaded to github too. FYI</p><aside class="onebox githubblob" data-onebox-src="https://github.com/shutuzhice/CT/blob/master/VS_OutPut_message_2nd.txt">
  <header class="source">

      <a href="https://github.com/shutuzhice/CT/blob/master/VS_OutPut_message_2nd.txt" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/shutuzhice/CT/blob/master/VS_OutPut_message_2nd.txt" target="_blank" rel="noopener nofollow ugc">shutuzhice/CT/blob/master/VS_OutPut_message_2nd.txt</a></h4>


    <pre><code class="lang-txt">Build started...
1&gt;------ Build started: Project: CTKResEdit, Configuration: Debug x64 ------
2&gt;------ Build started: Project: LZMA, Configuration: Debug x64 ------
3&gt;------ Build started: Project: OpenSSL, Configuration: Debug x64 ------
4&gt;------ Build started: Project: sqlite, Configuration: Debug x64 ------
5&gt;------ Build started: Project: bzip2, Configuration: Debug x64 ------
6&gt;------ Build started: Project: zlib, Configuration: Debug x64 ------
7&gt;------ Build started: Project: python-source, Configuration: Debug x64 ------
8&gt;------ Build started: Project: tbb, Configuration: Debug x64 ------
9&gt;------ Build started: Project: Swig, Configuration: Debug x64 ------
10&gt;------ Build started: Project: SimpleITK-download, Configuration: Debug x64 ------
11&gt;------ Build started: Project: BRAINSTools, Configuration: Debug x64 ------
12&gt;------ Build started: Project: CTKAppLauncherLib, Configuration: Debug x64 ------
4&gt;Performing update step for 'sqlite'
4&gt;No patch step for 'sqlite'
4&gt;Performing configure step for 'sqlite'
4&gt;loading initial cache file C:/D/S4R/sqlite-prefix/tmp/sqlite-cache-Debug.cmake
4&gt;-- Selecting Windows SDK version 10.0.18362.0 to target Windows 10.0.19041.
4&gt;-- Configuring done
13&gt;------ Build started: Project: CTKAPPLAUNCHER, Configuration: Debug x64 ------
</code></pre>


  This file has been truncated. <a href="https://github.com/shutuzhice/CT/blob/master/VS_OutPut_message_2nd.txt" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>thanks</p>

---

## Post #7 by @lassoan (2021-08-12 04:36 UTC)

<p>It seems that the error is caused by some network connectivity issues:</p>
<pre><code class="lang-auto">47&gt;CMake Error at Base/QTCore/Testing/Cxx/CMakeLists.txt:23 (file):
47&gt;  file DOWNLOAD HASH mismatch
47&gt;
47&gt;    for file: [C:/D/S4R/Slicer-build/Base/QTCore/Testing/Cxx/Resources/19354-linux-amd64-ScriptedLoadableExtensionTemplate-svn19354-2012-02-23.tar.gz]
47&gt;      expected hash: [dd619c9bbd8f058f85c124d775fe5fec1883f05ce4c1025c0f245db1ec088b51]
47&gt;        actual hash: [e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855]
47&gt;             status: [35;"SSL connect error"]
47&gt;
47&gt;
47&gt;
47&gt;CMake Error at Base/QTCore/Testing/Cxx/CMakeLists.txt:23 (file):
47&gt;  file DOWNLOAD HASH mismatch
47&gt;
47&gt;    for file: [C:/D/S4R/Slicer-build/Base/QTCore/Testing/Cxx/Resources/19615-macosx-amd64-CLIExtensionTemplate-svn19615-2012-03-18.tar.gz]
47&gt;      expected hash: [57d76d876cb96bde01d30a16d42316941209c8b6c22ad311d623d918597141c0]
47&gt;        actual hash: [e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855]
47&gt;             status: [28;"Timeout was reached"]
47&gt;
47&gt;
47&gt;
47&gt;CMake Error at Base/QTCore/Testing/Cxx/CMakeLists.txt:23 (file):
47&gt;  file DOWNLOAD HASH mismatch
47&gt;
47&gt;    for file: [C:/D/S4R/Slicer-build/Base/QTCore/Testing/Cxx/Resources/19615-macosx-amd64-LoadableExtensionTemplate-svn19615-2012-03-18.tar.gz]
47&gt;      expected hash: [3ce4a2f0485c9f5db56fb48727421fbe9ccef213c345175e8defb573ce2113da]
47&gt;        actual hash: [e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855]
47&gt;             status: [28;"Timeout was reached"]
</code></pre>
<p>Maybe your workplace blocks download from github or you have some SSL errors (certificates issue, or using a CMake version that has no SSL support, etc.).</p>

---

## Post #8 by @wrx15113330303 (2022-04-27 03:16 UTC)

<p>hi there, did you solve this problem? I have the same error.</p>

---

## Post #9 by @lassoan (2023-05-30 18:00 UTC)

<p>Slicer downloads additional files for testing during the build process. Make sure the CMake can download files from <code>https://github.com/Slicer/SlicerTestingData/releases/download/...</code> during build (for example, from <a href="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/57d76d876cb96bde01d30a16d42316941209c8b6c22ad311d623d918597141c0">this URL</a>).</p>

---

## Post #10 by @Kening_Zhang (2023-08-19 06:22 UTC)

<p>Hi, I have same error too. Are there some specific soultions?</p>

---

## Post #11 by @lassoan (2023-08-19 09:16 UTC)

<p>If you cannot access github then you may try to use a different internet connection or a VPN.</p>

---

## Post #12 by @Kening_Zhang (2023-08-19 10:36 UTC)

<p>I tried but it still not work</p>

---

## Post #13 by @iwangwangwang (2023-09-14 12:44 UTC)

<p>I got the same error and I had use a VPN, but it still didn’t work, sadness <img src="https://emoji.discourse-cdn.com/twitter/frowning_face.png?v=12" title=":frowning_face:" class="emoji" alt=":frowning_face:" loading="lazy" width="20" height="20"></p>

---

## Post #14 by @2733845631 (2024-04-15 10:56 UTC)

<p>I tried but it still not work,Are there some specific soultions?</p>

---
