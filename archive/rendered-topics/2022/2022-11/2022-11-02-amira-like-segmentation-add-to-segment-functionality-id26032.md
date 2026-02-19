---
topic_id: 26032
title: "Amira Like Segmentation Add To Segment Functionality"
date: 2022-11-02
url: https://discourse.slicer.org/t/26032
---

# Amira like segmentation - add to segment functionality

**Topic ID**: 26032
**Date**: 2022-11-02
**URL**: https://discourse.slicer.org/t/amira-like-segmentation-add-to-segment-functionality/26032

---

## Post #1 by @mcranium (2022-11-02 11:53 UTC)

<p>Dear 3D Slicer community,<br>
a colleague of mine, with whom I often collaborate is doing manual segmentation of muscles in µCT scans of small arthropods. Due to the small size, automatic segmentation is often not feasible. So, they will end up doing the segmentation by hand. Muscles often have very complex topologies and the segmentation work is also part of the learning and understanding process of the anatomy of the animal.</p>
<p>They worked extensively with Amira before, which has a feature that allows for a quite efficient workflow:<br>
The segmentation is done in something like a sandbox mode. They can segment some slices, and apply a fill between slices function, judge whether they like the result and then add the interpolated slices to a named segment that is currently selected using a shortcut. This way they can segment individual muscle strands, one after another and add them to a segment.</p>
<p>The desired workflow is as follows.</p>
<ol>
<li>select a segment in the segment editor</li>
<li>turn on the sandbox mode (what is painted will not automatically part of the selected segment)</li>
<li>manually draw in several slices</li>
<li>apply a fill between slices function</li>
<li>check the interpolation (at best in 3D), proceed with step 6 or undo step 4 or clear the “sandbox” content</li>
<li>add the interpolated “sandbox” segmentation to the previously selected segment</li>
<li>optionally repeat with step 3</li>
</ol>
<p>I know that it is possible to achieve this in 3D Slicer by creating new segments and merging them using the boolean operators. However, this is not very efficient. They often do manual segmentations for several hours and reported that they were more than twice as fast if they used this workflow in Amira compared to using 3D Slicer.</p>
<p>Is there a way to implement such “sandbox mode - add to segment” functionality in 3D Slicer? I know that this might be a niche functionality, but on the other hand, the lack of such functionality is the only reason why my colleague is still drawn to using Amira over open source software.</p>
<p>For those who are wondering about how the results of such models usually look like, here is a figure of an open access article. This example is definitively on the lower end of the spectrum regarding the complexity and amount of reconstructed muscles.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03b64e664be0deb80923cbfd2293667a69d92e76.jpeg" data-download-href="/uploads/short-url/wQ1lAY1XqfX0SO4cb3Ac4ns3um.jpeg?dl=1" title="Screenshot from 2022-11-02 12-12-53" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03b64e664be0deb80923cbfd2293667a69d92e76_2_631x500.jpeg" alt="Screenshot from 2022-11-02 12-12-53" data-base62-sha1="wQ1lAY1XqfX0SO4cb3Ac4ns3um" width="631" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03b64e664be0deb80923cbfd2293667a69d92e76_2_631x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03b64e664be0deb80923cbfd2293667a69d92e76_2_946x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03b64e664be0deb80923cbfd2293667a69d92e76_2_1262x1000.jpeg 2x" data-dominant-color="BEA292"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-02 12-12-53</span><span class="informations">1267×1003 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is it possible to achieve this functionality using a python script? I mean the core components are there, they are just not efficiently accessible? I would of course offer my help if it is possible to include this functionality into the 3D Slicer Segment Editor or as an extension for 3D Slicer. However, I have to point out that I am not a software engineer and what I can offer is only a basic proficiency in Python, limited to simple scripts and data analysis.</p>
<p>Thank you for looking into this! I admire your work and always try to promote others to give 3D Slicer a try.</p>

---

## Post #2 by @Andinet_Enquobahrie (2022-11-03 09:54 UTC)

