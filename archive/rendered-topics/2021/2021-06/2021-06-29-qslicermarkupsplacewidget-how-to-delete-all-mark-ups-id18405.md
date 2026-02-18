# qSlicerMarkupsPlaceWidget - How to delete all mark-ups

**Topic ID**: 18405
**Date**: 2021-06-29
**URL**: https://discourse.slicer.org/t/qslicermarkupsplacewidget-how-to-delete-all-mark-ups/18405

---

## Post #1 by @seanchoi0519 (2021-06-29 18:02 UTC)

<p>Trying to learn the qSlicerMarkupsPlaceWidget Class (<a href="https://apidocs.slicer.org/master/classqSlicerMarkupsPlaceWidget.html#a212ef3f3e7f44e87462d077957d070d5" class="inline-onebox" rel="noopener nofollow ugc">Slicer: qSlicerMarkupsPlaceWidget Class Reference</a>).</p>
<p>Everything is good however I’d like to modify the delete button so that it deletes ALL mark-ups instead of just the last one. I’d like to modify this on my .py file however it seems like the code for Markups module is done by C++.</p>
<p>Not only that, as it currently stands, if I click the delete button (delete last added markup point), it only deletes the sphere balls, but not the line. I’d like to delete the line as well.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dac8818cba2566cc78333be7b6628603abc6bd2.jpeg" data-download-href="/uploads/short-url/4evuCKAbHnhjj0s66xVXFNTFYxs.jpeg?dl=1" title="Screen Shot 2021-06-30 at 4.00.20 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dac8818cba2566cc78333be7b6628603abc6bd2_2_637x500.jpeg" alt="Screen Shot 2021-06-30 at 4.00.20 AM" data-base62-sha1="4evuCKAbHnhjj0s66xVXFNTFYxs" width="637" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dac8818cba2566cc78333be7b6628603abc6bd2_2_637x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dac8818cba2566cc78333be7b6628603abc6bd2_2_955x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dac8818cba2566cc78333be7b6628603abc6bd2_2_1274x1000.jpeg 2x" data-dominant-color="C5C5C4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-30 at 4.00.20 AM</span><span class="informations">1416×1110 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here is my code currently:<br>
lineNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsLineNode”, ‘L’)<br>
w=slicer.qSlicerMarkupsPlaceWidget()<br>
w.setMRMLScene(slicer.mrmlScene)<br>
w.setCurrentNode(lineNode)<br>
w.buttonsVisible=False<br>
w.placeButton().show()<br>
w.deleteButton().show()<br>
w.setDeleteAllMarkupsOptionVisible(True) # this doesn’t seem to change anything<br>
w.show()<br>
w.onVisibilityButtonClicked()<br>
lineNode.GetDisplayNode().SetGlyphScale(0.5)</p>
<p>Thanks in advance</p>

---

## Post #2 by @smrolfe (2021-06-29 19:36 UTC)

<p>The delete all points option shows up with a long mouse press. There is an <a href="https://github.com/Slicer/Slicer/pull/5325" rel="noopener nofollow ugc">update of this widget</a> in-progress that will change this to a drop down menu arrow, since this interface option is rarely used and can be confusing.</p>
<p>Which version of Slicer are you using? The place button should be updating with the current markup type, and deleting the line and last point with the delete button, or the line and both points with the delete all option. This was working for me with your code snippet.</p>

---

## Post #3 by @seanchoi0519 (2021-06-30 05:31 UTC)

<p>Thanks for your reply Sara. Here is a video of what I’m experiencing: <a href="https://drive.google.com/file/d/1fxfweDUOilw1sWqsZEkKXfBG56vtKMXl/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">deletemarkupvideo.mov - Google Drive</a></p>
<p>As we can see, the line is persisting although the spheres can be removed.<br>
Also, is there a way for me to edit so that instead of the long mouse press, I can delete all using a single mouse press? in the .py file.</p>

---

## Post #4 by @seanchoi0519 (2021-06-30 05:33 UTC)

<p>Lastly, instead of summoning a separate tab window for the qSlicerMarkupsPlaceWidget, is there a way for me to have it stay within the 3D scene view window only?</p>

---

## Post #5 by @smrolfe (2021-06-30 17:18 UTC)

<p>Are you using the stable version of 3D Slicer? This behavior is caused by the widget not updating to the correct markup type, but I can’t replicate this error on my end.</p>
<p>You could incorporate this widget in a module, but these functions will also be available in the main toolbar in the upcoming markups update.</p>

---

## Post #6 by @seanchoi0519 (2021-07-01 06:41 UTC)

