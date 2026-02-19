---
topic_id: 17917
title: "Modifications To Cardiac Module Or Suggestion To Module For"
date: 2021-06-02
url: https://discourse.slicer.org/t/17917
---

# Modifications to Cardiac module or suggestion to module for annotation of geometrical components

**Topic ID**: 17917
**Date**: 2021-06-02
**URL**: https://discourse.slicer.org/t/modifications-to-cardiac-module-or-suggestion-to-module-for-annotation-of-geometrical-components/17917

---

## Post #1 by @hmaguilera (2021-06-02 09:33 UTC)

<p>Hi,<br>
I am new to 3D Slicer and I would like to use it to study the mitral valve from 3D echocardiography.<br>
What I am looking for may already be an available extension, but I have not found it. What I would like is the cardiac module, with some modifications. Is it possible to add features to an extension? Currently, I am using a Matlab GUI that i have developed to extract geometrical components, but the view manipulation and volume viewing are not as good as in 3D Slicer. Therefore, it would be nice to incorporate some of my features in a module if it is not already an available extension.</p>
<p>I want to extract the cardiac components for all time-frames in the cardiac cycle. In the end I want to export the components as CSV’s or similar to run Matlab codes on the components. However, to do so I need it in a specific format, and I also want to be able to annotate in a certain way. What I want to do is:</p>
<p>For each individual time-frame i want to annotate geometrical components. I want to extract them by annotating one component at a time and store it based on the current frame in terms of 3D coordinates. E.g. I would like to extract the posteromedial papillary muscle head location from frame 1:end, before annotating the other papillary muscles. (I like this way of annotating because then I am able to follow the individual component through the cycle). Then as i move through time I also want the annotated components in that time-frame to be plotted in the volume. I also want to be able to delete and modify annotated features. (E.g. if i have annotated 10 points around the annular circumference I want the possibility to move through time and only modify the locations of e.g. the annular point at the anterior horn to update the annular spline.)</p>
<p>I want to be able to turn on e.g. Annulus mode, and then the extension should store the points in the current time frame and also plot in the current time frame.</p>
<p>Here is a Pseudocode of what i want to do for one of the features. May be easier to understand.</p>
<pre><code class="lang-auto">get Frame
get Points %annotated on volume

append the Points to Annulus(frame) if anything is annotated
    
if Annulus(frame) contains more than X points
    create spline of annulus points
end

in current time frame:
plot Annular points
plot Spline

store Annular points at that time frame in CSV or structure

if delete/modify mode
get Point
find  index of Point closest to Annulus(frame) points
delete  or swap Annulus(frame).index

update and plot

</code></pre>

---

## Post #2 by @lassoan (2021-06-04 05:07 UTC)

<aside class="quote no-group" data-username="hmaguilera" data-post="1" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>Is it possible to add features to an extension?</p>
</blockquote>
</aside>
<p>Yes. Entire 3D Slicer and all extensions are open-source and freely usable and modifiable, customizable, extensible.</p>
<aside class="quote no-group" data-username="hmaguilera" data-post="1" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>For each individual time-frame i want to annotate geometrical components.</p>
</blockquote>
</aside>
<p>You can annotate one slice (add points, curves, etc.) then use Sequences module to create a time sequence of each annotation that you want to specify for each time point: click the green <code>+</code> button to create a new sequence, then select the node (e.g., curve node) as proxy node and check the “Save changes” checkbox to sautomatically save the current state of the node for each time point of the image sequence.</p>
<aside class="quote no-group" data-username="hmaguilera" data-post="1" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>E.g. I would like to extract the posteromedial papillary muscle head location from frame 1:end, before annotating the other papillary muscles. (I like this way of annotating because then I am able to follow the individual component through the cycle).</p>
</blockquote>
</aside>
<p>This should work well. When you step to the next image frame (Ctrl+Shift+Right-arrow) then the current position of the node is copied to this new frame, so you can just adjust the position of the papillary muscle tip.</p>
<aside class="quote no-group" data-username="hmaguilera" data-post="1" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>I also want to be able to delete and modify annotated features. (E.g. if i have annotated 10 points around the annular circumference I want the possibility to move through time and only modify the locations of e.g. the annular point at the anterior horn to update the annular spline.)</p>
</blockquote>
</aside>
<p>You can replay all the time-varying nodes in slice and 3D views, make adjustments, etc., so this should be no problem at all.</p>
<p>You can use “Valve annulus analysis” module of SlicerHeart extension to very quickly and accurately define the annulus curve. It still uses slightly older markups infrastructure (at that time closed curves were not available, therefore we used markups fiducial points to designate a curve), and the module may be a bit heavyweight if all you need is the annulus curve and you want to mark it on many image frames. Therefore, you may consider using the “Valve View” module instead, which allows quick marking of annulus contour points by automatically rotating the views around the annulus axis when a curve point is placed.</p>
<aside class="quote no-group" data-username="hmaguilera" data-post="1" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>I want to extract the cardiac components for all time-frames in the cardiac cycle. In the end I want to export the components as CSV’s or similar to run Matlab codes on the components.</p>
</blockquote>
</aside>
<p>Markups are saved as json by default. A time sequence of a markup will be saved in a zip file (with .mrb file extension that you can rename to .zip and unzip it). You can easily parse this json file and save the point coordinates into a csv file - see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#use-markups-json-files-in-python-outside-slicer">example here</a>.</p>
<p>On a side note: Using Matlab made sense 5-10 years ago, but Python has become so much better in so many aspects that Matlab is no longer relevant in all but a few niche applications. By switching to Python you will start acquiring essential skills (Python programming experience is expected for most R&amp;D jobs nowadays), you get access to several magnitudes more tools and libraries, get much more opportunity to find collaborators and share your work with others so that you can make an impact.</p>

