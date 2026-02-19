---
topic_id: 42588
title: "Simultaneously Display A Sequence At Different Indices"
date: 2025-04-16
url: https://discourse.slicer.org/t/42588
---

# Simultaneously display a sequence at different indices

**Topic ID**: 42588
**Date**: 2025-04-16
**URL**: https://discourse.slicer.org/t/simultaneously-display-a-sequence-at-different-indices/42588

---

## Post #1 by @jamesobutler (2025-04-16 19:00 UTC)

<p>How would I go about displaying a sequence in the slice views where one 2D slice viewer is displaying the sequence at a given index and another 2D slicer viewer is displaying the same sequence at a different index?</p>
<p>Consider the following use case - I have loaded Cardiac CT sequence and I have created a segmentation sequence that segments the heart at each of the indices. How would I go about showing the CT+segmentation at <strong>systole</strong> in the “Red” 2D slice viewer and also the CT+segmentation at <strong>diastole</strong> in the “Green” 2D slice viewer? Where the current layout is Red+Green so both would be seen simultaneously.</p>
<p>Maybe <a class="mention" href="/u/lassoan">@lassoan</a> you have knowledge in this area of Sequences functionality as well as Cardiac.</p>
<p>This principle of displaying the a specific index of a sequence in a given 2D slice viewer could apply more broadly for comparing states of a sequence. I have considered creation duplicate objects in the Slicer scene as a workaround, but it can be difficult to keep things in sync if say I want to edit the segmentation at diastole while also simultaneously viewing the segmentation at systole. This is because any changes to my copied node I would have to update the object in the sequence as well and vice versa.</p>

---

## Post #2 by @lassoan (2025-04-16 19:33 UTC)

<p>This is a quite common use case in cardiac analysis. You can use multiple sequence browser nodes, each displaying a different time point. It works very well with segmentation, etc. all the sequence browser nodes can refer to the same sequences.</p>
<p>The only inconvenient thing is that you need to be mindful of which sequence browser node is selected in the Sequence toolbar. SlicerHeart modules often have sequence browser widget in the module GUI to make it easier to work with multiple sequence browser nodes in various views.</p>

---

## Post #3 by @jamesobutler (2025-04-16 19:39 UTC)

<p>Could you provide a mrb with a scene setup like this? I observe that if I have 2 sequence browsers that have the same synchronized sequence nodes specified that changing the index of one versus the other doesn’t produce the result I want to see. This is because the 2D slice viewer specifies a given volume node rather than a specific sequence index of said volume node.</p>

---

## Post #4 by @lassoan (2025-04-17 04:42 UTC)

<p>You can show different time point in each Slicer view by using different proxy nodes in each browser node. The slice viewer does not know anything about sequences, it just displays a proxy node.</p>

---

## Post #5 by @jamesobutler (2025-04-17 13:29 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="1" data-topic="42588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>have considered creation duplicate objects in the Slicer scene as a workaround, but it can be difficult to keep things in sync if say I want to edit the segmentation at diastole while also simultaneously viewing the segmentation at systole. This is because any changes to my copied node I would have to update the object in the sequence as well and vice versa.</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="42588">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can show different time point in each Slicer view by using different proxy nodes in each browser node.</p>
</blockquote>
</aside>
<p>Isn’t different proxy nodes resulting in multiple objects in the scene that I then I have to manage keeping in sync? If I update the segmentation of one of the proxy nodes I would then want it to be updated in the other.</p>

---

## Post #6 by @lassoan (2025-04-17 16:31 UTC)

<p>Each proxy node represents a different timepoint. You can view and update various timepoints in the same sequence via one or more proxy nodes. When you segment a volume sequence, then you usually store the segmentation in a sequence, too. No need for any manual updates, as the Sequences module keeps everything in sync.</p>

---

## Post #7 by @jamesobutler (2025-04-17 16:32 UTC)

