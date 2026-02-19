---
topic_id: 17685
title: "Trying To Diagnose An Issue With Virtualgl And Slicer"
date: 2021-05-19
url: https://discourse.slicer.org/t/17685
---

# Trying to diagnose an issue with VirtualGL and Slicer

**Topic ID**: 17685
**Date**: 2021-05-19
**URL**: https://discourse.slicer.org/t/trying-to-diagnose-an-issue-with-virtualgl-and-slicer/17685

---

## Post #1 by @DRC (2021-05-19 01:46 UTC)

<p>I am the principal developer and sole maintainer of VirtualGL, a Linux OpenGL remote display framework.  Without going into too much gory detail about how VirtualGL works, suffice it to say that one particular VirtualGL mode emulates the GLX API using EGL/DRI commands, and that mode and only that mode has a bug that causes Slicer to render incorrectly when depth peeling and Display ROI are both enabled:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebf2e7ae894ddd4e4ddb9da56fa32e092cd5f225.jpeg" data-download-href="/uploads/short-url/xFiCSHiMNhHm5b7qINU2dNTbIKp.jpeg?dl=1" title="screen shot demonstrating the rendering issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebf2e7ae894ddd4e4ddb9da56fa32e092cd5f225_2_690x371.jpeg" alt="screen shot demonstrating the rendering issue" data-base62-sha1="xFiCSHiMNhHm5b7qINU2dNTbIKp" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebf2e7ae894ddd4e4ddb9da56fa32e092cd5f225_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ebf2e7ae894ddd4e4ddb9da56fa32e092cd5f225_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebf2e7ae894ddd4e4ddb9da56fa32e092cd5f225.jpeg 2x" data-dominant-color="A1999C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen shot demonstrating the rendering issue</span><span class="informations">1343×724 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The other VirtualGL modes work fine with Slicer, and the VirtualGL mode that fails with Slicer works fine with other applications.  Also, the failure only occurs when both depth peeling and Display ROI are enabled.  If either is disabled, everything works fine.  Thus, I’m hoping that someone can provide details regarding what happens behind the scenes in Slicer when both depth peeling and Display ROI are enabled.  I’ve pored over the source code, both for Slicer and VTK, and I can’t determine exactly what’s happening at the OpenGL level.  Also, very oddly, when I use apitrace to capture the Slicer workflow that would normally cause the issue, the issue cannot be reproduced when the captured OpenGL and GLX commands are replayed through apitrace.</p>
<p>To be 100% clear, this is my bug, not yours.  I’m just asking for help in understanding what Slicer is doing at the OpenGL level when both depth peeling and Display ROI are enabled.  Any assistance is greatly appreciated.</p>

---

## Post #3 by @lassoan (2021-05-19 02:54 UTC)

<p>It is awesome that you are working on this, thank you!</p>
<p>ROI widget is special because its sides are semitransparent. Since volume rendering is semi-transparent as well, <a href="https://blog.kitware.com/vtk-technical-highlight-dual-depth-peeling">depth peeling</a> is needed for correct rendering.</p>
<p>Depth peeling relies on the Z buffer. Maybe the issue is that somehow the Z buffer is not initialized or reset correctly or maybe its resolution is not sufficient? I can see some glitches with volume rendering + ROI widget display + depth peeling when using Intel Iris graphics (it does not happen with Nvidia) when zooming in and rotating around:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d380dc48041174d1902f280b34b5b9526529f9c.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d380dc48041174d1902f280b34b5b9526529f9c.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d380dc48041174d1902f280b34b5b9526529f9c.mp4</a>
    </source></video>
  </div><p></p>
<p>Is this similar to what you are seeing?<br>
Does it make any difference if you zoom in/out?</p>
<p>Note that recent Slicer Preview Releases use VTK9, which has lots of changes in the rendering pipeline. It would be interesting to see if this newer version works any better.</p>

---

## Post #4 by @muratmaga (2021-05-19 03:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="17685">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that recent Slicer Preview Releases use VTK9, which has lots of changes in the rendering pipeline. It would be interesting to see if this newer version works any better.</p>
</blockquote>
</aside>
<p>I can confirm that the issue continues to happen with the latest Linux preview:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e85ed5f932cb7bcf8c9b7f77ab16830bf7a6ee9.jpeg" data-download-href="/uploads/short-url/bcEbbM2G8FCM0FxwhA9hbttSNmh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e85ed5f932cb7bcf8c9b7f77ab16830bf7a6ee9_2_517x334.jpeg" alt="image" data-base62-sha1="bcEbbM2G8FCM0FxwhA9hbttSNmh" width="517" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e85ed5f932cb7bcf8c9b7f77ab16830bf7a6ee9_2_517x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4e85ed5f932cb7bcf8c9b7f77ab16830bf7a6ee9_2_775x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e85ed5f932cb7bcf8c9b7f77ab16830bf7a6ee9.jpeg 2x" data-dominant-color="BDBDCF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">839×543 89.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2021-05-19 03:47 UTC)

