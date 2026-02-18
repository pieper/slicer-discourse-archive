# Finding the minimum value of each sequence

**Topic ID**: 35597
**Date**: 2024-04-18
**URL**: https://discourse.slicer.org/t/finding-the-minimum-value-of-each-sequence/35597

---

## Post #1 by @dael0207 (2024-04-18 11:37 UTC)

<p>“Hello esteemed folks! I’m a beginner user of Slicer. During development, I need to find the minimum value of each sequence. How can I achieve this using Python? I’ll attach a picture. If my question isn’t clear, I’ll make adjustments. Thank you so much.”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa453231795ab83275993229d74859404e0662e4.png" data-download-href="/uploads/short-url/oihq9EJaORmzwidOum1SlQ3f8lS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa453231795ab83275993229d74859404e0662e4_2_690x344.png" alt="image" data-base62-sha1="oihq9EJaORmzwidOum1SlQ3f8lS" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa453231795ab83275993229d74859404e0662e4_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa453231795ab83275993229d74859404e0662e4_2_1035x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa453231795ab83275993229d74859404e0662e4.png 2x" data-dominant-color="32313B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1103×550 23.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-04-18 15:46 UTC)

<p>Maybe you mean this?</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.app.layoutManager().sliceWidget("Red").sliceController().sliceOffsetSlider().minimum
-138.21430206298828
&gt;&gt;&gt; slicer.app.layoutManager().sliceWidget("Red").sliceController().sliceOffsetSlider().maximum
116.78569793701172
&gt;&gt;&gt; 
</code></pre>

---

## Post #3 by @jamesobutler (2024-04-18 17:02 UTC)

<p>If you are trying to determine something like volume bounds you are better off using</p>
<pre data-code-wrap="python"><code class="lang-python">bounds = np.zeros(6)
volume_node.GetBounds(bounds)
</code></pre>

---

## Post #4 by @dael0207 (2024-04-22 01:45 UTC)

<p>yes right!! thank you very much and have a good day <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
