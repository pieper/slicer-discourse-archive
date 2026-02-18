# Continous color table for heatmap

**Topic ID**: 33464
**Date**: 2023-12-20
**URL**: https://discourse.slicer.org/t/continous-color-table-for-heatmap/33464

---

## Post #1 by @muratmaga (2023-12-20 05:52 UTC)

<p>We have an image in which the voxel values are the statistical effect sizes ranging from about -0.3 to 0.9. Most of the image is 0s (voxels that didn’t reach significance). I would like to render this image in a way that negative values are a blue to green ramp (-1, 0), positive values green to red (0, 1), and values of 0 are not shown at all.</p>
<p>I am trying creating color tables but have no luck. I appreciate if someone can guide me.</p>
<p>attached is a sample nRRD file: <a href="https://app.box.com/s/bfr72p0ms3nus79sk4uq0k1hc9u18nvg" class="inline-onebox">Box</a></p>

---

## Post #2 by @muratmaga (2023-12-20 06:13 UTC)

<p>To give a visual example, this is with my modified color table which supposedly have symmetric values from -2 to 2 with 256 colors.</p>
<p>For whatever reason, the scale bar is displaying values only from -0.1 to 0.3 even though the max and min values for this volume is clearly reported to be -0.3 to 0.9 range<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b54951b284657c76be568689508e872383a0f40.jpeg" data-download-href="/uploads/short-url/aKp1H5kX2j0MiMpxBo3FtYk02nC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b54951b284657c76be568689508e872383a0f40_2_690x495.jpeg" alt="image" data-base62-sha1="aKp1H5kX2j0MiMpxBo3FtYk02nC" width="690" height="495" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b54951b284657c76be568689508e872383a0f40_2_690x495.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b54951b284657c76be568689508e872383a0f40_2_1035x742.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b54951b284657c76be568689508e872383a0f40_2_1380x990.jpeg 2x" data-dominant-color="7DB7E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3354×2408 781 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af20be05921550ca9128ed2b60e55477056ffda9.jpeg" data-download-href="/uploads/short-url/oZfHQX5sfc9szP9oNM5mtjOKyiR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af20be05921550ca9128ed2b60e55477056ffda9_2_490x500.jpeg" alt="image" data-base62-sha1="oZfHQX5sfc9szP9oNM5mtjOKyiR" width="490" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af20be05921550ca9128ed2b60e55477056ffda9_2_490x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af20be05921550ca9128ed2b60e55477056ffda9_2_735x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af20be05921550ca9128ed2b60e55477056ffda9_2_980x1000.jpeg 2x" data-dominant-color="DEDFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1512×1540 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @muratmaga (2023-12-20 06:45 UTC)

<p>I made progress up to a point. Min/Max window level adjustment is really not intuitiuve to work with. So the remaining issue, how can I supress 0 values to be shown in slide views. Since I cannot enter a split range into the threshold value, threshold setting is not very useful.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/776edd4fbe0a550795db3542225f108ee893cd0a.jpeg" data-download-href="/uploads/short-url/h2ylot1ZSwIKGr28J5VSaheMHLY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/776edd4fbe0a550795db3542225f108ee893cd0a_2_690x388.jpeg" alt="image" data-base62-sha1="h2ylot1ZSwIKGr28J5VSaheMHLY" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/776edd4fbe0a550795db3542225f108ee893cd0a_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/776edd4fbe0a550795db3542225f108ee893cd0a_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/776edd4fbe0a550795db3542225f108ee893cd0a_2_1380x776.jpeg 2x" data-dominant-color="71B976"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4454×2508 696 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2023-12-20 06:59 UTC)

<p>In volume rendering I can hack something with manually adjusting things. But I need to be able to do this more consistently with more control over colors, and particularly in 2D as well.<br>
Please provide pointers/suggestions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55bd29efad6c2ec7d1d700d94694da8960d8ce29.jpeg" data-download-href="/uploads/short-url/cetRJauYgHOp9V4NbiVJMVee2GB.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55bd29efad6c2ec7d1d700d94694da8960d8ce29_2_690x387.jpeg" alt="image" data-base62-sha1="cetRJauYgHOp9V4NbiVJMVee2GB" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55bd29efad6c2ec7d1d700d94694da8960d8ce29_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55bd29efad6c2ec7d1d700d94694da8960d8ce29_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55bd29efad6c2ec7d1d700d94694da8960d8ce29_2_1380x774.jpeg 2x" data-dominant-color="66AD72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4466×2508 854 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2023-12-21 00:05 UTC)

