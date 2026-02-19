---
topic_id: 31803
title: "Conversion Of A Complex Structure From Closed Surface To Bin"
date: 2023-09-20
url: https://discourse.slicer.org/t/31803
---

# Conversion of a complex structure from closed surface to binary labelmap

**Topic ID**: 31803
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/conversion-of-a-complex-structure-from-closed-surface-to-binary-labelmap/31803

---

## Post #1 by @Matteboo (2023-09-20 14:06 UTC)

<p>Hello,</p>
<p>I import in Slicer a  segmentation of bloodvessel in .stl format.<br>
However I want to do operation on it in slicer (use the scisor tool for example) and to do that I need to change the master represenation from “Closed surface” to “Binary LabelMap”<br>
It works for small segmentation but it doesn’t work for a big complex one.<br>
Is there any tricks to make the conversion easier for 3Dslicer ?<br>
Also I don’t really know why the conversion isn’t working. Slicer just stop responding as if it’s computing in the background but the calculation never finish.<br>
When 3Dslicer is computing, my CPU usage is 35%, my RAM usage is 63% (13,9 Go of available RAM) and my GPU is at 2% usage so I don’t think the issue is that my PC is not powerfull enought.</p>
<p>If anybody has any advice, that would be very helpfull</p>
<p>Here is a link to the file that’s causing an issue <a href="https://drive.google.com/file/d/1LIGiy7LulJkyYNr2xmTWkt17iqMUYRVq/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">translated_vessels.stl - Google Drive</a></p>

---

## Post #2 by @chir.set (2023-09-20 14:38 UTC)

<p>Your file does load immediately on my system (5.5.0-2023-09-13 r32175, Linux). Looks like pulmonary vessels that need smoothing. It’s not a big file.</p>
<p>Are you perchance using Mac with M1/M2 CPU? There have been some many reports of simple tasks not performing well on that emulated OS.</p>

---

## Post #3 by @Matteboo (2023-09-20 16:09 UTC)

<p>The file loads easily is converting the file to a binary label time that isn’t working.<br>
I’m on window 10.<br>
I let 3DSlicer run for more than 2hours and when I got back the conversion was done.<br>
I guess it just takes a lot of time but I don’t know why.<br>
My CPU is a ryzen 7 3750H and my GPU is a RTX2060 if that can help.</p>

---

## Post #4 by @chir.set (2023-09-20 17:54 UTC)

<p>I misread your post, sorry. The conversion is burning my CPU too. We’ll probably end up saying it’s big a workload.</p>

---

## Post #5 by @Matteboo (2023-09-21 13:48 UTC)

<p>What’s weird is that my CPU isn’t burning or anything, it’s sitting at 35% use all the way throught the conversion.<br>
Is there a setting that I could have activated by mistake that reduces the amount of CPU used for this operation?</p>

---

## Post #6 by @cpinter (2023-09-22 10:34 UTC)

<p>Unfortunately the conversion algorithms (and many other algoritms) that Slicer uses from VTK are not all well optimized, and so the majority of the computations happen on a single thread. Since Slicer is mainly a research tool, and the underlying libraries are also developed from research grants, performance optimization has not been a priority.</p>
<p>There is a recently published algorithm for voxelization that might speed up this specific conversion considerably. Please see here:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/7224">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/7224" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/7224" target="_blank" rel="noopener">ENH: Adding the ability to leverage 3D Surface Nets for isocontouring</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jacob-moore22:feature/SurfaceNets</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-09-11" data-time="17:14:21" data-timezone="UTC">05:14PM - 11 Sep 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jacob-moore22" target="_blank" rel="noopener">
            <img alt="jacob-moore22" src="https://avatars.githubusercontent.com/u/133793250?v=4" class="onebox-avatar-inline" width="20" height="20">
            jacob-moore22
          </a>
        </div>

        <div class="lines" title="9 commits changed 4 files with 235 additions and 26 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/7224/files" target="_blank" rel="noopener">
            <span class="added">+235</span>
            <span class="removed">-26</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This aims to allow users to choose to leverage [3D surface nets](https://discour<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/7224" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">se.vtk.org/t/new-isocontouring-filter-for-discrete-labled-volumetric-data-vtksurfacenets3d/10614) to generate closed surfaces from segmented structures. This filter is more performant than the currently utilized flying edges. To use surface nets, check the "Use Surface Nets" box in the "Show 3D" drop-down menu, as shown. 
![image](https://github.com/Slicer/Slicer/assets/133793250/f5148397-2158-4c0a-9584-7f53833cbcb4)
For more information, see #7103</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Matteboo (2023-09-25 11:25 UTC)

<p>Thanks for the explanation.</p>
<p>It’s good to know that a faster algorithm exists, but I think that in the near future I’ll just find other ways or launch the conversion while I’m doing something else <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
