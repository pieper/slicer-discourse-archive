# Constraining flood fill to size brushsize

**Topic ID**: 9146
**Date**: 2019-11-14
**URL**: https://discourse.slicer.org/t/constraining-flood-fill-to-size-brushsize/9146

---

## Post #1 by @Leon (2019-11-14 11:11 UTC)

<p>Yesterday I came across this video (<a href="https://www.youtube.com/watch?v=HdTKZKumw8o" rel="nofollow noopener">https://www.youtube.com/watch?v=HdTKZKumw8o</a>) from the people of Itkgray (<a href="https://web.stanford.edu/group/vista/cgi-bin/wiki/index.php/ItkGray" rel="nofollow noopener">https://web.stanford.edu/group/vista/cgi-bin/wiki/index.php/ItkGray</a>). It’s a  branch of ItkSnap.</p>
<p>Here you see them using the paintbrush with a ‘Floodfill’ setting for segmenting the white matter of the brain.</p>
<ul>
<li>Set the active drawing label to ‘white’ with the correct hemisphere.</li>
<li>Use the <strong>Paintbrush tool</strong> to fill in most of the white matter and the ventricles.<br>
The axial view works well for this; using <strong>Floodfill</strong> with the <strong>3D brush on</strong> at a tolerance of ~5 and/or the <strong>square</strong> and <strong>round brush.</strong>
</li>
<li>It may help to start dorsally and work down, cleaning up the subcortical areas as you progress.</li>
</ul>
<p><a href="https://web.stanford.edu/group/vista/cgi-bin/wiki/index.php/File:Segment_coarse1.png" rel="nofollow noopener"><img src="https://web.stanford.edu/group/vista/wikiupload/thumb/d/dd/Segment_coarse1.png/250px-Segment_coarse1.png" alt width="250" height="209"></a></p>
<p><a href="https://web.stanford.edu/group/vista/cgi-bin/wiki/index.php/File:Segment_coarse1.png" rel="nofollow noopener"><img src="https://www.stanford.edu/dept/its/includes/mediawiki-1.16.5/skins/common/images/magnify-clip.png" alt width="15" height="11"></a></p>
<p>I was wondering if this option is also available in Slicer? I haven’t found it (yet) and from what I noticed, it now only works on the entire 3D-image and you can’t contain it to only a brushsize or other volume.</p>
<p>Or is there maybe a workaround for this? My idea would be to do a coarse, completely filled segmentation with for instance the ‘Fill between slices’ option and then use the ‘Flood filling’, constrained to the coarse segmentation.</p>
<p>Any other suggestions?</p>

---

## Post #2 by @lassoan (2019-11-14 14:01 UTC)

<aside class="quote no-group" data-username="Leon" data-post="1" data-topic="9146">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>‘Fill between slices’ option and then use the ‘Flood filling’, constrained to the coarse segmentation.</p>
</blockquote>
</aside>
<p>You are very lucky. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> have just added yesterday (rev 28613) a new effect “Local threshold” Segment Editor effect (via SegmentEditorExtraEffects extension) that does this. It computes an intensity range from a small region that you draw on the image, then you Ctrl-click at the position you want to fill around. You can choose between various fill strategies (flood fill, grow from seeds, watershed) and it works quite robustly in 3D.</p>

---

## Post #3 by @Leon (2019-11-14 15:19 UTC)

<p>Great work! Lucky me!</p>

---
