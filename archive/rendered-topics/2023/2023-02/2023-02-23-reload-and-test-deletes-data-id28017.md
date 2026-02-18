# Reload and Test deletes data

**Topic ID**: 28017
**Date**: 2023-02-23
**URL**: https://discourse.slicer.org/t/reload-and-test-deletes-data/28017

---

## Post #1 by @rhodesdante (2023-02-23 16:24 UTC)

<p>Is there a way to recover data that is removed when one clicks on the “Reload and Test” button on some modules? I have accidentally pressed this button once or twice recently on different modules and it is frustrating to have my data wiped from the scene. Thanks!</p>

---

## Post #2 by @rhodesdante (2023-02-23 16:39 UTC)

<p>An example functionality that might be useful for preventing this might be an option in the application settings (next to “Confirm on Restart” checkbox, for example) that is enabled by default that ensures the user actually wants to reload and test, and warns that it will delete the scene’s data</p>

---

## Post #3 by @pieper (2023-02-23 18:32 UTC)

<p>The Reload and Test feature is exposed only in developer mode and is meant to quickly test new code from a fresh start.  If others agree, I would be okay a confirmation dialog before closing the scene.  It would be just a small change to the <code>ScriptedLoadableModuleWidget</code> base class.</p>

---

## Post #4 by @rhodesdante (2023-02-23 20:51 UTC)

<p>That would certainly help me prevent accidentally closing the scene–thanks!</p>

---

## Post #5 by @pieper (2023-02-23 21:02 UTC)

<p>Would you be able to draft a PR?</p>

---

## Post #6 by @rhodesdante (2023-02-23 21:27 UTC)

<p>I can certainly give it a try, but I have never done so before. Is there a tutorial for this I can follow?</p>

---

## Post #7 by @rhodesdante (2023-02-23 21:47 UTC)

<p>Nevermind, found it here: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html#how-to-submit-a-pr" class="inline-onebox" rel="noopener nofollow ugc">Contributing to Slicer — 3D Slicer documentation</a>. I’ll let you know if I am able to figure this out in a timely manner. Thanks again.</p>

---

## Post #8 by @pieper (2023-02-23 22:12 UTC)

<p>Yes, exactly.  You can search in the repository for the <code>onReloadAndTest</code> method and consider options to add a dialog (probably a <code>ctkMessageBox</code>).</p>

---
