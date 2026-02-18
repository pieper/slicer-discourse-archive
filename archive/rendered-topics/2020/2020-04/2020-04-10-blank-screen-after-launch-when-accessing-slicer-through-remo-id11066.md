# Blank Screen after launch when accessing Slicer through remote desktop

**Topic ID**: 11066
**Date**: 2020-04-10
**URL**: https://discourse.slicer.org/t/blank-screen-after-launch-when-accessing-slicer-through-remote-desktop/11066

---

## Post #1 by @APern (2020-04-10 02:37 UTC)

<p>I’m experiencing difficulty with running 3D Slicer. The program launches but the Slicer window is completely blank, as seen in the attached picture. This has been a consistent and repeatable error without any useful error message from the program. Could you please let me know if you have any thoughts on how to troubleshoot and resolve this issue?</p>
<p>I am running a Windows 10 computer on the university network. Is it possible I’m missing a Windows file the program depends on? I have tried uninstalling and reinstalling and checking compatibility settings.</p>
<p>Also, could using the program through remote access be complicating the way it runs? We’ve done some preliminary trouble-shooting along this line of thinking. Initially, I assumed this was an issue with the remote-access software but my research colleague is able to remotely access and successfully use Slicer.  We have the same user permissions and are using the same remote access software.</p>
<p>Thank you for the help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa5aaeaac4ce541d6e530324e0574bdac3935b71.jpeg" data-download-href="/uploads/short-url/oj1sgsc45Bybive9x4ByA5rQcZb.jpeg?dl=1" title="Slicer_Blank_Window" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa5aaeaac4ce541d6e530324e0574bdac3935b71_2_375x500.jpeg" alt="Slicer_Blank_Window" data-base62-sha1="oj1sgsc45Bybive9x4ByA5rQcZb" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa5aaeaac4ce541d6e530324e0574bdac3935b71_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa5aaeaac4ce541d6e530324e0574bdac3935b71_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa5aaeaac4ce541d6e530324e0574bdac3935b71_2_750x1000.jpeg 2x" data-dominant-color="A1A29F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_Blank_Window</span><span class="informations">3024×4032 2.22 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-04-10 02:50 UTC)

<p>Remote desktop client, server, and graphics card driver must all support the minimum required OpenGL version.</p>
<p>Until recently, Windows remote desktop’s OpenGL support was insufficient, but recently it got upgraded, so Slicer runs fine via Windows RDP. VNC and TeamViewer known to work well, so it is surprising that it seems to struggle on your computer.</p>
<p>You can try these:</p>
<ul>
<li>upgrade your graphics card and TeamViewer versions</li>
<li>check if there are any 3D acceleration settings in TeamViewer that you can change</li>
<li>launch Slicer (locally) before connecting to the computer from a remote computer</li>
<li>change OpenGL profile settings by setting <code>SLICER_OPENGL_PROFILE</code> environment variable <code>no</code>, <code>core</code> or <code>compatibility</code>
</li>
<li>use a different graphics card</li>
<li>use a different remote desktop software (RealVNC, TightVNC, Chrome Remote Desktop, etc.)</li>
<li>use a software renderer, such as Mesa (see details <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">here</a>)</li>
</ul>

---

## Post #3 by @Arghya_pal (2022-02-24 16:05 UTC)

<p>Not sure whether you still need it or not - but I am posting it for the community.<br>
If someone sees the same problem the following line can be tried:</p>
<p>MESA_GL_VERSION_OVERRIDE=3.2 MESA_GLSL_VERSION_OVERRIDE=150 ./Slicer</p>

---

## Post #4 by @lassoan (2022-02-25 15:13 UTC)

<p><a class="mention" href="/u/arghya_pal">@Arghya_pal</a> What operating system did you use? Have you set up Mesa as OpenGL renderer?</p>

---

## Post #5 by @mameco (2023-03-01 11:20 UTC)

<p>Hi experts,<br>
I have roughly the same problem (see attached image). My IT installed 3D-Slicer 5.2.1 on my virtual PC a couple of weeks ago; I use RDP</p>
<p>Any help is appreciated, Thanks in advance!</p>
<p>Martin Metzger</p>
<p>System config:<br>
Device: Intel(R) Xeon(R) CPU E5-2660 v4 <span class="mention">@2.00GHz</span> 2.00GHz<br>
RAM: 16,0 GB<br>
64-bit OS, x64-based Processor<br>
OS: Windows 10 Enterprise<br>
Version: 22H2<br>
Built: 19045.2364<br>
Windows feature Experience Pack 120.2212.4190.0</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f51eb5edc5c3282785f417da721197a7efeebcc.png" data-download-href="/uploads/short-url/mJpqCo1xjNPzbgc7rDHQ0Txsf5a.png?dl=1" title="2023-03-01_BlankScreenAfterLaunch" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f51eb5edc5c3282785f417da721197a7efeebcc_2_690x446.png" alt="2023-03-01_BlankScreenAfterLaunch" data-base62-sha1="mJpqCo1xjNPzbgc7rDHQ0Txsf5a" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f51eb5edc5c3282785f417da721197a7efeebcc_2_690x446.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f51eb5edc5c3282785f417da721197a7efeebcc_2_1035x669.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f51eb5edc5c3282785f417da721197a7efeebcc.png 2x" data-dominant-color="FBFBFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-03-01_BlankScreenAfterLaunch</span><span class="informations">1172×758 30.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2023-03-02 06:18 UTC)

<p>Windows RDP requires careful configuration to allow hardware graphics acceleration. Your IT support people should be able to set everything up for you (see how it is done for example in <a href="https://learn.microsoft.com/en-us/azure/virtual-desktop/configure-vm-gpu">Azure</a>).</p>
<p>If they have trouble setting this up then you can <a href="https://slicer.readthedocs.io/en/latest/user_guide/get_help.html#slicer-application-does-not-start">switch to a software renderer</a>. This is simple and you can still use RDP but it will slow down the rendering.</p>
<p>You may also use a different remote desktop solution. Most remote desktop software (VNC, TeamViewer, Chrome remote desktop, etc.) uses full graphics capabilities of the host system, so if you switch to any of those then everything will work.</p>

---

## Post #7 by @mameco (2023-03-02 12:17 UTC)

<p>Hi, Andras Lasso,</p>
<p>Thank you for your quick answer.</p>
<p>Martin Metzger</p>

---
