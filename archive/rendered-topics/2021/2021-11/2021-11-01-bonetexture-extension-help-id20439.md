# BoneTexture Extension Help

**Topic ID**: 20439
**Date**: 2021-11-01
**URL**: https://discourse.slicer.org/t/bonetexture-extension-help/20439

---

## Post #1 by @jamieawren (2021-11-01 13:14 UTC)

<p>Hello All,</p>
<p>I am currently having trouble with the BoneTexture Extension and was hoping that someone may be of help. I have a cranium that I have segmented into 8 segments, and I would like to use the BoneTexture extensions “Compute BM Features” to compute BV/TV, etc for each of the 8 segments. I have created the segments and exported them as a binary label map. I then put the master scan for the “input scan” and would like to use each of the segments as the “mask”, however when I do so, I get the same result for each segment. Is this because slicer is exporting all the segments into a single binary label map when I do the export? Is there a way to do this? It’s a very critical part of my research project, so any help whatsoever would be greatly appreciated.</p>
<p>Take good care,</p>
<p>Jamie</p>

---

## Post #2 by @jamieawren (2021-11-01 13:23 UTC)

<p>I found a workaround shortly after I posted! If you hide all segments except for the one you want to export to a binary label map and do that for each segment respectively, then you will be able to compute the BM features for each segment individually.</p>

---

## Post #3 by @lassoan (2021-11-02 20:36 UTC)

<p>If you need analyze many images then you can automate these steps by a short Python scripts. Even better, you could update the Python script that <a href="https://github.com/Kitware/BoneTextureExtension/blob/master/BoneTexture/BoneTexture.py">BoneTexture analysis Python script</a> to iterate through all the segments and report results for each.</p>

---

## Post #4 by @jamieawren (2021-11-03 14:29 UTC)

<p>I’m very, very, (very) novice when it comes to Python so I’m in a situation when the time to do it manually may be = to the time it would take to run the scripts. I’ll take a whack at it though! Thank you!</p>

---
