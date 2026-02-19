---
topic_id: 9797
title: "Bilateral Filter Not Working"
date: 2020-01-13
url: https://discourse.slicer.org/t/9797
---

# Bilateral Filter not working

**Topic ID**: 9797
**Date**: 2020-01-13
**URL**: https://discourse.slicer.org/t/bilateral-filter-not-working/9797

---

## Post #1 by @juday (2020-01-13 21:45 UTC)

<p>Slicer Ver 4.11 2019-12-16 on Windows</p>
<p>I’m unable to run Bilateral image filter in Simple filters. The progress bar does not move.</p>

---

## Post #2 by @pieper (2020-01-13 21:57 UTC)

<p>It’s a pretty slow filter, so you might give it time.</p>
<p>Or maybe there’s an error - did you check the error log?</p>

---

## Post #3 by @juday (2020-01-13 22:02 UTC)

<p>There was no error message. I waited about 5-10 min and there was no progress. I’ll try to be patient. Thanks for your swift response.</p>

---

## Post #4 by @lassoan (2020-01-13 22:06 UTC)

<p>Try on a small sample data set first, such as MRHead. Also try with latest stable and latest preview releases and let us know what you find.</p>

---

## Post #5 by @juday (2020-01-16 03:56 UTC)

<p>I tried on the stable release (4.10.2) using sample MRHead data. The filter successfully ran and completed in 10 min 27s. But the preview release (4.11.0 2020-01-08) seems stuck at 0% even after 5 min for the sample MRHead data.</p>

---

## Post #6 by @lassoan (2020-01-16 04:10 UTC)

<p>Could you try a preview release from a few weeks ago (before ITK version update). You can specify “offset” parameter to get access to earlier releases, for example: <a href="https://download.slicer.org/?offset=-20">https://download.slicer.org/?offset=-20</a></p>

---

## Post #7 by @lassoan (2020-01-16 20:49 UTC)

<p>I’ve tried with latest preview (ITK v5.1rc01) and latest stable (ITK v4.13.1) and found that the new version was a little bit faster (completed in 272s instead of 283s) but progress was not reported (stuck at 0% the whole time).</p>
<p>Progress reporting is mostly broken for other filters, too. Filters that complete quickly (e.g., MedianImageFilter with 3x3x3 kernel) the progress is stuck for 1-2 seconds at 0% and after that sometimes you see a quick filling up of the progress bar within a second. For filters that take longer time (e.g., MedianImageFilter with 5x5x5 kernel) we don’t see any progress (it is stuck at 0%) and then the operation is completed. Median computation is much faster with ITK5 though (with 5x5x5 kernel it takes 5s instead of 30s).</p>
<p><a class="mention" href="/u/blowekamp">@blowekamp</a> <a class="mention" href="/u/thewtex">@thewtex</a> Is progress reporting known to be changed/broken in ITK or SimpleITK? Or maybe this only happens in Slicer? Maybe it’s due to the new threading infrastructure?</p>
<p>It is interesting that for interactive use cases correct progress reporting seems to be more important than small speed improvements (users perception is that the filter is faster if they can see that the operation is making progress).</p>

---

## Post #8 by @blowekamp (2020-01-16 21:04 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Yes the progress reporting was dramatically changed in ITKv5 as a result of the multi-threading refactoring. The basic filters ( the ones that don’t have a mini-pipeline internally ) only reports progress when the a thread is completely done. That is basically at the completion for many filters which don’t have additional step in their process.</p>

---

## Post #9 by @lassoan (2020-01-16 21:13 UTC)

<aside class="quote no-group" data-username="blowekamp" data-post="8" data-topic="9797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/blowekamp/48/1386_2.png" class="avatar"> blowekamp:</div>
<blockquote>
<p>The basic filters ( the ones that don’t have a mini-pipeline internally ) only reports progress when the a thread is completely done</p>
</blockquote>
</aside>
<p>Wow, this is a significant regression. If the performance improvement is marginal (such as in case of bilateral filter’s 272sec vs 283sec - 5% faster) then probably many people would prefer the old behavior (slightly slower but with consistent progress reporting) for interactive use. I’ve start a discussion on this on the ITK forum (<a href="https://discourse.itk.org/t/no-progress-reporting-in-itk5/2630" class="inline-onebox">No progress reporting in ITK5 - Engineering - ITK</a>).</p>

---

## Post #10 by @dzenanz (2020-01-17 14:11 UTC)

