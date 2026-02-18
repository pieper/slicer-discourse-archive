# Show/hide segment surface in 3D view

**Topic ID**: 837
**Date**: 2017-08-07
**URL**: https://discourse.slicer.org/t/show-hide-segment-surface-in-3d-view/837

---

## Post #1 by @fedorov (2017-08-07 16:53 UTC)

<p>I created a segment, and I confirmed its master representation is Binary labelmap.</p>
<p>I then created surface by pushing the button “Create surface” in Segment Editor. I noticed that having a 3D surface rendered while performing editing in-slice leads to a noticeable slow-down of editor interactions, so I was looking for an option to disable surface rendering in 3D view, but I could not find this option.</p>
<p>I can un-click “Create surface” button (as aside, it is somewhat non-intuitive to me that “create” button acts as a checkbox) - the surface is gone from 3D view, but apparently it is also deleted and if I click “Create surface” it is being re-generated, since there is a noticeable delay.</p>
<p>The “eye” button in the segments list disables both segment overlay in slice and its rendering in 3d view. If mouse over the “eye” I see some mention of advanced visibility options, but long press does not trigger any such options (or maybe I need to press in some specific location of the button? there is no hint in its appearance about the advanced capability).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07f3b63146cd68c2eed6ef6ebe6367a27ed82083.png" alt="image" data-base62-sha1="18luvWatK1s6fTjkdTLBP05q8f1" width="198" height="108"></p>
<p>As a suggestion:</p>
<ul>
<li>I think “Create surface” should not be checkable, or if it stays checkable, its title should change to something else other than “Create surface” after surface has been created (“Delete surface”?)</li>
<li>I think it would be helpful to be able to control visibility of the segment surface in 3d view without having to delete the surface.</li>
<li>Tooltip for the eye icon in the segments list appears to be inconsistent with the actual behavior.</li>
</ul>
<p>Tested with the latest available nightly of Slicer on mac - Aug 1.</p>

---

## Post #2 by @fedorov (2017-08-09 18:49 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> just wanted to make sure you saw this</p>

---

## Post #3 by @cpinter (2017-08-09 19:37 UTC)

<ul>
<li>Makes sense, we can change the name of the button. <a class="mention" href="/u/lassoan">@lassoan</a> please comment, as you had pretty strong opinions about this button earlier</li>
<li>The surface is not “deleted” and “created”. This is a very important feature of Segmentations (see Validity problem in <a href="https://www.slicer.org/w/images/a/ae/20160526_Segmentations.pdf">slides</a>), that the non-master representations are either up-to-date, or invalidated (removed so that they are re-created on demand). When you edit the labelmap, the surface becomes invalid immediately, and needs to be updated.</li>
<li>I’ll fix it, this used to work. Two other ways to hide/show the surface
<ul>
<li>Segmentations module Display section</li>
<li>Subject hierarchy right-click on the eye icon in the row of the segmentation</li>
</ul>
</li>
</ul>

---

## Post #4 by @lassoan (2017-08-10 02:21 UTC)

<p>2 posts were split to a new topic: <a href="/t/how-to-use-masking-in-segment-editor/852">How to use masking in Segment editor</a></p>

---

## Post #6 by @cpinter (2017-08-09 22:00 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> As it turns out about the third point, the options are there, but the flag that determines whether the advanced options are visible is false by default, but the tooltip was set nevertheless. What I did so far was to set the tooltip only if the advanced options are available.</p>
<p>As far as I remember we kept it disabled by default to avoid further clutter. Thoughts?</p>

---

## Post #7 by @lassoan (2017-08-09 22:03 UTC)

<blockquote>
<p>Makes sense, we can change the name of the button. <a class="mention" href="/u/lassoan">@lassoan</a> please comment, as you had pretty strong opinions about this button earlier</p>
</blockquote>
<p>We already got feedback about the misleading button name (state button has action name) and I agree we should change it. The name should clearly indicate that it toggles closed surface representation (and not just hides/shows it) but otherwise I don’t have any strong preference.</p>

---

