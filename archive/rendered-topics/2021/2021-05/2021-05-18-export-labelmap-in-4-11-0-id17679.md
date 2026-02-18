# Export Labelmap in 4.11.0

**Topic ID**: 17679
**Date**: 2021-05-18
**URL**: https://discourse.slicer.org/t/export-labelmap-in-4-11-0/17679

---

## Post #1 by @Cassandra_Donatelli (2021-05-18 17:53 UTC)

<p>Hello,</p>
<p>I am trying to export a segmentation as a lablemap and have not been successful since updating to 4.11.0. I keep getting the error “Failed to export segments from segmentation XYZ to lablemap node XYZ-label! Most probably the segment cannot be converted into binary labelmap representation.”</p>
<p>The reason I’m trying to export the lablemap is because I need the binary slices for another analysis out side of slicer. I’m using code in imageJ and Matlab to calculate the second moment of area and fractal dimension of the slices and I use the binary (0 = not thing, 1 = thing) slices to do this.</p>
<p>I’m following the same protocol I’ve used in past versions of slicer, but I’ve never seen this error before. Is there another option I should be using that I missed in the update? Is anyone else getting this error in slicer 4.11.0?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2021-05-18 18:27 UTC)

<p>First off, you may not need to export your segmentations to do those calculations. Have you checked Segment Statistics Module which provides some of those <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" class="inline-onebox">Segment statistics — 3D Slicer documentation</a></p>
<p>And perhaps other metrics you need can be added (or already available) in elsewhere. My first suggestion would be to explore those before you try to use yet another program. Also I think <a class="mention" href="/u/jmhuie">@jmhuie</a>  might have already one this as a module. See this post. <a href="https://discourse.slicer.org/t/calculating-second-moment-of-area-from-segment/16459/4" class="inline-onebox">Calculating Second Moment of Area from Segment - #4 by jmhuie</a></p>
<p>As for your error, it is not clear to me what’s going on without seeing your data. We routinely export labelmaps from segmentations, and haven’t encountered this error with any of the 4.11 or 4.13 versions of Slicer. if you can upload the segmentation and the volume that give you the error we can try to troubleshoot.</p>

---

## Post #3 by @lassoan (2021-05-19 03:51 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="17679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>you may not need to export your segmentations to do those calculations. Have you checked Segment Statistics Module which provides some of those <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment statistics — 3D Slicer documentation</a></p>
</blockquote>
</aside>
<p>Yes, in addition to Segment statistics module, you can use Radiomics extension to compute fractal dimenision and dozens of other metrics. So, there should be no need to struggle with Matlab or ImageJ.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="17679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>We routinely export labelmaps from segmentations</p>
</blockquote>
</aside>
<p>Yes, this should work without problems. See examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">script repository</a>.</p>

---

## Post #4 by @Cassandra_Donatelli (2021-06-04 17:47 UTC)

<p>Hello,</p>
<p>I’ve tried now to export several different labelmaps with the same error, and unfortunately there is no way to upload segmentations in this chat forum. Is there another place I could upload the data?</p>
<p>Again, I’ve done this many many times before, and am only now encountering an error with this new update.</p>
<ul>
<li>Cassandra</li>
</ul>

---

## Post #5 by @Cassandra_Donatelli (2021-06-04 17:48 UTC)

<p>Hello,</p>
<p>Thank you for the tip regarding the Radiomics extension. Unfortunately, it doesn’t appear when I open “extension manager.” Is this extension not updated yet for 4.11.0?</p>
<p>Thanks!</p>

---

## Post #6 by @lassoan (2021-06-04 20:32 UTC)

<aside class="quote no-group" data-username="Cassandra_Donatelli" data-post="4" data-topic="17679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cassandra_donatelli/48/10975_2.png" class="avatar"> Cassandra_Donatelli:</div>
<blockquote>
<p>there is no way to upload segmentations in this chat forum. Is there another place I could upload the data?</p>
</blockquote>
</aside>
<p>You can upload the data set anywhere (Dropbox, OneDrive,…) and post the link here.</p>
<aside class="quote no-group" data-username="Cassandra_Donatelli" data-post="5" data-topic="17679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cassandra_donatelli/48/10975_2.png" class="avatar"> Cassandra_Donatelli:</div>
<blockquote>
<p>Radiomics extension. Unfortunately, it doesn’t appear when I open “extension manager.” Is this extension not updated yet for 4.11.0?</p>
</blockquote>
</aside>
<p>It should be available. What Slicer version and operating system do you use? Do you see any errors in the application log?</p>

---

## Post #7 by @jmhuie (2021-06-05 17:52 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="17679">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>And perhaps other metrics you need can be added (or already available) in elsewhere. My first suggestion would be to explore those before you try to use yet another program. Also I think <a class="mention" href="/u/jmhuie">@jmhuie</a> might have already one this as a module. See this post. <a href="https://discourse.slicer.org/t/calculating-second-moment-of-area-from-segment/16459/4">Calculating Second Moment of Area from Segment - #4 by jmhuie</a></p>
</blockquote>
</aside>
<p>Hey Cassandra, Murat is correct. For my module you will be able to measure second moment of area for the segment without need to exporting to a labelmap.</p>

---