<p>No intermediate progress reporting should occur only for single-threaded case. For multi-threaded case, there should be at least a few progress updates, one for each work unit finishing in the calling thread. Less for default <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/eb8ce3c6195b13878721ffc5475e1f32e183843a/Modules/Core/Common/src/itkPoolMultiThreader.cxx#L96-L103" rel="nofollow noopener">PoolMultiThreader</a>, more for <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/eb8ce3c6195b13878721ffc5475e1f32e183843a/Modules/Core/Common/src/itkTBBMultiThreader.cxx#L33-L41" rel="nofollow noopener">TBBMultiThreader</a>. The code for invoking progress updates is <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/eb8ce3c6195b13878721ffc5475e1f32e183843a/Modules/Core/Common/src/itkMultiThreaderBase.cxx#L477-L627" rel="nofollow noopener">here</a>, most updates should occur from these few lines:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/eb8ce3c6195b13878721ffc5475e1f32e183843a/Modules/Core/Common/src/itkMultiThreaderBase.cxx#L619-L622" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/InsightSoftwareConsortium/ITK/blob/eb8ce3c6195b13878721ffc5475e1f32e183843a/Modules/Core/Common/src/itkMultiThreaderBase.cxx#L619-L622" target="_blank" rel="nofollow noopener">InsightSoftwareConsortium/ITK/blob/eb8ce3c6195b13878721ffc5475e1f32e183843a/Modules/Core/Common/src/itkMultiThreaderBase.cxx#L619-L622</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="619" style="counter-reset: li-counter 618 ;">
<li>if (rnc-&gt;callingThread == std::this_thread::get_id())</li>
<li>{</li>
<li>  rnc-&gt;filter-&gt;UpdateProgress(float(rnc-&gt;pixelProgress) / rnc-&gt;pixelCount);</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Edit: low hanging fruit is to use TBBMultiThreader in Slicer, as Slicer already has it in its super-build. It uses many more work units by default, so progress should be reported more frequently.</p>

---

## Post #11 by @lassoan (2020-01-17 14:50 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="10" data-topic="9797">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>No intermediate progress reporting should occur only for single-threaded case.</p>
</blockquote>
</aside>
<p>For a good user experience, progress reporting is needed for any computation that may take longer than a few seconds, regardless of how it is implemented internally. Let’s discuss this on the <a href="https://discourse.itk.org/t/no-progress-reporting-in-itk5/2630">ITK forum</a>.</p>
<aside class="quote no-group" data-username="dzenanz" data-post="10" data-topic="9797">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>low hanging fruit is to use TBBMultiThreader in Slicer, as Slicer already has it in its super-build</p>
</blockquote>
</aside>
<p>Thank you, I’ll try this now and report back.</p>

---

## Post #12 by @dzenanz (2020-01-17 15:12 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="10" data-topic="9797">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>No intermediate progress reporting should occur only for single-threaded case.</p>
</blockquote>
</aside>
<p>I was stating what should be happening given the current state of library code. Point being that there should be some progress reporting by default.</p>
<p>Of course, progress reporting is desirable regardless of threading.</p>
<p>(I accidentally edited my original post instead of quoting it here).</p>

---

## Post #13 by @lassoan (2020-01-17 15:53 UTC)

<p>I’ve tried ITK with TBB threading and indeed progress reporting is more granular:</p>
<ul>
<li>Bilateral: 17% (after 30sec), 37%, 64%, 80%, 83%, 86%, 89%, 90%, 91%, …</li>
<li>Median: 21%, 34%, 45%, 50%, 61%, 66%, 71%, …</li>
</ul>
<p>TBB seems to have start with large work units (first report arrives at about 20% completion) and gradually reducing their sizes (near the end, progress is reported at about every 0.1%). Unfortunately, granularity at the initial stages is too low.</p>
<p><a class="mention" href="/u/dzenanz">@dzenanz</a> I’m looking forward to your improvements in ITK that you’ve mentioned in the ITK topic. Let us know if there is anything we can test.</p>

---

## Post #14 by @dzenanz (2020-01-17 16:25 UTC)

<p>You should probably make TBB the default in Slicer’s build of ITK, because it has better load balancing for unevenly complex work distribution, and plays better with non-ITK load on the CPU. Our Pool implementation is the default purely due to build convenience (no further dependencies required).</p>

---

## Post #15 by @lassoan (2020-01-18 19:25 UTC)

<p>OK, I’ll <a href="https://github.com/Slicer/Slicer/pull/1305">enable TBB for ITK builds in Slicer</a> after Windows factory machine is restored.</p>
<p>Interestingly, switching to TBB also seems to dramaetically improve performance of some filters. For example, bilateral filtering processing time is decreased from 280s to 150s. It sounds almost too good, but we can do more tests once Slicer is updated.</p>

---
