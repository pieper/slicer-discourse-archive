---
topic_id: 28026
title: "Slicer Custom App Build Error"
date: 2023-02-23
url: https://discourse.slicer.org/t/28026
---

# Slicer custom app build error

**Topic ID**: 28026
**Date**: 2023-02-23
**URL**: https://discourse.slicer.org/t/slicer-custom-app-build-error/28026

---

## Post #1 by @sm-philips (2023-02-23 21:43 UTC)

<p>Hello,</p>
<p>I am trying to build a custom app following the instructions here: <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a></p>
<p>When building, I get the following error:</p>
<pre><code class="lang-auto">Could not find a package configuration file provided by "ITK" (requested
version 4.3) with any of the following names:

    ITKConfig.cmake
    itk-config.cmake
</code></pre>
<pre><code class="lang-auto">Could not find a package configuration file provided by "VTK" with any of
 the following names:

    VTKConfig.cmake
    vtk-config.cmake
</code></pre>
<p>I was under the impression that superbuild would take care of VTK and ITK dependencies.</p>
<p>In one of the forum posts I found that adding:</p>
<pre><code class="lang-auto">set(Slicer_VTK_VERSION_MAJOR 9 CACHE STRING "VTK major version (8 or 9)" FORCE)
mark_as_superbuild(Slicer_VTK_VERSION_MAJOR)
</code></pre>
<p>to the CMakeLists.txt solved the issue for the person. It didnt however solve anything for me. Still get the same error.</p>
<p>Any help would be appreciated. Thank you!</p>

---

## Post #2 by @Sam_Horvath (2023-02-24 19:58 UTC)

<p>So, it should take care of that.</p>
<p>In the top-level folder, is there an ITK-build and a VTK-build folder with build artifacts in it?</p>
<p>It would also be helpful to check if there are build errors earlier in the log that prevented ITK and VTK from building.</p>

---

## Post #3 by @sm-philips (2023-02-27 20:28 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a><br>
First to answer your questions, the ITK-build folder has some artifacts, but the VTK-build folder does not.</p>
<p>Instead of building ALL_BUILD, I built just the VTK project, and this is the error I got.</p>
<pre><code class="lang-auto">22&gt;Cloning into 'F:/GP_rel/VTK/ThirdParty/vtkm/vtkvtkm/vtk-m'...
22&gt;Downloading data/README.md (643 B)
22&gt;Error downloading object: data/README.md (b30a14a): Smudge error: Error downloading data/README.md (b30a14a308f64c6fc2969e2b959d79dacdc5affda1d1c0e24f8e176304147146): batch response: Post "https://gitlab.kitware.com/vtk/vtk-m.git/info/lfs/objects/batch": x509: certificate signed by unknown authority
22&gt;
22&gt;Errors logged to F:\GP_rel\VTK\.git\modules\VTK-m\lfs\logs\20230227T152310.7229115.log
</code></pre>
<p>The log file contained:</p>
<pre><code class="lang-auto">git-lfs/2.13.3 (GitHub; windows amd64; go 1.16.2; git a5e65851)
git version 2.32.0.windows.2

$ git-lfs.exe filter-process
Error downloading object: data/README.md (b30a14a): Smudge error: Error downloading data/README.md (b30a14a308f64c6fc2969e2b959d79dacdc5affda1d1c0e24f8e176304147146): batch response: Post "https://gitlab.kitware.com/vtk/vtk-m.git/info/lfs/objects/batch": x509: certificate signed by unknown authority

Post "https://gitlab.kitware.com/vtk/vtk-m.git/info/lfs/objects/batch": x509: certificate signed by unknown authority
batch response
github.com/git-lfs/git-lfs/errors.newWrappedError
	D:/a/git-lfs/git-lfs/errors/types.go:198
github.com/git-lfs/git-lfs/errors.Wrap
	D:/a/git-lfs/git-lfs/errors/errors.go:74
github.com/git-lfs/git-lfs/tq.(*tqClient).Batch
	D:/a/git-lfs/git-lfs/tq/api.go:77
github.com/git-lfs/git-lfs/tq.Batch
	D:/a/git-lfs/git-lfs/tq/api.go:40
github.com/git-lfs/git-lfs/tq.(*TransferQueue).enqueueAndCollectRetriesFor
	D:/a/git-lfs/git-lfs/tq/transfer_queue.go:559
github.com/git-lfs/git-lfs/tq.(*TransferQueue).collectBatches.func1
	D:/a/git-lfs/git-lfs/tq/transfer_queue.go:453
runtime.goexit
	go/src/runtime/asm_amd64.s:1371
Error downloading data/README.md (b30a14a308f64c6fc2969e2b959d79dacdc5affda1d1c0e24f8e176304147146)
github.com/git-lfs/git-lfs/errors.newWrappedError
	D:/a/git-lfs/git-lfs/errors/types.go:198
