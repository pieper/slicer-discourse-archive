# Pre/post-op CBCT matching

**Topic ID**: 11438
**Date**: 2020-05-06
**URL**: https://discourse.slicer.org/t/pre-post-op-cbct-matching/11438

---

## Post #1 by @Aras_J (2020-05-06 22:47 UTC)

<p>Hello everyone,</p>
<p>I am very new to Slicer and clicking myself through the basic tutorials learning this amazing tool step by step. But: what do i have to search for or is the any tutorial for following task:</p>
<p>Loading pre- and post op cbct’s of the skull - “match”?! them and then automatically define lower jaw movement in the translation and rotational axes.</p>
<p>Thanks in advance and delete my post or relink somewhere i find the answers if this is too basic/spam.</p>
<p>best regards from germany<br>
AJ</p>

---

## Post #2 by @timeanddoctor (2020-05-07 02:13 UTC)

<p>You can registrate the pre and post op sull by landmark registration. and calculate the transform  for the angle and line moving.</p>

---

## Post #3 by @cpinter (2020-05-07 08:38 UTC)

<p><a class="mention" href="/u/aras_j">@Aras_J</a> This is a completely legit question, don’t worry <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> The term you are looking for are image registration, the verb for which is register (not registrate).<br>
There are several modules in Slicer to do it, including the already mentioned landmark registration (for which I recommend the Fiducial registration wizard in the SlicerIGT extension). For images the first way I’d suggest trying is automatic image based registration. For that I think the SlicerElastix extension is your best bet, but there are others like the BRAINS registration, for which you can find tutorials and the registration case library <a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Registration">here</a>.</p>
<p>In your specific case what I recommend is doing a rigid registration of the two CBCTs using SlicerElastix so that the jaws can be assessed in the same frame of reference, then segment (delineate, contour) the lower jaws using Segment Editor (there are tons of material about it in the forum and the documentation), and then find out the spatial relationship of the two segmented jaws.</p>

---

## Post #4 by @joachim (2020-05-08 11:17 UTC)

<p>If you want to learn Slicer, I will recommend you these nice tutorials: <a href="https://github.com/SlicerMorph/W_2020" rel="nofollow noopener">https://github.com/SlicerMorph/W_2020</a>  (under <em>LabXX_Slicer_X</em>). Take a look at <a href="https://github.com/SlicerMorph/W_2020/tree/master/Lab09_Slicer_Scripting#example-1-aligning-volumes-using-landmarks-frankfort-alignment-plane" rel="nofollow noopener">this example</a>.</p>

---

## Post #5 by @Aras_J (2020-05-09 11:14 UTC)

<p>Thank you very much.</p>

---
