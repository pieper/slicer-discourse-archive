---
topic_id: 19208
title: "Organization Of Segment Editor Effects Into Categories"
date: 2021-08-16
url: https://discourse.slicer.org/t/19208
---

# Organization of Segment Editor effects into Categories

**Topic ID**: 19208
**Date**: 2021-08-16
**URL**: https://discourse.slicer.org/t/organization-of-segment-editor-effects-into-categories/19208

---

## Post #1 by @jamesobutler (2021-08-16 13:21 UTC)

<p>I have created a Slicer PR with some changes that puts Segment Editor effects into categories to improve usability so that users have a better understanding of the types of segment editors effects. This is implementing a brainstormed idea by <a class="mention" href="/u/umesh_persad">@Umesh_Persad</a> and <a class="mention" href="/u/lassoan">@lassoan</a> in Based on <a href="https://discourse.slicer.org/t/segment-editor-user-interface-improvements/9029" class="inline-onebox">Segment Editor User Interface Improvements</a>. This PR currently doesn’t address all improvements to Segment Editor layout as mentioned in that previous discourse thread, but address a single enhancement of placing segment editor effects into categories. I forsee a new category being “Automatic” that is more AI based. What do you all think?</p>
<p>There is obviously more vertical space being used with different categories on their own row, however it is in the name of usability/understanding. A long list of effects as it is now is often intimidating about knowing which one to use. It frequently requires using them all to understand what they do, but I know some people that take the approach of not trying things out because they are afraid of messing something up. They want to know more about an effect before they commit to clicking it.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5799">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5799" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5799" target="_blank" rel="noopener nofollow ugc">ENH: Segment Editor effects placed into categories</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:segment-editor-organization</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-08-16" data-time="03:29:06" data-timezone="UTC">03:29AM - 16 Aug 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 46 additions and 10 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5799/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+46</span>
          <span class="removed">-10</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This PR aims to improve understanding of different segment editor effects by pla<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5799" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">cing them into categories.

Based on original planning from @upersad and @lassoan at https://discourse.slicer.org/t/segment-editor-user-interface-improvements/9029

