# New user-stuck getting segment editor tools to work

**Topic ID**: 26472
**Date**: 2022-11-28
**URL**: https://discourse.slicer.org/t/new-user-stuck-getting-segment-editor-tools-to-work/26472

---

## Post #1 by @Lohi (2022-11-28 07:20 UTC)

<p>well, super-basic stuff… i can’t seem to get tools to work, at all…clearly something basic missing; i tried a little tutorial, which included a data set to download in a tar.gz format…this <em>seemed</em> to open into three views, but there is an instruction to set threshold values 410 to 4096, but what appears to br ‘threshold’ vslues are greyed out, and reading ‘9’.<br>
when i get back to my desktop machine, i’ll try to get a more complete description, but, in any case, i can’t seem to figure out these tools, at all.</p>

---

## Post #2 by @pieper (2022-11-28 08:57 UTC)

<p>It sounds like you may have missed a step.  Make sure you are using a tutorial from a recent version of Slicer.  If you are still having trouble post some screenshots and someone should be able to make some suggestions for you.</p>

---

## Post #3 by @Lohi (2022-11-28 10:05 UTC)

<p>it seems like i miss a step, no matter what i try… part of the problem, and I’ve done it myself, is that the people with the experince, and the spirit to contribute, have too much expertise, and simply can’t see the little things that they do, as second nature, and the preferences already set, and, sometimes, a sequence that is required: thus, a simple guy like me blunders into a series of dead-ends. btw, you mentioned “camera” into a viewport, which immediately clarified something, but the word “camera” doesn’t seem to appear in the documentation that i found. Also, the Microsoft mouse scroll wheel button works for the 'three button mouse’s things, thanks…</p>

---

## Post #4 by @lassoan (2022-11-28 14:26 UTC)

<p>It may be easier to post a full screenshot of your computer and mark where you don’t see what you expect.</p>
<p>If you encounter any problems, you can try to use sample data sets, to see if there may be something special/unexpected in your data.</p>

---

## Post #5 by @Lohi (2022-11-28 23:19 UTC)

<p>Here’s the ‘state’ I was in, using scissors tool, and the tools seem to be displaying, but not doing anything…you can probably spot in ten seconds what’s wrong…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/ca5af60041efe010e6afbcff872012307d7458bb.jpeg" data-download-href="/uploads/short-url/sS7kA0IXwuQ5E6z9X1JjhJHvevF.jpeg?dl=1" title="Screenshot 2022-11-29 at 0.13.54 .png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca5af60041efe010e6afbcff872012307d7458bb_2_562x401.jpeg" data-base62-sha1="sS7kA0IXwuQ5E6z9X1JjhJHvevF" alt="Screenshot 2022-11-29 at 0.13.54 .png" width="562" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca5af60041efe010e6afbcff872012307d7458bb_2_562x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca5af60041efe010e6afbcff872012307d7458bb_2_843x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/ca5af60041efe010e6afbcff872012307d7458bb_2_1124x802.jpeg 2x" data-dominant-color="9D9DA0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-11-29 at 0.13.54 .png</span><span class="informations">1528×1090 296 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2022-11-29 03:06 UTC)

<p>Thank you, the screenshot is very helpful!</p>
<p>“Erase inside” erases parts from existing segments. You will not see any effect of this until you paint something. Choose “Fill inside” to paint something first (or use any of the other effects Paint, Draw, Threshold, etc.).</p>
<p>I would also recommend to hide volume rendering when you are segmenting, because it occludes your 3D view.</p>

---

## Post #7 by @Lohi (2022-11-29 07:40 UTC)

<p>thanks, Maestro!</p>
<p>perhaps you can imagine that this aspect of the erase and scissors tools are not at all self-evident? It seemed, to my simple mind, that one might simply use those tools to increase rendering performance by reducing image volume, or eliminate parts of the image that occlude other parts… and there is no error indicated if there is nothing for the tool to operate on…<br>
to someone who has used the tool, or developed it, it is ‘self-evident’ that the scissors and erase work on selections, which are part of a ‘segment’ that one is building, simply by the name of the tool-set ‘segmentation editor’.<br>
i guess that what i was trying to do is more like a free-form ROI selection? That’s what i thought the scissors tool did, because that’s how it works in Osirix and Horus…<br>
one more box ‘ticked’ in learning, but, maybe, something to think about clarifying to people who could easily be coming from those other imaging tools?<br>
btw, i was following a tutoring from ‘medislicer’, a French person’s tutorial … another pointer about tutorials: perhaps the tutorial should be done with larger pointer size in use, and larger fonts, and, checked for video quality…it’s often very difficult to see the pointer as the teacher selects items, difficult to read selected module names, and, in the case of the tutorial from this gentleman’s, the contrast was so low, and icons so small, that it was really hard to see what was being selected. Again, not to devalue the efforts of all the people who are selflessly trying to help us out, just some observations, from someone who has had to produce training presentations for colleagues and customers …</p>
<p>again, thanks for quickly clarifying! screenshots are clearly ‘the way to go’.</p>

