---
topic_id: 33827
title: "Integrate Slicer Into A Web Interface"
date: 2024-01-17
url: https://discourse.slicer.org/t/33827
---

# Integrate Slicer into a web interface

**Topic ID**: 33827
**Date**: 2024-01-17
**URL**: https://discourse.slicer.org/t/integrate-slicer-into-a-web-interface/33827

---

## Post #1 by @MarcMR (2024-01-17 16:19 UTC)

<p>Hello,<br>
We are using 3D slicer with some custom made plugins (plugins that connect to images in our database and others).<br>
We want other users to interacts with “our” 3d slicer. Ideally (instead of them installing it locally on their computer which can be cumbersome because there are a lot of plugins) we are thinking about the possibility de develop a web interface so that we can just give them an adress, and they can use slicer through a brower interface without the need to install anything.</p>
<p>Do you know if such an integration has already been developed so that we can have a look at it an reuse what has been done ? If not, do you think it is feasable technically and how would you proceed ?</p>
<p>Thanks a lot for your help !</p>

---

## Post #2 by @lassoan (2024-01-17 17:28 UTC)

<p>There are several solutions for this. You can run Slicer in a docker container and connect to it from a web broser as shown here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/pieper/SlicerDockers">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/dc2f796837ddaa3aa9b98e294f96a6623868cb0cc7a42b465625e6b04d840dc0/pieper/SlicerDockers" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/pieper/SlicerDockers" target="_blank" rel="noopener">GitHub - pieper/SlicerDockers: docker config files for slicer</a></h3>

  <p>docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If you need a more sophisticated setup (user authentication, Slicer instance automatically started when a user logs in, connection with hospital PACS, etc.) then that’s all doable, too. Several people on this forum have set up such systems using various technology stacks. However, significant expertise and effort are required to set up and manage a server that provides this - I don’t think there is a free and open-source turn-key solution.</p>

---

## Post #3 by @muratmaga (2024-01-17 18:17 UTC)

<aside class="quote no-group" data-username="MarcMR" data-post="1" data-topic="33827">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/marcmr/48/68990_2.png" class="avatar"> MarcMR:</div>
<blockquote>
<p>We want other users to interacts with “our” 3d slicer. Ideally (instead of them installing it locally on their computer which can be cumbersome because there are a lot of plugins) we are thinking about the possibility de develop a web interface so that we can just give them an adress, and they can use slicer through a brower interface without the need to install anything.</p>
</blockquote>
</aside>
<p>there are about at least couple dozen different ways of doing this. Depends on your technical skills, and how you want to run the Slicer.</p>
<p>One of the simpler solutions would be to run Slicer on Linux box, which is setup to use turboVNC and VirtualGL (if you want 3D acceleration, and remote GPU support). Then you create linux accounts for your users, and then they can connect using the dedicated TurboVNC client (works on mac, windows and linux) and login their desktop session and fully interact with the “your” computer with your Slicer installed.</p>
<p>If installing turbovnc client is a deal breaker, you can also do the similar setup with noVNC or other alternatives that will work through a web browser. Based on my experience, dedicated turbovnc client gives better network performance, particularly if you are on slow connections.</p>
<p>It is important to note, VNC (in any form), does not allow application isolation. Meaning if you want your folks to have only access to Slicer on the computer and nothing else, that’s not possible. However, things being fully configurable in Linux, you can create a custom environment, in which they can only easily start Slicer.</p>
<p>If you want to limit people’s access to resources (constrain the memory usage, number of cores they can use etc), you can go down the docker route.</p>

---
