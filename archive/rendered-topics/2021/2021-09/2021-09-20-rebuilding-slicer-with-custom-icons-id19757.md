---
topic_id: 19757
title: "Rebuilding Slicer With Custom Icons"
date: 2021-09-20
url: https://discourse.slicer.org/t/19757
---

# Rebuilding slicer with custom icons

**Topic ID**: 19757
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/rebuilding-slicer-with-custom-icons/19757

---

## Post #1 by @Chintha_Siva_Prasad (2021-09-20 07:56 UTC)

<p>I am compiling slicer. And want to change the icons too. Where should I change the icons in the source code? And are there any image resolution constraints?</p>

---

## Post #2 by @Sam_Horvath (2021-09-20 15:34 UTC)

<p>We currently do not have all of the icons in one central place in the repo.  Icons specific to modules will be found in the resources folder of that module.</p>
<p><a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Markups/Resources/Icons">Markups module icons</a></p>
<p><a href="https://github.com/Slicer/Slicer/tree/master/Base/QTGUI/Resources/Icons">Generic icons used throughout Slicer</a></p>

---

## Post #3 by @lassoan (2021-09-21 20:50 UTC)

<p>We are in the process of replacing Slicer icons by simpler, contemporary, dual tone design, using higher resolution. Do you want to do some similar, or you just want to replace the Slicer logo?</p>

---

## Post #4 by @Chintha_Siva_Prasad (2021-09-23 10:42 UTC)

<p>Yeah I am trying to do the similar.</p>

---

## Post #5 by @lassoan (2021-09-24 02:42 UTC)

<p>See progress here:</p>
<ul>
<li>Draft pull request (incomplete, just preliminary tests): <a href="https://github.com/Slicer/Slicer/pull/5887" class="inline-onebox">ENH: Improve icon set by lassoan · Pull Request #5887 · Slicer/Slicer · GitHub</a>
</li>
<li>Discussion: <a href="https://discourse.slicer.org/t/update-slicers-icon-set/12483/14" class="inline-onebox">Update Slicer's icon set - #14 by lassoan</a>
</li>
<li>Labs page: <a href="https://github.com/Slicer/Slicer/wiki/Modern-Look" class="inline-onebox">Modern Look · Slicer/Slicer Wiki · GitHub</a>
</li>
</ul>
<p>We don’t plan to work on creating an icon theme (which would make it very easy to replace the entire icon set), so if you want you can investigate that and come up with a proposal (preferably as a drafy pull request that we can try).</p>
<p>You could also help with finalizing the icon creation process and creating icons using that.</p>

---
