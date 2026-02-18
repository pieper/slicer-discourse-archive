# "Compare Volumes" module - display order

**Topic ID**: 31261
**Date**: 2023-08-21
**URL**: https://discourse.slicer.org/t/compare-volumes-module-display-order/31261

---

## Post #1 by @Michele_Bailo (2023-08-21 13:33 UTC)

<p>Hi everyone,<br>
I recently discovered the “Compare volumes” module from this post: <a href="https://discourse.slicer.org/t/link-views-in-three-over-three-configuration/24564/4">Link views in three over three configuration - Support - 3D Slicer Community</a></p>
<p>I find this module great for the rapidity with which it allows me to compare different clinical series (either different modalities acquired at the same time-point or same modalities acquired in different time-points). I have been using Slicer in my daily routine for several years to compare images for both clinical and research reasons, but till a few months ago I had to create layouts manually each time. So thank you very much for developing this module!</p>
<p>I have, however, two issues that I would like to ask your suggestions/help on.</p>
<ol>
<li>
<p>When I want to compare follow-up studies acquired at different time-points, the “Parameters” window does not allow me to select (and therefore view) them in the order most useful to me (for example a chronological order would be ideal). What should I change in the module script to have them listed by volume “name” instead of “MRML ID” (which only depends on the order I imported them in the dataset)? In the latter case, it would be sufficient for me to rename the sequences with the exam date to have them automatically displayed in the proper order.</p>
</li>
<li>
<p>When there are many studies to be compared (≥6) using the AxiSagCor “Orientation”, the visualization of each study in the same line is no longer optimal (especially while using a “widescreen” resolution).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04696434ca438e9ec11e6b9df0d152c11a061883.jpeg" data-download-href="/uploads/short-url/D1I1abkRe35SZpqPnzOSFYGt11.jpeg?dl=1" title="Screenshot 2023-08-21 140005" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04696434ca438e9ec11e6b9df0d152c11a061883_2_690x375.jpeg" alt="Screenshot 2023-08-21 140005" data-base62-sha1="D1I1abkRe35SZpqPnzOSFYGt11" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04696434ca438e9ec11e6b9df0d152c11a061883_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04696434ca438e9ec11e6b9df0d152c11a061883_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04696434ca438e9ec11e6b9df0d152c11a061883_2_1380x750.jpeg 2x" data-dominant-color="7E817F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-21 140005</span><span class="informations">1920×1044 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>It would be probably better to have each study arranged in the same column (as in the following screenshot)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/486f3375d7b7c4beb49f0c554b8a67b230d63063.jpeg" data-download-href="/uploads/short-url/akMCKjC5aCREd8znYHuxXYQu8lt.jpeg?dl=1" title="Screenshot 2023-08-21 150348" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486f3375d7b7c4beb49f0c554b8a67b230d63063_2_690x374.jpeg" alt="Screenshot 2023-08-21 150348" data-base62-sha1="akMCKjC5aCREd8znYHuxXYQu8lt" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486f3375d7b7c4beb49f0c554b8a67b230d63063_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486f3375d7b7c4beb49f0c554b8a67b230d63063_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486f3375d7b7c4beb49f0c554b8a67b230d63063_2_1380x748.jpeg 2x" data-dominant-color="727271"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-21 150348</span><span class="informations">1920×1041 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there a way for me to select/change how studies are displayed (lines or columns)?</p>
<p>I’m really sorry to bother you with these issues but, as a neurosurgeon, my expertise in scripting is quite limited and I have no one here to help me with that <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"> .<br>
I understand that the second issue might require too much effort to be worth spending energy/time on it<br>
if I am the only one experiencing problems with it. However, I hope, at least, that someone could help me with the first one without too much effort.</p>
<p>Thank you very much in advance!</p>

---

## Post #2 by @pieper (2023-08-21 19:03 UTC)

<p>Thanks for the feedback on the module.  The data you are working with is exactly why the code was developed in the first place.  Other than some odd bug fixes I haven’t worked with this code in a while and I’m not sure when I’d find time, but maybe someone else wants to give it a try?</p>
<aside class="quote no-group" data-username="Michele_Bailo" data-post="1" data-topic="31261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michele_bailo/48/67234_2.png" class="avatar"> Michele_Bailo:</div>
<blockquote>
<p>select (and therefore view) them in the order</p>
</blockquote>
</aside>
<p>it may not be documented, but you should be able to drag-and-drop the entries in the Volumes list to control the order they are displayed in the layout.  If that’s not enough then probably adding some buttons or a menu to choose sorting orders could make sense.</p>
<aside class="quote no-group" data-username="Michele_Bailo" data-post="1" data-topic="31261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michele_bailo/48/67234_2.png" class="avatar"> Michele_Bailo:</div>
<blockquote>
<p>each study arranged in the same column</p>
</blockquote>
</aside>
<p>That’s a good idea.  Probably that would be a relatively small change but it would require python coding.  The <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L337-L434">code in question is here</a>.</p>
<p>Another option of course is to get a bigger monitor <img src="https://emoji.discourse-cdn.com/twitter/eyes.png?v=12" title=":eyes:" class="emoji" alt=":eyes:" loading="lazy" width="20" height="20"></p>