<p>Does it make a difference if you use perspective projection (instead of orthogonal) in the 3D view?<br>
Does it make any difference if you zoom in/out a lot?<br>
Does the artifact disappear if you disable and re-enable depth peeling or hide and show the ROI?</p>

---

## Post #6 by @muratmaga (2021-05-19 03:52 UTC)

<p>If I disable and then re-enable depth-peeling, artifact appears again.<br>
When I hide the ROI, artifact disappears. Showing it brings it back.<br>
Zooming in/out to extremes has no impact.<br>
Perspective vs orthogonal has no impact<br>
All tested with latest preview.</p>

---

## Post #7 by @lassoan (2021-05-19 03:54 UTC)

<p>Thank you. These behavior are all differ from what happens on Intel Iris graphics, so they seem to be unrelated problems.</p>

---

## Post #8 by @lassoan (2021-05-19 03:57 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> could you try if you see the same issue if you display the new markups ROI (not the old annotation ROI)?</p>

---

## Post #9 by @muratmaga (2021-05-19 03:59 UTC)

<p>It does, but a in a different way:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efb9ec0576ed4944a121942ce91c04c3885cb8cd.jpeg" data-download-href="/uploads/short-url/ycIrZajJVKLml8igQ4SSytogxPf.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efb9ec0576ed4944a121942ce91c04c3885cb8cd_2_516x349.jpeg" alt="image" data-base62-sha1="ycIrZajJVKLml8igQ4SSytogxPf" width="516" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efb9ec0576ed4944a121942ce91c04c3885cb8cd_2_516x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efb9ec0576ed4944a121942ce91c04c3885cb8cd_2_774x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efb9ec0576ed4944a121942ce91c04c3885cb8cd_2_1032x698.jpeg 2x" data-dominant-color="B7AAB8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1181×798 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @DRC (2021-05-19 04:01 UTC)

<p>VirtualGL’s EGL back end (the mode that emulates GLX using EGL/DRI) uses FBOs behind the scenes in order to emulate double buffering (because EGL doesn’t support double buffering for off-screen surfaces.)  I do notice that Slicer and/or VTK are using FBOs as well, so my guess is that VirtualGL is interfering somehow.  Can someone point me to the place in the Slicer and/or VTK code where the low-level OpenGL stuff is happening to implement depth peeling and Display ROI?</p>

---

## Post #11 by @lassoan (2021-05-19 04:50 UTC)

<p>Depth peeling is implemented in this rendering pass: <a href="https://github.com/Kitware/VTK/blob/master/Rendering/OpenGL2/vtkDualDepthPeelingPass.cxx">https://github.com/Kitware/VTK/blob/master/Rendering/OpenGL2/vtkDualDepthPeelingPass.cxx</a>. Have a look at how it is used in vtkOpenGLRenderer and vtkOpenGLGPUVolumeRayCastMapper classes. If you need help with debugging lower-level rendering mechanisms, it may make sense to ask VTK developers on the <a href="https://discourse.vtk.org/">VTK forum</a>.</p>

---

## Post #12 by @pieper (2021-05-19 15:20 UTC)

<p>It may be tricky, but folks on the VTK forum would I’m sure be very interested to see a pure-VTK example of this issue to help debugging (that is, to remove Slicer-related complexities).  E.g. maybe one could start with an example <a href="https://kitware.github.io/vtk-examples/site/Python/VolumeRendering/SimpleRayCast/">like this one</a> and add some depth peeling and transparent objects.</p>

---

## Post #13 by @DRC (2021-05-19 15:42 UTC)

<p>If I could bring up a VTK-only example, it would greatly facilitate me debugging the issue myself.  Alas, I have tried to bring up a few of them without success.  The main issue is that all of the examples I have found require newer versions of VTK, but the only machine I have that supports EGL/DRI is still running CentOS 7, which is too old to build those newer versions of VTK.  I will examine the source code, as advised above.</p>

---

## Post #14 by @pieper (2021-05-19 15:58 UTC)

<p>If you can diagnose from the source code that’s great.</p>
<p>But just FYI if you are able to run Slicer on the machine you can run vtk examples too.  If you download the example linked above to /tmp/SampleRayCast.py, and then give it a .vtk volume file as an argument it should work for you like this example:</p>
<p><code>~/Downloads/Slicer-4.11.20210226-linux-amd64/bin/PythonSlicer /tmp/SampleRayCast.py ~/Documents/MRHead.vtk</code></p>
<p>(here I made MRHead.vtk by downloading the MRHead from the SampleData module and saving it as .vtk format.)</p>

