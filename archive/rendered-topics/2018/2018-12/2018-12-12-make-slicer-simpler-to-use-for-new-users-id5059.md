---
topic_id: 5059
title: "Make Slicer Simpler To Use For New Users"
date: 2018-12-12
url: https://discourse.slicer.org/t/5059
---

# Make Slicer simpler to use for new users

**Topic ID**: 5059
**Date**: 2018-12-12
**URL**: https://discourse.slicer.org/t/make-slicer-simpler-to-use-for-new-users/5059

---

## Post #1 by @lassoan (2018-12-12 18:46 UTC)

<p>This topic is forked from the <a href="https://discourse.slicer.org/t/hangout-2018-12-11/5035/10">meeting minutes of weekly hangout on 2018-Dec-11</a>.</p>
<p>We discussed how the UI and UX could be improved. Here is a very short list, we should probably create a poll or conduct a user study …</p>
<ul>
<li>Create two different applications ? Or have theme like Blender ? Simple vs Advanced</li>
<li>Collect specific list of UI issues:
<ul>
<li>user can not find the eye icon in volume rendering</li>
</ul>
</li>
<li>Display volume in 3D by default</li>
<li>Free “real estate” by hiding (or relocating) the Slicer icon ?</li>
</ul>

---

## Post #2 by @lassoan (2018-12-11 16:23 UTC)

<p>These are great ideas to discuss. It would be important to make simple things as simple as possible to do in Slicer.</p>
<p>If we get to know any specific issue then we can address that. But addressing usability in general is really hard.</p>
<p>I’m not a believer of having a “simple mode” for powerful applications, mostly because all the attempts that I have seen have mostly failed: in applications that I did not know, they did not make learning any easier; in applications that I knew already, it just made things harder to access. But we can certainly evaluate this option for Slicer, maybe we can do better.</p>
<p>Predefined workspaces/perspectives optimized for certain tasks seem to be a good idea, too, but based on my experience with various software, they do not help much; and flexible layouts make the software more difficult to learn because my screen always looks completely different than those shown in examples and tutorials. Experts don’t use predefined workspaces much either, because they rather set up their highly optimized workspace; but ability to customize layout and save/restore it is a useful feature for experts.</p>

---

## Post #3 by @pieper (2018-12-11 16:46 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> mentioned the issue with users not understanding the ‘eye’ icon in the volume rendering as an example of something that’s obvious once you know it but hard to learn.  This struck me as a specific usability thing we might address.  One option, noted above, would be to have newly loaded volumes show in 3D like the do in 2D (probably with a preference option to turn off this behavior).</p>
<p>I suspect there are many other similar features we could (carefully) consider and introduce to help both novice and advanced users while still keeping unified interface for documentation and tutorial purposes.</p>

---

## Post #4 by @muratmaga (2018-12-11 17:25 UTC)

<p>The challenge is, it is hard to measure whether there are consistently painful issues across different user domains and whether it makes sense to commit dev time to fix them. But if you are looking usability issues, I offer one observation below:</p>
<p>One frustrating point that I consistently observe when I train new users is that the existing default 4 up view and modules tab is not linked very well. Your segmentation might be a completely different then the volume you might be looking at the slice view or in volume rendering window. I am not sure what the solution might be, but perhaps the ‘simple mode’ would restrict the user to load only one ‘master’ volume at a time, and visibility icons (whether they are in the modules tab or in slice views) are linked, and every other dataset would be stuff derived from this ‘master’ volume.</p>

---

## Post #5 by @rkikinis (2018-12-11 17:34 UTC)

<p>Hi Steve,</p>
<p>I like this idea a lot.</p>
<p>Best<br>
Ron</p>

---

## Post #6 by @jamesobutler (2018-12-12 04:28 UTC)

<p>For me, I’ve noticed that users frequently struggle with the fact that you can be modifying/manipulating data from the module GUI, but not actually viewing what you are manipulating in the main layout. This leads to frustrations that nothing appears to be happening.</p>
<p>In the custom application that I work on, we try to make it simple enough to users that might not even be super proficient with computers in general. We have kept one volume shown in red, yellow, green slices instead of allowing a volume shown in red and then maybe a different one in yellow.</p>
<p>The fact that Slicer can do so many things is great, but also extremely overwhelming. It’s almost like using Adobe Premiere Pro to edit video for the first time. I guess there’s a reason why there is an iMovie and why there is a Final Cut Pro. Maybe trying to appeal to the casual image technologist could broaden the user base in a manner that could bring in more funding for Slicer development to support new functionality for advanced power users. Also, hopefully new developers with the rise of python programming.</p>

