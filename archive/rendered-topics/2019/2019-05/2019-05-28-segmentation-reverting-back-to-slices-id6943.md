---
topic_id: 6943
title: "Segmentation Reverting Back To Slices"
date: 2019-05-28
url: https://discourse.slicer.org/t/6943
---

# Segmentation- Reverting back to Slices

**Topic ID**: 6943
**Date**: 2019-05-28
**URL**: https://discourse.slicer.org/t/segmentation-reverting-back-to-slices/6943

---

## Post #1 by @juliawithrow (2019-05-28 06:30 UTC)

<p>Hi!</p>
<p>I’m working on segmenting a skeletal model. I have created the model and saved it, but now want to go back and edit parts of my segmentations in the axial and coronal views, but am not sure how to get back to these slices after the model has been created. Any tips?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2019-05-28 12:08 UTC)

<p>Hi <a class="mention" href="/u/juliawithrow">@juliawithrow</a> -</p>
<p>There should be no problem saving and reloading segmentations for further editing.  Did you review the documentation and tutorials?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="onebox" target="_blank" rel="nofollow noopener">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>

---

## Post #3 by @juliawithrow (2019-05-28 12:45 UTC)

<p>Yes, I understand that I think. The only issue I’m having is if I reimport the dicom or non dicom data it has lost my progress in segmenting. I just need to go back to where I was right before I made the model.</p>

---

## Post #4 by @pieper (2019-05-28 16:22 UTC)

<p>You should be able to just save the scene (click the ‘wrapped package’ icon if you want to save a single file with all the data embedded).  Then you can reload the scene later and get back to where you were.  Is that not working for you?</p>

---

## Post #5 by @juliawithrow (2019-05-28 16:40 UTC)

<p>Once I create the model out of the segmentations, 3D slicer makes the segmentation slices go to a black screen. When I save this model, it won’t let me ever go back to the slices. I think the problem is how it deletes the slices when I make the model. Does this make sense? Sorry for any confusion.</p>

---

## Post #6 by @cpinter (2019-05-28 17:13 UTC)

<p>Do you use Slicer 4.10.2? Do you use Segment Editor?</p>

---

## Post #7 by @pieper (2019-05-28 21:22 UTC)

<p><a class="mention" href="/u/juliawithrow">@juliawithrow</a> it sounds like you are using the legacy Editor module - in recent versions of Slicer the slice views do get reset after doing model building (you’d need to reset them in the slice view controllers).  But instead we suggest you migrate to the Segment Editor instead, which has a lot of new features and is being actively supported.</p>

---

## Post #8 by @juliawithrow (2019-05-28 21:33 UTC)

<p>I’m using 4.10.1 for mac osx is this the one that would be having issues?</p>

---

## Post #9 by @juliawithrow (2019-05-28 21:35 UTC)

<p>How do I reset them in the slice view controllers? I will update ASAP but for now I just hope to get back to the slices, I am going to have to restart the entire segmentation if I can’t get back.</p>
<p>Thank you for all of the help so far</p>

---

## Post #10 by @pieper (2019-05-28 22:34 UTC)

<p>You need to re-select the source image as the master volume after you apply the Make Model effect.  That will reset the viewers with the background and labelmap.</p>
<p>HTH,<br>
Steve</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a9c200af9abaee4fdaa02cae21fadbc9129055e.png" alt="image" data-base62-sha1="m3K1G5oj8eDIFkWKNL8pEjHo9tA" width="491" height="137"></p>

---