<p>Mario,</p>
<p>Can you generate a short video (screencast) demonstrating the workflow you described above in Amira? A video would show the functionality better. If the functionality is something that is useful for the wider Slicer community, we can help with the implementation.</p>
<p>-Andinet</p>

---

## Post #3 by @pieper (2022-11-03 12:21 UTC)

<p>+1 to the suggestion from <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a></p>
<p>Writing specialized segmentation tools and workflows is definitely something we want to support and hopefully all the hooks are available to implement what you need.</p>

---

## Post #4 by @mcranium (2022-11-06 12:04 UTC)

<p>Thanks for the very positive replies! I uploaded a video screen cast to YouTube (unlisted):</p>
<div class="youtube-onebox lazy-video-container" data-video-id="ICDMHlZdFPM" data-video-title="Amira manual segmentation workflow" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=ICDMHlZdFPM" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/ICDMHlZdFPM/hqdefault.jpg" title="Amira manual segmentation workflow" width="" height="">
  </a>
</div>

<p>Sorry, that it took so long, but you know how it is when you cannot simply run the software on your own computer…</p>
<p>I think that this kind of workflow could also be of interest for users in other subfields in the biomedical spectrum. Good scans are often expensive and difficult to make and the quality of the scans at high magnifications is often not good enough to achieve desirable results by using automated methods. Further, the segmentation is often not there to separate objects of different materials but in the case of our example objects of the same material (muscles) in a complex environment. I can imagine similar situations for example with neurons, blood vessels, etc. There one of the main objectives while segmenting is also understanding the topology of the objects. Also, I think the developers of Amira would not have put this as their default (or only?) method for manual segmentation, despite being less intuitive for new users, if it were not of interest for a wider spectrum of users.</p>
<p>I hope this helps to deliver a better understanding why this kind of workflow is so important to us and maybe others as well.</p>

---

## Post #5 by @muratmaga (2022-11-06 23:22 UTC)

<aside class="quote no-group" data-username="mcranium" data-post="4" data-topic="26032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcranium/48/17153_2.png" class="avatar"> mcranium:</div>
<blockquote>
<p>Thanks for the very positive replies! I uploaded a video screen cast to YouTube (unlisted):</p>
</blockquote>
</aside>
<p>What you shown is already possible with Slicer, it might require couple more clicks than the Amira interface.</p>
<p>Each time you are segmenting a new muscle section:</p>
<ol>
<li>Set the modify other segments to “Allow Overlap”</li>
<li>Create a new segment for the new section to be segmented.</li>
<li>use the Draw tool to paint the few sections you want to interpolate in between. (optionally enable editable intensity range to have more control over voxel selection)</li>
<li>After 4-5 such outlines, use the Fill between slices tool (again optionally with intensity range enabled).</li>
<li>Repeat the steps 2-4 for each segment you are playing with.</li>
</ol>
<p>Once done, use the logical operators with Add option to combine the segments into a single segment.</p>

---

## Post #6 by @lassoan (2022-11-07 05:11 UTC)

<p>Here is a video of this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="u93kI1MG6Ic" data-video-title="Quick manual segmentation with contour interpolation" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=u93kI1MG6Ic" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/u93kI1MG6Ic/maxresdefault.jpg" title="Quick manual segmentation with contour interpolation" width="" height="">
  </a>
</div>

<p>If you segment multiple structures then you need to simply paint all those in the selected few slices.</p>
<p>I would also add that “Fill between slices” is a last resort tool, for cases when there is no contrast between the structure you want to segment and surrounding tissues (e.g., the user draws contours based on where he knows the boundary is, even though it is not really visible). For the most common case, when the segmented structure has slightly different intensity compared to surrounding, you can segment faster and more accurately using “Grow from seeds” effect.</p>

---

## Post #7 by @mcranium (2022-11-07 13:56 UTC)

<p>Dear responders,<br>
I am well aware of the possibility to do it this way in 3D Slicer. My idea was to make this more efficient. In Amira this kind of work requires very little effort because you only need one shortcut to fill between slices and one to add your segmented slices to an already pre-selected segment.</p>
<p>My question is whether it is possible to create an equally efficient workflow in 3D Slicer. As you pointed out, the core functions are already present. Maybe this could be done by creating an extension that can be installed by users who desire this kind of segmentation workflow over the already existing one. “SegmentEditorExtraEffects” does modify the segmentation editor interface, which makes me think that this might be possible.</p>

