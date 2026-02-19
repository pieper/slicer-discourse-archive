---
topic_id: 6269
title: "Update Slicer While Keeping Extensions And Custom Modules"
date: 2019-03-25
url: https://discourse.slicer.org/t/6269
---

# Update Slicer while keeping extensions and custom modules

**Topic ID**: 6269
**Date**: 2019-03-25
**URL**: https://discourse.slicer.org/t/update-slicer-while-keeping-extensions-and-custom-modules/6269

---

## Post #1 by @Prashant_Pandey (2019-03-25 01:56 UTC)

<p>OS: Windows 10</p>
<p>I’m using Slicer 4.8 with a number of published extensions (SlicerElastix, slicerIGT, etc.), and custom python modules and MatlabBridge modules. Every time I update to a more recent Slicer version I have to re-install and reconfigure all of those extensions and modules manually, is there a more automatic way to copy over extensions and modules to a new Slicer install? Thanks</p>

---

## Post #2 by @lassoan (2019-03-25 03:06 UTC)

<p>Yes, in the Extension Manager’s “Restore Extensions” tab you can choose to reinstall all or selected previously installed extensions. I’m not sure if it can go back as far as Slicer-4.8, but it is definitely available in Slicer-4.10 and later.</p>
<p>Usually stable versions are only released 1-2x per year, so reinstalling extensions even manually does not seem a lot of work.</p>
<p>Maybe you didn’t know that you can drag-and-drop folders (even multiple at once) into the folder list in Application Settings window’s Modules’s section. That should take care of setting all your the custom module paths.</p>
<p>You can also compile all your custom modules to a few extensions and install them from file (toolbox icon in extension manager).</p>
<p>You can also set paths from Python or edit Slicer-NNN.ini files in a text editor.</p>
<p>You may also create an custom Slicer package that bundles all necessary extensions. You may either build the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="nofollow noopener">custom Slicer</a> or use <a href="https://www.slicer.org/wiki/Documentation/Labs/CustomSlicerGenerator" rel="nofollow noopener">CustomSlicerGenerator</a> to build one from an installed version.</p>
<p>There are even more options, but I think the ones listed above should cover most use cases.</p>

---
