---
topic_id: 1839
title: "Commit 69E26835E Would Burn My Discrete Gpu"
date: 2018-01-14
url: https://discourse.slicer.org/t/1839
---

# Commit 69e26835e would burn my discrete GPU!

**Topic ID**: 1839
**Date**: 2018-01-14
**URL**: https://discourse.slicer.org/t/commit-69e26835e-would-burn-my-discrete-gpu/1839

---

## Post #1 by @chir.set (2018-01-14 20:23 UTC)

<p>Since commit 69e26835e, Slicer freezes as soon as I move a Volume Rendering model when I use the discrete GPU of my laptop(DRI_PRIME=1). Temperature increases to near 100°C until the system itself hangs with a noisy fan spinning. kill, killall, pkill and xkill don’t stop Slicer. I have no other choice than powering off by long pressing the power button. I have to wait 10-15 minutes before getting back a usable system, I even thought some internal device was burnt.</p>
<p>This does not happen with commit 69e26835e if I just use the iGPU, but rendering is not sharp as it is less powerful than the dGPU. It does not happen on my desktop PC with a single GPU PCI-E card neither.</p>
<p>No such behaviour happens with preceding commit 486c6ee7a. I can offload to the dGPU and voilà.</p>
<p>Commit 69e26835e introduces many changes, there are probably things to fix.</p>
<p>I build Slicer on Arch Linux, configured as follows :</p>
<blockquote>
<p>cmake -DSlicer_VTK_VERSION_MAJOR:INT=9 -DQt5_DIR:PATH=/usr/lib/cmake/Qt5 -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=0 -DBUILD_TESTING:BOOL=0 -DCMAKE_BUILD_TYPE:STRING=Release …/Slicer</p>
</blockquote>
<p>with gcc 7.2.1 20171224, cmake version 3.10.1 and Qt 5.10.0.</p>
<p>For the record, my laptop has an AMD A10-7300 APU, with an AMD Kaveri iGPU, and an AMD Topaz dGPU. I am using the amdgpu kernel module and the open source xf86-video-amdgpu driver.</p>
<hr>
<p>Secondly, I need your advice for another issue.</p>
<p>(question moved to <a href="https://discourse.slicer.org/t/how-can-we-avoid-removing-all-vtk-directories-when-updating-slicer/1840" class="inline-onebox">How can we avoid removing all VTK directories when updating slicer</a>)</p>

---

## Post #2 by @lassoan (2018-01-15 15:17 UTC)

<p>The is certainly below Slicer’s level, but we can help in troubleshooting. Overheating is a low-level (hardware, driver, configuration) issue, but if you only encounter this with Slicer and other VTK-based applications then it is worth investigating how VTK uses your GPU differently compared to other applications.</p>
<p>Can you reproduce this with a simple VTK GPU volume rendering example? You can try <a href="https://lorensen.github.io/VTKExamples/site/Cxx/VolumeRendering/SimpleRayCast/">this example</a> as it is, and then replace <code>vtkFixedPointVolumeRayCastMapper</code> by <code>vtkGPUVolumeRayCastMapper</code>.</p>

---

## Post #3 by @chir.set (2018-01-15 19:55 UTC)

<p>I built VTK9 on my laptop, I dont know if it’s the official one from Kitware or the fork at github/Slicer.</p>
<p>SimpleRayCast did not hang when the model is rotated, neither with vtkFixedPointVolumeRayCastMapper nor with vtkGPUVolumeRayCastMapper. That’s for both DRI_PRIME={0,1}. Example application GPURenderDemo in the VTK tree runs without issue also.</p>
<p>I am downloading the VTK fork at gitub/Slicer to test, I suppose it’s the one Slicer uses.</p>

---

## Post #4 by @lassoan (2018-01-15 20:03 UTC)

