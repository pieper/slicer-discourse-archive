# New Segment Editor layout - vertical effect toolbar

**Topic ID**: 19649
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/new-segment-editor-layout-vertical-effect-toolbar/19649

---

## Post #1 by @lassoan (2021-09-13 19:51 UTC)

<p>Thanks to all the development efforts of <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and feedback from the community, the new, more space-efficient Segment Editor user interface is now ready (available in latest Slicer Preview Release). The main difference is that the effect toolbar is vertical, with fixed number of columns and without icon labels. This layout makes it easier to remember where to find an effect (because the same effect always appears at the same place), and the space is used more efficiently (there is less need for scrolling).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7a87dfbdf1b798215c165caafdf2a6771214f32.jpeg" data-download-href="/uploads/short-url/nVaJhbqhuzfTvTzdUhmofeQw9MK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a87dfbdf1b798215c165caafdf2a6771214f32_2_690x419.jpeg" alt="image" data-base62-sha1="nVaJhbqhuzfTvTzdUhmofeQw9MK" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a87dfbdf1b798215c165caafdf2a6771214f32_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a87dfbdf1b798215c165caafdf2a6771214f32_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a7a87dfbdf1b798215c165caafdf2a6771214f32_2_1380x838.jpeg 2x" data-dominant-color="A3A1A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1167 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Feedbacks and suggestions are welcome.</p>

---

## Post #2 by @tomekcz (2021-09-15 14:01 UTC)

<p>This is looking great. One minor suggestion now that the Effect labels have been removed and the button icons are much smaller is to consider creating some new artwork for very common effects to harmonize them with well-known painting and image editing programs.</p>
<p>For example, the Draw tool could be made into a simple pencil icon, the Paint tool could just be a paintbrush, Flood Filling could be a paint can, Level Tracing could be a magic wand, Eraser just a simple eraser. I’m not sure what exactly to do with Scissors, the icon implies cutting/deleting to me, but the functionality is more like a “shapes” tool that lets you draw circles and rectangles. The more advanced, 3D image icons are probably fine as is, but worth putting some thought into given the new design.</p>

---

## Post #3 by @lassoan (2021-09-15 14:15 UTC)

<aside class="quote no-group" data-username="tomekcz" data-post="2" data-topic="19649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tomekcz/48/11462_2.png" class="avatar"> tomekcz:</div>
<blockquote>
<p>consider creating some new artwork for very common effects to harmonize them with well-known painting and image editing programs</p>
</blockquote>
</aside>
<p>Good idea. Contributions for improving these icons are very welcome. We actually need to update all Slicer icons, as screen resolutions increased since the current icons were created and the style has become inconsistent over the years.</p>

---

## Post #4 by @simonoxen (2021-09-16 07:44 UTC)

<p>Hi, just looked at this, it is great! Thanks for the effort!</p>
<p>One comment: would it make sense to put the undo/redo buttons like the picture attached? Then they would also always stay in the same place and not relocate in the GUI with each effect description.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be39465f1bf076f9e448eaa556032456bca5ed1c.png" data-download-href="/uploads/short-url/r8NqFX2nOlPVmr3gs9qHnbZjNpO.png?dl=1" title="segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be39465f1bf076f9e448eaa556032456bca5ed1c_2_421x500.png" alt="segment" data-base62-sha1="r8NqFX2nOlPVmr3gs9qHnbZjNpO" width="421" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be39465f1bf076f9e448eaa556032456bca5ed1c_2_421x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be39465f1bf076f9e448eaa556032456bca5ed1c_2_631x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be39465f1bf076f9e448eaa556032456bca5ed1c_2_842x1000.png 2x" data-dominant-color="F1F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment</span><span class="informations">1148×1362 80.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think it might also be clearer that they are not dependent on the effect</p>
<p>Thanks</p>

---

## Post #5 by @lassoan (2021-09-16 11:46 UTC)

