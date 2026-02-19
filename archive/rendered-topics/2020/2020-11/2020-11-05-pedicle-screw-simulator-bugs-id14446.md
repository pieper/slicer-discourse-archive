---
topic_id: 14446
title: "Pedicle Screw Simulator Bugs"
date: 2020-11-05
url: https://discourse.slicer.org/t/14446
---

# Pedicle Screw Simulator bugs

**Topic ID**: 14446
**Date**: 2020-11-05
**URL**: https://discourse.slicer.org/t/pedicle-screw-simulator-bugs/14446

---

## Post #1 by @mau_igna_06 (2020-11-05 14:52 UTC)

<p>Hi. I found some bugs on the PedicleScrewSimulator extension. The ones I’d like to be solved the most are number 6 and 7 because they affect funcionality, the other ones refer to the GUI</p>
<p>1- In step “5. Place Screws”: load screw-length of 550 and screw-width of 35 and it does nothing and gives an error on the python console<br>
2- Also in step 5: length and width should be divided by ten because it’s 55mm not 550mm<br>
3- Also in step 5: if you press “Insert Screw”/“Reset screw” with no screw loaded it gives an error on the python console; it should do nothing or that the buttons be not enabled until a screw is loaded.<br>
4- Also in step 5: “Load Screw” becomes enabled after selecting “Screw Length” and it should wait until “Screw Width” is also selected<br>
5- Also in step 5: sliders are enabled before screw is loaded and they shouldn’t. If you move the slider (with no screw loaded) it gives a python console error.<br>
6- Also in step 5: load a screw, insert the screw, change “Insertion Site” and the screw position gets reseted. It should stay the same.<br>
7- Also in step 5: load a screw, after that move one slider then change “Insertion Site”. Problem: Slider keeps on the same place after the change on insertion site, it should update to the last slider value selected for this “Insertion Site”. Temporal record of the slider positions for “Insertion Sites” should be done.<br>
8- In step “3. Identify Insertion Landmarks”: level doesn’t appear after 3 or more fiducials are placed (I don’t know if this is an error)</p>

---

## Post #2 by @lassoan (2020-11-05 16:13 UTC)

<p>Thanks for reporting these. I don’t think anybody is funded right now to work on this module, but you can easily fix all these issues. It is just a Python scripted module, so you can go and edit the code to change the behavior any way you want. If you send a pull request with the suggested changes then I can make sure those fixes are tested and integrated into the module.</p>

---

## Post #3 by @mau_igna_06 (2020-11-05 18:17 UTC)

<p>Thank you for the reply Andras. I tried to make the pull request but I couldn’t, I’ll try to fix the code anyway.</p>

---
