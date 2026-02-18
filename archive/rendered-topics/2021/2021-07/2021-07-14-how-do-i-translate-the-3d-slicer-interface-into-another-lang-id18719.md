# How do I translate the 3D Slicer interface into another language?

**Topic ID**: 18719
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/how-do-i-translate-the-3d-slicer-interface-into-another-language/18719

---

## Post #1 by @Viacheslav (2021-07-14 04:08 UTC)

<p>Hi all, I enabled Slicer_BUILD_I18N_SUPPORT support in CMake, the .ts and .qm files for the desired language were created after compiling the solution and the language selection appeared in the UI. Using Qt Linguist, I translated the resulting qSlicerBaseQTGUI_ru.ts file. After recompiling the solution and selecting the language you want, nothing changed, the entire interface is still in English. What am I doing wrong?</p>

---

## Post #2 by @pieper (2021-07-14 15:30 UTC)

<p>I’m afraid the internationalization features are still a work-in-progress and maybe haven’t been tried with the latest versions of Slicer and Qt.  You can probably make it work with more effort.  But the full interface is not yet ready to translate (we need more tr macros in the code and other things).  We hope to be funded for this at some point but don’t know yet.</p>

---

## Post #3 by @Viacheslav (2021-07-14 16:55 UTC)

<p>I have little experience with Qt. Can you explain in more detail, do I need to supplement the source code of the program for the translation to work or described my actions should be enough for at least a partial translation of the interface?</p>

---

## Post #4 by @pieper (2021-07-14 16:59 UTC)

<p>What I mean to say is that it’s not a solved problem yet in the context of Slicer so there are no ste-by-stop instructions beyond what you have found so far.  I believe it is a solvable problem but currently the implementation is incomplete and won’t completely work unless we get some dedicated funding or volunteer effort.</p>

---