| Current | This PR |
|----------|---------|
|![image](https://user-images.githubusercontent.com/15837524/129507731-97dabd1e-0807-42d8-bbd8-48c621c5a7a4.png)|![image](https://user-images.githubusercontent.com/15837524/129507234-9fccc85a-3a46-4cdb-b10c-1cc700f96de0.png)|</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<div class="md-table">
<table>
<thead>
<tr>
<th>Current</th>
<th>This PR</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="https://user-images.githubusercontent.com/15837524/129507731-97dabd1e-0807-42d8-bbd8-48c621c5a7a4.png" alt="image" width="424" height="500"></td>
<td><img src="https://user-images.githubusercontent.com/15837524/129507234-9fccc85a-3a46-4cdb-b10c-1cc700f96de0.png" alt="image" width="372" height="499"></td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @jamesobutler (2021-08-16 15:43 UTC)

<p>The “Uncategorized” effects are to represent what non-Slicer core effects might look like if they don’t have a category defined for them yet. These are currently those from the “SegmentEditorExtraEffects” extension.</p>
<p>If categorization is desired:</p>
<ul>
<li>Do we limit the number of categories to a few + an other/uncategorized? Or could an extension define 5 new effects that add 5 new categories? I currently have provided the category in a hardcoded manner in the PR, but could define the category in the effect file instead.</li>
</ul>

---

## Post #3 by @muratmaga (2021-08-16 16:10 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> thanks for taking on.</p>
<p>With this row-wise organization, where would be the current masking/editable field? For example if I click Threshold, would it popup right below the threshold and above Global row? If not, I don’t think this would be very usable arrangement.</p>
<p>Couple other comments (not for this specifically, in general). Our effect buttons are too big. That’s mostly because of the the names are also included in the button (look at the size of Fill Between Slices, Logical Operations). If we think icon only buttons do not easily explain what the function is, let’s remove the icons and only have the labels as multi line. For non-english localizations this will require creating the buttons in the native language, but probably that’s not a big thing.</p>
<p>If this is not viable, can we remove the text from the buttons, and only show up when it is hovered over?</p>
<p>Plus, the wide buttons causing the width of the module panel to increase automatically, which is I find it a very disturbing behavior.</p>
<p>If we make buttons smaller, I think this will open up a way to create a reasonably sized toolbar that will have most of the functionality of Segment Editor contained (similar to what <a class="mention" href="/u/smrolfe">@smrolfe</a> is doing for markups).</p>

---

## Post #4 by @jamesobutler (2021-08-16 16:47 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="3" data-topic="19208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Our effect icons are too big. That’s mostly because of the the names are also included in the icons (look at the size of Fill Between Slices, Logical Operations).</p>
</blockquote>
</aside>
<p>I think in most cases you mean that the effect buttons can be too large at times (not the icon). This being because the text in the button makes it larger rather than the icon.</p>
<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="3" data-topic="19208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If this is not viable, can we remove the text from the icons, and only show up when it is hovered over?</p>
</blockquote>
</aside>
<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="3" data-topic="19208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If we think the actual icons do not easily explain what the function is, let’s remove the icons and only have the labels as multi line.</p>
</blockquote>
</aside>
<p>I do think the icons do provide some information about what the effect does, but not all the necessary information and neither does the name. The effect buttons already shows a hover tooltip that is the segment effect name, so if we want to enforce equal size segment editor effect buttons by way of equal size icons with no text shown below, then that could be possible. Other applications with various tools for image annotating, usually use an icon only, with the hover tooltip detailing both the name of the effect and also a short description of the tool. The addition of a short description in the tooltip could help if the text was removed from the segment effect button.</p>
<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="3" data-topic="19208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Plus, the wide icons causing the width of the module panel to increase automatically, which is I find it a very disturbing behavior.</p>
</blockquote>
</aside>
<p>Note that this actually happens not due to the effect button size, but rather the effect options. A specific effect options can be larger in width than others which causes the module panel to increase when it is selected. I’m not addressing that in this PR, but that is another issue that was brought up for general segment editor improvements.</p>

---

## Post #5 by @muratmaga (2021-08-16 16:51 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="19208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I think in most cases you mean that the effect buttons can be too large at times (not the icon). This being because the text in the button makes it larger rather than the icon.</p>
</blockquote>
</aside>
<p>Exactly. Sorry for mixing them up! [Edited the original post]</p>

---

## Post #6 by @jamesobutler (2021-08-16 17:01 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="19208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>With this row-wise organization, where would be the current masking/editable field? For example if I click Threshold, would it popup right below the threshold and above Global row? If not, I don’t think this would be very usable arrangement.</p>
</blockquote>
</aside>
<p>Currently the positions within Segment Editor are all still the same. This PR is changing positions of effects within the current location of the segment effects.</p>
<p>If you want masking options moved below say “Threshold” effect button, then that would also mean that masking options would now be above the effect options. Currently all effects are in a stacked widget with the appropriate page selected based on the selected effect.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c95a9766ed33a9ccc6aac390f23581962f10778e.png" data-download-href="/uploads/short-url/sJg3ThTWIf49yNkBrtx4IMCnSxg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c95a9766ed33a9ccc6aac390f23581962f10778e_2_284x500.png" alt="image" data-base62-sha1="sJg3ThTWIf49yNkBrtx4IMCnSxg" width="284" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c95a9766ed33a9ccc6aac390f23581962f10778e_2_284x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c95a9766ed33a9ccc6aac390f23581962f10778e_2_426x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c95a9766ed33a9ccc6aac390f23581962f10778e_2_568x1000.png 2x" data-dominant-color="F0E6E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">628×1102 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2021-08-16 17:07 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="6" data-topic="19208">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>If you want masking options moved below say “Threshold” effect button, then that would also mean that masking options would now be above the effect options.</p>
</blockquote>
</aside>
<p>Sorry what I meant both the “effect options” and “Masking” to be opened right below the selected effect.</p>

---

## Post #8 by @jamesobutler (2021-08-16 17:12 UTC)

<p>If both of those opened directly below the effect, then I would have further to travel if I wanted to go the “Watershed” effect next as all other categories and effects below would get pushed below the effect options and masking.</p>

---

## Post #9 by @muratmaga (2021-08-16 17:26 UTC)

<p>Yes, but they would be in a place that would link the user actions to the effect.</p>
<p>I still think the major improvement will come from reorganizing the buttons to take up much less space, so that we can develop a toolbar where the effects and a segmens are shown, and these tool specific settings are displayed in the module bar.</p>

---

## Post #10 by @jamesobutler (2021-08-16 17:38 UTC)

<p>I actually would be against development towards more actions in the toolbar and rather implement functionality into a ribbon interface.  A toolbar is putting functionality on one row, but I don’t think segment editor can be put into such limited space.</p>

---

## Post #11 by @muratmaga (2021-08-16 17:53 UTC)

<p>is ribbon interface a possibility with QT? If so, I agree it makes sense…</p>
<p>The toolbar I envision is unlikely to have the full functionality of the module, but helps to reduce the clutter within the module view so that we don’t have to scroll up and down in the module panel.</p>

---

## Post #12 by @jamesobutler (2021-08-16 18:14 UTC)

<p><a class="mention" href="/u/umesh_persad">@Umesh_Persad</a> did prototype a ribbon based interface. Ribbon based interface essentially uses a QTabWidget.</p>
<aside class="quote quote-modified" data-post="22" data-topic="9029">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segment-editor-user-interface-improvements/9029/22">Segment Editor User Interface Improvements</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Here is the ribbon simulation with Slicer Designer and buttons. I would need to get the icons. 
[Ribbon%20light%20mode] 
[ribbon%20dark%20mode]
  </blockquote>
</aside>

<p>As it relates to this topic of organizing segment editor effects into categories, do you think that is helpful for improving understanding about the type of effects? Is the increase in number of rows for each category a deal breaker for you because the effect options for say the “Manual” category of effects are now farther away than they are currently?</p>

---

## Post #13 by @muratmaga (2021-08-16 18:31 UTC)

<p>I am just not sure if category adds a meaningful level of understanding of effects. These are all standard image operation effects (with slight difference such as islands vs connected components). Anybody who has used a 3D image processing software before will know what they do. Anybody who is starting anew, will have to experiment on each of those tools.</p>
<p>Also when I read global, I may interpret that the outcome of that operation will overwrite all other existing segments (which is true by default, but not so much if allow overlap is selected).</p>
<p>I appreciate the effort, and hopefully will be useful, but I am concerned this will make the segment editor module panel vertically too long. It is already too long, and we are proposing to add more rows.</p>

---

## Post #14 by @rbumm (2021-08-16 18:59 UTC)

<p>This is an interesting approach, what about using tabs to save space?<br>
I think the categories may confuse the user more that they help.<br>
I am working with Pixinsight a lot, an astronomical image processing software,  and I very much like it´s  functionality to choose effect windows from a menu, see all the effect options in an big and well tooltiped options window, “throw” the effect onto a astro image or “draw” the effect option window as icon onto the Pixisight desktop. A geat way to define your workflow by ordering and moving around the icons, opening the effects on demand and throwing them onto the image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/aced83e1175c05b131e3e6d2aad18ea5ef468ea9.jpeg" data-download-href="/uploads/short-url/oFMZVkLTxGf2sy5zMcfiZgHiYqd.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aced83e1175c05b131e3e6d2aad18ea5ef468ea9_2_690x388.jpeg" alt="image" data-base62-sha1="oFMZVkLTxGf2sy5zMcfiZgHiYqd" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aced83e1175c05b131e3e6d2aad18ea5ef468ea9_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aced83e1175c05b131e3e6d2aad18ea5ef468ea9_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aced83e1175c05b131e3e6d2aad18ea5ef468ea9_2_1380x776.jpeg 2x" data-dominant-color="6A686C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @mikebind (2021-08-16 20:58 UTC)

<p>I appreciate the attempt to simplify. However, I also agree that it is not clear that grouping into categories will be very helpful.  It takes effort to understand exactly what each effect is and how it works, as well as things like how each effect interacts with masking settings and what options there are within each effect. For me, access to the complexities of all of these options is one of the reasons I find Slicer to be the best tool I work with. Grouping the effects into a few categories would not help me.  For new users, I also think general categories like the ones listed might be more confusing than not. “Threshold” seems like a “Global” effect, more so than “Margin”, for example.</p>
<p>To save space, what if the segment table and effects areas were (separately) collapsible, and when collapsed, showed the currently selected segment and currently selected effect? When one wanted to change effects or change selected segment one would expand the section and select.</p>
<p>On another topic that has been discussed here, I like having the text labels on the effect buttons.  It is much easier for me to remember the tool by the name than by the icon.  If the text label was gone, I would likely need to hover over icons to remember what they were, which would be a much more tedious process than glancing through the labels.</p>

---

## Post #16 by @lassoan (2021-08-16 21:05 UTC)

<p>I agree that it is currently hard to locate effects and it would be great to improve this. Large size of the Segment editor module GUI is a problem, too, because it forces the user to scroll a lot. We would need layout improvements that address both issues.</p>
<p>Introducing rows and large category labels would help with finding effects, but it would uses much more space, so we would need to scroll a lot more.</p>
<p>I quite like the vertical toolbar shown <a href="https://discourse.slicer.org/t/change-segment-editor-button-layout/18343/4">here</a>. We could probably have two columns, if needed. It would be a regular toolbar - no flow layout, button labels hidden by default (very easy show/hide, just a flag).</p>
<blockquote>
<p>is ribbon interface a possibility with QT? If so, I agree it makes sense…</p>
</blockquote>
<p>Not really. We could use similar high-level layout as ribbon controls, but tabbed widgets and groupboxes are just a very small part of the whole ribbon concept. I like the ribbon interface and it would give Slicer a modern look, but it would require a lot of work to be implement and it should be then used for the whole GUI, not just for Segment Editor.</p>

---

## Post #17 by @lassoan (2021-09-13 19:54 UTC)

<p>Thanks to all the efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a>, the new Segment Editor layout is now ready - see more information (and provide any feedback and suggestions) in this topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="19649">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/new-segment-editor-layout-vertical-effect-toolbar/19649">New Segment Editor layout - vertical effect toolbar</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks to all the development efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and feedback from the community, the new, more space-efficient Segment Editor user interface is now ready (available in latest Slicer Preview Release). The main difference is that the effect toolbar is vertical, with fixed number of columns and without icon labels. This layout makes it easier to remember where to find an effect (because the same effect always appears at the same place), and the space is used more efficiently (there is less n…
  </blockquote>
</aside>


---