github.com/git-lfs/git-lfs/errors.Wrapf
	D:/a/git-lfs/git-lfs/errors/errors.go:85
github.com/git-lfs/git-lfs/lfs.(*GitFilter).downloadFile
	D:/a/git-lfs/git-lfs/lfs/gitfilter_smudge.go:115
github.com/git-lfs/git-lfs/lfs.(*GitFilter).Smudge
	D:/a/git-lfs/git-lfs/lfs/gitfilter_smudge.go:76
github.com/git-lfs/git-lfs/commands.smudge
	D:/a/git-lfs/git-lfs/commands/command_smudge.go:127
github.com/git-lfs/git-lfs/commands.filterCommand
	D:/a/git-lfs/git-lfs/commands/command_filter_process.go:120
github.com/spf13/cobra.(*Command).execute
	go/pkg/mod/github.com/spf13/cobra@v0.0.3/command.go:766
github.com/spf13/cobra.(*Command).ExecuteC
	go/pkg/mod/github.com/spf13/cobra@v0.0.3/command.go:852
github.com/spf13/cobra.(*Command).Execute
	go/pkg/mod/github.com/spf13/cobra@v0.0.3/command.go:800
github.com/git-lfs/git-lfs/commands.Run
	D:/a/git-lfs/git-lfs/commands/run.go:105
main.main
	D:/a/git-lfs/git-lfs/git-lfs.go:33
runtime.main
	go/src/runtime/proc.go:225
runtime.goexit
	go/src/runtime/asm_amd64.s:1371
Smudge error
github.com/git-lfs/git-lfs/errors.newWrappedError
	D:/a/git-lfs/git-lfs/errors/types.go:198
github.com/git-lfs/git-lfs/errors.NewSmudgeError
	D:/a/git-lfs/git-lfs/errors/types.go:284
github.com/git-lfs/git-lfs/lfs.(*GitFilter).Smudge
	D:/a/git-lfs/git-lfs/lfs/gitfilter_smudge.go:85
github.com/git-lfs/git-lfs/commands.smudge
	D:/a/git-lfs/git-lfs/commands/command_smudge.go:127
github.com/git-lfs/git-lfs/commands.filterCommand
	D:/a/git-lfs/git-lfs/commands/command_filter_process.go:120
github.com/spf13/cobra.(*Command).execute
	go/pkg/mod/github.com/spf13/cobra@v0.0.3/command.go:766
github.com/spf13/cobra.(*Command).ExecuteC
	go/pkg/mod/github.com/spf13/cobra@v0.0.3/command.go:852
github.com/spf13/cobra.(*Command).Execute
	go/pkg/mod/github.com/spf13/cobra@v0.0.3/command.go:800
github.com/git-lfs/git-lfs/commands.Run
	D:/a/git-lfs/git-lfs/commands/run.go:105
main.main
	D:/a/git-lfs/git-lfs/git-lfs.go:33
runtime.main
	go/src/runtime/proc.go:225
runtime.goexit
	go/src/runtime/asm_amd64.s:1371

Current time in UTC: 
2023-02-27 20:23:10

ENV:
LocalWorkingDir=F:\GP_rel\VTK\ThirdParty\vtkm\vtkvtkm\vtk-m
LocalGitDir=F:\GP_rel\VTK\.git\modules\VTK-m
LocalGitStorageDir=F:\GP_rel\VTK\.git\modules\VTK-m
LocalMediaDir=F:\GP_rel\VTK\.git\modules\VTK-m\lfs\objects
LocalReferenceDirs=
TempDir=F:\GP_rel\VTK\.git\modules\VTK-m\lfs\tmp
ConcurrentTransfers=8
TusTransfers=false
BasicTransfersOnly=false
SkipDownloadErrors=false
FetchRecentAlways=false
FetchRecentRefsDays=7
FetchRecentCommitsDays=0
FetchRecentRefsIncludeRemotes=true
PruneOffsetDays=3
PruneVerifyRemoteAlways=false
PruneRemoteName=origin
LfsStorageDir=F:\GP_rel\VTK\.git\modules\VTK-m\lfs
AccessDownload=none
AccessUpload=none
DownloadTransfers=basic,lfs-standalone-file
UploadTransfers=basic,lfs-standalone-file
GIT_CONFIG_PARAMETERS=
GIT_DIR=F:/GP_rel/VTK/.git/modules/VTK-m
GIT_EXEC_PATH=C:/Program Files/Git/mingw64/libexec/git-core
GIT_INTERNAL_GETTEXT_SH_SCHEME=fallthrough
GIT_PREFIX=
GIT_PROTOCOL_FROM_USER=0

</code></pre>
<p>I tried disabling git ssl verification in the folders. But that did not solve the issue. I am familiar with basic git needed to maintain a repository, but this feels above my level of knowledge.</p>

---

## Post #4 by @jcfr (2023-02-27 22:03 UTC)

