---
topic_id: 1055
title: "Viewing Volume Origin Alignment Of Frankfurt Plane"
date: 2017-09-14
url: https://discourse.slicer.org/t/1055
---

# Viewing volume origin/ alignment of Frankfurt plane?

**Topic ID**: 1055
**Date**: 2017-09-14
**URL**: https://discourse.slicer.org/t/viewing-volume-origin-alignment-of-frankfurt-plane/1055

---

## Post #1 by @Aidan (2017-09-14 23:40 UTC)

<p>Hi all,</p>
<p>I’ve been looking for answers to what seems like a relatively trivial problem, but without much luck. Hopefully I’m just missing something obvious!</p>
<p>I have CT and MRI volumes of anesthetized animals in a stereotaxic frame that will be used to plan surgeries (the surgeries will use the same stereotaxic frame). Since the stereotax was not necessarily perfectly aligned to the scanner field, I therefore need to move the origin of these volumes to correspond with the stereotaxic origin (the center of the ear bars), and perform rigid transforms in order to align the Frankfurt plane (the horizontal plane that passes through the auditory meatus/ ear bars and infraorbital ridge/ eye bars) as the axial plane of the volume.</p>
<p>In the Volumes module I can edit the ‘image origin’ in mm. However, I have no idea how I am changing the origin relative to structures in the volume (e.g. ear bars). Is there a simple way for me to move the crosshair to the same coordinates as the current image origin, so that I can move the origin to the center of the ear bars?</p>
<p>Ideally what is needed here is an analog of the ACPC transform module. Instead of manually selecting the anterior and posterior commissures (internal landmarks), the user would select the tips of the left and right ear bars, plus the contact point of the eye bars with the infraorbital ridge (external landmarks). Then a transform would be applied to align the Franfurt plane and move the origin to between the ear bars. It seems mathematically straightforward - can anybody point me to some online references that might help me create such a module?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-09-15 00:37 UTC)

<p>This problem is usually solved using landmark registration.</p>
<p>You can either use Landmark registration module in the Slicer core; or Fiducial registration wizard module in SlicerIGT extension.</p>

---

## Post #3 by @Aidan (2017-09-15 01:48 UTC)

<p>Thanks Andras. I’ve had a look at the Landmark registration module - I can see how it’s useful for co-registering volumes across modalities (CT &lt;-&gt; MRI). I can also see how this allows me to select landmarks within a volume (e.g. tips of the ear bars), but I don’t understand how I can use those selected landmarks to transform a single volume (e.g. aligning a CT volume so that the Frankfurt plane = the axial plane)… is there some additional documentation (beyond this: <a href="https://www.slicer.org/wiki/Documentation/4.4/Modules/LandmarkRegistration" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.4/Modules/LandmarkRegistration</a>) that would explain this for me?</p>

---

## Post #4 by @lassoan (2017-09-15 02:09 UTC)

<p>Once you have the transform that aligns the moving volume to the fixed volume, you can apply that transform to the moving volume (dynamically transform the volume) and optionally harden the transform on the volume (overwrite image position and orientation in the volume node). If you need the two volumes to be be in the same grid (same origin, spacing, axis directions) then resample the moving volume on the grid of the fixed volume using Resample scalar volume module.</p>

---

## Post #5 by @Aidan (2017-09-15 02:56 UTC)

<p>Thanks for taking the time to explain further Andras, but I’m afraid either I’m still not getting it, or I’m not communicating my problem clearly enough.</p>
<p>What I need to do is very straight forward and I know I can do it in other imaging software but I’d really like to be able to do it in Slicer since the rest of my processing pipeline also requires Slicer.</p>
<p>Specifically, I need to visually select the <em>voxel</em> coordinate of a single volume that corresponds to the stereotaxic origin (i.e. xyz = [0,0,0] mm - see the location of the crosshairs in the attached image).</p>
<p>Once I have that coordinate, I can write this to the header of my volume file (e.g. .nii) using the ‘Volumes’ module, and do whatever transforms I need.</p>
<p>So is there any way to manually place the cursor/ crosshair in a volume and get the <em>voxel</em> coordinate in Slicer?</p>

---

## Post #6 by @lassoan (2017-09-15 03:10 UTC)

<aside class="quote no-group" data-username="Aidan" data-post="5" data-topic="1055">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c5a1d2/48.png" class="avatar"> Aidan:</div>
<blockquote>
<p>is there any way to manually place the cursor/ crosshair in a volume and get the voxel coordinate in Slicer?</p>
</blockquote>
</aside>
<p>Voxel coordinate is shown in the data probe widget in the lower left corner of the screen. If you need to get the coordinate in a module then you can ask the user to place a markup fiducial or get the crosshair position as shown in the example here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_current_mouse_coordinates_in_a_slice_view" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #7 by @Aidan (2017-09-15 03:17 UTC)

<p>Thanks! I warned you it was probably very simple <img src="https://emoji.discourse-cdn.com/twitter/roll_eyes.png?v=5" title=":roll_eyes:" class="emoji" alt=":roll_eyes:"></p>

---
