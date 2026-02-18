# Improve recognizability of Segment Editor effects icons

**Topic ID**: 19772
**Date**: 2021-09-20
**URL**: https://discourse.slicer.org/t/improve-recognizability-of-segment-editor-effects-icons/19772

---

## Post #1 by @jamesobutler (2021-09-20 21:15 UTC)

<p>With recent optimization of the Segment Editor module GUI the segment effects are now displayed a QToolButtons with icons that do not display text with the button. Text was removed to make the buttons more compact and to align with the style of other programs such as Paint, Photoshop, Gimp etc where they don’t put text under each effect in their list of tools.</p>
<p>As originally suggested by <a class="mention" href="/u/tomekcz">@tomekcz</a>, we could update the segment editor effect icons to more closely align with the icons used in other programs.</p>
<aside class="quote quote-modified" data-post="2" data-topic="19649">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/tomekcz/48/11462_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-segment-editor-layout-vertical-effect-toolbar/19649/2">New Segment Editor layout - vertical effect toolbar</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category --style-square " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
    </div>
  </div>
  <blockquote>
    This is looking great. One minor suggestion now that the Effect labels have been removed and the button icons are much smaller is to consider creating some new artwork for very common effects to harmonize them with well-known painting and image editing programs. 
For example, the Draw tool could be made into a simple pencil icon, the Paint tool could just be a paintbrush, Flood Filling could be a paint can, Level Tracing could be a magic wand, Eraser just a simple eraser. I’m not sure what exact…
  </blockquote>
</aside>

<p>Familiarity is key to improving usability as indicated over in this <a href="https://discourse.slicer.org/t/segment-editor-user-interface-improvements/9029/20">post</a>:</p>
<aside class="quote no-group" data-username="Umesh_Persad" data-post="20" data-topic="9029">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/umesh_persad/48/4719_2.png" class="avatar"><a href="https://discourse.slicer.org/t/segment-editor-user-interface-improvements/9029/20">Segment Editor User Interface Improvements</a></div>
<blockquote>
<p>Three key principles of usability are familiarity, consistency and feedback. In other words, if the interface is similar to what people already know and use (standards), it will be easier to use. Menu names, structures and layouts are what users are familiar with using other software. For example, why “Segmentation Effects” versus “Segmentation Tools”. This was why Blender was so hard to use until the Blender 2.8 update. Experts could use it but the majority of people could not.</p>
</blockquote>
</aside>
<h2><a name="p-66616-current-segment-editor-effects-icons-1" class="anchor" href="#p-66616-current-segment-editor-effects-icons-1" aria-label="Heading link"></a>Current Segment Editor effects icons</h2>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea171934e22ed4465423af226b5e17321c493f55.png" alt="image" data-base62-sha1="xoRdpvJDoydvNXAu9wDQFyqKVWR" width="91" height="342"></p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Column 1</th>
<th>Column 2</th>
</tr>
</thead>
<tbody>
<tr>
<td>No editing</td>
<td>Threshold</td>
</tr>
<tr>
<td>Paint</td>
<td>Draw</td>
</tr>
<tr>
<td>Erase</td>
<td>Level Tracing</td>
</tr>
<tr>
<td>Grow from seeds</td>
<td>Fill between slices</td>
</tr>
<tr>
<td>Margin</td>
<td>Hollow</td>
</tr>
<tr>
<td>Smoothing</td>
<td>Scissors</td>
</tr>
<tr>
<td>Islands</td>
<td>Logical operators</td>
</tr>
<tr>
<td>Mask Volume</td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #2 by @lassoan (2021-09-20 21:30 UTC)

<p>What do you think about using/combining <a href="https://fonts.google.com/icons">Google material design icons</a>?They come with Apache license - all free to use, modify, combine, etc.</p>
<p>Paint: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d5a8aa2597f357bb493cf9d9576742e49bd441d.png" alt="image" data-base62-sha1="4bFPwlVruI6sn3YqPzg1QaecNrf" width="63" height="65"><br>
Draw: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/354e3747af67fa765d49e5efd82e0f84b363aaef.png" alt="image" data-base62-sha1="7BySJvFUlAm0KtLJHv7efB5Lawf" width="57" height="66"><br>
Scissors: <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a82b2df80be6d3e66bcd2bbeb185b526522082f.png" alt="image" data-base62-sha1="3MwqXXICMk4sYaspVTN01phhnd5" width="62" height="72"></p>
<p>We could change the two tone icons to use color in the Slicer logo.</p>

