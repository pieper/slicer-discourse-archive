---
topic_id: 42209
title: "Suggestion For Adding Ai Functions With Discourse Ai"
date: 2025-03-18
url: https://discourse.slicer.org/t/42209
---

# Suggestion for adding ai functions with discourse ai

**Topic ID**: 42209
**Date**: 2025-03-18
**URL**: https://discourse.slicer.org/t/suggestion-for-adding-ai-functions-with-discourse-ai/42209

---

## Post #1 by @motive2791 (2025-03-18 19:01 UTC)

<p>discourse plugin supports ai now with many functions, like ai search, summary, related</p>
<p>may be our forum can add these function</p>
<aside class="onebox discoursetopic" data-onebox-src="https://meta.discourse.org/t/discourse-ai/259214">
  <header class="source">
      <img src="https://d11a6trkgmumsb.cloudfront.net/optimized/3X/b/3/b33be9538df3547fcf9d1a51a4637d77392ac6f9_2_32x32.png" class="site-icon" width="32" height="32">

      <a href="https://meta.discourse.org/t/discourse-ai/259214" target="_blank" rel="noopener nofollow ugc" title="03:54PM - 07 March 2025">Discourse Meta – 7 Mar 25</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/402;"><img src="https://d11a6trkgmumsb.cloudfront.net/optimized/4X/6/6/2/6625cade54deb235ee8c900c766ebbb121a3bb91_2_1024x597.avif" class="thumbnail" width="690" height="402"></div>

<div class="title-wrapper">
  <h3><a href="https://meta.discourse.org/t/discourse-ai/259214" target="_blank" rel="noopener nofollow ugc">Discourse AI</a></h3>
  <div class="topic-category">
      <span class="badge-wrapper bullet">
        <span class="badge-category-bg" style="background-color: #F7941D;"></span>
        <span class="badge-category clear-badge">
          <span class="category-name">Plugin</span>
        </span>
      </span>
    <div class="topic-header-extra">
      <div class="list-tags">
        <div class="discourse-tags">
          <svg class="fa d-icon d-icon-tag svg-icon svg-string"><use href="#tag"></use></svg>
            <span class="discourse-tag simple">official</span>
            <span class="discourse-tag simple">ai</span>
        </div>
      </div>
    </div>
  </div>
</div>

  <p>:discourse2: Summary Integration between AI features and Discourse   🌐 Website Discourse AI Features | Discourse - Civilized Discussion   🛠 Repository Link GitHub - discourse/discourse-ai   📖 Install Guide How to install plugins in Discourse      ...</p>

  <p>
    <span class="label1">Reading time: 7 mins 🕑</span>
      <span class="label2">Likes: 218 ❤</span>
  </p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @pieper (2025-03-18 19:54 UTC)

<p>Agreed, it would be great to make this available.  Unfortunately it’s not free.</p>

---

## Post #3 by @muratmaga (2025-03-18 20:09 UTC)

<p>Is there still cost to pay for self-hosted ones like Slicer forum? Or are you talking about API token cost? If the latter, JetStream2 might be of use: <a href="https://docs.jetstream-cloud.org/inference-service/overview/#which-models-do-you-offer" class="inline-onebox" rel="noopener nofollow ugc">Overview - Jetstream2 Documentation</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f139ef67d3dc30c25dc60872f35ecfe163d6d481.png" data-download-href="/uploads/short-url/ypZc98l9mhKk0xVvKf4cDp35GOl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f139ef67d3dc30c25dc60872f35ecfe163d6d481.png" alt="image" data-base62-sha1="ypZc98l9mhKk0xVvKf4cDp35GOl" width="690" height="394" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">865×495 30.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Discourse AI seems to interface all of those three models JS2 offer: <a href="https://meta.discourse.org/t/discourse-ai-large-language-model-llm-settings-page/319903" class="inline-onebox" rel="noopener nofollow ugc">Discourse AI - Large Language Model (LLM) settings page - Site Management - Discourse Meta</a></p>

---

## Post #4 by @lassoan (2025-03-19 04:29 UTC)

<p>Yes, API tokens cost money. There are about 6000 page views per day. Very rough estimate: assuming $0.03 per interaction and average one interaction per page view would cost $5400/month. There are about 1800 signed-in user visits per month, so if we charged users a few dollars per month for AI usage that would cover the costs.</p>
<p>Discourse indeed supports vLLM, so it may be possible to use Jetstream2 for free AI features. To try, we would need Model id, URL, API key:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9c4d0f083c41f0b6e1c6f209e170726d2d61395.png" data-download-href="/uploads/short-url/qvo0xzbTwBdRwpnOTJs6jhnXSXX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c4d0f083c41f0b6e1c6f209e170726d2d61395_2_273x500.png" alt="image" data-base62-sha1="qvo0xzbTwBdRwpnOTJs6jhnXSXX" width="273" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c4d0f083c41f0b6e1c6f209e170726d2d61395_2_273x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c4d0f083c41f0b6e1c6f209e170726d2d61395_2_409x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9c4d0f083c41f0b6e1c6f209e170726d2d61395_2_546x1000.png 2x" data-dominant-color="282929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">949×1734 73.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2025-03-19 04:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="42209">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Discourse indeed supports vLLM, so it may be possible to use Jetstream2 for free AI features. To try, we would need Model id, URL, API key:</p>
</blockquote>
</aside>
<p>I don’t really know much about LLMs and their API. This is what I found on their website. Hope it helps: <a href="https://docs.jetstream-cloud.org/inference-service/api/#api-endpoints" class="inline-onebox" rel="noopener nofollow ugc">Access the APIs - Jetstream2 Documentation</a></p>
<p>They are a very supportive group and have weekly office hours on ever Tuesday 2p (ET). They might be able to help you.</p>

---

## Post #6 by @pieper (2025-03-19 20:26 UTC)

<p>It’s a great idea to use the JS2 servers.  Unfortunately I couldn’t get them to work with discourse but they do work well and you can get a lot of detailed info about Slicer from either the Llama or DeepSeek models they expose through Open WebUI.</p>

---
