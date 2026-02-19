---
topic_id: 10121
title: "How To Disable Saving Png When Saving An Mrml Scene"
date: 2020-02-05
url: https://discourse.slicer.org/t/10121
---

# How to disable saving PNG when saving an mrml scene

**Topic ID**: 10121
**Date**: 2020-02-05
**URL**: https://discourse.slicer.org/t/how-to-disable-saving-png-when-saving-an-mrml-scene/10121

---

## Post #1 by @Vincent_C (2020-02-05 07:40 UTC)

<p>Hi all,</p>
<p>How can I disable the .png that automatically saves when I save the an mrml scene? I have no use for this screenshot of my scene and would like to turn off this feature.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-02-05 15:39 UTC)

<p>The thumbnail is saved with the scene to allow third-party software to preview scene content without being able to parse the files.</p>
<p>You can save the scene without this screenshot by using a Python command (calling <code>qSlicerCoreIOManager::saveScene</code> with an empty screenshot parameter).</p>

---

## Post #3 by @Vincent_C (2020-02-05 18:48 UTC)

<p>Thanks, this is helpful!</p>
<p>Using the command saves all the scene files. How can I save <strong>only</strong> the .mrml scene and .seg.nrrd?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-02-05 19:17 UTC)

<p>In general, the .mrml file is incomplete without the additional files that it refers to. The .seg.nrrd file is designed to be fairly self-contained, so you may not need to store the .mrml file. If there are some specific things you want to store with the segmentation then you can either add custom tags to segments (those are saved in the .seg.nrrd file) or create a json sidecar (additional metatada in a separate file).</p>

---
