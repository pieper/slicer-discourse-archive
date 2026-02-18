# App crashing on windows server

**Topic ID**: 2659
**Date**: 2018-04-23
**URL**: https://discourse.slicer.org/t/app-crashing-on-windows-server/2659

---

## Post #1 by @anandmulay3 (2018-04-23 08:32 UTC)

<p>OS : windows server 2016 standard<br>
app is not working on this windows 10 (windows server 2016) version.<br>
Does it have any issue for this OS support.</p>

---

## Post #2 by @anandmulay3 (2018-04-23 13:12 UTC)

<p>its a virtual machine( currently giving a try on windows 10 pro), and i have tested slicer 4.8.1 which is working but latest 4.9 version crashes while normal loading,</p>

---

## Post #3 by @lassoan (2018-04-23 13:25 UTC)

<p>Recent nightly version of Slicer require OpenGL 3.2 (released about 10 years ago). This allows magnitude better performance on most current computers, but it means that it may not be compatible with systems with severely limited OpenGL capability. For example, standard remote desktop protocol is not sufficient, so you need to set up RemoteFX.</p>

---
