# Best strategy to integrate airway segmentation into LungCTSegmenter?

**Topic ID**: 19674
**Date**: 2021-09-14
**URL**: https://discourse.slicer.org/t/best-strategy-to-integrate-airway-segmentation-into-lungctsegmenter/19674

---

## Post #1 by @rbumm (2021-09-14 20:27 UTC)

<p>I am planning to integrate an airway segmentation into the LungCTSegmenter extension.<br>
Would it make sense to invest time and connect the current CIP airway segmentation module or would you recommend writing that completely new using the recent segment editor features?</p>
<p>I could call the current CIP airway segmentation from the LungCTSegmenter and transform the generated labelmap into segmentation and display it, in one go. Airway segmentation results are quite good, the procedure itself is, however, slow. The process is not very interactive but we could make use of the one trachea markup which I demand from the users and go from there. As a con, one could not  correct for leaks etc. easily.</p>
<p>Any advice or ideas are welcome. Thanks.</p>

---

## Post #2 by @lassoan (2021-09-14 21:10 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="1" data-topic="19674">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>the procedure itself is, however, slow</p>
</blockquote>
</aside>
<p>Is specifying the inputs takes time or the automatic computation? How long do they take?</p>
<aside class="quote no-group" data-username="rbumm" data-post="1" data-topic="19674">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Airway segmentation results are quite good</p>
</blockquote>
</aside>
<p>How does the segmentation result quality compare with what you can get with Grow from seeds, Local threshold, Fast marching, Flood filling, and Watershed?</p>

---

## Post #3 by @rbumm (2021-09-15 06:48 UTC)

<p>Specifying the inputs is the easy part, it just needs one seed in the trachea, which I usually already have.</p>
<p>A CIP airway segmentation takes around 140 s to complete.<br>
The results are often acceptable, but sometimes important bronchi are just missed (like B2 right in this case of the public COV dataset).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5a9b6ebf8073da1a38552ad47312baf5d40d98c.jpeg" data-download-href="/uploads/short-url/pV426cGXmkzcusa29LWW8Na5QGU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5a9b6ebf8073da1a38552ad47312baf5d40d98c_2_690x336.jpeg" alt="image" data-base62-sha1="pV426cGXmkzcusa29LWW8Na5QGU" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5a9b6ebf8073da1a38552ad47312baf5d40d98c_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5a9b6ebf8073da1a38552ad47312baf5d40d98c_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b5a9b6ebf8073da1a38552ad47312baf5d40d98c_2_1380x672.jpeg 2x" data-dominant-color="BFBFC5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×936 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With kernel type B70f I get the best results concerning leaks.<br>
It would be important to have an option to place additional seeds in bronchi that are missed.</p>
<blockquote>
<blockquote>
<p>How does the segmentation result quality compare with what you can get with Grow from seeds, &gt;&gt;Local threshold, Fast marching, Flood filling, and Watershed?</p>
</blockquote>
</blockquote>
<p>The results are only slightly better and require more manual input.</p>

---

## Post #4 by @rbumm (2021-09-15 07:51 UTC)

<p>An closer look at the missed bronchi:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2d78ee1d7934743b407462d092ec76055edac46.jpeg" data-download-href="/uploads/short-url/yEhnuX3DCodKtY1llXlKwIturTE.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2d78ee1d7934743b407462d092ec76055edac46_2_649x500.jpeg" alt="image" data-base62-sha1="yEhnuX3DCodKtY1llXlKwIturTE" width="649" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2d78ee1d7934743b407462d092ec76055edac46_2_649x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2d78ee1d7934743b407462d092ec76055edac46.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2d78ee1d7934743b407462d092ec76055edac46.jpeg 2x" data-dominant-color="99999A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">723×557 69.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @rbumm (2021-09-15 15:46 UTC)

<p>HU’s of parenchyma and bronchi in the above CT are almost identical and this kind of segmentation is certainly a difficult task. However, detailed subsegmental bronchi as shown in this older video</p>
<div class="youtube-onebox lazy-video-container" data-video-id="mcGqcxU5qBE" data-video-title="Airway Segmentation Tutorial" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=mcGqcxU5qBE" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/mcGqcxU5qBE/maxresdefault.jpg" title="Airway Segmentation Tutorial" width="" height="">
  </a>
</div>

<p>can hardly be obtained with the current CIP and the three kernel options - as long as I am not missing something here. At least, this kind of detail would be sufficient for clinical use. The video also shows that an earlier version had a direct 3D display of the created labelmap, which is a nice feature.</p>

---

## Post #6 by @lassoan (2021-09-15 18:23 UTC)