<p>You can find the details of VTK repository and git branch/tag in External_VTKv9.cmake:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/SuperBuild/External_VTKv9.cmake#L103-L121" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/SuperBuild/External_VTKv9.cmake#L103-L121" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/SuperBuild/External_VTKv9.cmake#L103-L121</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="103" style="counter-reset: li-counter 102 ;">
<li>ExternalProject_SetIfNotDefined(</li>
<li>  ${CMAKE_PROJECT_NAME}_${proj}_GIT_REPOSITORY</li>
<li>  "${git_protocol}://github.com/Slicer/VTK.git"</li>
<li>  QUIET</li>
<li>  )</li>
<li>
</li>
<li>set(_git_tag)</li>
<li>if("${Slicer_VTK_VERSION_MAJOR}" STREQUAL "7")</li>
<li>set(_git_tag "43f6ee36f6e28c8347768bd97df4d767da6b4ce7")</li>
<li>elseif("${Slicer_VTK_VERSION_MAJOR}" STREQUAL "9")</li>
<li>set(_git_tag "db38b04f8d90204a5e2dccbdacfefc4ded0d3ee0")</li>
<li>else()</li>
<li>message(FATAL_ERROR "error: Unsupported Slicer_VTK_VERSION_MAJOR: ${Slicer_VTK_VERSION_MAJOR}")</li>
<li>endif()</li>
<li>ExternalProject_SetIfNotDefined(</li>
<li>  ${CMAKE_PROJECT_NAME}_${proj}_GIT_TAG</li>
<li>  ${_git_tag}</li>
<li>  QUIET</li>
<li>  )</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @chir.set (2018-01-15 21:29 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="http://github.com/Slicer/VTK.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/VTK: WARNING: This is NOT the official upstream VTK git repository</a></p>
</blockquote>
</aside>
<p>Ah, VTK is downloaded from github while building Slicer, so I just tested two similar trees, with same results.</p>
<p>Anyway, my main use case is not my laptop. So I’ll still be able to keep pace with Slicer development, until the nightly builds on your website come with VTK9. I need that for Volume Rendering as it just works without the GPU proprietary driver, which is not the case for VTK7 currently in the nightly builds.</p>

---

## Post #6 by @chir.set (2018-01-16 11:24 UTC)

<p>To my dismay, I just discovered that Slicer freezes when rotating a Volume Rendering model on my work desktop PC also. It has a single AMD RX480 GPU. Using therefore a build from a previous commit.</p>

---

## Post #7 by @lassoan (2018-01-16 13:48 UTC)

<p>What is the size of your volume?<br>
How much GPU memory usage do you allow in volume rendering settings?</p>
<p>Could you try if you have similar issues with volume rendering in ParaView?</p>

---

## Post #8 by @Sankhesh_Jhaveri (2018-01-16 14:03 UTC)

<p>Going over past conversations in this thread, were you able to run SimpleRayCast on the desktop with AMD GPU. Did you that have issues too?</p>
<p>If you have a VTK build, you could also run the volume rendering tests</p>
<pre><code>$ ctest -V -R vtkRenderingVolume*</code></pre>

---

## Post #9 by @chir.set (2018-01-16 17:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What is the size of your volume?</p>
</blockquote>
</aside>
<p>I’m using CTA-cardio.nrrd from your repo.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How much GPU memory usage do you allow in volume rendering settings?</p>
</blockquote>
</aside>
<p>On my work machine, 8 GB, corresponding to the VRAM of my GPU.<br>
On my laptop, 3GB : 1 GB for the iGPU and 2 GB for the dGPU.</p>
<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ParaView</p>
</blockquote>
</aside>
<p>Downloaded PataView, but can’t find time now to learn how to create a Volume Rendering model there.</p>

---

## Post #10 by @chir.set (2018-01-16 17:08 UTC)

<aside class="quote no-group" data-username="Sankhesh_Jhaveri" data-post="8" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sankhesh_jhaveri/48/1081_2.png" class="avatar"> Sankhesh_Jhaveri:</div>
<blockquote>
<p>run SimpleRayCast on the desktop with AMD GPU.</p>
</blockquote>
</aside>
<p>SimpleRayCast results on my work desktop PC with AMD RX480 GPU :</p>
<p>vtkFixedPointVolumeRayCastMapper : normal behaviour<br>
vtkGPUVolumeRayCastMapper : immediate UI freeze leading to hard reboot on first run, immediate UI freeze with only mouse active but useless on second run.</p>
<p>I’ll try again at home on my laptop when possible.</p>

---

## Post #11 by @lassoan (2018-01-16 17:09 UTC)

<p>How much GPU memory do you specify in Slicer (Volume rendering module, Advanced section, Techniques tab)?</p>
<p>To test in ParaView: You can only load uncompressed volumes, so re-save CTA-cardio with compression disabled. Then, load the volume and in Properties/Display/Representation, choose “Volume”.</p>

---

## Post #12 by @chir.set (2018-01-16 17:11 UTC)

<aside class="quote no-group" data-username="Sankhesh_Jhaveri" data-post="8" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sankhesh_jhaveri/48/1081_2.png" class="avatar"> Sankhesh_Jhaveri:</div>
<blockquote>
<p>you could also run the volume rendering tests</p>
</blockquote>
</aside>
<p>ctest -V -R vtkRenderingVolume*<br>
UpdateCTestConfiguration  from :/home/user/src/SimpleRayCast/DartConfiguration.tcl<br>
UpdateCTestConfiguration  from :/home/user/src/SimpleRayCast/DartConfiguration.tcl<br>
Test project /home/user/src/SimpleRayCast<br>
Constructing a list of tests<br>
Updating test list for fixtures<br>
Added 0 tests to meet fixture requirements<br>
Checking test dependency graph…<br>
Checking test dependency graph end<br>
No tests were found!!!</p>
<p>Can’t understand what it means.</p>

---

## Post #13 by @lassoan (2018-01-16 17:14 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="12" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>No tests were found!!!</p>
</blockquote>
</aside>
<p>By default, Slicer does not build test applications when VTK is built. In CMake’s VTK project, set BUILD_TESTING variable to ON, then configure and build VTK. After that, volume rendering tests will be found.</p>

---

## Post #14 by @jcfr (2018-01-16 17:35 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="10" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>SimpleRayCast results on my work desktop PC with AMD RX480 GPU :</p>
<p>vtkFixedPointVolumeRayCastMapper : normal behaviour</p>
<p>vtkGPUVolumeRayCastMapper : immediate UI freeze leading to hard reboot on first run, immediate UI freeze with only mouse active but useless on second run.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a> <a class="mention" href="/u/lassoan">@lassoan</a> Look like the example allows to reproduce the problem.</p>

---

## Post #15 by @chir.set (2018-01-16 17:48 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Then, load the volume and in Properties/Display/Representation, choose “Volume”.</p>
</blockquote>
</aside>
<p>After accepting the dialog about time consuming process in ParaView, it starts computing and the UI freezes after about 5 secs. No model is displayed yet.</p>

---

## Post #16 by @ihnorton (2018-01-16 17:50 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="1" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I am using the amdgpu kernel module and the open source xf86-video-amdgpu driver.</p>
</blockquote>
</aside>
<p>Can you try the Radeon driver instead, as a differential? (or maybe you did already?)</p>
<p><a href="https://wiki.archlinux.org/index.php/AMD_Catalyst" class="onebox" target="_blank" rel="noopener">https://wiki.archlinux.org/index.php/AMD_Catalyst</a></p>

---

## Post #17 by @chir.set (2018-01-16 17:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>After that, volume rendering tests will be found.</p>
</blockquote>
</aside>
<p>ctest -V -R vtkRenderingVolume* &amp;&gt; ~/tmp/ctest.log</p>
<p>It shows a few windows for less than 1 sec each, until the UI freezes. Mouse cursor is till available but useless. Here is what could be logged :</p>
<blockquote>
<p>UpdateCTestConfiguration  from :/home/user/src/VTK-build/DartConfiguration.tcl<br>
Parse Config file:/home/user/src/VTK-build/DartConfiguration.tcl<br>
Add coverage exclude regular expressions.<br>
Add coverage exclude: vtk[^.]+(Java|Python).cxx<br>
Add coverage exclude: .<em>vtkOpenGLState.</em><br>
Add coverage exclude: .<em>Testing.Cxx.<em>cxx<br>
Add coverage exclude: .<em>Testing.Cxx.<em>h<br>
Add coverage exclude: .<em>moc_.<em>cxx<br>
Add coverage exclude: .</em>/Rendering/OpenGL/vtkgl.</em><br>
Add coverage exclude: .</em>/Utilities/.</em><br>
Add coverage exclude: .</em>/ThirdParty/.</em><br>
Add coverage exclude: .<em>vtkOpenGLPolyDataMapper.</em><br>
SetCTestConfiguration:CMakeCommand:/usr/bin/cmake<br>
UpdateCTestConfiguration  from :/home/user/src/VTK-build/DartConfiguration.tcl<br>
Parse Config file:/home/user/src/VTK-build/DartConfiguration.tcl<br>
Test project /home/user/src/VTK-build<br>
Constructing a list of tests<br>
Done constructing a list of tests<br>
Updating test list for fixtures<br>
Added 0 tests to meet fixture requirements<br>
Checking test dependency graph…<br>
Checking test dependency graph end<br>
test 41<br>
Start  41: vtkRenderingVolume-HeaderTest</p>
<p>41: Test command: /bin/python2 “/home/user/src/VTK/Testing/Core/HeaderTesting.py” “/home/user/src/VTK/Rendering/Volume” “VTKRENDERINGVOLUME_EXPORT”<br>
41: Test timeout computed to be: 3600<br>
41: Use export macro: VTKRENDERINGVOLUME_EXPORT<br>
1/89 Test  <span class="hashtag-raw">#41:</span> vtkRenderingVolume-HeaderTest …   Passed    0.81 sec<br>
test 353<br>
Start 353: vtkRenderingVolumeOpenGL2-HeaderTest</p>
<p>353: Test command: /bin/python2 “/home/user/src/VTK/Testing/Core/HeaderTesting.py” “/home/user/src/VTK/Rendering/VolumeOpenGL2” “VTKRENDERINGVOLUMEOPENGL2_EXPORT”<br>
353: Test timeout computed to be: 3600<br>
353: Use export macro: VTKRENDERINGVOLUMEOPENGL2_EXPORT<br>
2/89 Test <span class="hashtag-raw">#353:</span> vtkRenderingVolumeOpenGL2-HeaderTest …   Passed    0.19 sec<br>
test 1208<br>
Start 1208: vtkRenderingVolumeCxx-ProjectedTetrahedraZoomIn</p>
<p>1208: Test command: /home/user/src/VTK-build/bin/vtkRenderingVolumeCxxTests “ProjectedTetrahedraZoomIn” “-D” “/home/user/src/VTK-build/ExternalData//Testing” “-T” “/home/user/src/VTK-build/Testing/Temporary”<br>
1208: Test timeout computed to be: 3600<br>
1208: Loading /home/user/src/VTK-build/ExternalData//Testing/Data/ironProt.vtk<br>
1208: Loading /home/user/src/VTK-build/ExternalData//Testing/Data/neghip.slc<br>
1208: Generic Warning: In /home/user/src/VTK/Rendering/Volume/Testing/Cxx/ProjectedTetrahedraZoomIn.cxx, line 197<br>
1208: This test will always pass.<br>
1208:<br>
3/89 Test <span class="hashtag-raw">#1208:</span> vtkRenderingVolumeCxx-ProjectedTetrahedraZoomIn …   Passed    2.30 sec<br>
test 1209<br>
Start 1209: vtkRenderingVolumeCxx-TestFinalColorWindowLevel</p>
<p>1209: Test command: /home/user/src/VTK-build/bin/vtkRenderingVolumeCxxTests “TestFinalColorWindowLevel” “-D” “/home/user/src/VTK-build/ExternalData//Testing” “-T” “/home/user/src/VTK-build/Testing/Temporary” “-V” “/home/user/src/VTK-build/ExternalData/Rendering/Volume/Testing/Data/Baseline/TestFinalColorWindowLevel.png”<br>
1209: Test timeout computed to be: 3600<br>
1209: 0Standard0.182799<br>
1209: 0.342806<br>
4/89 Test <span class="hashtag-raw">#1209:</span> vtkRenderingVolumeCxx-TestFinalColorWindowLevel …   Passed    0.59 sec<br>
test 1210<br>
Start 1210: vtkRenderingVolumeCxx-TestFixedPointRayCastLightComponents</p>
<p>1210: Test command: /home/user/src/VTK-build/bin/vtkRenderingVolumeCxxTests “TestFixedPointRayCastLightComponents” “-D” “/home/user/src/VTK-build/ExternalData//Testing” “-T” “/home/user/src/VTK-build/Testing/Temporary” “-V” “/home/user/src/VTK-build/ExternalData/Rendering/Volume/Testing/Data/Baseline/TestFixedPointRayCastLightComponents.png”<br>
1210: Test timeout computed to be: 3600<br>
1210: CTEST_FULL_OUTPUT (Avoid ctest truncation of output)<br>
1210: 0Standard0.152745<br>
1210: 0.236041<br>
5/89 Test <span class="hashtag-raw">#1210:</span> vtkRenderingVolumeCxx-TestFixedPointRayCastLightComponents …   Passed    0.77 sec<br>
test 1211<br>
Start 1211: vtkRenderingVolumeCxx-TestGPURayCastAdditive</p>
<p>1211: Test command: /home/user/src/VTK-build/bin/vtkRenderingVolumeCxxTests “TestGPURayCastAdditive” “-D” “/home/user/src/VTK-build/ExternalData//Testing” “-T” “/home/user/src/VTK-build/Testing/Temporary” “-V” “/home/user/src/VTK-build/ExternalData/Rendering/Volume/Testing/Data/Baseline/TestGPURayCastAdditive.png”<br>
1211: Test timeout computed to be: 3600<br>
1211: CTEST_FULL_OUTPUT (Avoid ctest truncation of output)<br>
1211: 5.27712Standard0.062804<br>
1211: 0.128531<br>
6/89 Test <span class="hashtag-raw">#1211:</span> vtkRenderingVolumeCxx-TestGPURayCastAdditive …   Passed    0.34 sec<br>
test 1212<br>
Start 1212: vtkRenderingVolumeCxx-TestGPURayCastCompositeBinaryMask</p>
<p>1212: Test command: /home/user/src/VTK-build/bin/vtkRenderingVolumeCxxTests “TestGPURayCastCompositeBinaryMask” “-D” “/home/user/src/VTK-build/ExternalData//Testing” “-T” “/home/user/src/VTK-build/Testing/Temporary” “-V” “/home/user/src/VTK-build/ExternalData/Rendering/Volume/Testing/Data/Baseline/TestGPURayCastCompositeBinaryMask.png”<br>
1212: Test timeout computed to be: 3600<br>
1212: CTEST_FULL_OUTPUT (Avoid ctest truncation of output)<br>
1212: 0.00261438Standard0.0450981<br>
1212: 0.061025<br>
7/89 Test <span class="hashtag-raw">#1212:</span> vtkRenderingVolumeCxx-TestGPURayCastCompositeBinaryMask …   Passed    0.33 sec<br>
test 1213<br>
Start 1213: vtkRenderingVolumeCxx-TestGPURayCastCompositeMaskBlend</p>
<p>1213: Test command: /home/user/src/VTK-build/bin/vtkRenderingVolumeCxxTests “TestGPURayCastCompositeMaskBlend” “-D” “/home/user/src/VTK-build/ExternalData//Testing” “-T” “/home/user/src/VTK-build/Testing/Temporary” “-V” “/home/user/src/VTK-build/ExternalData/Rendering/Volume/Testing/Data/Baseline/TestGPURayCastCompositeMaskBlend.png”<br>
1213: Test timeout computed to be: 3600<br>
1213: CTEST_FULL_OUTPUT (Avoid ctest truncation of output)<br>
1213: 0Standard0.069319<br>
1213: 0.14196<br>
8/89 Test <span class="hashtag-raw">#1213:</span> vtkRenderingVolumeCxx-TestGPURayCastCompositeMaskBlend …   Passed    0.38 sec<br>
test 1214<br>
Start 1214: vtkRenderingVolumeCxx-TestGPURayCastCompositeMask</p>
<p>1214: Test command: /home/user/src/VTK-build/bin/vtkRenderingVolumeCxxTests “TestGPURayCastCompositeMask” “-D” “/home/user/src/VTK-build/ExternalData//Testing” “-T” “/home/user/src/VTK-build/Testing/Temporary” “-V” “/home/user/src/VTK-build/ExternalData/Rendering/Volume/Testing/Data/Baseline/TestGPURayCastCompositeMask.png”<br>
1214: Test timeout computed to be: 3600<br>
1214: CTEST_FULL_OUTPUT (Avoid ctest truncation of output)<br>
1214: 0.392157Standard0.078526<br>
1214: 0.153189<br>
9/89 Test <span class="hashtag-raw">#1214:</span> vtkRenderingVolumeCxx-TestGPURayCastCompositeMask …   Passed    0.33 sec<br>
test 1215<br>
Start 1215: vtkRenderingVolumeCxx-TestGPURayCastCompositeToMIP</p>
<p>1215: Test command: /home/user/src/VTK-build/bin/vtkRenderingVolumeCxxTests “TestGPURayCastCompositeToMIP” “-D” “/home/user/src/VTK-build/ExternalData//Testing” “-T” “/home/user/src/VTK-build/Testing/Temporary” “-V” “/home/user/src/VTK-build/ExternalData/Rendering/Volume/Testing/Data/Baseline/TestGPURayCastCompositeToMIP.png”<br>
1215: Test timeout computed to be: 3600<br>
1215: CTEST_FULL_OUTPUT (Avoid ctest truncation of output)</p>
</blockquote>
<p>Now I have to finish my paper work !</p>

---

## Post #18 by @chir.set (2018-01-16 18:17 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="16" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>Can you try the Radeon driver instead, as a differential?</p>
</blockquote>
</aside>
<p>Well the RX480 GPU won’t work with the radeon kernel module. I’ll try that on my laptop ASAP.</p>
<p>(BTW, the page you referenced is much outdated. Catalyst is dead, Xorg is versioned to 1.1.19.)</p>

---

## Post #19 by @Sankhesh_Jhaveri (2018-01-17 20:36 UTC)

<p>We were able to test this on the same GPU on a mac with proprietary AMD drivers. No issues.<br>
It could be a driver issue.</p>
<p>There have been many changes to the volume rendering code in VTK that went into commit 69e26835e. Now that you have a VTK build, would you be able to run <code>git bisect</code> to isolate the VTK commit that introduced this issue?</p>

---

## Post #20 by @jcfr (2018-01-17 20:58 UTC)

<p>Thanks</p>
<p>Here are more details about git bisect: <a href="https://blog.kitware.com/regression-hunting-from-slicer-cdash-error-to-itk-master/">https://blog.kitware.com/regression-hunting-from-slicer-cdash-error-to-itk-master/</a></p>
<p>And an example of test script that could be adapted: <a href="https://gist.github.com/jcfr/6029698">https://gist.github.com/jcfr/6029698</a></p>
<p><a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a>  I guess the bisect test script could rebuild and only execute the test process <code>TestGPURayCastCompositeToMIP</code>. Then, if it doesn’t stop after a while, it could be killed if it doesn’t exit.  Do you have test script that could be reused for this type of problem ?</p>
<p>but if the machine freeze, I guess he would have to be a manual bisect with a systematic restart of the machine …</p>

---

## Post #21 by @Sankhesh_Jhaveri (2018-01-17 21:37 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Why not just run <code>ctest</code> for the particular test? It will report a failure if the test times out.</p>

---

## Post #22 by @jcfr (2018-01-17 22:46 UTC)

<p>Yes. Good point. we would just have to make sure the timeout is not 3600s.</p>

---

## Post #23 by @chir.set (2018-01-17 22:50 UTC)

<aside class="quote no-group" data-username="Sankhesh_Jhaveri" data-post="19" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sankhesh_jhaveri/48/1081_2.png" class="avatar"> Sankhesh_Jhaveri:</div>
<blockquote>
<p>would you be able to run git bisect to isolate the VTK commit that introduced this issue?</p>
</blockquote>
</aside>
<p>I’ll look into that as from tomorrow evening, will be busy in OR tomorrow.</p>

---

## Post #24 by @chir.set (2018-01-18 12:01 UTC)

<aside class="quote no-group" data-username="Sankhesh_Jhaveri" data-post="19" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sankhesh_jhaveri/48/1081_2.png" class="avatar"> Sankhesh_Jhaveri:</div>
<blockquote>
<p>would you be able to run git bisect to isolate the VTK commit that introduced this issue?</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="Sankhesh_Jhaveri" data-post="19" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sankhesh_jhaveri/48/1081_2.png" class="avatar"> Sankhesh_Jhaveri:</div>
<blockquote>
<p>We were able to test this on the same GPU on a mac with proprietary AMD drivers</p>
</blockquote>
</aside>
<p>Well, I installed the AMDGPU-PRO proprietary driver on my RX480 PC and Volume Rendering just works.<br>
It used to work with VTK9 up to commit 486c6ee7a without amdgpu-pro. I suppose commit 69e26835e now requires OpenCL explicitly to work among many other changes in VTK. It was so conveniant for Slicer to just work fully without porting packages built for other distros. So either I continue with 486c6ee7a or I use amdgpu-pro.</p>
<p>I think that bisecting VTK becomes superfluous. I can still do it if you think it’s useful.</p>

---

## Post #25 by @chir.set (2018-01-21 10:47 UTC)

<aside class="quote no-group" data-username="Sankhesh_Jhaveri" data-post="19" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sankhesh_jhaveri/48/1081_2.png" class="avatar"> Sankhesh_Jhaveri:</div>
<blockquote>
<p>would you be able to run git bisect to isolate the VTK commit that introduced this issue?</p>
</blockquote>
</aside>
<p>Regardless of Volume Rendering working as expected with amdgpu-pro proprietary package on Linux, and accounting in particular that Volume Rendering used to work as expected without the proprietary package, I performed the bisect of VTK with the following results :</p>
<blockquote>
<p>db38b04f8d90204a5e2dccbdacfefc4ded0d3ee0 : BAD<br>
ca174d0ff382ba25d9ebf949e201a84351f63963 : BAD<br>
e5b528dbfefd8ea934a507eb6b9f6e4ad74bd0f4 : BAD<br>
92310ce2ae77413cf027281ffe3ff79981c38f36 : BAD<br>
4722a46045ebab9695a944ff5f0e3816e2530f49 : BAD<br>
69821aeec42b13ab776bcf2113068c686ed25741 : BAD<br>
a632f77e3fa955dbf17813a803ddae43a9675021 : BAD</p>
<p>:040000 040000 79dd4489981278880c229b9cb216bc12f06e9651 5cd872014cfc65a4d021486b8cde01d69aacbed1 M      Common<br>
:040000 040000 b004405dd3fca6b649fcb1c72d3e015505647156 0491e6089fcba3fcdb49538ec37ea44bdee61513 M      Rendering<br>
:040000 040000 472990bf77ee19ab98b00737c486529cc347cc37 975b1195e27fd6c93362d5c2386cff7b51aaa4a7 M      Testing</p>
<p>0a80c1818ce96c8edc785b11532361780ab6b2ae : GOOD<br>
0e852c83d0e1cceff29e4df74b2059a085ed8518 : GOOD<br>
41f2ba3ae8e8c25223d32a37191b971ef839cd38 : GOOD<br>
887c5065ec2220be04b105ce1d966c5162e729af : GOOD</p>
</blockquote>
<p>All tests were done with SimpleRayCast. Up to the first bad commit after db38b04f8d (start), Slicer was rebuilt with the corresponding VTK commit by modifying SuperBuild/External_VTKv9.cmake. Slicer’s behaviour was similar to SimpleRayCast, and the latter only was used afterwards. ctest always freezes my laptop with all commits, defeating automation.</p>
<p>This unexpected behaviour is observed with the Topaz XT [Radeon R7 M260/M265 / M340/M360 / M440/M445] (lspci output, laptop dGPU) and with the Ellesmere RX480 GPUs.<br>
Volume Rendering works normally with the Kaveri [Radeon R6 Graphics] (laptop iGPU) and the Oland PRO [Radeon R7 240/340] GPUs.</p>
<p>All this without any proprietary package.</p>
<p>I don’t know if the Slicer/VTK teams would consider if :</p>
<ul>
<li>the proprietary package is mandatory on Linux,</li>
<li>the open source amdgpu kernel module or the open source xf86-video-amdgpu package is faulty,</li>
<li>commit a632f77e3 can be reviewed for greater usability of VTK derived software on Linux.</li>
</ul>
<p>Please note that I am posting these for information purposes only, though it’s clear the third option would suit me best.</p>
<p>Regards.</p>

---

## Post #26 by @chir.set (2018-01-29 20:25 UTC)

<p>I noticed that if ‘Crop Enable’ checkbox is ticked in Volume Rendering, with or without being unchecked next, after having first selected a volume in the uppermost combobox, then Slicer does not freeze when the resulting 3D volume is rotated on those two failing GPUs.</p>
<p>I applied this patch and Slicer then behaves normally.</p>
<pre><code>diff --git a/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingModuleWidget.cxx b/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingModuleWidget.cxx
index 8b92cc3a6..892e2d605 100644
--- a/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingModuleWidget.cxx
+++ b/Modules/Loadable/VolumeRendering/Widgets/qSlicerVolumeRenderingModuleWidget.cxx
@@ -353,6 +353,14 @@ void qSlicerVolumeRenderingModuleWidget::onCurrentMRMLVolumeNodeChanged(vtkMRMLN
       // instead of whichever current one.
       dnode-&gt;Modified();
       }
+      /*
+       * Workaround nasty UI freeze with AMD RX480 and R7-260 GPUs
+       * http://discourse.slicer.org/t/commit-69e26835e-would-burn-my-discrete-gpu/1839/25
+       */
+      if (dnode-&gt;GetCroppingEnabled())
+       dnode-&gt;SetCroppingEnabled(false);
+      dnode-&gt;SetCroppingEnabled(true);
+      dnode-&gt;SetCroppingEnabled(false);
     }

   this-&gt;setMRMLDisplayNode(dnode);
