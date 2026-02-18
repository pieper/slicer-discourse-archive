# Translation of "volume" term to other languages

**Topic ID**: 21608
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/translation-of-volume-term-to-other-languages/21608

---

## Post #1 by @lassoan (2022-01-24 23:23 UTC)

<p>Moving a <a href="https://crowdin.com/project/slicer/discussions/5">discussion that we started on crowdin</a> to this forum for better visibility and to include more people.</p>
<p>Opened Jan 22, 2022</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/14733716/medium/4245397b99d0b13bc8813fc20121ca24.jpg" alt="Andras Lasso" title="Andras Lasso" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/lassoan">Andras Lasso</a></p>
<p>2 days ago</p>
<p>We have found it difficult to translate “volume” (to Hungarian, but probably the issue is the same for other languages). “Volume” word in Hungarian would just refer to “amount of space in a container”.</p>
<p>The problem is that “volume” is an abbreviation of “image volume” or “volumetric image”. Using a two-word translation would be too long (at some places would not even fit), and in general it would make the user interface (and talking about the user interface) a bit more complicated.</p>
<p>We are considering using just <strong>“image”</strong> as a basis for translation. Does anyone have a better suggestion?</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/15112075/medium/6632070822eebc2cd55f961cc1dc2a97.png" alt="Andrey Fedorov" title="Andrey Fedorov" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/andrey.fedorov">Andrey Fedorov (andrey.fedorov)</a></p>
<p>4 hours ago</p>
<p>We have the same issue with the Russian translation. The problem with using just “image” is that the English version of “image” is also present in Slicer, and we will end up using the same non-English concept for two different English concepts in the same interface. But I do not have a better idea, other than using “volumetric image”, which will lead to all those issues you summarized.</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/14733716/medium/4245397b99d0b13bc8813fc20121ca24.jpg" alt="Andras Lasso" title="Andras Lasso" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/lassoan">Andras Lasso</a></p>
<p>2 hours ago</p>
<p>“Image” is just used at 16 places in Slicer core (maybe a few ten more if we also extract strings from CLI and Python modules). In many of these cases it is used interchangeably with “Volume”. “Image” can be used everywhere instead of “volume”.</p>
<p>I guess your concern is that “volume” may suggest that a multi-slice volume is expected and not a single-slice volume. There are places where this distinction would make things less clear (for example, when you right-click on a slice view then one of the actions is “Copy image”, which gives a hint that it probably copies a 2D image (screenshot) and not the whole volumetric image). However, the number of these special cases are so low that it should be possible to address them by rephrasing the text or adding tooltip.</p>
<p>By the way, I’ve checked a few other software (ITK-Snap, MITK, Weasis, OsiriX) and all of them seem to just use “image” for both 2D and volumetric images. The “volume” term is not used in libraries either - VTK and ITK use “image”, except in some comments or some class documentations. So, probably we should switch to “image” not just in translations but in English, too.</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/15112075/medium/6632070822eebc2cd55f961cc1dc2a97.png" alt="Andrey Fedorov" title="Andrey Fedorov" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/andrey.fedorov">Andrey Fedorov (andrey.fedorov)</a></p>
<p>2 hours ago</p>
<blockquote>
<p>I guess your concern is that “volume” may suggest that a multi-slice volume is expected and not a single-slice volume.</p>
</blockquote>
<p>Yes, exactly. My personal preference would be to maintain that distinction.</p>
<p><img src="https://crowdin-static.downloads.crowdin.com/avatar/14733716/medium/4245397b99d0b13bc8813fc20121ca24.jpg" alt="Andras Lasso" title="Andras Lasso" width="96" height="96"></p>
<p><a href="https://crowdin.com/profile/lassoan">Andras Lasso</a></p>
<p>43 minutes ago</p>
<p>We actually don’t rely on this distinction now. In the current Slicer message list of 2600 terms we only use “image” 3 times to refer to a 2D image (in the other 20 or so occurrences, it refers to a volume). Therefore, basically no information would be lost, we could just document that in Slicer, as in most (if not all) other medical image computing software, image may refer to 2D or volumetric images.</p>

---

## Post #2 by @pieper (2022-01-24 23:47 UTC)

<p>Slicer traditionally used Volume pretty consistently, but when we added ITK we got a lot of uses of image.</p>
<p>In general yes, it makes sense to harmonize the terms for better consistency.  Already ‘point list’ is so much better than ‘fiducials’ and people have also been noting that scene and node are used oddly in Slicer, so they are definite candidates for improvement.</p>
<p>As a side note I agree moving discussions here is better than using crowdin’s discussion tools, which don’t seem as nice or visible.</p>

---

## Post #3 by @jamesobutler (2022-01-25 00:02 UTC)

