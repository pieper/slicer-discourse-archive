# Adding near-real time collaborative manual segmentation

**Topic ID**: 29255
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/adding-near-real-time-collaborative-manual-segmentation/29255

---

## Post #1 by @kchawla-pi (2023-05-02 18:40 UTC)

<p>I am looking into building a plugin to collaboratively annotate and segment sMRI. The idea is that we can invite specific people via email and they (and only they) can all join and collaborate a volume as a team via a low latency connection, everything running on our local servers so the hospital’s data does not leave the servers.</p>
<p>What would that entail? I would appreciate any guidance &amp; support that can be offered so I know where to start.</p>
<p>I expect I will need to know how Slicer stores its segmentation data in memory as an MRI is being segmented. I expect I will have to stream that data to all connected users.</p>

---

## Post #2 by @lassoan (2023-05-02 18:47 UTC)

<p>There are collaborative editing possibilities at many different levels. For example, each user can run a local Slicer instance and sync data with others via OpenIGTLink. Or, you can run a single VNC-enabled Slicer docker image and allow many people to connect and control (there is one cursor, it can be controlled by anyone who has connected with the control-enabled link, similarly how you take control of a user’s computer in zoom, but VNC allows anybody from the group to take control, automatically).</p>

---

## Post #3 by @Javes7777 (2025-08-27 12:11 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
Is there a real-time collaborative environment in slicer3d that allows multiple users to work just like google docs?</p>

---

## Post #4 by @pieper (2025-08-27 12:25 UTC)

<p>There have been some very interesting experiments, but no currently available tool as far as I know.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.sciencedirect.com/science/article/pii/S1532046405000237">
  <header class="source">
      <img src="https://www.sciencedirect.com/shared-assets/103/images/favSD.ico" class="site-icon" alt="" width="32" height="32">

      <a href="https://www.sciencedirect.com/science/article/pii/S1532046405000237" target="_blank" rel="noopener">sciencedirect.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:112/150;"><img src="https://ars.els-cdn.com/content/image/1-s2.0-S1532046405X00272-cov150h.gif" class="thumbnail" alt="" width="112" height="150"></div>

<h3><a href="https://www.sciencedirect.com/science/article/pii/S1532046405000237" target="_blank" rel="noopener">Group-Slicer: A collaborative extension of 3D-Slicer</a></h3>

  <p>In this paper, we describe a first step towards a collaborative extension of the well-known 3D-Slicer; this platform is nowadays used as a standalone …</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Javes7777 (2025-08-27 13:28 UTC)

<p>yeah this one is from 2005,<br>
I found another paper:</p>
<p><a href="https://sfu-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=TN_cdi_hal_primary_oai_HAL_hal_03095450v1&amp;context=PC&amp;vid=SFUL&amp;lang=en_US&amp;search_scope=default_scope&amp;adaptor=primo_central_multiple_fe&amp;tab=default_tab&amp;query=title%2Ccontains%2Ccollaborative%2CAND&amp;query=any%2Cexact%2C3d%20slicer%2CAND&amp;sortby=rank&amp;mode=advanced&amp;offset=0" rel="noopener nofollow ugc">OpenDose3D: A free, <mark>collaborative 3D Slicer</mark> module for patient-specific dosimetry</a></p>
<p>But its behind a firewall and it also has something to do with dosimetry, which I am not sure allows editing segmentations.</p>

---

## Post #6 by @lassoan (2025-08-29 18:20 UTC)

<p>Google docs like editing is implemented in <a href="https://www.dnahive.com/imaging3d.html">ImagineHive</a> (some more information in a related Project Week <a href="https://projectweek.na-mic.org/PW40_2024_GranCanaria/Projects/ImagineHive/">project page</a>). You can find contact email on the webpage, but if you are interested I can also give more direct contact information in a private message.</p>

---
