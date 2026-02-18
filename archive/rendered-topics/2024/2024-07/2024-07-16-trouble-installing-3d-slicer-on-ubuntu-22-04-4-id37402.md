# Trouble Installing 3D Slicer on Ubuntu 22.04.4

**Topic ID**: 37402
**Date**: 2024-07-16
**URL**: https://discourse.slicer.org/t/trouble-installing-3d-slicer-on-ubuntu-22-04-4/37402

---

## Post #1 by @dat-rohit (2024-07-16 14:05 UTC)

<p>Hey everyone,</p>
<p>I’m trying to install 3D Slicer and I am encountering an issue where I’m unable to launch the application due to what seems to be like a graphical rendering error. Here are the details of the problem and steps I’ve already taken:</p>
<ul>
<li>
<p>I am installing 3D Slicer on a GPU cluster and hence I am connected to it via SSH with the -X option (for graphics display)</p>
</li>
<li>
<ul>
<li>Operating System: Ubuntu 2.04.4 LTS (Jammy Jellyfish)</li>
</ul>
</li>
<li></li>
<li>
<p><strong>3D Slicer Version:</strong> 5.6.2</p>
</li>
<li>
<p>GPU: NVIDIA GeForce RTX 3090</p>
</li>
<li></li>
<li>
<p>CUDA Version: 12.2</p>
</li>
<li>
<p>When I try to launch 3D Slicer (<code>./Slicer</code>), the GUI layout popup but the inside is blank and I receive the following error message:</p>
</li>
</ul>
<pre><code class="lang-auto">Error #1 while writing setting "Modules/AdditionalPaths"
Error #1 while writing setting "Modules/IgnoreModules"
Error #1 while writing setting "Extensions/ManagerEnabled"
Error #1 while writing setting "Extensions/ServerUrl"
Error #1 while writing setting "Extensions/FrontendServerUrl"
Error #1 while writing setting "Extensions/InstallPath"
Switch to module:  "Welcome"
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
Ignore argument received via command-line (not a valid URL or existing local file):  "--debug-output"
composeAndFlush: QOpenGLContext creation failed
composeAndFlush: makeCurrent() failed
composeAndFlush: makeCurrent() failed
composeAndFlush: makeCurrent() failed
composeAndFlush: makeCurrent() failed
composeAndFlush: makeCurrent() failed
composeAndFlush: makeCurrent() failed
composeAndFlush: makeCurrent() failed
composeAndFlush: makeCurrent() failed
</code></pre>
<p><em>The <code>composeAndFlush: makeCurrent() failed</code> continues recursively until I terminate the process.</em></p>
<ul>
<li>
<p>I already tried manually setting the following variables: LD_LIBRARY_PATH, QT_QPA_PLATFORM_PLUGIN_PATH, LIBGL_ALWAYS_INDIRECT=1, LIBGL_ALWAYS_SOFTWARE=1, LIBGL_ALWAYS_INDIRECT=1, QT_XCB_GL_INTEGRATION=xcb_egl<br>
 → None of it helps</p>