---

## Post #7 by @lassoan (2018-12-12 15:18 UTC)

<aside class="quote no-group quote-post-not-found" data-username="muratmaga" data-post="5" data-topic="5035">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"><a href="https://discourse.slicer.org/t/2018-12-11-hangout/5035/5">2018.12.11 Hangout</a></div>
<blockquote>
<p>One frustrating point that I consistently observe when I train new users is that the existing default 4 up view and modules tab is not linked very well.</p>
</blockquote>
</aside>
<p>We noticed this issue a couple of years ago and developed <em>Subject hierarchy</em> module to address this. Now Subject hierarchy is available as the first tab in Data module.</p>
<p>Subject hierarchy shows all displayable data in the scene and you can perform all basic operations (show/hide in all views, delete, rename, apply transform, etc.) without switching modules. Novice users don’t even need to know about any other modules.</p>
<p>When you want to edit properties of a node, you can right-click on it and select <em>Edit properties</em>. This takes you to the module appropriate for editing the selected node <em>and it also selects that node as active node in the GUI</em>. The user does not need to know which module is for editing a particular node type or select the active node manually.</p>
<p>I think what we miss is better promotion of the Subject hierarchy. We should advertise it much more in tutorials and make it easier to find when using the application. For example, when after the first data set is loaded (but at least when DICOM loading is completed), we should automatically switch to Data module.</p>

---

## Post #8 by @muratmaga (2018-12-12 17:14 UTC)

<p>Yes, I agree. I think the Data Module should be default opening tab instead of Welcome. That’s what I do when I train new users; the first thing I show them is how to make the Data module as the default one.</p>
<p>While subject hierarchy is an improvement, it still doesn’t resolve the some of the issues. E.g., I can’t control the volume rendering from subject hierarchy. When I click the eye icon, it simply removes it from the slice view, whereas my expectation as a novice would have been to disable/enable the 3D rendering as well. Or at least in my version of subject hierarchy (r27534), there is nothing indicating an option for volume rendering.</p>
<p>That’s what  mean in the ‘simple mode’ (or whatever we want to call) everything needs to be tied together much more cohesively.</p>

---

## Post #9 by @cpinter (2018-12-12 18:25 UTC)

<aside class="quote no-group quote-post-not-found" data-username="jamesobutler" data-post="7" data-topic="5035">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"><a href="https://discourse.slicer.org/t/2018-12-11-hangout/5035/7">2018.12.11 Hangout</a></div>
<blockquote>
<p>It’s almost like using Adobe Premiere Pro to edit video for the first time. I guess there’s a reason why there is an iMovie and why there is a Final Cut Pro</p>
</blockquote>
</aside>
<p>I fully agree. But at the same time we want to keep Slicer a swiss army knife because it’s so versatile that advanced users and “smart” people (who can find things in the wiki and discourse answers) can do almost anything they might want to do with their medical data.<br>
What I was thinking about for example is to have a slicelet just for segmentation. So we wouldn’t have simple mode and advanced mode (which I think would open a can of worms and would be very hard to maintain and also we’d need to re-train existing users), but there would be simple custom apps for the most typical use cases.</p>
<aside class="quote no-group quote-post-not-found" data-username="lassoan" data-post="8" data-topic="5035">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/2018-12-11-hangout/5035/8">2018.12.11 Hangout</a></div>
<blockquote>
<p>when after the first data set is loaded (but at least when DICOM loading is completed), we should automatically switch to Data module</p>
</blockquote>
</aside>
<p>Exactly.</p>
<aside class="quote no-group quote-post-not-found" data-username="muratmaga" data-post="9" data-topic="5035">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"><a href="https://discourse.slicer.org/t/2018-12-11-hangout/5035/9">2018.12.11 Hangout</a></div>
<blockquote>
<p>I can’t control the volume rendering from subject hierarchy</p>
</blockquote>
</aside>
<p>This statement is not true as it is. There is a way to control volume rendering from SH, but it’s hard to find (right-click the eye icon and another kind of context menu shows up).</p>
<p>I know that SH could be and should be simpler. However, there are mechanisms in Slicer that prevent this currently. For example the fact that 2D volume display works in a completely different way from any other show/hide. Along the same line, regular show/hide of “3D” data (i.e. anything other than volumes) shows/hides it in 3D (DisplayNode::SetVisibility), and there is a quite de-coupled mechanism for 2D visibility for these data objects (SetSliceIntersectionVisibility). This second issue I tried to address by calling both when you click the eye in SH. But I haven’t figured out a good way for volumes. If somebody has a good idea to unify these concepts, it would be great.</p>
<p>Showing the volume in 3D by default might be a good idea, but the problem with that one is that usually a “raw” volume rendering shows up as a gray cube, and it would do more harm than good in my opinion. Maybe if we had a <em>really</em> stable automatic volume property setter…</p>

