# Merging Prostate Dose with Planning CT using segmented objects

**Topic ID**: 7735
**Date**: 2019-07-24
**URL**: https://discourse.slicer.org/t/merging-prostate-dose-with-planning-ct-using-segmented-objects/7735

---

## Post #1 by @hexagram (2019-07-24 01:54 UTC)

<p>Hi, I have two imaeges in DICOM which I need to import into slices. The two images are a prostate dose (treatment plan) and a patient CT featuring segmented a prostate. The prostate dose is of a different size than the patient CT, and I am trying to re-size the dose to fit inside the CT such that the segmented prostates on both the dose and the CT overlap with one another.</p>
<p>Here is what I have already done:</p>
<ol>
<li>I have successfully imported the Dose, CT, and segments into slicer using the SlicerRT extension for DICOM images.</li>
<li>I then right click the Dose (in the data tree) and click ‘Register this’, I right click the CT register the Dose using  Interactive Landmark Registration. This is where I am stuck</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/511e910c1d72edf1eecf87711d59e19a98112092.png" data-download-href="/uploads/short-url/bzCa9mroPikHs3FDBLUwvXgxC2C.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/511e910c1d72edf1eecf87711d59e19a98112092_2_690x415.png" alt="image" data-base62-sha1="bzCa9mroPikHs3FDBLUwvXgxC2C" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/511e910c1d72edf1eecf87711d59e19a98112092_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/511e910c1d72edf1eecf87711d59e19a98112092_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/1/511e910c1d72edf1eecf87711d59e19a98112092_2_1380x830.png 2x" data-dominant-color="7AB172"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1565×943 482 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In the bottom row after going through this process I can see the CT image overlaid with the Dose image (which I assume means that they have been sucessfully co-registered), however I can’t find any way to access this image in a file. It doesn’t appear in the tree as far as I can tell. I see a “Prostate dose-transformed” volume in the data tree however I cannot view it at the same time as the CT volume (checking one volume immediately unchecks another, thereby preventing the overlay of images I briefly see yet cannot access).</p>
<p>So, how do I actually access the co-registered images? Does the procedure I have tried even make sense or am I on the wrong track altogether? I have tried the tutorials but they were not really designed for this type of problem so I was not able to understand co-registration very well through them.</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-07-24 20:38 UTC)

<aside class="quote no-group" data-username="hexagram" data-post="1" data-topic="7735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hexagram/48/4250_2.png" class="avatar"> hexagram:</div>
<blockquote>
<p>It doesn’t appear in the tree as far as I can tell. I see a “Prostate dose-transformed” volume in the data tree however I cannot view it at the same time as the CT volume (checking one volume immediately unchecks another, thereby preventing the overlay of images I briefly see yet cannot access).</p>
</blockquote>
</aside>
<p>You can display two volumes (foreground and background) in slice viewers. From the data module you can only set the background volume and you need to use the slice view controllers to set a foreground volume. See Slicer 4.10 <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Data_Loading_and_3D_Visualization">Data loading and visualization tutorial</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerRT#Comprehensive_tutorials">SlicerRT tutorials</a> for step-by-step instructions.</p>

---

## Post #3 by @Cody_Xie (2021-10-08 12:18 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="7735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>4.10 <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Data_Loading_and_3D_Visualization" rel="noopener nofollow ugc">Data loading and visualization tutorial</a></p>
</blockquote>
</aside>
<p>Sorry Andras, but the link for ‘Slicer 4.10 Data loading and visualization tutorial’ is no longer available. Could you tell me where I can see it now? Many thanks in advance!</p>

---

## Post #4 by @lassoan (2021-10-08 13:21 UTC)

<p>You can use the more recent Slicer 5.0 tutorial now (with the latest Slicer Preview Release).</p>
<p>We’ll fix the link for the 4.10 tutorial anyway (see <a href="https://github.com/Slicer/Slicer/issues/5796" class="inline-onebox">Re-home data organized in `NA-MIC/Public/SampleData` · Issue #5796 · Slicer/Slicer · GitHub</a>).</p>

---

## Post #5 by @Cody_Xie (2021-10-08 13:45 UTC)

<p>Dear Andras,</p>
<p>thank you so much for your quick reply!</p>
<p>May I know if this is the document you mean?<br>
chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/viewer.html?pdfurl=https%3A%2F%<a href="http://2Fspujol.github.io" rel="noopener nofollow ugc">2Fspujol.github.io</a>%2FSlicerVisualizationTutorial%2FSlicerVisualizationTutorial_SoniaPujol.pdf&amp;clen=4905101&amp;chunk=true</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2021-10-08 13:53 UTC)

<p>Yes, this one: <a href="https://spujol.github.io/SlicerVisualizationTutorial/">https://spujol.github.io/SlicerVisualizationTutorial/</a></p>

---

## Post #7 by @Cody_Xie (2021-10-08 13:54 UTC)

<p>OK, thank you so much. Have a nice weekend!</p>

---

## Post #8 by @lassoan (2021-10-08 13:54 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html">Getting started section of the Slicer documentation</a> is a good starting point, too.</p>

---

## Post #9 by @Cody_Xie (2021-10-08 13:56 UTC)

<p>Indeed, I read it months ago and it really helped <img src="https://emoji.discourse-cdn.com/twitter/grinning_face_with_smiling_eyes.png?v=10" title=":grinning_face_with_smiling_eyes:" class="emoji" alt=":grinning_face_with_smiling_eyes:"></p>

---