<p>I’ve checked the <a href="https://github.com/acil-bwh/ChestImagingPlatform/blob/develop/CommandLineTools/SegmentLungAirways/SegmentLungAirways.cxx">source code of Segment Lung Airways module</a> and it is shockingly complicated. This is the kind of algorithm that is developed with a lot of manual effort by adding more and more rules to handle all kinds of situations that are encountered during testing on various data sets. It should provide better results than simple generic methods (such as Grow from seeds, Fast marching, etc.), but as more and more rules are added, the more complicated and slower the algorithm becomes.</p>
<p>In theory, you could go through the code, understand it, and improve it, for example by adding more rules or inject more user inputs (e.g., seed points) into it. However, you are probably much better off with training a neural network for this, because it is a relatively simple problem, you have tons of images to train on. To generate ground truth segmentation, you can use the current airway segmentation module, but review and fix all the errors manually. Once you have segmented a few dozen data sets, you may be able to use <a href="https://github.com/Project-MONAI/MONAILabel#monai-label">MONAILabel</a> to do the rest.</p>
<p>If you are not ready to jump into deep learning and/or performance of the current airway segmenter module is sufficient, then you can simply add an option in your lung segmenter module to call this module. If ChestImagingPlatform is not installed then you can show a popup asking the user to confirm installation of the extension (see how to install an extension from Python scripting <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#download-and-install-extension">here</a>).</p>

---

## Post #7 by @rbumm (2021-09-16 06:25 UTC)

<p>Thanks for sharing the link to the sources, just did not find it.<br>
I will probably implement an option to use the CIP airway segmenter first, try to understand workflow and parameters, but will have MONAILabel on the screen, too.</p>

---

## Post #8 by @rbumm (2021-09-16 11:52 UTC)

<p>If I use MONAIlabel here, will a user have to start its server or install anything complicated?<br>
I want to make this as user-friendly as possible.</p>
<p>The MONAILabel approach would probably have the benefit that it could be combined with the right and left lung detection.</p>

---

## Post #9 by @lassoan (2021-09-16 13:55 UTC)

<p>MONAILabel is currently optimized for people who want to train their own models. It requires a few setup steps (although it could be automated in a Python scripted module) and - depending on the model - it may require the user to have a good GPU.</p>
<p>If you want to make things as simple for users as possible, don’t require GPU and any setup, then you can upload the model to an NVidia Clara server (such as the public Slicer segmentation server) and let users do the segmentation using the <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#readme">NVidia AIAA segment editor effect</a>.</p>

---

## Post #10 by @rbumm (2021-09-17 13:12 UTC)

<p>As a first step, I implemented the CIP airway segmenter CLI call into the LungCTSegmenter, which works great.<br>
This is nearly ready. Before I can make this commit, I would need to know how to switch the visibility of a labelmap off in a python script. And how to switch visibility of a CT volume on.<br>
I know how to do this for segmentations using the displaynode and Visibility2DOn(), but the day begins to be very ineffective seaching the net how to do that with a labelmap or a CT volume. Probably   <a class="mention" href="/u/lassoan">@lassoan</a> you know it by heart.</p>
<p>This</p>
<pre><code class="lang-auto">scalarVolumeDisplayNode = self.labelmapVolumeNode.GetScalarVolumeDisplayNode()
scalarVolumeDisplayNode.VisibilityOff()
</code></pre>
<p>does not work. The problem is not related to airway segmentation, where I am delete the created labelmap after conversion into a segmentation, but for the Parenchyma Analysis labelmap which the segmenter builds.</p>
<p>It  is the last detail I need to implement, then I would commit and push the segmenter.</p>
<p>Will evaluate AI airway segmentation as well. From all MONAILabel examples I saw until now, the segmentations looked somewhat bulky, the vessels very tubular, but I would need to test all this before I can really judge.</p>

---

## Post #11 by @rbumm (2021-09-17 13:22 UTC)

<p>Test result, lung mask generation and airway segmentation combined (1 start click, 13 fiducial clicks, 1 checkbox click, one apply click, 203 sec processing on a gaming laptop, CT: from open source COV dataset) :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28e5d5ba4d93396dbc60723e333d9498f1604d7d.jpeg" data-download-href="/uploads/short-url/5PNw6hMqh7gY003YbcXEdij4e97.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28e5d5ba4d93396dbc60723e333d9498f1604d7d_2_690x453.jpeg" alt="image" data-base62-sha1="5PNw6hMqh7gY003YbcXEdij4e97" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28e5d5ba4d93396dbc60723e333d9498f1604d7d_2_690x453.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28e5d5ba4d93396dbc60723e333d9498f1604d7d_2_1035x679.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28e5d5ba4d93396dbc60723e333d9498f1604d7d.jpeg 2x" data-dominant-color="767777"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1230×809 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @lassoan (2021-09-17 13:28 UTC)

<p>Labelmaps can only be displayed in 3D using volume rendering, which has many limitations (this was one of the main motivation for the development of the segmentation infrastructure). You can only render a single labelmap layer in a view. You cannot edit/touch-up labelmaps directly. I could list many more limitations of labelmaps compared to segmentations but even these should be enough that justify using segmentations instead.</p>
<p>I would recommend to import the computed labelmap to segmentation node and delete the labelmap node.</p>

---

## Post #13 by @rbumm (2021-09-17 13:30 UTC)

<p>Done that, it is what you see in the example above, the problem is not related to that.</p>
<p>It is related to the labelmap I still generate for Parenchyma analysis, I just want to switch that labelmap display off in 2D and 3D. And the CT volume display on again.</p>

---

## Post #14 by @lassoan (2021-09-17 13:39 UTC)

<p>Haven’t you implemented segmentation support for Parenchyma analysis, so that it takes segmentation directly? In Parenchyma analysis you can delete the temporary labelmap volume after the analysis is completed.</p>

---

## Post #15 by @rbumm (2021-09-17 13:44 UTC)

<p>Yes, but this PR is still open. But this is a good idea. I will just assume that it is merged and remove the labelmap generation in segmenter ? And I will try to remove the temp labelmap in Parenchyma Analysis. Tried that before, there was an error message coming up, will need to analyze that.</p>

---

## Post #16 by @lassoan (2021-09-17 13:54 UTC)

<p>We can always switch to a temporarily forked version of CIP extension to get your changes in Slicer quickly, and then switch back to the official version when your changes got merged.</p>

---

## Post #17 by @rbumm (2021-09-18 19:27 UTC)

<p>I committed the CLI call to CIP airway segmentation, removed the CIP Parenchyma Analysis labelmap generation as you suggested, and incremented the version to 2.45. Pushed this to LungCTAnalyzer. The LCTA WIKI will be updated accordingly.</p>

---
