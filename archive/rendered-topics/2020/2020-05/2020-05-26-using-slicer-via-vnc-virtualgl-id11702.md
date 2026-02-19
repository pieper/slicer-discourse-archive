---
topic_id: 11702
title: "Using Slicer Via Vnc Virtualgl"
date: 2020-05-26
url: https://discourse.slicer.org/t/11702
---

# Using Slicer via VNC + VirtualGL

**Topic ID**: 11702
**Date**: 2020-05-26
**URL**: https://discourse.slicer.org/t/using-slicer-via-vnc-virtualgl/11702

---

## Post #1 by @Deepa (2020-05-26 03:39 UTC)

<p>I’m trying to access Slicer installed on a server through tigervnc client. But I get the following error</p>
<pre><code>[user@server ~]$ vglrun glxgears
No protocol specified
Error: couldn't open display :0
[user@server ~]$ vncserver -list

TigerVNC server sessions:

X DISPLAY #     PROCESS ID
:1              10902
:5              14662
[user@server ~]$ export DISPLAY=:1
[user@server ~]$ cd Slicer-4.11.0-2020-05-19-linux-amd64/
[user@server Slicer-4.11.0-2020-05-19-linux-amd64]$ vglrun ./Slicer
No protocol specified
[VGL] ERROR: Could not open display :0.
vtkDebugLeaks has found no leaks.
</code></pre>
<p>I’ve used export DISPLAY=:1 and I still get [VGL] ERROR: Could not open display :0.<br>
Any help?</p>

---

## Post #2 by @muratmaga (2020-05-26 04:31 UTC)

<p>I think the first command shows that either</p>
<ol>
<li>There is no X0 session running or</li>
<li>VirtualGL is not configured correctly.</li>
</ol>
<p>Particularly did you run the vglserver_config after installtin the VGL? If so, did you restricted the framebuffer access to vglusers (which is default). You may have to add your user to vglusers groups.</p>
<p>Follow the specific instructions for correctly configuring the server here:<br>
<a href="https://cdn.rawgit.com/VirtualGL/virtualgl/2.6.3/doc/index.html#hd006" class="onebox" target="_blank" rel="nofollow noopener">https://cdn.rawgit.com/VirtualGL/virtualgl/2.6.3/doc/index.html#hd006</a></p>
<p>If you can’t get glxgears working, it is unlikely that Slicer would work.</p>

---

## Post #3 by @Deepa (2020-05-26 09:45 UTC)

<p>Thank you.</p>
<p>I didn’t add the display flag last time. After adding the display flag I get,</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="11702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>framebuffer access to vglusers (which is default). You may have to add your user to vglusers groups.</p>
</blockquote>
</aside>
<p>I think the issue that currently occurs is due to the above reason that you mentioned<br>
vglrun -d :1 glxgears<br>
[VGL] NOTICE: Automatically setting VGL_CLIENT environment variable to<br>
[VGL]    xx.x.x.xx, the IP address of your SSH client.<br>
failed to create drawable<br>
[VGL] ERROR: in OGLDrawable–<br>
[VGL]    82: Could not create Pbuffer</p>

---

## Post #4 by @muratmaga (2020-05-26 17:20 UTC)

<p>If you are remoting into your session via vnc directly, you really don’t need to set the display parameter.<br>
To me error still tell me that the user is not part of the vglusers group, and VGL doesn’t have permission to access the framebuffer.</p>
<p>if you say</p>
<p><code>&gt; id $USER</code></p>
<p>do you see vglusers group listed in the output, otherwise it won’t work.</p>

---

## Post #6 by @Deepa (2020-06-03 10:55 UTC)

<aside class="quote no-group" data-username="justauser" data-post="6" data-topic="10083">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/aca169/48.png" class="avatar"><a href="https://discourse.slicer.org/t/error-glsl-1-50-is-not-supported/10083/6">error: GLSL 1.50 is not supported</a></div>
<blockquote>
<p>MESA_GL_VERSION_OVERRIDE=3.2 ./Slicer</p>
</blockquote>
</aside>
<p>from <a href="https://discourse.slicer.org/t/error-glsl-1-50-is-not-supported/10083/4" class="inline-onebox">error: GLSL 1.50 is not supported - #4 by pieper</a> helped.</p>
<p>Unfortunately, even after changing the VGL permission settings to allow all users, VGL didn’t work for me.</p>
<p>Thanks for the support</p>

---

## Post #7 by @mau_igna_06 (2022-04-27 12:11 UTC)

<p>Did you achieve VGL working for Slicer?</p>

---

## Post #8 by @Deepa (2022-04-27 15:52 UTC)

<p>Yes, I think <code>MESA_GL_VERSION_OVERRIDE=3.2 ./Slicer </code> worked for me.</p>

---

## Post #9 by @muratmaga (2022-04-28 16:30 UTC)

