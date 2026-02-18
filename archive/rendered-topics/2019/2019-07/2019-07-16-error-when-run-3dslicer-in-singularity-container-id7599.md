# Error when run 3DSlicer in singularity container

**Topic ID**: 7599
**Date**: 2019-07-16
**URL**: https://discourse.slicer.org/t/error-when-run-3dslicer-in-singularity-container/7599

---

## Post #1 by @lxwgcool (2019-07-16 00:22 UTC)

<h2><a name="p-26686-the-following-errors-is-reported-when-i-run-3dslicer-in-singularity-container-1" class="anchor" href="#p-26686-the-following-errors-is-reported-when-i-run-3dslicer-in-singularity-container-1" aria-label="Heading link"></a>The following errors is reported when i run 3DSlicer in singularity container:</h2>
<h2><a name="p-26686-x-error-badvalue-integer-parameter-out-of-range-for-operation-2-extension-155-uknown-extension-minor-opcode-3-unknown-request-resource-id-0x0-cannot-create-glx-context-aborting-2" class="anchor" href="#p-26686-x-error-badvalue-integer-parameter-out-of-range-for-operation-2-extension-155-uknown-extension-minor-opcode-3-unknown-request-resource-id-0x0-cannot-create-glx-context-aborting-2" aria-label="Heading link"></a>X Error: BadValue (integer parameter out of range for operation) 2<br>
Extension:    155 (Uknown extension)<br>
Minor opcode: 3 (Unknown request)<br>
Resource id:  0x0<br>
Cannot create GLX context.  Aborting.</h2>
<p>The singularity container is created based on ubuntu 16.04.<br>
3DSlicer is downloaded from 3DSlicer released archive.<br>
The version of 3D slicer i tried is v4.4 and v4.5.1.<br>
Phenomenon: the GUI of 3DSlicer stuck for few seconds and  then closed automatically. Please check the screenshot below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbe3c8a4bfd583cb25427162e0b464dfd405d6ba.png" data-download-href="/uploads/short-url/t5GWXvtdFR7BHbSYBbAhAU9CrPk.png?dl=1" title="Screenshot%20from%202019-07-15%2017-48-00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe3c8a4bfd583cb25427162e0b464dfd405d6ba_2_662x500.png" alt="Screenshot%20from%202019-07-15%2017-48-00" data-base62-sha1="t5GWXvtdFR7BHbSYBbAhAU9CrPk" width="662" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe3c8a4bfd583cb25427162e0b464dfd405d6ba_2_662x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe3c8a4bfd583cb25427162e0b464dfd405d6ba_2_993x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbe3c8a4bfd583cb25427162e0b464dfd405d6ba_2_1324x1000.png 2x" data-dominant-color="4E4D4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202019-07-15%2017-48-00</span><span class="informations">1372×1035 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried this singularity container in two host machines, one with OS ubuntu 18.01 and another with OS redhat 6.7. I got the same error in both of those two host machines.</p>
<p>No idea how to solve this problem.</p>
<p>Thanks so much for any suggestion.<br>
Best<br>
Xin</p>

---

## Post #2 by @pieper (2019-07-16 11:53 UTC)

<p>Hi -</p>
<p>You need a OpenGL support in your X server to run Slicer.</p>
<p>I haven’t done it for Singularity, but it works well for Docker (no GPU acceleration, but software emulation works well).</p>
<p>Let us know how it goes.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/SlicerDockers/blob/master/x11/Dockerfile" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerDockers/blob/master/x11/Dockerfile" target="_blank" rel="nofollow noopener">pieper/SlicerDockers/blob/master/x11/Dockerfile</a></h4>
<pre><code class="lang-"># DOCKER-VERSION 1.0
# x11 image for other SlicerDocker platform images
# (based on https://github.com/dit4c/dockerfile-dit4c-container-x11 debian branch)
FROM stevepieper/base
MAINTAINER pieper@isomics.com

