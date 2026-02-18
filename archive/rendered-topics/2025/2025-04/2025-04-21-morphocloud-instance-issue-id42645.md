# MorphoCloud Instance Issue

**Topic ID**: 42645
**Date**: 2025-04-21
**URL**: https://discourse.slicer.org/t/morphocloud-instance-issue/42645

---

## Post #1 by @Ellie_In (2025-04-21 11:35 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9213180caa26e5df308fea394c90502c9bcf5e87.png" data-download-href="/uploads/short-url/kQeCots2naYhJyoWEHe4gexxtZ5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9213180caa26e5df308fea394c90502c9bcf5e87_2_690x303.png" alt="image" data-base62-sha1="kQeCots2naYhJyoWEHe4gexxtZ5" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9213180caa26e5df308fea394c90502c9bcf5e87_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9213180caa26e5df308fea394c90502c9bcf5e87_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/9213180caa26e5df308fea394c90502c9bcf5e87_2_1380x606.png 2x" data-dominant-color="15191F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1844×810 64.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I was wondering if anyone had any experience with MorphoCloud instances and could help me figure out what is going wrong. When I try to unshelve my instance, I get an error that says “failed to associate floating IP with unshelved instance.” I understand JetStream is having some issues, but not sure if this is related? Thanks.</p>

---

## Post #2 by @muratmaga (2025-04-21 14:58 UTC)

<p>There is an issue with older instances with IP addresses. I manually launched your instance. You should be able to access now.</p>
<p>Meanwhile, know that the cloud provider (JetStream2) we use has a scarcity of g3.xl instances we use on the MorphoCloud. Your instance may still fail to unshelve due to lack of resources. In general you want to check this link on the number of resources. If the g3.xl type shows red (4 or less available) then chances are your instance will not launch.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://docs.jetstream-cloud.org/overview/status/#availability-of-scarce-resources">
  <header class="source">
      <img src="https://docs.jetstream-cloud.org/favicon.ico" class="site-icon" width="59" height="59">

      <a href="https://docs.jetstream-cloud.org/overview/status/#availability-of-scarce-resources" target="_blank" rel="noopener nofollow ugc">docs.jetstream-cloud.org</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://docs.jetstream-cloud.org/overview/status/#availability-of-scarce-resources" target="_blank" rel="noopener nofollow ugc">Status and News - Jetstream2 Documentation</a></h3>

  <p>Jetstream2 Documentation</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>We are bringing back the CPU only instances to deal with the scarcity issue, but for that you need to create a new ticket, as instance types cannot be changed after creation.</p>

---

## Post #3 by @Kurt_Riggin (2025-05-29 18:37 UTC)

<p>Hello, I’m facing similar issues with my instance, but there doesn’t seem to be a lack of resources from JetStream2 for the g3.xl type (currently showing 56 available)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf340547720fc84af4828a06faf664c7bc2f0fb4.png" data-download-href="/uploads/short-url/rhsEkBSC72YLNQLkP0MA9vrfwj2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf340547720fc84af4828a06faf664c7bc2f0fb4_2_690x268.png" alt="image" data-base62-sha1="rhsEkBSC72YLNQLkP0MA9vrfwj2" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf340547720fc84af4828a06faf664c7bc2f0fb4_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf340547720fc84af4828a06faf664c7bc2f0fb4_2_1035x402.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf340547720fc84af4828a06faf664c7bc2f0fb4_2_1380x536.png 2x" data-dominant-color="14171D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1704×662 39.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would I need to create a new ticket for my instance?</p>

---

## Post #4 by @muratmaga (2025-05-29 19:38 UTC)

<p>Try again with /unshelve, I think it should work this time.</p>

---
