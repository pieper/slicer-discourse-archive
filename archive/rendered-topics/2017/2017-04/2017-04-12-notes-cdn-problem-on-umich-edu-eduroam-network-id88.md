# [notes] CDN problem on umich.edu eduroam network

**Topic ID**: 88
**Date**: 2017-04-12
**URL**: https://discourse.slicer.org/t/notes-cdn-problem-on-umich-edu-eduroam-network/88

---

## Post #1 by @ihnorton (2017-04-12 21:05 UTC)

<p>Some users at University of Michigan cannot access the Discourse CDN for some site resources. Here’s a debugging conversation (I followed up by email up from <a href="https://discourse.slicer.org/t/problems-to-connect-to-the-discourse-forum-from-uofm/85/4">this topic</a>).</p>
<p>They can’t connect to these other Discourse sites either:</p>
<blockquote>
<p><a href="https://talk.jekyllrb.com/">https://talk.jekyllrb.com/</a></p>
</blockquote>
<p>They see a browser error loading resource, and can’t ping the CDN. Does this ring any bells?</p>
<hr>
<p>(user):</p>
<blockquote>
<p>On my side, I tried with Safari and Chrome and I have the same result. I can open <a href="http://discourse.org">discourse.org</a> and the other hosts I tried.</p>
</blockquote>
<blockquote>
<p>What happens is the web page loads first the text in a browser tab:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/3524fa7d7ead9e1ed58d19d6d945008e917dd961.jpg" width="552" height="94"><br>
Then the page stays blank and after few minutes it sends a timeout error in the chrome console:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/160c8eb409902c3a24de47572b58373772da390b.png" data-download-href="/uploads/short-url/393pko1KOCNs5zwmeOkUG7KMETp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/160c8eb409902c3a24de47572b58373772da390b_2_690x216.png" alt="image" data-base62-sha1="393pko1KOCNs5zwmeOkUG7KMETp" width="690" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/160c8eb409902c3a24de47572b58373772da390b_2_690x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/160c8eb409902c3a24de47572b58373772da390b_2_1035x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/160c8eb409902c3a24de47572b58373772da390b.png 2x" data-dominant-color="F1DBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1124×353 186 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<hr>
<p>(me):</p>
<blockquote>
<p>Ok, that helps to narrow it down a little bit. Can you ping <a href="http://discourse-cdn-sjc1.com/standard2">discourse-cdn-sjc1.com/standard2</a>? Is there any ad-blocker installed on these computers? There’s a bug report that sounds kind of similar, where some software was blocking the Discourse CDN due to false positive:</p>
</blockquote>
<blockquote>
<p><a href="https://meta.discourse.org/t/discourse-cdns-are-blocked-by-privacy-badger/17127/17" class="inline-onebox">Discourse CDNs are blocked by privacy badger - #17 by vi0oss - site feedback - Discourse Meta</a></p>
</blockquote>
<blockquote>
<p>Might be happening on your network if they use a similar heuristic or list.</p>
</blockquote>
<hr>
<p>(user):</p>
<blockquote>
<p>That ping is not working.</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea9eb204e7e6963ee6fc0e868a575e2784ed77ab.png" data-download-href="/uploads/short-url/xtxJlrnPZ2QRFxgS6qUYiNronRF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea9eb204e7e6963ee6fc0e868a575e2784ed77ab_2_690x106.png" alt="image" data-base62-sha1="xtxJlrnPZ2QRFxgS6qUYiNronRF" width="690" height="106" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea9eb204e7e6963ee6fc0e868a575e2784ed77ab_2_690x106.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea9eb204e7e6963ee6fc0e868a575e2784ed77ab_2_1035x159.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea9eb204e7e6963ee6fc0e868a575e2784ed77ab.png 2x" data-dominant-color="111111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1118×172 59.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>There is an ad-blocker in my Chrome but not in Safari, and I tried to disable the ad-blocker and the issue is still the same.</p>
</blockquote>
<blockquote>
<p>Then, why can I access the website with my smartphone on the same network, would it be linked to the browser?</p>
</blockquote>
<hr>
<p>(me):</p>
<blockquote>
<p>Since you can’t ping the CDN at all, it’s probably not the browser. That seems like it might be a block at the institution level (since you said multiple computers), or at least local firewall.</p>
</blockquote>
<blockquote>
<p>I think the ones I originally linked are mostly business hosting, so they might be hitting a different CDN. Can you try these, they’re on the same plan as Slicer and hits a similar CDN for me:</p>
</blockquote>
<p><code>https://talk.jekyllrb.com/</code><br>
<code>https://discourse.ros.org</code></p>
<blockquote>
<blockquote>
<p>Then, why can I access the website with my smartphone on the same network, would it be linked to the browser?</p>
</blockquote>
</blockquote>
<blockquote>
<p>Assuming you are connected to wi-fi, but also have cell service, maybe it falls back to unblocked cell network if a request fails – I’m not sure what the request resolution rules are on various phones.</p>
</blockquote>
<hr>
<p>(user):</p>
<blockquote>
<p>When we tried on laptops, we used eduroam, so not really specific. But, on the computers plugged on the department wifi it’s working fine.</p>
</blockquote>
<hr>
<p>(me):</p>
<blockquote>
<p>Ok I missed that the first time: so just to clarify</p>
</blockquote>
<blockquote>
<ul>
<li>the problem is only on the wifi network called eduroam?</li>
</ul>
</blockquote>
<blockquote>
<ul>
<li>the regular university wifi works ok? – I guess that would be MWireless and MGuest (from here: <a href="http://its.umich.edu/enterprise/wifi-networks/wifi" class="inline-onebox">WiFi / U-M Information and Technology Services</a>)</li>
</ul>
</blockquote>
<blockquote>
<p>I think you need to contact the university IT in this case – looks like “4HELP@umich.edu” (from the site above). I don’t think there is much Discourse can do if the CDN is blocked on that specific wireless network. From what I can tell, eduroam is just an authentication provider, so university IT controls the configuration.</p>
</blockquote>
<blockquote>
<p>It looks like someone else saw weird issues with eduroam too, but no follow-up on any resolution:</p>
</blockquote>
<blockquote>
<p><a href="https://meta.discourse.org/t/mobile-clicking-create-new-account-causes-processing-spinner-icon-to-keep-spinning/55508/15">https://meta.discourse.org/t/mobile-clicking-create-new-account-causes-processing-spinner-icon-to-keep-spinning/55508/15</a></p>
</blockquote>

---

## Post #2 by @ihnorton (2017-04-12 21:16 UTC)

<p>(user):</p>
<blockquote>
<p>I tried with MWireless and eduroam =&gt; not working but with MGuest =&gt; working. So, the solution is to contact IT or to switch to a non-blocking network to access the discourse.</p>
</blockquote>
<p>So, they are going to follow-up with university IT, because there is nothing we or Discourse can do about local network settings.</p>

---