---

## Post #8 by @muratmaga (2022-11-29 14:00 UTC)

<aside class="quote no-group" data-username="Lohi" data-post="7" data-topic="26472">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b782af/48.png" class="avatar"> Lohi:</div>
<blockquote>
<p>i guess that what i was trying to do is more like a free-form ROI selection?</p>
</blockquote>
</aside>
<p>You can use the scissors as the free-hand selection tool. Just change the mode from erase to fill as <a class="mention" href="/u/lassoan">@lassoan</a> suggested.</p>

---

## Post #9 by @Lohi (2022-11-29 16:02 UTC)

<p>so…set scissors to “erase outside”…‘fill inside’…so, using scissors in the opposite way that one ‘intuitively’ expects. is it so that the scissors tool, used that way, affects all slices in a view, or sequence? learning a new tool set, while struggling with neurological problems is a bit of a hard road. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"><br>
thank for the support!</p>

---

## Post #10 by @muratmaga (2022-11-29 16:11 UTC)

<aside class="quote no-group" data-username="Lohi" data-post="9" data-topic="26472">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b782af/48.png" class="avatar"> Lohi:</div>
<blockquote>
<p>so…set scissors to “erase outside”…‘fill inside’…so, using scissors in the opposite way that one ‘intuitively’ expects. is it so that the scissors tool, used that way, affects all slices in a view, or sequence? learning a new tool set, while struggling with neurological problems is a bit of a hard road. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
</blockquote>
</aside>
<p>By default it affects all the slices, however, you can set the “depth limit” it is going to apply by using the Slice Cut option. As opposed to thinking how scissors “should be working” based on your experience with other software, you need to focus on how “it is working” in Slicer (as well as all the other tools in segment editor). You might find this tutorial helpful for segmentation in Slicer: <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/Segmentation.md">https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/Segmentation.md</a></p>

---

## Post #11 by @Lohi (2022-11-29 18:22 UTC)

<p>gee…“instead of thinking how it should be working”… i am working on getting a handle on it, but also comparing to the majority of applications, even graphical, or spectrum analyzers. it just means shifting mental gears. different isn’t always better, but one has to work with what is.</p>

---

## Post #12 by @Lohi (2022-11-29 23:06 UTC)

<p>That tutorial is working pretty well for me, but there are a couple of things that I’m not ‘getting’, yet… tomorrow…</p>
<p>Thanks for the link</p>

---

## Post #13 by @muratmaga (2022-11-30 00:36 UTC)

<aside class="quote no-group" data-username="Lohi" data-post="12" data-topic="26472">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b782af/48.png" class="avatar"> Lohi:</div>
<blockquote>
<p>but there are a couple of things that I’m not ‘getting’,</p>
</blockquote>
</aside>
<p>Sounds good. Fire them away here, if you need more help.</p>

---

## Post #14 by @lassoan (2022-12-01 01:06 UTC)

<aside class="quote no-group" data-username="Lohi" data-post="11" data-topic="26472">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b782af/48.png" class="avatar"> Lohi:</div>
<blockquote>
<p>i am working on getting a handle on it, but also comparing to the majority of applications</p>
</blockquote>
</aside>
<p>We try to follow common conventions, but most other imaging software are 2D oriented, while Slicer works in 3D everywhere. Most concepts that work great in 2D are unusable or would be very limited in 3D.</p>
<p>The other difficulty is that Slicer has magnitudes more features than most other imaging applications and we generally avoid guardrails, which would limit on what functions are used on what data and how.</p>
<p>The end result is that Slicer requires significant learning effort, even for doing simple things. But we are here to help and the effort may worth it, as you get a free tool that you can use to solve almost any 3D imaging related tasks that you will ever come across.</p>

---

## Post #15 by @Lohi (2022-12-01 11:31 UTC)

