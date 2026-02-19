---
topic_id: 21055
title: "Is Resampling Necessary"
date: 2021-12-14
url: https://discourse.slicer.org/t/21055
---

# Is Resampling Necessary?

**Topic ID**: 21055
**Date**: 2021-12-14
**URL**: https://discourse.slicer.org/t/is-resampling-necessary/21055

---

## Post #1 by @jamieawren (2021-12-14 15:53 UTC)

<p>Hi Everyone,</p>
<p>I am using CT images to create segments of the cranium, and certain structures within the cranium, and then will be using segment statistics to compare the HU and volume for the segments between two different treatment groups. All the CT scans were done under the same protocol. Is it necessary to resample the images so the scans are isotropic? Does anyone have a good resource for the logic of resampling scans?</p>
<p>Thank you!</p>
<p>Jamie</p>

---

## Post #2 by @muratmaga (2021-12-14 22:58 UTC)

<p>If you are going to need to use filters for smoothing, or do morphological operations (dilation and erosion), you will find that resultant segments will look better if you have isotropic data.</p>

---

## Post #3 by @jamieawren (2021-12-15 16:43 UTC)

<p>Thank you! I am just doing segment statistics and bone morphometry features of the segments. But I think I still need to resample as some of the data is very disparate. The Crop Volume module tends to freeze slicer, so I think I will use Resample Scalar Volume, even though it appears to be a legacy module.</p>

---

## Post #4 by @muratmaga (2021-12-15 16:48 UTC)

<p>Crop Volume should work work. if it is freezing and becomes non-responsive, I suspect you are running out of memory. You will have the same problem if you try with the resampleScalarvolume.</p>
<p>What is the image spacing of your original data, the volume size, and data type? (You can find those under the volumes module). What it is the factor you are putting in Crop Volume (if you only want isotropic data, you should keep factor 1, and check isotropic voxels option).</p>

---

## Post #5 by @jamieawren (2021-12-15 17:55 UTC)

<p>resampleScalarvolume runs without a hiccup in approximately 30secs, but CropVolume gets hung up…</p>
<p>Image spacing is 0.566mmx0.566mmx0.5mm, but it varies. Some scans are all 0.5x0.5x0.5 while some go up to .7x.7x.5.</p>
<p>The volume size is 512x512x736. The data type is Scalar.</p>

---

## Post #6 by @muratmaga (2021-12-15 20:49 UTC)

<p>CropVolume shouldn’t hang, which version of Slicer is this?</p>
<p>What are you entering as voxel spacing to ResampleScalar?<br>
What factor are you putting in to CropVolume?</p>

---

## Post #7 by @jamieawren (2021-12-16 13:02 UTC)

<p>I’m using version 4.11.20210226 on an Intel Mac Running Monterey. My voxel spacing is 0.5mmx0.5mmx0.5mm and I believe I was using 1 as the factor for CropVolume.</p>

---

## Post #8 by @muratmaga (2021-12-16 16:04 UTC)

<p>Himm, everything looks normal. For a moment I was worried you might be entering 0.5 as if it is spacing not a factor to CropVolume, which actually would double the volume dimension in each axis (and more if you also checked the isotropic option). So you would end with a volume that’s 8-10 times larger than the original, which would have explained why CropVolume wasn’t finished or getting stalled.</p>
<p>But if that’s not the case, I wouldn’t know why cropvolume wouldn’t perform while resamplescalarvolume would, because under the hood I think they use the same command. <a class="mention" href="/u/lassoan">@lassoan</a> do you have any suggestions.</p>

---

## Post #9 by @jamieawren (2021-12-16 16:32 UTC)

<p>If I resample the volumes that are not 0.5mmx0.5mmx0.5mm, would I also need to resample the volumes that were already 0.5x0.5x0.5, for continuity’s sake?</p>

---

## Post #10 by @lassoan (2021-12-16 17:18 UTC)

<p>“Crop volume” module uses “Resample scalar/vector/DWI volume” module for resampling internally. I agree with <a class="mention" href="/u/muratmaga">@muratmaga</a> that running out of memory is the most likely issue.</p>
<p>Since your data set size without resampling is 400MB, if you resample with scaling factor of 0.5 then it increases the data size to 3.2GB, which means that you need about 30GB virtual memory space - on macOS it means that you need to have at least 30GB free disk space - if you want to make sure that the issue is not temporarily running out of memory.</p>

---
