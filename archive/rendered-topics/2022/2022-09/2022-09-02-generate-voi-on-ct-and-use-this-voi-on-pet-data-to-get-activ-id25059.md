---
topic_id: 25059
title: "Generate Voi On Ct And Use This Voi On Pet Data To Get Activ"
date: 2022-09-02
url: https://discourse.slicer.org/t/25059
---

# Generate VOI on CT and use this VOI on PET data to get activity information

**Topic ID**: 25059
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/generate-voi-on-ct-and-use-this-voi-on-pet-data-to-get-activity-information/25059

---

## Post #1 by @Niamh_Mc_Ardle (2022-09-02 20:51 UTC)

<p>Hi there,</p>
<p>I am new to 3D Slicer and was looking for an answer to my question in the forum but I haven’t been able to find one yet.</p>
<p>I would like to use my CT image to obtain a VOI of the lungs and liver. I would then like to apply this VOI to my PET data and work out the activity in the VOI for both my lungs and liver.</p>
<p>Is this possible?</p>
<p>I would be grateful for any and all help you could offer me, or even point me in the best direction to go with this.</p>
<p>Kind Regards,<br>
Niamh</p>

---

## Post #2 by @lassoan (2022-09-03 14:40 UTC)

<p>You can use Segment Editor module to specify a VOIs (in Slicer it is called segments) based on the CT (using paint effect, thresholding, etc.). You can then use this segment to blank out all the values outside the segment in the PET image (using “Mask volume” effect): . You can then get all the voxel values from the masked volume as a numpy array in the Python console using <code>slicer.util.arrayFromVolume</code> and compute the activity using numpy functions.</p>
<p>I would recommend <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">this tutorial</a> to learn about Python scripting in Slicer.</p>
<p>If you have a complete workflow, we can help you create a nice automated module from it, with a convenient graphical user interface, using Python scripting.</p>

---

## Post #3 by @Niamh_Mc_Ardle (2022-09-13 12:42 UTC)

<p>Thanks so much Andras!</p>

---
