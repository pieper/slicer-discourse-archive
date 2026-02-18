# Should we delete topics that end up not containing any useful information?

**Topic ID**: 3079
**Date**: 2018-06-05
**URL**: https://discourse.slicer.org/t/should-we-delete-topics-that-end-up-not-containing-any-useful-information/3079

---

## Post #1 by @lassoan (2018-06-05 14:21 UTC)

<p>I have been thinking about this, too. Should we delete topics that end up not containing any useful information (similarly to those that have been posted by error)?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/ihnorton">@ihnorton</a> <a class="mention" href="/u/fedorov">@fedorov</a></p>

---

## Post #2 by @pieper (2018-06-05 14:46 UTC)

<p>I don’t like editing history as it leads to confusion for the people who remember seeing something and then it is gone (or changed).</p>

---

## Post #3 by @jcfr (2018-06-05 15:08 UTC)

<blockquote>
<p>Should we delete topics that end up not containing any useful information (similarly to those that have been posted by error)?</p>
</blockquote>
<p>vs</p>
<blockquote>
<p>don’t like editing history as it leads to confusion for the people who remember seeing something and then it is gone (or changed).</p>
</blockquote>
<p>Could go either way.</p>
<p>In that particular case, I suspect the user didn’t realize Slicer should be restarted.</p>
<p>Marking the topic as resolved is a good first step i think. It shows the questions was addressed in some way.</p>

---

## Post #4 by @lassoan (2018-06-05 15:25 UTC)

<p>Such topic wastes time of all future forum readers that will try to find information on the site. If I search something on a forum then I read the first 5-10 topics that are found. Thus, any garbage topic left on the site reduces the chance of finding relevant answers.</p>
<p>Any deleted content is not actually deleted for a while (several weeks?), just indicated that it is deleted (it shows up with red borders or something like that), so people who get email notification and click on the link can still see what’s going on.</p>
<p>I agree that it may be difficult to decipher history when posts are edited/deleted, but this impacts magnitudes less number of people (only those signed up to get email notification about all topics; or those who set to follow a particular topic) than people who are trying to find information by searching on the site or using google. So, I think we should prioritize good final search results over accurate history.</p>

---

## Post #5 by @cpinter (2018-06-05 15:33 UTC)

<p>I think removing noise is more beneficial overall. If we deem a thread not useful and remove it, then I think it means that whoever wants to find it, shouldn’t, because it won’t help them. So we should only remove topics that have no added value whatsoever.</p>

---

## Post #6 by @fedorov (2018-06-05 17:03 UTC)

<p>I second <a class="mention" href="/u/pieper">@pieper</a>, I would not edit history.</p>
<p>In addition to the reasons Steve mentioned, repeated questions on the same topic is an indication that users have troubles locating the answers, which may or may not be due to the noise in the forum. That information is important on its own. Also, evaluation of the post’s value is subjective. Once we start deleting posts, this sets us on a slippery slope. I would only remove spam messages.</p>
<p>I would also hope that most useful/comprehensive posts will naturally separate from noise and repeat posts due to larger number of likes, I would let that happen on its own.</p>
<p>What I would suggest is to improve FAQ to make the topics that come up again and again more prominent. Maybe featuring those in the ReadTheDocs version could help. We could also add guidelines for posting a question that would instruct users to check specific page with FAQ first before posting a new message.</p>

---

## Post #7 by @cpinter (2018-06-05 17:18 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="6" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>indication that users have troubles locating the answers</p>
</blockquote>
</aside>
<p>What if we don’t even know the question based on the thread? For example in case of this one, I’m not sure what the actual problem was. Is keeping this one any useful?<br>
(Edit: “this one” is the topic where this originally was, <a href="https://discourse.slicer.org/t/cannot-find-my-installed-extension-in-modules/3072">here</a>)</p>
<p>I agree on the “slippery slope” notion, but we could have a brief checklist that makes this decision objective.</p>

