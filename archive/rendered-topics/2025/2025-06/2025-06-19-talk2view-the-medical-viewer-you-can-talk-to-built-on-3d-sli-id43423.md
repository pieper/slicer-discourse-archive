# Talk2View - The medical viewer you can talk to - Built on 3D Slicer

**Topic ID**: 43423
**Date**: 2025-06-19
**URL**: https://discourse.slicer.org/t/talk2view-the-medical-viewer-you-can-talk-to-built-on-3d-slicer/43423

---

## Post #1 by @andy97 (2025-06-19 16:31 UTC)

<p>Hi everyone,</p>
<p>We’re excited to share the first very early (and experimental) release of <a href="https://talk2view.com" rel="noopener nofollow ugc">Talk2View</a>, the medical image viewer you can talk to.</p>
<p>The idea behind Talk2View is that rather than navigating through complex menus, buttons and tools, users can interact with medical images and models using natural language. Whether it’s visualizing anatomy, manipulating 3D views, or referencing educational material, our goal is to make imaging tools easier and faster to use—especially for students, clinicians, and researchers who may not have technical backgrounds.</p>
<p>You can find out more about Talk2View on our website:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://talk2view.com">
  <header class="source">
      <img src="https://talk2view.com/lovable-uploads/5b250093-59f1-4784-ac98-06931b2e619a.png" class="site-icon" width="500" height="500">

      <a href="https://talk2view.com" target="_blank" rel="noopener nofollow ugc">talk2view.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://talk2view.com" target="_blank" rel="noopener nofollow ugc">Talk2View</a></h3>

  <p>Talk2View - A medical viewer you can talk to</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>We invite you to sign up and download our latest Talk2View release here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://talk2view.com/download">
  <header class="source">
      <img src="https://talk2view.com/lovable-uploads/5b250093-59f1-4784-ac98-06931b2e619a.png" class="site-icon" width="500" height="500">

      <a href="https://talk2view.com/download" target="_blank" rel="noopener nofollow ugc">talk2view.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://talk2view.com/download" target="_blank" rel="noopener nofollow ugc">Talk2View</a></h3>

  <p>Talk2View - A medical viewer you can talk to</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Talk2View is a commercial product built on top of 3D Slicer. We’ve made deliberate choices around licensing to support our goals, but we’re also clear that none of this would be possible without the open-source work behind 3D Slicer. We’re grateful to the community for building such a solid platform.</p>
<p>We recognize there are different views on how open-source and commercial efforts should intersect. Our focus is on building something useful, and where there’s overlap or opportunity to collaborate with the community, we’re open to it.</p>
<p>We want to sincerely thank the 3D Slicer community. The years of open-source work that have gone into building 3D Slicer made this possible.</p>
<p>Best,</p>
<p>Andy, Ben, Kat, Wilson, and the rest of Talk2View Team</p>

---

## Post #2 by @Deep_Learning (2025-06-20 13:30 UTC)

<p>is this using model context protocol?</p>

---

## Post #3 by @andy97 (2025-06-23 18:08 UTC)

<p>Hi!</p>
<p>We currently do not use Model Context Protocol (MCP) in our application yet, but we do have plans to integrate it in the future. Our priority is to ensure that it is implemented securely and correctly, especially given some of the security concerns identified in current implementations.</p>
<p>What are your thoughts on using MCP to wrap existing custom 3D Slicer extensions/modules to be used by the AI Agent?</p>

---

## Post #4 by @Deep_Learning (2025-06-26 14:36 UTC)

<p>MCP opens too many doors…</p>
<p>When I heard about mcp (which i was calling/typing mpc for weeks) it reminded me not of usb but of bluetooth.  It’s going to be so important.</p>
<p>---- What are your thoughts on using MCP to wrap existing custom 3D Slicer extensions/modules to be used by the AI Agent?</p>
<p>Are extensions independent enough to be used as a tool?  An opensource emr would be a great tool.</p>

---

## Post #5 by @benzwick (2025-06-27 14:04 UTC)

<p>We have now also <a href="https://discourse.slicer.org/t/talk2view-the-medical-viewer-you-can-talk-to-now-available-as-a-3d-slicer-extension/43515">released Talk2View as an extension for 3D Slicer</a>. This means that 3D Slicer users can use Talk2View within their existing environment by simply downloading and installing the Talk2View extension from our website <a href="http://www.talk2view.com" rel="noopener nofollow ugc">www.talk2view.com</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a7cfa7e055badf0e6d17afdc283154036c35850.jpeg" data-download-href="/uploads/short-url/jL7EG16Y508C8g041puTxYoN6oM.jpeg?dl=1" title="Screenshot_20250627_025825" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a7cfa7e055badf0e6d17afdc283154036c35850_2_690x425.jpeg" alt="Screenshot_20250627_025825" data-base62-sha1="jL7EG16Y508C8g041puTxYoN6oM" width="690" height="425" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a7cfa7e055badf0e6d17afdc283154036c35850_2_690x425.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a7cfa7e055badf0e6d17afdc283154036c35850_2_1035x637.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a7cfa7e055badf0e6d17afdc283154036c35850_2_1380x850.jpeg 2x" data-dominant-color="9D999D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20250627_025825</span><span class="informations">1960×1208 712 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
