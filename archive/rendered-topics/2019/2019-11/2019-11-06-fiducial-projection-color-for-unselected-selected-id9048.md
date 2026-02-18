# Fiducial projection color for unselected/selected

**Topic ID**: 9048
**Date**: 2019-11-06
**URL**: https://discourse.slicer.org/t/fiducial-projection-color-for-unselected-selected/9048

---

## Post #1 by @ezgimercan (2019-11-06 19:31 UTC)

<p>In preview version, when 2D projection is turned on; unselecting one fiducial changes the color of all fiducials in slice view (2D projection). Compare preview and stable:<br>
Stable:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa8cb35c57522c057c728940f4a5721579b8d60d.jpeg" data-download-href="/uploads/short-url/okKCq3lq0x0WzeiqpwhY1YKvEYZ.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa8cb35c57522c057c728940f4a5721579b8d60d_2_481x375.jpeg" alt="PNG" data-base62-sha1="okKCq3lq0x0WzeiqpwhY1YKvEYZ" width="481" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa8cb35c57522c057c728940f4a5721579b8d60d_2_481x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa8cb35c57522c057c728940f4a5721579b8d60d_2_721x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/aa8cb35c57522c057c728940f4a5721579b8d60d_2_962x750.jpeg 2x" data-dominant-color="C6C4C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1102×857 255 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Preview:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e912c53676b8da21d1cd47a1dfc6108f351b204.png" data-download-href="/uploads/short-url/8VuDnItbR98fn4QFDFdBgGOkuUY.png?dl=1" title="slicer6" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e912c53676b8da21d1cd47a1dfc6108f351b204_2_517x359.png" alt="slicer6" data-base62-sha1="8VuDnItbR98fn4QFDFdBgGOkuUY" width="517" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e912c53676b8da21d1cd47a1dfc6108f351b204_2_517x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e912c53676b8da21d1cd47a1dfc6108f351b204_2_775x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e912c53676b8da21d1cd47a1dfc6108f351b204.png 2x" data-dominant-color="ACAAAE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer6</span><span class="informations">975×678 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-11-06 21:54 UTC)

<p>Projected fiducials color depends on the base color (if fiducial color is enabled and all points are selected then the selected color, if there are unselected points then the unselected color; otherwise chosen projection color) and whether the point is in front or behind the slice (base color or the inverse of the base color). State of individual points is not taken into account when determining the projected point color.</p>
<p>Could you describe your use case? What do you use point selection state for?</p>

---

## Post #3 by @ezgimercan (2019-11-07 00:24 UTC)

<p>Ah, I see what’s happening. It is a completely different functionality.<br>
In the stable version, the projection color was the same as 3D rendering color (unless fiducial color is selected). So when you unselected a fiducial, it was turning to unselected color in both 3D rendering and slice views but the selected fiducials were staying the original selected color.<br>
My use case is simply unselecting a point and locating that point on the specific slice using projections. I guess I can use “Show Slice Intersections” button.<br>
Using the same colors from the 3D rendering for behind/on/in front of the current slide distinction is what threw me off. And the location of landmarks and slice view randomly turning all of them to the unselected color seemed like a bug - because I could see the 3D rendering of the unselected point turning blue as in Stable version but all of the projections also turning blue didn’t make sense. They were just all behind or in front of the current slice…</p>

---

## Post #4 by @lassoan (2019-11-07 14:21 UTC)

<p>I agree that the markup point projection coloring behavior is not clear and consistent. We’ll improve it before the stable release.</p>
<p>Note that if you click on a markups point then it is shown in all slice views (so it becomes visible even without projection enabled).</p>
<p>Do you use the point selection state for anything (the checkbox in the markups list)?</p>

---

## Post #5 by @ezgimercan (2019-11-07 17:34 UTC)

<blockquote>
<p>Note that if you click on a markups point then it is shown in all slice views (so it becomes visible even without projection enabled).</p>
</blockquote>
<p>I didn’t notice this. It is very useful. But it only works if you know which point you are interested in 3D view, right? It doesn’t work from the list?</p>
<p>My lab follows some templates (basically a predetermined list of landmarks in a specific order) when landmarking CTs and we have Python scripts that name the Fiducials in this given order. So most of the time, I want to pick a Fiducial from the list (not knowing where it would be either in 3D or slice views), and locate it in all views. I was using Jump Slices and unselect functions together to do this.</p>
<p>On another note, we would love to have a mechanism to load template lists (this is a functionality other commercial tools provide, e.g. 3DMd) and fill the list but this is a big change from the current functionality. Also, it would require an “empty landmark” concept. For our current pipeline, I ask annotators to add a fiducial at 0,0,0 by using the + button and handle it later in the analysis.</p>

---

## Post #6 by @lassoan (2019-11-07 17:53 UTC)

<p>We already have an “empty landmark” concept implemented (each landmark has a state: undefined, preview, and defined), for the exact use case that you described. It will allow you to predefine landmark names and properties and then place them. We just need to implement a few more things before it becomes usable (add GUI for unsetting point positions; change placement logic to place undefined points before adding new points; save placement state to file).</p>

---