---

## Post #8 by @lassoan (2018-06-05 17:37 UTC)

<p>There is no such thing as a slippery slope. We can establish some guidelines that we follow and stick to it. If we want to change the rules then we do that.</p>
<p>For example, when a user essentially revokes a question (“sorry, my bad”) and there have been no useful answers, then I think it is safe to delete the post.</p>
<p>I agree that the fact of even receiving a question is a piece of valuable information, but we do not need to keep this information in the forum. For example, a note can be added to a related mantis issue.</p>

---

## Post #9 by @fedorov (2018-06-05 17:46 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>What if we don’t even know the question based on the thread? For example in case of this one, I’m not sure what the actual problem was. Is keeping this one any useful?<br>
(Edit: “this one” is the topic where this originally was, <a href="https://discourse.slicer.org/t/cannot-find-my-installed-extension-in-modules/3072">here</a>)</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/cpinter">@cpinter</a> I think this post is in fact a great example that demonstrates why posts like this should not be deleted.</p>
<p>I may be wrong of course, but my interpretation of the problem that user had is that the module that PET-DICOM extension installs is a DICOM plugin, which is an “invisible” module and cannot be found in the list of modules. I can definitely see how this can be confusing to the users. This is also an example where for one developer this post could be noise, but in fact it can provide valuable insight for improving documentation. You cannot address something like this with a checklist. I also don’t quite see what why keeping this post would be particularly problematic.</p>
<p>In the situations where a post does not make sense (at least for the specific developer/maintainer at a given time), we could assign a descriptive tag to lump all such topics together. Developers/maintainers could on their spare time go over the topics in that category to try to get insight on the trends and interpret issues better.</p>
<p>About mantis, it contains interpretations and well-defined technical issues, while I think of the forum as “raw” user feedback. I am not convinced of the value of deleting such evidence documents.</p>

---

## Post #10 by @cpinter (2018-06-05 17:54 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>installs is a DICOM plugin, which is an “invisible” module</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>I suspect the user didn’t realize Slicer should be restarted</p>
</blockquote>
</aside>
<p>This is what I mean, that we don’t know the question. We can guess around, but if we don’t know what the question was, the information is not useful.</p>
<p>At this point this is equiuvalent of thinking about design, that we do anyway. We already know that extensions containing DICOM plugins are not obvious to use. But this is not coming from a vague question where we cannot be sure what it refers to.</p>

---

## Post #11 by @fedorov (2018-06-05 18:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There is no such thing as a slippery slope. We can establish some guidelines that we follow and stick to it. If we want to change the rules then we do that.</p>
</blockquote>
</aside>
<p>The slippery slope is that current simple guidelines (i.e., don’t delete unless spam) will need to be more complex and will be changing over time to address things as we discover them, and they will have to become subjective (right now spam vs non-spam can be pretty objective). We are dealing with humans, not machines.</p>
<p>What if you have a non-native speaker who has troubles explaining the issue? How would you feel if you posted a question on a forum, which was not understood, but then you got busy with other things and didn’t respond in time to clarify, just to find that your post is gone? Can you demonstrate a precedent in another forum where a similar policy is successfully implemented?</p>
<p>Those rules can also be interpreted as censorship, as users might feel passionate about their role in the community.</p>
<p>With all the discussion so far, I respectfully disagree with removing any posts, unless they are clearly abusive or can be attributed to spam.</p>
<p>As an aside, we are now in a situation where we have a dissent in opinion, and I guess we could start with establishing a checklist of how to resolve such situation. Or is this the case where “benevolent dictator rule” applies?</p>

---

## Post #12 by @cpinter (2018-06-05 18:18 UTC)

