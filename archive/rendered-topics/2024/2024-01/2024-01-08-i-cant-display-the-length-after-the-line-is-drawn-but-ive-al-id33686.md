# I can't display the length after the line is drawn, but I've already checked the "length" option

**Topic ID**: 33686
**Date**: 2024-01-08
**URL**: https://discourse.slicer.org/t/i-cant-display-the-length-after-the-line-is-drawn-but-ive-already-checked-the-length-option/33686

---

## Post #1 by @gong (2024-01-08 20:42 UTC)

<p>I can’t display the length after the line is drawn, but I’ve already checked the “length” option.My version is slicer 5.6.1 apple version</p>

---

## Post #2 by @jamesobutler (2024-01-08 21:19 UTC)

<p>Are you by chance using SlicerMorph? Or trying to use undo/redo functionality for Markups module objects which includes the Line object?</p>
<p>This seems reminiscent of the following post:</p><aside class="quote quote-modified" data-post="4" data-topic="31609">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/markups-tools-not-measuring-slicer-5-4-0/31609/4">Markups tools not measuring Slicer 5.4.0</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    <a class="mention" href="/u/jmhuie">@jmhuie</a> what do you mean by stops measuring? 
I am trying to replicate this on an intel Mac I have, and line tools works as expected, but it doesn’t display the measurement field regardless whether slicermorph customization are enabled or disabled? Is this what you are referring to as the issue? 
We did recently enabled undo for markups through the customization script, but I am not seeing any errors in the log file either. 
<a class="mention" href="/u/smrolfe">@smrolfe</a> 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff41cbf974133847e812e6ee12ffdd7eafc2e76f.png" data-download-href="/uploads/short-url/Aq6ISGQ0zpy6Sgkx7TXfWVhbo1V.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a>
  </blockquote>
</aside>

<p>However the above resulted in a change to the SlicerMorphRC file which should be used in the latest Slicer 5.6.1 assuming you re-installed SlicerMorph using the Slicer extensions manager which pulls the latest from the internet.</p>

---

## Post #3 by @muratmaga (2024-01-08 21:42 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="33686">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Or trying to use undo/redo functionality for Markups module objects which includes the Line object?</p>
</blockquote>
</aside>
<p>I can confirm that in 5.6.1 if the SlicerMorph customizations are used, undo is only enabled for fiducial objects, and measurements are displayed correctly for line objects.</p>

---