# Install
# - MESA DRI drivers for software GLX rendering
# - X11 dummy &amp; void drivers
# - RandR utility
# - X11 xinit binary
# - reasonable fonts for UI
# - x11vnc
# - python-websockify
# - openbox
# - tint2
# - xterm
# - lxrandr
# - nitrogen
RUN apt-get update &amp;&amp; DEBIAN_FRONTEND=noninteractive apt-get install -y \
</code></pre>

  This file has been truncated. <a href="https://github.com/pieper/SlicerDockers/blob/master/x11/Dockerfile" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lxwgcool (2019-07-18 16:23 UTC)

<p>Hi Steve,</p>
<p>Thanks so much for your reply. Since i need to run 3DSlicer in HPC cluster, I cannot use docker to do it (which requires sudo).</p>
<p>I think the X server in our HPC cluster should support opengl, since i can run multiple GUI based software in our cluster. Here is the output of “glxinfo”:</p>
<pre><code class="lang-auto">--------------
xil14026admin@cn01:~$ glxinfo | grep render
direct rendering: Yes
    GLX_MESA_multithread_makecurrent, GLX_MESA_query_renderer, 
    GLX_MESA_query_renderer, GLX_OML_swap_method, GLX_SGI_make_current_read, 
OpenGL renderer string: Gallium 0.4 on llvmpipe (LLVM 3.6, 128 bits)
    GL_EXT_vertex_array_bgra, GL_NV_conditional_render, 
    GL_ARB_clip_control, GL_ARB_conditional_render_inverted, 
--------------
</code></pre>
<p>I think the reason i get this error maybe caused by 3DSlicer tries to write something in system folder (such as libpulse). Is there any way to remove all the libraries, which require access to the system folder and write something in it during the runtime? If it could be, recompiling a special version of 3DSlicer without contain those sytem-folder-write-based functions may let 3DSclier fit HPC cluster.</p>
<p>Thanks so much for your help<br>
Best<br>
Xin</p>

---

## Post #4 by @pieper (2019-07-18 17:13 UTC)

<p>There really wouldn’t be anything in Slicer that requires sudo, but I really don’t have any experience with Singularity so perhaps it adds extra constraints.  Are you able to run other graphics apps inside Singularity, like glxgears or ParaView?  It would be nice to get this working, since it sounds like a pretty common use case (cluster nodes with no root access).</p>

---

## Post #5 by @lxwgcool (2019-07-18 21:17 UTC)

<p>Dear Steve,</p>
<p>Thanks so much for your prompt reply. I just compiled 3DSlicer installation package (4.9) through docker in my desktop (ubuntu 18.04). I also created a new singularity container through my original recipe file. It seems works in both of my desktop (ubuntu 18.04) and our cluster (redhat 6.7).</p>
<p>I will spend additional time to check why the old singularity container doesn’t work.<br>
I am all set now. Thanks so much for your time.<br>
Best<br>
Xin</p>

---

## Post #6 by @pieper (2019-07-19 00:04 UTC)

<p>That’s great Xin <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:">  - any chance you could share the instructions / recipe / image for future reference.</p>

---

## Post #7 by @lxwgcool (2019-07-19 00:40 UTC)

<p>Sure Steve:)  I work for UConn HPC 16 hours per week during summer. I will back to office on Monday next week and create a recipe file of singularity for 3DSlicer. Please let me know what is your favorite way to share files.</p>
<p>Have a good night<br>
Best<br>
Xin</p>

---

## Post #8 by @pieper (2019-07-19 00:58 UTC)

<p>Thanks Xin - that will be excellent.  I think a github repository is best for the recipe, and then maybe an image in singularity hub (I think that’s the right terminology, but whatever corresponds to github Dockerfile and dockerhub).</p>

---

## Post #9 by @lxwgcool (2019-07-22 22:19 UTC)

<p>Dear Pieper,</p>
<p>I already uploaded the recipe file and readme doc of how to build/use 3DSlicer with singularity container.<br>
Please check the link below:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/lxwgcool/singularity" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars1.githubusercontent.com/u/11053933?s=400&amp;amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/lxwgcool/singularity" target="_blank" rel="nofollow noopener">lxwgcool/singularity</a></h3>

<p>singularity-recipe-share. Contribute to lxwgcool/singularity development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Have a good night<br>
Best<br>
Xin</p>

---

## Post #10 by @pieper (2019-07-23 12:20 UTC)

<p>Thanks for posting that Xin! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---