<p>I agree with most of what you say. I’d feel very bad if somebody deleted my post although I’m trying to do my best. However there are extreme cases that we can cover. Here are two already, which are super easy to decide, and I don’t think there is any subjectivity involved.</p>
<ol>
<li>Person asking the question revokes the question</li>
<li>Person asking the question replies that it was solved without giving any details about the method of solution</li>
</ol>
<p>This second one even came up just a week ago at a conference, as an example how can stack exchange can be annoying. Even if it’s done with good intentions, it is just bad practice that could be a rule of our forum.</p>
<p>There are moderators on every forum, and if the forum has rules, then we can work to enforce them. In this case the goal is to avoid noise.</p>

---

## Post #13 by @pieper (2018-06-05 18:36 UTC)

<p>I agree posts in category 2 can be annoying, but I liked the gentle reminder you sent recently <a class="mention" href="/u/cpinter">@cpinter</a> and even if the original poser never comes to fix it, in a way, it’s exactly to <a class="mention" href="/u/fedorov">@fedorov</a>’s point that if someone finds that thread it will be a hint that they shouldn’t make posts like that (if it were deleted then nobody would ever find it!).</p>
<p>In any case, I wish it were easier to find old posts that are relevant.  The search results aren’t as useful as they could be maybe in part because of content-free threads, but I think mostly because we aren’t tagging/liking or otherwise curating as much as we could to make good content come to the top.</p>

---

## Post #14 by @cpinter (2018-06-05 18:46 UTC)

<p>Yes the ultimate goal is to make search more usable. If there is a way to “star” threads we think are most useful in any given category, and which show up on the top when it fits the search category, then it would solve the problem. If all of us know that it’s possible and the way it can be done, then it would be a good way to facilitate finding relevant information. (Although this is also a subjective process! So in that sense not different from the trimming approach)</p>
<p>Good point about the wider utility of my reminder, but I don’t think I’ll remind everyone <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> I just don’t open some topics because they are out of my expertise… However if there is a way to skew search results in favor of the most useful posts, then I’m OK with leaving useless posts up.</p>

---

## Post #15 by @fedorov (2018-06-05 18:51 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="14" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>However if there is a way to skew search results in favor of the most useful posts, then I’m OK with leaving useless posts up.</p>
</blockquote>
</aside>
<p>It is already there:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2cee4ea8eb08bf98cef0570e0cb2bc7d48f503e.png" data-download-href="/uploads/short-url/yDYOD9lTfN4ZiVE75vfli315MoC.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2cee4ea8eb08bf98cef0570e0cb2bc7d48f503e_2_636x500.png" alt="image" data-base62-sha1="yDYOD9lTfN4ZiVE75vfli315MoC" width="636" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2cee4ea8eb08bf98cef0570e0cb2bc7d48f503e_2_636x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2cee4ea8eb08bf98cef0570e0cb2bc7d48f503e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2cee4ea8eb08bf98cef0570e0cb2bc7d48f503e.png 2x" data-dominant-color="F3F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">814×639 91.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @cpinter (2018-06-05 19:30 UTC)

<p>If we can influence the default settings then it is useful. If you have to change something it is not, because nobody will do that.</p>

---

## Post #17 by @fedorov (2018-06-05 19:52 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="14" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>(Although this is also a subjective process! So in that sense not different from the trimming approach)</p>
</blockquote>
</aside>
<p>It is subjective, but it is not lossy! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<p>The rating system is a self-regulating distributed mechanism that is familiar to all users. We should just keep encouraging folks to use it more. Even if just the core group of active users starts giving more “thumbs up” to threads that are good, this will quickly help reduce the visibility for threads like the ones you want to remove, since by definition they will not get any "thumbs up"s.</p>

---

## Post #18 by @fedorov (2018-06-05 19:53 UTC)

<p>Plus, as was mentioned earlier, we should use topic tags more. This is again a place where some guidelines would help, and where we have better control of the outcome, since tags can be curated by core contributors (and they are also not going to lead to any content loss).</p>

---

