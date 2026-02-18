# Copying segment names/colors from one segmentation to another

**Topic ID**: 21204
**Date**: 2021-12-25
**URL**: https://discourse.slicer.org/t/copying-segment-names-colors-from-one-segmentation-to-another/21204

---

## Post #1 by @muratmaga (2021-12-25 18:16 UTC)

<p>I have two segmentations of the same volume derived in different ways (monailabel vs reference). While the order of the segments are same and correct, the colors and segment labels are different between (one uses actual organ names, the other goes segment_1 segment_2).</p>
<p>I want to make them consistent so that I can make visualizations. If possible, I would like to have the segment names to be consistent but, it is really the colors that I care.  How can I do this?</p>

---

## Post #2 by @muratmaga (2021-12-27 19:38 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> do you have suggestions?</p>

---

## Post #3 by @lassoan (2021-12-27 19:41 UTC)

<p>You can read segment, name, color, etc. from one segmentation and set it in the other. Do you have any constraints that would make this difficult?</p>

---

## Post #4 by @muratmaga (2021-12-27 19:54 UTC)

<p>I don’t think I know how to do that from UI.</p>

---

## Post #5 by @lassoan (2021-12-27 20:03 UTC)

<p>You can use a color node to assign color and segment name to a label value in a labelmap volume when you import it into a segmentation. A color node is created automatically when a labelmap volume is exported from the segmentation.</p>
<p>Of course this should not be necessary. Existing modules should be fixed up to set/preserve segment names appropriately. Can you describe your complete data processing flow?</p>

---

## Post #6 by @muratmaga (2021-12-27 20:12 UTC)

<p>For every</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="21204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Can you describe your complete data processing flow?</p>
</blockquote>
</aside>
<p>I have two labelmaps/segmentations derived from volumes. One is a labelmap of atlas-based segmentation of the volume from ANTs (external to Slicer). These do not have segment names associated with them, when we import them into Slicer (as segmentation), they go Segment_1, Segment_2 so forth.</p>
<p>After touching up manually, we feed these into MONAILabel and train a model. For MONAI, we provided the correct segment names and label numbers into the multilabel-deepedit script. When MONAILabel segments one of these volumes, the segment names are indeed correct labels we provided in the script.</p>
<p>So between my manual labelmap and MONAILabel derived one, we have correct ordering of the segments, but colormaps do not match. I would like to make the following visualization, but with the identical colors (if possible labels as well) in both segmentations. (left monai, right my reference segmentation).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95cd880b6fa910901789b45b998597eaa71eaa73.jpeg" data-download-href="/uploads/short-url/lnduvNsS09BvtsCTKVQhReNVAQ3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95cd880b6fa910901789b45b998597eaa71eaa73_2_690x452.jpeg" alt="image" data-base62-sha1="lnduvNsS09BvtsCTKVQhReNVAQ3" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95cd880b6fa910901789b45b998597eaa71eaa73_2_690x452.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95cd880b6fa910901789b45b998597eaa71eaa73_2_1035x678.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/95cd880b6fa910901789b45b998597eaa71eaa73_2_1380x904.jpeg 2x" data-dominant-color="545350"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1260 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2021-12-27 21:00 UTC)

<p>That’s perfect! All you need to do is to select the correct color node when you load the segmentation (or you import the labelmap into a segmentation node):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df6a0b97226bf6b34c1a06215e3e0d73d1ba3aed.png" data-download-href="/uploads/short-url/vSpFXRzReO6sMOhWA9drFZiAkXP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df6a0b97226bf6b34c1a06215e3e0d73d1ba3aed_2_690x314.png" alt="image" data-base62-sha1="vSpFXRzReO6sMOhWA9drFZiAkXP" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df6a0b97226bf6b34c1a06215e3e0d73d1ba3aed_2_690x314.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df6a0b97226bf6b34c1a06215e3e0d73d1ba3aed_2_1035x471.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/f/df6a0b97226bf6b34c1a06215e3e0d73d1ba3aed_2_1380x628.png 2x" data-dominant-color="393938"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1436×654 31.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can create a color node conveniently by setting up a segmentation with colors and segment names and export it to a labelmap volume (result of the export operation is a volume node and a color node).</p>

---

## Post #8 by @muratmaga (2021-12-27 22:38 UTC)

<p>I can’t get it to work. Here are my steps:</p>
<ol>
<li>Export the MONAILabel segmentation as a labelmap. This creates a color table as you indicated.</li>
<li>Use Add Data to import the reference labelmap. I choose the description as Segmentation, and than specific the color node that exported in Step 1.</li>
</ol>
<p>After this, colors are not the same. Though, segments labels and ordering are correct (up to a point, there are some renamed as invalid).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0307b87322de883d4d68b5d40b9256c796dd8581.jpeg" data-download-href="/uploads/short-url/qNYmdiR0tDg0ctrEKduP9G6p0d.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0307b87322de883d4d68b5d40b9256c796dd8581_2_690x93.jpeg" alt="image" data-base62-sha1="qNYmdiR0tDg0ctrEKduP9G6p0d" width="690" height="93" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0307b87322de883d4d68b5d40b9256c796dd8581_2_690x93.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0307b87322de883d4d68b5d40b9256c796dd8581_2_1035x139.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0307b87322de883d4d68b5d40b9256c796dd8581_2_1380x186.jpeg 2x" data-dominant-color="DDE4EB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1826×248 67.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>There is also something wrong with the exported color table as there are two background entries, which causing the shift.</p>
<pre><code class="lang-auto">maga@magalab-ML:~/Documents$ cat KOMP_ColorTable.ctbl 
# Color table file /home/maga/Documents/KOMP_ColorTable.ctbl
# 52 values
0 Background 0 0 0 0
1 background 0 0 0 255
2 left_lung 197 165 145 255
3 cranial_lobe 128 174 128 255
4 middle_lobe 241 214 145 255
5 caudal_lobe 177 122 101 255
6 accessory_lobe 111 184 210 255
7 left_kidney 185 102 83 255
8 right_kidney 185 102 83 255
9 stomach_wall 216 101 79 255
10 stomach_lumen 221 130 101 255
11 medial_lobe_of_liver 144 238 144 255
12 left_lobe_of_liver 192 104 88 255
13 right_lobe_of_liver 220 245 20 255
14 caudate_lobe_of_liver 78 63 0 255
15 left_adrenal 255 250 220 255
16 right_adrenal 230 220 70 255
17 rectum 200 200 235 255
18 bladder 250 250 210 255

