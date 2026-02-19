---
topic_id: 20271
title: "Simple Color Vs Terminology Color Usage"
date: 2021-10-20
url: https://discourse.slicer.org/t/20271
---

# Simple Color vs Terminology Color usage

**Topic ID**: 20271
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/simple-color-vs-terminology-color-usage/20271

---

## Post #1 by @jamesobutler (2021-10-20 19:00 UTC)

<p>I have found it confusing that 2 similar looking color objects bring up different options.</p>
<p>First, there is the color selector in a node table such as in this table in the Markups module, but also used in the Segment Editor module and the Data module.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a35641788b2a8f782f178e553d3f2845b3cd7512.png" alt="image" data-base62-sha1="niWD2OPISVtNjLEWUPnY9EMc6gW" width="542" height="140"></p>
<p>Second, there is this color selector used in various place mode widgets including the markups toolbar<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e8a2a8316ceaf4c5819350038e8a80670cd9058.png" alt="image" data-base62-sha1="8VfCBf7KPhJ563SzRbna4VqFcJa" width="132" height="37"></p>
<p>It is confusing that these look the same (square color that can be double-clicked), but bring up different options. The version in the table brings up a qSlicerTerminologySelectorDialog and the other brings up a simple QColorDialog.</p>
<p><strong>qSlicerTerminologySelectorDialog</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d039f53970b13645f54b50df1e2adf6a225f314.png" alt="image" data-base62-sha1="1R7Y10XKShGp06XU4xGLnpn9F0E" width="306" height="404"></p>
<p><strong>QColorDialog</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1da71a0227e209b4986122ef419b150ed86a8264.png" alt="image" data-base62-sha1="4ejRksdoJRqxDQ2CPLJrRL7EkoQ" width="502" height="417"></p>
<ul>
<li>Does a terminology selector dialog make sense in the context of the Markups module? Would you set markups color primarily based on the terminology? Or is terminology primarily used in the context of segmentations?</li>
<li>Currently it feels like terminology is being forced onto the user first and simple color is the supported secondary option. It would seem to make sense for simple color selection to be the primary first option, with the support for the user to have color selection have more functionality by supporting terminology selection as the advanced option. This may be a QColorDialog is shown first with a button to open up the Terminology selector as the second option if they cannot be combined into a single dialog.</li>
</ul>

---

## Post #2 by @smrolfe (2021-10-20 20:49 UTC)

<p>The terminology selector does not make sense for markups in my use cases.  Also, many of the terminology label colors are dull and for fiducial visibility I prefer brighter colors. I agree with making QColorDialog the primary option.</p>

---

## Post #3 by @jamesobutler (2021-10-21 16:34 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> or <a class="mention" href="/u/lassoan">@lassoan</a> Do you know the history behind color selection in Slicer? Is there a historical reason why terminology color usage is presented as the primary option instead of the simple color option?</p>

---

## Post #4 by @lassoan (2021-10-21 17:05 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Do you know the history behind color selection in Slicer? Is there a historical reason why terminology color usage is presented as the primary option instead of the simple color option?</p>
</blockquote>
</aside>
<p>We got this implementation when we switched from node combobox to subject hierarchy tree and made us realize how much sense it makes, so we kept this behavior.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Currently it feels like terminology is being forced onto the user first and simple color is the supported secondary option.</p>
</blockquote>
</aside>
<p>Yes, I think this is true. It encourages users to consider specifying what the item is, and provide for free spell-checked, translatable, machine-readable, archival-quality name and automatic default color.</p>
<aside class="quote no-group" data-username="smrolfe" data-post="2" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/smrolfe/48/3659_2.png" class="avatar"> smrolfe:</div>
<blockquote>
<p>The terminology selector does not make sense for markups in my use cases</p>
</blockquote>
</aside>
<p>Actually, you would benefit from using terminology selector for landmarking. It would make your templating workflows much more robust if you specified the template, because you would actually know what that template is, instead of trying to deduce it from the landmark points that you have in the markups file.</p>
<p>You can add your own terms by specifying a coding scheme (it could be <code>99SLICERMORPH</code>), code name (displayed name, such as <code>Maga2019 Mouse skull template</code>) and code value (machine-readable, language and spelling independent value, such as <code>TPL-MOUSE-001</code>) triplets in a json file.</p>
<hr>
<p>It seems that the huge advantages of using standard terminology is not obvious to users. Hiding this feature would be easy, but I think we should improve its usability instead. For example, if the user does not find an existing term then we could offer to save it as a new term.</p>

