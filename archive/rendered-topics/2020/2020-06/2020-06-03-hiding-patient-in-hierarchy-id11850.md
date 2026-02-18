# Hiding patient in hierarchy

**Topic ID**: 11850
**Date**: 2020-06-03
**URL**: https://discourse.slicer.org/t/hiding-patient-in-hierarchy/11850

---

## Post #1 by @gcsharp (2020-06-03 16:52 UTC)

<p>When I click on the eyeball at the patient level the subject hierarchy, I would expect it to hide the entire patient (both CT and structure set), but it only hides the structure set.   Is this a bug or is this “works as designed”?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b98f8563cec6c97bd6ccc437f6802b897e80b771.png" alt="2020-06-03_12-46_1" data-base62-sha1="qtxP7h8a2avERGIETDKOKXEcqw9" width="622" height="266"></p>

---

## Post #2 by @cpinter (2020-06-03 17:53 UTC)

<p>Volume slice visibility is done through a completely different mechanism than the visibility of other data types such as models, segmentations, fiducials, etc. The normal eye icon affects only these kinds of data (and now with a recent improvement also volume rendering), but not 2D volume visibility. You can see that also the icon indicates that it is different.</p>
<p>As I remember there is an option in the study right-click menu "Show volumes in study"m but I’m not sure if there is one for hiding as well.</p>

---

## Post #3 by @gcsharp (2020-06-03 18:29 UTC)

<p>Thank you Csaba.  Yes, I assumed that this behavior is because the of the different mechanisms.  Clicking the eyeball+volume does show and hide the volume.  The eyeball at the study level doesn’t do anything.  My opinion is that usability is improved if parent levels hide their children, regardless of the mechanism difference.  I’ll go ahead and file a bug report, but obviously this is not anything urgent.</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4961" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4961" target="_blank" rel="nofollow noopener">Controlling visibility of volume node children in subject hierarchy</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-03" data-time="18:38:40" data-timezone="UTC">06:38PM - 03 Jun 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/gregsharp" target="_blank" rel="nofollow noopener">
          <img alt="gregsharp" src="https://avatars0.githubusercontent.com/u/327896?v=4" class="onebox-avatar-inline" width="20" height="20">
          gregsharp
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">The visibility toggle button (ie. the eyeball button) in the subject hierarchy can be used to show or hide the children...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @cpinter (2020-06-03 21:20 UTC)

<p>This is something that has caused us a headache for years. Until last year the eye icon of the parents showed/hid all the children one by one. Then we made a change (in course of the Model Hierarchy rework) that the children’s displayable managers consider the folder type parents’ visibility.</p>
<p>If the study item does not affect the children (of type segmentation, model, etc.), then it is a bug.<br>
If the volume show/hide does not work, then it is also a bug.<br>
But there might be some things that are features <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> I’ll do some testing tomorrow.</p>

---

## Post #5 by @lassoan (2020-06-03 21:46 UTC)

<p>Yes, the problem is that volume display is different from all other nodes, as there is a limit on how many volumes can be displayed at once.</p>
<p>With multi-volume rendering, the issue is resolved for 3D views.</p>
<p>We could also update the slice views to be able to display any number of volumes. It would make the behavior more consistent and there are applications where display of more than 2 volumes would be useful.</p>

---

## Post #6 by @gcsharp (2020-06-03 22:12 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="11850">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If the study item does not affect the children (of type segmentation, model, etc.), then it is a bug.<br>
If the volume show/hide does not work, then it is also a bug.</p>
</blockquote>
</aside>
<p>Those are working very well for me.  Show/hide is very usable, almost perfect!</p>

---

## Post #7 by @Danielle_Wasserman (2022-06-21 20:33 UTC)

<p>I’m afraid that I have the recurring problem of not being able to hide the model by clicking the eye in the hierarchy. It happened yesterday with one specimen and now it is happening with multiples. I can hide the markups but not the 3d model and I must be able to do it to proceed with my markup placement. I hope very much to resolve as soon as possible as I am incredibly behind on my work.</p>

---

## Post #8 by @lassoan (2022-06-22 01:22 UTC)

<p>The problem was reported <a href="https://github.com/Slicer/Slicer/issues/6445">here</a> and a fix will be available in tomorrow’s Slicer Preview Release.</p>

---