## Post #8 by @fedorov (2017-08-10 03:12 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>As far as I remember we kept it disabled by default to avoid further clutter. Thoughts?</p>
</blockquote>
</aside>
<p>I don’t think it adds much clutter, since it will not be shown by default. I assume you meant to add a little drop-down hint, as done in slice views link button? This by far would be a lot more convenient than the other options you mentioned to control surface view by going to other modules.</p>
<aside class="quote no-group" data-username="cpinter" data-post="3" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>The surface is not “deleted” and “created”.</p>
</blockquote>
</aside>
<p>I definitely don’t know what is happening under the hood, but from the user perspective, if I un-click “Create surface” button, and then click it again right away (i.e., the representation does not change in between, so I would expect it to be up-to-date), there is a significant delay until I see the surface again in 3d view. It looks like the surface is re-generated, but perhaps it should not be if it didn’t change. You should be able to easily reproduce the delay by thresholding a whole body CT to make a segment.</p>
<p>I did find the other option to control 3d view in Segmentations. It shows up faster when I re-enable it, but there is still some delay.</p>

---

## Post #9 by @lassoan (2017-08-10 03:31 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>This by far would be a lot more convenient</p>
</blockquote>
</aside>
<p>The issue with the long-press dropdown was that we often activated those advanced visualization options unintentionally and that slowed down the operation. Also, keeping closed surface representation but not showing it should be discouraged, as you would still need to wait for the closed surface representation to be computed but you would not see the result. Implementing background conversion between representations would be nice and we plan to do it in the future, but it is quite low priority.</p>
<p>We could easily add segmentation display options to the Segment Editor module, but it would make an already complex module even more complicated (similarly, it would be useful to have segment import/export directly there…). Do you think we should merge Segmentations module features into Segment editor? Or fuse the two modules into one?</p>
<p>I think for now we should focus on making it more clear what the show/hide icon and Create surface buttons do. What do you think about keeping the button as a checkbox but change the title to simply <code>3D</code> or <code>Show in 3D</code>?</p>

---

## Post #10 by @cpinter (2017-08-10 13:30 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>un-click “Create surface” button, and then click it again right away</p>
</blockquote>
</aside>
<p>I see. I don’t see this as a real use case, but we can certainly not delete it just hide it.</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>This by far would be a lot more convenient</p>
</blockquote>
</aside>
<p>For sure. What we could also do is to add these options to the segment right-click menu as well. I don’t see any disadvantage of exposing this option in multiple places, especially if (as you also seem to agree) the long-press option is disabled by default. Currently the only action in that right-click menu is “Show only selected segments”. We could add the 2D outline, 2D fill, and 3D visibility options as well.</p>

---

## Post #11 by @cpinter (2017-08-10 15:15 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="10" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I see. I don’t see this as a real use case, but we can certainly not delete it just hide it.</p>
</blockquote>
</aside>
<p>Actually this will be problematic after all. If we hide it but keep the representation, then after every editing step the conversion will still take place. According to the original design this should not be the case, but apparently some part of the code requests the surface so it’s re-generated.</p>
<p>Can you tell us whether this quick show/hide of only the surface while keeping the 2D is a general request, or is it annoying in a specific use case?<br>
Would it be enough to show/hide the segment or the segmentation?</p>

---

## Post #12 by @fedorov (2017-08-10 16:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>keeping closed surface representation but not showing it should be discouraged, as you would still need to wait for the closed surface representation to be computed but you would not see the result.</p>
</blockquote>
</aside>
<p>You might want to think about use cases where the user does not need to always see all of the segments. If you, for example, work with an atlas, you need to toggle visibility of individual structures, out of hundreds, while, for example, editing one single segment. If the segments are not edited, there should be no need to recompute the surface.</p>
<p>I don’t think the user should be discouraged from certain actions based on how things are implemented. They will see the performance hit, and will adjust their actions accordingly. But there should also not be unnecessary performance degradation where it is not needed, such as toggling surface visibility.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you think we should merge Segmentations module features into Segment editor? Or fuse the two modules into one?</p>
</blockquote>
</aside>
<p>Sometimes I ask myself the same question, but I see good and bad either way… Maybe as a compromise to help users in the short term, add a shortcut button to jump directly to Segmentations from Segment Editor, and give some hint about what capabilities are available from there?</p>
<aside class="quote no-group quote-modified" data-username="cpinter" data-post="11" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<blockquote>
<p>I see. I don’t see this as a real use case, but we can certainly not delete it just hide it.</p>
</blockquote>
<p>Actually this will be problematic after all. If we hide it but keep the representation, then after every editing step the conversion will still take place. According to the original design this should not be the case, but apparently some part of the code requests the surface so it’s re-generated.</p>
<p>Can you tell us whether this quick show/hide of only the surface while keeping the 2D is a general request, or is it annoying in a specific use case?</p>
<p>Would it be enough to show/hide the segment or the segmentation?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/cpinter">@cpinter</a> the example I provided is not a real use case, but just a simple way to reproduce the problem.</p>
<p>The specific situation where I came across this is the following. I played with brain MR images to segment the tumor. I had surface rendering enabled, and noticed that there is a delay in applying Segment Editor effects. So I thought if I disable surface rendering, I can do editing more quickly, and then show the surface again after I am done. That’s when I noticed that even if I don’t touch the segment, and change my mind and need to look at 3d again after looking around in 2d, I get this delay.</p>
<p>It’s definitely not a stopper. Should I file a bug report about the fact that surface is re-generated when segment is unchanged? As I mentioned earlier, the behavior in show/hide of surface is different between Segmentations and Segment Editor, so maybe making those consistent is a good task to tackle, whenever there are cycles.</p>