---

## Post #5 by @jamesobutler (2021-10-21 17:25 UTC)

<p>For my workflow I’m usually segmenting the same thing multiple times. If I have multiple subcutaneous tumors in a Volume, I would not want these segments to all have the same color. I care about color for uniqueness as we also have a custom statistics table where the segment name is colored as well for easier matching by color. We don’t have human data or use the DICOM standard, so DICOM standard terminology colors aren’t important to us. We care about the measurement first.</p>
<p>How colors are set up currently it takes more effort to have less information. However I would advocate where more effort should lead to more information where you start with the simplest form of information first. Such as simple color first with the ability to add more terminology information as the secondary option. Terminology requires more effort and time so terminology is something I don’t frequently care about.</p>

---

## Post #6 by @jamesobutler (2021-10-21 20:02 UTC)

<p><a class="mention" href="/u/div">@DIV</a> You mentioned over in the following post, about the clicks to set a basic color for segments.</p>
<aside class="quote quote-modified" data-post="1" data-topic="20236">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segment-editor-reduce-the-number-of-mouse-clicks-to-set-basic-colour-for-segment/20236">Segment Editor: reduce the number of mouse clicks to set basic colour for segment</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    If I wish to set a Basic Color for a segment I need seven mouse clicks (or six operations): 

double-click the relevant swatch for Segment color;
click Color in the (badly named) Slicer dialogue box;
click Basic tab in the Select Color dialogue box;
click a swatch under Basic colors;
click OK in the Select Color dialogue box;
click Select in the Slicer dialogue box. 
That is too many mouse clicks for a basic operation that I regularly perform.

I often have multiple segments representing the sam…
  </blockquote>
</aside>

<p>How do you use colors? What is your use case? Have you used <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/terminologies.html" rel="noopener nofollow ugc">terminologies</a>?</p>

---

## Post #7 by @lassoan (2021-10-22 01:21 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I care about color for uniqueness as we also have a custom statistics table where the segment name is colored as well for easier matching by color.</p>
</blockquote>
</aside>
<p>This is a very specific and reasonable need, which would not be hard to address.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>We don’t have human data or use the DICOM standard, so DICOM standard terminology colors aren’t important to us. We care about the measurement first.</p>
</blockquote>
</aside>
<p>Using coded values instead of random custom strings to describe meaning or content of something is not related to DICOM or human data.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>How colors are set up currently it takes more effort to have less information.</p>
</blockquote>
</aside>
<p>Terminology allows the users to specify more information (coded term, color) with less effort: double-click the terminology selector, start typing what’s there (for example, type <code>mas</code> for mass), hit Enter and you are done.</p>
<p>I see that things should be improved, because if you want to use “tumor” instead of “mass” then it should be trivially easy to create a new term. For example, when you first type “tumor”, Slicer should ask if you want to create a new term from this. Generating unique colors would be important, too.</p>
<hr>
<p>It would be easy to just add an option to the application settings that would allow tucking away terminologies, but I think we can make terminologies work better, so that they would not get in the way and users would understand how it helps them. It could work similarly to how auto-complete works in all modern software.</p>

---

## Post #8 by @mhalle (2021-10-22 01:46 UTC)

<p>The problem described here is a persistent one dating back to the use of color lookup tables.  LUTs associated integer labels, RGB or RGBA colors, and descriptive strings, By locking these three items, the locked three very different concepts together: data description, rendition style, and semantic meaning.</p>
<p>Things are a bit more advanced and flexible with terminologies in Slicer today. The data description piece is now sort of separate (we don’t have to label our models with the same integer labels used in a label map) but the conflation of semantic label and style remains. “Bone” isn’t a color, though in an anatomy atlas bone may have a characteristic color. In such a context, bone and a bone color might be directly mapped. On the other hand, in a population study of livers, each subject’s liver might be uniquely colored. In a lesion study, the lesions might be colored by a quantitative value.</p>
<p>In relational database terms, we might want to join color to a model based on different values such as semantic label or subject ID or lesion volume. We might want to do they do that dynamically for data exploration. Or we might want to do multiple types of joins at once: a base layer that’s an anatomy atlas overlaid with fiducials colored using a different semantic scheme.</p>
<p>As Andras says, semantic labeling using terminologies is very useful. But a richer way to use visual colors or styles to depict information in biomedical visualization is also very useful, as is a broader concept of semantic labeling (for instance, by locally defined fiducial or landmark type rather by some standardized vocabulary). Addressing the issue starts with understanding and disambiguating these different concepts. Then we can build more flexible visualization mechanisms and methods.</p>
<p>By the way, the colors in the default Slicer anatomy color table were created by using a spectrophotometer to measure the colors used in print atlases for various anatomical materials. That’s one reason why the colors are not highly saturated. It was a fun project to create more universally recognizable anatomical atlases, but that’s not the only medical application of Slicer.</p>

