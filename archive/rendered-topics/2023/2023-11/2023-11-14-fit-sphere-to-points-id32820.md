---
topic_id: 32820
title: "Fit Sphere To Points"
date: 2023-11-14
url: https://discourse.slicer.org/t/32820
---

# Fit sphere to points

**Topic ID**: 32820
**Date**: 2023-11-14
**URL**: https://discourse.slicer.org/t/fit-sphere-to-points/32820

---

## Post #1 by @ben.rodwell (2023-11-14 20:24 UTC)

<p>I am trying to fir a sphere between 4 control points using the script below. I have set my four points using the markups module and when I run the script in the python interactor it generates a new model in the models module but it is not visible and so I am just wondering what I am doing wrong and how do I actually use this script to generate a sphere?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/markups.html#specify-a-sphere-by-multiple-control-points" rel="noopener nofollow ugc">Script repository: Specify a sphere by multiple control points</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/036158325b5c8aa549a26206f6a726a856316dbe.png" data-download-href="/uploads/short-url/tTZvytc5vyVKiS4GeIOuYsIT26.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036158325b5c8aa549a26206f6a726a856316dbe_2_690x400.png" alt="image" data-base62-sha1="tTZvytc5vyVKiS4GeIOuYsIT26" width="690" height="400" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036158325b5c8aa549a26206f6a726a856316dbe_2_690x400.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036158325b5c8aa549a26206f6a726a856316dbe_2_1035x600.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/036158325b5c8aa549a26206f6a726a856316dbe_2_1380x800.png 2x" data-dominant-color="5A626B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1691×981 178 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-11-14 20:25 UTC)

<p>All you need to do is to replace <code>pointListNode</code> by the node that stores your input points (e.g., <code>pointListNode=getNode('F')</code>) and then copy-paste the example code from the script repository.</p>

---

## Post #3 by @ben.rodwell (2023-11-15 02:14 UTC)

<p>Hi Andras, thanks a bunch for your help, I realize now that I was using separate markup points instead of putting them all into a single points list which was causing my issue earlier!</p>

---
