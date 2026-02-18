# New Segment Statistics: Oriented Bounding Box, Diameter and More

**Topic ID**: 10203
**Date**: 2020-02-11
**URL**: https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203

---

## Post #1 by @Sunderlandkyl (2020-02-11 14:08 UTC)

<p>New statistics have been added to the Segment Statistics module:</p>
<ul>
<li>Centroid</li>
<li>Oriented bounding box</li>
<li>Feret diameter</li>
<li>Perimeter</li>
<li>Roundness</li>
<li>Flatness</li>
<li>Elongation</li>
<li>Principal axes/moments</li>
</ul>
<p>These statistics are not enabled by default. To enable them, click on the “Options” button beside the “Labelmap Statistics” checkbox, and select the statistics that you would like calculated from the popup window.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1215fbf5a379c4665e2091ef31cba1e48ae25474.png" data-download-href="/uploads/short-url/2zZH7fLta4P90vWGbpxlusk3hqY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1215fbf5a379c4665e2091ef31cba1e48ae25474_2_517x359.png" alt="image" data-base62-sha1="2zZH7fLta4P90vWGbpxlusk3hqY" width="517" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1215fbf5a379c4665e2091ef31cba1e48ae25474_2_517x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1215fbf5a379c4665e2091ef31cba1e48ae25474_2_775x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1215fbf5a379c4665e2091ef31cba1e48ae25474.png 2x" data-dominant-color="EFF1EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">814×566 32.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can read the documentation for the Segment Statistics module <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmentstatistics.html" rel="noopener nofollow ugc">here</a>.</p>
<p><strong>Oriented bounding box:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e72285939b0de724fdb92c1f2509b07eb474397a.jpeg" data-download-href="/uploads/short-url/wYIg0J7wFKzWP3CWq8W1fDzMzsm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e72285939b0de724fdb92c1f2509b07eb474397a_2_552x375.jpeg" alt="image" data-base62-sha1="wYIg0J7wFKzWP3CWq8W1fDzMzsm" width="552" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e72285939b0de724fdb92c1f2509b07eb474397a_2_552x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e72285939b0de724fdb92c1f2509b07eb474397a_2_828x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e72285939b0de724fdb92c1f2509b07eb474397a_2_1104x750.jpeg 2x" data-dominant-color="9795B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1533×1043 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Feret diameter and centroid:</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d375f2b5aeb4bb014a0c2e4e9bbb545b90fe02be.jpeg" data-download-href="/uploads/short-url/uaFrPsv05kYcCqvYNju1rDQWXgy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d375f2b5aeb4bb014a0c2e4e9bbb545b90fe02be_2_552x378.jpeg" alt="image" data-base62-sha1="uaFrPsv05kYcCqvYNju1rDQWXgy" width="552" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d375f2b5aeb4bb014a0c2e4e9bbb545b90fe02be_2_552x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d375f2b5aeb4bb014a0c2e4e9bbb545b90fe02be_2_828x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d375f2b5aeb4bb014a0c2e4e9bbb545b90fe02be_2_1104x756.jpeg 2x" data-dominant-color="9997AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1521×1044 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>Principal axes and moments</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e7172a358013703714098d133f9a91da2e91e84.png" data-download-href="/uploads/short-url/dttWsYQUMsRm6548lyJ7OG6jIyg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e7172a358013703714098d133f9a91da2e91e84_2_552x309.png" alt="image" data-base62-sha1="dttWsYQUMsRm6548lyJ7OG6jIyg" width="552" height="309" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e7172a358013703714098d133f9a91da2e91e84_2_552x309.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e7172a358013703714098d133f9a91da2e91e84_2_828x463.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5e7172a358013703714098d133f9a91da2e91e84_2_1104x618.png 2x" data-dominant-color="9A9AC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1472×827 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>For developers:</strong><br>
A new filter called vtkITKLabelShapeStatistics has been added to vtkITK that can be used to calculate the above statistics on any labelmap image.</p>
<p>An example script for visualizing segment OBB can be found <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_size.2C_position.2C_and_orientation_of_each_segment" rel="noopener nofollow ugc">here</a>.<br>
The ITK paper for the shape label filter can be found <a href="https://www.insight-journal.org/browse/publication/176" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #2 by @Carlos_Felipe_Lobo (2023-07-21 13:34 UTC)

<p>Hello <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>,<br>
The statistics available in the module are fantastic and have helped me a lot, thank you.<br>
I’m just not able to visualize the box, sphere and axes in 3D, as shown in the images. Could you help me with this issue?<br>
Thank you very much and congratulations for the work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd95e9bf772af47124f911cbe7f58a25fd68436f.png" data-download-href="/uploads/short-url/r39qBR1zQBy1u9Bo1pKPtunRNIX.png?dl=1" title="segmentStatistics" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd95e9bf772af47124f911cbe7f58a25fd68436f_2_690x303.png" alt="segmentStatistics" data-base62-sha1="r39qBR1zQBy1u9Bo1pKPtunRNIX" width="690" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd95e9bf772af47124f911cbe7f58a25fd68436f_2_690x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd95e9bf772af47124f911cbe7f58a25fd68436f_2_1035x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd95e9bf772af47124f911cbe7f58a25fd68436f_2_1380x606.png 2x" data-dominant-color="545466"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentStatistics</span><span class="informations">1914×841 52.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2023-07-21 13:57 UTC)

<p>You can copy-paste <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi">this code snippet</a> into the Python console to display the bounding boxes.</p>

---

## Post #4 by @Carlos_Felipe_Lobo (2023-07-21 16:08 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="1" data-topic="10203">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>moment</p>
</blockquote>
</aside>
<p>Thank you for your attention and for the quick response <a class="mention" href="/u/lassoan">@lassoan</a> . The boxes turned out fine. I am now looking for a script to display principal axes and moments. Do you know if there are any available?<br>
Thank you very much</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4273d6240f8cbf346558d69c73a20a0ba577b17.png" data-download-href="/uploads/short-url/pHI0XFvTJB4SEqGzkLl1xjnjuqr.png?dl=1" title="segmentStatistics" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4273d6240f8cbf346558d69c73a20a0ba577b17_2_690x247.png" alt="segmentStatistics" data-base62-sha1="pHI0XFvTJB4SEqGzkLl1xjnjuqr" width="690" height="247" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4273d6240f8cbf346558d69c73a20a0ba577b17_2_690x247.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4273d6240f8cbf346558d69c73a20a0ba577b17_2_1035x370.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4273d6240f8cbf346558d69c73a20a0ba577b17_2_1380x494.png 2x" data-dominant-color="565260"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentStatistics</span><span class="informations">1918×688 66.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2023-07-21 17:08 UTC)

<p>The box axes are the principal axes.</p>

---

## Post #6 by @Carlos_Felipe_Lobo (2023-07-21 17:50 UTC)

<p>Thank you! I appreciate the help <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @lassoan (2023-11-27 07:05 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/segmentation-size-measurements-craniocaudal-length-and-max-diameter-to-table/20825/8">Segmentation size measurements (craniocaudal length and max diameter) to table</a></p>

---