---

## Post #13 by @cpinter (2017-08-10 16:36 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>add a shortcut button to jump directly to Segmentations from Segment Editor, and give some hint about what capabilities are available from there</p>
</blockquote>
</aside>
<p>I like this idea.</p>
<aside class="quote no-group" data-username="fedorov" data-post="12" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>If the segments are not edited, there should be no need to recompute the surface</p>
</blockquote>
</aside>
<p>True, validity could be handled on a per-segment basis. Unfortunately this would be a considerable implementation task, as representations are currently handled per-segmentation, and this change would require moving all the master representation and conversion related logic to the vtkSegment level. Imagine the segments and representations the rows and columns of a table. Now we can only remove whole rows or columns, but after this change we could remove individual cells. It’s a major change in the code, especially considering all testing and bugfixing etc.<br>
A relatively easy way I see to support this is a specialized segment editor, where you have your atlas, and you edit one segment at a time. So basically we would have two segmentations: the atlas, and the edited segment only.</p>
<aside class="quote no-group" data-username="fedorov" data-post="8" data-topic="837">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I did find the other option to control 3d view in Segmentations. It shows up faster when I re-enable it, but there is still some delay.</p>
</blockquote>
</aside>
<p>We tried and found the same. We’ll investigate, as there should be no delay in simply showing a segment in 3D.</p>
<p>Summarizing the definite actionables so far:</p>
<ul>
<li>Rename Create surface button (“Show 3D” ?)</li>
<li>Investigate slow show/hide of only the surface representation</li>
<li>Add button to Segment Editor to switch to Segmentations. Its name TBD. The tooltip should mention visibility options, import/export, conversion parameters. Maybe long-click for quick export?</li>
</ul>

---

## Post #14 by @fedorov (2017-08-10 16:56 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> thank you for the detailed explanation and suggestions! This all makes sense to me.</p>
<p>Yes, a shortcut for quick export would probably be helpful, considering how often this question comes up.</p>

---

## Post #15 by @cpinter (2017-08-30 15:38 UTC)

<p>Just referencing the PR which contains the changes requested here:<br>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/783" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/783" target="_blank">Cannot load any DICOM volume</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:54" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:55" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #16 by @cpinter (2017-09-09 15:54 UTC)

<p>PR above integrated in<br>
<a href="https://github.com/Slicer/Slicer/commit/36fe64b16734c962156c5f574280a6fa7b9cccb6" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/36fe64b16734c962156c5f574280a6fa7b9cccb6</a></p>

---

## Post #17 by @cpinter (2017-09-09 15:57 UTC)

<p>Show/hide segmentation performance issue fixed in<br>
<a href="https://github.com/Slicer/Slicer/commit/0a4374c08b401d23f88159ee45ae2dc81243205d" class="onebox" target="_blank">https://github.com/Slicer/Slicer/commit/0a4374c08b401d23f88159ee45ae2dc81243205d</a><br>
Tested on the brain atlas. Hiding the segmentation is faster than hiding the model hierarchy, and show seems to take the same amount of time.</p>

---
