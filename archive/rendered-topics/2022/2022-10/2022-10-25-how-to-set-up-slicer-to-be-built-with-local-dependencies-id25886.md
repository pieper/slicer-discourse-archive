# How to set up Slicer to be built with local dependencies

**Topic ID**: 25886
**Date**: 2022-10-25
**URL**: https://discourse.slicer.org/t/how-to-set-up-slicer-to-be-built-with-local-dependencies/25886

---

## Post #1 by @miniminic (2022-10-25 06:00 UTC)

<p>When building, Slicer needs to download various dependencies like ctk,itk,vtk from links. If I download these dependencies locally beforehand and I want slicer to compile with local dependencies, how should I set them? thank you</p>

---

## Post #2 by @pieper (2022-10-25 12:27 UTC)

<p>It would be possible for you to search through the build system and set things up to point to local downloads of dependencies, but this would not be stable since they change fairly often and everything is set up to download on the fly.  It could help if you describe what problem you are trying to solve.</p>

---

## Post #3 by @miniminic (2022-10-25 12:46 UTC)

<p>Just like a normal vs project, I can package it and copy paste it on another computer without any configuration or downloading anything from the network, just double click to run the .sln file and build. I hope slicer will be able to completely migrate the whole project to another computer like this.</p>

---

## Post #4 by @jamesobutler (2022-10-25 13:14 UTC)

<p>Are you trying to avoid building Slicer on your 2nd developer computer? Or are you trying to distribute custom code to another person to try out?</p>

---

## Post #5 by @miniminic (2022-10-25 13:18 UTC)

<p>Yes I might be developing on a computer that is completely disconnected from the Internet. I can’t download slicer dependencies from the Internet. I’m trying to copy slicer to such a computer for development</p>

---

## Post #6 by @miniminic (2022-10-26 02:29 UTC)

<p>Where is this build system and how should I set them up to use local dependencies such as ctk, itk, vtk</p>

---

## Post #7 by @lassoan (2022-10-27 05:50 UTC)

<p>You can set local repository URLs when you configure your project in CMake, by using <code>Slicer_${proj}_GIT_REPOSITORY</code> variables. You can find the default URLs in <code>SuperBuild\External_....cmake</code> files.</p>

---

## Post #8 by @miniminic (2022-10-27 06:18 UTC)

<p>Ok, thank you very much.</p>

---
