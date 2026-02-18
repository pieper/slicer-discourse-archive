# Preset for masks in segmentation

**Topic ID**: 20414
**Date**: 2021-10-29
**URL**: https://discourse.slicer.org/t/preset-for-masks-in-segmentation/20414

---

## Post #1 by @mohammed_alshakhas (2021-10-29 15:45 UTC)

<p>i would like to suggest putting the option to save presets for MASKS  in segmentation .</p>
<p>i struggle to fine tune a mask with threshold or other effects im using , but the frustrating part is that i need to go back and forth in my segmentation work flow and i guess many other do the same .</p>
<p>however when you go back its so effortful to guess the previous mask setting and i usually used free painting / drawing without mask just because its hard to fine tune again</p>
<p>i wish to to have and mask list or some sort  of preset add . id love the preset add mostly cause my work is limited to certain indication so eventually id use presevious mask</p>
<p>simple example that i always waste time fine tuning is when i pain a hazy cortex , i need to adjust contrast then then use threshold to make a mask. repeatred this step 10s of times and i hope the comminty develop something for it</p>
<p>cheers</p>

---

## Post #2 by @lassoan (2021-10-30 12:54 UTC)

<p>If you need to do a series of actions many times then you may consider defining a keyboard shortcut for it.</p>
<p>For example:</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#change-window-level-brightness-contrast-or-colormap-of-a-volume">adjust contrast</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-segment-editor-effects-from-script-qmrmlsegmenteditorwidget">modify segment editor parameters</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#customize-keyboard-shortcuts">customize keyboard shortcuts</a></li>
</ul>
<p>If you are not sure how to put this all together or how to automate a specific step then let us know.</p>

---

## Post #3 by @mohammed_alshakhas (2021-10-30 19:25 UTC)

<p>First I’d love to find out how to make shortcuts for these actions , however  my main issues isn’t just doing the action but mostly  find the right value for it like find the correct threshold to use again  is time consuming .</p>
<p>By having preset mask the values as well as the action is needed to be saved when I believe to be highly useful for users</p>

---

## Post #4 by @muratmaga (2021-10-30 19:34 UTC)

<p>İf you are having to do a lot of exploration for each dataset, i don’t think presets will be much of use to you. Presets by definition work for best for things that are similar in ranges/intensities. Sound like your datasets are very variable.</p>

---

## Post #5 by @mohammed_alshakhas (2021-10-30 19:40 UTC)

<p>not quite ,<br>
like for example when i segment . i routinely use three or more masks based on threshold  .<br>
i need to go back and forth to define those thresholds . anatomy is not always easy to judge so i require adjusting the contrast before i decide the correct threshold for some .</p>
<p>if i save it as a preset i can just flip back to previous mask and carry on painting segment rather than repeating the work to define the mask .</p>

---

## Post #6 by @lassoan (2021-10-30 20:59 UTC)

<p>You can add a shortcut to save the current settings to your preset list and another shortcut to cycle between saved presets.</p>

---

## Post #7 by @mohammed_alshakhas (2021-11-02 16:50 UTC)

<p>can you please explain hows that can be done ?<br>
thanks</p>

---

## Post #8 by @lassoan (2021-11-02 21:45 UTC)

<p>Can you tell about your progress so far? Have you tried code snippets in the script repository to set window/level of a volume? Have you tried the code snippet that registers keyboard shortcuts?</p>

---

## Post #9 by @mohammed_alshakhas (2021-11-03 06:09 UTC)

<p>I’m a surgeon by trade, so I have no knowledge of coding, I only use UI.</p>

---

## Post #10 by @lassoan (2021-11-16 06:45 UTC)

<p>Maybe you can hire a student or a contract software developer to help you with this. If you just want to have keyboard shortcuts for existing features then probably it is just a couple of hours work for a software developer who has some Python development experience. If you want a module with some nice and convenient graphical user interface then that will take more time and it may worth finding someone who has Slicer development experience.</p>
<p>If you don’t find anyone among people you know then you can ask one of the <a href="https://www.slicer.org/commercial-use.html#commercial-partners">Slicer commercial partners</a> or describe what you need in a topic in the <a href="https://discourse.slicer.org/c/announcements/jobs/22">Jobs category</a> and see if someone contacts you.</p>

---

## Post #11 by @mohammed_alshakhas (2021-11-16 09:58 UTC)

<p>It is not that essential for me .<br>
However this feature is very useful and I found it in more than one software like itk-snap , mimic and proplan .</p>
<p>I hope to see it in slicer one day .</p>

---

## Post #12 by @lassoan (2021-11-16 13:19 UTC)

<p>Maybe I misunderstood something. Where is it in ITK-Snap?</p>

---

## Post #13 by @mohammed_alshakhas (2021-11-20 09:27 UTC)

<p>it is not explicit in ITK - snap but it is in mimics</p>
<p>in ITK snap, the mask specifications threshold and area of editing don’t change. they are  independent.</p>
<p>however, the thing in slicer is that masks are not independent.  for example, if I set threshold for segment A, the threshold  change will stay when I work in segment B. which is not productive</p>
<p>that’s not the case in ITK snap. your mask is completely independent.  whatever you do in a certain mask is saved</p>
<p>in  my work  for example, i need different   thresholds and areas of editing for each<br>
1 soft tissue<br>
2 thick  cortex<br>
3 soft cortex<br>
4 pathology</p>
<p>so it would be great if either I can do custom masks ( presets ) I can use with any segment</p>
<p>or each segment mask becomes independent of the reset, and won’t alter once I move to the next segment and start a new mask.</p>
<p>this will allow me to go back and modify a segment without repeating all the mask editing</p>
<p>i know for an expert those might not be necessary, BUT they can save tons of time for a regular user like myself.</p>

---

## Post #14 by @lassoan (2021-11-20 13:56 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="13" data-topic="20414">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>mask specifications threshold and area of editing don’t change. they are independent.</p>
</blockquote>
</aside>
<p>This is available in Slicer, too. Each segment can be used as a mask. Enable overlapping segments and then create a segment.</p>
<p>You can create soft tissue, thick cortex, soft cortex, pathology segments using Thresholding. Then you can choose one of these segments as “Editable area”.</p>

---

## Post #15 by @pieper (2021-11-20 14:02 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I think what <a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> is pointing out is that in Slicer we have a global editing threshold that is used for all painting operations no matter which segment is selected.  Maybe there should be an option of setting per-segment thresholds.</p>

---

## Post #16 by @mohammed_alshakhas (2021-11-20 18:00 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>  Yes , that’s exactly my point .</p>

---
