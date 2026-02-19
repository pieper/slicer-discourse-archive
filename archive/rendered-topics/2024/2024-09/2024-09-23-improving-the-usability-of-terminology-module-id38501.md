---
topic_id: 38501
title: "Improving The Usability Of Terminology Module"
date: 2024-09-23
url: https://discourse.slicer.org/t/38501
---

# Improving the usability of terminology module

**Topic ID**: 38501
**Date**: 2024-09-23
**URL**: https://discourse.slicer.org/t/improving-the-usability-of-terminology-module/38501

---

## Post #1 by @muratmaga (2024-09-23 16:23 UTC)

<p>I would like to propose a few changes to the behavior of the Terminology Module to increase its usage and adoption.</p>
<ol>
<li><strong>Change the double-click rename behavior</strong>. Currently a segment can be renamed manually by double clicking its name. Given the importance of using proper terms and avoid typos, I suggest we change the behavior such that double clicking the name (or color) will bring the terminology dialog box. If there are no suitable terms to choose from, then the user can actually edit the Name field, as they currently do in the segment editors subject hierarchy. Note that this renaming behavior is already available, and it only add one more click to the process of manually editing a segment name.</li>
<li><strong>To allow recycling of custom names</strong>, create a new button that will add the the current contents of the Name and Color field to the user’s custom terminology. This way user can grow their own terminology terms and color schemes.</li>
<li><strong>Allow creation of custom color tables</strong>: Allow user search and add the terminology to a selection list that can then be exported as a custom color table to convert labelmaps. Label ID are assigned by the order they are added to the list, and user should be able to re-arrange the list.</li>
</ol>
<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @cpinter (2024-09-24 09:06 UTC)

<p>Thanks for bringing up these issues!</p>
<ol>
<li>I think this is fine as long as we have a setting for it in Application Settings. I would only change the default once the new approach has been thoroughly tried and accepted.</li>
<li>Sounds reasonable. You imagine this button to be in the Terminology Navigator dialog right? One issue I see is that the name and color do not fulfill the minimum requirements for a new term (“type”), because the <code>CodingSchemeDesignator</code> and <code>CodeValue</code> fields are not specified (<code>CodeMeaning</code> is the name). Should we take these from the currently selected item? The other issue is that the next thing the user will want is saving the terminology to JSON file, so that feature should be added at the same time. Maybe that could be a new button in the Terminologies module.</li>
<li>Yes this is something that I needed in the past as well. We need to design the GUI so that it does not add too much complexity to the existing widgets.</li>
</ol>
<p>Cross-referencing this issue here: <a href="https://github.com/Slicer/Slicer/issues/6975" class="inline-onebox">Improvements to the Terminologies module. · Issue #6975 · Slicer/Slicer · GitHub</a></p>
<p>So it seems that there are more issues to discuss:</p>
<ol start="4">
<li>Change the default terminology. This could go into Application settings / Segmentations. There is already a default terminology entry selector.</li>
<li>I remember <a class="mention" href="/u/muratmaga">@muratmaga</a> that you also wanted to change the single-click selection in the category selector. It is indeed inconvenient when you have many categories. Also can be confusing to people.</li>
</ol>
<p>There are simple bugs as well, but this list should be enough to discuss.</p>

---

## Post #3 by @muratmaga (2024-09-24 14:46 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="38501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>You imagine this button to be in the Terminology Navigator dialog right?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="38501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>CodingSchemeDesignator</p>
</blockquote>
</aside>
<p>Can be something like “Custom” I imagine.</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="38501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>hange the default terminology. This could go into Application settings / Segmentations. There is already a default terminology entry selector.</p>
</blockquote>
</aside>
<p>I am not sure what this setting is trying to modify. It is asking me to pick up a specific term from a terminology. That’s not what I mean, I want to set a whole category (in this case my Uberon ontology) as default. Alternative is what I suggested, Terminology Navigator remembers the last terminology user interacted and brings that, as opposed to keep defaulting Slicer’s Segmentation category.</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="38501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I remember <a class="mention" href="/u/muratmaga">@muratmaga</a> that you also wanted to change the single-click selection in the category selector. It is indeed inconvenient when you have many categories. Also can be confusing to people.</p>
</blockquote>
</aside>
<p>Thanks for reminding it. I forgot! Yes, a way to choose multiple category selector and turn on/off them is needed. Current behavior of turning them on/off one by one gets really annoying when you have more a few category.</p>

---

## Post #4 by @cpinter (2024-09-24 14:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="38501">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am not sure what this setting is trying to modify. It is asking me to pick up a specific term from a terminology. That’s not what I mean, I want to set a whole category (in this case my Uberon ontology) as default. Alternative is what I suggested, Terminology Navigator remembers the last terminology user interacted and brings that, as opposed to keep defaulting Slicer’s Segmentation category.</p>
</blockquote>
</aside>
<p>Sorry for the confusion. All I said was that since there is already a terminology related setting there, we can add one more selector for the default context. Remembering the last selection would also be reasonable. It would set the same kind of setting I suppose.</p>

---

## Post #5 by @muratmaga (2024-09-24 14:56 UTC)

<p>No, I am really trying to understand what it does. It seems like a potentially useful setting and can be broadly useful in a situation like this, but not clear what to me what it is asking me to do? Here, I am trying to set Uberon as default, but as you can see Select is not activated, and expecting me to click on a term on the right.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c892d3ebc40e581667fa0c217632e3b036edabac.png" data-download-href="/uploads/short-url/sCm4pPmWBDL8OvMwHrE0iAcPRE0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c892d3ebc40e581667fa0c217632e3b036edabac_2_690x493.png" alt="image" data-base62-sha1="sCm4pPmWBDL8OvMwHrE0iAcPRE0" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c892d3ebc40e581667fa0c217632e3b036edabac_2_690x493.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c892d3ebc40e581667fa0c217632e3b036edabac_2_1035x739.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c892d3ebc40e581667fa0c217632e3b036edabac_2_1380x986.png 2x" data-dominant-color="D5E1E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1658×1186 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2024-09-24 15:09 UTC)

<p>Using this setting you can specify what terminology entry should the new empty segments get assigned until you change them. By default it is Slicer terminology / Tissue / Tissue.</p>
<p>Select is not enabled because type selection is None. A valid type needs to be selected here.</p>

---

## Post #7 by @muratmaga (2024-09-25 16:08 UTC)

<p>Now that I understand its function, I agree we need a second setting that will set the default Terminology category for the user. Terminology can be a custom one the user generated manually, or an imported one like Uberon.</p>

---