<p>What do you think about showing it below the effect toolbar?<br>
It would keep the (none) effect stand out and and preserve the concept of workflows starting in the top-left corner (you would not start with undo/redo). Also, if you scroll up to see the all segment effects and masking settings then the top of the effect list may not be visible anymore.</p>
<p>Could you give this a try to implement this and give it a try how it works for you? Probably placing it into a separate frame (not in the effect toolbar) would be better, so that if the effect toolbar is configured with more columns, the undo/redo would still span the whole width.</p>

---

## Post #6 by @simonoxen (2021-09-17 05:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="19649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It would keep the (none) effect stand out and and preserve the concept of workflows starting in the top-left corner (you would not start with undo/redo)</p>
</blockquote>
</aside>
<p>I see, this makes sense.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="19649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Could you give this a try to implement this and give it a try how it works for you?</p>
</blockquote>
</aside>
<p>Yes, unfortunately lately haven’t had much time to work on developing in Slicer environment. This could be something to check out in the future.</p>

---

## Post #7 by @lassoan (2021-09-17 13:36 UTC)

<p>No problem. Thanks for the suggestion anyway.</p>
<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> when you implemented this new design, have you experimented with placing the undo/redo buttons in different locations? Would you have time to me to give it a try to put it under the effect toolbar?</p>

---

## Post #8 by @jamesobutler (2021-09-17 13:40 UTC)

<p>I never considered moving the undo/redo button location, but moving it to smaller toolbuttons under the Segment Effect frame does make sense. That would then bring up masking to be directly below the effect options groupbox.</p>
<p>Yes, I can spend some time maybe this weekend to experiment with that change.</p>

---

## Post #9 by @jamesobutler (2021-09-18 15:36 UTC)

<p>Here’s some images of the prototype. I’ve put it below the segment effects as <a class="mention" href="/u/lassoan">@lassoan</a> suggested based on the concept of the workflow starting at the top left and then working down. I’ve put the undo/redo in a similar styled frame groupbox like the effects frame.</p>
<p>I made it a separate frame rather than putting inside the same one as the effects to decouple logic associated with effect count which is based on the number of items in the layout in the effects layout. I had previously considered putting a horizontal line at the bottom of the effects frame and then putting the undo/redo buttons below that which would have had everything within that same effects frame. However, the two separate frames (Effects group and then the Undo/Redo group) appears to work well too.</p>
<p>Let me know what you think and I’ll issue a PR.</p>
<p>Overview Prototype:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/550b5d7c7fff031242534c79d5ad322c5fa56280.jpeg" data-download-href="/uploads/short-url/c8kVXhjFJ2oRd0B3mhQ4GtAUQ9y.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/550b5d7c7fff031242534c79d5ad322c5fa56280_2_690x370.jpeg" alt="image" data-base62-sha1="c8kVXhjFJ2oRd0B3mhQ4GtAUQ9y" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/550b5d7c7fff031242534c79d5ad322c5fa56280_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/550b5d7c7fff031242534c79d5ad322c5fa56280_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/550b5d7c7fff031242534c79d5ad322c5fa56280_2_1380x740.jpeg 2x" data-dominant-color="818189"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>1Column:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b122111d202c0671b566c290b0d5df7c0a4c4636.png" alt="image" data-base62-sha1="pgZv0CeAF8aOTHkaUqiCP0AeNbU" width="59" height="197"></p>
<p>2 Column (Default)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bc1b3f319d91e8e897c015597613bbeed20be03.png" alt="image" data-base62-sha1="fng5WP16KIcimbbOH57VTWKyU9B" width="83" height="134"></p>
<p>3+ Column<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b838f3c7fc14c17c314294e6fe8248b8ba0c448.png" alt="image" data-base62-sha1="aM1FREFhc8z1tJZQTIyFV7ZDIla" width="120" height="137"></p>

---

## Post #10 by @lassoan (2021-09-18 15:59 UTC)

<p>This looks great!</p>
<p>Just one small change we could consider is adjustment of the space between the effects frame and undo/redo frame. The space between the two frames should be the same (or maybe a bit larger) than the internal margin (space between the frame and the buttons inside).</p>

---

## Post #11 by @jamesobutler (2021-09-18 16:08 UTC)

