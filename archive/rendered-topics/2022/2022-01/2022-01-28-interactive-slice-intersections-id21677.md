# Interactive slice intersections

**Topic ID**: 21677
**Date**: 2022-01-28
**URL**: https://discourse.slicer.org/t/interactive-slice-intersections/21677

---

## Post #1 by @dgmato (2022-01-28 13:55 UTC)

<p>Until now, slice intersection navigation was based on hotkeys like <em>Shift+drag</em> for moving the 3D cursor, or <em>Ctrl+Alt+drag&amp;drop</em> for rotation of the slice planes when slice intersections are shown.</p>
<p>We added a new feature to enable <strong>interactive slice intersections</strong>. This feature will enable to move the slice intersection point or rotate the slice planes using only the mouse, by clicking and dragging the slice intersection lines in the 2D views. When hovering over the intersection lines, the mouse cursor changes to indicate which action is available for the user: translation or rotation. Ordinary keyboard-based controls are also available using this new interactive mode.</p>
<p>This feature can be activated and customized in the <em>ViewersToolbar</em> once the ordinary slice intersection mode has been activated. Also, translation and rotation actions can be enabled or disabled using the <em>Interaction Options</em> in the <em>ViewersToolbar</em>.</p>
<p>See video below:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e91bbee20b883ea664544f258f0600502530210d.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e91bbee20b883ea664544f258f0600502530210d.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e91bbee20b883ea664544f258f0600502530210d.mp4</a>
    </source></video>
  </div><p></p>
<p>Some useful links:</p>
<ul>
<li>
<p><a href="https://github.com/Slicer/Slicer/commit/bc5d5b45fcb1949a2545ee1c2e2c1f35976698ac" rel="noopener nofollow ugc">Commit</a></p>
</li>
<li>
<p><a href="https://github.com/Slicer/Slicer/issues/5544#issuecomment-1023296672" rel="noopener nofollow ugc">Issue</a></p>
</li>
</ul>
<p>The feature is available in the latest Slicer Preview Release.</p>
<p>Any feedback and suggestions are welcome.</p>
<p>David</p>

---

## Post #2 by @juangmagic (2022-01-29 00:42 UTC)

<p>It is Fantastic… I love it, thank you very much. Maybe this function could work with the crosshair tool too, and allow 3D visualization of the intersection.</p>

---

## Post #3 by @DNeil (2022-01-30 08:35 UTC)

<p>Wow! This looks great!<br>
<img src="https://emoji.discourse-cdn.com/twitter/clap.png?v=12" title=":clap:" class="emoji only-emoji" alt=":clap:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji only-emoji" alt=":+1:"></p>

---

## Post #4 by @jamesobutler (2022-01-31 16:05 UTC)

<p>Is there a way to have the slice intersections be interactive, but also still intersect? Currently, when in interactive mode, they are in a crosshair mode and not actually intersecting. Slicer’s Crosshair object has both a “basic crosshair” and “basic + intersection” option.</p>
<p>Interactive is OFF:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13706d80541fe6aeff9cb25d90538efd7c787aee.png" alt="image" data-base62-sha1="2LXWJgpe9bl1pGpQy5ixnnzHqOO" width="296" height="314"></p>
<p>Interactive is ON:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df78fb56a9b1f8598a0b3f4ddb700e85c5f1cb3d.png" alt="image" data-base62-sha1="vSVG30znA7fQpV14idLZQyHEOMB" width="266" height="315"></p>

---

## Post #5 by @dgmato (2022-01-31 16:41 UTC)

<p>The current implementation can be adjusted to show the intersection. There is a constant in <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionInteractionRepresentation.cxx#L91" rel="noopener nofollow ugc"><em>vtkMRMLSliceIntersectionInteractionRepresentation</em></a> that can be modified to “ShowIntersection”. This will show the intersection of the lines, while maintaining the rest of functionalities.</p>
<p>By default, we decided to keep the intersection hidden. You could change the visualization mode by changing the value of <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionInteractionRepresentation.cxx#L91" rel="noopener nofollow ugc">this constant</a> in your custom build.</p>
<p>However, we may consider adding a property in the <em>vtkMRMLSliceDisplayNode</em> so that this visualization mode can be easily modified by the users. We’ve already added some custom properties in the <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSliceDisplayNode.h#L63" rel="noopener nofollow ugc"><em>vtkMRMLSliceDisplayNode</em></a> to control the visibility and to enable/disable the rotation and translation actions for the interactive mode. We could add something similar to control the visualization mode, defining if the intersection is shown or not.</p>

