# virtualGL issue with nightly

**Topic ID**: 5050
**Date**: 2018-12-11
**URL**: https://discourse.slicer.org/t/virtualgl-issue-with-nightly/5050

---

## Post #1 by @muratmaga (2018-12-11 22:59 UTC)

<p>We have been using vgl to run Slicer remotely with HW acceleration on a Linux server quite a while now. I just installed one of the nightly from 12/06 and I am getting a blank Slicer window with these errors</p>
<blockquote>
<p>[maga@magalab-head ~]$ vglrun +v /home/apps/Slicer-4.11.0-2018-12-06-linux-amd64/Slicer<br>
[VGL] NOTICE: Added /usr/lib64/VirtualGL to LD_LIBRARY_PATH<br>
[VGL] Shared memory segment ID for vglconfig: 809205760<br>
[VGL] VirtualGL v2.4 64-bit (Build 20150505)<br>
[VGL] Opening connection to 3D X server :0<br>
[VGL] Shared memory segment ID for vglconfig: 809271310<br>
[VGL] VirtualGL v2.4 64-bit (Build 20150505)<br>
[VGL] Opening connection to 3D X server :0<br>
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to ‘/tmp/runtime-maga’<br>
QXcbIntegration: Cannot create platform OpenGL context, neither GLX nor EGL are enabled<br>
Switch to module:  “Data”<br>
QXcbIntegration: Cannot create platform OpenGL context, neither GLX nor EGL are enabled<br>
QXcbIntegration: Cannot create platform OpenGL context, neither GLX nor EGL are enabled<br>
QOpenGLWidget: Failed to create context</p>
</blockquote>
<p>4.8.1 works fine with the same vgl version.</p>
<blockquote>
<p>[maga@magalab-head ~]$ vglrun +v /home/apps/Slicer-4.8.1-linux-amd64/Slicer<br>
[VGL] NOTICE: Added /usr/lib64/VirtualGL to LD_LIBRARY_PATH<br>
[VGL] Shared memory segment ID for vglconfig: 809402427<br>
[VGL] VirtualGL v2.4 64-bit (Build 20150505)<br>
[VGL] Opening connection to 3D X server :0<br>
[VGL] Shared memory segment ID for vglconfig: 809467966<br>
[VGL] VirtualGL v2.4 64-bit (Build 20150505)<br>
[VGL] Opening connection to 3D X server :0<br>
Number of registered modules: 169<br>
Number of instantiated modules: 166<br>
[VGL] WARNING: VirtualGL attempted and failed to obtain a true color visual on<br>
[VGL]    the 3D X server :0 suitable for off-screen rendering.<br>
[VGL]    This is normal if the 3D application is probing for visuals with<br>
[VGL]    certain capabilities, but if the app fails to start, then make sure<br>
[VGL]    that the 3D X server is configured for true color and has accelerated<br>
[VGL]    3D drivers installed.<br>
[VGL] Using Pbuffers for rendering<br>
[VGL] Using pixel buffer objects for readback (BGR → BGRA)<br>
^XNumber of loaded modules: 166<br>
Switch to module:  “Data”</p>
</blockquote>
<p>Any suggestions how to mitigate this issue? I should note that nightly works fine if I actually interactively login to the server through regular X-session. Running through vgl seems to cause the issue.</p>

---

## Post #2 by @lassoan (2018-12-11 23:47 UTC)

<p>To run Slicer 4.9 and later, you need OpenGL 3.2.</p>

---

## Post #3 by @muratmaga (2018-12-12 00:35 UTC)

<p>Actually it turns out to be an issue with QT5 and openGL see <a href="https://sourceforge.net/p/virtualgl/mailman/message/32659289/" rel="nofollow noopener">https://sourceforge.net/p/virtualgl/mailman/message/32659289/</a></p>
<p>Updating my install of virtualgl to &gt;2.5 and using +xcb with vglrun resolved the issue.</p>

---

## Post #4 by @mattjolley (2019-06-13 19:09 UTC)

<p>We want to remote connect to linux machines in our lab with GPUs.  They are running RHEL(distro specified/supported by institution).  We do deep learning(doesn’t require OpenGL), but also want to look at the segmentation results on the remote machine using Slicer (hence the need for OpenGL).</p>
<p>We are struggling to get OpenGL support with Slicer over VNC.  Specifically we cannot move the MPR planes in Slicer over VNC.</p>
<p>If you have a stable implementation we would be very appreciative if you would share the details.</p>
<p>Thank You.</p>

---

## Post #5 by @pieper (2019-06-13 19:27 UTC)

<p><a class="mention" href="/u/mattjolley">@mattjolley</a> - do you have root access on your linux machine?</p>

---

## Post #6 by @mattjolley (2019-06-13 21:06 UTC)

<p>Yes.  We (or at least the linux admins) have root access.</p>
<p>Remote Desktops might end up working better for us to avoid VPN, but this is an option.</p>
<p>We started with TeamViewer, but it has crashed a lot.</p>

---

## Post #7 by @muratmaga (2019-06-13 22:40 UTC)

<p>Is your opengl problem specific to Slicer (i.e., can you get the other opengl programs working fine, what happens when you say vglrun +v glxinfo, do you see the correct driver for your graphics card being listed)?</p>
<p>I have a centos 7.2 system that I followed the default VirtualGL installation instructions (which is essentially adding this repo <a href="https://virtualgl.org/Downloads/YUM" rel="nofollow noopener">https://virtualgl.org/Downloads/YUM</a>), yum install VirtualGL and running vglserver_config.</p>

---

## Post #8 by @muratmaga (2019-06-13 22:47 UTC)

<p>Also if you are using a local linux machine with X, you really don’t need the vnc to connect to your remote HPC system. See vgltransport section in<br>
<a href="https://cdn.rawgit.com/VirtualGL/virtualgl/2.6.1/doc/index.html#hd008002" class="onebox" target="_blank" rel="nofollow noopener">https://cdn.rawgit.com/VirtualGL/virtualgl/2.6.1/doc/index.html#hd008002</a></p>
<p>vnc makes it easier for windows users…</p>

---