<p>Correctly setup VGL shouldn’t require this override, since it should provide a opengl version that’s compatible with Slicer e.g.,</p>
<pre><code class="lang-auto">maga@magalab-ML:~/Downloads$ vglrun /opt/VirtualGL/bin/glxinfo |more
name of display: :1.0
display: :1  screen: 0
direct rendering: Yes
server glx vendor string: VirtualGL
server glx version string: 1.4
server glx extensions:
    GLX_ARB_create_context, GLX_ARB_create_context_profile, 
    GLX_ARB_get_proc_address, GLX_ARB_multisample, GLX_EXT_swap_control, 
    GLX_EXT_visual_info, GLX_EXT_visual_rating, GLX_SGIX_fbconfig, 
    GLX_SGIX_pbuffer, GLX_SGI_make_current_read, GLX_SGI_swap_control
client glx vendor string: VirtualGL
client glx version string: 1.4
client glx extensions:
    GLX_ARB_create_context, GLX_ARB_create_context_profile, 
    GLX_ARB_get_proc_address, GLX_ARB_multisample, GLX_EXT_swap_control, 
    GLX_EXT_visual_info, GLX_EXT_visual_rating, GLX_SGIX_fbconfig, 
    GLX_SGIX_pbuffer, GLX_SGI_make_current_read, GLX_SGI_swap_control
GLX version: 1.4
GLX extensions:
    GLX_ARB_create_context, GLX_ARB_create_context_profile, 
    GLX_ARB_get_proc_address, GLX_ARB_multisample, GLX_EXT_swap_control, 
    GLX_EXT_visual_info, GLX_EXT_visual_rating, GLX_SGIX_fbconfig, 
    GLX_SGIX_pbuffer, GLX_SGI_make_current_read, GLX_SGI_swap_control
Memory info (GL_NVX_gpu_memory_info):
    Dedicated video memory: 8192 MB
    Total available memory: 8192 MB
    Currently available dedicated video memory: 7356 MB
OpenGL vendor string: NVIDIA Corporation
OpenGL renderer string: Quadro RTX 4000/PCIe/SSE2
OpenGL core profile version string: 4.6.0 NVIDIA 470.82.01
OpenGL core profile shading language version string: 4.60 NVIDIA
OpenGL core profile context flags: (none)
OpenGL core profile profile mask: core profile
OpenGL core profile extensions:
</code></pre>

---

## Post #10 by @mau_igna_06 (2022-04-28 20:21 UTC)

<p>I’ve made it work. I’ll share details on a few days</p>

---

## Post #11 by @muratmaga (2022-04-28 20:26 UTC)

<p>Good to hear. We have been using VGL for a while, almost never had any installation/configuration issues for vanilla centos or ubuntu. Love to hear your use case.</p>

---

## Post #12 by @mau_igna_06 (2022-04-30 01:31 UTC)

<p>Our team started from <a href="https://github.com/SlicerMorph/SlicerMorphCloud" rel="noopener nofollow ugc">this repository</a> some months ago.</p>
<p>But we wanted not to execute a window manager on our environment.</p>
<p>The TurboVNC manual tells you how to do this <a href="https://rawcdn.githack.com/TurboVNC/turbovnc/3.0beta1/doc/index.html#hd009001" rel="noopener nofollow ugc">here</a>:</p>
<blockquote>
<h3>Procedure</h3>
<ol>
<li>Follow the procedure described in Chapter <a href="https://rawcdn.githack.com/TurboVNC/turbovnc/3.0beta1/doc/index.html#TurboVNC_Usage" rel="noopener nofollow ugc">6</a> for starting a TurboVNC session and connecting to it.</li>
<li>Open a new terminal inside the TurboVNC desktop.</li>
<li>In the terminal, start a 3D application using VirtualGL:<br>
<code>/opt/VirtualGL/bin/vglrun [vglrun options] 3D-application-executable-or-script [arguments]</code></li>
</ol>
</blockquote>
<p>So, supposing we have achieved 1.<br>
We just need to do 2. and 3.</p>
<ol start="2">
<li>can be translated by unix convention to prefixing the contents of the next line to the code on 3.<br>
<code>DISPLAY=$VNCDISPLAY sh</code></li>
</ol>
<p>So with 3. (leaving default options) our total command is:<br>
<code>DISPLAY=$VNCDISPLAY sh /opt/VirtualGL/bin/vglrun path/to/slicer/Slicer</code></p>
<p>But that doesn’t work, at least on our configuration.</p>
<p>Searching the error code on the VirtualGL issues solves this, <a href="https://github.com/VirtualGL/virtualgl/issues/184#issuecomment-988812275" rel="noopener nofollow ugc">according to dcommander</a>:</p>
<blockquote>
<p><code>eglinfo</code> accesses the DRI devices in the same way that VirtualGL does, so if <code>eglinfo egl</code> works, that suggests that <code>VGL_DEVICE=egl</code> should work. As to why the specific DRI devices don’t work, I have no idea. Perhaps the user account does not have appropriate permissions for the matching <strong>/dev/dri/render</strong> * devices? Did you run <code>vglserver_config</code> in the container?</p>
</blockquote>
<p>The key here is that <code>VGL_DEVICE=egl</code> should work.</p>
<p>That means setting the option <code>-d egl</code> on <code>vglrun</code> according to its help-text.</p>
<p>So our corrected command is:<br>
<code>DISPLAY=$VNCDISPLAY sh /opt/VirtualGL/bin/vglrun -d egl path/to/slicer/Slicer</code></p>
<p>And it correctly works.</p>

---
