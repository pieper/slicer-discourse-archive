# Email mode config improvements

**Topic ID**: 140
**Date**: 2017-04-13
**URL**: https://discourse.slicer.org/t/email-mode-config-improvements/140

---

## Post #1 by @gcsharp (2017-04-13 20:51 UTC)

<p>Dear all,</p>
<p>I humbly submit that I dislike the new e-mail list.<br>
(No offense intended.  But I cannot tell a lie.)</p>
<p>See attachment for what it looks like in html e-mail (Outlook).<br>
The topic content is overshadowed by heavy-handed formatting.</p>
<p>In txt e-mail (Claws) the content/formatting ratio is better.<br>
But the excerpt feature does not work.  Also, there is no way<br>
to access images from a text e-mail client since they are<br>
neither attached nor is there a full URL link.</p>
<p>-Greg</p>
<p>PS: How can I see which e-mail is tied with which sub-forum?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da471548a5c8efec2e70b5ba715ad29580f538ec.png" data-download-href="/uploads/short-url/v8YnM6BHWUSAAMwodwnm9XpDwhm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da471548a5c8efec2e70b5ba715ad29580f538ec.png" alt="image" data-base62-sha1="v8YnM6BHWUSAAMwodwnm9XpDwhm" width="690" height="471" data-dominant-color="C0BDBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×736 37 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2017-04-13 20:53 UTC)

