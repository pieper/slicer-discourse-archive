# How can I configure Slicer to open automatically with my preferred settings for the View Controllers module?

**Topic ID**: 20233
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/how-can-i-configure-slicer-to-open-automatically-with-my-preferred-settings-for-the-view-controllers-module/20233

---

## Post #1 by @DIV (2021-10-19 11:49 UTC)

<p>There are certain repeated actions that I do repeatedly that are becoming repetitious…</p>
<p>For instance, adding yellow rulers to each of the three slice viewers requires <em>many mouse clicks</em>.  (This is true no matter whether it’s done through the View Controllers module or the equivalent drop-down toolbars in, say, the four-up view port.)</p>
<ul>
<li>Assuming that I want these always to <strong>appear by default</strong> when I launch 3D Slicer, is there a convenient way to <strong>configure</strong> that?  (And similar things such as no interpolation of background, preferred display of orientation marker, …)  [<em>I have no idea.</em>]</li>
<li>If the settings are desired, say, 50% of the time, is there a convenient way to write a <strong>script</strong> for this in Python, so that the user-defined display settings can be implemented collectively with just a couple of mouse clicks?  [<em>I guess that it may be possible, given the existence of the Python Interactor — which I’ve never used.</em>]</li>
</ul>
<p>—DIV</p>

---

## Post #2 by @jamesobutler (2021-10-19 12:42 UTC)

<p>A series of tasks such as adding yellow rulers to the slice views can be performed using the slicerrc file discussed at <a href="https://slicer.readthedocs.io/en/latest/user_guide/settings.html#application-startup-file" class="inline-onebox" rel="noopener nofollow ugc">Application settings — 3D Slicer documentation</a>.</p>
<p>Pretty much everything can be automated through python coding. See the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" rel="noopener nofollow ugc">Slicer script repository</a> for some examples. There also other posts on the forum that have answered the coding type questions you have asked.</p>

---

## Post #3 by @muratmaga (2021-10-19 14:24 UTC)

<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Assuming that I want these always to <strong>appear by default</strong> when I launch 3D Slicer, is there a convenient way to <strong>configure</strong> that?</p>
</blockquote>
</aside>
<p>Edit-&gt;application settings-&gt;view<br>
The choose your ruler type.</p>

---

## Post #4 by @lassoan (2021-10-20 04:58 UTC)

<aside class="quote no-group" data-username="DIV" data-post="1" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>no interpolation of background</p>
</blockquote>
</aside>
<p>I would strongly recommend not doing this. It introduces staircases in the image signal that are not present in the original continuous signal. See details in this discussion:</p>
<aside class="quote quote-modified" data-post="10" data-topic="13918">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918/10">Volume display - Interpolate turned off by default in newest stable?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Interpolated image shows you the faithfully reconstructed continuous signal from the discrete samples. This reconstruction is lossless if sample-rate criterion is satisfied (see more details <a href="https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem">here</a>). The criterion is not always satisfied - that’s when you see staircase artifacts in the reconstructed image (in both slice views, volume rendering, and reconstructed surfaces): 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e2131f4e5e4dfc53650494641005ab3d8014a49.jpeg" data-download-href="/uploads/short-url/8RCIQSyJC6Le9lCBgPunGs1bNq1.jpeg?dl=1" title="image">[image]</a> 
Interpolation is still about the best thing you can do, and definitely provides much more faithful reconstruction …
  </blockquote>
</aside>


---

## Post #5 by @DIV (2021-10-20 07:14 UTC)

<p>Thanks, muratmaga.<br>
Indeed it is helpful to set <em>a few key view settings</em> through<br>
Edit-&gt;application settings-&gt;view</p>
<p>However it doesn’t allow <em>every</em> option to be pre-configured there (and nor should it).  For instance, the colour of the ruler cannot be specified there.</p>

---

## Post #6 by @DIV (2021-10-20 07:34 UTC)

<p>Hello, Andras.<br>
From your cited discussion I found:</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="13918">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/volume-display-interpolate-turned-off-by-default-in-newest-stable/13918/10">Volume display - Interpolate turned off by default in newest stable?</a></div>
<blockquote>
<p>I agree that it can be useful to show the voxel grid during segmentation so that you know how fine details you can paint and where. Note that this is the grid of the binary labelmap representation of the segmentation and not the grid of the background scalar volume.</p>
</blockquote>
</aside>
<p>So this is interesting for two reasons.<br>
Firstly, I am mainly interested in this for segmentation.<br>
Secondly, I am not sure of what is being used to define the grid of a segment if not the grid of a scalar volume.</p>
<p>On the latter point, so far I had found the segments (e.g. from the <strong>Threshold</strong> effect) rather jagged for small features, so recently I have been creating new <em>scaled</em> cropped volumes from these small objects (through the <strong>Crop Volume</strong> module, with <strong>Spacing scale</strong> set to, say, 0.50x or 0.20x and with the <strong>Interpolator</strong> set to “B-spline”).<br>
So I suspect — correct me if I’m wrong — that this would avoid some of the staircase issues you’re talking about, because interpolation is still performed somewhere along the way.<br>
On the other hand, perhaps I’m overlooking a clever feature in Slicer whereby I can use a refined grid for the segment, different from any extant volume??</p>
<p>—DIV</p>

---

## Post #7 by @muratmaga (2021-10-20 15:17 UTC)

<aside class="quote no-group" data-username="DIV" data-post="5" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>However it doesn’t allow <em>every</em> option to be pre-configured there (and nor should it). For instance, the colour of the ruler cannot be specified there.</p>
</blockquote>
</aside>
<p>There are simply too many ways people want to configure things. Preferences are only allows a a small subset of common things.<br>
That’s why there is a startup script (.slicerrc.py) that you can configure not exposed options in the UI in the way you want.</p>

