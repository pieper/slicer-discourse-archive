# Slicer template based build environment using docker

**Topic ID**: 20398
**Date**: 2021-10-28
**URL**: https://discourse.slicer.org/t/slicer-template-based-build-environment-using-docker/20398

---

## Post #1 by @Dwij_Mistry (2021-10-28 06:03 UTC)

<p>Hi,</p>
<p>I am very new in Docker build environment setup can you please explain me how to setup and use docker baed environment.</p>
<p>I have gone through <a href="https://github.com/Slicer/SlicerBuildEnvironment" rel="noopener nofollow ugc">GitHub - Slicer/SlicerBuildEnvironment: A repository of scripts to set up a Slicer build environment.</a> but not getting how to setup for slicer custom templet.</p>
<p>Is there any way to do cmake and make using docker.<br>
or any other best way to build a code.</p>

---

## Post #2 by @lassoan (2021-10-29 03:49 UTC)

<p>Could you tell a bit more about what you would like to achieve? Build Slicer? Build extensions and to avoid building Slicer? Run Slicer?</p>

---

## Post #3 by @Dwij_Mistry (2021-11-08 12:20 UTC)

<p>I am building custom slicer from templet provided by <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">slicer cat</a></p>
<p>I have gone through <a href="https://github.com/Slicer/SlicerBuildEnvironment" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerBuildEnvironment</a> and able to build it but getting issue in how to execute the executable I am using "qt5-centos7 to use GCC 7 " based docker image.</p>
<p>I want to make run the executable in Windows 10.</p>
<p>But not getting how to achieve.</p>

---

## Post #4 by @lassoan (2021-11-08 19:16 UTC)

<p>The SlicerBuildEnvironment docker image is for testing the build. We have separate dockerfiles for running Slicer, which typically install a precompiled release in the image and set up a vnc server so that you can see the GUI of the application running in the container. Probably you can combine the two kinds of images.</p>
<p>However, to better reproduce the end-user experience, it is probably better to build Slicer using the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">standard build instructions</a> and test it by running directly, natively on a physical machine.</p>

---

## Post #5 by @Dwij_Mistry (2021-11-09 10:52 UTC)

<p>Thank you very much sir.</p>
<p>we are using standard build environment but facing issue while replicating build environment in multiple local system, however we are keeping same tool versions.<br>
Any solution for this?</p>

---

## Post #6 by @lassoan (2021-11-09 12:54 UTC)

<p>What operating systems are causing trouble? What problems do you have when replicating the build environment: build fails on some systems or the generated binaries are not compatible with each other?</p>

---

## Post #7 by @Dwij_Mistry (2021-11-10 06:37 UTC)