<p>Very strange. Yes I’m using the latest stable version - 4.11.20210226<br>
Could it be something related to my code? If you wouldn’t mind copying &amp; pasting my code into yours.</p>
<p>And great yes I plan to incorporate the widget into my module. Would you be able to provide a brief guidance on how I can do this programmatically? Any example project that incorporates qSlicerMarkupsPlaceWidget programmatically would be great</p>
<p>Thanks a lot Sara!</p>

---

## Post #7 by @seanchoi0519 (2021-07-01 06:57 UTC)

<p>Another weird thing I noticed was, on my python console, I get an error that it does not recognize the .onVisibilityButtonClicked() function</p>
<p>AttributeError: qSlicerMarkupsPlaceWidget has no attribute named ‘onVisibilityButtonClicked’</p>
<p>However without adding this piece of code I actually cannot see the widget at all - so I’m not sure why it would register it as an error?</p>

---

## Post #8 by @seanchoi0519 (2021-07-01 16:06 UTC)

<p>I’ve downloaded the preview version 4.13.0-2021-06-30 and the ruler function seems to work fine! Thanks for all your help.</p>

---

## Post #9 by @seanchoi0519 (2021-07-01 17:09 UTC)

<p>Hi Sara, is it just me or has placing a fiducial point become a little buggy after this update? I feel like even if I move just a little bit after I click, or don’t hold the mouse click long enough, the fiducial point does not get placed. Has there been a change in code with regards to this?</p>

---

## Post #10 by @smrolfe (2021-07-01 17:17 UTC)

<p>Great! If you are adding the qSlicerMarkupsPlaceWidget to a module, it might be helpful to check out the <a href="https://github.com/Slicer/Slicer/blob/0094e9a35bd266cc8b0e677858dabce797c9928f/Modules/Loadable/Markups/Widgets/qSlicerSimpleMarkupsWidget.cxx" rel="noopener nofollow ugc">SimpleMarkupsWidget</a> which uses this widget to see how to set the parameters.</p>
<p>I am also working on an update to the qSlicerMarkupsPlaceWidget which should be available in the next stable version, that will add it to the main Slicer toolbar.</p>

---

## Post #11 by @muratmaga (2021-07-01 17:28 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="9" data-topic="18405" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>Hi Sara, is it just me or has placing a fiducial point become a little buggy after this update? I feel like even if I move just a little bit after I click, or don’t hold the mouse click long enough, the fiducial point does not get placed. Has there been a change in code with regards to this?</p>
</blockquote>
</aside>
<p>This is probably what you are seeing: <a href="https://discourse.slicer.org/t/feedback-requested-requirements-to-place-a-fiducial/18407/15" class="inline-onebox">Feedback requested: Requirements to place a fiducial - #15 by tomekcz</a></p>

---

## Post #12 by @seanchoi0519 (2021-07-01 17:31 UTC)

<p>Great, look forward to it! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #13 by @seanchoi0519 (2021-07-01 17:32 UTC)

<p>Yes it is! I have to agree with the people, that for me it is not a welcomed change <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #14 by @tomekcz (2021-07-01 17:33 UTC)

<p>Yes agreed. I think we can come up with a better way.</p>
<p>Just need a consensus on how to overload the Left-click button properly so that the 3D view can be manipulated at the same time as point placement.</p>

---

## Post #15 by @seanchoi0519 (2021-07-01 18:08 UTC)

<p>Hmmm, after the update, I’m still having an issue with the delete button. Is there no way for me to delete all of the lines present?</p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1ipaEY62-aT-HNqQaFBNl4NyltG89mpN4/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1ipaEY62-aT-HNqQaFBNl4NyltG89mpN4/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
    
<div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://lh4.googleusercontent.com/TX63Lqpe0Bp685t_iemhDNLT6geHN-MqGu04mzcMz2H6vG4O4cVWlwrpa1tokbXRXHI=w1200-h630-p" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://drive.google.com/file/d/1ipaEY62-aT-HNqQaFBNl4NyltG89mpN4/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">markupdelete.mov (video)</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @smrolfe (2021-07-01 18:40 UTC)

<p>With the current behavior, the “delete all” button removes points from the current markups node only. Removing all points from active and non-active nodes could potentially be useful, but also risky.</p>
<p>Are there cases where a simple “clear scene” would not work?</p>

---

## Post #17 by @seanchoi0519 (2021-07-02 07:18 UTC)

<p>Oh okay. So is there no way for me to delete all of the lines using the delete button?<br>
I do have models I’d like to keep in the scene so clear scene would not be so ideal.</p>

---

## Post #18 by @smrolfe (2021-07-02 19:51 UTC)

<p>Not currently. Also note that it does not delete the line node itself, will just the control points in the node.</p>

---

## Post #19 by @lassoan (2021-07-09 15:07 UTC)

<p>You can go to Markups or Data module, select all the markups in the tree that you want to delete, then right-click and select Delete.</p>

---
