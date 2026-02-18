# Segmentation visualization toggle is linked when it should not

**Topic ID**: 19940
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/segmentation-visualization-toggle-is-linked-when-it-should-not/19940

---

## Post #1 by @fedorov (2021-09-30 20:54 UTC)

<p>It appears that toggling visibility of segmentation in slice view toggles all of the viewers, even if the views are unlinked. Is this a bug? I see the same behavior both in latest and stable. If I export segmentation as labelmap, it behaves as I would expect, where with unlinked views just the current view visibility is toggled.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f6ef28f61ca62cf1675a4102fdd91bbaac38a0f.gif" alt="2021-09-30_16-49-16" data-base62-sha1="939MDQY38ACxLWB9OG9asW11ujR" width="586" height="500" class="animated"></p>

---

## Post #2 by @lassoan (2021-09-30 21:07 UTC)

<p>This is the correct and expected behavior for every nodes in Slicer. Only display of volume nodes (scalar and labelmap) in slice views are the exception because of the limitation that you cannot easily display any number of volumes in the same slice view.</p>
<p>You can very easily display nodes only in selected views, by <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data">drag-and-dropping the node from the Data module to the views where you want to see them</a>.</p>

---

## Post #3 by @fedorov (2021-09-30 21:10 UTC)

<p>Thanks for the clarification. I didn’t realize this is the expected behavior.</p>
<p>cc: <a class="mention" href="/u/erikziegler">@erikziegler</a> - I was wrong, strangely, it’s not a bug.</p>

---

## Post #4 by @lassoan (2021-09-30 21:14 UTC)

<p>For consistency, we could remove the segmentation node selector from the view controller (the same way as you cannot show/hide markups or models using the slice view controller). We added segmentations visibility controls there to make transitions from labelmaps easier. However, I’m not sure how often this is used and since it does not have the limitation of volume layers, maybe it is too confusing have these controls there along with volume layer controls.</p>

---

## Post #5 by @fedorov (2021-12-22 21:18 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> sorry, I am removing most of my comment, since I realize it is exactly the same issue.</p>
<p>BUT</p>
<p>According to the documentation here <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view:" class="inline-onebox">User Interface — 3D Slicer documentation</a></p>
<blockquote>
<p>“<strong>Layer visibility</strong> “eye” buttons and <strong>Layer opacity</strong> spinboxes control visibility of segmentations and volumes in the slice view.”</p>
</blockquote>
<p>My interpretation of the above is that it should toggle layer visibility in a single view, not in all views.</p>
<p>Should this bit of the documentation be rephrased? The actual behavior is not what the documentation seems to imply.</p>

---

## Post #6 by @lassoan (2021-12-22 22:29 UTC)

<p>We only added the eye icon to the slice view to keep things more familiar for people when transitioning from labelmap volume to segmentation. Segmentation visibility setting works slightly differently than volume layer selectors, because you can display any number of segmentations in a slice view, while volume display is limited to 2+1.</p>
<p>I see the following options to make things more clear:</p>
<ul>
<li>Option A: Improve documentation. However, I would consider it a failure if users need to read the documentations to figure out how to use the software.</li>
<li>Option B: Remove the segmentation visibility selector from the slice view controllers. We don’t have it for any other nodes than volumes (and we only have that for volumes due to historical reasons). It is much easier to use drag-and-drop from the Data module to choose which node is displayed in which views.</li>
<li>Option C: Make behavior more similar to the layer selectors in that it would only show/hide the segmentation in the current view. I would still not make the behavior exactly the same as for volumes by forcing showing a single segmentation per view, so this would be a partial solution only.</li>
</ul>
<p>I think option B is the best both in term of consistency and simplicity in usage and maintenance, but I’m not sure if users are ready for the change, i.e., if they already use the Data module’s eye icon and drag-and-drop instead of the slice view controllers.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <a class="mention" href="/u/muratmaga">@muratmaga</a></p>

---

## Post #7 by @jamesobutler (2021-12-22 23:52 UTC)