<p>Thanks for the detailed report.</p>
<p>Few questions to help further understand:</p>
<ul>
<li>
<p>What is the version of Slicer specified in the top-level <code>CMakeLists.txt</code>  ?</p>
</li>
<li>
<p>What are the global settings specific to <code>git-lfs</code> ?</p>
<pre><code class="lang-auto">git config --global --get-regexp "filter.lfs.*"
</code></pre>
</li>
<li>
<p>Are you able to run the following command ?</p>
<pre><code class="lang-auto">git clone https://gitlab.kitware.com/vtk/vtk-m.git
</code></pre>
</li>
</ul>

---

## Post #5 by @sm-philips (2023-03-01 14:39 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Find reply to your questions.</p>
<ol>
<li>
<p>I do not have a slicer version. But the SHA I am using is 4f3d97c612b417cb8fe1c5688910f71d23a35852 (verified commit from Feb 21st)</p>
</li>
<li>
<p>I am afraid I am unfamiliar with this. But the command did not return any output.</p>
</li>
<li>
<p>Yes. I can clone it independently.</p>
</li>
</ol>
<p>I made some progress on my end in the meanwhile. I was able to build VTK project independently in the solution after running the following command <code>git config --global http.sslBackend schannel</code>.</p>
<p>The next error to resolve is from CTK. When I build CTK, this is the error I get.</p>
<pre><code class="lang-auto">14&gt;  -- Build files have been written to: F:/GP_rel/CTK-build/PythonQt-build
14&gt;  No build step for 'PythonQt'
14&gt;  Performing install step for 'PythonQt'
14&gt;  CMake Error at cmake_install.cmake:43 (file):
14&gt;    file INSTALL cannot find
14&gt;    "F:/GP_rel/CTK-build/PythonQt-build/Release/PythonQt.dll": No error.
</code></pre>
<p>I disabled Slicer_USE_PYTHONQT_WITH_OPENSSL following instructions <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/common_errors.html" rel="noopener nofollow ugc">here</a>, which I don’t think is the issue. I reinstalled Qt with all the components just in case. I am surprised this is giving me issues on Windows, but built without any issues on a Mac along with SlicerIGT extension.</p>

---

## Post #6 by @Sam_Horvath (2023-03-01 16:17 UTC)

<p>So, this particular error is one that I have been seeing occasionally on windows custom app builds but have not been able to track down the source yet.</p>
<p>Workaround:<br>
In <code>F:/GP_rel/CTK-build/PythonQt-build</code> run this command:<br>
<code> cmake --build . --config Release --target PythonQt</code></p>
<p>What is happening in that the higher level builds are not correctly triggering the PythonQt build for some reason.  The <code>cmake</code> command will specifically build that target and then you can try the CTK build again.</p>

---

## Post #7 by @sm-philips (2023-03-02 14:49 UTC)

<p>Thank you for this.This built CTK. I still have some issues with pip not being found when I do ALL_BUILD. But that’s only affecting the python interactor. I can open the app and read tracking data now.</p>
<p>I believe the cause for a lot of my issues is the workstation being behind a company proxy. Even with admin privileges it is hard to get rid of network issues.</p>

---

## Post #8 by @Sam_Horvath (2023-03-02 15:16 UTC)

<p>Good to hear.  Re: the CTK issue, <a class="mention" href="/u/jcfr">@jcfr</a> has narrowed it down to a regression with newer CMake version causing PythonQt to not build with the CTK superbuild, so there will be a fix merged for that in the near future.</p>

---

## Post #9 by @jcfr (2023-03-02 17:19 UTC)

<p>Regression can be reproduced using the following project.</p>
<p>Waiting this is addressed, using CMake 3.24.3 is expected to work.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/jcfr/cmake-ExternalProject-install-step-regression">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/jcfr/cmake-ExternalProject-install-step-regression" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/ebd2bd386656698359a43f73160888aff44f7e97348c1c397db2161368227b37/jcfr/cmake-ExternalProject-install-step-regression" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/jcfr/cmake-ExternalProject-install-step-regression" target="_blank" rel="noopener">GitHub - jcfr/cmake-ExternalProject-install-step-regression: Reproduce a...</a></h3>

  <p>Reproduce a regression introduced in CMake v3.25 through kitware/cmake@66b5d51f3 - GitHub - jcfr/cmake-ExternalProject-install-step-regression: Reproduce a regression introduced in CMake v3.25 thro...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @jcfr (2023-03-02 21:34 UTC)

<p>As a follow up, the commit introducing the regression in CMake has been reverted, a test case has been added, and the original issue has been re-opened.</p>
<p>A Slicer pull-request has also been created to report an error message if an unsupported CMake version is being used. Waiting CMake <code>3.25.3</code> is released, consider using <code>3.24.3</code>.</p>
<p>See <a href="https://github.com/Slicer/Slicer/pull/6852">https://github.com/Slicer/Slicer/pull/6852</a></p>

---
