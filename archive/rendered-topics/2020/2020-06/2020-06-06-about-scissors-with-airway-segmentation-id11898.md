# About scissors with airway segmentation

**Topic ID**: 11898
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/about-scissors-with-airway-segmentation/11898

---

## Post #1 by @anitakh1 (2020-06-06 12:49 UTC)

<p>i used ‘segment lung airway’ module for airway segmentation. there are some leakages which i want to cut from volume. how can i do that. segment editor scissor only chops the selection made there during processing. how can i chop volume in volume rendering if i use segment lung airway module for segmentation?</p>

---

## Post #2 by @lassoan (2020-06-06 23:20 UTC)

<p>You can import the labelmap volume into a segmentation node and edit it in Segment Editor. If you want to blank out parts of a volume inside or outside a segment then use “Mask volume” effect (provided  by SegmentEditorExtraEffects extension).</p>

---

## Post #3 by @anitakh1 (2020-06-07 15:59 UTC)

<p>thank you sir for your prompt reply. i loaded the data and converted into labelmap using volumes. then i imported the label volume as master volume in segment editor (after installing SegmentEditorExtraEffects extension). then i used mask volume. but when i used show3D in this, it’s not showing 3D rendering. now how to use scissors to cut part of volume if it’s not showing the 3D volume? pl suggest. i am missing something, pl correct.</p>

---

## Post #4 by @lassoan (2020-06-07 18:42 UTC)

<p>You can show 3D volumes in 3D view by using Volume Rendering volume.</p>
<p>It is very rarely necessary to modify voxels of an acquired image. Can you write a bit more about the clinical problem and the approach you are trying to implement?</p>

---

## Post #5 by @anitakh1 (2020-06-09 11:47 UTC)

<p>actually i am using these airway segmented results as ground truth to train my CNN network for airway segmentation. so i have to remove all leakages. pl suggest how to do that.<br>
thank you</p>

---

## Post #6 by @lassoan (2020-06-09 13:20 UTC)

<p>OK, so you don’t need to modify the original image volume, only fix segmentation errors. There is no need for mask volume, simply edit your segmentation with various tools. For example, you can cut off extra regions using Scissors effect; or just cut connections with the leaked regions and then use Islands effect to discard all disconnecte regions. You can also cut off regions using Surface cut effect (provided by SegmentEditorExtraEffects extension).</p>

---

## Post #7 by @anitakh1 (2020-06-12 07:38 UTC)

<p>thanks a lot. it worked for few volumes as many branches got isolated. another thing i wanted to ask. i am using Segment Lung Airways module for airway segmentation but it’s doing slight over segmentation. is there any way to control segmentation in it.<br>
thank you</p>

---

## Post #8 by @lassoan (2020-06-12 15:38 UTC)

<p>Can you post a few screenshots?</p>
<p>The module’s source code is available <a href="https://github.com/acil-bwh/ChestImagingPlatform/blob/Slicer-CIP/CommandLineTools/SegmentLungAirways/SegmentLungAirways.cxx">here</a>. There are a number of hardcoded parameters that could be exposed in the module, but it is hard to tell which ones would make the most difference. If you are willing to build Slicer and Slicer-CIP extension then you could experiment with this and find out which parameters you need to tune.</p>
<p>Alternatively, you can use Segment Editor module to touch up the automatic segmentation results; or use Segment Editor to segment the airways from scratch. Grow from seeds, Fast marching, Local thresholding effects are all good candidates. Local thresholding and Fast marching effects are provided by SegmentEditorExtraEffects extension.</p>

---

## Post #9 by @anitakh1 (2020-06-14 05:57 UTC)

<p>thanks for your prompt reply. will surely try to use the ones recommended</p>

---