---

## Post #15 by @DRC (2021-05-20 19:56 UTC)

<p>Thanks for the tip about running VTK examples.  I guess I would just need an example that demonstrates the same type of rendering that Slicer performs when depth peeling and Display ROI are both enabled.  Unfortunately, such an example is beyond my ability to produce.</p>
<p>After examining the code and the apitrace logs more closely, I am still clueless as to what the problem is.  I may be wrong, but I don’t think it’s FBO-related.  VirtualGL’s EGL back end only interferes with FBO functions when the default framebuffer is being used, and since VTK creates and uses its own FBOs, there should be no interference.  It seems to me that if Z buffer initialization or resolution were the problem, then we should see the same rendering bug with the GLX back end, but we don’t.  (And it’s really telling that playing back the apitrace capture-- which, to be clear, was captured on the local display without VirtualGL-- through VirtualGL’s EGL back end also fails to reproduce the bug.  That’s the part that is really confusing me.)  Also, VirtualGL’s own unit tests are fairly comprehensive and include quite a few conformance checks to ensure that we are properly emulating double buffering for the default framebuffer without interfering with application-generated FBOs.  Also, although the EGL back end still lacks a few of the GLX and OpenGL features that the GLX back end supports, the apitrace logs don’t indicate that the application is using any of those features.</p>
<p>I’m afraid that, without a more stripped-down program that demonstrates the problem, there isn’t much more I can do about it.  I don’t have the resources to continue focusing on this.  I will note also that I have tried this example: <a href="https://vtk.org/Wiki/VTK/Tutorials/TranslucentGeometry" class="inline-onebox" rel="noopener nofollow ugc">VTK/Tutorials/TranslucentGeometry - KitwarePublic</a>, but it doesn’t reproduce the issue.</p>

---

## Post #16 by @DRC (2021-05-20 19:57 UTC)

<p>GitHub issue filed against VirtualGL: <a href="https://github.com/VirtualGL/virtualgl/issues/168" class="inline-onebox" rel="noopener nofollow ugc">EGL back end: incorrect rendering with 3D Slicer when depth peeling and "Display ROI" are both enabled · Issue #168 · VirtualGL/virtualgl · GitHub</a></p>

---

## Post #17 by @jcfr (2021-05-26 13:43 UTC)

<h3><a name="p-60217-stripped-down-program-1" class="anchor" href="#p-60217-stripped-down-program-1" aria-label="Heading link"></a>stripped-down program</h3>
<blockquote>
<p>without a more stripped-down program</p>
</blockquote>
<p>Could you try this implementation of the example (see <a href="https://kitware.github.io/vtk-examples/site/Cxx/Visualization/CorrectlyRenderTranslucentGeometry/">CorrectlyRenderTranslucentGeometry</a>) which is the up-to-date and maintained one.  (Thanks <a class="mention" href="/u/sankhesh_jhaveri">@Sankhesh_Jhaveri</a> for pointing this out <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=15" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20">)</p>
<p>Note that I didn’t have a chance to check if it was different from the one from  the wiki.</p>
<h3><a name="p-60217-version-of-vtk-2" class="anchor" href="#p-60217-version-of-vtk-2" aria-label="Heading link"></a>version of VTK</h3>
<p>Last, the version of VTK 9 we use in  Slicer is  <a href="https://github.com/Slicer/VTK/tree/slicer-v9.0.20201111-733234c785">Slicer/VTK@slicer-v9.0.20201111-733234c785</a>, could you try to build the example against this specific version to check if you can reproduce the problem ?</p>

---

## Post #18 by @pieper (2021-05-26 13:48 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p><a class="mention" href="/u/drc">@DRC</a> will you be able to build and test the example?</p>
<p>If not <a class="mention" href="/u/muratmaga">@muratmaga</a> and I have been discussing the option of creating a python test script to see if we can replicate the issue in pure VTK without Slicer.</p>

---

## Post #19 by @DRC (2021-05-27 16:04 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I was finally able to get that exact version of VTK to build on my machine, but unfortunately, the issue does not reproduce with the CorrectlyRenderTranslucentGeometry example.</p>

---

## Post #20 by @pieper (2021-05-28 20:11 UTC)

<p>You could try adding depth peeling to the example code <a class="mention" href="/u/alireza">@alireza</a> added here: <a href="https://discourse.slicer.org/t/incorrect-volume-rendering-bounds-first-and-last-slice/17827/5" class="inline-onebox">Incorrect volume rendering bounds - first and last slice - #5 by alireza</a></p>