## Post #19 by @fedorov (2018-06-05 20:39 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="16" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If we can influence the default settings then it is useful.</p>
</blockquote>
</aside>
<p>Here’s a post on (if I understand correctly!) how to configure discourse to sort by the number likes by default: <a href="https://meta.discourse.org/t/sort-filter-by-likes/26193">https://meta.discourse.org/t/sort-filter-by-likes/26193</a></p>

---

## Post #20 by @cpinter (2018-06-05 20:59 UTC)

<p>I made an observation about the “Most Liked” option, which was not obvious to me, and which makes me wonder if it’s the good choice.</p>
<p>I liked two of Andras’ comments in the best thread about an issue that came up many times (because I didn’t want to like the question itself), and found that the search results point to any post/comment with the most likes, and not just the threads. See the multiple occurrences of “Save volume rendering as STL file” in <a href="https://discourse.slicer.org/search?q=volume%20rendering%20st%20order%3Alikes">this search</a>.</p>
<p>In this form I don’t find this very useful. It would be much better if added all the likes together and showed the threads. I don’t want to dismiss anything, just an observarion so that we can make the most educated decision.</p>

---

## Post #21 by @fedorov (2018-06-05 21:02 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="20" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>It would be much better if added all the likes together and showed the threads.</p>
</blockquote>
</aside>
<p>I agree, this indeed would be very useful. I wonder if there is a plugin for that!</p>
<p>A related, I guess, idea could be to add “solved” or “solution” tag, which could then be used to configure the search using the existing search interface.</p>

---

## Post #22 by @fedorov (2018-06-06 15:53 UTC)

<p>About lumping the post likes together, I asked the question on the Discourse forum, but despite trying to clarify several times, I did not get an answer: <a href="https://meta.discourse.org/t/discourse-q-a-plugin-for-sorting-posts-with-the-most-likes-at-the-top/8414/24">https://meta.discourse.org/t/discourse-q-a-plugin-for-sorting-posts-with-the-most-likes-at-the-top/8414/24</a>. I guess my responses to that thread could also be deleted as I don’t think I added any useful information! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=5" title=":smiley:" class="emoji" alt=":smiley:"> Feel free to post to that “topic” to clarify/follow up.</p>

---

## Post #23 by @cpinter (2018-06-06 15:59 UTC)

<p>Thanks for trying! Their answers are frustrating at the least. In this sense I shouldn’t answer questions about “Segmentation Editor” because technically there is no such thing…</p>
<p>I’ll give it a go myself, hoping to get the terms right, and leave no possibility to intentionally misunderstand.</p>

---

## Post #24 by @cpinter (2018-06-07 16:28 UTC)

<p>These guys there are killing me… Maybe it’s a competition about how many replies you can muster without actually answering.</p>

---

## Post #25 by @fedorov (2018-06-07 16:43 UTC)

<p>I agree, that exchange was very un-helpful. I am not sure … Maybe this is our opportunity to feel “on the other side of the fence”. They have a community that has certain expectations (that we don’t know), and maybe the attitude is “this is so simple that if you cannot figure it out you don’t belong here”. No idea.</p>

---

## Post #26 by @lassoan (2018-06-07 16:51 UTC)

<p>Yes, it’s very interesting to experience what is it like to be a newbie. Discourse guys give correct answers and they answer quickly, but we still end up walking away with a bad impression because they are not friendly or empathetic.</p>

---

## Post #27 by @cpinter (2018-06-07 17:17 UTC)

<p>Definitely an interesting experience, but if the same style inquiry had been on our discourse, then we would have split the discussion into a topic in the right place, and gave some actual answer. Maybe brief and maybe with follow-up questions, but not such dismissive replies for sure. I’ll keep trying for a bit though.</p>

---

