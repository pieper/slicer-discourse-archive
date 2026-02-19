---
topic_id: 10692
title: "How To Create A 4D Animation"
date: 2020-03-15
url: https://discourse.slicer.org/t/10692
---

# how to create a 4D animation

**Topic ID**: 10692
**Date**: 2020-03-15
**URL**: https://discourse.slicer.org/t/how-to-create-a-4d-animation/10692

---

## Post #1 by @starhopper (2020-03-15 12:44 UTC)

<p>I’ve got a sequence of image stacks acquired in time lapse way. I want to visualize them by creating a 4D animation. Firstly I have to convert those image stacks into a DICOM file, thus I can browse it with MultiVolumeExplorer. Under Data module, I can create a new study and export it as a DICOM. But it ended up with splitting my image stacks into folders containing individual images of corresponding stacks. How can I generate a multivolume files that can be recognized by MutltiVolumeExplorer?</p>

---

## Post #2 by @lassoan (2020-03-15 12:46 UTC)

<p>I would recommend to use Sequences extension for this. If you load all the volumes into the scene then you can import them into a replayable 4D sequence as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes</a></p>

---

## Post #3 by @starhopper (2020-03-16 09:10 UTC)

<p>It does worked out! Thank you for this recommendation!</p>

---