---

## Post #6 by @chir.set (2022-01-31 17:26 UTC)

<p>This is certainly a great addition making reslicing easier for new comers.</p>
<p>I’m wondering about the feasibility of a small enhancement :</p>
<ul>
<li>Add more buttons in the ‘Crosshair selection’ toolbar</li>
<li>One button to activate intersection</li>
<li>One button to activate intersection interactively</li>
</ul>
<p>Currently, the drop down menu allows to activate intersection, and we have to open the menu again to choose interaction. More buttons would allow a one-step switch.</p>
<p>It’s not compelling, just a small usability addition.</p>

---

## Post #7 by @jamesobutler (2022-01-31 17:26 UTC)

<p>Yes <a class="mention" href="/u/dgmato">@dgmato</a> would you be able to make the following changes to have the options like the current crosshair options?</p>
<ul>
<li>“No crosshair” is like the “Slice intersections” checkbox being unchecked</li>
<li>“Basic crosshair” would be “Slice intersections” checkbox checked, with the crosshair spacing, but with interactions off</li>
<li>“Basic + intersection” would be like the current option where “Slice intersections” checkbox is checked, with interactions off</li>
</ul>
<p>The “Interaction” checkbox would then only toggle whether interaction is on/off and would not make any display changes to slice intersections. Display of the slice intersections such as whether the lines comes to a cross or have an open crosshair would not change and same goes with slice intersections line thickness would not change either when “Interaction” is toggled (line thickness is currently changing which is odd).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb9fd08c35d09eac8af1ce257b289031debd0083.png" alt="image" data-base62-sha1="xCqBCHidihpFolpNhu7JTHqj9Hd" width="204" height="338"></p>

---

## Post #8 by @dgmato (2022-01-31 19:39 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> I agree with you that the toolbar selection could be improved. Currently, you need to open the menu twice to activate the interactive slice intersections mode, which may not be convenient.</p>
<p>If I understood correctly, your idea is to add three more options to control the visualization mode of the slice intersection mode. These three options would substitute the “Slice Intersections” checkbox. Then, we would have one check box (“Interaction”) to activate/deactivate the interactive mode, and the “Interaction Options” to enable/disable the translation and rotation actions during interaction. Right?</p>
<p>I like this idea proposed by <a class="mention" href="/u/jamesobutler">@jamesobutler</a>. I think it would be pretty intuitive for the users. Also, I really like the icon you showed in <a href="https://discourse.slicer.org/t/crosshair-vs-slice-intersections/21700/2">this post</a>.</p>
<p>The current design of the toolbar options was proposed by <a class="mention" href="/u/lassoan">@lassoan</a>, who suggested following a similar approach to the markups interactivity configuration (see discussion <a href="https://github.com/Slicer/Slicer/pull/6008#discussion_r746238229" rel="noopener nofollow ugc">here</a>). What do you think <a class="mention" href="/u/lassoan">@lassoan</a>?</p>

---

## Post #9 by @jamesobutler (2022-01-31 20:03 UTC)

<p>It seems like there is desire from some groups to have the open crosshair display type, while others prefer the lines actually fully intersecting. Due to this requirement I believe the options have to be like what was already done for the “Crosshair” object type. If just one of these options was all that was needed, then the simple checkbox could be done, but that doesn’t seem to be the case here.</p>
<aside class="quote no-group" data-username="dgmato" data-post="8" data-topic="21677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dgmato/48/14079_2.png" class="avatar"> dgmato:</div>
<blockquote>
<p>These three options would substitute the “Slice Intersections” checkbox. Then, we would have one check box (“Interaction”) to activate/deactivate the interactive mode, and the “Interaction Options” to enable/disable the translation and rotation actions during interaction. Right?</p>
</blockquote>
</aside>
<p>Yes that is correct.</p>
<p>I think this similar duplication between “Slice Intersections” functionality and the “Crosshair” object functionality is what I was discussing at in another thread. This post (linked below) from <a class="mention" href="/u/cpinter">@cpinter</a> reflects on this topic of maybe “Slice intersections” is truly replacing the “Crosshair” object because it’s hard to see a reason to have duplicate options for each here in this menu.</p>
<aside class="quote" data-post="5" data-topic="21700">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/crosshair-vs-slice-intersections/21700/5">Crosshair vs Slice Intersections</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    To reflect on the actual topic, I have a hard time finding a usage for the crosshair too. It is a singleton, and so there is a single crosshair in the application, sort of like a “current point of interest” as I interpret it. The one thing I can think of where crosshair is more than slice intersections is that it is visible in 3D. Maybe we should add a checkbox for slice intersection visiblity in 3D and get rid of crosshairs altogether?
  </blockquote>
