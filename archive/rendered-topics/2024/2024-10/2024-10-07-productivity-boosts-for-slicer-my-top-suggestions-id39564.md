# Productivity Boosts for Slicer: My Top Suggestions

**Topic ID**: 39564
**Date**: 2024-10-07
**URL**: https://discourse.slicer.org/t/productivity-boosts-for-slicer-my-top-suggestions/39564

---

## Post #1 by @Deep_Learning (2024-10-07 12:53 UTC)

<p>I use Slicer daily, and I believe a few small changes could significantly enhance my productivity. Some of these suggestions may seem minor, but I’m curious if other frequent users feel the same way. I’m open to working on these myself if they make sense.</p>
<p><strong><span class="hashtag-raw">#1</span></strong> After pressing the “Show 3D” button, I always have to click the “Center View” button. It would be great to have this action automated or an option to set this as a preference, with the current behavior as the default.</p>
<p><strong><span class="hashtag-raw">#2</span></strong> I often find myself pressing “Show 3D” after loading a segmentation. A preference to enable “Show 3D” automatically upon loading a segmentation would save time, with the current state as the default.</p>
<p><strong><span class="hashtag-raw">#3</span></strong> When loading .nii.gz files, I spend a lot of time switching from volume to segmentation. Could .seg.nii.gz files be automatically recognized as segmentation, similar to .seg.nrrd files?</p>
<p><strong><span class="hashtag-raw">#4</span></strong> It would be helpful to have the ability to clone a segment directly within the segmentation module, rather than switching to the Data module.</p>
<p><strong><span class="hashtag-raw">#5</span></strong> Lastly, the selection of a segment doesn’t transfer from the Data module to the Segmentation module. It would be beneficial if this selection could carry over.</p>
<p>Thanks for considering these suggestions!</p>

---

## Post #2 by @muratmaga (2024-10-07 22:36 UTC)

<p>Thanks for the feedback.</p>
<p>Slicer has a very large user community and it is difficult to apply what you requested broadly without breaking other people’s expectation.</p>
<p>(For example what if the user do not want the 3D viewer to be enabled by default, since their data is too large or some other reason).</p>
<p>Having said that, you can implement everything you need on your own Slicer using a bit of python scripting, then you can save them into the application start script (slicerrc.py) and have them available to you each time you use your slicer.</p>
<p>See details at: <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#runtime-environment-variables" class="inline-onebox" rel="noopener nofollow ugc">Application settings — 3D Slicer documentation</a></p>

---

## Post #3 by @jamesobutler (2024-10-07 22:45 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="39564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>For example what if the user do not want the 3D viewer to be enabled by default, since their data is too large or some other reason</p>
</blockquote>
</aside>
<p>I think a majority of folks would agree that if they set an object to show in the slice viewers that they would also expect it to show in the 3D viewer in some form.</p>
<p>There could be a minority which doesn’t like this behavior because they work with very large data, but that could probably be handled by a special exception for that minority. Extra large data seems like a special workflow case and not a normal case for most users. Therefore there is probably some coding that could be done to make things easier with different application defaults for this majority of users for the most common workflows.</p>

---

## Post #4 by @muratmaga (2024-10-07 23:33 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="39564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>that could probably be handled by a special exception for that minority. Extra large data seems like a special workflow case and not a normal case for most users.</p>
</blockquote>
</aside>
<p>What about the people doing slice by slice segmentation, like painting, erasing, drawing? That would mean once the 3D visualization is enabled, every mouse click would require rebuilding of the model of the model. Even in small data, this would probably cause unintended slowness.</p>
<p>I am not against these, the point that it is hard to come up with generally acceptable behavior. Particularly when that behavior has been around for a while and now became de facto expectation.</p>
<p>What I also mean, all of these is possible without waiting for the consensus. I sure have my own requirements, and it is usually a much faster route to implement those in the customization file then to get the core change. That’s all.</p>

---

## Post #5 by @jamesobutler (2024-10-07 23:36 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="39564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>What about the people doing slice by slice segmentation, like painting, erasing, drawing? That would mean once the 3D visualization is enabled, every mouse click would require rebuilding of the model of the model. Even in small data, this would probably cause unintended slowness.</p>
</blockquote>
</aside>
<p>There is ultimately some improvement that can be made to Slicer core to “make simple things simple and complex things possible”. The Slicer core sample data is probably a good starting point for typical user workflow. So if 3D visualization is fine while slice painting say the MRHead sample dataset then Slicer core could proceed with those type of changes.</p>

