# Flip orientation in the axial viewport?

**Topic ID**: 2759
**Date**: 2018-05-04
**URL**: https://discourse.slicer.org/t/flip-orientation-in-the-axial-viewport/2759

---

## Post #1 by @drusmanbashir (2018-05-04 10:52 UTC)

<p>Hi,<br>
While viewing axial slices, I wish to be able to flip the view so that the right side becomes left and vice-versa like in every DICOM viewer. Is this function there / a plugin that allows it?</p>
<p>Thanks<br>
Usman.</p>

---

## Post #2 by @pieper (2018-05-04 13:10 UTC)

<p>Hi Usman -</p>
<p>For Slicer we prefer to be consistent in the use radiology clinical conventions for left/right viewing to minimize the chances for misinterpretation (the neuroimaging community has an unfortunate history of mixing up left/right and we want to be careful to avoid that).</p>
<p>But if you want to change a view, you can use the Reformat module to make arbitrary changes to the slice planes.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @drusmanbashir (2018-05-04 14:40 UTC)

<p>That’s the dev’s decision though if it were a real problem, clinical workstations (where orientation mistakes can have disasterous consequences) would not have this function. Perhaps in a future update…</p>
<p>Usman.</p>

---

## Post #4 by @lassoan (2018-05-04 15:40 UTC)

<aside class="quote no-group" data-username="drusmanbashir" data-post="3" data-topic="2759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/drusmanbashir/48/1282_2.png" class="avatar"> drusmanbashir:</div>
<blockquote>
<p>Perhaps in a future update…</p>
</blockquote>
</aside>
<p>You don’t need to wait for a future update, as the feature has been already implemented. It just has not been exposed on the user interface, because there are so many things are there already and there has not been strong request for this specific feature.</p>
<p>You can left-right “flip” slice view orientation presets by editing you .slicerrc.py file as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_slice_view_orientation" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #5 by @lassoan (2019-01-23 18:38 UTC)

<p>2 posts were split to a new topic: <a href="/t/change-displayed-image-orientation-labels-l-r/5487">Change displayed image orientation labels (L, R, …)</a></p>

---

## Post #6 by @Nathan (2022-11-01 23:15 UTC)

<p>Can you update your instructions on where to change this?</p>
<p>I am curious why you changed the default slice view from the Radiologist conventions…</p>

---

## Post #7 by @jamesobutler (2022-11-02 00:37 UTC)

<aside class="quote no-group" data-username="Nathan" data-post="6" data-topic="2759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c5a1d2/48.png" class="avatar"> Nathan:</div>
<blockquote>
<p>Can you update your instructions on where to change this?</p>
</blockquote>
</aside>
<p>Clicking through the links to the new location will reach you to:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-default-slice-view-orientation" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-default-slice-view-orientation</a></p>

---

## Post #8 by @lassoan (2022-11-03 12:47 UTC)

<aside class="quote no-group" data-username="Nathan" data-post="6" data-topic="2759">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c5a1d2/48.png" class="avatar"> Nathan:</div>
<blockquote>
<p>I am curious why you changed the default slice view from the Radiologist conventions…</p>
</blockquote>
</aside>
<p>We haven’t changed it. Make sure you load your DICOM images with the DICOM module. Using “Add data” module with a DICOM file would pass slices directly to a volume reader, which is not guaranteed to load all DICOM images correctly.</p>

---

## Post #9 by @Nathan (2022-11-03 15:23 UTC)

<p>Thank you both for the response.</p>
<p>It’s very weird - yesterday it was flipping the images on my installation on a new PC of Slicer. I can’t get it to repeat this behavior today. If it happens again, I will let you know.</p>
<p>-Nathan</p>

---