<p>There seem to be so many interdependencies that I get to ‘the same place’ as I was at yesterday, but, it’s not the same place, at all.<br>
I appreciate that you folks seem pretty willing to help, but hate to burn up bandwidth that you probably need for your ‘day job’…</p>
<p>In any case, I’m supposed to be admitted to hospital on Monday, to, hopefully, get a bit more insight into my rather rare, and refractory-to-diagnosis neuro problems… I’ll probably do a bit more in the next day or two. I did get a pretty good extraction of the C-spine, with selection by threshold, and scissors and eraser, but having a bear of a time figuring out the ‘grow from seeds’ tool, and tried following three different tutorials, but it seems that most of them assume something…</p>
<p>Here’s a couple of ‘typical’ source images…</p>
<p>Again, thanks for the help, and willingness <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c63afca984248e7d4897bdfa3086aae4520a55ec.png" data-download-href="/uploads/short-url/shCUVioKTiOU37qU0Pwzv75JiXi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c63afca984248e7d4897bdfa3086aae4520a55ec_2_627x500.png" alt="image" data-base62-sha1="shCUVioKTiOU37qU0Pwzv75JiXi" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c63afca984248e7d4897bdfa3086aae4520a55ec_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c63afca984248e7d4897bdfa3086aae4520a55ec_2_940x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c63afca984248e7d4897bdfa3086aae4520a55ec.png 2x" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×826 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13ab17d29d73e47734b81fc5725d08acc59908d9.jpeg" data-download-href="/uploads/short-url/2NZDv6orq9g02yZSA0Y0ZaWcIJ3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ab17d29d73e47734b81fc5725d08acc59908d9_2_547x500.jpeg" alt="image" data-base62-sha1="2NZDv6orq9g02yZSA0Y0ZaWcIJ3" width="547" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ab17d29d73e47734b81fc5725d08acc59908d9_2_547x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13ab17d29d73e47734b81fc5725d08acc59908d9_2_820x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13ab17d29d73e47734b81fc5725d08acc59908d9.jpeg 2x" data-dominant-color="505050"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">992×906 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @Lohi (2022-12-01 22:00 UTC)

<p>Hi Andras;<br>
are you in TO? If so, do you know any of the Neurology folks who might work with CSF leak/ SIH?</p>
<p>Just working on a sequence, doing a Scissors operation on ‘All slices’, which takes some time… are there any operations that have a ‘Progress Bar’ implemented? As is, it’s sometimes hard to tell if it’s a huge processing load, or a system ‘hang’…</p>
<p>Just wondering.<br>
Back to the fun…</p>

---

## Post #17 by @lassoan (2022-12-03 15:16 UTC)

<aside class="quote no-group" data-username="Lohi" data-post="16" data-topic="26472">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b782af/48.png" class="avatar"> Lohi:</div>
<blockquote>
<p>are you in TO?</p>
</blockquote>
</aside>
<p>I’m in Kingston, ON.</p>
<aside class="quote no-group" data-username="Lohi" data-post="16" data-topic="26472">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/b782af/48.png" class="avatar"> Lohi:</div>
<blockquote>
<p>are there any operations that have a ‘Progress Bar’ implemented? As is, it’s sometimes hard to tell if it’s a huge processing load, or a system ‘hang’…</p>
</blockquote>
</aside>
<p>Only very few effects have progress bar. It would be nice to add to more but there are many other things to add/fix/improve, so I’m not sure when this is going to happen. Is there any specific effect that often makes you wonder whether it is worth waiting?</p>
<p>Slicer does not hang, so you just need to wait if something takes a long time (of course all software have bugs and so a hang is theoretically possible but thousands of people use Slicer every day, so most likely some of them would have reported it).</p>

---

## Post #18 by @Lohi (2022-12-03 17:08 UTC)

<p>ok, sir … my uncle was teaching at RMC, many the years ago, so we visited there from Petawawa several times; i recollect from a visit in 2002, it being a nice small city.</p>
<p>good to hear that Slicer is so robust! the 3d display from a 0,5 mm slice MRI seems to run for a while, but it’s getting to be an old machine. <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"> like the operator.</p>
<p>off to see the wizard, tomorrow, Dr. J Beck in Freiburg, to see if the best in the land can get the diagnosis nailed down…</p>
<p>keep well, thanks for the help and encouragement. I’ll probably be off-line for 6-10 days.</p>

---

## Post #19 by @lassoan (2022-12-18 17:02 UTC)

<p>A post was split to a new topic: <a href="/t/analyzing-myelography-images/26806">Analyzing myelography images</a></p>

---