---

## Post #6 by @muratmaga (2024-10-08 00:10 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="5" data-topic="39564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>So if 3D visualization is fine while slice painting say the MRHead</p>
</blockquote>
</aside>
<p>That would be setting the bar extremely too low. That dataset is not representative of the data coming out of the modern clinical scanners like CBCT, or even higher resolution (0.325mm spacing) CTs. Most clinical CTs comes out of our radiology department is now 512x512x384 voxels, which is about 8-10 times larger than MRHead.</p>
<p>But again, it is doable. We just need to agree on a dataset that has an acceptable minimal size and perhaps a computer spec that is also expectable to test the performance.</p>

---

## Post #7 by @Deep_Learning (2024-10-08 09:39 UTC)

<p>What about a check box preference “3D auto mode”?  The current state is good for users with poor compute and new users (“show 3d” can seem like a freeze).  I would argue that auto show 3D and auto center view would be useful with the largest data.  Let’s say that loading takes 20 seconds.  The benefit is two fold.  <span class="hashtag-raw">#1</span> when loading is done, You know that it is done, because you can see your results in the 3D view,  currently, there is no visual cue.  <span class="hashtag-raw">#2</span> When loading is done, you are good to go.  No button pressing.  And no need to change to the Segmentation Module for access to the “Show 3D button”.   And then press center view.  I will do that at least 20 times today.</p>

---

## Post #8 by @Deep_Learning (2024-10-08 09:46 UTC)

<p><span class="hashtag-raw">#6</span> There is a pop up window when loading.  I believe with a cancel button.  I would suggest a preference/option to not show this window.  Use case, 1000 pts.  Running a script in the python window, all day.  Every time a pt is loaded, this window pops up, making multitasking on the computer difficult.  I actually have many slicers running with many pop windows on load…  No option to minimize the windows and have them running in the background.</p>

---

## Post #9 by @cpinter (2024-10-08 11:09 UTC)

<p><span class="hashtag-raw">#1</span> and <span class="hashtag-raw">#2:</span> I think anything can be added as long as they have a setting, and we wait with changing the default until we’re sure. For example, I just submitted a <a href="https://github.com/Slicer/Slicer/pull/7983">PR</a> that adds a segmentation-related setting, these could be similar.</p>
<p><span class="hashtag-raw">#3:</span> .seg.nrrd files are a special format, with special metadata and special handling of segments/layers. I think it would be really misleading handling a .seg.nii.gz extension, because it will still be a standard .nii.gz (simple 3D, no overlaps in segments, no extra metadata, etc.) but would suggest that it is also a special Slicer format</p>
<p><span class="hashtag-raw">#4:</span> Could be useful. But have you tried new segment → Logical operator / Copy? The result is the same.</p>
<p><span class="hashtag-raw">#5:</span> This would raise way too many concerns. Typically Slicer modules do not “know about each other”, and any synchronization happens via the MRML scene. Adding a glodal “selected segment” MRML property would be quite strange. I think this is a simple no.</p>
<p><span class="hashtag-raw">#6:</span> Do you mean the splash screen? Please search the forum, there have been many discussions about this, even very recently. I’m also annoyed by the splash screen, but not enough to do anything about it. When you start Slicer the second (or N&gt;1’th time), it launches within a second on my computer.</p>

---

## Post #10 by @Deep_Learning (2024-10-19 11:41 UTC)

<p>Make no mistake.  I am a big fan of slicer…   not at all complaining…</p>
<p>A good feature might be an external script exceuted auto on loading.  I was thinking that I would also like to auto set the view on load, in addition to center view, etc.</p>

---

## Post #11 by @pieper (2024-10-19 11:53 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="10" data-topic="39564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>Make no mistake. I am a big fan of slicer… not at all complaining…</p>
</blockquote>
</aside>
<p>Great!  That’s what this forum is meant to support.</p>
<aside class="quote no-group" data-username="Deep_Learning" data-post="10" data-topic="39564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>external script exceuted auto on loading</p>
</blockquote>
</aside>
<p>Have you looked at what you can do with <code>.slicerrc.py</code>?  You can configure the app in many ways and also register observers to react to new nodes being added to the scene.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file</a></p>

---
