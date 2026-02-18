# A user's proposal for Markups Module enhancements

**Topic ID**: 3362
**Date**: 2018-07-03
**URL**: https://discourse.slicer.org/t/a-users-proposal-for-markups-module-enhancements/3362

---

## Post #1 by @jclauneuro (2018-07-03 14:32 UTC)

<p>Dear 3D Slicer Developers,</p>
<p>I’ve been a regular user of 3D Slicer for a few years now. In particular, I make use of the Markups Module a fair amount for image fiducial placement. We have protocols in which upwards of 250 individual markup points are placed (for evaluating registration quality and for visualizing intracranial electrode locations).</p>
<p>I’ve had the opportunity now to train ~50 students on how to use the Markups module and a few clinicians. My proposal below relates to observations when teaching new users how to use the module and questions/comments that have come up.</p>
<p>I would like to ask about the possibility at some point of offering a few features in the Markups module that could really enhance productivity and usability:</p>
<ol>
<li>A Markup undo button (in case a markup is placed or moved accidentally).</li>
<li>The ability to move/copy multiple rows in the Markups module to a different MarkupsFiducial (currently I’ve only managed to do this for one fiducial at a time).</li>
</ol>
<p>Happy to expand on our workflow and use cases if necessary. I’ll also be attending Slicer Project Week in London, Ontario, Canada in a few weeks in case there is time to discuss then (see here for details: <a href="https://github.com/NA-MIC/ProjectWeek/tree/master/PW29_2018_London_Canada" rel="nofollow noopener">https://github.com/NA-MIC/ProjectWeek/tree/master/PW29_2018_London_Canada</a>). I will likely be offering our intro to slicer (i.e. markups) tutorial during that time should there be enough interest.</p>
<p>best regards,<br>
jclau</p>

---

## Post #2 by @pieper (2018-07-03 22:44 UTC)

<p>Those sound like great ideas - we don’t have anyone actively working on the Markups right now, but <a class="mention" href="/u/lassoan">@lassoan</a> mentioned he is planning to dive into at least the widget implementation and maybe he’ll also do some other features while he’s at it (I don’t know his full plans).  I think he’ll be at the London Project Week.</p>

---

## Post #3 by @jclauneuro (2018-07-05 20:42 UTC)

<p>Sounds great. I’ll get in touch with <a class="mention" href="/u/lassoan">@lassoan</a> if he’s in London.<br>
Do you have a mechanism for submitting feature requests other than this forum? e.g. on Github?</p>

---

## Post #4 by @pieper (2018-07-05 22:10 UTC)

<aside class="quote no-group" data-username="jclauneuro" data-post="3" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jclauneuro/48/1821_2.png" class="avatar"> jclauneuro:</div>
<blockquote>
<p>Do you have a mechanism for submitting feature requests other than this forum?</p>
</blockquote>
</aside>
<p>Yes, we use <a href="https://issues.slicer.org/my_view_page.php">issues.slicer.org</a> for detailed tracking.  You can file the ideas in the Markups category there.</p>
<p>Thanks</p>

---

## Post #5 by @jclauneuro (2018-07-06 00:04 UTC)

<p>Okay, I’ve created a separate feature request for each of the enhancements suggested:</p>
<blockquote>
<ol>
<li>A Markup undo button (in case a markup is placed or moved accidentally).<br>
<a href="https://issues.slicer.org/view.php?id=4576" class="inline-onebox" rel="noopener nofollow ugc">Undo feature for Markups module · Issue #4576 · Slicer/Slicer · GitHub</a></li>
</ol>
</blockquote>
<blockquote>
<ol start="2">
<li>The ability to move/copy multiple rows in the Markups module to a different MarkupsFiducial (currently I’ve only managed to do this for one fiducial at a time).<br>
<a href="https://issues.slicer.org/view.php?id=4577" class="inline-onebox" rel="noopener nofollow ugc">moving/copying multiple rows (fiducials) to a different MarkupsFiducial · Issue #4577 · Slicer/Slicer · GitHub</a></li>
</ol>
</blockquote>

---

## Post #6 by @lassoan (2018-07-06 04:16 UTC)

<p>I’ll be there at the project week in London.</p>
<p>I’ll comment on the features requests in the created issues.</p>

---

## Post #7 by @muratmaga (2018-07-07 23:49 UTC)

<p>Yes, markup module can use some love. I have couple other suggestions as well:</p>
<ol>
<li>
<p>Once a fiducial is placed, we need the ability to restrict its movement in 3D viewer to single planes for more controlled placement. For example, <strong>a</strong> stroke moves it incrementally along Anterior (and <strong>shift + A</strong> along Posterior), <strong>r</strong> moves it along Right (and <strong>shift + R</strong> along left) so forth.</p>
</li>
<li>
<p>The issue of scaling of 3D glyph size with respect to the slice view is still not resolved (at least in the resolutions that I am working on -tens of microns). I have to constantly move the slider back and forth to make it visible in the slice view and then not gigantic in the 3D view. I actually don’t understand the logic behind 3D glyph getting bigger as I zoom into a specimen. It is a point, why doesn’t render at a fix scale (say twice the voxel size) regardless of the field of view?</p>
</li>
</ol>
<p>Should I post these to Mantis?</p>

---

## Post #8 by @jclauneuro (2018-07-09 16:50 UTC)

<p>Great suggestions, <a class="mention" href="/u/muratmaga">@muratmaga</a>. I’ve noticed the issue with glyph sizing as well.</p>
<p>Fyi, I submitted the two requests above late last week and the copy/paste functionality has already been implemented (pending review) and the undo feature may involve mostly reviving existing code. Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the rapid response!</p>
<p>The Markups Module is one of the key features in Slicer for which I have found no equivalent in other open source image analysis/visualization packages. I have several other (more minor) enhancements I would be happy to suggest if there are plans to dedicate resources to improving this module.</p>

---

## Post #9 by @lassoan (2018-07-09 17:12 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I actually don’t understand the logic behind 3D glyph getting bigger as I zoom into a specimen. It is a point, why doesn’t render at a fix scale (say twice the voxel size) regardless of the field of view?</p>
</blockquote>
</aside>
<p>The glyph is in the 3D scene, rendered as a 3D actor, therefore by its size is defined in the 3D scene and not in screen size or pixel size. If we simply rendered it as a 2D actor then it would lead to many issues - it would always visible (even if it should not, e.g., because some foreground object occluded it), its size would not provide hint about its distance from camera, etc.</p>
<p>It could be possible to have a hybrid solution - use 2D actor but try to figure out when it should be hidden; or use a 3D actor but try to normalize its size - but it is not easy to implement, has not been required for any funded projects, and no community member volunteered so far to address this.</p>

---

## Post #10 by @MMMPPPMMM (2018-07-11 11:24 UTC)

<p>I would like to load a list with fiducial names (bony landmarks) in order to avoid that the rater has to input all the names by himself. Is this possible somhow?<br>
Then the rater could select the already named fiducial and pick the position on the segmented surface or the slice view.</p>
<p>And would it be possible, that the fiducial sticks to the segemented surface if it’s moved in 3D:<br>
Here is an example video: <a href="https://streamable.com/kc47h" rel="nofollow noopener">https://streamable.com/kc47h</a></p>
<p>Kind regards</p>

---

## Post #11 by @muratmaga (2018-07-11 22:15 UTC)

<p>You can do that. Generate your blank landmark labels using the Markup tool, save that file (.fcsv), and reload it each time you need to annotated a new specimen.</p>
<p>The challenge with this approach is that modifying a fiducial position easily and effectively is not straightforward, at least with the current tools. More so, if you are doing it in 3D renderer. It is almost easier to do it from scratch, and copy and paste the landmark label from a text file.</p>
<p>A slightly better approach would be do a full set of landmarks on one of your specimens, and save it as a reference. Then, register every sample rigidly to that one, and then load the reference landmarks. That way at least the landmark set will be in roughly approximate positions. However, if you have large size differences it would not work.</p>

---

## Post #12 by @muratmaga (2018-07-11 22:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> There is a good chance we may be able take on these issues, with guidance from you, Steve and other experts. Our timeline and commitment should be more clear in the next couple weeks.</p>

---

## Post #13 by @MMMPPPMMM (2018-07-12 10:10 UTC)

<p>Hi muratmaga</p>
<p>Thanks for your answer.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="11" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>The challenge with this approach is that modifying a fiducial position easily and effectively is not straightforward, at least with the current tools. More so, if you are doing it in 3D renderer. It is almost easier to do it from scratch, and copy and paste the landmark label from a text file.</p>
</blockquote>
</aside>
<p>Yes, that is exactly the problem. I could create a list with the desired names and the fiducial at the origin (0,0,0), but then it’s not possible to reposition the fiducial to the surface of the object, especially if the object is far away from the origin.</p>
<p>So IMO it would be useful if an existing fiducial could be repositioned easily including the stick-to-surface feature: <a href="https://streamable.com/kc47h" rel="noopener nofollow ugc">https://streamable.com/kc47h</a></p>
<aside class="quote no-group" data-username="muratmaga" data-post="11" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>A slightly better approach would be do a full set of landmarks on one of your specimens, and save it as a reference. Then, register every sample rigidly to that one, and then load the reference landmarks. That way at least the landmark set will be in roughly approximate positions. However, if you have large size differences it would not work.</p>
</blockquote>
</aside>
<p>I think this would introduce bias to the rating. The rater should determine the postion by himself without seeing a rough approximation.</p>

---

## Post #14 by @muratmaga (2018-07-13 05:01 UTC)

<p>Stick to surface feature would be definitely useful. However, that will only work with 3D models. Volume rendering technique does not provide a surface to stick the fiducials on.</p>

---

## Post #15 by @lassoan (2018-07-13 19:23 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="14" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>However, that will only work with 3D models.</p>
</blockquote>
</aside>
<p>Markup placement already works with volume rendered images just as well as with 3D models.</p>

---

## Post #16 by @muratmaga (2018-07-14 02:44 UTC)

<p>I meant the proposed functionality of ‘stick to surface during fiducial modification’ would only work with 3d models.</p>

---

## Post #17 by @lassoan (2018-07-14 05:05 UTC)

<p>Stick to surface will be probably implemented using VTK <strong>picker</strong> classes, which can find 3D position of a point visible in a view at a chosen position. These picker classes already work with most actor types, such as polydata models and volumes. There is no limitation here.</p>
<p>You are right that VTK <strong>locator</strong> classes require mesh inputs. However, locators are not needed (and not well suited) for 3D position computations for “stick to surface” feature. If for some reason you needed locators for 3D volumes anyway, then you could generate the necessary iso-surface very quickly.</p>

---

## Post #18 by @muratmaga (2018-07-14 05:40 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks for the clarification.</p>

---

## Post #19 by @jclauneuro (2018-07-25 23:15 UTC)

<p>It was great meeting many of you at the Slicer Project Week last week in London, Canada!</p>
<p>I wanted to summarize some of the discussions I’ve had with <a class="mention" href="/u/lassoan">@lassoan</a> in the interim, and also review his implementation of the enhancements to date.</p>
<p>Andras has implemented the copy and paste feature on nightly (20180725) such that multiple (not necessarily contiguous) rows can be selected. Then using the new Copy and Paste icons, the selected rows can be pasted to a new list or spreadsheet. Hotkeys for copy and paste also work!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b02b5a14929d39ddba91102d78ea0b32ede6691.jpeg" data-download-href="/uploads/short-url/8q1Yv2uIPBhoE94CGNY0DRoFXON.jpg?dl=1" title="Slide1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b02b5a14929d39ddba91102d78ea0b32ede6691_2_690x257.jpg" alt="Slide1" data-base62-sha1="8q1Yv2uIPBhoE94CGNY0DRoFXON" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b02b5a14929d39ddba91102d78ea0b32ede6691_2_690x257.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b02b5a14929d39ddba91102d78ea0b32ede6691_2_1035x385.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3b02b5a14929d39ddba91102d78ea0b32ede6691_2_1380x514.jpg 2x" data-dominant-color="EDF1F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slide1</span><span class="informations">2564×957 391 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>One <strong>open</strong> issue to be resolved is that the old right click Copy functionality still only supports a single row. I spoke earlier with Andras, and the most intuitive solution here is probably just to make this functionality the same as with the icons/hotkeys.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/ded99c3337b1b52e674a0b3c695d841933531aff.jpeg" data-download-href="/uploads/short-url/vNqe0VZXaJYVgA9j5kkG2QJwK63.jpg?dl=1" title="Slide2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded99c3337b1b52e674a0b3c695d841933531aff_2_690x449.jpg" alt="Slide2" data-base62-sha1="vNqe0VZXaJYVgA9j5kkG2QJwK63" width="690" height="449" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded99c3337b1b52e674a0b3c695d841933531aff_2_690x449.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded99c3337b1b52e674a0b3c695d841933531aff_2_1035x673.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded99c3337b1b52e674a0b3c695d841933531aff_2_1380x898.jpg 2x" data-dominant-color="E7ECF0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slide2</span><span class="informations">1458×950 263 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #20 by @jcfr (2018-07-26 06:40 UTC)

<p>Thanks for the detailed report, this will  be great to include in our release notes <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="jclauneuro" data-post="19" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jclauneuro/48/1821_2.png" class="avatar"> jclauneuro:</div>
<blockquote>
<p>and the most intuitive solution here is probably just to make this functionality the same as with the icons/hotkeys</p>
</blockquote>
</aside>
<p><img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #21 by @MMMPPPMMM (2018-08-16 10:27 UTC)

<aside class="quote no-group" data-username="MMMPPPMMM" data-post="10" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9a28c/48.png" class="avatar"> MMMPPPMMM:</div>
<blockquote>
<p>And would it be possible, that the fiducial sticks to the segemented surface if it’s moved in 3D:<br>
Here is an example video: <a href="https://streamable.com/kc47h" rel="noopener nofollow ugc">https://streamable.com/kc47h </a></p>
</blockquote>
</aside>
<p>I think I’ve found an old issue dealing with this feature:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/3849">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/3849" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/3849" target="_blank" rel="noopener nofollow ugc">Constrain fiducials and other markups to a surface</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="00:09:17" data-timezone="UTC">12:09AM - 13 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-17" data-time="03:35:21" data-timezone="UTC">03:35AM - 17 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener nofollow ugc">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=3849). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Does somebody know if there is an issue regarding this feature:</p>
<aside class="quote no-group" data-username="MMMPPPMMM" data-post="10" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9a28c/48.png" class="avatar"> MMMPPPMMM:</div>
<blockquote>
<p>I would like to load a list with fiducial names (bony landmarks) in order to avoid that the rater has to input all the names by himself. Is this possible somhow?<br>
Then the rater could select the already named fiducial and pick the position on the segmented surface or the slice view.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="MMMPPPMMM" data-post="13" data-topic="3362">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/a9a28c/48.png" class="avatar"> MMMPPPMMM:</div>
<blockquote>
<p>I could create a list with the desired names and the fiducial at the origin (0,0,0), but then it’s not possible to reposition the fiducial to the surface of the object, especially if the object is far away from the origin.</p>
</blockquote>
</aside>

---
