# Markups - highlight selected markup clicked in 3D view?

**Topic ID**: 11670
**Date**: 2020-05-22
**URL**: https://discourse.slicer.org/t/markups-highlight-selected-markup-clicked-in-3d-view/11670

---

## Post #1 by @hherhold (2020-05-22 15:04 UTC)

<p>Hi all,</p>
<p>I looked through the topics and docs and this seems like a pretty obvious thing, but I didn’t find it anywhere.</p>
<p>Is there a way to click on a markup in the 3D view and have it highlighted in the markups list in the markup module? I feel like this should work but I’m doing something wrong.</p>
<p>Thanks in advance!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2020-05-22 15:19 UTC)

<p>Yes, you can right-click on the markup and choose “Edit properties”. It opens Markups module, with the clicked markup node selected.</p>

---

## Post #3 by @muratmaga (2020-05-22 15:20 UTC)

<p>That’s a useful feature to have, but I don’t think it is implemented. You can hover over the point, and then right click on it and say ‘toggle point’ and that sort of gives an indication of which one is in the list. But not really ideal for large number of points.</p>

---

## Post #4 by @muratmaga (2020-05-22 15:21 UTC)

<p>Sorry, that doesn’t work in my case (i.e., it doesn’t show the right fiducial selected in the control points). r29055 (windows)</p>

---

## Post #5 by @lassoan (2020-05-22 15:33 UTC)

<p>We haven’t thought about highlighting the point, too, just the markup (and use “toggle select point” for cross-referencing points across views and modules), but it should be quite easy to implement. What is your use case (how would you use and for what applications)?</p>

---

## Post #6 by @hherhold (2020-05-22 15:41 UTC)

<p>Regarding what Murat said, right-clicking in 2D or 3D does not bring up a menu - this appears not to be implemented.</p>
<p>I have a number of markups that label particular morphologies, and I need to edit the names and descriptions. It would be simplest to click in 3D and have it selected in the list in the markups module (or right click, or shift-click, or command-click, I’m flexible). Right now I basically select and de-select markups to see which one is which in the 3D view, or use jump slices to see where it is.</p>

---

## Post #7 by @muratmaga (2020-05-22 15:42 UTC)

<p>Right click is a fairly new feature. Perhaps you are running an older build?</p>
<p>Ditto on the use case. We have similar ones too…</p>

---

## Post #8 by @hherhold (2020-05-22 15:46 UTC)

<p>I’m running May 5 nightly. I’ll grab a newer one.</p>
<p>Thanks! Hope you guys are well.</p>

---

## Post #9 by @lassoan (2020-05-22 15:53 UTC)

<p>Right-click should be available in May 5 version. Do you use a Mac? I’ve noticed that on some touchpad/mouse on Mac create many pointer events, even when the point is not or barely moved, which defeats the current click detection mechanism. Maybe we need to increase the click detection’s motion tolerance.</p>

---

## Post #10 by @hherhold (2020-05-22 15:56 UTC)

<p>I am on a Mac, yes. I was looking through the commits since May 5 and didn’t see anything obvious, so I was wondering why it doesn’t work.</p>
<p>I am using an external mouse, not a touchpad, if that makes a difference.</p>

---

## Post #11 by @hherhold (2020-05-22 16:04 UTC)

<p>In qSlicerMarkupsModuleWidget.cxx, I see a connection for right-click in the activeMarkupTableWidget. Is there a different place where the signal comes from the 3D view or a slice view (presumably to the same slot)?</p>

---

## Post #12 by @lassoan (2020-05-22 16:07 UTC)

<p>Markup node selection is initiated by the 2D/3D markups widget and it ends with calling <code>qSlicerMarkupsModuleWidget::setEditedNode</code>. Markups ID could be passed in the <code>context</code> argument.</p>

---

## Post #13 by @hherhold (2020-05-22 16:14 UTC)

<p>OK. But this <em>is</em> implemented already? I was mostly looking for where it might be not working. Sorry for my confusion!</p>

---

## Post #14 by @lassoan (2020-05-22 16:25 UTC)

<p>Yes, context menu on right-click is implemented and it works already. If the context menu does not appear for you then it is a bug.</p>

---

## Post #15 by @hherhold (2020-05-22 16:35 UTC)

<p>yeah, it does not appear to work. I’m right-clicking very carefully with an external mouse so it does not appear to be a trackpad/touchpad noisy-right-click-with-two-fingers issue.</p>

---

## Post #16 by @pieper (2020-05-22 16:50 UTC)

<p>Odd, it works fine for me on mac with either mouse or trackpad.</p>

---

## Post #17 by @muratmaga (2020-05-22 16:55 UTC)

<p>You are right clicking after the fiducial color changed from red to blue (meaning it is selected), right? Otherwise it doesn’t work? Any chance you might have interactions disabled?</p>

---

## Post #18 by @lassoan (2020-05-22 19:19 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="15" data-topic="11670">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>yeah, it does not appear to work.</p>
</blockquote>
</aside>
<p>Do you have a debug-mode build? It would be awesome if you could track this down. I would suspect that your mouse driver generates a mouse event between pressing and releasing the button, even if you don’t physically move the mouse (or maybe you move it by 0.00001mm) and that confuses the click detection logic here: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLViewInteractorStyle.cxx#L89" class="inline-onebox">Slicer/Libs/MRML/DisplayableManager/vtkMRMLViewInteractorStyle.cxx at main · Slicer/Slicer · GitHub</a>. If indeed this is the problem then it could be fixed by checking how much the mouse was moved instead of just detecting that a mouse move event was fired.</p>