<p>Of course documentation should always be up-to-date with latest functionality and if found to not match then it should be updated.</p>
<p>As it relates to these widgets in the Slice Controller:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6287cd86860aa629d61e22eb981064ad6149478b.png" data-download-href="/uploads/short-url/e3DKoATEFVsPoXWW1dssSvDsWmv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6287cd86860aa629d61e22eb981064ad6149478b.png" alt="image" data-base62-sha1="e3DKoATEFVsPoXWW1dssSvDsWmv" width="690" height="191" data-dominant-color="F1EBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">702×195 11.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>I take advantage of volume selection in the slice controller for picking between foreground and background and often swapping volumes between the two layers to change which volume extent is used. I think I use this the most in the Slice Controller because I haven’t discovered how else to change foreground/background volume specification in the GUI. Is this the only place?</li>
<li>I can’t say I have ever used the “labelmap” layer of widgets. This may be because I always use volume nodes or segmentation nodes. It’s unclear to me why labelmap would be needed if these 2 options already exist. For me, the labelmap appears prominent in Slicer, but a waste of space to me.</li>
<li>For the “Segmentation” layer, I have also never used these widgets. I think because I’m typically in the Segment Editor module or Data module and there are easy ways there to toggle the visibility on/off. I find that setting visibility for a given slice viewer is not my primary use. My primary use is to show a segmentation/volume/etc to be visible in all slice views. It would be a more advanced use case for me to only display it in a single slice view but not another. This more advanced use case being a “Compare” type workflow however single individual viewing is my primary workflow.</li>
<li>The widget I like the best in the set of Segmentation widgets is the one that toggles outline/fill etc. I would use this more if it was present in the “Segmentations” module in the display section at minimum, but also in the “Segment Editor” module as well.</li>
<li>I find it difficult to toggle Segmentation node and individual segment visibility in the two comboboxes of the slice controller. It is a lot of clicks to toggle visibility on/off for multiple objects. It is quicker and easier from the “Segment Editor” module or the “Data” module. <strong>Therefore I would be fine with Option B as well.</strong></li>
</ul>
<p>I hope some of my thoughts here are helpful as part of gathering user behavior related to the Slice Controller to make everything easier for new users.</p>

---

## Post #8 by @fedorov (2021-12-23 02:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is the correct and expected behavior for every nodes in Slicer. Only display of volume nodes (scalar and labelmap) in slice views are the exception because of the limitation that you cannot easily display any number of volumes in the same slice view.</p>
</blockquote>
</aside>
<p>I have to say that I am still struggling to understand why per-slice toggle is not possible. I followed the steps, and if I drag a segmentation from Data module list to a slice viewer, and after that toggle segmentation visibility it toggles in a single view. But then I dragged it into other views, and it seemed to be toggling in all views. And I could not figure out how to remove a segmentation from a specific view if I no longer want it to be visible.</p>
<p>I am definitely biased, but I think toggle behavior for labelmap was very intuitive, and didn’t require reading any documentation to understand. Therefore, <strong>my preference is Option C</strong>.</p>
<p>Would be great to hear thoughts from other users.</p>

---

## Post #9 by @muratmaga (2021-12-23 02:41 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>And I could not figure out how to remove a segmentation from a specific view if I no longer want it to be visible.</p>
</blockquote>
</aside>
<p>You need to use the segmentation module, and expand the advanced option<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b729f8b13ee0aa463e4bb96be2aa0a838c45119b.png" data-download-href="/uploads/short-url/q8liDc3hrqMSpwfPb9DaowbT7qX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b729f8b13ee0aa463e4bb96be2aa0a838c45119b_2_412x500.png" alt="image" data-base62-sha1="q8liDc3hrqMSpwfPb9DaowbT7qX" width="412" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b729f8b13ee0aa463e4bb96be2aa0a838c45119b_2_412x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b729f8b13ee0aa463e4bb96be2aa0a838c45119b_2_618x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b729f8b13ee0aa463e4bb96be2aa0a838c45119b_2_824x1000.png 2x" data-dominant-color="EDF0F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">869×1054 25.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @fedorov (2021-12-23 02:46 UTC)

