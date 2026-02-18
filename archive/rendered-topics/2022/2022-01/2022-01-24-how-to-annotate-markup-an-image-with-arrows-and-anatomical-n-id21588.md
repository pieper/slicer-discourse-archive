# How to annotate/markup an image with arrows and anatomical names

**Topic ID**: 21588
**Date**: 2022-01-24
**URL**: https://discourse.slicer.org/t/how-to-annotate-markup-an-image-with-arrows-and-anatomical-names/21588

---

## Post #1 by @Young_Wang (2022-01-24 02:47 UTC)

<p>Operating system: MacOS Monterey 12.1(21C52)<br>
Slicer version:3D Slicer 4.11.2021026<br>
Expected behavior:<br>
Actual behavior:<br>
Please see the example shown here. Maybe this is an easy thing to be but I have yet found anything useful when searching the keywords “annotation, markup”<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a3412a4897a89c9d593f9401efd5f27b3c8a28d.jpeg" data-download-href="/uploads/short-url/cRYxluAau7JHAxdAbd2WuN3RaHj.jpeg?dl=1" title="Screen Shot 2022-01-23 at 3.00.48 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a3412a4897a89c9d593f9401efd5f27b3c8a28d_2_690x361.jpeg" alt="Screen Shot 2022-01-23 at 3.00.48 PM" data-base62-sha1="cRYxluAau7JHAxdAbd2WuN3RaHj" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a3412a4897a89c9d593f9401efd5f27b3c8a28d_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a3412a4897a89c9d593f9401efd5f27b3c8a28d_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a3412a4897a89c9d593f9401efd5f27b3c8a28d_2_1380x722.jpeg 2x" data-dominant-color="5E5B4C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-01-23 at 3.00.48 PM</span><span class="informations">1920×1006 90.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Juicy (2022-01-25 07:51 UTC)

<p>I am not sure of a way to do this in 3D Slicer. To make an image like this of a single slice I would just make a screen shot and use Paint or MS Word to make the annotations. Sorry, not sure how useful this suggestion is but no one else had replied.</p>

---

## Post #3 by @hherhold (2022-01-25 12:52 UTC)

<p>I’m not sure what program is shown in your image, or if it’s interactive. For publication plates, I use the screen capture module or just a direct screen grab from slicer, then annotate in Illustrator. Word/Paint work as well, as <a class="mention" href="/u/juicy">@Juicy</a> mentioned. For images that need high resolution for large prints, I’ll export PLY (or OBJ) format models and use Blender to render out publication prints at whatever resolution (DPI) I need, then annotate in Illustrator.</p>

---

## Post #4 by @Young_Wang (2022-01-25 14:26 UTC)

<p>Hi <a class="mention" href="/u/hherhold">@hherhold</a> <a class="mention" href="/u/juicy">@Juicy</a>, thank you so much for replying to my post. This screenshot is from <a href="http://uwmsk.org/temporalbone/images/normal/axial/axial.html" class="inline-onebox" rel="noopener nofollow ugc">Interactive Atlas: Axial</a> and I often see annotated images for publication, education and training purposes. I personally find it is very helpful to have a way to mark up images directly. For example, with Horos, another DICOM reviewer, one can annotate on the DICOM images directly. I wonder if the slicer development team can add this as a new feature. I program primarily in python but I am happy to contribute if it’s deemed to be useful for others.</p>

---

## Post #5 by @hherhold (2022-01-25 14:32 UTC)

<p>That’s a nice interface. Looks like they have pre-annotated every slice so that it will add labels to any clicked position.</p>
<p>I’ve used Horos before (though it’s been a while) but not the annotation tools. Slicer allows annotation of points/measurements/etc using the Markups module, but that does not include lines, or lines with arrows. For my purposes, I find the rasterization of text and markups to be of too low resolution for publication-quality plates and figures, so that’s why I use Illustrator. But for websites, etc I can see how this would be useful.</p>

---

## Post #6 by @muratmaga (2022-01-25 17:44 UTC)