<p>Any suggestions to hide 0 values (green background)? <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #6 by @muratmaga (2023-12-21 00:44 UTC)

<p>I tried setting 0 to NaN, but then in slice views it switch to color of minimum value in the dataset (even though the data probe shows it as NaN)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d86d2ced4ddb93b9250bfc6a2cde203efad54d41.jpeg" data-download-href="/uploads/short-url/uSB2xKArr8pkzYEimylfqNwVbsR.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d86d2ced4ddb93b9250bfc6a2cde203efad54d41_2_690x422.jpeg" alt="image" data-base62-sha1="uSB2xKArr8pkzYEimylfqNwVbsR" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d86d2ced4ddb93b9250bfc6a2cde203efad54d41_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d86d2ced4ddb93b9250bfc6a2cde203efad54d41_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/8/d86d2ced4ddb93b9250bfc6a2cde203efad54d41_2_1380x844.jpeg 2x" data-dominant-color="928796"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1176 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2023-12-21 21:25 UTC)

<p>We are still looking for a solution.  <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #8 by @lassoan (2023-12-22 16:05 UTC)

<p>To specify a color transfer function I would recommend using a procedural color node (where you can define any color for any absolute value) instead of a color table (where you specify color values at regular intervals that you later map to some intensity range). See full example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-map-and-display-color-legend">script repository</a>.</p>
<blockquote>
<p>Any suggestions to hide 0 values (green background)?</p>
</blockquote>
<p>Display threshold can be used for hiding background.</p>

---

## Post #9 by @muratmaga (2023-12-22 16:43 UTC)

<p>my values range from negative to positive, zero being in the middle not at the lowest value. How can I just threshold 0, or a range like (-0.0001, 0.00001) ?<br>
There are values close 0 on either side, and they are not discernible if 0 is rendered in the overlay<br>
For example this is the full range<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/5413705f867041b9cc1064b8140d5efa18557941.jpeg" data-download-href="/uploads/short-url/bZLKPliKYQ0c12JeDPXO8VCPfup.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5413705f867041b9cc1064b8140d5efa18557941_2_290x500.jpeg" alt="image" data-base62-sha1="bZLKPliKYQ0c12JeDPXO8VCPfup" width="290" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5413705f867041b9cc1064b8140d5efa18557941_2_290x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5413705f867041b9cc1064b8140d5efa18557941_2_435x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/5413705f867041b9cc1064b8140d5efa18557941_2_580x1000.jpeg 2x" data-dominant-color="466766"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1246×2144 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>negative only (-0.3 to -0.01)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6241ed2a565d3137f8aab9341f2c069d47495da9.jpeg" data-download-href="/uploads/short-url/e1e2peBK95RUOytb2PTwim44mPn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6241ed2a565d3137f8aab9341f2c069d47495da9_2_310x500.jpeg" alt="image" data-base62-sha1="e1e2peBK95RUOytb2PTwim44mPn" width="310" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6241ed2a565d3137f8aab9341f2c069d47495da9_2_310x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6241ed2a565d3137f8aab9341f2c069d47495da9_2_465x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/6241ed2a565d3137f8aab9341f2c069d47495da9_2_620x1000.jpeg 2x" data-dominant-color="515151"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×2158 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>positively only (0.01 to 0.9)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4669a3ac0694779a628f796e8aad02be4c6b2b6.jpeg" data-download-href="/uploads/short-url/wAwGEJHfldUzJ56v8s2oaoefJNY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4669a3ac0694779a628f796e8aad02be4c6b2b6_2_301x500.jpeg" alt="image" data-base62-sha1="wAwGEJHfldUzJ56v8s2oaoefJNY" width="301" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4669a3ac0694779a628f796e8aad02be4c6b2b6_2_301x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4669a3ac0694779a628f796e8aad02be4c6b2b6_2_451x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4669a3ac0694779a628f796e8aad02be4c6b2b6_2_602x1000.jpeg 2x" data-dominant-color="525453"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1308×2170 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want the last two together in the same image.</p>

---

## Post #10 by @lassoan (2023-12-24 14:00 UTC)