<p>Yes, I looked around more and found it.</p>
<p>Wouldn’t it be helpful if the eye button corresponding to the segmentations layers toggled visibility of all segmentations in the selector below</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d02c47a4236d0ba5f61dc0e2fd62cd27122d780.png" alt="image" data-base62-sha1="dgOkIaUIUxfYeuxgbZBpocJxxOo" width="558" height="284"></p>
<p>either in the current slice (if slice views are unlocked) or in all slices otherwise?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f111c21b95f0c24e47b631c57801df1cc2747ac9.png" alt="image" data-base62-sha1="yoB7gAixeMmTWWSg7ULcklotjHr" width="162" height="126"></p>

---

## Post #11 by @muratmaga (2021-12-23 02:51 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="10" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Wouldn’t it be helpful if the eye button corresponding to the segmentations layers toggled visibility of all segmentations in the selector below</p>
</blockquote>
</aside>
<p>It would be probably helpful. However, given models, markups, volumes are set this way (from their specific module) I didn’t find it very confusing. Just quite buried (like the others).</p>
<p>I am wondering if it would be useful to do all of this in a ‘data visibility’ module to control all these different data types using the same interface in the same place (as opposed to use the Advanced tabs of each module). Maybe even have it under the data module somehow.</p>

---

## Post #12 by @lassoan (2021-12-23 02:56 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I am still struggling to understand why per-slice toggle is not possible</p>
</blockquote>
</aside>
<p>It is possible, but the behavior would still not the same as the label layer selector, because that automatically hides the previously displayed label, which we don’t want to do for segmentations.</p>
<p>Dragging to views works the same way for all nodes: if you drag a node from the Data module to a view then it is displayed in that view only (or that view group, if the views are linked). You can reset these per-view display settings in the right-click menu of the eye icon in Data module.</p>
<p>We could add a checkable view list to the right click menu of the eye icon, if you think that would help.</p>
<p>When we implement proper slice displayable managers for volumes so that we can display any number of volumes in a slice view (probably within a few years) then the layer selectors will need to go anyway. So we are looking for improving usability of the layer selectors in the short/mid term. As a long term solution, I like the way how ParaView does it: the eye icon in the Data tree only adjusts the visibility of the node in the view that has the focus (when you click on a view it gets the focus, which is indicated by a highlight of the border).</p>

---

## Post #13 by @cpinter (2021-12-23 16:35 UTC)

<p>I agree with each and every point of <a class="mention" href="/u/jamesobutler">@jamesobutler</a> , that’s exactly how I use these features too. But we are Slicer dinosaurs, quite set in our ways. If we had to change the UI I’d probably remove this row from the controller to reduce confusion, however, it can be convenient for some users, so I’d vote for <strong>Option A</strong>.</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I am still struggling to understand why per-slice toggle is not possible</p>
</blockquote>
</aside>
<p>Historical reasons… we have been struggling with this division for many years now, that the volumes and all the rest of the data are shown in a different way. Volumes can only be shown in 2D as the foreground or background of the slice views, and these are exclusive, and quite rigid, thus the link views feature was necessary etc. Any other type, however, model, markup, segmentation, or anything else is “just shown”, so shown in all views or not shown, and per-view visibility is a quite special feature where you need to have multiple display nodes for the same data node telling each view whether the node is visible in that view or not (please note that volume nodes are so different this is done via a different mechanism there).</p>
<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>When we implement proper slice displayable managers for volumes so that we can display any number of volumes in a slice view (probably within a few years) then the layer selectors will need to go anyway.</p>
</blockquote>
</aside>
<p>Yes, this will be the ultimate solution. Until then, we can just balance between familiar and 100% correct. Because as you, Andriy, found out, although the familiar feature is there, it works slightly differently. If we remove it, many people will be looking for it. If we implement the per-view feature there, it would be an unproportinally large time investment from developers (at least that’s what I think), and it would then mess up the display nodes (creating multiple ones), which, I suspect, will lead to even larger issues. I’d say fix up the documentation and focus on the ultimate solution.</p>

---

## Post #14 by @lassoan (2021-12-23 17:46 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="13" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>it would then mess up the display nodes (creating multiple ones)</p>
</blockquote>
</aside>
<p>One display node can manage selective display in certain views, so we would not need to add more display nodes. But it would certainly take more effort than adding some clarifications to the documentation.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> after you have tried drag-and-drop for selecting what nodes are displayed in which views, do you still want to use the slice view controllers for this?</p>