---

## Post #9 by @jamesobutler (2021-10-22 02:20 UTC)

<p>I see how using terminology can make things more helpful, but if I don’t want to code a meaning to a color then that shouldn’t be harder than setting a terminology.</p>
<p>A simple color selector of the basic colors like the QColorDialog with a terminology selector below that would be all I would need for a better experience. Currently using terminologies and having that archival information has not been needed for our users. Statistics from longitudinal studies are more important to our users than the archival information. Users are not segmenting multiple objects in a given volume. It’s always the same type of object. They aren’t building up an atlas.</p>

---

## Post #10 by @mhalle (2021-10-22 02:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would be easy to just add an option to the application settings that would allow tucking away terminologies, but I think we can make terminologies work better, so that they would not get in the way and users would understand how it helps them. It could work similarly to how auto-complete works in all modern software.</p>
</blockquote>
</aside>
<p>This application also suggest to me the ability to incorporate, import, or subset multiple terminologies. For instance, a base anatomy or tissue material terminology that is overlaid by a custom specialized terminology.</p>

---

## Post #11 by @jamesobutler (2021-10-22 02:33 UTC)

<p>Additional note about something I’ve done which may honestly be worse than not coding a terminology to a color which is I’ll code the wrong terminology from the terminology list just because it is quick and simple for me to use its color.</p>

---

## Post #12 by @lassoan (2021-10-22 03:41 UTC)

<aside class="quote no-group" data-username="mhalle" data-post="10" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar"> mhalle:</div>
<blockquote>
<p>This application also suggest to me the ability to incorporate, import, or subset multiple terminologies. For instance, a base anatomy or tissue material terminology that is overlaid by a custom specialized terminology.</p>
</blockquote>
</aside>
<p>You can already import and edit multiple terminologies, but you need to edit text (json) files, which is probably not convenient enough. What do you mean by “overlaid by a custom specialized terminology”? Being able to select terms from multiple terminologies?</p>

---

## Post #13 by @DIV (2021-10-25 12:53 UTC)

<p>Hi, James.<br>
As you’ve invited my comment I can let you know my current practice, whilst you keep in mind that it may not be optimal and may not represent the majority of users…</p>
<p>Foremost I care about the colours of the individual segments of a segmentation, and in this there are a few priorities:</p>
<ol>
<li>To readily distinguish one segment from another.  Here I would be more-or-less in line with your earlier statement (quoted below).</li>
</ol>
<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I care about color for uniqueness</p>
</blockquote>
</aside>
<ol start="2">
<li>To provide distinction between a segment and another ‘overlaid’ object.  In the 3D viewing port that would most commonly be a 3D rendering of the volume, but could also be an object imported into the Data structure from an STL file (<em>e.g</em>. somebody else’s earlier attempt at a segmentation of the same feature);  also control points from the Markups module (mostly Fiducial markers).  In the 2D slice viewers of course it would be the DICOM series (which are typically CT scans, which I view in greyscale).</li>
<li>To allow clear visualisation of surface morphology in the 3D view:  some colours seem to me to have more obvious shadows.</li>
</ol>
<p>Besides all of that, I might try to organise colours thematically:  let’s say red, orange and pink for objects imported as STLs, and blue, cyan and green for segments.</p>
<p>I don’t use terminologies, as</p>
<ul>
<li>the audience is generally me;</li>
<li>I don’t segment lots of different types of features (I’m not trying to build an atlas);</li>
<li>I am mainly interested in segmenting one main type of feature (brain aneurysms, with a shortish length of connected arteries).</li>
</ul>
<p>Furthermore — and this may not be an obvious workflow, so I describe it here in some detail — I may have <strong>multiple segments for one single feature</strong>.</p>
<p>For example (1), I might …</p>
<ul>
<li>create a <strong>preliminary segment</strong> based on thresholding;</li>
<li>make a copy of that segment and smooth it by one method;</li>
<li>make a further copy of the original segment and smooth it by a different method;  and</li>
<li>compare the three segments to identify the impact of each smoothing effect and choose the ‘best’ one.</li>
</ul>
<p>For example (2), I might …</p>
<ul>
<li>create a <strong>preliminary segment</strong>;</li>
<li>make a copy of that segment and use the Scissors, Erase, Paint and/or Draw effects to ‘manually’ add/remove voxels;</li>
<li>I can compare the two segments to see the impact of my changes;  and</li>
<li>if at some later stage I decide that the changes weren’t quite right, then the preliminary segment is still available to try again.</li>
</ul>
<p>For example (3), I might …</p>
<ul>
<li>segment the feature using a Threshold effect;</li>
<li>segment the <em>same feature</em> (from scratch) using a Grow from seeds effect;</li>
<li>compare the two segments, and choose the ‘best’ one to export.</li>
</ul>
<p>Hope this helps,<br>
DIV</p>