---

## Post #8 by @lassoan (2022-11-07 18:26 UTC)

<aside class="quote no-group" data-username="mcranium" data-post="7" data-topic="26032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcranium/48/17153_2.png" class="avatar"> mcranium:</div>
<blockquote>
<p>In Amira this kind of work requires very little effort because you only need one shortcut to fill between slices and one to add your segmented slices to an already pre-selected segment.</p>
</blockquote>
</aside>
<p>It requires 4 clicks in Slicer - 2 clicks to initialize, 2 clicks to apply (one click to go to Fill between slices effect, another o click Initialize or Update). It is also fully dynamic - it automatically updates segmentation in 3D as soon as you add any new segmented slices or you modify a slice. Amira’s tool does not seem to support this auto-update mode, only manual update, so to me Amira’s tool seems to be less convenient than Slicer’s.</p>
<p>Is the problem that for a new user it is hard to discover where to do those 2x2 clicks have to be made? Or you would prefer a keyboard shortcut instead of the 2 clicks? Or you want to disable auto-update by default and have a keyboard shortcut to manually update?</p>

---

## Post #9 by @mcranium (2022-11-08 09:47 UTC)

<p>What I would like, and what should probably also be possible with simply having a script rather than an extension, is to have shortcuts that spare me that extra clicks.</p>
<p>I could imagine something like this:</p>
<p>Shortcut 1:</p>
<ul>
<li>retrieve the name of the currently selected segment and store it in a variable named <code>parent</code>
</li>
<li>creates a new segment with a name that is for sure not in use like “temp#123”</li>
<li>selects the newly created segment “temp#123”</li>
<li>turn on the allow-overlap mode</li>
</ul>
<p>Shortcut 2:</p>
<ul>
<li>fill between slices (maybe there is already a shortcut that I am currently not aware of)</li>
</ul>
<p>Shortcut 3:</p>
<ul>
<li>check whether the currently selected segment is named “temp#123” (safety mechanism to avoid merging other segments with a shortcut)</li>
<li>use the logic operator “Add” to combine the segment “temp#123” and the segment with the name that is stored in <code>parent</code>
</li>
<li>select the segment with the name that is stored in <code>parent</code>
</li>
</ul>
<p>I really like the the auto updated preview that 3D Slicer has (as I usually don’t use Amira, I am not sure if it has this function, it could be simply not activated), so I have no intention to disable it, unless I run into hardware limitations.</p>
<p>I hope my intention for this question/suggestion/help-request got a bit clearer now. If somebody could help me write a script for creating and enabling such shortcuts this would be awesome.</p>

---

## Post #10 by @lassoan (2022-11-08 13:58 UTC)