</aside>


---

## Post #10 by @chir.set (2022-01-31 21:06 UTC)

<aside class="quote no-group" data-username="dgmato" data-post="8" data-topic="21677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dgmato/48/14079_2.png" class="avatar"> dgmato:</div>
<blockquote>
<p>your idea is to add three more options</p>
</blockquote>
</aside>
<p>Not exactly. The crosshair toolbar has only 1 button currently. I’m thinking of a second toggle button that would activate/deactivate intersection, and a third toggle button that will activate/deactivate interaction (and also activate/deactivate intersection by necessity).</p>
<p>If the second button is deactivated, the third one should be deactivated.</p>
<p>If the third one is activated, the second one should be activated.</p>
<p>The drop down menu does not have to change.</p>
<p>The crosshair toolbar would contain 3 buttons in all, instead of one (which is currently like a sub-menu in a menu bar).</p>

---

## Post #11 by @lassoan (2022-02-01 02:18 UTC)

<p>I agree that we should add a separate toolbar button for slice intersection display. The intersections could be displayed by a single click and interactivity could be enabled by 2 clicks. Configuration of the slice intersection type could be also added in the menu of that button.</p>
<p>So, we would end up with two buttons in the crosshair toolbar:</p>
<ul>
<li>Crosshair (toggle)
<ul>
<li>No jump slices / Jump slices - offset / Jump slices - centered</li>
<li>No crosshair / Basic crosshair / … / Small basic + intersection</li>
<li>Fine crosshair / Medium crosshair / Thick crosshair</li>
</ul>
</li>
<li>Slice intersections (toggle)
<ul>
<li>Interaction (toggle)</li>
<li>Interaction options (submenu): Translate (toggle) / Rotate (toggle) – we can change this design but it should be consistent with how we configure interactions for markups (in view context menu when clicking on a control point)</li>
<li>Full line / Skip line crossings  – in the future there could be an option to show the line for the infinite slice plane (don’t shorten the line when a slice is zoomed in)</li>
<li>Fine / Medium / Thick – not needed now, just could be added in the future</li>
</ul>
</li>
</ul>
<p>In the future we could add an application settings to set default slice intersection mode (interactive or non-interactive). I would not add it yet, because the feature is still somewhat immature: it is not compatible with Segment Editor (due to Segment Editor not using widgets and so there are two components competing for viewer events). For now, users can add a Python code snippet if they want to enable interactive slice intersection by default.</p>
<hr>
<p>About removing crosshair. I would love to see any simplification and removal of unused features, but I don’t think we can remove the crosshair, no matter how sophisticated slice intersections become. Crosshair and slice intersections are related, as both display lines and the crosshair can make slices move (and therefore move slice intersections). However, the crosshair has some important properties:</p>
<ul>
<li>there is always one single crosshair position in the entire scene (while there may be 0 to many slice intersection points)</li>
<li>a crosshair can be always specified (even when there is only a single slice view, or there are no slice views just 3D views)</li>
<li>the crosshair can be used to cross-reference a position across slice and 3D views; or between 3D views</li>
<li>the crosshair position can be always set to the current mouse pointer position (while slice intersections are preferably drag-and-dropped, because if you have many slice intersections it may not be clear which intersection the user intends to move)</li>
</ul>

---

## Post #12 by @cpinter (2022-02-01 11:09 UTC)

<p>Separating the two features seems to have a consensus.</p>
<p>Yes I assume there are users who use crosshairs and would like to keep doing so. I, however, am still a bit confused about how it works (or supposed to work), and what is its purpose, i.e. how it is intended to be used.</p>
<ul>
<li>It cannot be drag&amp;dropped, it can only be moved using the Shift key (is this true btw?). I really would expect that if it is an important “landmark” then it can be moved without shortcuts.</li>
<li>If you drag the slider in a slice view, then there is apparently no way to navigate back. Again, if we consider the crosshair VIP position in the scene, jumping back should be simple, but at least possible.</li>
</ul>
<p>So to me it seems like a bit obscure feature for select users, and I imagine that if I had to highlight points in the scene, using fiducial points are easier (and they support both above features in a simple way). The only thing fiducials cannot do is moving the VIP one with the Shift key.</p>