<p>I would lean on the side that “Image” refers to a 2D item while a “Volume” refers to a 3D item. We have had some discussions in our group that referring to a single slice object as a “Volume” is a little weird as normally it would be referred to as just a simple “image”. Since Slicer is focused on 3D, hence the name “3D Slicer”, I think it would be better to use “Volume” with the weird cases of 2D objects still called “Volumes” because they are technically 3D volumes with a 1 voxel 3rd dimension. My guess is that ITK and other programs that used “Image” were originally 2D focused and 3D support was added later.</p>
<p>In addition, my group “SonoVol”, uses the term “Vol” for “Volume” because we make 3D ultrasound volumes. So probably some bias towards the “Volume” term over “Image” haha</p>

---

## Post #4 by @pieper (2022-01-25 00:16 UTC)

<p>Good points James, thanks for chiming in.  ITK chose image for kind of the opposite reason since it was designed for n-dimensional data and felt, as I recall, that Volume would be too restrictive to 3D.</p>
<p>This is why the translation process is so interesting and revealing.  We need to balance the desire to use existing words vs the need to name new technical concepts where there aren’t always good words in any language.</p>

---

## Post #5 by @jamesobutler (2022-01-25 00:30 UTC)

<p>Volumes as a term seems to be commonly known as being a set of images while itself is not an image. Where there are n-dimensions of images but the collective is not an image. Similar in weird context as when we had the “fiducial” node which itself contained “fiducials”. It was confusing and needed a different term of “fiducial list”/“point list” to describe the collective of “fiducials”/“points”.</p>
<p>We typically wouldn’t say “moving images”, but rather a “video” or “sequence” as Slicer uses.</p>
<p>Definitely an interesting problem to solve for various language support. I wonder if some translations are going to result in a smaller or larger set of terms between languages where it is not going to be a 1:1 between English.</p>

---

## Post #6 by @lassoan (2022-01-25 06:19 UTC)

<p>I’ve been using Slicer for so long that I assumed that “volume” word is commonly used for referring to a volumetric image, but I’ve realized now that this is not the case at all.</p>
<p>All software applications that I could find use the term “image” and not “volume”. Not just the 2D-oriented applications, such as ImageJ, OsiriX, Weasis, OHIF; but also 3D software, such as ITK-Snap, Mimics, and MITK. DICOM standard does not use the “volume” word in this sense either (except a very few exceptions).</p>
<p>Probably we will need to use the “image” term in other languages because nobody would understand what “volume” refers to, but we can decide on the English term later.</p>

---

## Post #7 by @jamesobutler (2022-01-25 13:26 UTC)

<p>On <a href="https://www.slicer.org" rel="noopener nofollow ugc">https://www.slicer.org</a> it looks like there are multiple uses of 2D/3D/4D images/data.</p>
<p>There is a use of “3D Volume” in the area about “3D ultrasound reconstruction” and PlusToolkit’s “Volume Reconstruction” tools.</p>
<p>So seems possible to use “image” as a general term though “Volume” is used at times when specifically talking about 3D data.</p>
<p>Not sure if we would ever change the term from “Volume Rendering” to “Image Rendering” though. If anything maybe just dropping it to “Rendering”.</p>

---

## Post #8 by @mikebind (2022-01-25 19:19 UTC)

<p>I’m used to Slicer’s current terminology because most of my work in medical imaging has been in Slicer, but I have also noticed that almost no one outside of Slicer users refer to 3D images as “volumes”, and that this can be a confusing term at first to medical providers. Using the term “image” as the basis for translation internationally seems like it makes the most sense.</p>
<p>I think it would make sense for the english term to transition to “image” as well, with the dimensionality of the image specified when needed, but otherwise left ambiguous.</p>
<p>For most purposes, I think “slice” is a good term for a 2D image. It is not always appropriate, because not every 2D image is a slice from something bigger, and it’s possible to think of multi-dimensional “slices” (say a 3D slice of a 4D data set), but I think it is intuitive and by far the most common use case in 3D Slicer. It also fits that a “slice” can be thought of as anything you could look at in one of the “slice views”.</p>

---

## Post #9 by @pieper (2022-01-25 19:29 UTC)

<p>I like ‘image’ as the general term too.  Certainly ‘volume rendering’ is a common computer graphics term, but maybe that’s still jargony.  I agree ‘slice’ isn’t always accurate; DICOM uses ‘frame’ for that concept and that’s a good option.  But ‘slice’ in Slicer’s term ‘slice views’ is still a good term for what happens in that kind of view.</p>
<p>In addition to DICOM, we could look to <a href="https://www.rsna.org/practice-tools/data-tools-and-standards/radlex-radiology-lexicon">RadLex</a>, <a href="https://www.snomed.org/">SNOMED</a>, and <a href="https://ta2viewer.openanatomy.org/">TA2</a> for translation conventions.</p>