---

## Post #3 by @Michele_Bailo (2023-08-27 20:00 UTC)

<p>Many thanks for your reply. I didn’t know it was possible to drag and drop studies! This information is incredibly useful! Thank you very much.</p>
<p>The monitor is already quite big in terms of size and resolution. The main problem is that nowadays they all make them in 16:9 format, so they are much larger than tall <img src="https://emoji.discourse-cdn.com/twitter/sob.png?v=12" title=":sob:" class="emoji" alt=":sob:" loading="lazy" width="20" height="20"><br>
I understand however that this second issue would take too long to be implemented and probably not be worth it since (I think) I’m one of the very few people comparing such a large number of radiological studies simultaneously.<br>
Thanks again for your support!</p>

---

## Post #4 by @pieper (2023-08-27 21:31 UTC)

<aside class="quote no-group" data-username="Michele_Bailo" data-post="3" data-topic="31261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michele_bailo/48/67234_2.png" class="avatar"> Michele_Bailo:</div>
<blockquote>
<p>they all make them in 16:9 format</p>
</blockquote>
</aside>
<p>Just and idea but if you do this a lot you can rotate the monitor - most operating systems let you work with a rotated display.</p>
<aside class="quote no-group" data-username="Michele_Bailo" data-post="3" data-topic="31261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/michele_bailo/48/67234_2.png" class="avatar"> Michele_Bailo:</div>
<blockquote>
<p>too long to be implemented</p>
</blockquote>
</aside>
<p>It’s probably not a huge amount of work but the layout code is a little tricky so someone would need to figure the magic to make it work as you describe.  Let’s see if this feature request gets a lot of votes.  It’s very localized logic so this would be a “Good First Project” for someone who wants some programming experience.</p>

---

## Post #5 by @lassoan (2023-10-10 20:30 UTC)

<p>3 posts were split to a new topic: <a href="/t/compare-volumes-module-does-not-work-on-slicer-5-4/32142">Compare Volumes module does not work on Slicer-5.4</a></p>

---

## Post #6 by @Michele_Bailo (2024-01-02 14:29 UTC)

<p>Hi there,</p>
<p>I have been using this module a lot in the last months (with different Slicer versions, including the latest updates) since I often need to compare multiple series at the same times and I find it extremely helpful! So thanks again!</p>
<p>Unfortunately, I noticed that in those datasets where I used this module at least once, things start to go extremely slow thereafter: even scrolling a single series in the Red view alone shows extreme “lagging”. The problem persists even if save and close the scene, restart the pc (which is an incredibly powerful workstation with 128 GB DDR RAM and 12th Gen Intel Core i9-12900F, 2400 Mhz, 16 Cores, 24 Logical Processors; Windows 11) and reload the saved scene.</p>
<p>On the contrary, this problem does not occur when I “manually” set the same amount of panels, such as a “4 by 3” or even “7 by 3” scenes, without using the “compare volumes” module.</p>
<p>My impression is that once the “compare volumes” module is utilized to display multiple views, it somehow keeps occupying a huge amount of resources, even if the additional view-panels are not shown anymore. It gets better again if I manually delete all the additional Slice-views created from the “Data”-&gt;”All Nodes” module.</p>
<p>Do you think that it represents a problem inside the “compare module” script? Or, conversely, is there a way to auto-release the resources without requiring to manually delete the slices-view, one-by-one, in the “all nodes” windows, when the comparison is not needed anymore?</p>
<p>Thank you very much in advance.</p>
<p>Michele</p>

---

## Post #7 by @pieper (2024-01-02 15:34 UTC)

<p>Hi <a class="mention" href="/u/michele_bailo">@Michele_Bailo</a> - yes, it sounds like there’s optimization to be done in the script to be sure it is either freeing up resources or re-using them if possible.  It would be good to create an issue to track this (in <a href="https://github.com/Slicer/Slicer/issues">Slicer</a> since this is bundled with the app).  A good way to proceed would be to add a <a href="https://github.com/pieper/CompareVolumes/blob/master/CompareVolumes.py#L871">new test</a> that iteratively runs various parts of the module’s functionality and measures the performance impact like is done <a href="https://github.com/Slicer/Slicer/blob/main/Applications/SlicerApp/Testing/Python/ScenePerformance.py">here</a> or <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/PerformanceTests/PerformanceTests.py">here</a> so we can see where what is going on and confirm when it’s resolved.  This might be a simple fix.</p>

---

## Post #8 by @Michele_Bailo (2024-01-05 10:40 UTC)

<p>Thank you very much. I proceeded in opening to issue here:<br>
<a href="https://github.com/Slicer/Slicer/issues/7522" rel="noopener nofollow ugc">“Compare volumes” module permanently engulf working memory and processing units once used in a specific Slicer dataset. · Issue #7522 · Slicer/Slicer (github.com)</a></p>
<p>sincerely<br>
MB</p>

---