---

## Post #10 by @muratmaga (2018-12-12 19:06 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>. Thanks for the pointer. I never knew it existed! Making that more prominent would be more helpful.</p>
<p>I don’t think volume rendering coming like a box is necessarily a bad thing. At least it shows people that they are making progress. The challenge I have seen with the new users is that they can’t find the place to modify the transfer function (because Scalar Opacity Mapping tab is collapsed by default).</p>

---

## Post #11 by @cpinter (2018-12-12 19:16 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="5059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Making that more prominent would be more helpful</p>
</blockquote>
</aside>
<p>Yes we have ideas for that but none as good that we’d just go for it. The best idea so far is that we separate 2D and 3D visibility into two columns. Wouldn’t be hard to do either. But in general a consensus would be necessary. Unfortunately I cannot go to Las Palmas this time, but continuing this discussion there (including the rest of it, about simple mode and slicelets etc.) and reaching a decision would be really great.</p>

---

## Post #12 by @muratmaga (2018-12-13 05:21 UTC)

<p>Unfortunately I can’t make the PW either.<br>
I like two columns idea. I also would suggest making icons a bit bigger. On 4K screens (27") they look tiny and sometimes hard to tell what they show.</p>

---

## Post #13 by @lassoan (2018-12-13 17:12 UTC)

<p>Two columns might help, but we should think about other solutions, too, because two columns would mean that we need to click twice each time we want to show/hide a node. Also, if we add separate columns for 2D and 3D views, we may also need to add separate columns for table, plot, etc. views for consistency (table could be shown in a table and/or plot view). Another issue is that you cannot always easily toggle 3D visibility: if you turn off a model’s visibility then both 2D and 3D views will be affected. Maybe it would be better to keep a main visibility icon and adjust additional visualization options similarly as it is done now?</p>
<p>ParaView allows highlighting a view (by clicking in it) and then show/hide applies to that view. We could consider this approach.</p>
<p>In some other applications users drag a node to a view to display it in that view.</p>

---

## Post #14 by @chir.set (2018-12-13 17:58 UTC)

<p>My point of view as a user : it is simple enough.</p>
<p>This a very powerful application with a modular design to do tens of kinds of jobs. It is for users who <strong>want to invest time and effort</strong> to master it. They are not expected to master everything; I don’t master everything in Slicer for instance. But most users I know have the Windows-borne expectations : the application must know what they want to do before they move the mouse.</p>
<p>My opinion is that you would waste much developer’s time trying to accomodate such expectations. You’ll next find users who will still want it to be, not simpler, but as they wish it to be some day, and another way some other day.</p>
<p>Just my 2 cents.</p>
<p>Cheers.</p>

---

## Post #15 by @muratmaga (2018-12-13 18:29 UTC)

<p>I respectfully disagree.</p>
<p>It is not really so much about what users want now and they would want something else tomorrow. It is about identifying common issues that frustrate novice users who give Slicer a try before moving into something else.</p>
<p>Blender has always been like that to me. I always thought making a model spin around freely and capture its animation shouldn’t be this hard. That’s all I want to do in it. But because it is so hard, I never saw value in spending that much time investing on a single simple task. Have I done that, I would probably be using Blender for quite a bit of interesting scientific animations.</p>
<p>Slicer has been that way to me (and the people I train). I might be wrong but, I wouldn’t be surprised if 95% of the people is using 1% of the functionality of Slicer. The challenge is identifying that 1%, and making it easier so that we retain users, who see value in investing more time in more complex things. To me that basis has always been the core visualization and segmentation capabilities. Fixing common pitfalls for new users seems like a valuable use of time and a good way to keep project funded.</p>

---

## Post #16 by @cpinter (2018-12-13 18:36 UTC)

<p>I actually agree with both of you. I agree with <a class="mention" href="/u/chir.set">@chir.set</a> because I don’t think we need a “SimpleSlicer” and a regular Slicer to keep novice users happy, but it can be achieved with reasonable time investment. And I agree with you that we should strive to simplify the most trodden paths in Slicer even if the whole thing is extremely complex.</p>

---

## Post #17 by @brhoom (2018-12-13 18:50 UTC)

<blockquote>
<ul>
<li>Create two different applications ? Or have theme like Blender ? Simple vs Advanced</li>
</ul>
</blockquote>
<p>I am with the theme idea. Many radiologists used to use tools similar to <a href="https://horosproject.org" rel="noopener nofollow ugc">Horos</a>. It would be nice if we have a theme that creates a similar navigation functionality.</p>

---

## Post #18 by @cheer_chen (2018-12-13 23:49 UTC)

<p>I am new here. but I was fascinated by 3Dslicer. I am eager to learn how to use it, but there are few videos to learn this powerful tool. nice to see you.</p>

---

## Post #19 by @lassoan (2018-12-20 18:02 UTC)

<p>I’ll copy below posts from another topic that ended up discussing simple Slicer user interface.</p>

---

## Post #20 by @lassoan (2018-12-17 22:05 UTC)

<p>You can start Slicer with a script that hides all user interface elements that you don’t need. Maybe it could be then considered as a “simple DICOM viewer”. You can also run it in a docker container and make it available in a web browser (you then don’t even need to install anything).</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> How difficult would it be to make VNC access available for Slicer running using binder? Slicer could then work pretty well as a web-based DICOM viewer.</p>

---

## Post #21 by @avarghes23 (2018-12-17 22:28 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="15" data-topic="5082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/exporting-dicom-directory-after-segmenting-lesion/5082/15">Exporting DICOM directory after segmenting lesion</a></div>
<blockquote>
<p>You can start Slicer with a script that hides all user interface elements that you don’t need. Maybe it could be then considered as a “simple DICOM viewer”. You can also run it in a docker container and make it available in a web browser (you then don’t even need to install anything).</p>
</blockquote>
</aside>
<p>I might have to explore that option then. Would it similar to the “Slicelets” mentioned in this post?</p><aside class="quote" data-post="1" data-topic="5056">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/8e8cbc/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/is-it-possible-to-create-a-standalone-application-with-3d-slicer-and-run-it-without-3d-slicer-launching/5056">Is it possible to create a standalone application with 3D slicer and run it without 3D Slicer launching?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Operating system: win 10 
Slicer version: 4.8 
Expected behavior: 
Actual behavior: 
Hi Guys, 
Is it possible to create a standalone application with 3D slicer and run it without 3D Slicer launching? I mean the application can works in other computers without 3D Slicer. 
Thanks a lot!
  </blockquote>
</aside>

<p>Then I should be able to make a standalone application that has the four up view and the segmentations/segment editor module. Is that possible? I’m familiar with basic coding but not too familiar with Python so I’m also wondering how feasible this would be for me to get set up.</p>

---

## Post #22 by @ihnorton (2018-12-18 15:02 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="15" data-topic="5082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/exporting-dicom-directory-after-segmenting-lesion/5082/15">Exporting DICOM directory after segmenting lesion</a></div>
<blockquote>
<p>How difficult would it be to make VNC access available for Slicer running using binder? Slicer could then work pretty well as a web-based DICOM viewer.</p>
</blockquote>
</aside>
<p>Mybinder tightly restricts connections – for understandable reasons. There is a prototype extension called <a href="https://github.com/ryanlovett/nbnovnc">nbnovnc</a> which facilitates VNC over a websocket within Jupyter. I have an updated dockerfile which integrates and launches that, but found out nbnovnc is incompatible with current pip versions of various dependencies (and doesn’t seem to be actively maintained). I haven’t had a chance to dig in and try to fix this yet (might be possible to just pin to older versions, but some discussion on their issue tracker suggested it was not so simple).</p>

---

## Post #23 by @fedorov (2018-12-18 15:19 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="15" data-topic="5082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/exporting-dicom-directory-after-segmenting-lesion/5082/15">Exporting DICOM directory after segmenting lesion</a></div>
<blockquote>
<p>How difficult would it be to make VNC access available for Slicer running using binder? Slicer could then work pretty well as a web-based DICOM viewer.</p>
</blockquote>
</aside>
<p>I think in most cases users want a desktop/client-side viewer. I don’t think binder+VNC would replace this need, especially considering PHI. Users of Slicer have been asking for a quick image viewer for as long as I can remember. I think it might be worthwhile to consider a slicelet or some other customization that would deliver such functionality.</p>

---

## Post #24 by @lassoan (2018-12-18 17:30 UTC)

<aside class="quote no-group quote-post-not-found" data-username="fedorov" data-post="18" data-topic="5082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"><a href="https://discourse.slicer.org/t/exporting-dicom-directory-after-segmenting-lesion/5082/18">Exporting DICOM directory after segmenting lesion</a></div>
<blockquote>
<p>I think in most cases users want a desktop/client-side viewer. I don’t think binder+VNC would replace this need, especially considering PHI.</p>
</blockquote>
</aside>
<p>Images would be pulled from a provided URL on the fly. For sensitive data or faster performance a local JupyterHub installation can be used, too (it’s been set up like that in Children’s Hospital of Philadelphia to allow researchers to use shared GPU cluster from Jupyter notebooks).</p>
<p>Desktop viewer is even simpler, as there is no need for setting up remote desktop.</p>
<p>For example, <a href="https://gist.github.com/lassoan/7d4cec3012155e2597ee3f47157f0a65">this script</a> shows a this simplified user interface:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0881b7a7c85529bef93b50779a8b8b907819680.jpeg" data-download-href="/uploads/short-url/tKKVc0J2ZQgGAlTYSaJtkXWdljW.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0881b7a7c85529bef93b50779a8b8b907819680_2_690x464.jpeg" alt="image" data-base62-sha1="tKKVc0J2ZQgGAlTYSaJtkXWdljW" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0881b7a7c85529bef93b50779a8b8b907819680_2_690x464.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0881b7a7c85529bef93b50779a8b8b907819680.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0881b7a7c85529bef93b50779a8b8b907819680.jpeg 2x" data-dominant-color="898889"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">834×562 149 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Simplifications:</p>
<ul>
<li>Hide module panel - show a subject hierarchy tree instead</li>
<li>Hide push-pin icon in slice views (volumes can be shown/hidden using the data tree)</li>
<li>Toolbars are hidden (they can be re-enabled using menu)</li>
</ul>

---

## Post #25 by @pieper (2018-12-18 18:31 UTC)

<p>The nice part is that any simple viewer setup that works well on the desktop is also usable in the docker/novnc environment.</p>

---

## Post #26 by @avarghes23 (2018-12-20 17:07 UTC)

<p>That SimpleView screenshot looks perfect for my needs. Could somebody please tell how to execute that SimpleView.py script.  I believe that would be a great foundation for the simplified standalone program I am trying to create.</p>
<p>Program features:</p>
<ol>
<li>Be able to toggle between four-up view, red,green, and yellow slice only views, 3D view, or split screen (i.e.: red and 3D, green and 3D, or yellow and 3D)</li>
<li>Be able to view segmentations that were previously done by another user (So if I created the segmentation in Slicer Nightly, then the user can view that same segmentation in the simplified Slicer)</li>
<li>Be able to edit segmentations if needed</li>
<li>Must be executable as a standalone program (ideally as a desktop application with no internet required)</li>
</ol>
<p>Any suggestions or advice are much appreciated.</p>

---

## Post #27 by @lassoan (2018-12-20 18:33 UTC)

<aside class="quote no-group" data-username="avarghes23" data-post="26" data-topic="5059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>That SimpleView screenshot looks perfect for my needs. Could somebody please tell how to execute that SimpleView.py script.</p>
</blockquote>
</aside>
<p>To run it once, open Python console (Ctrl+3) and paste the code into the console.</p>
<p>To make Slicer always start up with this interface, edit your .slicerrc.py file (you can find its location shown in menu: Edit / Application settings / General / Application startup script).</p>

---

## Post #28 by @lassoan (2018-12-20 18:34 UTC)

<aside class="quote no-group" data-username="avarghes23" data-post="26" data-topic="5059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>Be able to toggle between four-up view, red,green, and yellow slice only views, 3D view</p>
</blockquote>
</aside>
<p>I’ve added a few layout switch buttons above the data tree:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ed543c73e721d4a6368e846bb3183629670fba5.png" data-download-href="/uploads/short-url/mF6mc2dvZqCXiPFIPVWpEFgVO9n.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed543c73e721d4a6368e846bb3183629670fba5_2_690x465.png" alt="image" data-base62-sha1="mF6mc2dvZqCXiPFIPVWpEFgVO9n" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9ed543c73e721d4a6368e846bb3183629670fba5_2_690x465.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ed543c73e721d4a6368e846bb3183629670fba5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ed543c73e721d4a6368e846bb3183629670fba5.png 2x" data-dominant-color="A4A6A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">837×565 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #29 by @muratmaga (2018-12-20 18:28 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> this simple view looks much less intimidating for the new users. However, starting it through command line kind of defeats the purpose (most new users wouldn’t know where to look at it).</p>
<p>Would you guys consider enabling this as the default layout after the installation ends. So like checkbox question. “Do you want to enable SimpleView layout of Slicer?” with a brief explanation of what it does and how to go find the modules and an option to disable it, if they want full layout?</p>

---

## Post #30 by @lassoan (2018-12-20 18:46 UTC)

<p>At this point, this script is more like an experiment to see what is that people find intimidating in the current GUI.</p>
<p>Should we hide most of the toolbars? Should we start up with the Data module? Should we simplify viewer controls?</p>
<p>It may be also a useful to make this data tree widget available in addition to module panel (as you can already do it):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d549b16c3e27cb6e7a415388011f484a12267f76.jpeg" data-download-href="/uploads/short-url/uqPArI4QoWHu3Sv4jxMMeXZd7Ey.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d549b16c3e27cb6e7a415388011f484a12267f76_2_690x362.jpeg" alt="image" data-base62-sha1="uqPArI4QoWHu3Sv4jxMMeXZd7Ey" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d549b16c3e27cb6e7a415388011f484a12267f76_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d549b16c3e27cb6e7a415388011f484a12267f76_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d549b16c3e27cb6e7a415388011f484a12267f76_2_1380x724.jpeg 2x" data-dominant-color="A5A6AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1918×1007 400 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #31 by @fedorov (2018-12-20 19:18 UTC)

<p>In the past, we also discussed the idea where extension-specific or operation-specific functionality could be exposed as separate application launchers/shortcuts. Here is that thread for completeness: <a href="https://discourse.slicer.org/t/customized-application-launchers/564" class="inline-onebox">Customized application launchers</a>. I still think that is a nice way to approach this problem.</p>

---

## Post #32 by @avarghes23 (2018-12-20 19:35 UTC)

<p>I was able to incorporate the SimpleView script into the Application startup script and it works perfectly. Now the only issue is that the SimpleView launches every time I open Slicer. I downloaded both the Nightly and the Stable  versions. Is there a way that I could have the Stable version use the SimpleView startup script and the Nightly version use the regular startup script?</p>

---

## Post #33 by @lassoan (2018-12-20 21:35 UTC)

<aside class="quote no-group" data-username="avarghes23" data-post="32" data-topic="5059">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/a9a28c/48.png" class="avatar"> avarghes23:</div>
<blockquote>
<p>Is there a way that I could have the Stable version use the SimpleView startup script and the Nightly version use the regular startup script?</p>
</blockquote>
</aside>
<p>You can put a version check in the script and only call showSimpleUserInterface(True) and createSimpleDataBrowser() if a specific version is found. For example:</p>
<pre><code class="lang-auto">if slicer.app.applicationVersion == '4.10.0':
    showSimpleUserInterface(True)
    createSimpleDataBrowser()
</code></pre>

---