<p><strong>We are using following configuration for the development.</strong></p>
<p>Operating system: Windows 10<br>
CMAKE: 3.18.2<br>
NSIS: 3.08<br>
QT: 5.15.0<br>
Visual Studio community 2019</p>
<p>Error and warnings are attached<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a9e990ca7678a2a8e8d38bc222619c3169fe52e.png" data-download-href="/uploads/short-url/huK2PKk7cZpObeTyEIAlvBM8lqK.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a9e990ca7678a2a8e8d38bc222619c3169fe52e_2_690x388.png" alt="error" data-base62-sha1="huK2PKk7cZpObeTyEIAlvBM8lqK" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a9e990ca7678a2a8e8d38bc222619c3169fe52e_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a9e990ca7678a2a8e8d38bc222619c3169fe52e_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7a9e990ca7678a2a8e8d38bc222619c3169fe52e_2_1380x776.png 2x" data-dominant-color="283742"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1920×1080 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/565992d2090b093d6edbe5a04e0f3095e8df29f2.png" data-download-href="/uploads/short-url/cjSYjzHWPucO08GgjUoX2sQXrYm.png?dl=1" title="warnings" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/565992d2090b093d6edbe5a04e0f3095e8df29f2_2_690x388.png" alt="warnings" data-base62-sha1="cjSYjzHWPucO08GgjUoX2sQXrYm" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/565992d2090b093d6edbe5a04e0f3095e8df29f2_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/565992d2090b093d6edbe5a04e0f3095e8df29f2_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/565992d2090b093d6edbe5a04e0f3095e8df29f2_2_1380x776.png 2x" data-dominant-color="2A2F34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">warnings</span><span class="informations">1920×1080 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>reference for the 1st error is <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8aaf6bdcde2bd26daedcbef19920a974bca52fe.png" data-download-href="/uploads/short-url/xch3OhFPEcLC5O1c5zImpOhe3OS.png?dl=1" title="e1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8aaf6bdcde2bd26daedcbef19920a974bca52fe.png" alt="e1" data-base62-sha1="xch3OhFPEcLC5O1c5zImpOhe3OS" width="690" height="288" data-dominant-color="282C31"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">e1</span><span class="informations">1139×477 26.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>reference for the 2nd error is <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b302f0a4e2c43b12f708d76d58ad5ecf32d39d73.png" data-download-href="/uploads/short-url/pxBLv8H97G1sjwKLBY5CQS0mTVV.png?dl=1" title="e2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b302f0a4e2c43b12f708d76d58ad5ecf32d39d73.png" alt="e2" data-base62-sha1="pxBLv8H97G1sjwKLBY5CQS0mTVV" width="690" height="292" data-dominant-color="2F3437"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">e2</span><span class="informations">1166×494 43 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>reference for the 3rd,4th and 5th error is <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebccca3ae32c5d47db662c5d9bace336d1d398be.png" data-download-href="/uploads/short-url/xDYXTosm1KcUFLCaHv8U15ExI86.png?dl=1" title="e345" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebccca3ae32c5d47db662c5d9bace336d1d398be_2_690x237.png" alt="e345" data-base62-sha1="xDYXTosm1KcUFLCaHv8U15ExI86" width="690" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebccca3ae32c5d47db662c5d9bace336d1d398be_2_690x237.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebccca3ae32c5d47db662c5d9bace336d1d398be_2_1035x355.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebccca3ae32c5d47db662c5d9bace336d1d398be_2_1380x474.png 2x" data-dominant-color="2F363D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">e345</span><span class="informations">1482×511 54.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2021-11-10 13:56 UTC)

<p>Is this the latest version on Slicer master branch of <a href="https://github.com/Slicer/Slicer" class="inline-onebox">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>?<br>
Have you built from scratch or you have previously built an earlier version of the source code in the same build tree?</p>

---

## Post #9 by @Dwij_Mistry (2021-11-11 04:29 UTC)

<p>No, First build is from <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">custom SliceCAT templet by Kitware</a> ,</p>
<p>First build system configuration is<br>
<strong>EDDITION:</strong> Windows Server 2016 Standard Evaluation<br>
<strong>VERSION:</strong> 1607<br>
<strong>OS BUILD:</strong> 14393.4651</p>
<p>I would like to give you brief introduction regards our development.<br>
First we started building on above mentioned system.<br>
which we are still using.</p>
<p>Now we are expanding the development team, and providing local personal system with following Operating system configurations.<br>
<strong>EDDITION:</strong> Windows 10 Home Single Language<br>
<strong>VERSION:</strong> 20H2<br>
<strong>OS BUILD:</strong> 19042.1288</p>
<p>and how we are building is First we are taking our custom templet and building it, which is successfully building then we are replacing <strong>slicersource-src</strong> folder with our latest developed code. then we are building and getting errors as mentioned in previous answer.</p>
<p>moreover is there any way to implement GITHUB in our development?</p>

---

## Post #10 by @lassoan (2021-11-11 05:40 UTC)

<aside class="quote no-group" data-username="Dwij_Mistry" data-post="9" data-topic="20398">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dwij_mistry/48/15265_2.png" class="avatar"> Dwij_Mistry:</div>
<blockquote>
<p>and how we are building is First we are taking our custom templet and building it, which is successfully building then we are replacing <strong>slicersource-src</strong> folder with our latest developed code.</p>
</blockquote>
</aside>
<p>This can certainly lead to build errors. For performance reasons, not all dependencies are rebuilt when you just change the Slicer source folder, which may result in trying to build a new Slicer with an older CTK version. You can fix this by rebuilding CTK manually - opening the (slicer-build)\CTK-build\CTK.sln project in Visual Studio and build it in the appropriate build mode. But the clean solution is to update the template to pull Slicer source from your repository and then do a clean build.</p>
<p>I don’t think that’s the issue here, but Windows Server works quite differently from a regular Windows version. If you can, use non-server Windows edition.</p>

---
