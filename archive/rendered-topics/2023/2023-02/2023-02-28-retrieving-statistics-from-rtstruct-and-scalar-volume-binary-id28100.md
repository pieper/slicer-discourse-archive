# Retrieving statistics from RTSTRUCT and scalar volume - binary labelmap representation computation is very slow

**Topic ID**: 28100
**Date**: 2023-02-28
**URL**: https://discourse.slicer.org/t/retrieving-statistics-from-rtstruct-and-scalar-volume-binary-labelmap-representation-computation-is-very-slow/28100

---

## Post #1 by @Markb (2023-02-28 17:15 UTC)

<p>Hi all. I have access to some data which consists of a CT dataset and an accompanying RTSTRUCT file. This loads fine in 3D slicer, and I’ve even used it to generate some masked data which I then use in some Monte Carlo software. What I would like to do is to get some stats using the same RTSTRUCT segments. When I run the Segment Statistics, I only get some physical information about the segment (volume, surface area) but nothing from the scalar volume statistics. The error log states “setViewLabel should be called before setViewNode !” but Google is little help at solving this.</p>
<p>At the moment, it looks like the RTSTRUCT imports as a closed surface, but from the docs I believe Segment Statistics might need a binary labelmap to do its thing (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" rel="noopener nofollow ugc">readthedocs</a>). I’ve tried converting in segmentations but it literally takes forever and eventually I end up force quitting 3D slicer (I’m talking leaving the PC for 30 minutes and still chugging away at 100% CPU). Because of the force quit, I can’t see any of the error logs generated. I’ve converted into ribbon in the past, when I created the masks, as that seemed pretty nippy but doesn’t work to generate the statistics.</p>
<p>I’m currently using v4.11 on Ubuntu (virtual machine that comes with the MC software).</p>
<p>Any ideas? Thank you very much</p>

---

## Post #2 by @Sunderlandkyl (2023-02-28 19:42 UTC)

<p>Can you send me the dataset?</p>

---

## Post #3 by @Markb (2023-03-01 09:34 UTC)

<p>Hi Kyle, I’m away from my data at the moment, so I’ll send it tonight. Would a Googledrive link or similar work for you?</p>
<p>Just to add, I think the setViewLabel message might be a big of a red herring as I’ve seen it pop up a few times unrelated to this now. I also got hold of v5.2 to see if that helps, but that won’t display the RTSTRUCT overlay at all</p>

---

## Post #4 by @Markb (2023-03-02 20:53 UTC)

<aside class="onebox allowlistedgeneric" data-onebox-src="https://accounts.google.com/v3/signin/identifier?dsh=S-368642228%3A1677790417838363&amp;continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F19lc34Aj9Rb9NSYFd_gjn5mAL-GelcD0D%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F19lc34Aj9Rb9NSYFd_gjn5mAL-GelcD0D%2Fview%3Fusp%3Dsharing&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;ifkv=AWnogHcS0BW1v9m0rYUoFHvOx8UamQeEwEQFIbtmRgQ1vEX4mS8cDs2KPZ9nZJRXDpn4TJkoGR91rw">
  <header class="source">

      <a href="https://accounts.google.com/v3/signin/identifier?dsh=S-368642228%3A1677790417838363&amp;continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F19lc34Aj9Rb9NSYFd_gjn5mAL-GelcD0D%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F19lc34Aj9Rb9NSYFd_gjn5mAL-GelcD0D%2Fview%3Fusp%3Dsharing&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;ifkv=AWnogHcS0BW1v9m0rYUoFHvOx8UamQeEwEQFIbtmRgQ1vEX4mS8cDs2KPZ9nZJRXDpn4TJkoGR91rw" target="_blank" rel="noopener nofollow ugc">accounts.google.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://accounts.google.com/v3/signin/identifier?dsh=S-368642228%3A1677790417838363&amp;continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F19lc34Aj9Rb9NSYFd_gjn5mAL-GelcD0D%2Fview%3Fusp%3Dsharing&amp;followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F19lc34Aj9Rb9NSYFd_gjn5mAL-GelcD0D%2Fview%3Fusp%3Dsharing&amp;passive=1209600&amp;service=wise&amp;flowName=WebLiteSignIn&amp;flowEntry=ServiceLogin&amp;ifkv=AWnogHcS0BW1v9m0rYUoFHvOx8UamQeEwEQFIbtmRgQ1vEX4mS8cDs2KPZ9nZJRXDpn4TJkoGR91rw" target="_blank" rel="noopener nofollow ugc">Google Drive: Sign-in</a></h3>

  <p>Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hopefully that link will work. Thank you</p>

---

## Post #5 by @Sunderlandkyl (2023-03-02 21:32 UTC)

<p>There are a lot of complex hollow structures that are giving the planar contour → closed surface conversion trouble. Likely because of this some surfaces are poorly constructed, causing a problem when converting it to a binary labelmap.</p>
<p>As a workaround, you can instead convert the structures to binary labelmaps by going through the ribbon model representation.</p>
<ol>
<li>
<p>Click on the arrow beside “Create” for Binary labelmap and click “Advanced create…”:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c5615ca7a56b364899a0358ac8b4e2695008d40.png" alt="image" data-base62-sha1="42FNX5h68oNPE5En6K3AxJGwqDC" width="345" height="52"></p>
</li>
<li>
<p>Choose the “Planar contour → Ribbon model → Binary labelmap” path and click create:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4fbe41bddbaeba2d8d908b034e67ebda0a5ad19.png" alt="image" data-base62-sha1="uo8TFdXlif1O44J23gDZvonPWNX" width="329" height="351"></p>
</li>
</ol>

---

## Post #6 by @Markb (2023-03-02 21:59 UTC)

<p>Ah, that works perfectly. Thank you!</p>

---
