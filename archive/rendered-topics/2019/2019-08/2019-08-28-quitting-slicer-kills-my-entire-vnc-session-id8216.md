# Quitting Slicer kills my entire VNC session

**Topic ID**: 8216
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/quitting-slicer-kills-my-entire-vnc-session/8216

---

## Post #1 by @hbraunDSP (2019-08-28 20:26 UTC)

<p>I’m having a problem where closing slicer causes the entire VNC session in which it’s running to quit.</p>
<p>My setup:</p>
<ul>
<li>I’m on Computer 1 (Windows 10)</li>
<li>My vnc session is on Computer 2 (RHEL 5.11)</li>
<li>From Computer 2, I <code>ssh</code> to Computer 3 (RHEL 7.6) and launch Slicer (version 4.8.1).</li>
<li>I am not an administrator on Computer 2 or 3, so I can’t easily upgrade Slicer. I’ll hopefully be switching to running it in a container soon though, so that could change.</li>
</ul>
<p>The problem behavior:</p>
<ul>
<li>If a non-trivial scene is present, closing Slicer (by clicking the “x” button or typing quit() in the python interactor) crashes the VNC session</li>
<li>killing the SlicerApp-Real process from the terminal does not crash the VNC session. This is how I’ve been working around it.</li>
<li>VNC leaves the lock file <code>/tmp/.X??-lock</code> intact, which indicates to me that it’s exiting abnormally without cleaning up after itself.</li>
<li>Doing this with only a blank scene does not cause VNC to quit.</li>
</ul>
<p>Is there any way I can stop this? Thanks!</p>

---

## Post #2 by @pieper (2019-08-28 20:54 UTC)

<p>Must be something in the shutdown process, perhaps OpenGL.  Could be something in Slicer, VNC, or X so it’s likely hard to debug or fix.</p>
<p>A few ideas:</p>
<ul>
<li>Slicer doesn’t need admin rights to install, so just unpackage the distribution archive and run from there.</li>
<li>The latest release and nightly builds have different OpenGL back ends than 4.8.1 so behavior might be different.</li>
<li>Manually killing <code>SlicerApp-real</code> sounds like an okay workaround if all else fails…</li>
</ul>

---

## Post #3 by @hbraunDSP (2019-08-29 14:58 UTC)

<p>Thanks. I’ll try a newer version of Slicer ASAP and hope it fixes things. I’m <em>really</em> hoping to fix this because I want to run some automatic batch processing from the command line, and I’d much rather just have Slicer quit when finished than have to verify it’s finished from the outside, then find and kill the correct process.</p>

---

## Post #4 by @pieper (2019-08-29 15:20 UTC)

<p>Agreed, it’s best if the new versions fix the problem.  As a patch/workaround you could call the system kill command from within your processing script to avoid whatever shutdown steps lead to the crash.</p>

---

## Post #5 by @hbraunDSP (2019-08-29 16:14 UTC)

<p>Yeah, I thought of that shortly after I posted…it’s ugly but it would work. Thanks!</p>

---