## Post #28 by @ihnorton (2018-06-07 18:04 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> (from <a href="https://meta.discourse.org/t/discourse-q-a-plugin-for-sorting-posts-with-the-most-likes-at-the-top/8414/25">here</a>):</p>
<blockquote>
<p>In the search result page every topic appears maximum once, ordered by the total number of likes in that topic, including the original post and the replies, which is in case of topic A is N*M. The link of the item in the search result page points to the original post in the topic (i.e. the whole topic).</p>
</blockquote>
<p>Is this what you want?</p>
<ul>
<li><a href="https://discourse.slicer.org/top?order=likes" class="inline-onebox">3D Slicer Community</a> (sorted by <em>total</em> likes on all posts in topic)</li>
</ul>
<p>See also:</p>
<ul>
<li><a href="https://discourse.slicer.org/top?order=op_likes" class="inline-onebox">3D Slicer Community</a> (sorted by number of likes on first post)</li>
</ul>

---

## Post #29 by @cpinter (2018-06-07 18:09 UTC)

<aside class="quote no-group quote-modified" data-username="ihnorton" data-post="28" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p><a href="https://discourse.slicer.org/top?order=likes" class="inline-onebox">3D Slicer Community</a> (sorted by <em>total</em> likes on all posts in topic)</p>
</blockquote>
</aside>
<p>Yes! If this is available for search, and we can make it the default, then problem solved.</p>

---

## Post #30 by @lassoan (2018-06-07 19:00 UTC)

