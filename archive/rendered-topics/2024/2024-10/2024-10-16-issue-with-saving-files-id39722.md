# Issue with Saving Files

**Topic ID**: 39722
**Date**: 2024-10-16
**URL**: https://discourse.slicer.org/t/issue-with-saving-files/39722

---

## Post #1 by @Marta_Fernandez (2024-10-16 11:36 UTC)

<p>I’m experiencing a strange issue with 3D Slicer 5.7 version. When I save a file in the program’s format to continue working later, the following happens: If I save the file on the desktop, it reopens exactly as I left it. However, if I save it in any other folder and then try to open it again, the file appears empty.</p>

---

## Post #2 by @pieper (2024-10-16 12:26 UTC)

<p>Is this windows?  Maybe it’s some onedrive issue.</p>

---

## Post #3 by @Marta_Fernandez (2024-10-16 12:35 UTC)

<p>Yes, I am using Windows. I am saving files in a folder on the desktop. The problem occurs when I save them in the folder instead of directly on the desktop.</p>

---

## Post #4 by @pieper (2024-10-16 12:38 UTC)

<p>I don’t use windows myself but lots of people do so let’s see if anyone else has seen this behavior.  You might want to describe more about your computer, like is it an institutional machine controlled by some admin, an new or old machine, what windows version, etc.</p>

---

## Post #5 by @Marta_Fernandez (2024-10-16 13:53 UTC)

<p>My computer has the latest version of Windows. It is a new personal computer with a Core i9 and an Nvidia graphics card. Thanks for your help.</p>

---

## Post #6 by @lassoan (2024-10-17 03:15 UTC)

<aside class="quote no-group" data-username="Marta_Fernandez" data-post="1" data-topic="39722">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marta_fernandez/48/10323_2.png" class="avatar"> Marta_Fernandez:</div>
<blockquote>
<p>However, if I save it in any other folder and then try to open it again, the file appears empty.</p>
</blockquote>
</aside>
<p>The .mrml file contains some data, but all the bulk data (images, segmentations, models, markup, etc.) are stored in additional files.</p>
<p>When you save as .mrml format in a new location, make sure you save all the files that are selected for saving by default.</p>
<p>If you want to save all data in a single file then you can save the scene in .mrb file format (by clicking the “package” icon).</p>
<p>If you find that saving still does not work as you expect then please save and load the scene, get the application log (menu: Help / Report a bug), and copy it here. If you work with real patient data then make sure to remove any patient information, e.g., in filenames.</p>

---
