# "Sticky" settings for sphere brush and editable intensity range

**Topic ID**: 13938
**Date**: 2020-10-08
**URL**: https://discourse.slicer.org/t/sticky-settings-for-sphere-brush-and-editable-intensity-range/13938

---

## Post #1 by @hherhold (2020-10-08 16:48 UTC)

<p>Often when I’m doing manual segmentation, I will use sphere brush when painting but not when erasing. I’ll also have Editable intensity range turned on when painting or using scissors but off when using Islands (remove selected) or erase.</p>
<p>I’ve often thought it would be nice for these settings to “stick” to tools - for example, editable intensity range switches automatically from on to off depending on what tool is selected.</p>
<p>Would this be generally useful? I’m happy to look into implementing it if there is interest. Users would be able to enable/disable this “sticky” behavior, I’m not proposing it be the new default.</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-10-08 17:06 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="13938">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>I’ve often thought it would be nice for these settings to “stick” to tools - for example, editable intensity range switches automatically from on to off depending on what tool is selected.</p>
</blockquote>
</aside>
<p>I think more often than not you want masking settings to be shared between all effects and not “stick” to tools. It is already quite hard to pay attention to set the right masking settings and making them change when you switch between effects would make it hopelessly overcomplicated for most users.</p>
<p>However, there can be certainly use cases in that you would want to switch between various masking settings. I’m not sure how this could be made generally available without making the already busy GUI even more complicated. Do you have any ideas how could it be possible? Would the ability to save masking settings (by assigning a name) and restore masking settings by selecting the name from a combobox help?</p>

---

## Post #3 by @hherhold (2020-10-08 17:13 UTC)

<p>Well, what I’ve wound up doing is using Shortcut keys and assigning them to programmable buttons on my mouse or drawing pad. I hit space + ‘i’ to switch between scissors and islands and turn on/off intensity range about 50 times per hour. About the only thing missing from this workflow is adding in a shortcut key for turning on and off sphere brush, which I’ve figured out how to do but not done it yet as it’s in the C++ part of the codebase.</p>
<p>This has been a perfectly useable workflow for me, so if most people prefer keeping masking settings between tools, I’m not one to rock the boat.</p>

---

## Post #4 by @lassoan (2020-10-08 17:15 UTC)

<p>Defining keyboard shortcuts for composite operations (switch between effects and various effect and masking options) is a good approach. You can change all effect parameters from Python, regardless of the effect is implemented in Python or C++. You can find list of effect parameter names <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#effect-parameters">here</a>.</p>

---
