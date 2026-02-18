# 1. Working directory, 2. Recording rotating 3D-reconstructions

**Topic ID**: 22418
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/1-working-directory-2-recording-rotating-3d-reconstructions/22418

---

## Post #1 by @Kim_Geboers (2022-03-09 19:41 UTC)

<p>Hi everyone,<br>
I have been using Slicer for a while and bought a new laptop, so I installed Slicer and We-transferred my data from my old laptop. The problem is, when I open the .mrml file, it is blank. When I add a working trajectory it loads all the data perfectly, but when I close Slicer and reopen the .mrml file, it opens blank again. So somewhere, the working directory gets lost or isn’t properly saved or something like that… Am I missing a step or what am I doing wrong?</p>
<p>A second question is regarding the recording of rotation 3D-reconstructions. I’ve read that I can use the Screen capture module. However, I have no clue where to find this module. I’ve also tried using the Sequence Browser to record, but I haven’t succeeded yet. I am not so good with all this technical stuff. The purpose is to record rotating 3D-reconstructed skulls of 1 patient, this is a comparison between the first and latest scan. The goal is to present this in a Powerpoint presentation, so optimally, both recordings need to play at the same time.<br>
I hope this can be achieved quite easily <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<p>Thank you for reading my message!<br>
Kim</p>

---

## Post #2 by @pieper (2022-03-09 20:04 UTC)

<p>The mrml file only stores a text description (xml) of the state of the scene but the bulk data is stored in independent files (volumes, model files, etc).  So you need to save all the files in the same relative locations in the new machine.  Or you can resave on the old machine as an MRB file (a bundle) using the package icon in the save dialog and that’s easier to move from machine to machine.</p>
<p>The screen capture module is a built-in module.  Just use the module search button (magnifying glass on the toolbar).</p>

---

## Post #3 by @Kim_Geboers (2022-03-09 20:22 UTC)

<p>Thank you for your quick reply!<br>
I copied all I had, not just the .mrml files. So I added a working directory to the map where I saved all the data. These data are grouped per case/patient and each case contains all of the files, that is nrrd, acsv, vp etc.<br>
To adapt data, in this case, skulls, I’ve always opened the .mrml file, made changes, saved it and every time I could reopen the .mrml file without being blank.<br>
When I save this as an MRB file, does this have any consequences, e.g. for extracting individual data at a later time?<br>
Found the screen capture module, thanks!!</p>

---

## Post #4 by @pieper (2022-03-09 20:31 UTC)

<p>If you use mrml then you need to make sure the relative paths between the .mrml file and the files it references are the same on both machines.  If you use .mrb you can just move each file around.  The .mrb file is just a .zip file with a different extension, so if you need to access the contents you can either use Slicer or you can rename the file with a .zip extension and use any zip tool.</p>

---