---

## Post #15 by @fedorov (2021-12-23 18:17 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="13" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>although the familiar feature is there, it works slightly differently</p>
</blockquote>
</aside>
<p>I personally would not say it works slightly different. It just looks like a bug. To me, the reason for updating the documentation is to explain the behavior, not help discover a feature of the UI.</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="12" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I am still struggling to understand why per-slice toggle is not possible</p>
</blockquote>
</aside>
<p>It is possible, but the behavior would still not the same as the label layer selector, because that automatically hides the previously displayed label, which we don’t want to do for segmentations.</p>
</blockquote>
</aside>
<p>Sorry, I am really slow to get this. In the above, I don’t understand what you mean by “the behavior would still not the same as the label layer selector, because that automatically hides the previously displayed label, which we don’t want to do for segmentations”. I am not suggesting to revise the behavior of the selector, but just the eye button, to toggle visibility of all segmentations/segments in the given view, when views are not linked.</p>
<p>Right now, toggling visibility of a segmentation per-view is already possible via “Segmentations &gt; Advanced &gt; Views”. That’s why I thought implementation of the per-slice visibility toggle would not require any major development work. I didn’t realize it requires significant effort, which I agree is not justified.</p>
<aside class="quote no-group" data-username="lassoan" data-post="14" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/fedorov">@fedorov</a> after you have tried drag-and-drop for selecting what nodes are displayed in which views, do you still want to use the slice view controllers for this?</p>
</blockquote>
</aside>
<p>I personally would like to, because otherwise I need to go to Segmentations module to do this. But given there is no interest from other users, and this would be a major development effort, it is not important.</p>
<p>I was just trying to understand what’s going on. Sorry for taking your time with these back and forth.</p>

---

## Post #16 by @lassoan (2021-12-23 23:42 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="15" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I personally would like to, because otherwise I need to go to Segmentations module to do this.</p>
</blockquote>
</aside>
<p>You don’t need to go to Segmentation module - you can set up most commonly needed visualizations without switching modules, just using the Data module.</p>
<p>For example, from the tree in Data module, you can drag-and-drop any node to any view. It makes the node show up only in the view(s) the node has been dragged into. You can reset this selective display by right-clicking on the eye icon and choosing “Show in all views”.</p>

---

## Post #17 by @muratmaga (2021-12-24 16:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For example, from the tree in Data module, you can drag-and-drop any node to any view. It makes the node show up only in the view(s) the node has been dragged into. You can reset this selective display by right-clicking on the eye icon and choosing “Show in all views”.</p>
</blockquote>
</aside>
<p>But you can’t set per slice view in the Data module. If you want one segmentation in yellow slice and another in green. I don’t think that’s possible without the segmentations module. Am I mistaken? That’s what I think <a class="mention" href="/u/fedorov">@fedorov</a> wants/needs…</p>

---

## Post #18 by @lassoan (2021-12-24 16:37 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="17" data-topic="19940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But you can’t set per slice view in the Data module. If you want one segmentation in yellow slice and another in green. I don’t think that’s possible without the segmentations module.</p>
</blockquote>
</aside>
<p>You certainly can! Drag-and-drop the segmentation from the data tree to the views that you want to appear in. No need to use the segmentations module for this.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data"><img src="https://github.com/Slicer/Slicer/releases/download/docs-resources/drag_to_view.gif" alt="" role="presentation" width="" height=""></a></p>

---

## Post #19 by @muratmaga (2021-12-24 16:46 UTC)

<p>Himm, I always assumed that when I drag and drop the segmentation it showed in all slice views, but apparently not.</p>
<p>This is nice…</p>

---

## Post #20 by @lassoan (2021-12-24 16:49 UTC)

<p>If views are linked then drag-and-drop into a view displays the node in all the views in the view group. Otherwise it just shows the node in that specific view.</p>
<p>You can use this to set up contents of views in a few seconds, with any nodes (volumes, models, markups, segmentations, …), without switching between modules.</p>

---
