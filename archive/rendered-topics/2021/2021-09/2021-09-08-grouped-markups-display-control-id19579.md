---
topic_id: 19579
title: "Grouped Markups Display Control"
date: 2021-09-08
url: https://discourse.slicer.org/t/19579
---

# Grouped markups display control

**Topic ID**: 19579
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/grouped-markups-display-control/19579

---

## Post #1 by @muratmaga (2021-09-08 18:26 UTC)

<p>Often, I need to visualize a group of markups together for comparison and need I way to control their display properties jointly via UI.</p>
<p>If we are to take on this, what would be the more straightforward way of implementing this behavior? Having a folder created by the user and all nodes to be control are moved inside, and in the markups window, the display is enabled for this folder level (which applies to all nodes inside it).</p>
<p>Or highlight the individual markups and develop a right-click action that will say something like “group display properties” and then whichever one is changed it applies to all the nodes within the group.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c7f07a8bb028b9bce1145fe72847d8762a20c2c.png" alt="image" data-base62-sha1="k2T0nRuq3AIOp0x6TgSfRxWFX5i" width="567" height="438"></p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>

---

## Post #2 by @jamesobutler (2021-09-08 18:35 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="19579">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Having a folder created by the user and all nodes to be control are moved inside, and in the markups window, the display is enabled for this folder level (which applies to all nodes inside it).</p>
</blockquote>
</aside>
<p>This reminds of related discussion about should a folder in the subject hierarchy be able to control display states of all things that are under it. Also discussed as <a href="https://github.com/Slicer/Slicer/issues/4961" class="inline-onebox" rel="noopener nofollow ugc">Controlling visibility of volume node children in subject hierarchy · Issue #4961 · Slicer/Slicer · GitHub</a>. Node visibility is a display property just like markup display visibility or markup color etc.</p>
<aside class="quote quote-modified" data-post="1" data-topic="17582">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/subject-level-visibility-button-works-only-partially/17582">Subject Level visibility button works only partially</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    It appears that setting the visibility off in subject level does not hide volume in slice views. To replicate: 

Download and render MRHead.
Create a single fiducial on MRHead 3D view.
Center the slice views on fiducial
create a new subject and nest both MRHead and fiducial node beneath it.
Turn off the visibility for the subject level and observe that all 3D views are turned off, as well as visibilty of fiducial in 2D view, but the volume in slice views remains visible.

Replicated in latest st…
  </blockquote>
</aside>

<p>I think this type of discussion will need to continue as there seemed to be many things to consider. For example a folder as shown in the subject hierarchy could contain nodes of a single type as shown, but it could also contains other nodes such as volume nodes.</p>

---

## Post #3 by @muratmaga (2021-09-08 18:40 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="19579">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I think this type of discussion will need to continue as there seemed to be many things to consider. For example a folder as shown in the subject hierarchy could contain nodes of a single type as shown, but it could also contains other nodes such as volume nodes.</p>
</blockquote>
</aside>
<p>While I would like to a general purpose method that applies to the other nodes (volumes, models, volume rendering) to control their disply settings, i think that will be too big. At the moment I would like to achieve this only for markups.</p>

---

## Post #4 by @lassoan (2021-09-08 19:00 UTC)

<p>This feature is already implemented for visibility, opacity, and color. Visibility and opacity of markups is already filtered by visibility and opacity of the folder display node. Color of the markups is only overridden by the folder display node if “Apply color to all children” option is enabled.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98469dedd2db3d74e417778209239925473a77f7.png" data-download-href="/uploads/short-url/lJ5S2cv2xKAYFowo0IrpOCdSBRJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98469dedd2db3d74e417778209239925473a77f7_2_690x374.png" alt="image" data-base62-sha1="lJ5S2cv2xKAYFowo0IrpOCdSBRJ" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98469dedd2db3d74e417778209239925473a77f7_2_690x374.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98469dedd2db3d74e417778209239925473a77f7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98469dedd2db3d74e417778209239925473a77f7.png 2x" data-dominant-color="BEBFC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1025×557 33.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you want to temporarily override other display properties then the markups widgets need to be updated to take into account information stored in the folder display node.</p>
<p>If you want to override markups-specific display properties then you could add a reference from the folder display node to a markups display node. That markups display node could be a new one or the display node of any markups in the branch.</p>
<p>The GUI for this would be probably menu item(s) in the color context menu (similarly to the “Apply color to all children”). When you select the folder node in markups module, the display properties editor could modify this overriding markups display node.</p>

---

## Post #5 by @pieper (2021-09-09 15:54 UTC)

<p>Another option could be a simple subject hierarchy plugin that would add something like a “Copy to siblings” in the visualization menu so that you could first edit the properties of one fiducial list and then easily apply it to all the others in the folder.  Or if you wanted this to be dynamic/automatic there could be linking modes like for views with observers and so forth.  None is very difficult, but we’d want to get it all working cleanly and decide if we want to prototype in SlicerMorph or add something to the core.</p>

---

## Post #6 by @lassoan (2021-09-09 16:42 UTC)

<p>Changing display properties is certainly much simpler than dynamically overriding them (it could be as simple as enabling multi-select in the node selector tree in Markups module), but it would cause permanent changes in the display node. <a class="mention" href="/u/muratmaga">@muratmaga</a> is permanent change of display properties desirable for your use cases?</p>

---

## Post #7 by @pieper (2021-09-09 17:00 UTC)

<p>Another fairly simple thing to do would be to add a menu item like “Make display preset” which pops up a dialog prompting for a name (default ‘template-%d’) and then these could be added to the folder’s visualization menu to apply to all the contents so you could easily switch among them.  These could also be persisted to the scene.</p>

---

## Post #8 by @muratmaga (2021-09-10 03:12 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="19579">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>is permanent change of display properties desirable for your use cases?</p>
</blockquote>
</aside>
<p>This should be fine. In fact, it think if it wasn’t permanent it would be a bit confusing.</p>

---
