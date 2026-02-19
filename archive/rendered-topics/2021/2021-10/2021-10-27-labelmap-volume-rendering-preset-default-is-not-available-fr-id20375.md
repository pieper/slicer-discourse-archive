---
topic_id: 20375
title: "Labelmap Volume Rendering Preset Default Is Not Available Fr"
date: 2021-10-27
url: https://discourse.slicer.org/t/20375
---

# Labelmap volume rendering preset (default) is not available from preset dropdown

**Topic ID**: 20375
**Date**: 2021-10-27
**URL**: https://discourse.slicer.org/t/labelmap-volume-rendering-preset-default-is-not-available-from-preset-dropdown/20375

---

## Post #1 by @DIV (2021-10-27 04:05 UTC)

<p>If I create a volume from the <strong>Simple Region Growing Segmentation</strong>  module, then I suppose it is a binary labelmap.<br>
It can be viewed in 3D through the <strong>Volume Rendering</strong> module.  By default this comes up with a kind of colourmap of repeating rainbow stripes (I am not sure if this has a formal name in Slicer), as seen in the <em>Advanced</em> panel.  Choosing a different volume-rendering Preset from the drop-down list in the <em>Display</em> panel is possible.  However, after doing so I didn’t see an obvious way to subsequently choose the original rainbow-stripe preset.<br>
Is there a convenient way to choose the rainbow-stripe preset later on?<br>
Either way, should this be added to the standard drop-down list of volume-rendering presets?<br>
—DIV</p>

---

## Post #2 by @muratmaga (2021-10-27 04:42 UTC)

<p>Segmentations are not immediately visible via volume rendering, you need to export them as label maps from Segmentation module. See this diagram for data type relationships in Slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/361e152f1f6d00e6f91da5a1cbc822a5ccea6f37.jpeg" data-download-href="/uploads/short-url/7IKeAShVgDn2Cu3GZXvGpAOBPrF.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/361e152f1f6d00e6f91da5a1cbc822a5ccea6f37_2_690x368.jpeg" alt="image" data-base62-sha1="7IKeAShVgDn2Cu3GZXvGpAOBPrF" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/361e152f1f6d00e6f91da5a1cbc822a5ccea6f37_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/361e152f1f6d00e6f91da5a1cbc822a5ccea6f37_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/361e152f1f6d00e6f91da5a1cbc822a5ccea6f37_2_1380x736.jpeg 2x" data-dominant-color="D9DFD7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1756×937 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I am not sure what repeating rainbow stripes pattern is. Normally labelmaps are displayed loaded with the Generic label lookup table. (It would be good if you can add a screenshot to your descriptions, to make sure we are on the same page).</p>
<p>Those volume rendering presets are not for labelmaps, but volumes that has continuous image intensities. I don’t think they will perform well for discrete labelmaps. If you want, you can choose the box that says “Synchronize with Volumes module” and choose the “Label” lookup table from volume module (or any other lookup table that makes sense for labelmaps).</p>

---

## Post #3 by @DIV (2021-10-27 05:45 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="20375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I am not sure what repeating rainbow stripes pattern is.</p>
</blockquote>
</aside>
<p>The multicoloured/rainbow stripes pattern seems to be the <code>Labels</code> Lookup Table, when comparing to the <em>Display</em> panel in the <strong>Volumes</strong> module.  On this basis I have just managed to get it back as a volume rendering setting by clicking the <code>Synchronize with Volumes module</code> tick-box in the <strong>Volume Rendering</strong> module.<br>
—DIV</p>

---

## Post #4 by @DIV (2021-10-27 06:21 UTC)