---

## Post #8 by @lassoan (2021-10-21 02:25 UTC)

<aside class="quote no-group" data-username="DIV" data-post="6" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>So this is interesting for two reasons.<br>
Firstly, I am mainly interested in this for segmentation.<br>
Secondly, I am not sure of what is being used to define the grid of a segment if not the grid of a scalar volume.</p>
</blockquote>
</aside>
<p>You can use many volumes to create the segments and not all of them have the same size and resolution. Also, you typically want the segmentation to be isotropic and sometimes you want it to be somewhat finer resolution than the input volume (to be able to represent small details that are actually not visible in the image, but the clinician knows that they are there and may want to define them with higher precision than the input image).</p>
<aside class="quote no-group" data-username="DIV" data-post="6" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>So I suspect — correct me if I’m wrong — that this would avoid some of the staircase issues you’re talking about, because interpolation is still performed somewhere along the way.</p>
</blockquote>
</aside>
<p>Staircase effect is mostly due to anisotropic spacing. Using Crop volume with isotropic spacing option eliminates this artifact. You can set the segment’s geometry using the “Specify geometry” button, then the user does not need to resample the volume (the segment editor module resamples it internally). However, typically it is simpler, more clear, and more memory efficient if the user crops and resamples the input volume before segmentation.</p>

---

## Post #9 by @DIV (2021-10-22 04:09 UTC)

<aside class="quote no-group quote-modified" data-username="muratmaga" data-post="7" data-topic="20233" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<aside class="quote no-group quote-modified" data-username="DIV" data-post="5" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>However it doesn’t allow <em>every</em> option to be pre-configured there (and <strong>nor should it</strong>).<br>
[…]</p>
</blockquote>
</aside>
<p>[…]That’s why there is […] not exposed options in the UI in the way you want.</p>
</blockquote>
</aside>
<p>Thanks, Muratmaga, but I did not express the preference for <em>all</em> options to be able to be set individually through the settings menu — actually, I expressed the opposite view (emphasis added above).<br>
—DIV</p>
<p>P.S. Another alternative (which I haven’t raised before) is for Slicer to simply ‘remember’ <em>(almost) all settings from the previous session</em> automatically (e.g. ruler colour, but not the zoom).  This could get complicated if multiple instances of Slicer are launched with different viewport settings, and some users mightn’t like it, so if implemented there could be a tickbox in the settings menu to enable/disable it.</p>

---

## Post #10 by @DIV (2021-10-22 04:42 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="8" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can use many volumes to create the segments and not all of them have the same size and resolution.  Also, you typically want the segmentation to be isotropic and sometimes you want it to be somewhat finer resolution than the input volume […].<br>
[…]<br>
You can set the segment’s geometry using the “Specify geometry” button, then the user does not need to resample the volume (the segment editor module resamples it internally).</p>
</blockquote>
</aside>
<p>So then from your comments and the documentation at <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="inline-onebox" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a> I think I understand now.</p>
<ul>
<li>Each Segmentation must be associated with a Volume (providing radiodensity) and a Geometry (providing the grid) at any given moment.</li>
<li>The Geometry of the Segmentation can be identical to the geometry of its Master Volume, or it can be a modified version of that (<em>e.g</em>. forced to be isotropic), or it can be based on a totally different source (possibly a Volume, with prespecified geometry, or perhaps a ROI with a customisable user-specified geometry).</li>
<li>From time to time the Volume and/or Geometry on which a Segmentation is based can be changed.</li>
</ul>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="8" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Staircase effect is mostly due to anisotropic spacing. Using Crop volume with isotropic spacing option eliminates this artifact. […] [T]ypically it is simpler, more clear, and more memory efficient if the user crops and resamples the input volume before segmentation.</p>
</blockquote>
</aside>
<p>Thank-you, Andras, I appreciate your advice, and will be aware of the benefits of applying isotropic sampling in future.  I had avoided this until now because I naïvely assumed that applying <em>more transformations</em> would likely introduce <em>more artefacts</em>!<br>
I am glad to hear that cropping the volume is considered an efficient approach — at least for my purposes, where the individual features of interest might occupy less than 1% of the whole original scan volume.<br>
—DIV</p>

---

## Post #11 by @lassoan (2021-10-22 19:06 UTC)

<aside class="quote no-group" data-username="DIV" data-post="10" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>Each Segmentation must be associated with a Volume (providing radiodensity) and a Geometry (providing the grid) at any given moment.</p>
</blockquote>
</aside>
<p>You only need a volume for editing segmentations. Some Segment Editor effects would not need it, but it was easier to just make this a prerequisite for segmentation.</p>
<aside class="quote no-group" data-username="DIV" data-post="10" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>The Geometry of the Segmentation can be identical to the geometry of its Master Volume, or it can be a modified version of that ( <em>e.g</em> . forced to be isotropic), or it can be based on a totally different source (possibly a Volume, with prespecified geometry, or perhaps a ROI with a customisable user-specified geometry).</p>
</blockquote>
</aside>
<p>Correct.</p>
<aside class="quote no-group" data-username="DIV" data-post="10" data-topic="20233">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/div/48/12816_2.png" class="avatar"> DIV:</div>
<blockquote>
<p>From time to time the Volume and/or Geometry on which a Segmentation is based can be changed.</p>
</blockquote>
</aside>
<p>Correct. Since image resampling is a lossy operation, and it is particularly bad for binary images, it is better to avoid changing geometry of existing segmentations. However, a one-time cropping and resampling to isotropic spacing before starting segmentation is usually beneficial.</p>

---
