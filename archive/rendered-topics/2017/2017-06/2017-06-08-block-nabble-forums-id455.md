# Block nabble forums

**Topic ID**: 455
**Date**: 2017-06-08
**URL**: https://discourse.slicer.org/t/block-nabble-forums/455

---

## Post #1 by @Fernando (2017-06-08 11:43 UTC)

<big>
For anyone coming here from the mailing list, if you are interested in using Discourse via email, please see the following post:
</big>
<aside class="quote quote-modified" data-post="1" data-topic="67">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/using-discourse-as-a-mailing-list/67">Using Discourse as a mailing list</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" style="--category-badge-color: #ED207B; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    <a href="https://discourse.slicer.org/latest">Sign up to Discourse</a> using your email address, and log in. 


Click user icon, then your user name: 
[image] 


Click “Preferences”: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd9d07e5bdd2cfefa06e8ee532f47cdbf55f7c16.png" data-download-href="/uploads/short-url/tkWjKfUY03QL7iZncehr0tyWMSi.png?dl=1" title="image.png" rel="noopener nofollow ugc">[image]</a> 


Click “Emails”: 
[image] 


Click “Enable mailing list mode”, and select frequency of emails: 
[image] 


By default, you will be subscribed to posts in all categories. To disable notifications for a category, visit the category page: 
[image] 
 and select the “Muted” option in the notification preference menu:  
[image] 


To respond via email, simp…
  </blockquote>
</aside>

<hr>
<p>Hi all,</p>
<p>Isn’t it possible to modify the top message of slicer-users/devel to say that they are discontinued, add a link to Discourse and block the possibility to create new topics? Also, maybe ask the posters where they found the link to slicer-users/devel. So that hidden links are modified / removed.</p>

---

## Post #2 by @lassoan (2017-06-08 12:35 UTC)

<p>I don’t have access to any of these services but I agree these would need to be done. I think it should be possible to block new posts to the mailing list and set up an auto-response.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> You told 1-2 weeks ago that everybody was busy with a grant renewal - maybe now you could find some time to address this?</p>

---

## Post #3 by @pieper (2017-06-08 13:26 UTC)

<p>Does anyone have experience or suggestions for best configuring mailman to be read-only?</p>

---

## Post #4 by @ihnorton (2017-06-08 13:31 UTC)

<p>Someone with admin access should be able to edit the landing page templates to remove the signup links, and post a link to discourse. There are various posts around about how to go further, but that one should be an easy start.</p>

---

## Post #5 by @ihnorton (2017-06-08 13:32 UTC)

<p>A post was split to a new topic: <a href="/t/inviting-slicer-list-users-to-discourse/458">Inviting slicer-[list] users to Discourse?</a></p>

---

## Post #6 by @ihnorton (2017-06-08 13:33 UTC)

<p>I edited the Feedback page for Nightly and 4.6 to point to Discourse:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Report_a_problem" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Report_a_problem</a></p>

---

## Post #7 by @pieper (2017-06-08 19:21 UTC)

<p><a class="mention" href="/u/ihnorton">@ihnorton</a> do you know where the landing page template is configured?  I already changed the introductory description but I don’t see a place to turn off signup links.</p>
<p>From a quick search it seems that it we could disable the list using “emergency” moderation mode [1] together with an autoresponder message [2] that explains the move to discourse.   If there are no better suggestions I can try doing that (or pass over admin rights to anyone interested in experimenting).</p>
<p><a href="http://www.gnu.org/software/mailman/mailman-admin/node14.html" class="onebox" target="_blank">http://www.gnu.org/software/mailman/mailman-admin/node14.html</a></p>
<p><a href="http://oregonstate.edu/helpdocs/faq/how-do-i-set-mailman-send-automatic-response-anyone-who-posts-list" class="onebox" target="_blank">http://oregonstate.edu/helpdocs/faq/how-do-i-set-mailman-send-automatic-response-anyone-who-posts-list</a></p>

---

## Post #8 by @pieper (2017-06-09 17:08 UTC)

<p>I found the spot where I could comment out the subscribe option for the lists and pointed people here instead:</p>
<p><a href="http://massmail.spl.harvard.edu/mailman/listinfo/slicer-devel" class="onebox" target="_blank">http://massmail.spl.harvard.edu/mailman/listinfo/slicer-devel</a></p>
<p><a href="http://massmail.spl.harvard.edu/mailman/listinfo/slicer-users" class="onebox" target="_blank">http://massmail.spl.harvard.edu/mailman/listinfo/slicer-users</a></p>

