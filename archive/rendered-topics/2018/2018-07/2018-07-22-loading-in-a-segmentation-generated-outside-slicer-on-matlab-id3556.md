---
topic_id: 3556
title: "Loading In A Segmentation Generated Outside Slicer On Matlab"
date: 2018-07-22
url: https://discourse.slicer.org/t/3556
---

# Loading in a segmentation generated outside slicer (on matlab)

**Topic ID**: 3556
**Date**: 2018-07-22
**URL**: https://discourse.slicer.org/t/loading-in-a-segmentation-generated-outside-slicer-on-matlab/3556

---

## Post #1 by @Nassir (2018-07-22 10:50 UTC)

<p>Hey guys! I’m trying to load a scalar volume that was exported out of slicer, “WHS_SD_rat_atlas_v2_original”, back in as a segmentation. The whole reason I am doing this is to avoid manually defining the segments.</p>
<p>To do so, I pulled together some matlab scripts I found online to make the matlab script “Copy_of_read_Atlas2” which loads the scalar volume together with a legend in the form of a .txt file. It begins to generate the segmentation file with header information embedded in the same file, similar to a segmentation that I exported out of slicer “1015Segmentation.seg”. There’s a loop in there that I have printing the information for each segment (line 169), but I have it set to 1 right now because this is a high-RAM demand script. I think it’s good to just get one segmentation going for now. Then there’s the loop that reassigns the scalar volume onto 4-D array for the segmentation (line 208, also set to 1). I think all that stuff works well.</p>
<p><em>I think the issue might have to do with datatypes? I don’t have a compsci background but I’m suspicious of all the "U"s that can be read (in matlab, line 25) off the bad generated segmentation. The generation of the data starts on line 225 in “Copy_of_read_Atlas2”.</em> Could someone point it out?</p>
<p><strong>Trying to load the bad segmentation into slicer crashes it.</strong> It won’t load on old versions of slicer (I’m using 4.8.1).</p>
<p>Here are all the files:</p>
<p><a href="https://drive.google.com/open?id=1vP9KQiKK9NHCrKB3G03fXsAV3JAclOdT" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1vP9KQiKK9NHCrKB3G03fXsAV3JAclOdT</a></p>

---

## Post #2 by @lassoan (2018-07-22 11:57 UTC)

<p>If you use a recent nightly build of Slicer then you can follow these steps:</p>
<ul>
<li>save segmentation from MATLAB as nrrd file using <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">nrrdwrite.m</a> (or return it from a MATLAB function using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">MatlabBridge</a>)</li>
<li>load the nrrd file into Slicer as labelmap volume (using <code>slicer.util.loadLabelVolume</code> method; if you use GUI to select and load the volume, in “Add data” dialog, click “Show options” and select labelmap option)</li>
<li>import the labelmap into a segmentation node as shown in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D">example</a>
</li>
</ul>

---

## Post #3 by @Nassir (2018-07-22 21:23 UTC)

<p>Thanks Andras! Those python interactor steps worked smoothly using the Nightly 4.9.0.  Cheers.</p>

---