<aside class="quote no-group" data-username="Young_Wang" data-post="1" data-topic="21588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>Please see the example shown here. Maybe this is an easy thing to be but I have yet found anything useful when searching the keywords “annotation, markup”</p>
</blockquote>
</aside>
<p>You can use a combination of point and line markups to create these within Slicer. For example below CC is rendered as a point with the glyph hidden (Corpus callosum is the label of the point). And yellow is a line markup with both control points hidden. However, as others commented out, it is easier to do those things in powerpoint or illustrator or inkscape where you can decorate your shapes to your hearts content.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2853ff389329197161df5f35545c1e84a1464b61.png" data-download-href="/uploads/short-url/5KL3OhDvCZmhsL5mQ3pDbbLNED7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2853ff389329197161df5f35545c1e84a1464b61.png" alt="image" data-base62-sha1="5KL3OhDvCZmhsL5mQ3pDbbLNED7" width="527" height="500" data-dominant-color="4D4D4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1109×1051 95.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Young_Wang (2022-01-25 22:08 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Thank you so much for your example and explanation. I really appreciate how responsive the slicer community is.</p>

---

## Post #8 by @stevenagl12 (2022-01-26 12:54 UTC)

<p>Is it possible for 3D Slicer to just get a text option for the markups module? It would be nice to be able to create a text box and add in the necessary information/make the text box disappear. This way you don’t need to add in a point when performing this type of action, and you can do things like label a slice such as what is done when taking the distance to bregma, etc.?</p>

---

## Post #9 by @Young_Wang (2022-01-26 12:58 UTC)

<p><a class="mention" href="/u/stevenagl12">@stevenagl12</a> That would be a handy feature for sure. For someone who recently starts learning anatomy, it could help me keep track of the anatomical features I identified and can be reviewed by others for a sanity check.</p>

---

## Post #10 by @hherhold (2022-01-26 13:06 UTC)

<p>You can actually kinda do that now. In the Markups module, you can make a new point list and add points wherever you like. Then go to Display in the Markups module, and set glyph size to zero. The text will stay, and you can change size, color, drop shadow, etc.</p>
<p>I label anatomical features all the time with markups using the glyph as a sphere to denote where things are, but you can remove the glyph if you want, or change it to a different shape.</p>

---

## Post #11 by @Young_Wang (2022-01-26 13:14 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a> perfect. Thank you for the detailed response. May I ask does this feature also provide arrows?</p>

---

## Post #12 by @hherhold (2022-01-26 13:18 UTC)

<p>No, if you want lines with end shapes, etc you need to add those to an exported image with something like paint or illustrator.</p>

---

## Post #13 by @muratmaga (2022-01-26 16:36 UTC)

<aside class="quote no-group" data-username="Young_Wang" data-post="9" data-topic="21588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/young_wang/48/13926_2.png" class="avatar"> Young_Wang:</div>
<blockquote>
<p>That would be a handy feature for sure</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/stevenagl12">@stevenagl12</a>  <a class="mention" href="/u/young_wang">@Young_Wang</a><br>
It would be handy, particularly if the textbox feature has more decoration options than the existing point label ones. However it is a too specific feature and existing functionality provides the minimum features to provide to fulfill this need. If someone needing this can take on implementing textbox feature or the arrows to cap the line markup that will be great.</p>

---

## Post #14 by @lassoan (2022-01-27 00:52 UTC)

<p>Most medical image viewers just allow labeling points with callout titles <strong>in a single 2D view</strong>. This functionality is available in Slicer, too, via the “line” markup. It could be made look prettier and more convenient, for example by adding an “arrow” markup that would use an oriented arrow as endpoint glyph; and the label would be displayed at the starting point by default. Contributions are welcome!</p>
<p>However, manual label and arrow endpoint positioning does not work at all <strong>in 3D</strong>: neither in 3D views nor in slice views with different orientations. The issue is that the optimal label position (or the decision if a label should be displayed at all) and arrow endpoint position depend on the view direction and on what else is visible in that view and where; and the end result should look esthetically pleasing and balanced, labels should not overlap each other and be displayed in less “busy” parts of the image, but they should be displayed closed to the arrow endpoint, etc. This is of course not feasible to do manually each time a view is rotated, therefore it has to be automated. But it is very difficult to implement an automatic optimization method for it. This is probably why callout title feature is very rarely (if ever) implemented in 3D. This feature is missing from even the most sophisticated 3D modeling software. Instead, callout titles are added using 2D drawing tools or post-processing software (such as Adobe After Effects).</p>
<p>Nevertheless, 3D callout titles could be implemented in Slicer in some way. It could not be a markup feature, because a target point position would not be sufficient input; but each label would need to be assigned to a displayable 3D object, such as a model or a segment. An algorithm could determine which parts of which objects are visible and where, maybe also identify uniform (less busy) regions in the image, then arrange labels in a way that the labels don’t overlap each other, not near busy image regions, and the leading lines are as short as possible and do not cross each other. Feasible for sure, but quite complex task.</p>

---

## Post #15 by @rbumm (2022-01-27 13:34 UTC)

<p>Great that you bring this up again, should definitely be realized. Can we not just make the label position and “outfit” of a fiducial more flexible (distance, text box)?</p>

---

## Post #16 by @Young_Wang (2022-01-27 14:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Dr. Lasso, thank you for your detailed response. I tend to contribute and try to implement this feature collaboratively with others. If you could point me to a starting point it would be much appreciated. I totally agree that 2D annotation/markup makes most of the sense and 3D callout could easily be done with other post-processing software.</p>

---

## Post #17 by @lassoan (2022-01-27 16:25 UTC)

<p>Are you thinking about implementing a new “arrow” markup type? Do you have C++ development experience?</p>

---

## Post #18 by @Young_Wang (2022-01-27 16:49 UTC)

<p>Yep. I know python fairly well but new to C++</p>

---

## Post #19 by @muratmaga (2022-01-27 16:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="21588" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are you thinking about implementing a new “arrow” markup type? Do you have C++ development experience?</p>
</blockquote>
</aside>
<p>Do we really need a new type? Can’t the existing line type revised to turn control points glyphs to capping arrows?</p>

---

## Post #20 by @lassoan (2022-01-27 19:31 UTC)

<p>The new type would be added for user convenience. It would allow us to set up different defaults for “arrow” markups and “line” markups. For arrows the defaults would be no glyph at start point, oriented arrow glyph at end point, don’t show length measurement, etc.</p>
<p>Either way, we should probably start with adding a new <code>GlyphOrientationMode</code> property to the to the <code>vtkMRMLMarkupsDisplayNode</code> class. This would control if we want to orient the glyph. Possible modesl:</p>
<ul>
<li>always upright and facing the viewer: this is the current orientation mode</li>
<li>use orientation of the markup’s “axis”: each markup could decide how to interpret this, but for a line it would mean something like direction vector of the line, pointing outwards</li>
<li>use the orientation that is stored in the control point: we already store an orientation for each control point, so we could use that for this purpose; I think we currently set it to be the normal of the surface where the point is defined on</li>
</ul>
<p>The oriented arrow could be implemented either using the second or third mode, so we don’t need to implement both.</p>
<p><a class="mention" href="/u/young_wang">@Young_Wang</a> Markups display - as well as all essential infrastructure in Slicer core - is implemented in C++ for performance and robustness. If you are ready to dig in then the first task is to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/index.html">build Slicer</a>. Give it a try and let us know if you need any help or you are ready for the next steps.</p>

---

## Post #21 by @rbumm (2022-02-07 13:16 UTC)

<p>This is a 2D working demo of enhancing the normal fiducial markup with a connector line:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1755dc1c3ac03fe0ac41599d9f72623359ddcaa.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1755dc1c3ac03fe0ac41599d9f72623359ddcaa.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1755dc1c3ac03fe0ac41599d9f72623359ddcaa.mp4</a>
    </source></video>
  </div><p></p>
<p>It could be made optional via a checkbox in the markup widget “Display” section to have that line on or off.</p>

---

## Post #22 by @Young_Wang (2022-02-07 13:38 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a>, Thank you so much for implementing this. I really like this feature, I think it’s both visually pleasing and functional. I also think the optional check box would be a great idea for those who are finding this feature too busy on the images. May I ask when can I find this feature in the released 3Dslicers? I was attempting to implement it but I haven’t found time to get this yet. Really appreciate your hard work.</p>

---

## Post #23 by @rbumm (2022-02-07 14:00 UTC)

<p>Dear <a class="mention" href="/u/young_wang">@Young_Wang</a> , I was glad that you brought this up again and dug into the code to find the entry point for that connector line. This is only a demo - the Slicer developer team members could comment. I still have several unsolved technical details in that implementation. But I agree that a connector line option would be really helpful and they are fun to place.  Technically, a pull request to <a href="https://github.com/Slicer/Slicer" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer</a> will follow, and only if the PR gets accepted this would be available in the Slicer preview release.</p>

---

## Post #24 by @lassoan (2022-02-07 19:01 UTC)

<p>Allowing display of labels at a certain distance from the control points, always shifted outwards in radial direction could be a nice and simple automatic line routing method, which could work well for many cases. So, it would be great if you could experiment with it a bit more.</p>
<p>There are issues, such as what to do control points that are close to the bounds of the view (the point would still be visible, but the label would be moved out of the view), or how to deal with overlap between labels, but it is hard to tell how much these impact practical usability without actually implementing and trying it.</p>

---

## Post #25 by @muratmaga (2022-02-07 19:19 UTC)

<aside class="quote no-group quote-modified" data-username="rbumm" data-post="23" data-topic="21588" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Dear <a class="mention" href="/u/young_wang">@Young_Wang</a> , I was glad that you brought this up again and dug into the code to find the entry point for that connector line. This is only a demo - the Slicer developer team members could comment. I still have several unsolved technical details in that implementation. But I agree that a connector line option would be really helpful and they are fun to place. Technically, a pull request to <a href="https://github.com/Slicer/Slicer" class="inline-onebox">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a> will follow, and only if the PR gets accepted this would be available in the Slicer preview release.</p>
</blockquote>
</aside>
<p>In the video, it appears you are creating each label as a separate pointList object (as opposed keeping them as control points within the object). Is that the intended use ?</p>

---

## Post #26 by @rbumm (2022-02-07 19:35 UTC)

<p>No, it is intended to work also if you “place multiple control points” of one pointList. But currently, this part is not functional <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #27 by @lassoan (2022-02-07 23:18 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> The implementation could be something like:</p>
<ul>
<li>add leading line length (and other display parameters, if needed) in the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRML/vtkMRMLMarkupsDisplayNode.h">markups display node</a>
</li>
<li>add an additional line actor for each control point that shifts the label and connects it to the control points in the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRMLDM/vtkMRMLMarkupsDisplayableManager.cxx">markups displayable manager</a>
</li>
</ul>

---

## Post #29 by @rbumm (2022-02-08 12:39 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="27" data-topic="21588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>add an additional line actor for each control point that shifts the label and connects it to the control points in the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/MRMLDM/vtkMRMLMarkupsDisplayableManager.cxx">markups displayable manager </a></p>
</blockquote>
</aside>
<p>I got the demo running by adding the label line actor in <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/VTKWidgets/vtkSlicerMarkupsWidgetRepresentation2D.cxx">markups widget representation 2D</a> - I see other actors being added here - would not this be the right place?</p>

---

## Post #30 by @lassoan (2022-02-08 14:40 UTC)

<p>The displayable manager is responsible for displaying the widgets, but it delegates the details to VTK widgets. So, your change in 2D widget representation was correct. The same label offset approach should work for the 3D representation, too.</p>
<p>If we want to avoid overlapping labels between all the widgets then some coordination between widgets at the displayable manager level may be necessary (or even among all displayable managers), but first let’s see how far we can get with this simpler radial label offset strategy.</p>

---

## Post #31 by @rbumm (2022-03-18 19:17 UTC)

<p>I have been working on this in recent weeks and came quite far by adding a connector line visibility checkbox and a relative line size slider. Loading and saving the line-related information and display of the line connectors in 2D and 3D view. This is under review now but expect it to be available soon.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/547742df90fd380bfeba15500546f9bcd22b4c9d.jpeg" data-download-href="/uploads/short-url/c3dCEMdTbO9djJyllbwRaCU7Sy1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/547742df90fd380bfeba15500546f9bcd22b4c9d_2_690x298.jpeg" alt="image" data-base62-sha1="c3dCEMdTbO9djJyllbwRaCU7Sy1" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/547742df90fd380bfeba15500546f9bcd22b4c9d_2_690x298.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/547742df90fd380bfeba15500546f9bcd22b4c9d_2_1035x447.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/547742df90fd380bfeba15500546f9bcd22b4c9d_2_1380x596.jpeg 2x" data-dominant-color="828388"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×830 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #32 by @Young_Wang (2022-03-22 12:42 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> this is absolutely awesome</p>

---

## Post #33 by @rbumm (2022-04-03 19:25 UTC)

<p>LabelConnectorLineColor can now be set. loaded, stored</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a75d9c6e8e8a1ee933ca3bd472ff7edc885418a3.jpeg" data-download-href="/uploads/short-url/nSAiuOQ5b4NWJJ6PqpDo1JKYqn9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a75d9c6e8e8a1ee933ca3bd472ff7edc885418a3_2_690x257.jpeg" alt="image" data-base62-sha1="nSAiuOQ5b4NWJJ6PqpDo1JKYqn9" width="690" height="257" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a75d9c6e8e8a1ee933ca3bd472ff7edc885418a3_2_690x257.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a75d9c6e8e8a1ee933ca3bd472ff7edc885418a3_2_1035x385.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a75d9c6e8e8a1ee933ca3bd472ff7edc885418a3_2_1380x514.jpeg 2x" data-dominant-color="7C7E83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1913×713 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #34 by @muratmaga (2022-04-04 17:21 UTC)

<p>This is awesome. Is it still experimental or already incorporated to the preview version?</p>

---

## Post #35 by @rbumm (2022-04-04 19:04 UTC)

<p>Thank you. It is not yet included in preview.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6188#issuecomment-1087812490">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6188#issuecomment-1087812490" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/6188" target="_blank" rel="noopener">ENH: Add connector line for fiducial markup label texts</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>rbumm:Branch_markuplabeltexts</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-02-14" data-time="18:44:06" data-timezone="UTC">06:44PM - 14 Feb 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/rbumm" target="_blank" rel="noopener">
          <img alt="rbumm" src="https://avatars.githubusercontent.com/u/18140094?v=4" class="onebox-avatar-inline" width="20" height="20">
          rbumm
        </a>
      </div>

      <div class="lines" title="1 commits changed 11 files with 888 additions and 326 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/6188/files" target="_blank" rel="noopener">
          <span class="added">+888</span>
          <span class="removed">-326</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Label text offsets and a connector line (as in anatomy books)  would be awesome <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6188" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">to have when labeling anatomical structures. 

 This is an implementation of label text connector lines for fiducial markups. 

![](https://user-images.githubusercontent.com/18140094/153926721-1eb54057-fbe7-49cb-a54a-bd8c779b68a3.png)

Please see the comments for questions. Thank you.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #36 by @rbumm (2022-08-01 17:59 UTC)

<p>ping <a class="mention" href="/u/chir.set">@chir.set</a></p>
<p>I have been working on a similar annotation project <a href="https://github.com/chir-set/ExtraMarkups/tree/main/Label/">like yours</a> earlier this year. All was started in this thread.  As I  suppose you are interested, we could probably revive this PR</p>

---

## Post #37 by @chir.set (2022-08-01 19:06 UTC)

<p>I see that your work is quite mature and just needs to be merged in Slicer. I hope this gets done soon, after which, mine would become moot and removed. For me, it has been a good and enriching experiment. You may of course borrow any feature you may find useful from it. Looking forward to use your implement in Slicer directly.</p>

---

## Post #38 by @Young_Wang (2022-10-05 23:21 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> thank you for making it possible</p>

---

## Post #39 by @Piergiorgio_Gaudioso (2023-12-05 13:49 UTC)

<p>What about exporting annotations/markups/segmentation in a DICOM file integrated with an MRI image? Is it possible? Could you provide a tutorial?</p>

---

## Post #40 by @rbumm (2023-12-05 14:45 UTC)

<p>Unfortunately, the annotations with connector lines have not been implemented in the Slicer source code yet.<br>
<a class="mention" href="/u/chir.set">@chir.set</a> has made an extension that has similar functionality, maybe you could try that …</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/chir-set/SlicerExtraMarkups">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/chir-set/SlicerExtraMarkups" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/81ca4b509ef45aa3ed1cd0227128d213b9f1f47974b7db253031986227b6ceac/chir-set/SlicerExtraMarkups" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/chir-set/SlicerExtraMarkups" target="_blank" rel="noopener">GitHub - chir-set/SlicerExtraMarkups: Custom markups for Slicer</a></h3>

  <p>Custom markups for Slicer. Contribute to chir-set/SlicerExtraMarkups development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #41 by @Piergiorgio_Gaudioso (2023-12-05 15:00 UTC)

<p>THank you for the information. Is it possible to export a DICOM file with those markups?</p>

---

## Post #42 by @rbumm (2023-12-05 15:16 UTC)

<p>Not with the ExtraMarkups, I dont think that is possible.<br>
Annotations, markups, and segmentation can be exported into DICOM format.</p>

---

## Post #43 by @chir.set (2023-12-05 15:20 UTC)

<aside class="quote no-group" data-username="Piergiorgio_Gaudioso" data-post="41" data-topic="21588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/piergiorgio_gaudioso/48/68592_2.png" class="avatar"> Piergiorgio_Gaudioso:</div>
<blockquote>
<p>Is it possible to export a DICOM file with those markups?</p>
</blockquote>
</aside>
<p>To my knowledge, no.</p>
<p>DICOM image data, metadata and markups nodes are different objects,  represented differently in memory, and stored differently on disk. They cannot be blended in a single file. If you want to keep these together, you may save your scene as an *.mrb file and share  or archive it.</p>

---

## Post #44 by @Piergiorgio_Gaudioso (2023-12-05 16:03 UTC)

<p>And this “.mrb” file can be visualized in a DICOM viewer? How can I save in this way?</p>

---

## Post #45 by @chir.set (2023-12-05 16:18 UTC)

<aside class="quote no-group" data-username="Piergiorgio_Gaudioso" data-post="44" data-topic="21588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/piergiorgio_gaudioso/48/68592_2.png" class="avatar"> Piergiorgio_Gaudioso:</div>
<blockquote>
<p>And this “.mrb” file can be visualized in a DICOM viewer?</p>
</blockquote>
</aside>
<p>If you mean <em>another</em> DICOM viewer, no. The <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#scenes" rel="noopener nofollow ugc">MRB</a> file does not even contain DICOM files, these are saved in NRRD format. It has meaning within Slicer only.</p>
<aside class="quote no-group" data-username="Piergiorgio_Gaudioso" data-post="44" data-topic="21588">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/piergiorgio_gaudioso/48/68592_2.png" class="avatar"> Piergiorgio_Gaudioso:</div>
<blockquote>
<p>How can I save in this way?</p>
</blockquote>
</aside>
<p>Check the <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" rel="noopener nofollow ugc">documentation</a>.</p>

---
