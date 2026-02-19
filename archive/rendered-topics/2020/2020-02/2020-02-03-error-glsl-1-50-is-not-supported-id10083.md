---
topic_id: 10083
title: "Error Glsl 1 50 Is Not Supported"
date: 2020-02-03
url: https://discourse.slicer.org/t/10083
---

# error: GLSL 1.50 is not supported

**Topic ID**: 10083
**Date**: 2020-02-03
**URL**: https://discourse.slicer.org/t/error-glsl-1-50-is-not-supported/10083

---

## Post #1 by @justauser (2020-02-03 14:01 UTC)

<p>Operating system:CentOS-7.6<br>
Slicer version: 4.11.0<br>
nvidia driver 418.87, cuda 10.1</p>
<p>Expected behavior: displays a DICOM image<br>
Actual behavior:doesn’t display anything, and issues errors such as:</p>
<p>error: GLSL 1.50 is not supported. Supported versions are: 1.10, 1.20, 1.30, 1.00 ES, and 3.00 ES</p>
<p>I don’t know if the error message is connected with the lack of DICOM display.</p>
<p>Any suggestions?</p>

---

## Post #2 by @pieper (2020-02-04 16:29 UTC)

<p>Hi -</p>
<p>It can be a challenge to get GPU drivers working on linux - here are some instructions that might help, based on <a href="https://github.com/QIICR/SlicerGCPSetup/blob/master/README.md">this document about how to start from scratch on a virtual machine</a>.  The are for debian but centos should be similar I guess.</p>
<pre><code class="lang-auto">Execute the following and take note of the BusID

sudo nvidia-xconfig --query-gpu-info
Open the X11 configuration file

sudo vim /etc/X11/xorg.conf
and insert the following BusID line using the BusID value you retrieved earlier into this Section:

Section "Device"
   Identifier     "Device0"
   Driver         "nvidia"
   VendorName     "NVIDIA Corporation"
   BusID          "PCI:0:4:0"
EndSection
or if /etc/X11/xorg.conf does not exist, create a file in /usr/share/X11/xorg.conf.d/xorg.conf with the contents listed above.
</code></pre>

---

## Post #3 by @justauser (2020-02-04 17:52 UTC)

<p>Thanks for replying. Sorry I should have said I have a GPU with nvidia driver installed ok but running headless and a remote x11 display. I get the same errors even after creating xorg.conf files with BusID.<br>
The error seems to be output alongside a dump of vtkPolyData2DVS.glsl (54 lines starting with 1: <span class="hashtag">#version</span> 150</p>

---

## Post #4 by @pieper (2020-02-04 18:58 UTC)

<p>It’s probably your remote X11 session that’s leading to the crash then.</p>
<p>I suggest using VNC to connect and let the remote machine do the rendering, like is shown in this video (which used the setup described in the link I sent earlier):</p>
<div class="lazyYT" data-youtube-id="oHZBFm02wbM" data-youtube-title="MGH100um remote rendering" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque&amp;start=5"></div>

---

## Post #5 by @muratmaga (2020-02-04 21:31 UTC)

<p>My suggestion is to get VirtualGL installed on your Linux system, and connect it via VNC (vgl sister project TurboVNC works really well, even on broadband) or  vglconnect (to tunnel) and execute Slicer (or any openGL based application) via vglrun command.</p>
<p>Instructions for installing on Linux:<br>
<a href="https://cdn.rawgit.com/VirtualGL/virtualgl/2.6.3/doc/index.html#hd005001" class="onebox" target="_blank" rel="nofollow noopener">https://cdn.rawgit.com/VirtualGL/virtualgl/2.6.3/doc/index.html#hd005001</a></p>

---

## Post #6 by @justauser (2020-02-04 23:10 UTC)

<p>Thanks for the tips. I had not heard of VirrtualGL, interesting.</p>
<p>However I have found a possible solution!</p>
<p>(MESA_GL_VERSION_OVERRIDE=3.2 ./Slicer )</p>
<p>I am not sure why it works but I can at least see a DICOM image now.<br>
And the error message has gone away.</p>

---

## Post #7 by @kpopuri (2020-10-07 17:07 UTC)

<p>This worked for us too! we were having trouble getting slicer to work over RDP . We actually set:</p>
<p><code>export MESA_GL_VERSION_OVERRIDE=3.3</code></p>
<p>according to our installed GL driver version:</p>
<pre><code>CentOS Linux release 7.7.1908 (Core)

server glx version string: 1.4
 client glx version string: 1.4
 GLX version: 1.4
 Max core profile version: 3.3
 Max compat profile version: 3.0
 Max GLES1 profile version: 1.1
 Max GLES[23] profile version: 3.0
OpenGL core profile version string: 3.3 (Core Profile) Mesa 18.0.5
 OpenGL core profile shading language version string: 3.30
 OpenGL version string: 3.0 Mesa 18.0.5
 OpenGL shading language version string: 1.30
 OpenGL ES profile version string: OpenGL ES 3.0 Mesa 18.0.5
 OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.00</code></pre>

---

## Post #8 by @tbillah (2020-11-13 19:47 UTC)

<p>Hi <a class="mention" href="/u/kpopuri">@kpopuri</a>, given your <code>ES 3.0</code> already satisfying minimum requirement:</p>
<blockquote>
<p>OpenGL ES profile version string: OpenGL ES 3.0 Mesa 18.0.5</p>
</blockquote>
<p>Did you realize why you needed the hack in the first place?</p>

---

## Post #9 by @kpopuri (2020-11-13 19:54 UTC)

<p><a class="mention" href="/u/tbillah">@tbillah</a> actually setting <code>export MESA_GL_VERSION_OVERRIDE=3.0</code> also does the trick, so I think the issue is not with the availability of the compatible openGL libs but rather letting slicer know about their existence. I am guessing slicer checks for some ENV variable to figure out the openGL version and if it cannot find the ENV variable, it defaults to setting that variable to an older GSL version (GSL 1.5) and then the downstream rendering engine reads that and falsely raises an error.</p>

---

## Post #10 by @tbillah (2020-11-13 19:59 UTC)

<p>Hello <a class="mention" href="/u/pieper">@pieper</a>, this may need more attention. If I am not parsing the log wrong, someone has:</p>
<blockquote>
<p>OpenGL ES profile version string: OpenGL ES 3.0 Mesa 18.0.5</p>
</blockquote>
<p>Yet, Slicer raised the reported error for them.</p>
<p>For what it’s worth, the hack worked for me on a cluster that has <code>OpenGL ES 2.0</code></p>

---

## Post #11 by @pieper (2020-11-14 16:42 UTC)

<p>I don’t use this approach for OpenGL on X (I use the methods I described above), so I don’t have much to suggest here.  Do other VTK-based programs work? (e.g. try ParaView and also VTK examples built from source).</p>

---