---

## Post #19 by @hherhold (2020-05-22 20:06 UTC)

<p>OK, this is odd. This is an older file I’m working with, maybe from January or so. When I just download sample data (CTACardio), place a fiducial, and right click in the 3D view, it works fine.</p>
<p>I took a look at the fcsv file and for my older file that does not work, I do not have entries for associatedNodeID for most of the entries, whereas the newer one I just made from the demo data has vtkMRMLScalarVolumeNode1 for all fiducials.</p>
<p>I also have CoordinateSystem=0 at the top, whereas the file I just created has LPS.</p>
<p>I did try hand-changing the coordinate system to LPS but this moves all my fiducials, and right click still doesn’t work.</p>
<p>I also added vtkMRMLScalarVolumeNode1 (which is a real, correct node) to all lines and right click still doesn’t work.</p>
<p>I really do think this is some kind of pilot error (me), or possibly an old file incompatibility (less likely).</p>
<p>Any ideas?</p>
<p>Thanks!</p>

---

## Post #20 by @lassoan (2020-05-22 20:12 UTC)

<p>Can you upload the scene .mrb file that reproduces this somewhere and post the link here?</p>

---

## Post #21 by @hherhold (2020-05-22 20:22 UTC)

<p>Oy, the MRB is kinda big. Couple of GB. I can see if I can trim it down… It’s an insect, of course, so no worries about making it anonymous, ha ha.</p>
<p>It is NOT the fcsv file - I copied my FCSV file from my setup that does not work into the one I just created with CTACardio, and I can right-click and it works fine. Likewise, if I copy the F.fcsv file from CTCardio to my setup that does not work, and I can’t right click. So it’s something in the MRML file. I’m checking the 3 blocks that have to do with markups.</p>

---

## Post #22 by @lassoan (2020-05-22 20:34 UTC)

<p>Then try <a class="mention" href="/u/muratmaga">@muratmaga</a>’s suggestion of making sure that the markups node is not locked (Control points/Interaction in Views enabled).</p>

---

## Post #23 by @hherhold (2020-05-22 21:17 UTC)

<p>Interaction in views was enabled. Still didn’t work.</p>
<p>I was finally able to get it working by deleting the node, then re-loading it. I’m slowly looking through the diffs in the XML between the working and non-working ones and I’ll let you know if I find the smoking gun.</p>
<p>Thanks very much for your help!</p>

---

## Post #24 by @hherhold (2020-05-24 13:15 UTC)

<p>Just a quick follow-up on this. I wasn’t able to tell which bit of XML was making it fail, but it appears to be some file version incompatibility in the MRML file. It is a very simple workaround/fix though-</p>
<ol>
<li>Go to Data module</li>
<li>Delete markups node</li>
<li>Go to “Add data”</li>
<li>re-load markups fcsv file</li>
</ol>
<p>Murat <a class="mention" href="/u/muratmaga">@muratmaga</a> and Andras <a class="mention" href="/u/lassoan">@lassoan</a> - Thanks for taking the time to look at it. I can probably make up a mrb that reproduces it but because it’s such a simple procedure to update the file, I see very little benefit in tracking down what’s going on in the code, but let me know.</p>

---

## Post #25 by @lassoan (2020-05-24 14:35 UTC)

<p>Can you share the original scene that reproduces the problem? You can share a few-gigabyte scene file via OneDrive or Google Drive.</p>

---

## Post #26 by @lassoan (2020-05-25 13:34 UTC)

<p>Thanks to the example scene that <a class="mention" href="/u/hherhold">@hherhold</a> shared, we found a subtle error in subject hierarchy module’s context menu observation mechanism setup that is not <a href="https://github.com/Slicer/Slicer/commit/e4d8fcd5408ec5275d826dcc6a0dc4a3be07d46c">fixed</a>. With this fix, context menu now always appears when the markup is right-clicked.</p>

---

## Post #27 by @hherhold (2020-05-25 14:00 UTC)

<p>Thanks Andras! I took a quick look at the change to help get more familiar with the code - it probably would have taken me months to figure that out!</p>
<p>I did also notice something this morning - when I do right click on a markup node and use “Rename point…” to change the name, then save, it does not mark the markups node as having been changed. If you don’t notice this and then exit after saving, you lose all the name changes. If you do manually check the markups node in the save dialog, it does save.</p>
<p>Does the change you made to the hierarchy code possibly fix this? I can start a new topic with this as a bug if necessary.</p>
<p>Thanks again,</p>
<p>-Hollister</p>

---

## Post #28 by @lassoan (2020-05-25 15:02 UTC)

<p>No need to create a new topic, I’ve fixed this in</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/454d3e5925029c51c6569a5d7261c0fafec28482" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/454d3e5925029c51c6569a5d7261c0fafec28482" target="_blank">BUG: Fix markups node not being marked as modified after modifying points</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-05-25" data-time="15:22:20" data-timezone="UTC">03:22PM - 25 May 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank">
          <img alt="lassoan" src="https://avatars0.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
        
      </div>

      <div class="lines" title="changed 2 files with 16 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/454d3e5925029c51c6569a5d7261c0fafec28482" target="_blank">
          <span class="added">+16</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">After moving or renaming points, markups node was not marked as modified in Save dialog. Fixed by updating StorableModifiedTime when control...</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #29 by @hherhold (2020-05-25 15:48 UTC)

<p>Awesome! Thanks again!</p>

---
