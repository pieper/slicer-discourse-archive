---
topic_id: 12415
title: "Python Module Logic Class"
date: 2020-07-07
url: https://discourse.slicer.org/t/12415
---

# Python Module Logic Class

**Topic ID**: 12415
**Date**: 2020-07-07
**URL**: https://discourse.slicer.org/t/python-module-logic-class/12415

---

## Post #1 by @vertebra (2020-07-07 13:18 UTC)

<p>Hello! We are working on testing our module, but it only sets the image to the FA.nrrd because of the ScriptedLoadableModuleTest. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3554cf7f97620906c4c478ae1bbe0fb215ef1162.png" data-download-href="/uploads/short-url/7BN0ITskuMFnSPs6mzN0pcQ8A8y.png?dl=1" title="Screen Shot 2020-07-07 at 8.57.32 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3554cf7f97620906c4c478ae1bbe0fb215ef1162_2_690x431.png" alt="Screen Shot 2020-07-07 at 8.57.32 AM" data-base62-sha1="7BN0ITskuMFnSPs6mzN0pcQ8A8y" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3554cf7f97620906c4c478ae1bbe0fb215ef1162_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3554cf7f97620906c4c478ae1bbe0fb215ef1162_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/3554cf7f97620906c4c478ae1bbe0fb215ef1162_2_1380x862.png 2x" data-dominant-color="7A7B87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-07 at 8.57.32 AM</span><span class="informations">1440×900 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see, our code uses a pre-placed fiducial point to create a segment around it(called lumbar in this case). Then it sets the parameters for the local threshold function, but the function doesn’t complete. What I mean by that is it sets the parameters but doesn’t control-click/run the function. We think this is because of our logic function.</p>
<p>Does anyone know how to alter the run function in the Scripted Loadable Module Logic to actually run your own program? Is that where we put in:</p>
<p>effect.self().apply(ijkPoints)</p>
<p>If so, how do we run all the functions in our main class?</p>
<p>Thanks!</p>

---

## Post #2 by @vertebrae (2020-07-07 13:33 UTC)

<p>(post withdrawn by author, will be automatically deleted in 24 hours unless flagged)</p>

---

## Post #5 by @vertebrae (2020-07-07 18:51 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> do you have a solution for this?</p>

---

## Post #6 by @lassoan (2020-07-07 19:26 UTC)

<p>FA.nrrd is an example that was used in old templates. Please use the latest module template.</p>
<p>You can use any test data - from Slicer’s sample data sets or anything that you upload into your own repository.</p>
<p>I’ve already described <a href="https://discourse.slicer.org/t/python-editing-feature-size-local-threshold/12393/16">in a different topic</a> how to run <code>apply</code> method of Local threshold effect. If you still have problems with that then please ask there. Provide link to your source code, if you have questions about why your code is not working.</p>

---

## Post #7 by @lassoan (2020-07-07 20:03 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/python-editing-feature-size-local-threshold/12393/18">Python - Editing Feature Size Local Threshold</a></p>

---
