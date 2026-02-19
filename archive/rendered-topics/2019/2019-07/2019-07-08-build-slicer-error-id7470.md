---
topic_id: 7470
title: "Build Slicer Error"
date: 2019-07-08
url: https://discourse.slicer.org/t/7470
---

# Build Slicer Error 

**Topic ID**: 7470
**Date**: 2019-07-08
**URL**: https://discourse.slicer.org/t/build-slicer-error/7470

---

## Post #1 by @Mohsen_Taheri (2019-07-08 17:24 UTC)

<p>Hi,<br>
I follow the buillding instruction step by step but when I want to build slicer I get this error  (Severity	Code	Description	Project	File	Line	Suppression State Error	EndUpdateResourceC	/D/S4D/Slicer-build/Slicer.exe [C:\D\S4D\Slicer-build\Applications\SlicerApp\SlicerUpdateLauncherIcon.vcxproj]	Slicer	C:\D\S4D\CUSTOMBUILD	1)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c65b506c95968f43c6e09e9f19999a9b6dff0510.jpeg" data-download-href="/uploads/short-url/siKb5pEpTz2QLmC3J0RItONHMn6.jpeg?dl=1" title="111" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c65b506c95968f43c6e09e9f19999a9b6dff0510_2_690x389.jpeg" alt="111" data-base62-sha1="siKb5pEpTz2QLmC3J0RItONHMn6" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c65b506c95968f43c6e09e9f19999a9b6dff0510_2_690x389.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c65b506c95968f43c6e09e9f19999a9b6dff0510_2_1035x583.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c65b506c95968f43c6e09e9f19999a9b6dff0510_2_1380x778.jpeg 2x" data-dominant-color="A0ABB9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">111</span><span class="informations">1606×906 324 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
also my Qt version is 5.10.0 and my compiler is Visual Studio 15 2017 Win64<br>
I appriciate if anyone could help me</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.11.0</p>

---

## Post #2 by @jcfr (2019-07-08 19:47 UTC)

<p>Hi,</p>
<p>It is hard to tell what the problem only looking at the screenshot you shared.</p>
<p>Here are few suggestions to get a better understanding of the problem:</p>
<ul>
<li>Scroll up to see if there is an other message with more details</li>
<li>Close Visual Studio, and open the solution file <code>C:\D\S4D\Slicer-build\Slicer.sln</code>, then re-run the build. This should give more details.</li>
</ul>

---

## Post #3 by @Mohsen_Taheri (2019-07-08 22:12 UTC)

<p>I tried to build <code>C:\D\S4D\Slicer-build\Slicer.sln</code> and there is a simillar error<br>
CUSTOMBUILD : error EndUpdateResourceC: /D/S4D/Slicer-build/Slicer.exe</p>

---

## Post #4 by @jcfr (2019-07-08 22:37 UTC)

<p>The command that is failing seems to be the following:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/e4e93ea8d5ae0de35d6d154d5a437bf44c855a27/CMake/SlicerMacroBuildApplication.cmake#L713-L718" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/e4e93ea8d5ae0de35d6d154d5a437bf44c855a27/CMake/SlicerMacroBuildApplication.cmake#L713-L718" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/e4e93ea8d5ae0de35d6d154d5a437bf44c855a27/CMake/SlicerMacroBuildApplication.cmake#L713-L718</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="713" style="counter-reset: li-counter 712 ;">
<li>add_custom_target(${SLICERAPP_APPLICATION_NAME}UpdateLauncherIcon ALL</li>
<li>  COMMAND</li>
<li>    ${CTKResEdit_EXECUTABLE}</li>
<li>      --update-resource-ico ${Slicer_BINARY_DIR}/${SLICERAPP_APPLICATION_NAME}${CMAKE_EXECUTABLE_SUFFIX}</li>
<li>      IDI_ICON1 ${SLICERAPP_WIN_ICON_FILE}</li>
<li>  )</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>By clicking on the “Output” tab you should be able to get more details. The idea would be to try to re-run the command in a regular terminal.</p>
<p>Probably something like this on your workstation:</p>
<pre><code class="lang-auto">C:\D\S4D\CTKResEdit\bin\CTKResEdit.exe --update-resource-ico  C:\D\S4D\Slicer-build\bin\Debug\SlicerApp-real.exe  IDI_ICON1 C:\D\S4\Applications\SlicerApp\Resources\Slicer.ico
</code></pre>
<p>By having a better understanding of the problem, we should be able to release an updated version of the <a href="https://github.com/jcfr/ResEdit/releases" rel="nofollow noopener">binaries</a> or update Slicer build system to always build one expected to work on the developer system.</p>

---

## Post #5 by @lassoan (2019-07-09 00:15 UTC)

<p>This error happens when you have Slicer.exe running (and during Slicer build, CTKResEdit wants to update the icon in Slicer.exe). Just close Slicer.exe and the error will go away. If you cannot find the running instance then restart your computer or use a utility such as LockHunter to find and close it.</p>

---