<p>Here are two solutions, by modifying an existing discrete color table to be a transparent in the center or a continous mapping function to be black in the center.</p>
<h2><a name="p-104920-option-a-discrete-color-table-1" class="anchor" href="#p-104920-option-a-discrete-color-table-1" aria-label="Heading link"></a>Option A: Discrete color table</h2>
<ul>
<li>Create a discrete color map that has <strong>transparent</strong> color in the middle and a different color on each side
<ul>
<li>Go to Colors module</li>
<li>Select <code>Colors</code> → <code>DivergingBlueRed</code> (a color function that that uses just 3 colors: blue = low<br>
values, white = center, red = high values)</li>
<li>Click <code>Copy</code> button (to create a modifiable copy), accept the proposed default name <code>DivergingBlueRedCopy</code></li>
<li>In the color table, for color 127, set <code>opacity</code> → <code>0</code> (to make the center of the color map transparent, to avoid adding a white haze for values around 0 in the overlay)</li>
</ul>
</li>
<li>Select this color map for the overlay volume
<ul>
<li>Go to Volumes module</li>
<li>Select <code>Active volume</code> → <code>Exp-02...</code></li>
<li>Select <code>Lookup Table</code> → <code>DivergingBlueRedCopy</code></li>
<li>Set Window/Level <code>L</code> → <code>0</code> (to make the center at 0)</li>
</ul>
</li>
<li>Set this colored image as overlay in the slice view controller
<ul>
<li>Select <code>Exp-02...</code> volume as foreground, set its opacity to around 0.5</li>
<li>Select <code>final</code> volume as background</li>
</ul>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a01fca31e94555eb4549f8c2b7b9ddb341ed71d8.jpeg" data-download-href="/uploads/short-url/mQwvhTC9hJKII1X5WSTm2yaHwQU.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01fca31e94555eb4549f8c2b7b9ddb341ed71d8_2_690x338.jpeg" alt="image" data-base62-sha1="mQwvhTC9hJKII1X5WSTm2yaHwQU" width="690" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01fca31e94555eb4549f8c2b7b9ddb341ed71d8_2_690x338.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01fca31e94555eb4549f8c2b7b9ddb341ed71d8_2_1035x507.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a01fca31e94555eb4549f8c2b7b9ddb341ed71d8_2_1380x676.jpeg 2x" data-dominant-color="4C494B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×942 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the abrupt change from transparent to opaque is not desirable then set more colors around the center semitransparent by decreasing their opacity values. It may be easier to do this by editing the color table in a text editor or by Python scripting.</p>
<h2><a name="p-104920-option-b-continuous-color-mapping-2" class="anchor" href="#p-104920-option-b-continuous-color-mapping-2" aria-label="Heading link"></a>Option B: Continuous color mapping</h2>
<p>Opacity cannot be specified for continuous color mapping, so we will use black as center color and use additive image blending.</p>
<ul>
<li>Create a continous color map that has <strong>black</strong> in the middle and a different color on each side
<ul>
<li>Go to Colors module</li>
<li>Select <code>Colors</code> → <code>RedGreenBlue</code> (a color function that that uses just 3 colors: red = low<br>
values, green = center, blue = high values)</li>
<li>Click <code>Copy</code> button (to create a modifiable copy), accept the proposed default name <code>RedGreenBlueCopy</code></li>
<li>Select the middle point (by entering <code>Point</code> → <code>1</code> above the color function editor)</li>
<li>Set center color to black (click on the colored square next to it, set the value to black using the brightness control bar on the right side, and click OK)</li>
</ul>
</li>
<li>Select this color map for the overlay volume
<ul>
<li>Go to Volumes module</li>
<li>Select <code>Active volume</code> → <code>Exp-02...</code></li>
<li>Select <code>Lookup Table</code> → <code>RedGreenBlueCopy</code></li>
<li>Set Window/Level <code>L</code> → <code>0</code> (to make the center at 0)</li>
</ul>
</li>
<li>Select additive image overlay display in the slice view controller
<ul>
<li>Select <code>Exp-02...</code> volume as foreground, set its opacity to 1</li>
<li>Select <code>final</code> volume as background</li>
<li>Click <code>Blend mode</code> icon and choose <code>Add</code></li>
</ul>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ecc7cd476ca888ff1c2bf397f3da4cfd63832a9.jpeg" data-download-href="/uploads/short-url/dwCZGtwnJC9Xhu0P04zVgS0ptC9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ecc7cd476ca888ff1c2bf397f3da4cfd63832a9_2_690x341.jpeg" alt="image" data-base62-sha1="dwCZGtwnJC9Xhu0P04zVgS0ptC9" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ecc7cd476ca888ff1c2bf397f3da4cfd63832a9_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ecc7cd476ca888ff1c2bf397f3da4cfd63832a9_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ecc7cd476ca888ff1c2bf397f3da4cfd63832a9_2_1380x682.jpeg 2x" data-dominant-color="48464C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×950 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<hr>
<p>Creating the color table is somewhat tedious, so it could make sense to add a transparent/black centered color table to the presets.</p>

---
