---
topic_id: 309
title: "Virtual Fragment Reconstruction Extension Help"
date: 2017-05-14
url: https://discourse.slicer.org/t/309
---

# Virtual Fragment Reconstruction Extension Help

**Topic ID**: 309
**Date**: 2017-05-14
**URL**: https://discourse.slicer.org/t/virtual-fragment-reconstruction-extension-help/309

---

## Post #1 by @Cardinals_16 (2017-05-14 11:15 UTC)

<p>Has anyone attempted to use the virtual fragment reconstruction extension described here:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.6/Extensions/VirtualFractureReconstruction" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.6/Extensions/VirtualFractureReconstruction</a></p>
<p>I can’t find any way to actually install the extension through the slicer interface or through the developer files that they’ve included. I’m fairly new to slicer to any help would be appreciated. Thanks!</p>

---

## Post #2 by @pieper (2017-05-14 15:09 UTC)

<p>The source code is available, but it’s for an older version of Slicer so it would need to be updated a bit.  I suspect it could be made to work if you have the time and are willing to learn about the build process.</p>

---

## Post #3 by @lassoan (2017-05-15 13:23 UTC)

<p>I’ve fixed the build errors (all trivial modifications due to VTK, ITK, and Slicer API updates). You can get the update version from <a href="https://github.com/lassoan/VirtualFractureReconstructionSlicerExtension">my forked repository</a>. I’ve also sent a <a href="https://github.com/kfritscher/VirtualFractureReconstructionSlicerExtension/pull/2">pull request</a> to the author to update the original repository.</p>
<p>If you build it and add the binary directories to the additional module paths, then modules should show up in the “Developer tools” and “Work in progress” categories. I haven’t tested the modules at all. If you find the modules useful then let me know and then I add the extension to the extension manager.</p>

---

## Post #4 by @Cardinals_16 (2017-05-15 14:24 UTC)

<p>Thank you for your help!! I’ll let you know if/when I get it working.</p>

---

## Post #5 by @Aube (2017-06-14 08:16 UTC)

<p>Dear Developers,</p>
<p>I’m working on a tibial plateau fracture, and i’m interested in the description of your extension <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/VirtualFractureReconstruction" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/VirtualFractureReconstruction</a>).</p>
<p>Even with the updated files( <a href="https://github.com/lassoan/VirtualFractureReconstructionSlicerExtension" rel="nofollow noopener">https://github.com/lassoan/VirtualFractureReconstructionSlicerExtension</a>), I didn’t find the way to install and use the extension. I’m working with 3D Slicer 4.6.2 on Windows 10 64bit.</p>
<p>I tried to build it with Cmake by calling the CMakelLists.txt in the master file, but the building finds errors. Actually, I don’t really know how to do it properly.</p>
<p>Any help would be very appreciated.</p>
<p>Thank you !</p>
<p>Aube (FR)</p>

---

## Post #6 by @pieper (2017-06-14 12:52 UTC)

<p>Hi Aube -</p>
<p>To build the extension you need to build your own Slicer locally - did you do that?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a></p>
<p>Best,<br>
-Steve</p>

---

## Post #7 by @lassoan (2017-06-15 03:36 UTC)

<p>I’ve added this extension to the extension index. It should be available in the Extension manager in the nightly version of Slicer that you download Friday or later.</p>

---

## Post #8 by @Aube (2017-06-16 15:25 UTC)

<p>Hi,</p>
<p>Pieper, Thank you for your answering !. It would be help full if I’ll need to install the extension on the stable 3D Slicer version.</p>
<p>Lassoan, I just found and install the extension on the nightly Slicer version. Thank you a lot !</p>
<p>Best regards,</p>
<p>Aube</p>

---
