---
topic_id: 13890
title: "Use 3D Slicer With Vr For Teaching"
date: 2020-10-06
url: https://discourse.slicer.org/t/13890
---

# Use 3D slicer with VR for teaching

**Topic ID**: 13890
**Date**: 2020-10-06
**URL**: https://discourse.slicer.org/t/use-3d-slicer-with-vr-for-teaching/13890

---

## Post #1 by @sebstax (2020-10-06 13:23 UTC)

<p>Dear all,</p>
<p>Have you ever used 3D slicer with virtual reality to teach?<br>
Is there a way to build pedagogical content with 3D slicer such as, locate the appropriate part, annotate the correct part?</p>
<p>I’ll be interested in getting your feedback.</p>
<p>Many thanks in advance.<br>
Best regards</p>

---

## Post #2 by @cpinter (2020-10-06 13:31 UTC)

<aside class="quote no-group" data-username="sebstax" data-post="1" data-topic="13890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/35a633/48.png" class="avatar"> sebstax:</div>
<blockquote>
<p>Have you ever used 3D slicer with virtual reality to teach?</p>
</blockquote>
</aside>
<p>What do you have in mind? Who has the headset on? What does she/he do?</p>
<aside class="quote no-group" data-username="sebstax" data-post="1" data-topic="13890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/35a633/48.png" class="avatar"> sebstax:</div>
<blockquote>
<p>Is there a way to build pedagogical content with 3D slicer such as, locate the appropriate part, annotate the correct part?</p>
</blockquote>
</aside>
<p>There are lots of anatomical atlases, but lots of basic interaction such as annotation is so far missing from SlicerVR. It will be added in the future for sure but we don’t have a concrete roadmap for that yet.</p>

---

## Post #3 by @sebstax (2020-10-07 09:08 UTC)

<p>thank you for the quick feedback.</p>
<p>the idea is to have a group of students. Up to 6 wearing VR headset, or AR headset.<br>
They visualize, and a teacher can select a part and ask of the user to annotate the part.</p>
<p>The idea is a pedagogical tool.</p>

---

## Post #4 by @cpinter (2020-10-07 11:00 UTC)

<aside class="quote no-group" data-username="sebstax" data-post="3" data-topic="13890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/35a633/48.png" class="avatar"> sebstax:</div>
<blockquote>
<p>can select a part</p>
</blockquote>
</aside>
<p>Select how?</p>
<p>Is this all happening remotely?<br>
Is everybody sharing the same live scene, or they load a Slicer scene individually?</p>
<p>SlicerVR currently is quite limited (it can show any scene, and you can navigate conveniently but basically that’s it), but some VR features are coming hopefully soon. For example collaboration within the same scene. Also annotation and segmentation within VR.</p>

---

## Post #5 by @sebstax (2020-10-07 12:12 UTC)

<p>I imagine the following set up :  a teacher on his desktop, selecting part in Slicer normal app. (or he could also have a VR headset, an gaze at a part with controller).<br>
A group of 6 students with headset, in the same room.</p>
<p>This is an idea for a long term project.<br>
Would you need support to develop a “scenaristic” mode for teaching in 3Dslicer VR?</p>

---

## Post #6 by @cpinter (2020-10-07 12:25 UTC)

<p>So as I understand there is the instructor with a desktop computer, loading a Slicer scene with some CT or MRI. Then gives the instruction to the students to segment one organ (I still don’t understand what you mean by “select”, but frankly also not sure about what you mean by “annotate” so I assume segment?). They do it in VR in the same scene, but not in a synchronized way, i.e. they don’t share the actual scene, but only use the same one for starting, then they do their own thing.</p>
<p>Does the instructor need to monitor the progress of the students real-time? If so, how do you imagine that?</p>
<p><a class="mention" href="/u/nagy.attila">@nagy.attila</a> You were thinking about something like this as well. Do you have anything to add?</p>
<aside class="quote no-group" data-username="sebstax" data-post="5" data-topic="13890">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/35a633/48.png" class="avatar"> sebstax:</div>
<blockquote>
<p>Would you need support to develop a “scenaristic” mode for teaching in 3Dslicer VR?</p>
</blockquote>
</aside>
<p>Thank you, we can of course use any help. First, however, we need to develop some core features to facilitate setting up such scenarios such as an actual in-VR UI that is still missing.</p>

