# DeCAL producing weird clustering of landmarks

**Topic ID**: 46071
**Date**: 2026-02-06
**URL**: https://discourse.slicer.org/t/decal-producing-weird-clustering-of-landmarks/46071

---

## Post #1 by @raranda22 (2026-02-06 11:14 UTC)

<p>Hello,</p>
<p>I have run DeCAL many times with a handful of meshes and curve semilandmarks from the MarkMyBird dataset. Each time, some of the surface landmarks cluster very closely together in strange ways. I would expect the points to appear more evenly distributed across the meshes, but that doesn’t seem to be the case. Might the issue relate to the input meshes for template generation, for example if the meshes represent highly variable shapes? Because I definitely use very different beaks to produce the template and apply dense corresponding landmarks.</p>
<p>Best,</p>
<p>Ricardo Ely</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/861c106e86ae79b8191fcd31c9b8b6a53c60d25d.jpeg" data-download-href="/uploads/short-url/j8o6IeJCvS6KKFD1a3LofQpM00d.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861c106e86ae79b8191fcd31c9b8b6a53c60d25d_2_690x378.jpeg" alt="image" data-base62-sha1="j8o6IeJCvS6KKFD1a3LofQpM00d" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861c106e86ae79b8191fcd31c9b8b6a53c60d25d_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/861c106e86ae79b8191fcd31c9b8b6a53c60d25d.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/861c106e86ae79b8191fcd31c9b8b6a53c60d25d.jpeg 2x" data-dominant-color="AFB18B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">976×535 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f08be35fd5a1796d151bba618940907e3b62ab6.jpeg" data-download-href="/uploads/short-url/4qxx4nYVS9Tr6COeUpDQ6gOVrXE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f08be35fd5a1796d151bba618940907e3b62ab6_2_690x435.jpeg" alt="image" data-base62-sha1="4qxx4nYVS9Tr6COeUpDQ6gOVrXE" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f08be35fd5a1796d151bba618940907e3b62ab6_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f08be35fd5a1796d151bba618940907e3b62ab6.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f08be35fd5a1796d151bba618940907e3b62ab6.jpeg 2x" data-dominant-color="ADAC7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">941×594 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86e6ab7ad5aab86c8851d3963cc574472cc9de83.jpeg" data-download-href="/uploads/short-url/jfobI84Sx0wZyVQfdYTpvoUI0ld.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86e6ab7ad5aab86c8851d3963cc574472cc9de83_2_690x442.jpeg" alt="image" data-base62-sha1="jfobI84Sx0wZyVQfdYTpvoUI0ld" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86e6ab7ad5aab86c8851d3963cc574472cc9de83_2_690x442.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86e6ab7ad5aab86c8851d3963cc574472cc9de83_2_1035x663.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86e6ab7ad5aab86c8851d3963cc574472cc9de83.jpeg 2x" data-dominant-color="B3B291"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1146×735 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-02-06 17:11 UTC)

<aside class="quote no-group" data-username="raranda22" data-post="1" data-topic="46071">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/raranda22/48/80343_2.png" class="avatar"> raranda22:</div>
<blockquote>
<p>Might the issue relate to the input meshes for template generation, for example if the meshes represent highly variable shapes?</p>
</blockquote>
</aside>
<p>How are you running the DeCAL pipeline? Are you using an existing template, or are you havign DeCAL generate the template? If you are doing the latter, how does the template look? Are the points uniformly distributed on it?</p>
<p>The rest of the points are not also very well distributed. So the first step is to check what the template looks like.</p>

---

## Post #3 by @raranda22 (2026-02-09 08:12 UTC)

<p>I forgot to mention these details you’re referring to. The first image is the template model. I am not using an existing template, I’m generating a new one. So you can clearly see the points are not uniformly distributed even on the template.</p>

---

## Post #4 by @muratmaga (2026-02-09 18:31 UTC)

<p>Yes, you can be sure that DeCAL won’t work, if your template does not have smooth distribution of points.</p>
<p>There are few things you need to understand about how decal works. The fixed landmarks (in your case your curves), provide the input about the how models need to be globally aligned for the downstream point by point correspondences. For that you don’t need a lot of landmark, 6-12 usually suffice provided that they are distributed nicely along the surface.</p>
<p>You have a lot of points, but they essentially trace only three lines, so a lot of those points are redundant and doesn’t help with alignment much. 3-4 points on each line would probably have given you the same result). There is nothing that constrains the end of the beak (towards the skull), nothing on the ventral or lateral side of the beaks. So it is not surprising that the template looks so noisy.</p>
<p>So unless you change your fixed landmarking scheme significantly, I don’t think DeCAL will work for you.</p>

---
