# Markups node creation icon is confusing users

**Topic ID**: 9016
**Date**: 2019-11-04
**URL**: https://discourse.slicer.org/t/markups-node-creation-icon-is-confusing-users/9016

---

## Post #1 by @muratmaga (2019-11-04 21:13 UTC)

<p>Currently same icon is used to create both a new fiducial in a list [1 below], and a new fiducial list [2] in the Markups module. This behavior is confusing to the users. I propose to modify the node creating one slightly to make it less similar. It might have visual clues to what it does (e.g., add three dots, have word Node/List on it etc).</p>
<p>[1] <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb8dfba7cd4497a8adecb6c5d9958bd45ad65159.png" alt="image" data-base62-sha1="t2J7FEiqCYLhqhaTaHvNQx4xL05" width="250" height="82"></p>
<p>[2] <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5819b05df11d4505c4e17fb49d71c951d62cb511.png" data-download-href="/uploads/short-url/czn3s3qM9gNCXmlVzs1iP0jKDAZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5819b05df11d4505c4e17fb49d71c951d62cb511_2_690x98.png" alt="image" data-base62-sha1="czn3s3qM9gNCXmlVzs1iP0jKDAZ" width="690" height="98" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5819b05df11d4505c4e17fb49d71c951d62cb511_2_690x98.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5819b05df11d4505c4e17fb49d71c951d62cb511.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5819b05df11d4505c4e17fb49d71c951d62cb511.png 2x" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">764×109 5.44 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-11-05 01:05 UTC)

<p>Adding text to markups module buttons should be no problem at all (other than that the module GUI might become a bit too wide). Adding a small “+” sign to the icon is easy, too. However, I don’t think these would be enough to make the toolbar behavior intuitive enough.</p>
<p>What do you think about adding a “current markups node” selector to the toolbar and having separate button for place point and for create new markups:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2d55011c79b13b00624047d3e359da9e425d6f1.png" data-download-href="/uploads/short-url/pw20DnAOJVYLJxAESfdz8u6jsVH.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2d55011c79b13b00624047d3e359da9e425d6f1_2_690x217.png" alt="image" data-base62-sha1="pw20DnAOJVYLJxAESfdz8u6jsVH" width="690" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2d55011c79b13b00624047d3e359da9e425d6f1_2_690x217.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2d55011c79b13b00624047d3e359da9e425d6f1_2_1035x325.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2d55011c79b13b00624047d3e359da9e425d6f1_2_1380x434.png 2x" data-dominant-color="F4E3BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1428×451 93.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2019-11-05 06:15 UTC)

<p>I think that looks great!</p>

---

## Post #4 by @pieper (2019-11-05 12:20 UTC)

<p>That does look handy, but also looks like a lot of real estate - maybe only display the markups toolbar if you are in markups. mouse mode?</p>

---

## Post #5 by @lassoan (2019-11-05 14:47 UTC)

