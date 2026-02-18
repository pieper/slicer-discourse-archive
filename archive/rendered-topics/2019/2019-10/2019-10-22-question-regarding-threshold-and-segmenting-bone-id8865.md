# Question regarding threshold and segmenting bone

**Topic ID**: 8865
**Date**: 2019-10-22
**URL**: https://discourse.slicer.org/t/question-regarding-threshold-and-segmenting-bone/8865

---

## Post #1 by @newellz (2019-10-22 18:38 UTC)

<p>Operating system:Windows 10 Enterprise<br>
Slicer version:4.10.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,</p>
<p>I am very much a novice to 3D slicer and slicer programs as a whole. I am currently attempting to segment bone projectile fragments embedded in bone of nearly identical density. Due to the close context of all of these objects and their similar density I have had no luck segmenting them using mask volume as I need to create a separate segment for every individual object. I have been manually painting every layer which as you can imagine is quite time consuming. In the early stages I had experimented with various volume and found one that allowed enough definition to diferentiate between the objects. As I go back I realize most of my early work had been done with different volume settings and a lot is segmented that is no longer showing up as bone. ( worked in W:8851 L:20399 before and now working in W:4637 and L19725) Does the earlier setting I was working have less definition because traces of underlying slices are showing through or am I effectively deleting bone from my view when I switch to a higher contrast?</p>

---

## Post #2 by @pieper (2019-10-22 20:10 UTC)

<p>Is this a CT dataset?  Those level window/level numbers look pretty big (expect level to be more like a few hundred to a couple thousand for bone if the data is in <a href="https://en.wikipedia.org/wiki/Hounsfield_scale" rel="nofollow noopener">Hounsfield units</a>).   Some screen shots or example data might help us suggest approaches.</p>

---

## Post #3 by @lassoan (2019-10-22 20:50 UTC)

<aside class="quote no-group" data-username="newellz" data-post="1" data-topic="8865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/43a26b/48.png" class="avatar"> newellz:</div>
<blockquote>
<p>I need to create a separate segment for every individual object</p>
</blockquote>
</aside>
<p>You can keep all fragments in one segment. When you are done with the segmentation, you can automatically split each fragment into a separate segment by using “Islands” effect’s “Split islands to segments” method. Segment statistics module can compute volume, surface, etc. properties for each segment.</p>

---

## Post #4 by @newellz (2019-10-23 15:05 UTC)

<p>I know this is micro ct data. How do you tell if it is in  Hounsfield units, because when I adjust the volume to the range you mentioned it is completely distorted.</p>

---

## Post #5 by @newellz (2019-10-23 15:12 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69d7e2e24d74aeb4c6d71bc9b500e09b9cd308ae.jpeg" data-download-href="/uploads/short-url/f6kFs3fetrZyofOiEOrJux54hT8.jpeg?dl=1" title="W%204637%20L%2019725" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69d7e2e24d74aeb4c6d71bc9b500e09b9cd308ae_2_690x218.jpeg" alt="W%204637%20L%2019725" data-base62-sha1="f6kFs3fetrZyofOiEOrJux54hT8" width="690" height="218" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69d7e2e24d74aeb4c6d71bc9b500e09b9cd308ae_2_690x218.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69d7e2e24d74aeb4c6d71bc9b500e09b9cd308ae_2_1035x327.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69d7e2e24d74aeb4c6d71bc9b500e09b9cd308ae_2_1380x436.jpeg 2x" data-dominant-color="5B5C63"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">W%204637%20L%2019725</span><span class="informations">3282×1039 488 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here are some screen shots of my project with the volumes module open and adjusted to the two settings Ive worked in.</p>

---

## Post #6 by @pieper (2019-10-23 15:24 UTC)

<p><a href="http://www.scanco.ch/index.php?id=faq_general#c926" rel="nofollow noopener">This reference</a> has a nice explanation.</p>
<p>It looks like you are doing a nice job.  You might find the 3D scissors tool useful to disconnect any points of contact between the pieces.</p>

---

## Post #7 by @muratmaga (2019-10-23 15:35 UTC)

<p>As <a class="mention" href="/u/pieper">@pieper</a> said, I think you are doing good with the data you have.</p>
<p>Going back to your original question, W/L ranges you set have no bearing on the segmentation directly. If you are using paint to draw masks, everything that’s within that mask for that segment is going to be exported (or saved) if your goal is to isolate those projectile pieces (regardless of what W/L you are looking at the slice). Having said that, different W/L ranges may result in you following different outlines, so it will indirectly impact the quality of segmentation.</p>
<p>Also this assumes you are not using any threshold to mask regions, but just painting those polygons. If you haven’t tried, try using Fill between slices effect in Segment Editor. That way you might be able to skip a few slices and speed up the segmentation.</p>
<p>I would also suggest switching to a newer version of slicer than 4.10.1 Possibly a preview version, and also add the SegmentEditorExtraEffects that might have some additional tools you can try and see if it works for your data.</p>

---

## Post #8 by @newellz (2019-10-23 16:49 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="8865">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Having said that, different W/L ranges may result in you following different outlines, so it will indirectly impact the quality of segmentation.</p>
</blockquote>
</aside>
<p>I may not have done such a good job presenting my question originally, but this directly comments on what I am needing to know. How exactly is this changing the outline that I follow when painting the segments? Am I effectively removing volume from these objects (i.e. distorting the true form of these objects) or are the areas that disappear when I change W/L ranges just remnants of what is present on an underlying slice?</p>

---