---

## Post #3 by @jamesobutler (2021-09-20 21:53 UTC)

<p>Yes licensing will be an important consideration if we are adopting the designs of others as most of us are not icon artists. Those google icons are simple and adopt similar designs of others.</p>
<p>A great overview of all of Photoshop’s toolbar effects: <a href="https://www.photoshopessentials.com/basics/photoshop-tools-toolbar-overview/" class="inline-onebox" rel="noopener nofollow ugc">Photoshop Tools and Toolbar Overview</a></p>
<h2><a name="p-66621-paintbrush-1" class="anchor" href="#p-66621-paintbrush-1" aria-label="Heading link"></a>Paint/Brush</h2>
<ul>
<li>
<p>Slicer “Paint”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b216935ebc075e66be918f7e7d8db6c16a3806ca.png" alt="Paint" data-base62-sha1="pprmbGftJ9YiR3geCXJHGDM17PY" width="21" height="21"></p>
</li>
<li>
<p>Photoshop “Brush”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a97135b524dd595c2eb102274beb5e5a83b6de0a.png" alt="image" data-base62-sha1="oaXf5wL0kDzvt3VHkzSejLGl04W" width="66" height="52"><br>
This brings up another item which is effect name. The “Brush” tool may be more common than saying to use the “Paint” tool.</p>
</li>
</ul>
<blockquote>
<p>The Brush Tool is Photoshop’s primary painting tool. Use it to paint brush strokes on a layer or on a layer mask.</p>
</blockquote>
<h2><a name="p-66621-drawpencil-2" class="anchor" href="#p-66621-drawpencil-2" aria-label="Heading link"></a>Draw/Pencil</h2>
<ul>
<li>
<p>Slicer “Draw”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd268511f8798c6898a63cca9deadade4554e842.png" alt="Draw" data-base62-sha1="A7tkm5k7q3n5ad2Y38VsidMDwcO" width="21" height="21"></p>
</li>
<li>
<p>Photoshop “Pencil”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb934e2853c8dfad3da577f282004afc0c165990.png" alt="image" data-base62-sha1="t2UwEt6ncVTSmovZ1FopirTiNq0" width="66" height="52"><br>
Again just like “Paint”/“Brush”, it may be more common to refer to this as “Pencil” instead of “Draw”. MS Paint also refers to it as the “Pencil” tool.</p>
</li>
</ul>
<blockquote>
<p>The Pencil Tool is another of Photoshop’s painting tools. But while the Brush Tool can paint soft-edge brush strokes, the Pencil Tool always paints with hard edges.</p>
</blockquote>
<h2><a name="p-66621-level-tracingpaint-bucket-3" class="anchor" href="#p-66621-level-tracingpaint-bucket-3" aria-label="Heading link"></a>Level Tracing/Paint Bucket</h2>
<ul>
<li>
<p>Slicer “Level Tracing”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13b217eb7f44187cee59758b6d80bec4dbfe6bec.png" alt="LevelTracing" data-base62-sha1="2OeDolXe5qa1hvTHYufaLfOiH7u" width="21" height="21"></p>
</li>
<li>
<p>Photoshop “Paint Bucket”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/482fe2c9dec94ecb64870317fe263e32c4c4c5c9.png" alt="image" data-base62-sha1="aiAYjV94cKpb9NVLkjJuMhmMbbP" width="66" height="52"></p>
</li>
</ul>
<blockquote>
<p>The Paint Bucket Tool fills an area of similar color with your Foreground color or a pattern. The “Tolerance” value determines the range of colors that will be affected around the area where you clicked.</p>
</blockquote>
<h2><a name="p-66621-eraseeraser-4" class="anchor" href="#p-66621-eraseeraser-4" aria-label="Heading link"></a>Erase/Eraser</h2>
<ul>
<li>
<p>Slicer “Erase”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a024c65cfb6ad1486ba7fe54fd8001be578ba75c.png" alt="Erase" data-base62-sha1="mQHbthKUeHsmjBDueoETESfbA60" width="21" height="21"></p>
</li>
<li>
<p>Photoshop “Eraser”<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/625a31ea7ef5a9b7badbcb0b16376d3353bbe812.png" alt="image" data-base62-sha1="e2426zeWK0KoEMJ84uQiGikBGcG" width="66" height="52"></p>
</li>
</ul>
<blockquote>
<p>The Eraser Tool in Photoshop permanently erases pixels on a layer. It can also be used to paint in a previous history state.</p>
</blockquote>