---

## Post #14 by @mikebind (2021-10-26 05:58 UTC)

<p>I really appreciate the discussion here. For my purposes, I am often trying to display multiple types of information so that it is best communicated through a set of snapshots.  This communication could be aided by using a consistent set of colors in a consistent terminology (which I have not tried to develop yet), so I appreciate that such a capability is present in Slicer. However I am also very often trying to choose colors for visual distinguishability, and since it is not easy to chose a set of ~25-30 colors which are all clearly distinct from each other and clearly distinct from grayscale and clearly distinct from the background of the 3D view, it is not uncommon for me to be trying out different colors for a particular structure or grouping of structures.  The current color selection interface is very tedious for trying out colors just to see how they look.  For example, to change the color for a MarkupsCurveNode in a recent preview release, I have to</p>
<ul>
<li>double-click on the color block in a hierarchy; this brings up a window titled Slicer and lists terminology terms</li>
<li>in this window I have to click on the color block again; this brings up a window titled Select Color and has a color node selector and a list of terminology terms.  I usually just want to use a basic color (because it’s not a bad set of colors and this makes it easier to choose the same color again in the future than specifying a custom color).</li>
<li>to get to Basic colors, I have to click on the tab titled Basic</li>
<li>Then I finally get to select my basic color (one more click)</li>
<li>and click OK (this returns me to the terminology/color selection window titled Slicer)</li>
<li>then I need to click Select, and finally the color I wanted to try out is applied to the curve</li>
</ul>
<p>That is 7 clicks to try out a color.  If I don’t like how that looks, I have to go through another 7 clicks to try a different color. If I want to try out 4 basic colors, that’s 28 clicks.</p>
<p>Of these 7, the last two clicks seem unnecessary.  Why not apply the selected color immediately, while the color selection window is still open? That way, while it would take a few clicks to get to whatever color selection method the user prefers, once reached, one could see the effect of the chosen color before leaving the window.</p>

---

## Post #15 by @jamesobutler (2021-10-26 12:30 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="14" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I am also very often trying to choose colors for visual distinguishability, and since it is not easy to chose a set of ~25-30 colors which are all clearly distinct from each other and clearly distinct from grayscale and clearly distinct from the background of the 3D view</p>
</blockquote>
</aside>
<p>Something in the custom app that we do is we utilize this list of 20 distinctive colors (<a href="https://sashamaps.net/docs/resources/20-colors/" class="inline-onebox" rel="noopener nofollow ugc">List of 20 Simple, Distinct Colors | Sasha Trubetskoy</a>). We order it based on accessibility so the colors that are difficult for those who are color blind are chosen toward the end.</p>

---

## Post #16 by @muratmaga (2021-10-26 14:41 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="14" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>it is not easy to chose a set of ~25-30 colors which are all clearly distinct from each other and clearly distinct from grayscale and clearly distinct from the background of the 3D view,</p>
</blockquote>
</aside>
<p>I use <a href="https://colorbrewer2.org/#type=sequential&amp;scheme=BuGn&amp;n=3">colorbrewer</a> when I need to make sure I choose distinct colors. But unfortunately 25-30 distinct colors are difficult to find whatever you do (either the transition between them will be too gradual or you will be including colors that are not color-blind safe). But for smaller subset (I think it goes up to 12), it worked fine for me. I believe the top number is sort of arbitrary, since it is a cartography tool, I don’t think they need lots of classes like we do.</p>

---