---

## Post #10 by @mikebind (2022-01-25 19:42 UTC)

<p>I often work with 4D data which are temporal sequences of 3D images, and I use the term ‘frame’ to refer to one image in the sequence, which is also the default behavior of the Sequences module. Because of that, I would prefer that “frame” not be adopted as the Slicer standard term for 2D image (though I recognize that my use case here may not be very common, so maybe shouldn’t carry much weight).</p>
<p>What would people think about just using “2D image” as the standard term?</p>

---

## Post #11 by @muratmaga (2022-01-25 21:17 UTC)

<p>IMO, “image” is too generic to be useful. People will consider things like textured 3D scans as images as well (e.g., all the stuff on Sketchfab), which we have minimal support. Likewise support for RGB images of histological slides or confocal data is at best sketchy.</p>
<p>What Slicer does in its core is image processing and visualization of volumetric data. Unless that’s going to change anytime soon, I am not seeing the benefit of replacing “volume” with “image”.</p>

---

## Post #12 by @lassoan (2022-01-25 21:37 UTC)

<p>All other software that works almost exclusively on 3D images uses just “image” (if you know any that uses “volume” or similar then let us know). Not just software applications, but software libraries, books, standards, etc. use “image”, too. The “volume” term for for volumetric image is really pure Slicerism. I’m very suprised - I haven’t realized this until a few days ago.</p>
<p>Since everyone else are fine with using the same word for both 2D and 3D image, Slicer should be OK, too. I like suggestion of <a class="mention" href="/u/jamesobutler">@jamesobutler</a> and <a class="mention" href="/u/mikebind">@mikebind</a> above that in the very rare uses cases where distinguishing between image dimensionality is useful (currently 2 strings out of the 24 occurrences of “image” in Slicer’s translatable strings) then we can use “2D image” or other specific word. For example right-click action “Copy image” can be replaced by something like “Copy screenshot”, “Copy captured image”, “Copy rendered image”, or “Capture image to clipboard”.</p>

---

## Post #13 by @fedorov (2022-01-25 22:12 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> if we proceed with your proposal, does this mean “Volumes” module will become “Images” module, and “Volume rendering” - “Image rendering”?</p>

---

## Post #14 by @pieper (2022-01-25 22:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="21608">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>if you know any that uses “volume” or similar then let us know</p>
</blockquote>
</aside>
<p>VolView was available from Kitware as a product at the time Slicer was first being developed and if you search now you will find lots of people use that term for rendering 3D data, not just Kitware.</p>
<p>Maybe one of the language packs we offer is “non-Slicer English” where all the Volumes are changed to Images and then we can see if we want to change the “official” terms in Slicer.  Not only community inertia but also documentation, training materials, etc would be a lot to change.</p>

---

## Post #15 by @lassoan (2022-01-25 22:23 UTC)

<p>Good point. Replacing “Volumes” and “Volume rendering” modules by a single “Images” module would make sense.</p>
<p>We don’t have separate module for setting 3D display properties of any other node types. The modules are split into two only due to historical reasons. Volume rendering settings should be just a section in “Images” module.</p>

---

## Post #16 by @fedorov (2022-01-25 22:50 UTC)

<aside class="quote no-group" data-username="pieper" data-post="14" data-topic="21608">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Not only community inertia but also documentation, training materials, etc would be a lot to change.</p>
</blockquote>
</aside>
<p>It’s not just that it will be a lot to change, but we will need to accept that there will be a lot we will not be able to change in the existing materials (including in other languages) either maintained by others, or those about existence of which we are not aware or forgot.</p>

---

## Post #17 by @lassoan (2022-01-25 23:15 UTC)

<p>My main concern with updating the English terms is that any change is annoying for users. One way to make it somewhat more tolerable is to bundle it with significant improvements.</p>
<p>When we are ready to invest into improvements in the volumes modules, we have solid multi-volume rendering implementation, have a good solution for simplifying volume rendering setup, and can update/create tutorials then it should be OK to change the wording along with all the changes.</p>
<p>Fortunately all of these improvements could fit in the scope, funding, and timeline of the CZI EOSS grant. We’ll just need to collect all these similar improvement ideas and prioritize.</p>

---

## Post #18 by @pieper (2022-01-25 23:56 UTC)

<p>Agreed, if we want to keep Volumes while we set up a parallel <code>Images</code> module like we have for other major upgrades (Segmentations, Sequences, Markups…) then we can switch people over when there’s feature parity plus feature and usability improvements.</p>

---