---

## Post #4 by @jamesobutler (2021-09-20 22:10 UTC)

<p>As I began to explain in the last post, should we name the items in the Segment Editor module as the “effect” or the “tool” being used? Such as you may use the “Pencil” tool to draw or the “Brush” tool to paint brush strokes. The simple/recognizable icons would be reflecting the tool rather than the effect/action. The current icons reflect more the action such as the pixels actively being placed in the “Draw” icon.</p>
<p>I think this is what <a class="mention" href="/u/umesh_persad">@Umesh_Persad</a> was getting at as it relates to naming them “Segmentation Tools” rather than “Segmentation Effects”. Photoshop refers to the buttons in the vertical layout as “Tools” rather than “Effects”.</p>

---

## Post #5 by @lassoan (2021-09-20 22:44 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="19772">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>should we name the items in the Segment Editor module as the “effect” or the “tool” being used?</p>
</blockquote>
</aside>
<p>I agree, everybodyelse  uses the term “tool”. Slicer uses the “tool” term, too, in Dynamic modeler module (which will be the engine for the Model Editor module in the future). Maybe it was not obvious 20 years ago that this term was going to win, or it was just a quick decision that was hard to change.</p>
<p>However, if I look at the cost and benefits of making this change (at least in the GUI &amp; documentation, but - to be consistent - also in the source code and everywhere else) then this change would rate very poorly compared to other things that we could work on.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="3" data-topic="19772">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>great overview of all of Photoshop’s toolbar effects</p>
</blockquote>
</aside>
<p>I don’t think that many medical professionals and researchers use Photoshop as much as a few decades ago. Nowadays, people do most image processing tasks using various apps. So, I would not prioritize familiarity for Photoshop users.</p>
<p>We should use similar terms as other medical image viewer and segmentation software, such as Mimics, ITK Snap, Osirix, MITK, OHIF, napari, and various commonly used commercial radiology software.</p>
<p>Changing the effect icons and names at the same time may not be the best idea, though. Probably we should change the icons soon and then the effect names in a few years.</p>

---

## Post #6 by @jamesobutler (2021-09-20 23:10 UTC)

<p>It appears we cannot change to a simple “Pencil” icon for the “Draw” effect as we would no longer be providing artwork for the thing being described. The current “Draw” icon is describing the action of draw rather than using a “Pencil”.</p>

---

## Post #7 by @lassoan (2021-09-20 23:34 UTC)

<p>The “pencil” icon above was actually the “edit” icon, so probably it was not a good fit anyway. Based on what the draw effect does, maybe using a “lasso” icon would be the most descriptive. We’ll probably merge the draw and scissors tools at some point (since they do the exact same thing, with a bit different limitations), so that would be a good opportunity to change the name and icon to “lasso”.</p>

---

## Post #8 by @jamesobutler (2021-09-20 23:43 UTC)

<p>As it relates to familiarity I don’t think Photoshop is a specific standard but also aligns well with well known applications like MS Paint. Familiarity of icons for actions like these in general I would say is better than primarily focusing on what other medical imaging applications refer to these tools. The other medical imaging applications may not be applying familiarity principles either. So if a user comes to 3D Slicer and has never used mimics or ITK-snap etc they can still rely on familiarity with other applications they have used before.</p>

---
