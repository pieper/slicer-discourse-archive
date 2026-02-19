---
topic_id: 3339
title: "Create A 3D Fetus From An Ultrasound 4D"
date: 2018-06-29
url: https://discourse.slicer.org/t/3339
---

# Create a 3D fetus from an ultrasound 4D

**Topic ID**: 3339
**Date**: 2018-06-29
**URL**: https://discourse.slicer.org/t/create-a-3d-fetus-from-an-ultrasound-4d/3339

---

## Post #1 by @danilo_santos_cunha (2018-06-29 20:47 UTC)

<p>Hello everyone!</p>
<p>I’m new here, and I’ve seem some conversations about this subject, but anyone knows how to convert an ultrasound 4Dn exam ( philips ) to a printable data?</p>

---

## Post #2 by @adamrankin (2018-06-29 21:16 UTC)

<p>Hehehe, are congratulations in order?</p>
<p>My wife wouldn’t let me scan <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"></p>
<p>See SlicerHeart extension for converting Philips 4D “dicom” files. Once complete, use the Sequences to load it as a 3d + t volume.</p>
<p>I’m unsure about volume reconstruction using Slicer. I’ve done it before using the Plus library.</p>
<p>Edit: If one of the 3D frames is particularly good, you could segment out the fetus from that frame, clean it up a bit in MeshLab, then 3D print it.</p>
<p>If you want to get really hardcore, you could print the fetus in PLA, and use it as a lost-plastic mold for casting it in bronze/brass.</p>
<p>I mean… not that I’ve thought about it.</p>

---