<p>The different proxy nodes and a second sequence browser seems to be no different than just loading the “CT Cardio Sequence” sample data twice into the scene. I’m not viewing the same object at 2 different time indices simultaneously in the layout manager, but viewing 2 copies that I’m viewing at different sequence indices.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/faf1112016b436200aa0fe4aba1c021f00d8bb4c.png" data-download-href="/uploads/short-url/zNVQLsaceblspqMNOk32jDImaKg.png?dl=1" title="{102D5EBB-F241-4DEC-8A7F-8DCC9A9CA972}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/faf1112016b436200aa0fe4aba1c021f00d8bb4c.png" alt="{102D5EBB-F241-4DEC-8A7F-8DCC9A9CA972}" data-base62-sha1="zNVQLsaceblspqMNOk32jDImaKg" width="174" height="134"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{102D5EBB-F241-4DEC-8A7F-8DCC9A9CA972}</span><span class="informations">174×134 13.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dbca60134495f1b2f4c1e27236cb1190fb83b49.png" data-download-href="/uploads/short-url/4f41uCFZMVJtmY4rl4REw9LYWuJ.png?dl=1" title="{A04509B0-E494-47B3-B5FF-3D0EEAC752A0}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dbca60134495f1b2f4c1e27236cb1190fb83b49.png" alt="{A04509B0-E494-47B3-B5FF-3D0EEAC752A0}" data-base62-sha1="4f41uCFZMVJtmY4rl4REw9LYWuJ" width="541" height="229"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{A04509B0-E494-47B3-B5FF-3D0EEAC752A0}</span><span class="informations">541×229 6.03 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2025-04-17 16:35 UTC)

<p>I would not recommend to make a copy of the sequence nodes. Instead, you can add a secondary browser node for your existing volume sequence and segmentation sequence nodes.</p>

---

## Post #9 by @jamesobutler (2025-04-17 16:38 UTC)

<p>I guess I’m having difficulties understanding how to use the Sequences module GUI to do this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b765b93e8ed065f47e46b8a5735e121670aa21.png" data-download-href="/uploads/short-url/odnCpu2N20U3UL77V4zGtWWe5wt.png?dl=1" title="{FD6A909A-7616-4D33-8182-C251586D0682}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9b765b93e8ed065f47e46b8a5735e121670aa21.png" alt="{FD6A909A-7616-4D33-8182-C251586D0682}" data-base62-sha1="odnCpu2N20U3UL77V4zGtWWe5wt" width="535" height="299"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{FD6A909A-7616-4D33-8182-C251586D0682}</span><span class="informations">535×299 11.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Upon creating a 2nd browser and adding the CTCardioSeq as synchronized sequence to it<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5a01079e4b139386f4d35203dd63d8f035f33e0.png" data-download-href="/uploads/short-url/utODwBJ9RemDtpa7V9vPX6cXj4Q.png?dl=1" title="{70F86730-06A6-4A1C-B2F1-AB54D8695E89}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5a01079e4b139386f4d35203dd63d8f035f33e0.png" alt="{70F86730-06A6-4A1C-B2F1-AB54D8695E89}" data-base62-sha1="utODwBJ9RemDtpa7V9vPX6cXj4Q" width="537" height="293"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{70F86730-06A6-4A1C-B2F1-AB54D8695E89}</span><span class="informations">537×293 11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I observe now that I have 2 copies in the scene:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0b6914fa97ce2cae414019b6f2a97ba4f56e475.png" data-download-href="/uploads/short-url/ylrK191K2zczGDkK3RzA0Hyn5CB.png?dl=1" title="{4C0F6083-3A92-4162-A79D-68C20CC8176A}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f0b6914fa97ce2cae414019b6f2a97ba4f56e475.png" alt="{4C0F6083-3A92-4162-A79D-68C20CC8176A}" data-base62-sha1="ylrK191K2zczGDkK3RzA0Hyn5CB" width="537" height="143"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{4C0F6083-3A92-4162-A79D-68C20CC8176A}</span><span class="informations">537×143 5.03 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2025-04-17 16:41 UTC)

<p>I agree that the Sequences module GUI is not easy to use. Maybe what is confusing is that your proxy nodes are called <code>CTCardioSeq</code>. If you check the “Rename” checkbox (so that the timepoint is included in the proxy node name) then it may make things more clear.</p>