</code></pre>
<p>Quite strange, as much as the unknown cause, as to how would this fix anything !</p>

---

## Post #27 by @pieper (2018-01-29 23:18 UTC)

<p>Interesting discovery.  It would indicate that there could be an uninitialized variable somewhere, probably in the driver,  It would be great of course if this issue could be tracked down and fixed at a level below Slicer because we would want to avoid hardware/driver specific code in the Slicer code base if we can avoid it (plus fixing at the source would have the most benefit for other users).</p>

---

## Post #28 by @chir.set (2018-03-31 13:39 UTC)

<p>Slicer commit 0efdac696 works flawlessly without any patch. No UI freeze. And cropping in Volume Rendering works with Depth Peeling on also. Both for nightly build 20180331 from your repository, and for Slicer locally built from source on Arch.  I guess it has to do with the VTK commit being used.</p>
<p>SimpleRayCast GPU rendering also works as expected on my discrete R7 M270 GPU, with VTK commit e42e7c4b76.</p>
<p>I wish to know what could have been the problem with 69e26835e, just out of curiosity.</p>
<p>Thanks.</p>

---

## Post #29 by @jcfr (2018-04-01 01:07 UTC)

<p>Thanks for the update. Since a lot of changes happen in the last three month, it’s gonna be hard to pin point the exact change addressing the problems. To get more insight, you could locally try this command:</p>
<pre><code class="lang-auto">cd VTK
gitk 590b341..7f00e99 ./Rendering/OpenGL2/
</code></pre>
<ul>
<li><a href="https://github.com/kitware/VTK/commit/590b341">590b341</a>: This corresponds to the VTK version (without Slicer/VTK patch) associated with Slicer commit <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26830">r26830</a></li>
<li><a href="https://github.com/kitware/VTK/commit/7f00e99">7f00e99</a>: This corresponds to the VTK version used in the latest Slicer <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27113">r27113</a></li>
</ul>
<p>Now, you mentioned that</p>
<aside class="quote no-group" data-username="chir.set" data-post="28" data-topic="1839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>SimpleRayCast GPU rendering also works as expected on my discrete R7 M270 GPU, with VTK commit e42e7c4b76.</p>
</blockquote>
</aside>
<p>This corresponds to a version of VTK newer that the one currently used in Slicer, here is the difference:  <a href="https://github.com/Kitware/VTK/compare/7f00e99...e42e7c4b76" class="inline-onebox">Comparing 7f00e99...e42e7c4b76 · Kitware/VTK · GitHub</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1aed224e4548be23485a13a80c3e8ae23217d67.png" data-download-href="/uploads/short-url/wctYW4ukUW6gdDsQXV5VfgesZ4X.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1aed224e4548be23485a13a80c3e8ae23217d67_2_690x214.png" alt="image" data-base62-sha1="wctYW4ukUW6gdDsQXV5VfgesZ4X" width="690" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1aed224e4548be23485a13a80c3e8ae23217d67_2_690x214.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1aed224e4548be23485a13a80c3e8ae23217d67_2_1035x321.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1aed224e4548be23485a13a80c3e8ae23217d67.png 2x" data-dominant-color="F9FAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1220×379 35.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will test and update the version currently used in Slicer.</p>

---

## Post #30 by @jcfr (2018-04-01 01:16 UTC)

<p>For reference, here is the PR updating VTK in Slicer: <a href="https://github.com/Slicer/Slicer/pull/928">https://github.com/Slicer/Slicer/pull/928</a></p>

---
