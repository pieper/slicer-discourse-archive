---
topic_id: 1376
title: "Could Not Save My 3D Model As Stl"
date: 2017-11-04
url: https://discourse.slicer.org/t/1376
---

# Could not save my 3d model as STL

**Topic ID**: 1376
**Date**: 2017-11-04
**URL**: https://discourse.slicer.org/t/could-not-save-my-3d-model-as-stl/1376

---

## Post #1 by @sertacaksoy (2017-11-04 07:28 UTC)

<p>Hi Slicer Users:</p>
<p>I am relatively a new user and would like to have a piece of mind from more experienced users. So I generally use <strong>Editor</strong> to segment my ROI’s, and it has a fantastic saving feature which allows me to save my 3d model as STL. But lately I’ve been using <strong>Segment Editor</strong> to overcome more troublesome segmentations. But when I try to save my 3d model, STL is absent.  My aim is to have work with it on meshlab. If you have any suggestions or solutions It would be great.</p>
<p>Thanks  A Lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91e237a12178ec6c7454f5a16ad50adf9767a738.png" data-download-href="/uploads/short-url/kOxTTyFyUBi5JvQPXJjWumQhaYg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/91e237a12178ec6c7454f5a16ad50adf9767a738_2_690x388.png" alt="image" data-base62-sha1="kOxTTyFyUBi5JvQPXJjWumQhaYg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/91e237a12178ec6c7454f5a16ad50adf9767a738_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/91e237a12178ec6c7454f5a16ad50adf9767a738_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/91e237a12178ec6c7454f5a16ad50adf9767a738_2_1380x776.png 2x" data-dominant-color="787B83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 515 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @ihnorton (2017-11-04 10:36 UTC)

<p>see</p>
<aside class="onebox pdf">
  <header class="source">
      <a href="https://na-mic.org/w/images/a/a6/SegmentationFor3DPrinting_TutorialContestWinter2017.pdf" target="_blank" rel="nofollow noopener">na-mic.org</a>
  </header>
  <article class="onebox-body">
    <a href="https://na-mic.org/w/images/a/a6/SegmentationFor3DPrinting_TutorialContestWinter2017.pdf" target="_blank" rel="nofollow noopener"><span class="pdf-onebox-logo"></span></a>
<h3><a href="https://na-mic.org/w/images/a/a6/SegmentationFor3DPrinting_TutorialContestWinter2017.pdf" target="_blank" rel="nofollow noopener">SegmentationFor3DPrinting_TutorialContestWinter2017.pdf</a></h3>

<p class="filesize">2.52 MB</p>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2017-11-04 14:38 UTC)

<p>It surprises me that despite all the effort in creating tutorials, advising people on the forum, improving the user interface, etc., people still have difficulty finding STL export - but this is the reality… At this point, I’m tempted to accept the idea of putting a printer (or 3D printer) icon in the Segment Editor module GUI that would bring up a directory selector and all visible segments would be written to that folder as STL files. <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> <a class="mention" href="/u/pieper">@pieper</a>  What do you think?</p>

---

## Post #4 by @pieper (2017-11-05 19:08 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>At this point, I’m tempted to accept the idea of putting a printer (or 3D printer) icon in the Segment Editor module GUI</p>
</blockquote>
</aside>
<p>That makes sense to me.</p>
<p>The other option that occurred to me would be adding STL as a save option in the save dialog and doing the export then.  You’d need to have a convention for including the individual segment names to STL filenames.</p>

---

## Post #5 by @lassoan (2017-11-06 02:44 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="1376">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>The other option that occurred to me would be adding STL as a save option in the save dialog and doing the export then.</p>
</blockquote>
</aside>
<p>I agree that this would be probably intuitive for the user, but unfortunately this would only work for data export, not for saving data in the scene (always the master representation is saved into the scene, which is usually binary labelmap; STL cannot store all the necessary segment metadata), and the “Save data” dialog is used for both export and scene saving.</p>

---

## Post #6 by @pieper (2017-11-06 12:17 UTC)

<p>How about saving the master representation along with the STL files in that case?  Since a segmentation will already map to a collection of files adding another one shouldn’t be a big problem.</p>
<p>But it’s true that a lot of programs have separate Export and Save menu options so maybe we should split the concepts.  There are many node types one might want to export in various lossy formats.</p>

---

## Post #7 by @ihnorton (2017-11-06 14:53 UTC)

<p>How about an “Export” button in the Subject Hierarchy context menu – if it is a QAction it could probably then be hooked in Segmentations tree view easily? Ideally it would allow multi-selection, and hook into the Save dialog so that only those selected nodes are offered.</p>
<p>Perhaps “important node types” could also register <code>Export to ...</code> and use that option to change the default file type for any selections of their class in the save dialog?</p>

---

## Post #8 by @cpinter (2017-11-06 15:00 UTC)

<p>I think the explicit button would be a more bulletproof solution, because if people cannot do a search for STL on discourse (there are at least 10 threads about this by now, so it’s easy to find if someone bothers to search), they won’t find the STL option in the save dialog either. The default saving option must remain the master representation, otherwise there will be bigger surprises (loading back will result in a different display and lossy data in the master representation). Saving the scene with both the master and STL could be a solution, but I think scene saving does not happen with the intent of using individual files from that in other programs (like for those who want do do 3D printing), but to load it back to Slicer later. Also, having “stray” files along with the scene that do not belong to any storage node is a loss of coherence in my view.</p>
<p>So in summary, I think STL is definitely an export type operation, and adding a button for it in Segment Editor would probably be both sufficient and easy enough to find.</p>

---

## Post #9 by @lassoan (2017-11-06 16:03 UTC)

<p>Adding an “Export for 3D printing” action in the subject hierarchy tree would be useful, but I agree with Csaba that it would still not be easy enough to find for users.</p>
<p>What do you think about adding it under the “Segmentations…” button menu? Would it be easy enough to find?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e085e81d8601bc689e67a0c47ccb6f62f769e363.png" alt="image" data-base62-sha1="w2dQwuIRQL6an0LnfXJW6A5qEGn" width="576" height="239"></p>
<p>Or, should we add a top-level button instead?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b67ffb3eac2daba7c49d618c2fee981e3eae282c.png" alt="image" data-base62-sha1="q2t66RGqsgHtgpVkIw7yWyvn9HC" width="544" height="213"></p>

---

## Post #10 by @cpinter (2017-11-06 17:11 UTC)

<p>There are already many buttons, but still I lean towards the dedicated button, so that it’s super easy to find.</p>
<p>We could also pin a topic to the main page like “FAQ: Save segmentation to STL”. So even people who don’t use search would see this (if they look), because you need to open the page to post a question.</p>

---

## Post #11 by @lassoan (2018-03-20 18:31 UTC)

<p>Implemented <a href="https://github.com/Slicer/Slicer/pull/919">direct STL file export from segmentation</a> - will be available in tomorrow’s nightly build.</p>

---