</li>
<li>
<p>I tried checking for any missing libraries with <code>ldd ./Slicer</code>:</p>
</li>
</ul>
<pre><code class="lang-auto">linux-vdso.so.1 (0x00007ffcf774d000)
	libSM.so.6 =&gt; /lib/x86_64-linux-gnu/libSM.so.6 (0x00007f94986b5000)
	libICE.so.6 =&gt; /lib/x86_64-linux-gnu/libICE.so.6 (0x00007f9498698000)
	libXrender.so.1 =&gt; /lib/x86_64-linux-gnu/libXrender.so.1 (0x00007f949868b000)
	libXext.so.6 =&gt; /lib/x86_64-linux-gnu/libXext.so.6 (0x00007f9498676000)
	libX11.so.6 =&gt; /lib/x86_64-linux-gnu/libX11.so.6 (0x00007f9498536000)
	libz.so.1 =&gt; /lib/x86_64-linux-gnu/libz.so.1 (0x00007f9498518000)
	librt.so.1 =&gt; /lib/x86_64-linux-gnu/librt.so.1 (0x00007f9498513000)
	libpthread.so.0 =&gt; /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f949850e000)
	libdl.so.2 =&gt; /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f9498509000)
	libstdc++.so.6 =&gt; /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f94982dd000)
	libm.so.6 =&gt; /lib/x86_64-linux-gnu/libm.so.6 (0x00007f94981f6000)
	libgcc_s.so.1 =&gt; /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f94981d4000)
	libc.so.6 =&gt; /lib/x86_64-linux-gnu/libc.so.6 (0x00007f9497fab000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f94986cf000)
	libuuid.so.1 =&gt; /lib/x86_64-linux-gnu/libuuid.so.1 (0x00007f9497fa2000)
	libbsd.so.0 =&gt; /lib/x86_64-linux-gnu/libbsd.so.0 (0x00007f9497f8a000)
	libxcb.so.1 =&gt; /lib/x86_64-linux-gnu/libxcb.so.1 (0x00007f9497f60000)
	libmd.so.0 =&gt; /lib/x86_64-linux-gnu/libmd.so.0 (0x00007f9497f51000)
	libXau.so.6 =&gt; /lib/x86_64-linux-gnu/libXau.so.6 (0x00007f9497f4b000)
	libXdmcp.so.6 =&gt; /lib/x86_64-linux-gnu/libXdmcp.so.6 (0x00007f9497f43000)

</code></pre>
<p><em> → it seems to be fine</em></p>
<p>Any help would be highly appreciated. Please let me know if any additional information would be useful.</p>

---

## Post #2 by @mau_igna_06 (2024-07-16 14:45 UTC)

<p>What about trying this?</p>
<pre><code class="lang-auto">cd SlicerDirectory
XDG_SESSION_TYPE=wayland ./Slicer
</code></pre>
<p>Hope it helps</p>

---

## Post #3 by @dat-rohit (2024-07-17 00:45 UTC)

<p>Thank you for your reply. I tried your solution but ended up getting the same error message with the same behaviour.</p>
<pre><code class="lang-auto">XDG_SESSION_TYPE=wayland ./Slicer
qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ""
Error #1 while writing setting "Modules/AdditionalPaths"
Error #1 while writing setting "Modules/IgnoreModules"
Error #1 while writing setting "Extensions/ManagerEnabled"
Error #1 while writing setting "Extensions/ServerUrl"
Error #1 while writing setting "Extensions/FrontendServerUrl"
Error #1 while writing setting "Extensions/InstallPath"
Switch to module:  "Welcome"
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
QOpenGLWidget: Failed to create context
composeAndFlush: QOpenGLContext creation failed
composeAndFlush: makeCurrent() failed
composeAndFlush: makeCurrent() failed

</code></pre>
<p>Would you have any idea as to why this does happen?</p>
<p>Thank you in advance</p>

---

## Post #4 by @muratmaga (2024-07-17 04:51 UTC)

<p>In my experience 3D GUI applications like Slicer rarely work if you are using the traditional X window forwarding approach, which I believe is what you are doing.</p>
<p>Instead of trying to troubleshoot this, ask admins of the GPU cluster if it is possible to run VNC on the cluster and install the VirtualGL library (<a href="https://virtualgl.org/">https://virtualgl.org/</a>).</p>
<p>That way you can connect through VNC and use the rather solid VirtualGL (vgl) library to do remote rendering on the GPU (with the traditional X forwarding rendering is actually happening on your own computer’s X server and that’s probably where all that OpenGL errors are coming from).</p>
<p>If fully contained VNC is not possibility, you should be able to do X forwarding with ssh tunneling through virtualGL and still be able to do remote 3D rendering. See <a href="https://virtualgl.org/vgldoc/2_2_1/#hd007003">https://virtualgl.org/vgldoc/2_2_1/#hd007003</a></p>

---

## Post #5 by @dat-rohit (2024-07-18 01:41 UTC)

<p>Thank you a lot for your answer. I will probably go for this solution as my problem doesn’t seem to have any viable fix.</p>

---

## Post #6 by @muratmaga (2024-07-18 05:17 UTC)

<p>Your use case is why virtualGL is developed in the first place. if you can get the admins install and configure with EGL backend, you should be able to do what you need to do.</p>

---