<p>You can configure in the preferences (<a href="https://discourse.slicer.org/users/lassoan/preferences">https://discourse.slicer.org/users/lassoan/preferences</a>, Email section) what you would like to get in the notification email.</p>

---

## Post #3 by @ihnorton (2017-04-13 21:40 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> thanks for the feedback! I’d rather we hear it now than have disgruntled users or less participation. Hopefully there are enough knobs available to make some of this better. I made a few tweaks that I hope will improve the situation – let me know how this looks to you by email.</p>
<p>I’m including the changes here, so I can remember what I did (and others can change/revert if needed).</p>
<ul>
<li>“Takes up way too much space”
<ul>
<li><code>email posts context</code> → 0</li>
</ul>
</li>
<li>“Only 10 characters visible” → shorten the title:
<ul>
<li><code>email prefix</code> → “Slicer” (instead of defaulting to <code>title</code>, which is “3D Slicer Forum”)</li>
</ul>
</li>
<li>“Stupid and redundant”, “Redundant. I already know the sender”</li>
<li>removed the following from “User Replied” “User Posted” “User Mentioned” “User Quoted” email templates (in admin settings):</li>
</ul>
<pre><code class="lang-auto">%{header_instructions}

%{context}

%{respond_instructions}
</code></pre>
<ul>
<li>“Image should be attachment or link”
<ul>
<li>I don’t quite know how to deal with this right now, unfortunately. Images are linked out to remote resources (and stripped from very short messages to avoid spam filter). Will investigate.</li>
</ul>
</li>
</ul>
<blockquote>
<p>PS: How can I see which e-mail is tied with which sub-forum?</p>
</blockquote>
<p>Email title. After the tweaks I think it should look like [Slicer/Forum feedback] (“Forum feedback” category), [Slicer/Support] (“Support” category), etc. We could potentially shorten names to get closer to the traditional [slicer-users] / [slicer-devel] length people are used to (unfortunately we can’t use the category “slug” in the title yet: <a href="https://github.com/discourse/discourse/pull/4799" class="inline-onebox">Add an optional category-specific [slug] for email subject lines. by icculus · Pull Request #4799 · discourse/discourse · GitHub</a>).</p>

---

## Post #4 by @ihnorton (2017-04-13 22:01 UTC)

<p>(another test for me to view on my test account)</p>
<ul>
<li>try using %{topic_slug} in the <code>email subject</code> setting</li>
</ul>

---

## Post #5 by @ihnorton (2017-04-13 22:03 UTC)

<p>(Oops, well that was ugly <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:">, reverting)</p>

---

## Post #6 by @lassoan (2017-04-14 06:03 UTC)

<p>The current [Slicer[Development] ] subject line prefix does not look nice: spacing is inconsistent, many square brackets, etc.</p>
<p>It would be also nice to be consistent with subject line prefix of GitHub notifications. For example, this is an email subject sent by GitHub:</p>
<blockquote>
<p>Re: [Slicer/Slicer] WIP: Use header metadata to initialize volume scalar range (<span class="hashtag-raw">#702</span>)</p>
</blockquote>
<p>I think [SlicerForum/Category/Subcategory] would be a short and consistent subject line prefix, for example:</p>
<blockquote>
<p>[SlicerForum/Support] Some subject abc abc<br>
[SlicerForum/Development] Some subject abc abc</p>
</blockquote>

---

## Post #7 by @ihnorton (2017-04-14 13:09 UTC)

<blockquote>
<p>It would be also nice to be consistent with subject line prefix of GitHub notifications.</p>
</blockquote>
<p>I agree, I tried a few iterations to get there but realized that the brackets around the category name are hard-coded in the template. So I reset it to <code> [Slicer][Development]</code> as the least-bad option. If the PR I linked above is merged and deployed then we’ll have more flexibility: it allows using the category short name (“slug”) and does not include brackets.</p>
<p>The other option would be to rename some categories, for example we could call Development <code>slicer-devel</code> and tweak the email subject template to only show the category name. It would look exactly like the old emails.</p>

---

## Post #8 by @lassoan (2017-04-14 13:32 UTC)

<p>I think [Slicer][Development] or [SlicerForum][Development] would be good for now and [SlicerForum/Development] or [Slicer/Forum/Development] in the long term. The old slicer-devel is not the best as we can have many more categories now and it’s also not consistent with how we name organizations and projects (for example, we use SlicerRT and not slicer-rt).</p>

---

## Post #9 by @gcsharp (2017-04-14 15:00 UTC)

<p>Wow, much better.  Thanks Isaiah!  I didn’t know this was possible.</p>
<p>These settings are only available for admins, not for users, right?</p>

---

## Post #10 by @gcsharp (2017-04-14 15:06 UTC)

<p>Agree old-style is not necessary.  My 2 cents: make as short as possible, so recipient can focus on content.  So “Slicer” &gt; “Slicer Forum”, and “Dev” &gt; “Development” etc.</p>

---

## Post #11 by @gcsharp (2017-04-14 15:49 UTC)

<p>It seems the “Include an excerpt of replied to post in emails” function is no longer working.<br>
Is it possible to get the excerpt without the fancy excerpt header?</p>

---

## Post #12 by @ihnorton (2017-04-14 18:15 UTC)

<aside class="quote no-group quote-post-not-found" data-username="gcsharp" data-post="29" data-topic="100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"><a href="https://discourse.slicer.org/t/initial-presentation/100/29">Initial presentation</a></div>
<blockquote>
<p>These settings are only available for admins, not for users, right?</p>
</blockquote>
</aside>
<p>Yeah, but squeaky wheel gets grease to the extent that tweaks are possible.</p>
<aside class="quote no-group quote-post-not-found" data-username="gcsharp" data-post="31" data-topic="100" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"><a href="https://discourse.slicer.org/t/initial-presentation/100/31">Initial presentation</a></div>
<blockquote>
<p>It seems the “Include an excerpt of replied to post in emails” function is no longer working.<br>
Is it possible to get the excerpt without the fancy excerpt header?</p>
</blockquote>
</aside>
<p>How’s this now? I put <code>%{context}</code> back, so 1 reply is included again, and leaving out <code>%{header_instructions}</code> appears to control the fancy formatting in the footer too.</p>
<p>As far as images: there are no options for attachments and/or inline Content-ID references. This may be intentional, to cut email cost (bulk, high-quality remailer isn’t free). So, hopefully images can be solved client-side. Technically the image URL is there in both the HTML and text versions, it’s just an <code>&lt;img&gt;</code> tag with no <code>&lt;a&gt;</code>. I realize these have minor downsides, but my suggestions:</p>
<ul>
<li>For Outlook: <a href="https://www.benchmarkemail.com/help-FAQ/answer/how-do-i-enable-my-email-client-to-display-images">enable remote content by sender domain</a>.</li>
<li>For Claws, several plugins for image viewing, which should understand the tag.</li>
</ul>

---

## Post #13 by @gcsharp (2017-04-17 13:09 UTC)

<p>I should have been more clear.  The problem is that the &lt; img&gt; tag is a relative link.  For example:</p>
<p>&lt; img src="//cdck-file-uploads-us1.s3.dualstack.us-west-2.amazonaws.com/flex002/uploads/slicer/original/1X/5ba5eb12ead7aa7295b5d2cada1c3c504730005d.png" width=“690” height=“456”&gt;</p>
<p>Outlook works fine.  But I don’t know how this can work in text e-mail, there is no reference to the server in the header.</p>

---

## Post #14 by @ihnorton (2017-04-18 15:17 UTC)

<p>I see. That does seem wrong, and there is no option that I’ve found to change it. I posted a message to the Discourse support site asking for help:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://meta.discourse.org/t/full-url-for-image-in-text-plain-emails/61198">
  <header class="source">
      <img src="https://d11a6trkgmumsb.cloudfront.net/optimized/3X/b/3/b33be9538df3547fcf9d1a51a4637d77392ac6f9_2_32x32.png" class="site-icon" width="" height="">

      <a href="https://meta.discourse.org/t/full-url-for-image-in-text-plain-emails/61198" target="_blank" rel="noopener" title="03:09PM - 18 April 2017">Discourse Meta – 18 Apr 17</a>
  </header>

  <article class="onebox-body">
    <img src="https://d11a6trkgmumsb.cloudfront.net/original/3X/e/c/ecc92a52ee7353e03d5c0d1ea6521ce4541d9c25.png" class="thumbnail" width="" height="">

<div class="title-wrapper">
  <h3><a href="https://meta.discourse.org/t/full-url-for-image-in-text-plain-emails/61198" target="_blank" rel="noopener">Full URL for image in text/plain emails</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #CEA9A9;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">support</span>
        </span>
      </span>
  </div>
</div>

  <p>In the the text/plain version of emails from Discourse,  URLs are relative. For example, the email notification for this post has the full URL in text/html, but only the relative URL in text/plain.  example email...</p>

  <p>
    <span class="label1">Reading time: 1 mins 🕑</span>
      <span class="label2">Likes: 8 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #15 by @ihnorton (2017-04-19 13:13 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> unfortunately, in the short term (1-2 months), I don’t think there’s going to be a solution to this. It appears to be a bug that no one paid attention to for <code>text/plain</code> emails (I would guess because “text mode”). The fix looks simple, but even if they change the code soon, it will likely take some time before such a code update would be deployed to the production servers.</p>
<p>One possible temporary solution is to apply a filter locally to messages from <a href="http://discoursemail.com">discoursemail.com</a> to prepend the full URL:</p>
<p><a href="http://www.claws-mail.org/faq/index.php/Filtering_and_Processing_of_Messages#Can_a_filter_modify_the_contents_of_a_message.3F" class="onebox" target="_blank">http://www.claws-mail.org/faq/index.php/Filtering_and_Processing_of_Messages#Can_a_filter_modify_the_contents_of_a_message.3F</a></p>

---

## Post #16 by @gcsharp (2017-04-20 13:52 UTC)

<p>Thank you Isaiah, the URL is not a show stopper, as I can switch to web<br>
browser to see images, but I really appreciate.</p>
<p>The “Include an excerpt of replied to post in emails” seems to no longer<br>
work at all.  (I have never seen an excerpt in text, but now also missing in<br>
html).  Any idea what is happening?</p>

---

## Post #17 by @ihnorton (2017-04-20 14:03 UTC)

<p>Hi Greg,</p>
<aside class="quote no-group">
<blockquote>
<p>The “Include an excerpt of replied to post in emails” seems to no longer<br>
work at all.  (I have never seen an excerpt in text, but now also missing in<br>
html).  Any idea what is happening?</p>
</blockquote>
</aside>
<p>Maybe I’m misunderstanding.  Would you mind to forward me a few messages (inorton @ bwh)? Do you see a “Previous Replies” section with 1 previous message quoted? It seems to be working correctly on my test account for both the <code>text/plain</code> and <code>text/html</code> sections – here’s what I get on my test account (which is in mailing list mode) for <a href="https://discourse.slicer.org/t/saving-images-from-slicer-views-in-headless-compute-node/138/11">this message</a>:</p>
<pre><code class="lang-auto">mike_i:
So thanks to you (and your older self from 6 years ago

Fair enough!

If it turns out you need to solve the other problem, for example extracting rendered 3D views from a headless Slicer I checked and a docker image that exposes a vnc connection for Xdummy works for me (you don't need to connect to it, just running the server seems to be enough).

-- 
Previous Replies


Thanks very much for the advice. Unfortunately, my project requires the linux machine to run automatically without a VNC connection to it. However, you did help me find a solution using a different method through an old post you made:
https://sourceforge.net/p/teem/mailman/message/27766556/

I think that approach is going to work. So thanks to you (and your older self from 6 years ago) I think the problem is solved! I'll keep you updated on my progress.

Mike

Posted by mike_i on 04/19/2017
</code></pre>

---

## Post #18 by @lassoan (2018-01-30 13:14 UTC)

<p>A post was split to a new topic: <a href="/t/whole-heart-data-set/1974">Whole heart data set</a></p>

---
