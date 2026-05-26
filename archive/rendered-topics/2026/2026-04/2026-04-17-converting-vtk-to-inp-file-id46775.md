---
topic_id: 46775
title: "Converting .vtk to .inp file"
date: 2026-04-17
url: https://discourse.slicer.org/t/46775
last_bumped: 2026-04-18T17:48:54.843Z
---

# Converting .vtk to .inp file

**Topic ID**: 46775
**Date**: 2026-04-17
**URL**: https://discourse.slicer.org/t/converting-vtk-to-inp-file/46775

---

## Post #1 by @Tom_F-T (2026-04-17 23:22 UTC)

<p>I am trying to make a 3D model of trabecular bone for FEA in Abaqus. I am using slicer to convert the DICOM files of the bone into a 3D model, but when i first did this the .stl file i exported from slicer was only a surface mesh and as such I couldnt assign a section to it in order to apply the material to it, and it said i needed a volumetric mesh. from research, and AI, I found that downloading my model from slicer as a .vtk file was the best idea. The issue is that Abaqus cannot open .vtk files and again from research it seems the best conversion would be to a .inp file. From these forums Ive seen that people have used the meshio package in order to do this but for some reason I am running into a wall with the conversion, presumably from what i’m writing in the python console. The most common issue I get is that it doesn’t recognise my vtk file as a vtk.<br>
Any help with this would be great, I’m pretty new at this so sorry if I am making any stupid mistakes. Thanks</p>

---

## Post #2 by @lassoan (2026-04-18 00:26 UTC)

<aside class="quote no-group" data-username="Tom_F-T" data-post="1" data-topic="46775">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tom_f-t/48/81964_2.png" class="avatar"> Tom_F-T:</div>
<blockquote>
<p>.stl file i exported from slicer was only a surface mesh</p>
</blockquote>
</aside>
<p>STL file can only store a surface mesh. For finite-element analysis you probably want to create a volumetric mesh.</p>
<p>You can use the <code>SegmentMesher</code> extension in 3D Slicer to create a volumetric mesh from a segmentation. Alternatively, you can export a surface mesh from Slicer and use fTetWild, TetGen, NetGen - or any of the hundreds of mesh generators - to create the volumetric mesh. Each mesher has different capabilities and limitations, so it is not trivial to find one that fulfills all your needs, but there are many options.</p>

---

## Post #3 by @Tom_F-T (2026-04-18 11:30 UTC)

<p>Thanks for the response, for the segmentmesher extension, can I use my STL file to create the segment to thus make the volumetric mesh or does it have to be a certain type of file?</p>

---

## Post #4 by @lassoan (2026-04-18 11:41 UTC)

<p>Your can import your STL file into a segmentation as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file">here</a>.</p>

---

## Post #5 by @Tom_F-T (2026-04-18 11:57 UTC)

<p>I manage to import the stl file as a segmentation, but for some reason everytime i try to use the segment mesher module my slicer crashes. I’ve done it with both tetgen and cleaver. would it be because i need to reduce the refinement of my mesh and make it coarser?</p>

---

## Post #6 by @lassoan (2026-04-18 12:27 UTC)

<p>Yes, start with coarser mesh and watch your RAM usage. You may need to configure more virtual memory in your system if you want to get very detailed mesh (but probably you want to avoid that, as it would harm your simulations, too).</p>

---

## Post #7 by @Tom_F-T (2026-04-18 13:24 UTC)

<p>Hi, Ive tried going back to using meshio in the python console, as I am still having issues with the app crashing when using segment mesher. i made the .vtk file by loading my dicom files and then saving that as a .vtk file, made sure to uncheck the compress, and when i load it again in slicer and go to use it to convert it still comes up with the error that it doesnt read it as a vtk.</p>
<p>&gt;&gt;&gt; import meshio</p>
<p>&gt;&gt;&gt; mesh = meshio.read(r"C:\Users\tomyf\OneDrive - Loughborough University\Desktop\Engineering\year 3\Indiviual Project\Specimen1_VOI4_Scan1.vtk")</p>
<p>Error: Couldn’t read file C:\Users\tomyf\OneDrive - Loughborough</p>
<p>University\Desktop\Engineering\year 3\Indiviual</p>
<p>Project\Specimen1_VOI4_Scan1.vtk as vtk</p>

---

## Post #8 by @Tom_F-T (2026-04-18 16:00 UTC)

<p>Hi there, I’ve managed to create the .inp file so no need to respond anymore. Thank you very much Mr. Lasso for your help and input, you’ve saved my project!</p>
<p>For those who find themselves in a similar situation, here are some pointers:<br>
First, AI can be helpful in this area, but it definitely trips up on itself and you can get lost in the problems and you don’t know what the original problem was. also, grok seemed to be the best for me, even though i had chatgpt+, it seemed to not know the stuff as good as grok.<br>
When saving your file as a .vtk file, make sure to uncheck the “Compress” box to make sure it saves as a volume.<br>
Also, when you use the SegmentMesher module, if you are on your laptop like I am there are two approaches you can make:<br>
you can either make the mesh really coarse using the Advanced dropdown (it’s described there), and then load it but for me it just made a structure which didnt resemble the desired model at all.<br>
Or you can increase the virtual memory of your laptop, which is what i did. This basically gives you more RAM using the disk of your laptop, therefore the app can run a more difficult process, just search how to do it. When choosing what to put as your Initial/Maximum, I tried the 1.5x/3x rule the internet tells you but that didn’t do anything so I ended up putting 30MB/70MB with a 16GB RAM, which eventually worked. However, you have to be ready for your laptop to crash a couple times, so you’ll have to tweak with the coarseness of the mesh as well but basically you just have to give the app time to load, even if it says (Not Responding), just wait until it either loads or crashes the entire laptop, and then start again (so make sure to save all your files before doing this!). Also make sure to reset it once done because it affects all your other processes and slows your computer down a bunch.</p>
<p>From here, use the meshio in the python console to convert it to an .inp file which will instantly save it to wherever you tell it to. Here’s the code I wrote exactly to copy into the console:</p>
<pre><code class="lang-auto">import meshio
mesh = meshio.read(r"C:\\path\\to\\file.vtk")
meshio.write(r"C:\\path\\to\\file.inp")
</code></pre>
<p>I don’t know if I’ll be able to respond to any questions but please put any replies if you want, probably to Mr.Lasso instead as he’s the expert.<br>
Good Luck and hope this is helpful <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2026-04-18 17:48 UTC)

<p>Thanks for sharing your experience, this is very useful.</p>
<p>Just a small explanation for this:</p>
<blockquote>
<p>make sure to uncheck the “Compress” box to make sure it saves as a volume.</p>
</blockquote>
<p>Compression does not affect what is saved, only how it is saved. Compression makes the file smaller, but some simpler VTK reader implementations can only read the uncompressed format.</p>

---
