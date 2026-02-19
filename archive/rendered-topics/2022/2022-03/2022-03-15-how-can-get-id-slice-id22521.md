---
topic_id: 22521
title: "How Can Get Id Slice"
date: 2022-03-15
url: https://discourse.slicer.org/t/22521
---

# How can get id slice?

**Topic ID**: 22521
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/how-can-get-id-slice/22521

---

## Post #1 by @nicdubovic (2022-03-15 14:08 UTC)

<p>I try to get id slices when using tools in the SegmentEditor module. How can I get it?</p>

---

## Post #2 by @mikebind (2022-03-15 15:22 UTC)

<p>I think there are a few different things you might mean.  Do you mean segment IDs (a string of characters which uniquely identifies a segment within a segmentation)? Or a slice view ID (a string of characters which uniquely identifies one of the slice view areas, like the Red, Yellow, or Green slices)?  Can you share a little more about what you are trying to do?</p>

---

## Post #3 by @nicdubovic (2022-03-15 15:40 UTC)

<p>I would like to get (if they exist) model slicing identifiers. I need to save the values of identifiers after the interaction of the instrument on the scene. And I need to know that for each slide there is a unique identifier belonging only to it and not changing. I think it can be found in dicome or there is another way. Please explain how to find it. if I’m not right, tell me.<br>
I guess I mean the second variant, but it’s not exactly</p>

---

## Post #4 by @mikebind (2022-03-15 16:32 UTC)

<p>I am still having trouble understanding exactly what you are looking for.  When you say the “interaction of the instrument on the scene”, are you referring to a surgical instrument (like for image-guided surgical interventions),  or are you referring to a segment editor tool (like “Threshold” or “Smoothing”)?</p>
<aside class="quote no-group" data-username="nicdubovic" data-post="3" data-topic="22521">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nicdubovic/48/10381_2.png" class="avatar"> nicdubovic:</div>
<blockquote>
<p>I think it can be found in dicom</p>
</blockquote>
</aside>
<p>There are unique identifiers in DICOM headers, but these don’t refer to Slicer objects, they instead allow cross referencing between DICOM files, so I’m not sure whether that is what you are looking for.</p>

---

## Post #5 by @nicdubovic (2022-03-15 16:59 UTC)

<p>I mean segment editor tools (like “Draw”, “Scissors”, “Draw”)</p>

---

## Post #6 by @mikebind (2022-03-15 17:02 UTC)

<p>Great, thanks.  If we take a step back from the details, what are you trying to accomplish?  If you had the identifiers you are looking for, what would you want to do with them?</p>

---

## Post #7 by @nicdubovic (2022-03-15 17:08 UTC)

<p>I want to log id’s slice after instrument click on scene in red / green / yellow planes<br>
If I move the slider, the current id of the viewed slice on which the tool draws will change.</p>

---

## Post #8 by @mikebind (2022-03-15 17:30 UTC)

<p>OK, I think I am beginning to understand.  You want to capture and log the image volume location where you click when using Segment Editor tools, is that correct?</p>
<p>I’m not sure whether there is an easy way to capture that information (the location of a click) while using Segment Editor effects, because I believe the Segment Editor effects capture the mouse click events and I’m not sure where you would intervene or get a signal from them to do your logging.  <a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a>, or <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a>, am I correct here?  Is there an event <a class="mention" href="/u/nicdubovic">@nicdubovic</a> could respond to to achieve this logging while using Segment Editor effects?</p>
<p>When you are not in Segment Editor, an easy way to record locations (which you can then translate back into voxel array coordinates if desired) is through placing Markups control points.</p>
<p>You might find this discussion helpful: <a href="https://discourse.slicer.org/t/how-to-capture-right-clicked/16668" class="inline-onebox">How to capture right clicked</a></p>

---

## Post #9 by @nicdubovic (2022-03-15 17:42 UTC)

<p>I want to capture and log the image volume location where you click when using Segment Editor tools.</p>
<p>Please take a look at the attached picture. This is the output of the Data Probe. At the bottom of the picture (B 107_2 (217, 252, 180)), there are what looks like slice numbers displayed in different planes.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b229b99429d1fcaf8b1a2e6cdfe15977ebefeee7.png" alt="image" data-base62-sha1="pq6nRNjVw1oDwLslusvP92Idlbh" width="331" height="163"></p>

---

## Post #10 by @mikebind (2022-03-15 17:49 UTC)

<p>Here is another relevant discussion which you might find helpful: <a href="https://discourse.slicer.org/t/print-dataprobe-text-with-shift-key/21331" class="inline-onebox">Print dataprobe text with shift key</a></p>

---

## Post #11 by @nicdubovic (2022-03-15 17:56 UTC)

<p>But I try do it using C++. I have static method of class which can log information</p>

---

## Post #12 by @pieper (2022-03-15 17:56 UTC)

<p>Generally the way effects manage events is internal to the effect so there’s not a good way to log exactly what the events correspond to, but you could probably detect that events are happening (clicks or keystrokes) in a way that doesn’t interfere with the effect and log those along with the info from the DataProbe module.  You can also know what effect was active at the time of the event, so things like paint should be easy enough to figure out.</p>

---

## Post #13 by @pieper (2022-03-15 17:57 UTC)

<aside class="quote no-group" data-username="nicdubovic" data-post="11" data-topic="22521" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nicdubovic/48/10381_2.png" class="avatar"> nicdubovic:</div>
<blockquote>
<p>But I try do it using C++</p>
</blockquote>
</aside>
<p>The code would be basically the same in C++</p>

---

## Post #14 by @nicdubovic (2022-03-15 18:31 UTC)

<p>Please tell me, is there a way to find out a slice ID (a string of characters which uniquely identifies one of the slice view areas, like the Red, Yellow, or Green slices)</p>

---

## Post #15 by @pieper (2022-03-15 18:52 UTC)

<p>These scripts should help:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=sliceView#capture-slice-view-into-png-file-with-white-background" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html?highlight=sliceView#capture-slice-view-into-png-file-with-white-background</a></p>

---
