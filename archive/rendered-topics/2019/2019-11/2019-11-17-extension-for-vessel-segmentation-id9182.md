# Extension for Vessel Segmentation

**Topic ID**: 9182
**Date**: 2019-11-17
**URL**: https://discourse.slicer.org/t/extension-for-vessel-segmentation/9182

---

## Post #1 by @marie (2019-11-17 21:26 UTC)

<p>Hey there!</p>
<p>I just came across this excellent post:</p><aside class="quote quote-modified" data-post="42" data-topic="1263">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/vmtk-vessel-filtering-not-working/1263/42">VMTK vessel filtering not working</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve described all the steps in this <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/" rel="noopener nofollow ugc">segmentation recipe</a>. Example of segmentation: 
                    <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/image-010.gif" target="_blank" class="onebox" rel="noopener nofollow ugc">
            [image]
          </a>

 
The only “manual” steps needed were choosing a few parameter values, so the whole workflow could be easily made fully automated - requiring only a single click and some optional parameter adjustments from the user.
  </blockquote>
</aside>

<p>This is exactly what I need!! I would really like to develop an extension combining all those steps. Is this possible? I just started reading about developing own modules/extensions and trying some things. I would like to make vessel segmentation easier for people who aren’t familiar with 3DSlicer.</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2019-11-18 21:24 UTC)

<p>I would recommend these tutorials for learning how to create custom modules to automate the vessel filtering method: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials</a></p>

---

## Post #3 by @marie (2019-12-17 22:26 UTC)

<p>Thanks for this helpful link!</p>
<p>I think I’m a bit more familiar with Slicer extensions by now. I created a new scripted module in Python using the Extension Wizard and I figured out how to design the user interface and how this kind of extension is working in general.<br>
So, to start with an easier project, I’m trying the following:</p>
<ul>
<li>work on a chosen input volume</li>
<li>use threshold (IsoData) to create a segment</li>
<li>split segment into islands</li>
<li>chose resulting segment(s) and export as stl<br>
(This is already working well for vessel-segmentation with high-contrast MRI.)</li>
</ul>
<p>Anyway, I still don’t know how to use the Segment Editor functionality in my own extension. Is there an easy way? I still have problems understanding the slicer module hierarchy…</p>
<p>Thanks for your help!</p>

---

## Post #4 by @lassoan (2019-12-18 01:24 UTC)

<aside class="quote no-group" data-username="marie" data-post="3" data-topic="9182">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/bc8723/48.png" class="avatar"> marie:</div>
<blockquote>
<p>Anyway, I still don’t know how to use the Segment Editor functionality in my own extension. Is there an easy way?</p>
</blockquote>
</aside>
<p>See examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---