---

## Post #13 by @lassoan (2022-02-01 18:21 UTC)

<p>The main use of the crosshair node are the followings</p>
<ul>
<li>Show a single point in all views for cross-reference (regardless of slice views exist or they intersect): you use it by toggling the crosshair button and moving the crosshair using shift+mousemove</li>
<li>Provide position for the Data Probe or any other module that wants to get a current mouse cursor position.</li>
<li>Move slice intersections: enabled by default but if you think that with the new slice intersections feature it is no longer needed then it could be made configurable in the application settings.</li>
</ul>
<p>These are all very commonly used features. We could say that they are somewhat “obscure” because it is not obvious how all these features are related to the crosshair. There is documentation (<a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html?highlight=crosshair#view-cross-reference">user</a>, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/mrml_overview.html?highlight=crosshair#basic-mrml-node-types">developer</a>, and quite a few examples in the script repository) - would adding more details help?</p>

---

## Post #14 by @mikebind (2022-02-01 20:41 UTC)

<p>So, if I am understanding correctly, the crosshair location’s real function is to serve as a singleton “currently selected location”.  This idea cannot be replaced by the concept of “wherever the slices intersect” because there may be no such place or many such places since the number and orientation of slices can be arbitrary. However, in the other direction, it is always possible to move existing slices such that the slice plane contains a “currently selected location” while maintaining their existing normal vector.</p>
<p>One other thing I would like to note is that moving slices (via shift-mousemove) only moves slices in the same ViewGroup (as defined in the layout). This is an important feature because sometimes you want leave one group of slices in a particular position while you search through another group (e.g. while looking for matching fiducial points in two image volumes).  Currently, this is handled by only moving slices in the same ViewGroup as the view or slice over which you are shift-mouse-moving.  I just wanted to mention this use case because it is a bit of an exception to the idea that all slices move in response to the crosshair postion.</p>
<p>I only very rarely use a visible crosshair, generally preferring the more visually informative colored slice intersections, but I use shift-mousemove all the time, which I now understand is using the crosshair node under the hood.</p>

---

## Post #15 by @DIV (2022-02-02 05:28 UTC)

<p>Hello, David.</p>
<p>For the translation, I wondered how it compared with the existing functionality of pressing <code>Shift</code> while moving the mouse (hovering) across one of the Slices.  I usually do this with the crosshair turned on.<br>
A separate discussion seems to have been created on that topic.</p>
<aside class="quote no-group" data-username="pieper" data-post="6" data-topic="21700">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"><a href="https://discourse.slicer.org/t/crosshair-vs-slice-intersections/21700/6">Crosshair vs Slice Intersections</a></div>
<blockquote>
<p>E.g. use shift-mousemove to position the slices</p>
</blockquote>
</aside>
<p>The rotation is a cool feature.  The question I had was about reverting to axes lining up with the original (DICOM/RAS) coordinates.  After some rotation has been performed, how should the user return to the ‘default’ alignment?</p>
<p>—DIV</p>

---

## Post #16 by @mikebind (2022-02-02 23:47 UTC)

<p>In each slice view, you can select ‘Axial’, ‘Coronal’, or ‘Sagittal’ to return to world RAS coordinate axes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab332725a8bb53be1b98b22c605081cc016c51de.png" data-download-href="/uploads/short-url/oqvf0vOxKqkfp3mOf5cQZjJl7bg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab332725a8bb53be1b98b22c605081cc016c51de.png" alt="image" data-base62-sha1="oqvf0vOxKqkfp3mOf5cQZjJl7bg" width="517" height="251" data-dominant-color="DDD7D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">761×370 16.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To return to the IJK image volume array axes directions, you can click the ‘Rotate to volume plane’  button:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c2fafa1c2e59704d294056e7c352cc41a6ee1ae.png" data-download-href="/uploads/short-url/k090N7JoqBCyVKsPcooj0FeW394.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c2fafa1c2e59704d294056e7c352cc41a6ee1ae_2_517x95.png" alt="image" data-base62-sha1="k090N7JoqBCyVKsPcooj0FeW394" width="517" height="95" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c2fafa1c2e59704d294056e7c352cc41a6ee1ae_2_517x95.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c2fafa1c2e59704d294056e7c352cc41a6ee1ae_2_775x142.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c2fafa1c2e59704d294056e7c352cc41a6ee1ae_2_1034x190.png 2x" data-dominant-color="E0D2CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1276×236 17.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #17 by @jamesobutler (2022-02-13 23:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="11" data-topic="21677">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>So, we would end up with two buttons in the crosshair toolbar:</p>
</blockquote>
</aside>
<p>I’ve issued the following PR with work for separating these two things into their own QToolButtons.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6186">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6186" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6186" target="_blank" rel="noopener nofollow ugc">ENH: Add separate toolbutton for slice intersections</a>
      </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:slice-intersections-toolbutton</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-13" data-time="23:28:06" data-timezone="UTC">11:28PM - 13 Feb 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="4 commits changed 11 files with 510 additions and 95 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6186/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+510</span>
            <span class="removed">-95</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This separates out Slice intersection visibility and associated interactive and <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6186" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">style actions into its own QToolButton as part of the "Crosshair Selection" QToolBar.

This work is based on the discussion over at https://discourse.slicer.org/t/interactive-slice-intersections/21677/11?u=jamesobutler.

| Current | This PR (Crosshair QToolButton) | This PR (Slice Intersections QToolButton) |
|----------|---------|---------|
|![image](https://user-images.githubusercontent.com/15837524/153779777-3aa71acb-8dc5-4f35-b0c5-dc691d17a248.png)|![image](https://user-images.githubusercontent.com/15837524/153779811-dfa20262-b9ad-4b03-81c8-0c7b19d74b2d.png)|![image](https://user-images.githubusercontent.com/15837524/153779832-3271baf8-2751-45d4-9788-8b321c97407e.png)|

## Current problems
- [ ] Currently the style updating changes (Full vs Skip line crossings and Fine/Medium/Thick line thickness) is not acting appropriately. This is part of commit `ENH: Add actions to customize slice intersections style`. Things aren't appropriately mapped and updating appropriately. It's unclear to me how best to modify the defined properties in vtkMRMLSliceIntersectionInteractionRepresentation where the interactive mode had been hardcoding a different style (slightly thicker and skip line crossings). Instead these style options should be applied whether interactive mode is enabled or not. There have been plenty of times users have asked on the forum to make the slice intersections thicker.
- [ ] Toggling slice view intersections from Markups module "Control Points" section is not in sync with the `IntersectingSlicesVisibleAction` checked state.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #18 by @Arash (2024-02-23 10:50 UTC)

<p>Thank you dgmato. It’s very interesting and useful. Without this useful feature, my 3D slicer’s crosshair has only almost useless features such as Fine crosshair, Medium crosshair, Thick crosshair :)) but no rotation and translation!<br>
However, I have a suggestion. Please kindly complete your post by clarifying how this feature can be activated and customized in the <em>ViewersToolbar</em>, and how the ordinary slice intersection mode can be activated. Also, how translation and rotation actions can be enabled or disabled using the <em>Interaction Options</em> in the <em>ViewersToolbar</em>, please? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #19 by @linhuanfeng (2024-09-04 08:41 UTC)

