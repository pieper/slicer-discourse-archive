# Set center of rotation for transform in 3D model

**Topic ID**: 21467
**Date**: 2022-01-14
**URL**: https://discourse.slicer.org/t/set-center-of-rotation-for-transform-in-3d-model/21467

---

## Post #1 by @Marta_Fernandez (2022-01-14 18:34 UTC)

<p>Hello.</p>
<p>I want to change the center of rotation of a 3d model(stl). I would like to rotate it in his own center of rotation (In the middle of the object). Because now I only can rotate it with a rotation around the 0.0 ax.<br>
Thanks for your answers and help</p>

---

## Post #2 by @mikebind (2022-01-14 20:34 UTC)

<p>There is a recipe for this in the script repository <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point</a></p>

---

## Post #3 by @Lin (2022-01-15 12:30 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=11" title=":grinning:" class="emoji only-emoji" alt=":grinning:"><br>
learned a ton, very useful to me.</p>

---

## Post #4 by @ortho3d (2023-11-13 08:10 UTC)

<p>Sorry I don’t understand the process.Shall I paste the script somewhere (in the code section?) I can’t rotate around a center of rotation I’d like to choose. thanks</p>

---

## Post #5 by @mikebind (2023-11-13 17:33 UTC)

<p>Yes, you can paste the code in the Python console (which can be opened/hidden by pressing Ctrl-3).  This area is a command prompt for an interactive python session in Slicer’s python environment.  Many scripts in the script repository will work without modification when pasted directly to the python console, however this one will need a little bit of editing by you before pasting, and a little bit of pre-work before you run it.</p>
<p>First you need to create a markups point where you want the center of rotation to be.  If this is the first markups point you have created and you have not specified a name, the default name will be “F”.  If the name of the markups node is not “F”, you need to change the second line of the script so that the name in <code>getNode()</code> matches the name of your markups node.</p>
<p>Next you need to create two transform nodes, one which will serve as your rotation<br>
controller, and one which will be automatically updated to represent rotation around your chosen center rather than around the origin. You can create linear transform nodes in the Transforms module.  You need to make a note of the names of the transforms you create and change lines 4 and 6 of the script to contain those names in the <code>getNode()</code> calls.</p>
<p>Then you are ready to paste the modified script (the whole thing at once) into the python console, which will run it.  Any modifications to the rotation controller transform will automatically result in modifications to the other transform such that it represents the same rotation, but around your chosen center instead of around the origin.</p>
<p>Next, you need to add the automatically updating transform as the parent transform to whatever you want to be rotating.  There are many ways to do this in Slicer.  You can use the Transforms module or the Transform hierarchy tab of the Data module, but the simplest is to use the Subject hierarchy tab of the Data module.  Find the object you want to rotate on the list, and then look to the right, there will be a small icon which looks like two rotated grids.  Right click on that and then select the name of the automatically updating transform.</p>
<p>Finally, you can go to the Transforms module, select the rotation controller transform, and move the sliders in the “Rotation” section. All objects with the automatically updating transform as the parent transform will now be rotated around your chosen center point.  That center point can also be interactively moved as desired.</p>

---

## Post #6 by @ortho3d (2023-11-13 20:06 UTC)

<p>thanks so much but a video would be great . I know we are all busy.<br>
Best regards</p>

---

## Post #7 by @lassoan (2023-11-13 20:23 UTC)

<p>FYI, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is working on a new transform widget that will allow rotation around a chosen point (and translation along object or world axes) in both 2D and 3D views. The first version of the feature may be available in the Slicer Preview Release within a couple of weeks.</p>
<p>You can track the progress of this work here:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/2579">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/2579" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/2579" target="_blank" rel="noopener">Transform Widget:  easy enhancements for more user-friendly manual registrations</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="23:47:59" data-timezone="UTC">11:47PM - 12 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
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
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=2579). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @Kenneth_Sutherland (2024-11-22 01:34 UTC)

<aside class="quote no-group quote-modified" data-username="Marta_Fernandez" data-post="1" data-topic="21467" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marta_fernandez/48/10323_2.png" class="avatar"> Marta_Fernandez:</div>
<blockquote>
<p>There is a recipe for this in the script repository</p>
</blockquote>
</aside>
<p>I have placed a fiducial  marker at the center of a MRI volume and can successfully run the script to rotate about the center. Now I want to translate the whole volume along the IS (z) axis. Is there a way to keep the marker at the center of the volume and rotate about this new position?</p>

---

## Post #9 by @lassoan (2024-11-24 13:01 UTC)

<p>In current Slicer Preview Release you can set the center of rotation for the transformation. Visually in a 2D/3D editor, or as center of a node, or by entering coordinates in the Transforms module, or using Python scripting setting the center in the transform node.</p>
<aside class="quote quote-modified" data-post="1" data-topic="36974">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-feature-interactive-transformation-adjustable-center-of-rotation/36974">New feature: Interactive transformation + adjustable center of rotation</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    Any nodes can now be translated, rotated, or scaled by interactive handles.  Editing operations can be constrained to specific axes and center of rotation can be freely chosen. The handles are available both in slice and 3D views. 
Transform nodes can be easily added and visualized for any node in 3D Slicer by right-clicking on the node in the Subject hierarchy visibility column and checking “Interaction”. 

  <a href="https://www.youtube.com/watch?v=ielxgJS-6SI" target="_blank" class="video-thumbnail" rel="noopener">
    [Transform Interaction Handles in 3D Slicer]
  </a>


<a name="visualization-options-1" class="anchor" href="#visualization-options-1"></a>Visualization options
Visualiza…
  </blockquote>
</aside>


---