---

## Post #7 by @sebstax (2020-10-07 12:49 UTC)

<p>to sum up, the first draft is the following :</p>
<p>The instructor is on a desktop or in VR , to be defined. For instance, he imports a DICOM file.</p>
<ul>
<li>6 students are in VR, in the same room as the instructor.</li>
<li>Everyone is logged in the same virtual scene, and see the DICOM file from his own angle.</li>
<li>The instructor ask user 1 to find a given anatomical part.</li>
<li>User 1 with VR controller manipulate the DICOM, zoom, find the appropriate part, and use a “select” tool or “annotate” tool to highlight the part.</li>
</ul>
<p>By annotate I mean he should be able to write, but probably not the best user experience. So it can be a “pin” tool instead.</p>
<p>An other idea :</p>
<ul>
<li>The instructor ask user 1 to find a given pathology.</li>
<li>User 1 with VR controller manipulate the DICOM, zoom, unzoom…</li>
<li>The instructor load an other DICOM and ask user 2 what is the pathology.</li>
</ul>

---

## Post #8 by @cpinter (2020-10-07 12:58 UTC)

<p>Thanks, much clearer now!</p>
<p>Yes, these features can be expected soon. This comes down to two main core functions that need to be added:</p>
<ul>
<li>Collaborative VR: sharing a live scene between Slicer instances. We are quite sure that we have won a grant just for this (the scores are out, the final decision not yet), which starts in a few months.</li>
<li>In-VR interactive widget: It is a very important core feature that has not been possible to add due to being stuck on VTK8. Now that Slicer has been updated to use the new VTK, we can start working on this too (showing any Slicer widget in VR, and use the controller as a laser pointer and be able to click etc.), hopefully in terms of the aforementioned grant, or something else. Once this is done, adding any widget that allows you to do something that you can do in regular Slicer would be super easy.</li>
</ul>

---

## Post #9 by @sebstax (2020-10-07 13:18 UTC)

<p>Thank you very much for the complete answer and sorry for the lack of information in my first message.</p>
<p>Fingers crossed for your team to get the grant!</p>

---

## Post #10 by @nagy.attila (2020-10-11 21:51 UTC)

<p>Hi all,</p>
<p>I think there could be two slightly different use cases.<br>
One is similar to what Sébastien described. On the other hand, that would more be “radiological anatomy”, as selecting anatomical features on scans (be it CT or MR) needs some practice. Both to use a (the) software, and actually to know what they are looking at or looking for. Like I can’t imagine using any software this way to teach first, maybe second year medical students.<br>
Placing a pin as an answer might be okay.<br>
Doing segmentations would involve a lot of manual work (in most cases) so unless this is what you/we want to teach it is not something we should hurry to implement.<br>
Of course just segmenting out a small anatomical feature (as an answer, for example) can be okay.</p>
<p>The other way that would maybe be feasible is to load a scene with already segmented structures (be it vtk models or segments)  and then teach details on those. It could be used instead of printed 3D models.</p>
<p>Probably the most important would be to have a way to annotate features on the fly in a convenient way. I have no idea how that could be done, ie. inputting text in VR is maybe not that fast and/or convenient.</p>
<p>Crossing my fingers for that grant too and let’s get back to it then! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Cheers,<br>
Attila</p>

---

## Post #11 by @cpinter (2020-10-12 08:16 UTC)

<p>Thanks for your insight, Attila!</p>
<p>I think the other scenario you describe is easier, because we can already share a scene like that (~broadcasting, when one person controls a scene that the others can also see in VR). Placing/moving fiducials may be enough in this case, while the instructor speaks. Unless I misunderstand something.</p>

---