---

## Post #3 by @hmaguilera (2021-06-09 11:07 UTC)

<p>Hi,<br>
Thank you very much for this detailed response.<br>
Some follow up questions:</p>
<p>When I annotate the annulus at one time-instance using fiducials, how do I store those points in a sequence? There are many choices for the Proxy Node, and can I select all annotated points for that sequence?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e845966b2c4ada8e79362c932e1eced96a89193e.png" alt="Fiducials_OneTime" data-base62-sha1="x8LRyzczYgSYuONVN2v5S1MDJAG" width="684" height="395"> and store them in one individual sequence? Currently I am not able to do so.</p>
<p>As mentioned, I want to annotate all time-frames. Therefore, I only want the annotated annulus at each individual time frame to be plotted in slicer view.  Now, when I annotate using fiducials, the annular points remain plotted when I move forward in time. Same with the annular curves when I use the "Valve annulus analysis” module of SlicerHeart extension. But this might be because I have not entirely understood how to use sequences.</p>
<p>The ideal situation would be to enter an annotation module that understands and reads the current frame. And based on the frame and the chosen anatomical component, we are able to store the points and also plot them in their respective frame. I have started to create this now but are trying to figure out how to:</p>
<p>Is there a way to extract the current frame based on<br>
Is it possible to extract the annulus at all time-frames and additionally store them based on the volume name so that it can be accessed and plotted when opening the volume in this “mode”?</p>
<p>Thanks again!<br>
Best,<br>
HM</p>

---

## Post #4 by @lassoan (2021-06-09 13:05 UTC)

<aside class="quote no-group" data-username="hmaguilera" data-post="3" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>When I annotate the annulus at one time-instance using fiducials, how do I store those points in a sequence? There are many choices for the Proxy Node, and can I select all annotated points for that sequence?</p>
</blockquote>
</aside>
<p>Use a Closed Curve markup node for annulus curve. Choose this curve node as proxy node.</p>
<aside class="quote no-group" data-username="hmaguilera" data-post="3" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>The ideal situation would be to enter an annotation module that understands and reads the current frame. And based on the frame and the chosen anatomical component, we are able to store the points and also plot them in their respective frame.</p>
</blockquote>
</aside>
<p>Sequences module does exactly this. You just need to add a sequence node to the image sequence’s browser node and set the markups curve as a proxy node.</p>
<aside class="quote no-group" data-username="hmaguilera" data-post="3" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>Is there a way to extract the current frame based on<br>
Is it possible to extract the annulus at all time-frames and additionally store them based on the volume name so that it can be accessed and plotted when opening the volume in this “mode”?</p>
</blockquote>
</aside>
<p>These are all straightforward to do. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#browse-a-sequence-and-access-currently-displayed-nodes">script repository</a>.</p>

---

## Post #5 by @hmaguilera (2021-06-10 11:55 UTC)

<p>Thanks again for the quick answer.</p>
<p>I found this code in the script repository:</p>
<pre><code class="lang-auto">     interactionNode = slicer.app.applicationLogic().GetInteractionNode()
     selectionNode = slicer.app.applicationLogic().GetSelectionNode()
     selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLMarkupsFiducialNode")
     fiducialNode = slicer.vtkMRMLMarkupsFiducialNode()
     slicer.mrmlScene.AddNode(fiducialNode)
     fiducialNode.CreateDefaultDisplayNodes()
     selectionNode.SetActivePlaceNodeID(fiducialNode.GetID())
     interactionNode.SetCurrentInteractionMode(interactionNode.Place)
