# Easing users communication with developers

**Topic ID**: 36793
**Date**: 2024-06-14
**URL**: https://discourse.slicer.org/t/easing-users-communication-with-developers/36793

---

## Post #1 by @mau_igna_06 (2024-06-14 22:30 UTC)

<p>I made this that I would be adding to my extension, see picture and code below:</p>
<ul>
<li>See first button of section “Bug reports, Feature requests and Community”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5651a526adfafaf740ccfa62d489601d2cade775.png" data-download-href="/uploads/short-url/cjBZ9qLBbDaN9RyJJaHHADiOoN7.png?dl=1" title="Screenshot from 2024-06-14 19-20-02_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5651a526adfafaf740ccfa62d489601d2cade775_2_267x500.png" alt="Screenshot from 2024-06-14 19-20-02_2" data-base62-sha1="cjBZ9qLBbDaN9RyJJaHHADiOoN7" width="267" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5651a526adfafaf740ccfa62d489601d2cade775_2_267x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5651a526adfafaf740ccfa62d489601d2cade775_2_400x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5651a526adfafaf740ccfa62d489601d2cade775_2_534x1000.png 2x" data-dominant-color="E4E3E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-06-14 19-20-02_2</span><span class="informations">697×1304 204 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<p>Logic for the first button:</p>
<pre><code class="lang-auto">def prepareSendEmailOnWebBrowser(self, emailVariable, subjectVariable, bodyVariable, ccVariable="", bccVariable=""):
  parsedBodyVariable = bodyVariable.replace(" ", "%20").replace("\n", "%0D%0A")
  parsedBodyVariable = "asdasfasfsafsaf"
  #
  prepareEmailString = (
    f'mailto:{emailVariable}?'
    f'subject={subjectVariable}&amp;'
    f'body={parsedBodyVariable}'
  )
  #
  if ccVariable != "":
    prepareEmailString += f'&amp;cc={ccVariable}'
  #
  if bccVariable != "":
    prepareEmailString += f'&amp;bcc={bccVariable}'
  #
  prepareEmailUrl = qt.QUrl(prepareEmailString)
  #
  # Open email client
  qt.QDesktopServices.openUrl(prepareEmailUrl)
</code></pre>
<p>This is how it looks like on Ubuntu:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06d79573b97fd5c1a37820c686f19c4b0c45d41e.png" data-download-href="/uploads/short-url/YwKyL12ROAqdpzWajDkSYYdt5s.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06d79573b97fd5c1a37820c686f19c4b0c45d41e_2_617x500.png" alt="image" data-base62-sha1="YwKyL12ROAqdpzWajDkSYYdt5s" width="617" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06d79573b97fd5c1a37820c686f19c4b0c45d41e_2_617x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06d79573b97fd5c1a37820c686f19c4b0c45d41e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06d79573b97fd5c1a37820c686f19c4b0c45d41e.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">809×655 33.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But <em><strong>Body</strong></em> variable does not work, could offer help on making it work or feedback on making this feature better (I would think other developer would like to have this on their extensions)</p>
<p>PS: not only email but <a href="https://meta.discourse.org/t/create-a-link-to-start-a-new-topic-with-pre-filled-information/28074" rel="noopener nofollow ugc">discourse use should also be considered</a> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2024-06-15 05:32 UTC)

<p>You probably don’t want to discuss issues in private emails, so you would either want to create a <a href="https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue#creating-an-issue-from-a-url-query">github issue</a> or a <a href="https://meta.discourse.org/t/create-a-link-to-start-a-new-topic-with-pre-filled-information/28074">discourse post</a> by opening a URL.</p>
<p>This is already implemented in the error report dialog:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3afde9cef4ae6124b1572e943c45ba0e1e053210.png" data-download-href="/uploads/short-url/8pRHp09r488kdZO1OiehzDY1afK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3afde9cef4ae6124b1572e943c45ba0e1e053210_2_460x499.png" alt="image" data-base62-sha1="8pRHp09r488kdZO1OiehzDY1afK" width="460" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3afde9cef4ae6124b1572e943c45ba0e1e053210_2_460x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3afde9cef4ae6124b1572e943c45ba0e1e053210_2_690x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3afde9cef4ae6124b1572e943c45ba0e1e053210_2_920x998.png 2x" data-dominant-color="3E4246"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1218×1322 95.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But it may be useful to add module-specific links for some modules or make these links more visible (because probably you haven’t noticed them).</p>

---

## Post #3 by @mau_igna_06 (2024-06-15 14:40 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="36793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>so you would either want to create a <a href="https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue#creating-an-issue-from-a-url-query" rel="noopener nofollow ugc">github issue</a> or a <a href="https://meta.discourse.org/t/create-a-link-to-start-a-new-topic-with-pre-filled-information/28074" rel="noopener nofollow ugc">discourse post</a> by opening a URL.</p>
</blockquote>
</aside>
<p>I may do that using <em>bone.reconstruction.planner(at)<a href="http://gmail.com" rel="noopener nofollow ugc">gmail.com</a></em> as a github bot or a discourse bot by forwarding received emails (I would prefer eliminating the friction that having to sign up causes).</p>
<p>Do you think this is possible?</p>
<p>cc: <a class="mention" href="/u/jcfr">@jcfr</a></p>

---

## Post #4 by @lassoan (2024-06-16 17:34 UTC)

<p>I agree that it could be useful to have a link in the module “Help &amp; Acknowledgment” section that lets users directly send bug report to the module developers. No scripting is needed for this, but instead you can add links in the module help text (as it is already done by default for the module documentation). This requires zero coding and maintenance and also a more compact and elegant way than adding a large button box.</p>
<p>You can use <code>mailto:</code> as URL protocol in the link to initiate sending an email instead of opening a forum or github page, but I don’t think we should encourage people to disclose their email address or communicate via disposable email addresses.</p>

---

## Post #5 by @mau_igna_06 (2024-06-16 18:44 UTC)

<p>Thanks for the feedback</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="36793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I agree that it could be useful to have a link in the module “Help &amp; Acknowledgment” section that lets users directly send bug report to the module developers.</p>
</blockquote>
</aside>
<p>But what’s not good about this solution, IMHO, is that users would find this section very hard to discover (I don’t think users are curious enough to find the links) so it would not solve the problem.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="36793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>No scripting is needed for this, but instead you can add links in the module help text (as it is already done by default for the module documentation). This requires zero coding and maintenance and also a more compact and elegant way than adding a large button box.</p>
</blockquote>
</aside>
<p>Agreed this would be easier for developers in general, but we should be the ones doing the effort to ease users communication. In a worst case scenario, user needs to report some part of the workflow always crashes Slicer and does not do it because of high friction to do the report: sign up to Github or sign up to Discourse</p>

---

## Post #6 by @lassoan (2024-06-17 00:29 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="5" data-topic="36793">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>user needs to report some part of the workflow always crashes Slicer and does not do it because of high friction to do the report: sign up to Github or sign up to Discourse</p>
</blockquote>
</aside>
<p>Some people may prefer disclosing their email address, some may prefer a click in the browser to authenticate. We may offer both and then see if one is much more popular than the other. Even anonymous submission could be implemented. However, overall I would not expect this to make a big difference in the number of people reporting problems.</p>
<p>Probably it would be more impactful if we added a crash reporting dialog, which would collect system information and application log (and maybe other data) and let the user submit by a single click.</p>

---