<p>What is the core code of the navigation point function code for 3D view and slice view</p>

---

## Post #20 by @lassoan (2024-09-04 10:43 UTC)

<p>Link to the source code was provided in the first post of the topic;</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/bc5d5b45fcb1949a2545ee1c2e2c1f35976698ac">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/bc5d5b45fcb1949a2545ee1c2e2c1f35976698ac" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/bc5d5b45fcb1949a2545ee1c2e2c1f35976698ac" target="_blank" rel="noopener">ENH: Add interactive slice intersections widget</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-01-27" data-time="02:52:25" data-timezone="UTC">02:52AM - 27 Jan 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/dgmato" target="_blank" rel="noopener">
          <img alt="dgmato" src="https://avatars.githubusercontent.com/u/10816661?v=4" class="onebox-avatar-inline" width="20" height="20">
          dgmato
        </a>
      </div>

      <div class="lines" title="changed 30 files with 4546 additions and 382 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/bc5d5b45fcb1949a2545ee1c2e2c1f35976698ac" target="_blank" rel="noopener">
          <span class="added">+4546</span>
          <span class="removed">-382</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">If "Interaction" flag is enabled then slice intersections can be drag-and-droppe<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/commit/bc5d5b45fcb1949a2545ee1c2e2c1f35976698ac" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">d in slice views.

Re #5544

Co-authored-by: Andras Lasso &lt;lasso@queensu.ca&gt;
Co-authored-by: Csaba Pinter &lt;pinter.csaba@gmail.com&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
