# Visualization of MRI’s of the lumbar and sacral vertebra

**Topic ID**: 7212
**Date**: 2019-06-18
**URL**: https://discourse.slicer.org/t/visualization-of-mri-s-of-the-lumbar-and-sacral-vertebra/7212

---

## Post #1 by @ProblemsStanding (2019-06-18 00:37 UTC)

<p>Operating system: windos 10 and a brain not made for this.<br>
Slicer version: 4.10.2<br>
Expected behavior: I want to make a 3D visualization from MRI’s of the lumbar and sacral vertebra with nerves, vessels, muscles levator ani, and nearby organs/cyst. My hope is to better understand what goes wrong when I stand up, sit or walk. I have DICOM files from MRI pelvic, abdominals and total columna. I also have MRI pelvic and abdominal from 2017 for comparison.</p>
<p>Actual behavior: I’ve read just about all training tutorials for a week now, but I still can’t get even close to my goal. There is to many basics I don’t understand. So I’m reaching out to see if anyone would have the time to help me create this visual, so I can get out of this wheelchair. Please refer me if there is a better place to ask for this kind of support.</p>

---

## Post #2 by @cpinter (2019-06-18 15:40 UTC)

<p>You can do volume rendering and/or segmentation to visualize structures.</p>
<p>Volume rendering is simpler but harder to differentiate between the structures. You need to choose a good starting transfer function and then tune it (shift slider, maybe the transfer function controls in the advanced section) to achieve good visualization.</p>
<p>Segmentation is done in the Segment Editor module, but for that you’ll need very good understanding of human anatomy and the way the different tissue types show up in different MR sequences.</p>
<p>Based on your description I don’t know how I could provide more help right now, but let us know if you have specific questions or you’d like to show some screenshots and describe what you’d like instead.</p>

---