<p>The Fill between slices effect already does almost exactly this. Instead of trying to manage everything in a single segmentation (and come up with a segment name that is not used and switch to allow overlap, to prevent unwanted modifications), Slicer simply creates a new “Preview” segmentation (you can see that if you switch to Data module while “Fill between slices” or “Grow from seeds” or “Watershed” effect is active), so there is no interference between the manually created inputs and continuously automatically updated segmentation results.</p>
<ul>
<li>Shortcut 1 = Click “Initialize” in “Fill between slices”</li>
<li>Shortcut 2 = automatic, no need to click anything (if you uncheck Auto-update then you need to click “Update” in “Fill between slices”)</li>
<li>Shortcut 3 = Click “Apply” in “Fill between slices”</li>
</ul>
<p>The only inconvenience that I see of the current workflow is that you need to switch to the “Fill between slices” module to initialize/update/apply. You don’t need to use your mouse for this, as you can just hit the “space” key to switch between the last two effects, but this shortcut is not easily discoverable and still requires some mental effort.</p>
<p>Would it fulfill your needs if we had the “Apply” and “Cancel” buttons (and if auto-update is disabled then an “Update” button; maybe also a “Restart” button) would be available in the Segment Editor module when an auto-update effect was active?</p>
<p>Something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7b0d74f338901097de0b5df1166777ac8de4a7a.png" data-download-href="/uploads/short-url/suxTBoRb1rzWjfbkU5PeF3qYP4m.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b0d74f338901097de0b5df1166777ac8de4a7a_2_530x500.png" alt="image" data-base62-sha1="suxTBoRb1rzWjfbkU5PeF3qYP4m" width="530" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b0d74f338901097de0b5df1166777ac8de4a7a_2_530x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b0d74f338901097de0b5df1166777ac8de4a7a_2_795x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7b0d74f338901097de0b5df1166777ac8de4a7a_2_1060x1000.png 2x" data-dominant-color="383B3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1083×1021 56.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or maybe even better:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fef3e9da0ce9e3826165d254a33eb56a5f63bfe.png" data-download-href="/uploads/short-url/kxiRa2n199z005adCJVRxPKzBds.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fef3e9da0ce9e3826165d254a33eb56a5f63bfe_2_504x500.png" alt="image" data-base62-sha1="kxiRa2n199z005adCJVRxPKzBds" width="504" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fef3e9da0ce9e3826165d254a33eb56a5f63bfe_2_504x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fef3e9da0ce9e3826165d254a33eb56a5f63bfe_2_756x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fef3e9da0ce9e3826165d254a33eb56a5f63bfe_2_1008x1000.png 2x" data-dominant-color="3B3E3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1086×1076 54.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @mcranium (2022-11-09 10:58 UTC)

<p>There is one problem with the solution you showed:</p>
<p>If the preview/sandbox segment is of the same segment as what has been previosly segmented, the fill between slices algorithm tries to incorporate everything instead of the not yet interpolated part.</p>
<p>Here is a screenshot of what I mean.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5448e85a627c5c86029f32de2ccd5f19bf11aeb.jpeg" data-download-href="/uploads/short-url/pRziRzVZyKYDijxO1NkCttjJ1aj.jpeg?dl=1" title="Screenshot from 2022-11-09 11-47-12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5448e85a627c5c86029f32de2ccd5f19bf11aeb_2_690x388.jpeg" alt="Screenshot from 2022-11-09 11-47-12" data-base62-sha1="pRziRzVZyKYDijxO1NkCttjJ1aj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5448e85a627c5c86029f32de2ccd5f19bf11aeb_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5448e85a627c5c86029f32de2ccd5f19bf11aeb_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/5/b5448e85a627c5c86029f32de2ccd5f19bf11aeb_2_1380x776.jpeg 2x" data-dominant-color="5E5D64"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-11-09 11-47-12</span><span class="informations">1920×1080 99.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I segmented one structure, filled between slices and began segmenting a new structure (of the same muscle that I intended to join later. As you can see the fill between slices algorithm made additions to the structure that I did not want it to make changes to (e.g. it prolonged the left muscle strand in the 3D view). Also, note the shape of the interpolated segment in the red view - it has sharp corners. This would not happen if I was working on a different segment.</p>
<p>I hope it gets clear what I mean.</p>

---

## Post #12 by @lassoan (2022-11-10 21:00 UTC)

<aside class="quote no-group" data-username="mcranium" data-post="11" data-topic="26032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcranium/48/17153_2.png" class="avatar"> mcranium:</div>
<blockquote>
<p>segmented one structure, filled between slices and began segmenting a new structure (of the same muscle that I intended to join later.</p>
</blockquote>
</aside>
<p>It is a different segment then. You can merge segments later if needed.</p>
<p>Fill between slices interpolates between all visible slices, so if there are segments that you want to exclude from interpolation then you can hide them or temporarily move them to a different segmentation (you can drag-and-drop segments between segmentations in Data module).</p>
<p>It may be simpler not to exclude segments but keep “Fill between slices” active until you are done with all (or at least a group) of your segments. The only drawback of this approach may be that you need to always segment complete slices. Therefore, if you want to fix up the automatic filling result of only one segment in a slice then you need to paint all the segments that are visible in that slice.</p>

---
