---
topic_id: 475
title: "Who Uses Dicom Data Bundle"
date: 2017-06-10
url: https://discourse.slicer.org/t/475
---

# Who uses DICOM data bundle?

**Topic ID**: 475
**Date**: 2017-06-10
**URL**: https://discourse.slicer.org/t/who-uses-dicom-data-bundle/475

---

## Post #1 by @lassoan (2017-06-10 19:42 UTC)

<p>Slicer can save the scene in a DICOM file that can be stored on a PACS or other DICOM archives. Review workstations (other than Slicer) cannot interpret the contents (other than showing a short description and a screenshot) but they may be able to download it and save it to file that Slicer can open.</p>
<p>As Slicer’s standard DICOM export capabilities are improved, this special Slicer-specific export capability may be removed in the future. To help us make an informed decision, please answer the poll below (even if you haven’t heard about this feature and don’t plan to use it).</p>
<div class="poll" data-poll-status="open" data-poll-type="regular" data-poll-name="poll">
<div>
<div class="poll-container">
<ul>
<li data-poll-option-id="864e96ef5cec639738e58599ef0ea24e">I haven’t heard about this feature and I don’t think I would use it</li>
<li data-poll-option-id="57c62cedcb4c9463014bf06cb523c37b">I haven’t heard about this feature but I think I will use it</li>
<li data-poll-option-id="515f2aac36003e9a36b7a2f257a136e6">I know about this feature but never use it</li>
<li data-poll-option-id="728cdb09a27e1679b1f0baa1f9e78123">I use it sometimes</li>
<li data-poll-option-id="871f7a85faf39ab137bf985727be0640">I use it regularly, this feature is important</li>
</ul>
</div>
<div class="poll-info">
<p>
<span class="info-number">0</span>
<span class="info-text">voters</span>
</p>
</div>
</div>
<div class="poll-buttons">
<a title="Display the poll results">Show results</a>
</div>
</div>

---

## Post #2 by @pieper (2017-06-10 20:04 UTC)

<p>I added this feature a while back but have never found any real use for it.  I would be fine to see it removed.</p>

---

## Post #3 by @lassoan (2017-06-10 20:19 UTC)

<p>Thanks for the information. The topic has come up while discussing this bug report: <a href="https://issues.slicer.org/view.php?id=2254">https://issues.slicer.org/view.php?id=2254</a></p>

---

## Post #4 by @fedorov (2017-06-11 02:46 UTC)

<p>In my opinion, Slicer standard DICOM export will not replace Slicer-specific export capabilities any time soon. The standard does not cover all of the types of data Slicer needs to store, and implementation of even all those that it covers will take a very big effort.</p>

---

## Post #5 by @lassoan (2017-06-11 11:31 UTC)

<p>The feature is potentially useful. I’ve asked the question because if we really want to make it easy to find and use then we need to invest time in it (not just now but later, continuously with maintenance, testing, support). If nobody uses the feature then we could spend the same time with improving or developing other things, such as standard DICOM export.</p>

---

## Post #6 by @pieper (2017-06-11 17:50 UTC)

<p>The original motivation for the data bundle was to allow people to use dicom storage tools to manage scene data.  So far I haven’t seen anyone doing that.</p>
<p>I agree with <a class="mention" href="/u/fedorov">@fedorov</a> that there’s a lot of Slicer data that doesn’t have a perfect match to standard DICOM objects, so we will always need some level of application-specific data format, but the point is that I don’t think it’s proven useful to opaquely store that inside a DICOM object as opposed to MRBs and other representations.</p>

---

## Post #7 by @fedorov (2017-06-11 18:23 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I agree, I am not advocating to keep it or fix it. Just saying that DICOM will not meet all of the needs.</p>
<p>My approach is to stay as close as possible to what DICOM supports, and use custom non-mrml-scene things where it is lacking the capabilities. I had a lot of very bad experience with scenes and don’t want to rely on them at all anywhere.</p>

---

## Post #8 by @lassoan (2017-06-11 19:26 UTC)

<p>Your bad experience with scene saving always surprises me. I use Slicer a lot for many projects (with tens of students, working full time) and we don’t have any issue with saving the application state into scene file and restoring everything. Could you please file a bug report for any issue that you know about or send list of related bug reports?</p>

---

## Post #9 by @fedorov (2017-06-12 04:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="475">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Your bad experience with scene saving always surprises me.</p>
</blockquote>
</aside>
<p>If you looked over all the issues I submitted related to scene/mrml, perhaps you would not be so surprised. Especially considering that some of those issues remained open for 5 years. And I had a lot for Slicer 3, which were never addressed. I was very active submitting bugs related to this topic many many years ago, but not anymore, since I realized they were never prioritized. It may work now, I don’t know. I just lost the faith in this feature, and I don’t want to revisit it.</p>

---

## Post #10 by @lassoan (2017-06-12 05:16 UTC)

<p>I’ve checked all errors you reported and still open (58 in total) and there are only 2-3 related to scene saving/loading, all are quite special cases. So, it seems scene saving/loading issues have been mostly solved after all. It’s OK not to use scene saving/loading, but it may be important for you and others to know that these features work reliably.</p>
<p>I’ve also stopped submitting bug reports to the bug tracker due to the long list of unresolved issues, but now I’m in the process of cleaning this up so that we can start using the bug tracker again for tracking and prioritizing issues.</p>

---

## Post #11 by @eeros (2017-06-12 11:09 UTC)

<p>I didn’t know about the existence of this feature. If it allows storing the entire scene easily to a PACS server, it sounds a very useful feature and I will likely start using it. I think that standard DICOM export can not replace it in a near future.</p>

---

## Post #12 by @pieper (2017-06-12 20:53 UTC)

<p>For context, here are the pros and cons of the approach as I see it:</p>
<p>Pros:</p>
<ul>
<li>it’s basically just a .mrb package binary blob added in a private tag of a dicom secondary capture, where a screen grab of the slicer display is the image portion of the capture image.</li>
<li>secondary captures are widely supported on PACS and on viewer software so people can transfer the data and see the screen capture on standard hardware.</li>
<li>the data transfer is ‘lossless’ from a slicer perspective since it preserves the normal scene state (assuming scenes work well for your use case).</li>
<li>putting binary blobs in private tags is pretty common in commercial systems.</li>
<li>the mrb binary data is just a renamed zip file that stores the mrml file and corresponding data in standard research formats (nrrd, vtk, csv, etc) so if someone really wanted to extract the data for another purpose it wouldn’t be too hard.</li>
</ul>
<p>Cons:</p>
<ul>
<li>the contents of our private tag is definitely non-standard</li>
<li>a scene file contains copies of all the image data (stored as nrrd in the .mrb) so it’s not efficient</li>
<li>a large binary blob in a secondary capture object is kind of an abuse of the standard and would likely cause performance issues on some viewers that expect an SC to be a lightweight object.</li>
<li>in general we try to avoid pushing Slicer results into clinical PACS systems.  Some careful testing would be a good idea.</li>
</ul>

---
