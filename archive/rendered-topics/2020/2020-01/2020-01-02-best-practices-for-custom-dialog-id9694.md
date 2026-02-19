---
topic_id: 9694
title: "Best Practices For Custom Dialog"
date: 2020-01-02
url: https://discourse.slicer.org/t/9694
---

# Best practices for custom dialog

**Topic ID**: 9694
**Date**: 2020-01-02
**URL**: https://discourse.slicer.org/t/best-practices-for-custom-dialog/9694

---

## Post #1 by @Niels (2020-01-02 19:50 UTC)

<p>For my module I would like to create a popup window to enable the user to fill in some fields and run some algorithm when pressing [OK] afterwards. I was wondering what the best way forward would be. I am now using a qt.QDialog base class that only contains the widgets and implemented the logic in the loadable module that makes use of the dialog. Is there a better solution for this? Should I implement the logic in any other place? The reason I’m asking is because I expect to add more dialogs at a later stage and I want to do it right.</p>

---

## Post #2 by @lassoan (2020-01-02 21:11 UTC)

<p>In most workflows, popup windows are unnecessary and they are very annoying for the users. Instead of popups, you can follow standard Slicer style and use Qt designer to create your module GUI (<a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a>).</p>

---

## Post #3 by @Niels (2020-01-03 22:27 UTC)

<p>Hi Andras,<br>
Yes i am also not a popup fan. My module follows the bootcamp training guides and i only need a popup to display an QRcode and type some fields that i retrieve from the server after my logic posted some data. For this a popup containing the image seems right. Would you still not recommend using a custom dialog for this?</p>

---

## Post #4 by @lassoan (2020-01-04 02:49 UTC)

<p>You may display QR code in your module GUI or in a docking window to avoid interrupting the user’s workflow.</p>
<p>If you must use a modal popup then you can create a window using QDialog as base class. If you are implementing a C++ loadable module then it probably makes more sense to implement widgets in C++ as well. Do not implement any logic or algorithm in GUI classes, but instead always put them into logic classes (e.g., module logic class) so that they can be used without GUI and can be accessed from other modules.</p>

---
