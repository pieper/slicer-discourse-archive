# Setting the I-S range for a MarkupsROI

**Topic ID**: 32357
**Date**: 2023-10-20
**URL**: https://discourse.slicer.org/t/setting-the-i-s-range-for-a-markupsroi/32357

---

## Post #1 by @wesselk (2023-10-20 21:12 UTC)

<p>Hello all,</p>
<p>I’m looking for python Get and Set methods for the ROI Settings in markups.  In the picture below, I am trying to retrieve the current value of the lower bound of the I-S range (-26.52 here) and then set it to 0.  All I can find information on is getting and setting Control Point center/radius.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f53dae3243d6f8cc6e5a99a1c1351924b36bbdc0.png" data-download-href="/uploads/short-url/yZv83Oqrxg2AIaBNjKyoOXkbqq4.png?dl=1" title="discourse_q" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f53dae3243d6f8cc6e5a99a1c1351924b36bbdc0_2_570x499.png" alt="discourse_q" data-base62-sha1="yZv83Oqrxg2AIaBNjKyoOXkbqq4" width="570" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f53dae3243d6f8cc6e5a99a1c1351924b36bbdc0_2_570x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f53dae3243d6f8cc6e5a99a1c1351924b36bbdc0_2_855x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f53dae3243d6f8cc6e5a99a1c1351924b36bbdc0.png 2x" data-dominant-color="D8D6DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">discourse_q</span><span class="informations">951×833 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance for any help</p>

---

## Post #2 by @wesselk (2023-10-23 17:26 UTC)

<p>I have found out how to retrieve the values (although they are mysteriously slightly off from the GUI values) but I still cannot figure out how to set new ranges.</p>
<p>sz = [0,0,0,0,0,0]<br>
roiNode.GetBounds(sz) <span class="hashtag-raw">#stores</span> the dimensions of my ROI into sz</p>
<p>This <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#write-markup-roi-to-json-file" rel="noopener nofollow ugc">documentation</a> seems to imply that even if I load in a markup roi from a file it will need to simply be the center and size rather than specified bounds.  There has to be a way to do this, right?</p>
<p>Best,</p>

---

## Post #3 by @mikebind (2023-10-23 18:34 UTC)

<p>It looks to me like the two ways to control the position and range of a MarkupsROI are the <code>SetCenter()</code> and <code>SetSize()</code> methods.  Those don’t provide a convenience method for setting the range on one dimension exactly, but it’s not too hard to do the calculations you would need.  You can get the current center (<code>GetCenter()</code>, and then change the 3rd element to the middle of your new desired I-S range, and get the current size (<code>GetSize()</code>) and change the 3rd element to your new desired range (or half your new desired range, I can’t tell right off whether the size is like a radius or a diameter…)</p>

---

## Post #4 by @wesselk (2023-10-23 18:45 UTC)

<p>Thanks Mike, I was just in the middle of responding with my solution when you commented.  The only issue I’m still having is the inaccuracy of the GetBounds() method, see below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/897f28bdad3f2d0988d83d6327216a35808b2370.png" data-download-href="/uploads/short-url/jClQJWtme9EFCAmH0WkOdEEHfby.png?dl=1" title="getBounds_errors" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/897f28bdad3f2d0988d83d6327216a35808b2370_2_690x103.png" alt="getBounds_errors" data-base62-sha1="jClQJWtme9EFCAmH0WkOdEEHfby" width="690" height="103" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/897f28bdad3f2d0988d83d6327216a35808b2370_2_690x103.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/897f28bdad3f2d0988d83d6327216a35808b2370_2_1035x154.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/897f28bdad3f2d0988d83d6327216a35808b2370_2_1380x206.png 2x" data-dominant-color="F9F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">getBounds_errors</span><span class="informations">1546×231 13.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I don’t know if this warrants a bug report, it reduces my precision but I am still getting good results.</p>
<h2><a name="p-102205-my-solution-1" class="anchor" href="#p-102205-my-solution-1" aria-label="Heading link"></a>My Solution</h2>
<p>I have written 2 functions, getCenterfromBounds() and getSizefromBounds().  I think I need this slightly more involved approach to edit the ROI to account for skewed volumes.  To set a new lower bound, it looks like this:</p>
<pre><code class="lang-auto">bounds = [0,0,0,0,0,0]
roiNode.GetBounds(bounds)
newLower = getNewLowerBound(bounds[5],bounds[4])
bounds[4] = newLower
newCenter = getCenterFromBounds(bounds)
newSize = getSizeFromBounds(bounds)
roiNode.SetCenter(newCenter)
roiNode.SetSize(newSize)
</code></pre>

---

## Post #5 by @lassoan (2023-10-24 13:45 UTC)

<p>I don’t think there is a bug in the bounds computation. Both <code>GetRASBounds()</code> and <code>GetBounds()</code> methods return accurate results. The difference is that one returns the extents in the world coordinate system while the other in the markup’s own coordinate system.</p>

---