</code></pre>
<p>This enables me to add new MarkupsFiducials, and also adds the annotated fiducials in a new category each time I run the code (MarkupsFiducial_1, MarkupsFiducial_2 etc) However, can I pre-define the name? And also append to one with a given name? I know this is possible in the Fiducial Registraion Wizard, but I want to define it in a module.</p>
<p>Let’s say I run the mentioned code above, but instead of getting a category names MarkupsFiducial_X I name it “Annulus”. And if i want to add more fiducial markers to that category i simply run the code again, and it appends the markers to the pre-named folder. I bet this is possible, but can not seem to find out how to do it.</p>
<p>Best,<br>
HM</p>

---

## Post #6 by @lassoan (2021-06-10 13:56 UTC)

<p>You don’t need to create the markups fiducial using Python scripting - you can create it in Markups module (click on new closed curve button, double click on the new node in the tree below, and type <code>annulus</code>) or using the toolbar.</p>
<p>You must not create a new annulus node for each time point, because then you would not be able to synchronized recording/replay of the moving annulus curve and the moving image. Just create one annulus curve node and add it as a proxy node in sequences module (to the same sequence browser as the image). If you find this too complicated (create a new sequence then choose the curve node as proxy node) then let us know and then we’ll brainstorm about how to simplify the user interface to make this easier.</p>
<p>In a week or two, <a class="mention" href="/u/smrolfe">@smrolfe</a> will integrate her <a href="https://github.com/Slicer/Slicer/pull/5325">markups improvements</a>, which should further improve things for you: there will be a new dedicated markups toolbar that will make it easy to add/edit/switch between markups; and you will be able to predefine names for markup control points.</p>

---

## Post #7 by @hmaguilera (2021-06-11 10:23 UTC)

<p>Hi,<br>
Thanks again for the reply!</p>
<p>I saw the Markups module, and it works nicely. I have tried it out more this morning, and it together with sequence module has the features that I was looking for. Is it possible though to display several modules at once? Let’s say cardiac view + Markups module?</p>
<p>I have gotten a bit more familiar with the sequence module now as well. However, I have some issues with the annular annotation for each time-step, at least when I use closed curve markups. The reason being that if annotate using one rotation axis, and during annotation alter this axis slightly by slicing in one of the two planes which control the rotation axis, I am not able to find the closed curve markup points because I now only see the curve. The same will be the issue when i annotate papillary muscles, as I might loose sight of the point if i slice through the plane.<br>
Something I therefore wanted to implement was a swap point feature. Where I am able to enter a mode related to the Closed Curve, or simply Fiducial markers, and swap my annotated point with the point closest to it (at that time-frame). This would speed up the annotation process, and for the Closed Curve would make it independent of the rotation axis choice. Changing the rotation axis to be in the middle of the annulus often helps, but if we loose the control points to alter the Closed Curve this may not work well without a swap point mode.</p>
<p>For my purpose I have to be consistent with the placement of the points (near the same location), as I use the information as boundary conditions in finite element analysis of the mitral valve.</p>
<p>I am looking forward to the markups improvements.<br>
Thanks again!</p>

---

## Post #8 by @lassoan (2021-06-11 18:19 UTC)

<aside class="quote no-group" data-username="hmaguilera" data-post="7" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>Is it possible though to display several modules at once? Let’s say cardiac view + Markups module?</p>
</blockquote>
</aside>
<p>Valve view module remains active when you switch to a different module, so most likely you can just switch to markups module. If you have to access features from multiple modules then you can create a simple Python scripted module with a custom GUI, which contains all the GUI widgets that you need. There are high-level widgets, such as markups table or subject hierarchy tree.</p>
<aside class="quote no-group" data-username="hmaguilera" data-post="7" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>The reason being that if annotate using one rotation axis, and during annotation alter this axis slightly by slicing in one of the two planes which control the rotation axis, I am not able to find the closed curve markup points because I now only see the curve.</p>
</blockquote>
</aside>
<p>To avoid any bias (caused by incorrect point marking in previous time point), it is probably safer to restart the curve from scratch for each time point. If you are not worried about bias and just want to slightly adjust the curve for each time point then you can go to Markups module / Control points section, enable “Click to jump slices” and check position of each point by clicking on it, then moving it in slice views (after you drag-and-dropped the point, you can click on it to show the new position in all other views).</p>
<p>You can insert points into a curve by Ctrl+Left-click and you could add a Python script that would observe the curve and remove the closest point to the new point, but probably the other solutions described above are better.</p>
<p>You can also compute the annulus curve positions and papillary muscle base positions automatically from a single frame, using Sequence Registration extension module (which can compute displacement field of across a 3D volume sequence). We tested this for the annulus markup on 4D ultrasound images and it worked very well.</p>
<p>It cannot track the leaflet motion though (as the displacement field is too discontinuous where the leaflets coapt), so if you need to track full leaflet motion then you need to segment the leaflets on each frame. We have neural networks for segmenting leaflets automatically that we will finalize and release during the <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/Projects/DeepHeart/">upcoming Slicer Project week #35</a>. This project week will be still virtual, so you should be able to join easily. We have lots of additional valve analysis tools that we are releasing progressively (as we complete studies and get the results published).</p>