<p>Normally the user arranges toolbar sections manually (move them closer to make them shorter, arrange them to multiple rows, etc.) . Automatically showing/hiding toolbar section would mess up manual arrangements. All toolbar sections are optional (you can show/hide each using the right-click menu) and Qt does some nice automatic collapsing of long toolbars and you can use multiple rows, so long sections may be tolerable.</p>
<p>We could also think switching to a ribbon-like menu instead of a menu+toolbar (<a href="https://github.com/martijnkoopman/Qt-Ribbon-Widget">https://github.com/martijnkoopman/Qt-Ribbon-Widget</a>, <a href="https://weekly-geekly.github.io/articles/48963/index.html">https://weekly-geekly.github.io/articles/48963/index.html</a>).</p>

---

## Post #6 by @muratmaga (2019-11-05 15:58 UTC)

<p>Actually, with 4K screens and maximized view, there is more than enough screen real-estate to fit that widget into the toolbar. If anything, toolbar usually doesn’t do a good job for separating individual sections so the rest is visible.</p>
<p>Having said that, I am also wondering if that whole widget can be part of the Markup module by itself (i.e., move from toolbar to the markups). I usually need the rest of the functionality as well (like being able to display points, color change etc)…</p>

---

## Post #7 by @pieper (2019-11-05 16:34 UTC)

<p>It’s not a big deal, but or the record my issue with real estate on the toolbar is that I end up using the default config a lot for actual work, either because I want to test it for development or because I use a bunch of different machines and don’t want to customize each one, so the default config is important to me, even if I’m using a 4K screen.  Plus of course it’s what most new users will have until the learn to customize (if they ever bother to).</p>
<p>My issue currently is that at the default window size already the extension manager and python console icons, which are the ones I use the most, aren’t displayed, so it’s several extra clicks (either resize the app or dig through the toolbar).  I wouldn’t mind the ribbon, but also like the idea of moving a lot of the markup configuration stuff to the markups module.</p>

---

## Post #8 by @jamesobutler (2019-11-05 16:47 UTC)

<p>I’d agree with not having this toolbar in the default configuration and having the functionality also in the markups module.</p>
<p>Also +1 for removing Capture/Restore from default toolbar configuration.</p>

---

## Post #9 by @cpinter (2019-11-05 20:51 UTC)

<p>Nice discussion. On my part I agree with <a class="mention" href="/u/pieper">@pieper</a> in that the Extension Manager and Python buttons are very important but often are forced out of the toolbar, and also agree with <a class="mention" href="/u/jamesobutler">@jamesobutler</a> that the Scene Views toolbar should not be visible by default.</p>
<p>I think the ribbon interface would be an overkill. It would only make sense if we came up with a good way to use its potential: defining meaningful ribbons and populating them to put them to good use. Of course then we’ll need to allow modules to define their sections. But given that each module has a panel, and the full ribbon is not much smaller than that, it would mostly be a duplication of the module panel, and it would kind of serve as a second selectable module. If we go that way then it needs a proper discussion.</p>

---

## Post #10 by @muratmaga (2019-11-05 21:42 UTC)

<p>Well if we will remove the 3D Slicer logo from the module panel (<a href="https://issues.slicer.org/view.php?id=3797" rel="nofollow noopener">https://issues.slicer.org/view.php?id=3797</a>) that will generate a lot of space of module specific toolbars and widgets, wouldn’t it?</p>

---

## Post #11 by @lassoan (2019-11-05 21:42 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="9" data-topic="9016">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If we go that way then it needs a proper discussion.</p>
</blockquote>
</aside>
<p>This may be that discussion.</p>
<p>We are running out of space. Even if we hide scene views toolbar by default, we want to show more controls for example for markups, sequences, and layouts (favorite layouts pinned to top-level to make them available by a single click).</p>
<p>If space was the only issue then maybe we could dock some toolbars to the left instead of the top and/or arrange toolbars into two rows by default. But a ribbon-like toolbar+menu would also make the application look more modern and familiar.</p>

---

## Post #12 by @lassoan (2019-11-06 04:37 UTC)

<p>There is a related discussion with some more ideas. It would be great if you could comment on those, too.</p>
<aside class="quote quote-modified" data-post="12" data-topic="9029">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segment-editor-user-interface-improvements/9029/12">Segment Editor User Interface Improvements</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Maybe something like this could work as a categorization: 
Manual editing: 

Paint
Draw
Erase
Level Tracing
Scissors

Semi-automatic editing: 

Threshold
Grow from seeds
Fill between slices
Watershed
Fast Marching
Flood Filling

Global editing: 

Margin
Smoothing
Logical operators

Modeling: 

Draw Tube
Surface Cut

Volumes: 

Mask Volume
Split Volume

How would you use these categories? 

That’s interesting and indeed it would be quite easy to implement (by adjusting the style sheet). Let’s se…
  </blockquote>
</aside>


---

## Post #13 by @muratmaga (2019-11-12 19:27 UTC)

<p>Is there a conclusion on these long-term discussion? Meawhile, we should do something on remedying the original issue (same icon, two different functions).</p>

---

## Post #14 by @lassoan (2019-11-14 14:51 UTC)

<p>Adding a small “+” sign to the icons in Markups module would not be a problem. Could you send a pull request with the proposed change?</p>

---
