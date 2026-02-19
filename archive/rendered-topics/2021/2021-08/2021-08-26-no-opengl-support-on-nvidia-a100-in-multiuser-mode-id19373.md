---
topic_id: 19373
title: "No Opengl Support On Nvidia A100 In Multiuser Mode"
date: 2021-08-26
url: https://discourse.slicer.org/t/19373
---

# No openGL support on Nvidia A100 in multiuser mode

**Topic ID**: 19373
**Date**: 2021-08-26
**URL**: https://discourse.slicer.org/t/no-opengl-support-on-nvidia-a100-in-multiuser-mode/19373

---

## Post #1 by @muratmaga (2021-08-26 16:00 UTC)

<p>We have been using Slicer as an interactive cloud application on VM hosted at JetStream using Tesla V100s. Now JetStream is transitioning into JetStream2 with A100s, an interesting limitation of the platform came up. According to the Nvidia’s documentation, A100 does not support openGL or Vulkan when it is configured in the Multi-user mode (MIG), which was the default for Jetstream (they slice the GPU in the partitions across users).</p>
<p>I know this is probably a niche thing, but there has been some interest in deploying Slicer in the cloud, so I thought I would pass it on. If you are using the GPU in passthrough and has full access, I don’t think this is not an issue:</p>
<p><a href="https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#app-considerations" class="onebox" target="_blank" rel="noopener nofollow ugc">https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#app-considerations</a></p>

---

## Post #2 by @pieper (2021-08-26 19:34 UTC)

<p>Interesting, I guess they aren’t "G"PUs anymore in that configuration.  I hope this isn’t a trend for nvidia to prioritize computing over graphics.</p>
<p>I’ve used A100s on a google VM before with no problem, but not in this partitioned mode.</p>

---

## Post #3 by @muratmaga (2021-08-26 19:43 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="19373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I hope this isn’t a trend for nvidia to prioritize computing over graphics.</p>
</blockquote>
</aside>
<p>That’s what worried me, and I think it is a real trend.</p>

---
