# How to solve the compilation problem of 3dslicer under the Linux system and arm64 architecture. Need help urgently!!!

**Topic ID**: 24251
**Date**: 2022-07-09
**URL**: https://discourse.slicer.org/t/how-to-solve-the-compilation-problem-of-3dslicer-under-the-linux-system-and-arm64-architecture-need-help-urgently/24251

---

## Post #1 by @wangyuyuyujun (2022-07-09 15:16 UTC)

<p>I want to install 3dslicer-5.0.2. I have installed qt5-5.13.0 and other dependencies, so I began to build 3dslicer from the source code. But when I compiled, there was an error. I found that linux-amd64 was configured after I executed the cmake command, but my computer was linux-arrch64, which led to an error when I compiled later. I don’t know whether 3dslicer can be compiled under arm64 architecture. If so, how can I modify the file so that cmake can correctly configure my computer? I hope you can help me. Thank you very much<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e884bd016ac96e22268be2c9706e20a9da82d99.png" data-download-href="/uploads/short-url/kkTOsNYuevjIQKSqHiXcAnm2kIN.png?dl=1" title="GAQ40PV%KYC0F)KV75GX" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e884bd016ac96e22268be2c9706e20a9da82d99.png" alt="GAQ40PV%KYC0F)KV75GX" data-base62-sha1="kkTOsNYuevjIQKSqHiXcAnm2kIN" width="535" height="500" data-dominant-color="181616"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">GAQ40PV%KYC0F)KV75GX</span><span class="informations">859×802 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a>Uploading: @N$5YEK{([LKXQ`OHN]@GR1.png…</a></p>

---

## Post #2 by @lassoan (2022-07-09 15:22 UTC)

<p>We have not attempted to build Slicer on arm64, so most likely you will run into issues. The most difficult part is 3D graphics, as there is a good chance that no suitable OpenGL drivers are available for your system.</p>
<p>What platform are you trying to build Slicer for?</p>
<p>What linux distro are you trying to use? <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> is working on something related - see <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SystoleOS/" class="inline-onebox">NA-MIC Project Weeks | Website for NA-MIC Project Weeks</a></p>

---

## Post #3 by @jamesobutler (2022-07-09 17:26 UTC)

<p>It’s been several years but maybe <a class="mention" href="/u/adamrankin">@adamrankin</a> or <a class="mention" href="/u/chir.set">@chir.set</a> have experimented more with Slicer for arm64.</p>
<aside class="quote quote-modified" data-post="1" data-topic="6459">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-for-ubuntu-arm64/6459">Slicer for Ubuntu arm64</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Notes on compilation efforts for compiling Slicer for arm64: 
Problem: VTK does not compile. 
Solution: 

Set VTK_OPENGL_HAS_EGL and VTK_OPENGL_HAS_ES
In &lt;SlicerDir&gt;/SuperBuild/External_VTK.cmake remove section that has -DModule_vtkGUISupportQtOpenGL:BOOL=ON in it
Edit QVTKOpenGLNativeWidget.cxx to use QOpenGLExtraFunctions instead of QOpenGLFunctions_3_2_Core


Problem: CTKAPPLAUNCHER is a download of amd64 
Solution: Overwrite executable &lt;Slicer-build&gt;/CTKAPPLAUNCHER/bin/CTKAppLauncher with co…
  </blockquote>
</aside>


---

## Post #4 by @wangyuyuyujun (2022-07-10 07:00 UTC)

<p>This is my machine information<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea165c00cd06977b686f5e4e6416f84e7a723e7.png" data-download-href="/uploads/short-url/rcovJyIDIvcoklP0AFMCzZgcgZx.png?dl=1" title="ZIHT_@MG}HUEG4NCDOOH(L" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea165c00cd06977b686f5e4e6416f84e7a723e7.png" alt="ZIHT_@MG}HUEG4NCDOOH(L" data-base62-sha1="rcovJyIDIvcoklP0AFMCzZgcgZx" width="690" height="131" data-dominant-color="070707"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ZIHT_@MG}HUEG4NCDOOH(L</span><span class="informations">1274×243 8.41 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
When building slicer, the system will depend on it, but these packages are AMD64, so my computer can’t run these binaries directly. Later, I found that there was a problem in the configuration, that is, the above problem. At present, I don’t know how to proceed to the next step. Do you have any good suggestions</p>

---

## Post #6 by @wangyuyuyujun (2022-07-10 07:11 UTC)

<p>There is no problem with pre dependencies and OpenGL. When I execute make -j 128 compilation, the system will automatically download, configure and compile some dependencies, but these dependencies are based on AMD64 architecture. Can I manually carry out this process to adapt my machine</p>

---

## Post #7 by @lassoan (2022-07-10 12:19 UTC)

<p>All dependencies are specified in CMake files in the SuperBuild folder. You can choose to build any of them before building Slicer and then set <code>Slicer_USE_SYSTEM_...=ON</code> CMake variable when you configure Slicer. To get started, you can disable Python support in Slicer to reduce the number of dependencies that you need to deal with.</p>

---

## Post #8 by @RafaelPalomar (2022-07-11 12:35 UTC)

<p><a class="mention" href="/u/wangyuyuyujun">@wangyuyuyujun</a>, <code>i386</code> and <code>amd64</code> seem to be hard-coded values in <a href="https://github.com/Slicer/Slicer/blob/115e32bdf8e478208fc2c75179cf2ecdb555d984/CMake/SlicerMacroGetOperatingSystemArchitectureBitness.cmake#L45-L50" rel="noopener nofollow ugc">here</a>. For the sake of moving forward with you project I suggest that you change <code>amd64</code> by your architecture as a workaround. Making this the right way is something we would need to do for the <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/SystoleOS/" rel="noopener nofollow ugc">Systole OS project</a>, but the priority on that project is to have a complete working version of Slicer for i386/amd64 first.</p>
<p>I hope this helps.</p>

---
