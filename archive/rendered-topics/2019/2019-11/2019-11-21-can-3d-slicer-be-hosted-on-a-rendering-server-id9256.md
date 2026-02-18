# Can 3D Slicer be hosted on a rendering server?

**Topic ID**: 9256
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/can-3d-slicer-be-hosted-on-a-rendering-server/9256

---

## Post #1 by @Yusuf (2019-11-21 17:04 UTC)

<p>Hi,<br>
Can the slicer3D be hosted off a render server so that multiple clients can access it with less powerful client hardware?</p>
<p>Thank you</p>

---

## Post #2 by @muratmaga (2019-11-21 18:01 UTC)

<p>That’s fairly easy to do on Linux using VirtualGL and TurboVNC.<br>
<a href="https://virtualGL.org" class="onebox" target="_blank" rel="nofollow noopener">https://virtualGL.org</a></p>

---

## Post #3 by @lassoan (2019-11-21 19:13 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/pieper">@pieper</a> Do you have experience in setting up a docker swarm with web VNC and reverse proxy so that multiple users can log on through the same webpage, each seeing his own Slicer instance?</p>
<p>We could host such a server in our lab, but we would need help with setting it up.</p>
<p>It could be used to demonstrate that Slicer can “run in a web browser” and it could be also configured to do segmentation or other tasks initiated from OHIF DICOM web viewer (download the data set, allow user to interact with it, then push back the data). It would be awesome to have this for RSNA.</p>

---

## Post #4 by @muratmaga (2019-11-21 19:34 UTC)

<p>Sorry, I have no experience with docker. But would love to see what you describe in action…</p>

---

## Post #5 by @pieper (2019-11-22 21:12 UTC)

<p>I don’t have a fully worked out example now, but have discussed working on this at project week with Emel to test with ePad.</p>
<p>I was planning to set something up using google cloud technologies so it would scale and basically be open to anyone willing to sign up for an account (at least for the first $300 worth of testing) can try it out.  But the same basic functionality should also be good to work with a server at Perk if you want to open it up.  Main issues I can think of are dealing with user accounts, TLS, allocating ports to users, etc.</p>
<p>On google I’ve been playing with the <a href="https://cloud.google.com/iap/">Identity Aware Proxy</a> which allows TLS and you can control authorization of connections to VMs or instances via google logins so we can get out of demo mode into something you could use for real work.  All this stuff can be controlled via the gcloud API, so my thought would be that you would be in OHIF or ePad and you’d ask for a Slicer instance to open up with the same study (hence I was calling the project SlicerStudyBuddy - name subject to discussion <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:">).  If you are logged to your google account and accessing one of their dicomweb servers it’s possible to pass the authentication token to the virtual Slicer instance so it can inherit that access to pull the data.</p>
<p>Would be interesting to try setting this up for RSNA, but of course the time is short.</p>

---

## Post #6 by @muratmaga (2019-11-22 21:37 UTC)

<p>There are alternatives:</p>
<p>NSF/XSEDE supports a program called Science Community Gateways Initiative. <a href="https://sciencegateways.org/" rel="nofollow noopener">https://sciencegateways.org/</a></p>
<p>We can request computational resources to be used by the public, as well as support for a gateway interface. These are free-of-charge services, but require competitive renewal every 12 months. Most likely the allocation will be on their Jetstream VM farm (<a href="https://jetstream-cloud.org/" rel="nofollow noopener">https://jetstream-cloud.org/</a>). Jetstream currently does not support GPUs, but there can be a hybrid solution.</p>
<p>Like any grant application, it will require a demonstrable need by the community.</p>

---

## Post #7 by @Yusuf (2019-11-25 10:04 UTC)

<p>Thank you indeed for all your replies and your time.</p>
<p>Regards</p>

---

## Post #8 by @lassoan (2019-11-26 19:58 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="9256">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I was planning to set something up using google cloud technologies so it would scale and basically be open to anyone willing to sign up for an account (at least for the first $300 worth of testing) can try it out.</p>
</blockquote>
</aside>
<p>This would be awesome to have for RSNA. Do you think you could have a chance to set this up?</p>
<p>In the long term, we will need both cloud and self hosting setup - cloud hosting is very scaleable and lots of pre-configured services are available; self hosting has no data privacy issues, can be more vendor neutral, and may cost less.</p>
<p>Science Community Gateways could be good, too, but if you need to write a proper proposal (not just a formality like filling out a form) every 12 months then I don’t see the point, as you could spend that time with writing larger grants that can fund cloud computing resources or buying your own hardware.</p>

---

## Post #9 by @muratmaga (2019-11-26 21:09 UTC)

<p>XSEDE grants  look somewhat like a regular grant initially, but competitive renewals (every 12 months) are much simpler, especially if you are hitting your target user numbers and can justify maintaining the resource. If not, you can dial down your request to more meaningful numbers.</p>
<p>It is really the lack of GPU on those VM is my main hesitation. Perhaps that will have that soon…</p>

---

## Post #10 by @pieper (2019-11-26 22:28 UTC)

<p>With the short week here I don’t think I’ll have time to set anything up before RSNA, but we can probably try some things on the fly there.</p>

---

## Post #11 by @fedorov (2019-11-26 23:14 UTC)

<p>I would be interested in this as well - let me know if you get together to work on this at RSNA!</p>

---

## Post #12 by @nchaves (2021-03-22 01:12 UTC)

<p>Hi, I hope everyone is doing fine! Out of curiosity, has there been any progress on the topic of this thread?</p>

---

## Post #13 by @muratmaga (2021-03-22 05:51 UTC)

<p>Recently we ran our week long SlicerMorph workshop on cloud using Docker containers. I made some comments on how it worked out here:</p><aside class="quote quote-modified" data-post="7" data-topic="16401">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-run-slicer-on-the-cloud-and-access-in-a-web-browser/16401/7">How to run Slicer on the cloud and access in a web browser</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We just finished the first day running SlicerMorph workshop on the Cloud. This note is for sharing the experience with other folks interested in running Slicer as an remote interactive desktop application (not thru Jupyter notebooks or binder). 


We are using this docker <a href="https://github.com/SlicerMorph/SlicerMorphCloud/" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerMorphCloud: Docker for running SlicerMorph on Cloud</a>, which provides a simple openbox WM, with a file browser, Slicer, R/Rstudio and Firefox. (same docker can be used for GPU accelerated setups with Nv…
  </blockquote>
</aside>

<p>Overall it went well. VNC sessions can be managed better (specifically issue <span class="hashtag-raw">#6</span>), but otherwise  experience has been quite pleasant.</p>

---
