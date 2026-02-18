# 3D Slicer customized application with display and GPU on different hosts

**Topic ID**: 24434
**Date**: 2022-07-21
**URL**: https://discourse.slicer.org/t/3d-slicer-customized-application-with-display-and-gpu-on-different-hosts/24434

---

## Post #1 by @Lee_Newberg (2022-07-21 17:19 UTC)

<p>Others have written a very nice lung-air app customization of 3D Slicer that makes use of a GPU.  I have a display-less Ubuntu 20.04 workstation with a good GPU and an Ubuntu 20.04 laptop with a display but a poor GPU.  I wish to have the computations done on the workstation, but have the interface showing up on my laptop display.  What’s the best practice for this for Ubuntu systems?</p>
<p>I have tried using an xterm on my laptop, ssh’ing to the workstation, and launching the application – and that does give me the display on my laptop via X11 forwarding, but the graphics are slow.  I’ve searched the web and found some postings about using a “software renderer” but that appears to be for Windows, not Ubuntu.  (Aside: I find those instructions to be confusing: which is the “renderer” computer, the one with the GPU or the one with the display, where I would follow the recommended steps?)</p>
<p>What’s the best practice for this?  Thanks!</p>

---

## Post #2 by @muratmaga (2022-07-21 17:32 UTC)

<p>This can be done quite readily (and freely) using VirtualGL and TurboVNC:</p>
<ol>
<li>On your headless (or displayless) Ubuntu 20.04  with GPU, you <a href="https://virtualgl.org/" rel="noopener nofollow ugc">will install VirtualGL</a> (this assumes you already have the GPU drivers installed on the Ubuntu host, if not you should start with that)</li>
<li>After install vgl, run /opt/VirtualGL/bin/vglserver_config, and follow the instructions.</li>
<li>
<a href="https://sourceforge.net/projects/turbovnc/files/" rel="noopener nofollow ugc">Install TurboVNC</a> on the same Ubuntu on host</li>
<li>Install TurboVNC on your laptop.</li>
</ol>
<p>Then open the TurboVNC client on your laptop and connect to your Ubuntu host as if you are using a ssh session (e.g., user@your.ubuntu.server). You would authenticate via the ssh password you normally use connecting to that host. After that you would see a unity desktop, and from there launch your Slicer application via command <code>vglrun</code>. So if your slicer path is something like $HOME/Downloads/Slicer/Slicer, you would do<br>
<code>vglrun $HOME/Downloads/Slicer/Slicer</code></p>

---

## Post #3 by @pieper (2022-07-21 17:34 UTC)

<p>Hi <a class="mention" href="/u/lee_newberg">@Lee_Newberg</a> -</p>
<p>I have good luck with x11vnc/noVNC and then tunneling the vnc connection through ssh.<br>
It’s the method <a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop">describe here</a>.  The scripts to configure a vanilla ubuntu machine are <a href="https://github.com/pieper/SlicerMachines/tree/main/scripts">here</a>.</p>

---

## Post #4 by @lassoan (2022-07-21 17:55 UTC)

<p>If your GPU computer needs to serve multiple users or you want to maximize the responsiveness of the GUI then you may consider running Slicer locally (on your laptop) and setting up a MONAILabel server (or some generic Python REST API server using <a href="https://rapidapi.com/blog/best-python-api-frameworks/">FastAPI, Flask, etc.</a>) to perform the tasks that require GPU.</p>

---
