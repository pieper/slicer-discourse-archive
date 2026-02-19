---
topic_id: 37626
title: "How To Add And Edit Module"
date: 2024-07-30
url: https://discourse.slicer.org/t/37626
---

# How to add and edit module

**Topic ID**: 37626
**Date**: 2024-07-30
**URL**: https://discourse.slicer.org/t/how-to-add-and-edit-module/37626

---

## Post #1 by @Jessica_de_Kort (2024-07-30 20:17 UTC)

<p>Hi there. I added a custom module into Slicer but I don’t know how to edit it through Slicer. Do I have to redownload the module everytime?</p>

---

## Post #2 by @mikebind (2024-07-31 19:46 UTC)

<p>In the application settings, turn on Developer Mode <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#developer-mode" class="inline-onebox" rel="noopener nofollow ugc">Application settings — 3D Slicer documentation</a> and restart Slicer.  This will add a “Reload and Test” section to the top of modules, including yours.  If you click the “Edit” button in that section, it will load the .py file with your module code in it in an editor. If you modify the code and save it, then the “Reload” button will reload your module code and you can test the changes (no need to restart Slicer).</p>

---