---

## Post #9 by @pieper (2017-06-09 17:21 UTC)

<p>I updated the settings and added auto-response to all posts:</p>
<blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ce7f5eaa373f424394d28c4057dd08a57deadc7.png" data-download-href="/uploads/short-url/mo3srh1FFdwDNLzUWo6lKjtv4dp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9ce7f5eaa373f424394d28c4057dd08a57deadc7.png" alt="image" data-base62-sha1="mo3srh1FFdwDNLzUWo6lKjtv4dp" width="690" height="189" data-dominant-color="F4F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">692×190 16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<p>I decided not to block new posts with ‘emergency’ mode, at least for now.  I think the autoresponse is enough.</p>
<p>I also emailed the lists with an announcement:</p>
<p><a href="http://massmail.spl.harvard.edu/public-archives/slicer-users/2017/012111.html" class="onebox" target="_blank" rel="noopener">http://massmail.spl.harvard.edu/public-archives/slicer-users/2017/012111.html</a></p>
<p>Any other ideas to complete the transition?</p>

---

## Post #10 by @pieper (2017-06-09 17:22 UTC)

<p>By the way I’m not sure who set up the nabble interface and I didn’t look into turning it off.</p>

---

## Post #11 by @lassoan (2017-06-09 17:26 UTC)

<p>Thanks Steve, this should help.</p>
<p>What happens if somebody sends an email to <a href="mailto:slicer-devel@bwh.harvard.edu">slicer-devel@bwh.harvard.edu</a>? Does it get posted (sent to all subscribers)?<br>
Is the auto-response sent to all subscribers?<br>
I think it would be important to block posting of new messages because those would just clutter the archives and annoy subscribers. If subscription is disabled now, we could save the current user list (just in case we want to send invitation to Discourse, etc) and remove all subscribers.</p>

---

## Post #12 by @fedorov (2017-06-09 17:28 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="455">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I’m not sure who set up the nabble interface and I didn’t look into turning it off</p>
</blockquote>
</aside>
<p>Gmail to the rescue! <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>---------- Forwarded message ----------<br>
From: Steve Pieper <a href="mailto:pieper@bwh.harvard.edu">pieper@bwh.harvard.edu</a><br>
Date: Tue, Dec 1, 2009 at 7:21 PM<br>
Subject: Re: Nabble for Slicer lists?<br>
To: Andriy Fedorov <a href="mailto:fedorov@bwh.harvard.edu">fedorov@bwh.harvard.edu</a></p>
<p>Hi Andriy -</p>
<p>Excellent - very good thought.  I’ve been trying to nag/threaten/bribe the help list to re-activate searchable archives for these lists but with no avail.</p>
<p>I went ahead and signed up and started archives for slicer-devel and slicer-users.  We can see how it goes.</p>
<p>Thanks for the pointer!</p>
<p>-Steve</p>
<p>Andriy Fedorov wrote:</p>
<blockquote>
<p>Steve,</p>
<p>If I am not mistaken, Slicer lists are not searchable, and are not<br>
indexed by Google at this point.</p>
<p>I don’t know if you know about Nabble (<a href="http://www.nabble.com/">http://www.nabble.com/</a>), but<br>
this seems like an easy way to index and archive Slicer lists for<br>
better visibility in the community and ease of use.</p>
<p>Some Kitware lists archived in Nabble as an example of the capabilities:</p>
<p><a href="http://old.nabble.com/VTK-f14272.html">http://old.nabble.com/VTK-f14272.html</a><br>
<a href="http://old.nabble.com/ITK-f14223.html">http://old.nabble.com/ITK-f14223.html</a></p>
<p>AF</p>
</blockquote>

---

## Post #13 by @pieper (2017-06-09 17:55 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> Okay, guilty as charged!</p>
<p>I think I figured out how to turn off nabble and added a link to here.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> for now I only added the auto-responder and (unless you all got the message above) it only goes back to the original poster.</p>
<p>I see your point though about letting posts go through.  I’ll switch to ‘emergency’ moderator mode.</p>

---

## Post #14 by @pieper (2017-06-09 18:05 UTC)

<p>Okay - now should have things set up to moderate all posts rather than send them and also sends the auto-response.</p>

---
