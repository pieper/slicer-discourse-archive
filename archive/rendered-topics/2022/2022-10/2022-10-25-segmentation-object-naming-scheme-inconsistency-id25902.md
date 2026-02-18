# Segmentation object naming scheme inconsistency

**Topic ID**: 25902
**Date**: 2022-10-25
**URL**: https://discourse.slicer.org/t/segmentation-object-naming-scheme-inconsistency/25902

---

## Post #1 by @muratmaga (2022-10-25 15:58 UTC)

<p>When I right click an object in Data module and choose segment this, the resultant segmentation object inherits the prefix of the volume name. However, if I go to the Segment Editor, it automatically creates a generic segmentation object that goes Segmentation_1, Segmentation_2. Can we make the latter match former (i.e, in segment editor do not create the segmentation object until a master volume is specified, and then inherit its name as a prefix).</p>
<p>I think the Data module behavior is a good for naming conventions, which should be encouraged for data management purposes. Also, I wonder if it makes sense to actually create the segmentation object nested under its master volume? It sure would make it easier visually to understand what going on. But I am not sure how to deal with cases where segment geometry is modified.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/d/ddff109e208d0415de83991dc5bc91a360476d14.png" alt="image" data-base62-sha1="vFRZGSeMruckrsIea7gnxVme7mk" width="659" height="248"></p>

---

## Post #2 by @lassoan (2022-10-27 06:19 UTC)

<p>Behavior of the high-level “Segment this…” is a high-level convenience feature in the Data module. It should not matter that its behavior is somewhat different compared to the lower-level feature of input node selection in Segment Editor module.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="25902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But I am not sure how to deal with cases where segment geometry is modified.</p>
</blockquote>
</aside>
<p>This is exactly the issue. Users would mistakenly think that the segmentation is associated with a single volume. It is quite often the case, but not always (you often have 3 volumes, acquired with 3 different slice orientations, and use all for creating a segmentation). Instead of setting the volume to be the parent item of the segmentation, we currently use a node reference, which provides a hint of association via highlighting the corresponding volume/segmentation node by coloring. This coloring is more subtle and more general (it could show association of a segmentation node with several source volumes) than parent/child relationship.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/824ec36c5c5f6c83e5e02a56c4e676deef4fc7a6.png" data-download-href="/uploads/short-url/iAKOTyF06cg8Ft7t4sndJcp6g7k.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824ec36c5c5f6c83e5e02a56c4e676deef4fc7a6_2_690x451.png" alt="image" data-base62-sha1="iAKOTyF06cg8Ft7t4sndJcp6g7k" width="690" height="451" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/824ec36c5c5f6c83e5e02a56c4e676deef4fc7a6_2_690x451.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/824ec36c5c5f6c83e5e02a56c4e676deef4fc7a6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/824ec36c5c5f6c83e5e02a56c4e676deef4fc7a6.png 2x" data-dominant-color="3C4547"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1005×658 43.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Probably the current behavior could be improved, but we would need to brainstorm a bit more to find a solution that makes things simpler without causing extra confusion.</p>

---

## Post #3 by @muratmaga (2022-10-27 16:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Probably the current behavior could be improved, but we would need to brainstorm a bit more to find a solution that makes things simpler without causing extra confusion.</p>
</blockquote>
</aside>
<p>Wow, I did not notice that behavior until you mentioned it. I occasionally saw the yellow strip on the volume object, but I chalked it up some QT rendering issue (as opposed to being a feature). It doesn’t help that it only highlights if you click the segmentation object (but not the actual segments).</p>
<p>This can potentially work, as you said if we can emphasize the connection between the master volume and the segmentation more clearly. Does QT have visual elements that may show like links between objects in Data module (as opposed to being nested under). This can come handy in other occasions as well.</p>

---

## Post #4 by @lassoan (2022-10-27 16:52 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="25902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Does QT have visual elements that may show like links between objects in Data module (as opposed to being nested under). This can come handy in other occasions as well.</p>
</blockquote>
</aside>
<p>We already highlight all node references in the subject hierachy tree (referring and referenced nodes with a slightly different color).</p>

---