---

## Post #11 by @jamesobutler (2025-04-17 16:45 UTC)

<p>Ok I see it reflecting the name now.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31d1bc55ce3bb65ea9e97fcb85a6bee982764a52.png" data-download-href="/uploads/short-url/76IKFjtCnieIMkaqj8PShgXqcsW.png?dl=1" title="{6F8FFEB0-B273-4E2D-9B59-13EF269B1383}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31d1bc55ce3bb65ea9e97fcb85a6bee982764a52.png" alt="{6F8FFEB0-B273-4E2D-9B59-13EF269B1383}" data-base62-sha1="76IKFjtCnieIMkaqj8PShgXqcsW" width="635" height="288"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{6F8FFEB0-B273-4E2D-9B59-13EF269B1383}</span><span class="informations">635×288 11.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I want to do next is simultaneously display my CTCardioSeq at frame 0 in the Red 2D Slice viewer and my CTCardioSeq at frame 2 in the Green 2D Slice viewer. This is because I ultimately desire viewing 2 different indices simultaneously in the layout rather than toggling between the two. How would I go about this?</p>

---

## Post #12 by @jamesobutler (2025-04-17 16:52 UTC)

<p>Ultimately it appears that I’m still dealing with creating an additional copy of the object in the scene so that modules such as Volume Rendering no longer have the single option of  rendering CTCardioSeq, but now has 2 different volumes to choose from. If I threshold my proxy node, then it doesn’t also threshold my display at the 2nd sequence index. I would have to try and keep this sync with various observe events. It’s confusing in that I’m not really viewing 1 sequence at different indices, but have created 2 different sequences that I’m manipulating.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa3dfab6f05c5413b1ad6814b69d4e324fdfbfcb.png" data-download-href="/uploads/short-url/oi1XwJN75qf3QtDAL0z6EptZ2Nt.png?dl=1" title="{9BBB9C7F-19FF-4809-94F4-03096D2C6473}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa3dfab6f05c5413b1ad6814b69d4e324fdfbfcb.png" alt="{9BBB9C7F-19FF-4809-94F4-03096D2C6473}" data-base62-sha1="oi1XwJN75qf3QtDAL0z6EptZ2Nt" width="635" height="125"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{9BBB9C7F-19FF-4809-94F4-03096D2C6473}</span><span class="informations">635×125 6.26 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/664dce26f4776f34b411637266179f7810591804.png" data-download-href="/uploads/short-url/eB1oJSQSwz3wIc8J7uMvyyHUmwY.png?dl=1" title="{B712A373-C91C-4684-9E7A-5AB9CAC87F01}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/664dce26f4776f34b411637266179f7810591804.png" alt="{B712A373-C91C-4684-9E7A-5AB9CAC87F01}" data-base62-sha1="eB1oJSQSwz3wIc8J7uMvyyHUmwY" width="644" height="248"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{B712A373-C91C-4684-9E7A-5AB9CAC87F01}</span><span class="informations">644×248 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @jamesobutler (2025-04-17 16:56 UTC)

<p>If I want to view the 10 sequence index CTCardioSeq in a tiled film strip view of all the axial views, then it seems like my scene one would have 10 scalar volume nodes in the scene along 10 different sequence browsers.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44e28e033e721b80d7e85dd3e2dd4d79d7e9eccd.jpeg" data-download-href="/uploads/short-url/9PnRh3wdkk4MSjNdfqu84tUTkXb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44e28e033e721b80d7e85dd3e2dd4d79d7e9eccd_2_690x370.jpeg" alt="image" data-base62-sha1="9PnRh3wdkk4MSjNdfqu84tUTkXb" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44e28e033e721b80d7e85dd3e2dd4d79d7e9eccd_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44e28e033e721b80d7e85dd3e2dd4d79d7e9eccd_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/44e28e033e721b80d7e85dd3e2dd4d79d7e9eccd_2_1380x740.jpeg 2x" data-dominant-color="A9A9A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1032 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
