# What is the slicer discourse e-mail address?

**Topic ID**: 1329
**Date**: 2017-10-31
**URL**: https://discourse.slicer.org/t/what-is-the-slicer-discourse-e-mail-address/1329

---

## Post #1 by @gcsharp (2017-10-31 14:08 UTC)

<p>I want to start a topic by e-mail.  What is the slicer discourse e-mail address?</p>

---

## Post #2 by @jcfr (2017-10-31 14:12 UTC)

<p>Hi Greg,</p>
<p>The addresses are:</p>
<ul>
<li>
<p><code>slicer+support@discoursemail.com</code> for the Support category</p>
</li>
<li>
<p><code>slicer+dev@discoursemail.com</code> for the Development category</p>
</li>
</ul>

---

## Post #3 by @lassoan (2017-10-31 17:06 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> I see you’ve posted this topic through email: <a href="https://discourse.slicer.org/t/build-error-on-linux/1334/2">Build error on linux</a></p>
<p>Posting through the web GUI allows you to make the post more structured, cleaner, easier to read (by applying formatting, not having email signature), attach keywords, automatically get suggestions for similar topics that you might want to amend, etc.</p>
<p>What is the main motivation for posting by email?<br>
Would you be comfortable if we touched up your posts (remove signature, apply formatting, etc.)?</p>

---

## Post #4 by @gcsharp (2017-11-01 13:59 UTC)

<p>Hi Andras,</p>
<p>Posting by browser requires more effort.  I can send an email without touching the mouse at all.</p>
<p>You make a good point about the signature.  It seems to get stripped when I reply.  If there is a way to strip it automatically for a new post that would be great!</p>
<p>Greg</p>

---

## Post #5 by @ihnorton (2017-11-01 14:07 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="4" data-topic="1329">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>It seems to get stripped when I reply.</p>
</blockquote>
</aside>
<p>From what I can tell, Partners doesn’t add it for replies.</p>

---

## Post #6 by @lassoan (2017-11-01 14:14 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="4" data-topic="1329">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Posting by browser requires more effort.  I can send an email without touching the mouse at all.</p>
</blockquote>
</aside>
<p>OK. Would you mind (and in general do you think people would mind) if we reformat their posts (remove signature, apply proper formatting, keywords, etc.)?</p>

---

## Post #7 by @gcsharp (2017-11-01 14:33 UTC)

<p>I certainly don’t mind.  But only if it is automatic.  If it is manual, I don’t want to waste anyone’s time so I will just make new posts in the browser.</p>
<p>Isaiah, that is an interesting theory.  But I tested replying from Partners to an external account and found that a sig is appended.  My theory is that Discourse strips the sig when it strips the original message.</p>

---

## Post #8 by @ihnorton (2017-11-01 14:46 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="7" data-topic="1329">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>Isaiah, that is an interesting theory.  But I tested replying from Partners to an external account and found that a sig is appended.  My theory is that Discourse strips the sig when it strips the original message.</p>
</blockquote>
</aside>
<p>I checked several threads to which I sent replies from my Partners address to my gmail, and came to the opposite conclusion (however, forwards and new emails <strong>did</strong> contain the signature).</p>
<p>You can see <a href="https://github.com/discourse/email_reply_trimmer/blob/master/lib/email_reply_trimmer/signature_matcher.rb">here</a> the very small set of signatures which Discourse automatically strips – all similar to “sent from iPhone”. See some discussion and links here:</p>
<aside class="onebox discoursetopic" data-onebox-src="https://meta.discourse.org/t/email-replies-filter-signatures/56323/3">
  <header class="source">
      <img src="https://d11a6trkgmumsb.cloudfront.net/optimized/3X/b/3/b33be9538df3547fcf9d1a51a4637d77392ac6f9_2_32x32.png" class="site-icon" width="" height="">

      <a href="https://meta.discourse.org/t/email-replies-filter-signatures/56323/3" target="_blank" rel="noopener" title="11:58PM - 24 February 2017">Discourse Meta – 24 Feb 17</a>
  </header>

  <article class="onebox-body">
    <img src="https://d11a6trkgmumsb.cloudfront.net/original/3X/e/c/ecc92a52ee7353e03d5c0d1ea6521ce4541d9c25.png" class="thumbnail" width="" height="">

<div class="title-wrapper">
  <h3><a href="https://meta.discourse.org/t/email-replies-filter-signatures/56323/3" target="_blank" rel="noopener">Email replies filter signatures?</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #CEA9A9;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">support</span>
        </span>
      </span>
  </div>
</div>

  <p>I know there was a request earlier for the addition of a reply between the lines style parser where only the stuff between some delimiters would be posted, dropping all the signatures, etc. See...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2017-11-01 14:49 UTC)

<p>Discourse is not an archive of emails (as it used to be with the mailing list) but a searchable knowledge base, so it is worth the effort of keeping it clean and easy to read. I can spend additional half minute with reformatting while I’m reading a post.</p>

---