<p>Hello, muratmaga.<br>
Thank-you for your suggestions.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="20375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Those volume rendering presets are not for labelmaps, but volumes that has continuous image intensities. I don’t think they will perform well for discrete labelmaps. If you want, you can choose the box that says “Synchronize with Volumes module” and choose the “Label” lookup table from volume module (or any other lookup table that makes sense for labelmaps).</p>
</blockquote>
</aside>
<p>I guess you’re right, but the output of the <strong>Simple Region Growing Segmentation</strong> module is called a “Volume”, and it seems to show up as a kind of “Volume” in the <strong>Data</strong>, <strong>Volumes</strong> and <strong>Volume Rendering</strong> modules.</p>
<p>I seem to have managed to produce 3D representations OK.</p>
<p>For <em>segments</em> I just click the big <code>Show 3D</code> button in the main (topmost) panel of the <strong>Segment Editor</strong> module.  This allows the option of smoothing the graphical display.</p>
<p>For the <em>labelmap volumes</em> I can display them in 3D through the <strong>Volume Rendering</strong> module;  it does need a suitable volume rendering setting to make sense though, and the default (as configured when the labelmap volume is first created), which seems to be that multicoloured/rainbow stripes pattern, <em>i.e.</em> the <code>Labels</code> Lookup Table, works fairly well.  (<em>I got some <em>partially</em> satisfactory results by heavily modifying a preset set of volume rendering settings, such as <code>CT-AAA</code>. The reason why none of the preset volume rendering settings work well with the labelmap volume is precisely because they all seem to be designed for volumes that have continuous image intensities, as you referred to.</em>)  The downside is that there is no option for smoothing the graphical rendering.<br>
Further to that last point (not part of my original query), my next task would be to figure out how to <strong>export the labelmap volume as an STL file</strong>.  AFAIK this can’t be done directly.  Although I haven’t yet done it, I am envisaging that I need to first convert the labelmap volume into a segment, which appears to be possible by one of two workflows:</p>
<ul>
<li>invoking the <code>Convert labelmap to segmentation node</code> option of the context menu generated when right-clicking on the name of a labelmap volume in the <em>Subject hierarchy</em> tab of the <strong>Data</strong> module; and(<em>?</em>)/or(<em>?</em>)</li>
<li>selecting the “Import” <code>Operation</code> in the <em>Export/import models and labelmaps</em> panel of the <strong>Segmentations</strong> module.</li>
</ul>
<p>Once the labelmap volume has been converted to a segment (perhaps within a new segmentation), then I expect I should be able to view it in 3D, optionally with a smoothed graphical depiction, in the same manner as for any other segment (as I described above).</p>
<p>So in relation to your flowchart/diagramme, perhaps there could be an arrow drawn from top right (Labelmap volume) to bottom left (Volume rendering)?<br>
Regarding your other comments, it may be pertinent to emphasise that while the <strong>Segment Editor</strong> module directly creates <code>Segment</code> objects, the <strong>Simple Region Growing Segmentation</strong> module directly creates <code>Volume</code> objects (of <code>LabelMapVolume</code> subtype).  That may be unexpected, considering the name of the latter module.</p>
<p>—DIV</p>

---

## Post #5 by @DIV (2021-10-27 06:28 UTC)

<aside class="quote no-group" data-username="DIV" data-post="3" data-topic="20375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>The multicoloured/rainbow stripes pattern seems to be the <code>Labels</code> Lookup Table, when comparing to the <em>Display</em> panel in the <strong>Volumes</strong> module. On this basis I have just managed to get it back as a volume rendering setting by clicking the <code>Synchronize with Volumes module</code> tick-box in the <strong>Volume Rendering</strong> module.</p>
</blockquote>
</aside>
<p>Although the above solved the immediate problem, I still think there seems to be merit in ensuring that the corresponding <code>Labels</code> volume rendering settings are available as a Preset in the drop-down list in the <em>Display</em> panel.</p>
<p>—DIV</p>

---

## Post #6 by @muratmaga (2021-10-27 16:07 UTC)

<aside class="quote no-group" data-username="DIV" data-post="4" data-topic="20375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>I guess you’re right, but the output of the <strong>Simple Region Growing Segmentation</strong> module is called a “Volume”, and it seems to show up as a kind of “Volume” in the <strong>Data</strong> , <strong>Volumes</strong> and <strong>Volume Rendering</strong> modules.</p>
</blockquote>
</aside>
<p>Sorry, my mistake. I thought you were using the seed based region growing from the Segment Editor, not the old legacy module. Yes, that outputs a labelmap directly (not a segmentation node), and you can use volume rendering module directly. Segment(s) generated by the <code>Segment Editor</code> can be visualized in 3D as a surface model (not as a volume rendering). For those, if you want to use volume rendering you will have to convert them to labelmap through the import/export tab of the <code>Segmentations</code> module.</p>
<p>Also if you use the Segment Editor and its associated tools, you can directly export your segmentation as an stl or any other 3D format Slicer supports. (Again use the import/export tab of <code>segmentations</code> module). Currently you have couple options:</p>
<ol>
<li>Continue using legacy tools (that are no longer supported). E.g. Model maker will take a label map and export a 3D surface.</li>
<li>Continue doing what you do, but use the <code>Segmentations</code> modules import/export tool to import your label map first as a segmentation, and then export as a 3D model.</li>
<li>Switch to using <code>Segment Editor</code> for your segmentations tasks.</li>
</ol>