## Post #17 by @mikebind (2021-10-26 15:29 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a>  and <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, I’ve used both of those very helpful resources before to come up with my own colormaps for the 17 or 20 ventricular segments used in nuclear medicine cardiac scans. In the current primary application I am using/developing, there are typically 15-20 stereotactic EEG electrodes (ideally each with their own easily distinguishable color, represented visually by markups curves or by modeled cylinders), plus a color to show which one is currently selected, plus a variety of possible other layers of data including annotations of prior resection cavities, fMRI motor (two sides) or language activation areas, and potentially also overlaid on the multicolored FreeSurfer parcellation.  In my experience, it’s no problem to get to 10-12 colors which show up well against all shades of grayscale and are all clearly distinguishable from one another.  30 is clearly impossible, so in complex cases I find that some color curation is necessary, especially because I’d probably like to use the “best” colors for the most important information, which can vary from case to case.</p>

---

## Post #18 by @pieper (2021-10-26 16:41 UTC)

<p>This is a helpful discussion.  It could make sense to write some modules to customize the color selection as a bulk operation based on high level constraints.</p>
<p>Also as food for thought I’ll point out that we haven’t exposed these rendering options but there are a ton of ways we could increase visual distinctiveness in 2D and 3D rather than just base color.</p>
<p><a href="https://blog.kitware.com/tag/physically-based-rendering/" class="onebox" target="_blank" rel="noopener">https://blog.kitware.com/tag/physically-based-rendering/</a></p>

---

## Post #19 by @DIV (2021-10-27 08:04 UTC)

<aside class="quote no-group quote-modified" data-username="mikebind" data-post="14" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I am also very often trying to choose colors for visual distinguishability, […]</p>
</blockquote>
</aside>
<p>So it seems that wanting distinct colours may be a common wish/requirement.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="15" data-topic="20271" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Something in the custom app that we do is we utilize this list of 20 distinctive colors (<a href="https://sashamaps.net/docs/resources/20-colors/" rel="noopener nofollow ugc">List of 20 Simple, Distinct Colors</a>). We order it based on accessibility so the colors that are difficult for those who are color blind are chosen toward the end.</p>
</blockquote>
</aside>
<p>I had another look back at the existing Basic colour swatches in Slicer.<br>
It may be worth reviewing this to see if a set of ‘optimally distinct’ colours can be provided.<br>
Also, I would prefer to arrange the Basic colours somehow by hue/saturation/value.  Currently there are three fully-saturated red colours (hue=0) of differing value that are not grouped, three fully-saturated green colours (hue=20) of differing value that are not grouped, and three top-valued pink colours (hue=300) of differing saturation that are not grouped, for example.</p>
<p>By way of comparison, my version of Microsoft Word presents 127 standard colour swatches (in <a href="https://websafecolors.info/color-chart" rel="noopener nofollow ugc">websafe</a> R/G/B steps of 00, 33, 66, 99, CC, &amp; FF), including white, plus 15 grey swatches, plus white (<em>again</em>) and black.  All are arranged in a systematic way.<br>
With regard to Slicer, 127 is of course too many colours to be distinct, but using all RGB combinations of R/G/B steps of 00, 7F (or 80), &amp; FF would yield 3³=27 colours (including black, white and medium-grey).  Maybe not <em>optimally</em> distinct, of course, but perhaps not too bad, and having the advantages of being systematic and simple (a.k.a. “Basic”?).  There are very few examples of this set of 27 colours presented online:  here is one, under “<a href="https://color.fandom.com/wiki/Hexadecimal_Chart" rel="noopener nofollow ugc">Priority 3 (27/27 named) and Priority 2 (8/8 named)</a>”.<br>
There’s also an interesting discussion of optimising visual distinctiveness of colours on <a href="https://stackoverflow.com/a/12224359/15273040" rel="noopener nofollow ugc">Stack Overflow</a>.</p>
<p>In any case, it does seem worth considering to include one or more greys among the Basic colours (black and white are already there).</p>
<aside class="quote no-group quote-modified" data-username="jamesobutler" data-post="11" data-topic="20271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>[…] I’ll code the wrong terminology from the terminology list just because it is quick and simple for me to use its color.</p>
</blockquote>
</aside>
<p>I have done this too, once or twice, but I found the colours in the terminology list seemed more muted, and less distinct.  Lots of reddish brown, at any rate, meaning lots of scrolling to find a ‘nice’ colour.</p>
<p>—DIV</p>

---