<p>The ordering by number of likes (<a href="https://discourse.slicer.org/top?order=likes">https://discourse.slicer.org/top?order=likes</a>) does not seem to show the most important topics. Maybe liking posts more consistently could improve the list, since ordering based on views gives a much better result: <a href="https://discourse.slicer.org/top?order=views">https://discourse.slicer.org/top?order=views</a>.</p>
<p>Still, the current starting page (<a href="https://discourse.slicer.org/categories">https://discourse.slicer.org/categories</a>) looks much nicer to me.</p>

---

## Post #31 by @Lorensen (2018-06-07 19:06 UTC)

<p>Does google search the discourse site?</p>

---

## Post #32 by @ihnorton (2018-06-07 19:25 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="29" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If this is available for search, and we can make it the default, then problem solved.</p>
</blockquote>
</aside>
<p>Looks like they <a href="https://github.com/discourse/discourse/commit/681334701dc76f710556990ad2aa45295ed1703d">specifically disabled</a> the aggregate search mode for sort-by-likes a few years ago because: <code>likes are a pain to aggregate so skip</code> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>ordering based on views gives a much better result: <a href="https://discourse.slicer.org/top?order=views">https://discourse.slicer.org/top?order=views </a>.</p>
</blockquote>
</aside>
<p>That does look good. (FWIW, the default <a href="https://discourse.slicer.org/top">top</a> ordering weights by several factors including likes and views)</p>

---

## Post #33 by @lassoan (2018-06-10 02:33 UTC)

<aside class="quote no-group" data-username="Lorensen" data-post="31" data-topic="3079" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lorensen/48/31_2.png" class="avatar"> Lorensen:</div>
<blockquote>
<p>Does google search the discourse site?</p>
</blockquote>
</aside>
<p>Yes, google indexes this forum. About 70% of page views originates from google search, about 25% direct links (most probably clicks from email notifications), and the remaining few percent is from github, twitter, researchgate, etc. So, about 3x more people find posts through google search than following links in email notifications.</p>

---

## Post #34 by @cpinter (2018-06-11 17:39 UTC)

<p>An update about the encounter with discourse support: instead of answering, they deleted or otherwise made unaccessible the whole topic: <a href="https://meta.discourse.org/t/discourse-q-a-plugin-for-sorting-posts-with-the-most-likes-at-the-top/8414">https://meta.discourse.org/t/discourse-q-a-plugin-for-sorting-posts-with-the-most-likes-at-the-top/8414</a></p>
<p>I think it’s safe to say that it’s not just a case of being on the other side of the fence…</p>

---

## Post #35 by @fedorov (2018-06-11 18:01 UTC)

<p>Incredible. Well, I say - that is definitely NOT the precedent we should follow!</p>
<p>Would never expect that kind of attitude from a co-founder of a platform that is intended to enable communication, mutual understanding and collaboration.</p>

---

## Post #36 by @lassoan (2018-06-11 18:05 UTC)

<p>I can’t believe it’s been actually deleted (if it is then I’m shocked). I’ve asked what happened, we’ll see if we get response: <a href="https://meta.discourse.org/t/cannot-find-a-topic/89626">https://meta.discourse.org/t/cannot-find-a-topic/89626</a></p>

---

## Post #37 by @fedorov (2018-06-11 18:18 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="35" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Would never expect that kind of attitude from a co-founder of a platform</p>
</blockquote>
</aside>
<p>I apologize for that statement - I should not jump to conclusions. In that topic we were in communication with the forum user that had a label “co-founder”, but I don’t have any evidence that user is responsible for the fact that the topic is no longer accessible.</p>

---

## Post #38 by @muratmaga (2018-06-12 04:03 UTC)

<p>Well they deleted that ‘topic’ as well <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #39 by @lassoan (2018-06-12 04:22 UTC)

<p>I received this response in email then apparently the topic got deleted:</p>
<blockquote>
<p>sam Sam Saffron co-founder June 12</p>
<blockquote>
<p>lassoan: I would recommend improving discourse to make polite deletion/clean-up of topics as effortless as a hard, immediate delete.</p>
</blockquote>
<p>Technically nothing needs to change in Discourse. I undeleted said topic, closed it, added a message and scheduled it for deletion in 4 days. All of this is built in to Discourse.<br>
Forcing “unconditional”, mega polite delete is overkill and can lead to loss aversion which is less than ideal.<br>
This level of dancing is not usually required but I guess in this case we can be a little more prudent.</p>
</blockquote>
<p>This answer condescending but makes sense. Discourse guy are also really nice because they provide Slicer forum hosting for free and they have developed a great tool that they offer to anyone for free. The only thing that does not make sense to me is that it seems that on their forum when they consider a discussion to be finished then they delete the entire topic. There is a good chance that other people have complained, too, but we know what happens to such topics.</p>

---

## Post #40 by @ihnorton (2018-06-12 13:43 UTC)

<p>Several of the main Discourse people also created StackOverflow, and it seems they have carried over a similar philosophy: strictly one issue per topic, delete/close early and often.</p>
<p>(they do have &gt;30,000 users on just that site, as compared to 1000 here, so I can understand a degree of expedient moderation. but it sure would be nice to have a brief explanation rather than the generic “page not found” when that happens!)</p>

---

## Post #41 by @cpinter (2018-06-12 14:00 UTC)

<p>Agreed, a notification about deletion and at least a link to the now-private archived page for a few days would be welcome. At least I got an email with my comments after I complained that I couldn’t reuse my meticulously written feature request. I’ll create a new topic from that soon.</p>
<p>It is definitely interesting that they mercilessly hard-delete topics even with potentially useful discussions, while we debate an occasional deletion of “obviously useless” topics. I accept a never delete policy though, as long as the search results are not cluttered with those.</p>
<p>And yes, being able to use Discourse for Slicer for free is a huge perk for sure.</p>

---

## Post #42 by @lassoan (2018-06-12 14:11 UTC)

<p>Immediate deletion is clearly a mistake. Anyone who were following the discussion but not getting email notifications could not see the answer and I could not even add a like to the answer. Also, valid questions were raised and got answered, so I don’t see the point in erasing this information. Finally, deleting an active topic feels like shutting the door in someone’s face while he is still talking - quite rude.</p>
<p>Anyway, this was a useful experience. It’ll help me to be a bit more empathetic towards people who post in the Slicer forum.</p>

---

## Post #43 by @fedorov (2018-06-12 14:28 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="25" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>They have a community that has certain expectations (that we don’t know), and maybe the attitude is “this is so simple that if you cannot figure it out you don’t belong here”.</p>
</blockquote>
</aside>
<p>It’s interesting how my initial characterization was spot on. I’ve been communicating on forums and email lists well over decade now, but I don’t think I have ever seen such a hostile reaction from a forum leader. That was shocking to me.</p>
<p>But it was indeed a useful experience, even though it did not convince me in the advantages of the deletion, quite the opposite. It is not easy to define what “the topic” is, and how not to deviate from it. It is also difficult to assign the value to a conversation, since it is subjective. I still believe combination of tag-based curation, “thumbs up” and activity count is a better way to self-regulate the content.</p>

---

## Post #44 by @cpinter (2018-06-13 18:12 UTC)

<p>I added a new topic in the feature category on meta about ordering by the total number of likes: <a href="https://meta.discourse.org/t/ordering-search-results-by-total-number-of-likes-in-topic/89804">https://meta.discourse.org/t/ordering-search-results-by-total-number-of-likes-in-topic/89804</a><br>
I hope the category and the description is acceptable, and we get an answer.</p>

---

## Post #45 by @cpinter (2018-06-13 18:16 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="43" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>I still believe combination of tag-based curation, “thumbs up” and activity count is a better way to self-regulate the content</p>
</blockquote>
</aside>
<p>Should we establish guidelines for tag-based curation?<br>
The only thing that I can think of right now that would help me find a useful topic in the future is to add a specific tag in addition to the ones describing the topic for just this purpose. For example “FAQ” or something similar that marks a topic that contains a comprehensive and well-illustrated answer for a question that tends to come up every now and then.</p>

---

## Post #46 by @jcfr (2018-06-13 19:47 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="45" data-topic="3079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>For example “FAQ”</p>
</blockquote>
</aside>
<p>Then, would we migrate the following pages into discourse ?</p>
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ" class="inline-onebox">Documentation/Nightly/Developers/FAQ - Slicer Wiki</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/4.8/FAQ" class="inline-onebox">Documentation/4.8/FAQ - Slicer Wiki</a></li>
</ul>

---

## Post #47 by @cpinter (2018-06-13 19:52 UTC)

<p>I’m talking about a tag called “FAQ”, not a topic. Many times when people don’t use the search or cannot fnd what they are looking for, but post a question that several others have asked before, then it’s easy to point to the best of those previous topics. I propose marking those “best previous topics” with a tag. It can be called something else if FAQ is not good.<br>
Of course if ordering by aggregate likes worked, then they would be the ones that are on top of searches. I am just looking for alternatives, and following up on <a class="mention" href="/u/fedorov">@fedorov</a>’s “tag curation” suggestion.</p>
<p>I wouldn’t migrate wiki pages to discourse, because it’s a different modality: community discussions vs official documentation.</p>

---

## Post #48 by @fedorov (2018-06-13 20:05 UTC)

<p>I agree.</p>
<p>In spirit of “staying on topic” <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:">, I am going to start a new topic to specifically brainstorm tag curation ideas.</p>

---

## Post #49 by @cpinter (2018-06-20 23:05 UTC)

<p>FYI we got an answer from the Discourse guys:</p>
<p>“This would require a major rewrite of the way search works. I’d estimate this would take a week of time for an engineer on our team who has been working with Discourse for years. For someone on the outside, who is not already intimately familiar with Discourse, probably more like 3 or 4 weeks of engineering time.”</p>

---

## Post #51 by @pieper (2018-12-28 21:25 UTC)

<p>FYI I silenced this MERRI account. It has several spam posts like this where it just echoed the previous post.</p>

---

## Post #52 by @fedorov (2018-12-28 21:51 UTC)

<p>I removed 2 of his posts and sent him a PM that he will be removed from the system if I encounter another one.</p>

---