---

## Post #7 by @DIV (2021-10-28 00:52 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="6" data-topic="20375">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>[…] options:</p>
<ol>
<li>Continue using legacy tools (that are no longer supported). […]</li>
</ol>
</blockquote>
</aside>
<p>Hi, Muratmaga.<br>
Essentially there were two problems.</p>
<ul>
<li>There was no obvious indication to me (as a simple user, not a developer) that the <strong>Simple Region Growing Segmentation</strong> module is a <em>legacy</em> tool.  I suppose it’s mentioned somewhere online, but I didn’t notice it in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/simpleregiongrowingsegmentation.html" rel="noopener nofollow ugc">current user guide for the module</a> either.  Maybe(?) there isn’t a need for cues in the software itself, but I do think this sort of status should be clearly indicated in the user guide.  For example, a statement like, “<strong><em>This module is retained for legacy workflows;  for new analyses it is recommended to instead use module X</em></strong>” at the top of the page.  (Or similar:  see this <a href="https://support.microsoft.com/en-us/office/norminv-function-87981ab8-2de0-4cb0-b1aa-e21d4cb879b8" rel="noopener nofollow ugc">documentation for the NORMINV function in Excel</a>, for instance.)  There is a set of <code>Legacy</code> items in the drop-down <em>Modules</em> menu on the toolbar, but it doesn’t contain the  <strong>Simple Region Growing Segmentation</strong> module, nor the <strong>Annotations</strong> module (which I am given to understand is also superseded by the <strong>Markups</strong> module).</li>
<li>I think I had an incorrect preconception of what the <strong>Simple Region Growing Segmentation</strong> module does.  After spending some time on it, it seems that essentially it performs <em>thresholding</em>, in which the key differences from the <em>Threshold</em> effect in the <strong>Segment Editor</strong> module are that (i) there is [optionally] a prior volumetric smoothing effect, and (ii) the upper and lower limits for the thresholding segmentation are computed ‘automatically’ based upon iterative analysis of the intensities around certain seed points (defined through <em>fiducial markers</em>).  Is that right?  And are you saying that the <em>Grow from seeds</em> effect in the <strong>Segment Editor</strong> module is roughly equivalent to the <em>Simple Region Growing Segmentation</em>?  The only reasons I tried out the <em>Simple Region Growing Segmentation</em> is because I wasn’t completely satisfied with the results I had so far from the <strong>Segment Editor</strong> module, and I thought that the <strong>Simple Region Growing Segmentation</strong> module offered something different.  The <strong>Segment Editor</strong> module is much more user friendly, though.</li>
</ul>
<p>—DIV</p>

---

## Post #8 by @muratmaga (2021-10-28 01:01 UTC)

<p>I personally never used the simple region growing segmentation module before, so I can’t really compare to the grow from the seeds in Segment Editor. All I can the latter works really well for some cases (e.g., <a href="https://discourse.slicer.org/t/new-segment-editor-feature-masking-in-grow-from-seeds-effect/4978" class="inline-onebox">New Segment Editor feature: masking in Grow from seeds effect</a>).</p>
<p>I can second the request to move simple region growing and annotations to the legacy folder.</p>

---

## Post #9 by @lassoan (2021-10-29 04:52 UTC)

<p>Simple region growing segmentation module is not bad, it is just not relevant anymore, since the Segment Editor has much better tools now. We recommend the Segment Editor module everywhere (forum, tutorials, documentation), while not the other modules that we don’t expect to work any better (and they are not as convenient to use as the ones in the Segment Editor). I guess further de-emphasizing the irrelevant modules by moving them to legacy category could make sense. I’ve submitted a pull request for this: <a href="https://github.com/Slicer/Slicer/pull/5971" class="inline-onebox">ENH: Move RobustStatisticsSegmenter and SimpleRegionGrowingSegmentation modules to legacy category by lassoan · Pull Request #5971 · Slicer/Slicer · GitHub</a></p>

---