---

## Post #21 by @DRC (2021-05-28 20:26 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I have no experience whatsoever with that and would not even know how to begin.</p>

---

## Post #22 by @pieper (2021-05-28 21:11 UTC)

<p>I would make the example for you but I’m tied up at least the next week.  If you nobody else can help you ping me again and I can give it a shot.</p>

---

## Post #23 by @DRC (2021-05-28 22:40 UTC)

<p>I’ll be gone for the next week anyhow and working on documentation after that, so there’s no huge rush.</p>

---

## Post #24 by @pieper (2021-06-21 17:11 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> tells me this issue is bottleneck for SlicerMorph, so it would be great to get to the bottom of it.  Unfortunately depth peeling seems to be touching low level in OpenGL driver code that is rarely used and different across platforms.</p>
<p><a href="https://gist.github.com/pieper/9d19de1b08f72f50ef29cdb243de4359">Here’s a script</a> that uses pure vtk python to do volume rendering with cropping and depth peeling that should be very similar to what Slicer does.  This renders script fine for me on mac and one linux machine but has some artifacts on a different linux machine (no VirtualGL involved).  It would be good to know if this can be used to track down the VirtualGL issue at the VTK level.</p>

---

## Post #25 by @DRC (2021-10-16 19:52 UTC)

<p>I believe that <a href="https://github.com/VirtualGL/virtualgl/commit/adabbd912ad0139c6bab698f8c20a18f2b8152e0" class="inline-onebox" rel="noopener nofollow ugc">EGLBE: Test/Fix issues with draw buffer state · VirtualGL/virtualgl@adabbd9 · GitHub</a> accidentally fixed this.  I can no longer reproduce the issue after that commit.</p>

---

## Post #26 by @pieper (2021-10-17 14:44 UTC)

<p>That’s great news, thanks for reporting back <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #27 by @lassoan (2021-10-17 17:41 UTC)

<p>This is great. What would we need to change in this Slicer docker image for Jupyter/Lab to get this fix?</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/Dockerfile">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/Dockerfile" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/Dockerfile" target="_blank" rel="noopener">Slicer/SlicerDocker/blob/master/slicer-notebook/Dockerfile</a></h4>


    <pre><code class="lang-">FROM debian:bullseye-20200422-slim

################################################################################
# Prevent apt-get from prompting for keyboard choice
#  https://superuser.com/questions/1356914/how-to-install-xserver-xorg-in-unattended-mode
ENV DEBIAN_FRONTEND=noninteractive

################################################################################
# Remove documentation to save hard drive space
#  https://askubuntu.com/questions/129566/remove-documentation-to-save-hard-drive-space
COPY etc/dpkg/dpkg.cfg.d/01_nodoc /etc/dpkg/dpkg.cfg.d/01_nodoc

################################################################################
# - update apt, set up certs, run netselect to get fast mirror
# - reduce apt gravity
# - and disable caching
#   from https://blog.sleeplessbeastie.eu/2017/10/02/how-to-disable-the-apt-cache/
RUN echo 'APT::Install-Recommends "0" ; APT::Install-Suggests "0" ;' &gt;&gt; /etc/apt/apt.conf &amp;&amp; \
    echo 'Dir::Cache::pkgcache "";\nDir::Cache::srcpkgcache "";' | tee /etc/apt/apt.conf.d/00_disable-cache-files &amp;&amp; \
    apt-get update -q -y
</code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/SlicerDocker/blob/master/slicer-notebook/Dockerfile" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #28 by @DRC (2021-10-19 15:08 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Unless you are using VirtualGL (and it doesn’t appear that you are), this issue is not relevant to you.</p>

---

## Post #29 by @lassoan (2021-10-19 18:23 UTC)

<p>Could you help with for switching to using VirtualGL? The dockerfile was created by someone else several years ago and I’m not sure what and how would need to be changed.</p>

---

## Post #30 by @DRC (2021-10-19 18:29 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Using VirtualGL isn’t just a matter of changing the Dockerfile.  You would need additional configuration on the host machine.  I do such work as a paid consultant, and if you are interested in hiring me, contact me off-list: <a href="https://virtualgl.org/About/Contact" class="inline-onebox" rel="noopener nofollow ugc">VirtualGL | About / Contact</a>.</p>

---

## Post #31 by @lassoan (2021-11-11 04:31 UTC)

<p>11 posts were split to a new topic: <a href="/t/volume-rendering-appearance-changes-if-roi-box-is-shown/20575">Volume rendering appearance changes if ROI box is shown</a></p>

---