</code></pre>

---

## Post #9 by @muratmaga (2021-12-27 22:48 UTC)

<p>OK. Deleting the first Background and then shifting down the corresponding the values by 1 fixed the problem.</p>
<p>I do not know why it exports two background colors.</p>

---

## Post #10 by @lassoan (2021-12-27 23:22 UTC)

<p>Is the invalid color table (duplicate background label) generation reproducible if you load the .seg.nrrd file and then export to labelmap? Can you share the .seg.nrrd file (upload somewhere and post the link)?</p>
<p>By the way, ANTs is available in Slicer. Have you tried using it? You can also compute the transform using any software and save as an ITK transform file or a displacement field volume, load that into Slicer, and warp the atlas in Slicer. These may make it unnecessary to manually load a colormap and apply it to a labelmap volume.</p>

---

## Post #11 by @muratmaga (2021-12-27 23:27 UTC)

<p>It is reproducible for me with this <a href="https://app.box.com/shared/static/zca0gnxq23wenv57943w0kg0sp7da50q.mrb" rel="noopener nofollow ugc">data from MONAILabel</a></p>
<p>Originals are only saved as labelmaps, we do not have seg.nrrd for those (This dataset predates SlicerANTs).</p>

---

## Post #12 by @lassoan (2021-12-28 02:08 UTC)

<p>MONAILabel creates a segmentation that actually has 2 background labels (0 and 1), which is redundant but valid. The first non-background label is 2.</p>
<p>If in your old labelmaps the first non-background label is 2 (or the order is different or there are any other differences) then you can still use the exported color table as a template, but you need to modify it to match the actual label values.</p>
<p>Can you share your multilabel-deepedit script so that we can have a look? If you did not intentionally have two background labels then most likely you need to fix something in that script (for example, do not specify 0 as a label, because 0 always means background).</p>

---

## Post #13 by @muratmaga (2021-12-28 02:19 UTC)

<p>I am working off the branch from <a class="mention" href="/u/diazandr3s">@diazandr3s</a> fork <a href="https://github.com/Project-MONAI/MONAILabel/tree/komp_deepedit" rel="noopener nofollow ugc">here</a></p>
<p>The only difference, there are more labels specified in that main.py. Here is my version of those sections:<br>
They match exactly the indices of the labelmaps. I didn’t modify anything else.</p>
<pre><code class="lang-auto">self.label_names = {
            "left lung": 1,
            "cranial lobe": 2,
            "middle lobe": 3,
            "caudal lobe": 4,
            "accessory lobe": 5,
            "left kidney": 6,
            "right kidney": 7,
            "stomach wall": 8,
            "stomach lumen": 9,
            "medial lobe of liver": 10,
            "left lobe of liver": 11,
            "right lobe of liver": 12,
            "caudate lobe of liver": 13,
            "left adrenal": 14,
            "right adrenal": 15,
            "rectum": 16,
            "bladder": 17,
            "left ventricle": 18,
            "right ventricle": 19,
            "left thymic rudiment": 20,
            "right thymic rudiment": 21,
            "third ventricle": 22,
            "mesencephalic vesicle": 23,
            "fourth ventricle": 24,
            "cerebral aqueduct": 25,
            "left lateral ventricle": 26,
            "right lateral ventricle": 27,
            "right olfactory bulb": 28,
            "left olfacotory bulb": 29,
            "right thalamus": 30,
            "left thalamus": 31,
            "right hypothamalus": 32,
            "left hypothalmus": 33,
            "right septal area": 34,
            "left septal area": 35,
            "left neopallial cortex abd amygdala": 36,
            "right neopallial cortex and amygdala": 37,
            "right striatum": 38,
            "left striatum": 39,
            "right ventricular zone": 40,
            "left ventricular zone": 41,
            "pons": 42,
            "left cerebellar primordium ": 43,
            "right cerebellar primordium": 44,
            "midbrain": 45,
            "medulla oblongata": 46,
            "spinal cord": 47,
            "vertebrae": 48,
            "left ventricle chamber": 102,
            "right ventricle chamber": 103,
            "background": 0,
        }
</code></pre>
<p>I did specify background as 0, because the original deepedit script has that.</p>

---

## Post #14 by @lassoan (2021-12-28 02:29 UTC)

<p>Probably that <code>"background": 0,</code> line is a mistake. Can you try if everything works as expected if you remove it?</p>

---
