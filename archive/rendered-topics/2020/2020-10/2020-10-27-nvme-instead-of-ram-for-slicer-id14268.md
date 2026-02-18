# NVMe instead of RAM for Slicer?

**Topic ID**: 14268
**Date**: 2020-10-27
**URL**: https://discourse.slicer.org/t/nvme-instead-of-ram-for-slicer/14268

---

## Post #1 by @NoobForSlicer (2020-10-27 13:41 UTC)

<p>I was performing some tasks and as usual the PC has too little RAM.</p>
<p>Now I know I can create virtual memory on my HDD.</p>
<p>But what about this? A friend is offering me a 1 TB NVMe 7000 mb/s for just 100 euros.</p>
<p>Would that be fast enough to be compared to Ram when used with Slicer?</p>
<p>Or would it be just like any other SSD.</p>
<p>The reason why I ask this is because from what I assume, it is not just bandwidth but latency that matters as well AND durability.</p>
<p>so here are the questions:</p>
<ol>
<li>How much faster can I expect it to be than my HDD currently?</li>
<li>How much slower is it than if I had all full real physical RAM memory?</li>
<li>does bandwidth matter? how much would it impact the work of slicer?</li>
<li>does latency matter? how much would latency of NVMe impact the work of slicer?</li>
<li>Would a NVMe be able to handle that type of writing and erasing data constantly as ram does?</li>
</ol>
<p>Thanks &lt;3 Hope I get some answers</p>

---

## Post #2 by @NoobForSlicer (2020-10-27 14:00 UTC)

<p>I am not sure why latency would matter here… We are basically dealing with a huge chunk of data in a volume which is not separated nor called for separately?! right?</p>
<p>once the user wants to browse and go up or down, he can just scroll and it’s not like many files have to be called for within 1 second or something…</p>
<p>it’s just 1 huge chunk of data.</p>
<p>Am I getting something wrong here?</p>

---

## Post #3 by @muratmaga (2020-10-27 15:21 UTC)

<p>Short answer is, while it will speed up the paging operations associated virtual memory compared to regular SSD, it still not be very fast. Those advertised speeds never materialize in real environments, and it is not a single chunk you are trying to read/write (it would if you had the memory).</p>
<p>If you are regularly working with large datasets and want to use Slicer, increasing physical memory is probably the better investment.  If you are only trying to get by, then it is ok, as it will speed up your regular IO as well.</p>

---

## Post #4 by @NoobForSlicer (2020-10-27 15:32 UTC)

<p>If you are only trying to get by, then it is ok,</p>
<p>Sadly I am a type of student who gets by even when buying his suit for his wedding <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=9" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #5 by @Alex_Vergara (2020-10-27 16:19 UTC)

<p>My 2c here<br>
You can free up some gigas from ram by using a graphic card. I would assume you don’t have one.</p>

---
