# Change default color palette for segmentation

**Topic ID**: 20288
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/change-default-color-palette-for-segmentation/20288

---

## Post #1 by @sronen71 (2021-10-21 16:13 UTC)

<p>When I start a new segmentation in segment editor, and add segments, the default color palette (Color node) is GenericAnatomyColors. How can I tell 3D Slicer to use a different palette (Color node) as default? For example, if I want to use the CartilageMRI Color node as default for all segmentations? Or at least select a set of colors for a single volume ? I saw in old Editor tool, it prompts you to select a set of colors, but this is not the behavior with the Segment Editor. How can I do it?</p>

---

## Post #2 by @lassoan (2021-10-22 18:25 UTC)

<p>We can have a look at how to change the color node shown there by default, but probably we can do better. Can you tell a bit about your segmentation workflow? How many structures do you segment per case? Howe many cases do you need to segment?</p>

---

## Post #3 by @hourglassnam (2022-01-13 08:16 UTC)

<p>Hi,<br>
I have the same question.<br>
The current default colors are too pale for me, and I would like to use a more vibrant color palette as default.<br>
I usually segment 5-10 structures per case.<br>
Is there any update on this matter?</p>

---

## Post #4 by @jamesobutler (2022-01-13 13:10 UTC)

<p>This is a bit related to another thread about Segmentations using simple colors vs Terminology colors. Where simple colors may just be a selection that are vibrant and where 2 segmentations of the same type object are given different colors for uniqueness. However Terminology uses a specific pre-defined color for a type of object being segmented and that same color always being used if segmenting the same object across volumes. Slicer makes users use Terminology colors as the primary option and makes it a bit more difficult to use colors in a simple color usage.</p>
<aside class="quote quote-modified" data-post="1" data-topic="20271">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/simple-color-vs-terminology-color-usage/20271">Simple Color vs Terminology Color usage</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I have found it confusing that 2 similar looking color objects bring up different options. 
First, there is the color selector in a node table such as in this table in the Markups module, but also used in the Segment Editor module and the Data module. 
[image] 
Second, there is this color selector used in various place mode widgets including the markups toolbar 
[image] 
It is confusing that these look the same (square color that can be double-clicked), but bring up different options. The versio…
  </blockquote>
</aside>


---