<p>This is with the spacing set to 11 (same as QGridLayout margin values) instead of the default 7. This what you are thinking?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c912540ba8eb81a0df58312aa9cac2d64cf7323.jpeg" data-download-href="/uploads/short-url/44IlcHcugckWDKmIqhl13jatUYz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c912540ba8eb81a0df58312aa9cac2d64cf7323_2_690x370.jpeg" alt="image" data-base62-sha1="44IlcHcugckWDKmIqhl13jatUYz" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c912540ba8eb81a0df58312aa9cac2d64cf7323_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c912540ba8eb81a0df58312aa9cac2d64cf7323_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c912540ba8eb81a0df58312aa9cac2d64cf7323_2_1380x740.jpeg 2x" data-dominant-color="808188"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @jamesobutler (2021-09-18 16:19 UTC)

<p>This is with the value set to 7. I thought this was the default, but actually looks a little different for the better. I think this looks a little better than the 11 value I showed above.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6045ff57a2bbf846892203c34c1c12236697e4bc.png" alt="image" data-base62-sha1="dJFNY8zErHDlUmsoUwppir8ux8o" width="96" height="191"></p>

---

## Post #13 by @jamesobutler (2021-09-18 16:29 UTC)

<p>I have issued PR based on this work and if others want to experiment different values for spacing they can easily do it with the code.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5875">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5875" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5875" target="_blank" rel="noopener nofollow ugc">ENH: Undo Redo segment editor buttons stay in same position</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:undo-redo-move</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-18" data-time="16:28:33" data-timezone="UTC">04:28PM - 18 Sep 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
          <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="1 commits changed 2 files with 75 additions and 32 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5875/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+75</span>
          <span class="removed">-32</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This moves the Undo and Redo buttons in the Segment Editor module to be under th<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5875" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">e effects groupbox. This is motivated by the desire for these buttons to not move when different segment editor effects are selected.

See https://discourse.slicer.org/t/new-segment-editor-layout-vertical-effect-toolbar/19649/9?u=jamesobutler for more details about this development.

