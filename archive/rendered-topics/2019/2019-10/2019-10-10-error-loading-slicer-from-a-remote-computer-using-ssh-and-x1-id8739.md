# Error loading slicer from a remote computer using ssh and X11 forwarding

**Topic ID**: 8739
**Date**: 2019-10-10
**URL**: https://discourse.slicer.org/t/error-loading-slicer-from-a-remote-computer-using-ssh-and-x11-forwarding/8739

---

## Post #1 by @Keyur_Shah (2019-10-10 23:13 UTC)

<p>I am a new MacOS user. I have a problem when I ssh into a remote computer using X11 forwarding. I am trying to view 3D Slicer from my remote computer. 3D Slicer loads correctly, but I am unable to visualize anything. However, if I hover the mouse I can see the menu options. But I am unable to see any data that I load. On the terminal, I see QOpenGLWidget: Failed to create context and composeAndFlush: QOpenGLContext creation failed composeAndFlush: makeCurrent() failed.</p>
<p>I tried updating my MacOS in the hope that the driver would also update. But that did not help either.</p>
<p>I am using a Mac mini (Late 2014), macOS Catalina with a 2.6 GHz Dual-Core Intel Core i5 processor and Intel Iris Graphics.</p>
<p>The problem is on the Mac, since Slicer loads when I ssh into the remote computer using my Ubuntu laptop.</p>
<p>Thanks in advance for your help.</p>
<p>Operating system: macOS Catalina<br>
Slicer version: 4.10/4.11<br>
Expected behavior: Slicer loads correctly<br>
Actual behavior: Slicer doesn’t load correctly</p>

---

## Post #2 by @muratmaga (2019-10-11 04:14 UTC)

<p>it sounds like your X11 server on the local machine doesn’t have opengl support. I am not entirely sure about mac, but in our lab we use VirtualGL (<a href="https://virtualgl.org/vgldoc/2_2_1/" rel="nofollow noopener">https://virtualgl.org/vgldoc/2_2_1/</a>) on the remote machine and connect to it from our desktop machines either using VNC (on windows/linux) or vglconnect (linux). That way opengl rendering is done on the remote machine. For us it works really well (a 1080TI easily supports 5-6 concurrent connections, all of which doing 3D rendering at reasonably large datasets 1-2 gigavoxels).</p>
<p>There are other alternatives that other may chime in.</p>

---

## Post #3 by @pieper (2019-10-11 17:42 UTC)

<p>The instructions are a bit rough, and geared toward doing the work on the cloud, but <a href="https://github.com/QIICR/SlicerGCPSetup" rel="nofollow noopener">this approach</a> is another way of using the remote GPU with Slicer.</p>

---