---

## Post #9 by @hmaguilera (2021-06-15 11:16 UTC)

<p>Hi,<br>
For the annulus annotation, all works perfectly now!</p>
<p>For the papillary muscles, you mentioned above that it was possible to create a sequence of one point(Papillary Muscle Tip)<br>
I tried creating a fiducial marker and create a sequence of it. But I am not able to choose the annotated Fiducial marker as a proxy-node in the Sequence module.  Only the MarkupFiducialDisplay is possible to choose as proxy node.<br>
Am i doing something wrong?</p>
<p>HM</p>

---

## Post #10 by @lassoan (2021-06-15 17:23 UTC)

<aside class="quote no-group" data-username="hmaguilera" data-post="9" data-topic="17917">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/bc8723/48.png" class="avatar"> hmaguilera:</div>
<blockquote>
<p>I tried creating a fiducial marker and create a sequence of it. But I am not able to choose the annotated Fiducial marker as a proxy-node in the Sequence module. Only the MarkupFiducialDisplay is possible to choose as proxy node.<br>
Am i doing something wrong?</p>
</blockquote>
</aside>
<p>There was a bug that prevented selection of markups fiducial nodes as proxy nodes. It is fixed in recent Slicer Preview Releases.</p>

---

## Post #11 by @hmaguilera (2021-06-16 06:19 UTC)

<p>Ok, thanks!<br>
When I initially downloaded Slicer I installed the Stable Release 4.11, which is the release I have been working with.<br>
I have now installed 4.13. Problem is now that it is not able to load DICOM from a GE machine, even though I follow the instructions given here: <a href="https://github.com/SlicerHeart/SlicerHeart#loading-various-3d4d-ultrasound-images-using-image3dapi" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerHeart/SlicerHeart: 3D Slicer extension for cardiac analysis</a><br>
This worked perfectly fine for the 4.11 release, and I am now not able to load DICOMS in 4.13 that I loaded in 4.11 correctly. Instead I get the volumes displayed as in the figure.</p>
<p>I have also tried to uninstall all Slicer versions, and reinstall. Moreover, I have renamed the files to .3dus.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c47c75b84e0a70156bdd44f2429092d4ae17bad3.jpeg" alt="image" data-base62-sha1="s2ceLC3bvE2YcKx1sRy3RHRu5B9" width="440" height="327"></p>
<p>For this version, the problem seems to be that I am not able to add the extension SlicerHeart. I get the following error code: No extensions found for win:64-bit, revision: ‘29979’. Please try a different combination</p>

---

## Post #12 by @hmaguilera (2021-06-16 10:45 UTC)

<p>Suddenly I was able to download SlicerHeart, and the problem was resolved!</p>

---

## Post #13 by @lassoan (2021-06-16 20:57 UTC)

<p>Extensions for Slicer Preview Releases usually appear around 2am and extensions are continuously added to it until about 11am. So, there is about a 9 hour gap between 2am-11am EST when the latest Slicer Preview Release does not have all the extensions yet. We are in the process of reworking the Slicer download site and we will resolve this (delay the release download until all extensions become available).</p>
<aside class="onebox githubissue">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/4976" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4976" target="_blank" rel="noopener">Show new Slicer Preview Release on download page when extension builds are completed</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-11" data-time="18:52:37" data-timezone="UTC">06:52PM - 11 Jun 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In certain timezones (most of Europe) there is a high chance that people don’t f<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ind any extensions for the release they have just downloaded.

It should be possible to somehow synchronize the time the new Slicer Preview Release package shows up on the download page - with the time when extension builds are complete.

Maybe it could be as simple as having an embargo period between 10pm EST and 12pm EST: packages that are uploaded during this time would all show up at the end of the period (at 12pm EST).

See this discussion: https://discourse.slicer.org/t/extension-manager-problems/11946/5?u=lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