| Current | This PR |
|----------|---------|
|![image](https://user-images.githubusercontent.com/15837524/133895687-bbf355b0-63a4-4e8f-8139-4832499b87d5.png)|![image](https://user-images.githubusercontent.com/15837524/133895637-9b5d8e05-0de0-4f1d-9e9a-28bbd744d613.png)|</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #14 by @lassoan (2021-09-18 17:16 UTC)

<p>Looks perfect to me, thank you. If there are no other comments then I’ll merge this later today.</p>

---

## Post #15 by @simonoxen (2021-09-20 08:35 UTC)

<p>That was fast, very nice! thanks!</p>

---

## Post #16 by @rbumm (2021-09-20 10:05 UTC)

<p>Do one has to use this new layout ? or is that an option ? I liked the older too because of the text labels.</p>

---

## Post #17 by @lassoan (2021-09-20 14:52 UTC)

<p>Yes, the labels are “nice”, that’s why we have been holding out until now. However, it has become clear that displaying the labels only in tooltips (as all other software do) is better, because it takes much less space. We now fix the button positions to make the toolbar buttons easier to find.</p>
<p>I see that for new users the labels could save time, and you can enable that with a single line of code (the varying width of the buttons will be fixed in tomorrow’s Slicer Preview Relase):</p>
<pre><code class="lang-python">getModuleGui('SegmentEditor').editor.effectButtonStyle = qt.Qt.ToolButtonTextUnderIcon
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/50739746cfee81e0a69b2fd400c6d268517561d6.jpeg" data-download-href="/uploads/short-url/btHQHAtsZVGGEysNanpkAbnbOhU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50739746cfee81e0a69b2fd400c6d268517561d6_2_690x420.jpeg" alt="image" data-base62-sha1="btHQHAtsZVGGEysNanpkAbnbOhU" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50739746cfee81e0a69b2fd400c6d268517561d6_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50739746cfee81e0a69b2fd400c6d268517561d6_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/50739746cfee81e0a69b2fd400c6d268517561d6_2_1380x840.jpeg 2x" data-dominant-color="A9AAAF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1170 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We could make the button style configurable in application settings, but it would be difficult to let users know that the option exists. It would be better to implement alternative solutions to make effect buttons easier to find.</p>
<p>What do you think about the suggestion above of making the icons more similar to commonly-used other software (Paint, Photoshop, Gimp?) - would that be sufficient?</p>

---

## Post #18 by @pieper (2021-09-20 16:40 UTC)

<p>The current tooltips are pretty good, but it could be nice if the buttons had a no-delay mouseover effect that set a label with the effect name, say at the top of the toolbar.  That way the information would be readily discoverable without taking much space.  Tool tips aren’t as nice because of the initial delay, they are sometimes covered by the mouse pointer, and because they jump around making them a little harder to read.</p>

---

## Post #19 by @jamesobutler (2021-09-20 16:46 UTC)

<p>Regarding other applications use of tool tips, how do their tool tips behave? What delay is a common value to show? You would of course not want to show it immediately but only during a moment of delayed inspection.</p>

---

## Post #20 by @rbumm (2021-09-20 16:50 UTC)

<p>The sidebar of effects is an elegant solution.<br>
Maybe we could make the label text toggle when the user right-clicks on this particular frame and selects a menu option “button texts”, then save this preference for the next start? New users would certainly benefit from the label texts because the full selection of editor tools can be quite overwhelming, as soon as people are experts they could hide the labels.<br>
Much of this is personal preference - f.e. I do not like program toolbars very much and prefer flexible, labeled buttons or using a menu.<br>
The problem with tool text is, that you always get a short but significant time delay to actually see them - in my Slicer installations this is around 3 s</p>
<p>Updating the icons and styling them similarly in a flexible resolution would be great.</p>

---

## Post #21 by @rbumm (2021-09-20 16:55 UTC)

<p>FileZilla has a great tool tips response of about half a second.</p>

---

## Post #22 by @jamesobutler (2021-09-20 17:19 UTC)

<p>Using the latest Slicer Preview for today the tooltip delay is slight for the first one, but is pretty quick on that order of a half second as I proceed over others.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a65445e6814d1d79134b86eed0eb0bee473e23.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a65445e6814d1d79134b86eed0eb0bee473e23.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35a65445e6814d1d79134b86eed0eb0bee473e23.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #23 by @lassoan (2021-09-20 17:28 UTC)

<p>The tooltip delay indeed feels long, something like 2 seconds, but I recorded a screen capture video and it actually really is just 0.7 seconds (this value is set in the <a href="https://stackoverflow.com/questions/59054556/how-to-disable-or-shorten-the-tooltip-delay-in-qtableview">default application style</a>). If tooltip is displayed for any of the buttons, then the tooltip is displayed immediately for all other buttons (until the moue pointer leaves the area).</p>
<p>Time improvement that we can get out of eliminating tooltip delay is negligible. The best we could achieve by removing the tooltip delay would be to shave off 0.7 seconds from finding a toolbar button. This is not much, because finding a toolbar button by iterating through every button using the mouse pointer is a very slow way of finding a button: it takes about 5-10 seconds in total. I don’t think it is worth changing the default tooltip delay for this marginal benefit. Most of the time we regret when we try to be smarter than everyone else and override such default behaviors.</p>
<p>We should think about solutions that allow newcomers to learn the effect icons faster (how they look and/or where they are).</p>
<ul>
<li>Having nicer icon would help for sure. I’m working on making the icons rendered crisper, with more details, but I don’t have a talent for drawing nice icons. Could anybody help with designing nice icons?</li>
<li>Showing the button labels is really easy. However, I’m not sure how it could be configured on the GUI in a way that users can find but does not cause clutter. Any suggestions?</li>
<li>Any other ideas for providing training wheels for new users that can be easily taken away?</li>
</ul>

---

## Post #24 by @jamesobutler (2021-09-20 17:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="23" data-topic="19649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Having nicer icon would help for sure. I’m working on making the icons rendered crisper, with more details, but I don’t have a talent for drawing nice icons. Could anybody help with designing nice icons?</p>
</blockquote>
</aside>
<p>I think having improved icons for Segment Editor module appears to be an agreed upon good task. Should we create a new discourse post explaining the current look of icons and then we can brainstorm ideas for new icons based on what other applications have to explain the similar type action?</p>

---

## Post #25 by @lassoan (2021-09-20 17:38 UTC)

<p>A post was split to a new topic: <a href="/t/move-effects-from-segmenteditorextraeffects-into-slicer-core/19768">Move effects from SegmentEditorExtraEffects into Slicer core</a></p>

---

## Post #26 by @muratmaga (2021-09-20 17:58 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="22" data-topic="19649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Using the latest Slicer Preview for today the tooltip delay is slight for the first one, but is pretty quick on that order of a half second as I proceed over others.</p>
</blockquote>
</aside>
<p>For me it is not so much the slowness, but the tooltips are actually kind of small to read. Is it possible to increase the size a bit more (without affecting the other tooltips)?</p>

---

## Post #27 by @jamesobutler (2021-09-20 21:16 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="24" data-topic="19649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Should we create a new discourse post explaining the current look of icons and then we can brainstorm ideas for new icons based on what other applications have to explain the similar type action?</p>
</blockquote>
</aside>
<p>Completed. See below</p>
<aside class="quote quote-modified" data-post="1" data-topic="19772">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/improve-segment-editor-effects-icons/19772">Improve recognizability of Segment Editor effects icons</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    With recent optimization of the Segment Editor module GUI the segment effects are now displayed a QToolButtons with icons that do not display text with the button. Text was removed to make the buttons more compact and to align with the style of other programs such as Paint, Photoshop, Gimp etc where they don’t put text under each effect in their list of tools. 
As originally suggested by <a class="mention" href="/u/tomekcz">@tomekcz</a>, we could update the segment editor effect icons to more closely align with the icons used in other …
  </blockquote>
</aside>


---

## Post #28 by @lassoan (2021-09-20 21:25 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="26" data-topic="19649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Is it possible to increase the size a bit more (without affecting the other tooltips)?</p>
</blockquote>
</aside>
<p>Can you show a screenshot? Have you set a larger font in Slicer application settings (scaled the Slicer font in application settings / Appearance / Font and size) or adjusted the application scaling settings in your operating system or in your <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#runtime-environment-variables">environment variables</a>?</p>

---

## Post #29 by @muratmaga (2021-09-21 03:36 UTC)

<p>I am using the default font size in Slicer (10 pts). When my laptop screen set to 1920x1080 and font scaling in windows is 100% (which is recommended for that resolution) this is what I see:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a31cfac5c59114d91dc128560c6affac294dba5a.jpeg" data-download-href="/uploads/short-url/ngXUNFBZIupW8pR4DxEH1VUDetQ.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a31cfac5c59114d91dc128560c6affac294dba5a_2_690x388.jpeg" alt="image" data-base62-sha1="ngXUNFBZIupW8pR4DxEH1VUDetQ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a31cfac5c59114d91dc128560c6affac294dba5a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a31cfac5c59114d91dc128560c6affac294dba5a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a31cfac5c59114d91dc128560c6affac294dba5a.jpeg 2x" data-dominant-color="84858C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×720 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I switch to 3840x2160 resolution (which is the native display for this laptop), and use 250% scaling (again recommended by windows) this is what I see:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eca25b62d71dbbb0b7a7032c12fa476f4a58483.jpeg" data-download-href="/uploads/short-url/8XsHvERq0V1SoBBCN4fa20f1YSn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eca25b62d71dbbb0b7a7032c12fa476f4a58483_2_690x388.jpeg" alt="image" data-base62-sha1="8XsHvERq0V1SoBBCN4fa20f1YSn" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eca25b62d71dbbb0b7a7032c12fa476f4a58483_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3eca25b62d71dbbb0b7a7032c12fa476f4a58483_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3eca25b62d71dbbb0b7a7032c12fa476f4a58483.jpeg 2x" data-dominant-color="8A8B91"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×720 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So definitely better with the scaling and higher DPI. I can stick with that. I used the lower resolution for some other applications…</p>

---

## Post #30 by @rbumm (2021-09-21 19:56 UTC)

<p>Could I just add that I did some segmentations today with the new vertical toolbar and I am quite lost without the button labels. The problem with tooltips is that you need to scan through several of the buttons to find what you need.<br>
But maybe I am just not the icon type of guy …</p>

---

## Post #31 by @lassoan (2021-09-21 20:12 UTC)

<p>The idea is that you visually recognize the buttons because the appearance and layout of the toolbar is always the same. Reading tooltips should be the last resort.</p>
<p>Word, PowerPoint, Excel, Gimp, PhotoShop, ITK-Snap, Mimics, etc. do not display labels (maybe for a few, or for button groups). I’ve only found that Paint is the one that adds more labels, but still more than half of the buttons are not labeled. I don’t think that everybody else is doing it wrong by not displaying labels. It might be that the effect icons are not easy enough to recognize, or maybe there is something else.</p>
<p>Can you give examples of software that display labels next to toolbuttons?</p>
<p>How do you use all the software that do not display labels next to toolbuttons? Do you always rely on the tooltip? Or you can recognize those icons more easily?</p>

---

## Post #32 by @muratmaga (2021-09-21 20:14 UTC)

<p>I am using the new toolbar, while I am fond of it, it does take some getting used to (like any change).</p>
<p>But the significance of this change is the predictable of the position of effects/tools. With the labels, it all depended on how wide your screen was, how big the module panel etc, whether you have 2, 3, or 4 rows of effects. Here the order will always stay the same, once you are used their positions, you will not need to search for them.</p>

---

## Post #33 by @rbumm (2021-09-21 20:37 UTC)

<p>In Pixinsight, an astromical image processing software that is packed with functions, the user can call all from a menu but can save these to modules to the desktop, move them, order, or group them according for each workflow. This is your personal project space which may span many screens.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdafbbeef0cdd681f29d6250e59b02defe273913.png" data-download-href="/uploads/short-url/r42KwZJmG8LnuA6BpTXTNcegQf1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdafbbeef0cdd681f29d6250e59b02defe273913_2_558x500.png" alt="image" data-base62-sha1="r42KwZJmG8LnuA6BpTXTNcegQf1" width="558" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdafbbeef0cdd681f29d6250e59b02defe273913_2_558x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bdafbbeef0cdd681f29d6250e59b02defe273913_2_837x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdafbbeef0cdd681f29d6250e59b02defe273913.png 2x" data-dominant-color="65666E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1103×988 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #34 by @lassoan (2021-09-21 20:58 UTC)

<p>This seems like a visual pipeline editor and not a toolbar. It is justified to have labels in this case because number and location of the blocks is not static (so it would impossible to find tools by visual memory) and you have huge amount of space.</p>

---

## Post #35 by @lassoan (2021-09-27 14:24 UTC)

<p>A post was split to a new topic: <a href="/t/adjust-segment-opacity-in-segment-editor/19880">Adjust segment opacity in Segment Editor</a></p>

---

## Post #37 by @jamesobutler (2021-12-05 19:06 UTC)

<p>To follow up here, <a class="mention" href="/u/rbumm">@rbumm</a> has proposed PR <a href="https://github.com/Slicer/Slicer/pull/6070" class="inline-onebox" rel="noopener nofollow ugc">ENH: Add ability to toggle segment editor tool button style by rbumm · Pull Request #6070 · Slicer/Slicer · GitHub</a> to re-enable the ability to show the Segment Editor Effect name on the buttons because of the concerns he raised previously in this thread.</p>
<p>Originally it was thought to toggle Effect text on the buttons by keyboard shortcut. <a class="mention" href="/u/pieper">@pieper</a> brought an idea to show the effect text when the active effect was “None” and then to hide it when selecting an effect. This was implemented in the PR and is shown in the video below.</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd9321746d7b82a331a0c14aa4561b86d9eef325.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd9321746d7b82a331a0c14aa4561b86d9eef325.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/dd9321746d7b82a331a0c14aa4561b86d9eef325.mp4</a>
    </source></video>
  </div><p></p>
<p>It appears this proposed design doesn’t help maintain Segment Editor Effect buttons location on screen as clicking an effect button then moves that effect button elsewhere on screen in addition to the other effects.</p>
<p>It was previously discussed above in this thread about other applications not displaying labels for many tool editing buttons. That also Slicer’s Segment Editor effect would generally benefit from improved icons for recognizability.</p>
<p>It’s unclear from current brainstorming how showing buttons labels will be possible in a way that does not cause clutter.</p>

---

## Post #38 by @chir.set (2021-12-05 19:44 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="37" data-topic="19649">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>a way that does not cause clutter.</p>
</blockquote>
</aside>
<p>How about a single widget that shows a panel on mouse hovering? That panel would contain all buttons with associated text. Is it a fundamental requirement that all effects be permanently displayed ?</p>
<p>The slice widgets for one already does that :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c730a0de5aef6593606e78befb0e53f47a546aa7.png" alt="hover_panel" data-base62-sha1="sq7cyiprvdy1JxrxY6kXiDzqUOH" width="668" height="228"></p>

---

## Post #39 by @chir.set (2021-12-05 19:50 UTC)

<p>Else, it could be like the preset combobox of ‘Volume rendering’, one that groups choices, expecting only one choice, the text of which is shown when selected.</p>

---

## Post #40 by @jamesobutler (2021-12-05 20:11 UTC)

<p>I think a design requirement is for quick selection between multiple effects as it is common to use multiple effects to manipulate a segment rather than generally only using one effect.</p>
<p>So whether effects in a pop up widget or in a QComboBox, that would increase the number of actions (mouse hover or mouse clicks) to switch between effects which is undesirable.</p>
<p>There is logic internally to the widget that allows setting which effects are displayed to enable essentially “favorite” effects and to hide effects that might not be used in certain custom applications. That could probably allow 1 column of effect buttons with effect name text shown in a manner that isn’t cluttered. However for Slicer core, a design of showing all the effects as the “default” design would be the better design for a majority of Slicer users.</p>
<pre><code class="lang-python">segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorWidget.setEffectColumnCount(1)
segmentEditorWidget.setEffectNameOrder(["None", "Threshold", "Paint", "Draw", "Erase"])
segmentEditorWidget.unorderedEffectsVisible=False
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/245a7223de2e0d5113673413df3038ff5dfb0d29.jpeg" data-download-href="/uploads/short-url/5bAY28j7gzf151IWtBKSEy5wpfj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/245a7223de2e0d5113673413df3038ff5dfb0d29_2_690x370.jpeg" alt="image" data-base62-sha1="5bAY28j7gzf151IWtBKSEy5wpfj" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/245a7223de2e0d5113673413df3038ff5dfb0d29_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/245a7223de2e0d5113673413df3038ff5dfb0d29_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/245a7223de2e0d5113673413df3038ff5dfb0d29_2_1380x740.jpeg 2x" data-dominant-color="85858C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #41 by @pieper (2021-12-05 21:09 UTC)

<p>Thanks for experimenting with this <a class="mention" href="/u/jamesobutler">@jamesobutler</a> .  The experiment you did with the ‘None’ effect showing the names of the effects is exactly what I was thinking.  I still like it, but I guess others can weigh in too.  It doesn’t bother me that the buttons get smaller.  What used to bother me about the old Segment Editor flow-layout toolbar was when buttons moved from, say, the end of one row to the start of the row below and you had to hunt for them.  Here they stay int he same places, just bigger and smaller.</p>
<p>If making the labels come and go with the None effect is too visually jarring, then a little checkbox to control label visibility also makes sense, along with the hotkey as suggested by <a class="mention" href="/u/rbumm">@rbumm</a> .</p>

---

## Post #42 by @lassoan (2021-12-05 22:24 UTC)

<p>For me the buttons collapsing under the click look really bad. The issue is particularly severe because the clicked button is resized.</p>
<p>I think we should not be creative here, but go with solutions that are commonly used in other software.</p>

---

## Post #43 by @hherhold (2021-12-06 00:41 UTC)

<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a> that the button collapse after click is very odd.</p>
<p>When the text was first removed, I was not a fan - I do like the extra space but I missed the text.</p>
<p>This went away after about 2 days. I haven’t missed it since. I will occasionally blank on what a given icon does for something I don’t use often, but switches between tools isn’t slow enough for me that I feel like I’ve wasted time clicking the wrong one.</p>
<p>One possibility is something similar to what Photoshop does (see pic below). If you click and hold, it will tell you the tool (and possible tools grouped under that one, which Slicer doesn’t do right now, but could in the future?)</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e373c65e7f21ce9e33056c9281cd3749f173026.png" alt="image" data-base62-sha1="21L1FRJ8tlcwp6TBtjRVqCjybj0" width="512" height="256"></p>

---

## Post #44 by @rbumm (2021-12-06 07:23 UTC)

<p>I agree, the collapsing series of buttons are not convincing.</p>

---

## Post #46 by @pieper (2021-12-06 13:43 UTC)

<p>Aren’t the tooltips helpful for this purpose?</p>

---

## Post #47 by @hherhold (2021-12-06 15:14 UTC)

<p>I think they work fine, and they’re consistent with other applications. What was the objection to them?</p>
<p>As mentioned, I think this is largely an issue with newcomers and coming up to speed quickly?</p>

---

## Post #48 by @lassoan (2021-12-06 15:32 UTC)

<p>Newcomers and occasional users who haven’t memorized look and location of the icons may prefer to see labels, at the cost of less space available for seeing images and/or need to scroll more to see all editor effect options.</p>
<p>Adding a checkbox into the segment editor widget to allow would make the GUI just slightly more complicated:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/918122fcca72c8e2fc97c49136eb4dc7925e270a.png" data-download-href="/uploads/short-url/kLbUfu3BSSGmiDQkyMDaOzNNJzQ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/918122fcca72c8e2fc97c49136eb4dc7925e270a_2_425x500.png" alt="image" data-base62-sha1="kLbUfu3BSSGmiDQkyMDaOzNNJzQ" width="425" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/918122fcca72c8e2fc97c49136eb4dc7925e270a_2_425x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/918122fcca72c8e2fc97c49136eb4dc7925e270a_2_637x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/918122fcca72c8e2fc97c49136eb4dc7925e270a_2_850x1000.png 2x" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1128×1324 72.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #49 by @muratmaga (2021-12-06 18:02 UTC)

<p>The issue with the labels is that they make the width of the icon too big. This is particularly concerning for effects llike the Fill Between Slices, Grow From Seeds, Logical Operators. On high-DPI screens, I occassionally encounter weird issues such as text being too large with relation to the icons (due to some issue with incorrect scaling, but it was never consistent).</p>
<p>If we are going to go back to having the labels, I propose using shorter labels for effects, so that the icons don’t take too much space, as well as be aesthetically a bit more consistent. Perhaps labels that are only 10 chr max, such as<br>
Grow from seed  → Grow / Grow seeds<br>
Logical Operators → Logical Ops<br>
Fill Between Slices → Thick Edit / Interpolate</p>

---

## Post #50 by @lassoan (2021-12-06 20:23 UTC)

<p>We would not go back to having labels. This would be just a clutch that could be turned on temporarily for people who want this. Kind of an accessibility feature.</p>
<p>I agree that it would be nice to simplify those long effect names, not just for the label lengths but also for making it easier to talk about effects.</p>
<p>“Grow seeds” sounds good and similar enough to the old name that it would probably not cause big issue.</p>
<p>I have a very good candidate for “Logical operators” effect name: “Combine”. It is short and works beautifully for intersect, union, etc. Unfortunately, it is not really applicable to invert and clear. It is also very different from the original name, so the name switch may not be smooth.</p>
<p>“Interpolate” is good for scientists and engineers but I don’t think that clinicians realize that “interpolate” means that they only need to segment on a few parallel slices. There can also be many kinds of interpolations and this one only supports interpolation between parallel slices.</p>

---
