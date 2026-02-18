# DeCAL & DeCA —> option for selecting sample basis for reference shape

**Topic ID**: 45075
**Date**: 2025-11-14
**URL**: https://discourse.slicer.org/t/decal-deca-option-for-selecting-sample-basis-for-reference-shape/45075

---

## Post #1 by @MrMarkus (2025-11-14 08:51 UTC)

<p>Dear SlicerMorph team,</p>
<p>would it be possible to add an additional option for the generation of the “mean shape”? For my work, probably for other users too, it would be very useful to be able to choose which shapes should be used for deriving the “mean shape”.</p>
<p>Motivation behind: bunch of CT skull data, two groups to compare, control group vs. group X. In case the skulls of group X are somehow “abnormal” this would for sure strongly influence the shape of the mean skull.</p>
<p>Hence I would prefer to select the control group as the basis for the “mean shape” and in the subsequent step to compare the shape changes of each individual skull of group X with the “mean shape” which was solely derived from the control group.</p>
<p>This would help to detect "minor” shape differences between the skull of the control group vs. the skulls of group X.</p>
<p>In case alle skull would serve as the basis for the “mean shape” I assume that “minor” differences between the “mean shape” and the individual skulls of group X wouldn’t be detectable, since the skulls of group X already contributed to the shape of the “mean shape” skull.</p>
<p>In short: how big are the chances that this option would be integrated in one of the next updates of DeCAL / DeCA?</p>
<p>I would highly appreciate  it !!!</p>
<p>THANKS!</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2025-11-14 15:32 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="1" data-topic="45075">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>In short: how big are the chances that this option would be integrated in one of the next updates of DeCAL / DeCA?</p>
</blockquote>
</aside>
<p>That option is already there. You just need to split the task of atlas creation and analysis in two separate steps.</p>
<p>First use the DecA with your normative samples to create the normal atlas, then use the second time with the full sample, but instead of choosing to create the atlas (default), use load an atlas option and specify the normative atlas you created in the first step.</p>

---

## Post #3 by @MrMarkus (2025-11-17 15:38 UTC)

<p>Thanks your response! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"><br>
That´s a great idea!<img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=15" title=":ok_hand:" class="emoji" alt=":ok_hand:" loading="lazy" width="20" height="20"></p>
<p>Best regards,<br>
Markus</p>

---
