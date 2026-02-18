# How to use Screen Capture Module to save slices as .png files one-by-one along one axial?

**Topic ID**: 21336
**Date**: 2022-01-05
**URL**: https://discourse.slicer.org/t/how-to-use-screen-capture-module-to-save-slices-as-png-files-one-by-one-along-one-axial/21336

---

## Post #1 by @user4 (2022-01-05 11:52 UTC)

<p>Hi all,this is the thing I want to do:<br>
I need to save all the ROI slice png files along one axial.For example,I need to save the slices from -20 to 20 along I-S axial according to the volume spacing information.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9162b7fffd19a1a048a9ff6447a8d2ac535bc2b1.png" data-download-href="/uploads/short-url/kK8JHE99MS6rsHbO64Rj0JCdEtP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9162b7fffd19a1a048a9ff6447a8d2ac535bc2b1.png" alt="image" data-base62-sha1="kK8JHE99MS6rsHbO64Rj0JCdEtP" width="690" height="245" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">905×322 12.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Manually,I first change the ROI I-S range -20 to -19.90 as follows<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d91fcdaaebb958b141ef819d93a0a52bd2f9961f.png" data-download-href="/uploads/short-url/uYLKtd7pcgYbaOTydHFeHhnthIb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d91fcdaaebb958b141ef819d93a0a52bd2f9961f.png" alt="image" data-base62-sha1="uYLKtd7pcgYbaOTydHFeHhnthIb" width="690" height="69" data-dominant-color="F5F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">893×90 4.13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then,I take a screen shot and save the png picture<br>
Next,I change the ROI I-S range -19.90 to -19.80 as follows<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba87a1213935ef4ce06c33f01dac37ad7200d835.png" data-download-href="/uploads/short-url/qC7orep0GxrDQiMQ2ufhGDM6fVX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba87a1213935ef4ce06c33f01dac37ad7200d835.png" alt="image" data-base62-sha1="qC7orep0GxrDQiMQ2ufhGDM6fVX" width="690" height="77" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">884×99 4.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then,I take a screen shot and save the png picture again.<br>
So, I need to repeat this operation 400 times to save all the slices along one axial which is super-boring and time waste.<br>
Is there any way to do it automatically?Thank you for any possible advice in advance.</p>

---

## Post #2 by @rbumm (2022-01-05 14:42 UTC)

<p>Hi,</p>
<p>I would recommend using the “Utilities” -&gt;“Screen Capture” extension for this purpose.</p>

---

## Post #3 by @rbumm (2022-01-05 15:45 UTC)

<p>To capture 31 images of a a series the “Red” view you could use:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c7f5a3ebf8d77893ed83759febd14ba6bd2b9f.png" data-download-href="/uploads/short-url/kWu7yZX46cCG1FS1hcpvXFD8Vqv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92c7f5a3ebf8d77893ed83759febd14ba6bd2b9f.png" alt="image" data-base62-sha1="kWu7yZX46cCG1FS1hcpvXFD8Vqv" width="442" height="499" data-dominant-color="EDEDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">538×608 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @user4 (2022-01-06 06:07 UTC)

<p>Sadly,this is Red slice is not the slice after volume rendering.The slice is controlled by window level but what I did is to get the slice after ray casting.</p>

---

## Post #5 by @rbumm (2022-01-06 07:55 UTC)

<p>Slicer 4.13.0:<br>
For recording the 3D view you can go to “Sequences”, create a new SequenceBrowser, select “Camera” as a Proxy node, and record the sequence that you want to generate the PNG file series from.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2d164a1a651e6ea4dde43359552dba8e27db623.png" alt="image" data-base62-sha1="rNrfCi3IIWgaVEILiB3kPZ3NEMr" width="575" height="457"></p>
<p>Then go to the “Screen Capture” extension, select animation mode → sequence, select the SequenceBrowser you created before and use “output type” → image series. Press “Capture” to create the PNG files.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e5226fe170b7d62e9e6d12fb92103ce5477dfaf.png" data-download-href="/uploads/short-url/8TjC31xBlWuKdm1vHLlfcU3e35J.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e5226fe170b7d62e9e6d12fb92103ce5477dfaf.png" alt="image" data-base62-sha1="8TjC31xBlWuKdm1vHLlfcU3e35J" width="414" height="500" data-dominant-color="F5F5F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">561×676 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @user4 (2022-01-06 09:41 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="21336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>record the sequence that you want to generate the PNG file series from.</p>
</blockquote>
</aside>
<p>Thanks Rudolf,<br>
What did you mean by record the sequence?I need to snapshot along one axial from bottom to top and if the volume is a 300x300x400 cube and I use the I-S orientation ,so I need to record 400 slice png files.Can you describe it in detail?Thanks for your help.</p>

---

## Post #7 by @rbumm (2022-01-06 10:43 UTC)

<p>Please post a screenshot of what you want to record exactly, maybe two of the png that you created, and tell us what you did in between to switch from png1 to png2.</p>

---

## Post #8 by @mikebind (2022-01-06 17:42 UTC)

<p>Volume rendering creates a 2D image by casting rays through a 3D volume and applying transfer functions for opacity and color for voxels encountered along each ray.  If I understand what you are trying to accomplish, you are clipping the volume rendering so that it shows data from only one axial slice at a time, and you are trying to go slice by slice and capture the volume rendering data into a stack of png images.</p>
<p>If you are interested in slice-by-slice data, then you don’t need volume rendering at all because ray casting is unnecessary. You can just convert your image volume into png files one slice at a time, using the same kind of transfer functions to translate image voxel values into png pixel values. This can be fairly easily accomplished with a small amount of python code.</p>
<p>If you just want to visualize your data (e.g. with color and/or transparency) and don’t actually need the individual png files, you may also be able to accomplish your goal by creating a custom lookup table which you can apply to the volume, and then all slice views will show the colorized data.</p>
<p>What is your ultimate goal?  What do you want to do with the png files if you could generate them?</p>

---

## Post #9 by @user4 (2022-01-07 02:14 UTC)

<p>Thanks Mike,<br>
You are very clever.My ultimate goal is to get the visualized data after ray casting.I want all the slice png files because I want to stack these 2D image back to a 3D volume.<br>
Since I have tried to accomplish this goal directly several times by rendering myself using python code,I was stucked with creating lookup table and I can’t figure out how to apply the transfer functions to raw volume.</p>

---

## Post #10 by @user4 (2022-01-07 03:01 UTC)

<p>Thanks Rudolf,<br>
Please let me show you two steps about what I am doing right now.<br>
In the begining,I apply transfer functions such as Scalar Opacity Mapping and Gradient Opacity to my raw volume and become like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c7f87ab9124a75a86159ef16f5fd1f383d4462b.png" data-download-href="/uploads/short-url/8DbSyn6JcIUaO1Fg8N1NhP0WLwv.png?dl=1" title="2021-07-28-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c7f87ab9124a75a86159ef16f5fd1f383d4462b_2_565x500.png" alt="2021-07-28-Scene" data-base62-sha1="8DbSyn6JcIUaO1Fg8N1NhP0WLwv" width="565" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c7f87ab9124a75a86159ef16f5fd1f383d4462b_2_565x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3c7f87ab9124a75a86159ef16f5fd1f383d4462b_2_847x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3c7f87ab9124a75a86159ef16f5fd1f383d4462b.png 2x" data-dominant-color="030706"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-07-28-Scene</span><span class="informations">1046×925 90.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I check the Volume information and this is a 300x300x400 volume and the spacing is 0.1mm so I need to slice by 0.1mm along one axial at one time.Then I go to volume rendering module and begin to slice the ROI.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c94cc9f239910e42df201b829a96ea07d5db24e4.png" data-download-href="/uploads/short-url/sIMur5p24ubOzE2CSRt9MIKFIri.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c94cc9f239910e42df201b829a96ea07d5db24e4.png" alt="image" data-base62-sha1="sIMur5p24ubOzE2CSRt9MIKFIri" width="690" height="98" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">914×130 3.34 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
First,I select the I-S orientation and do one slice like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/188a54267f2dac53e41f46cae1dfe35292202762.png" data-download-href="/uploads/short-url/3v5PhIBFWHeVH7oUsfqsWlx0Esa.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/188a54267f2dac53e41f46cae1dfe35292202762_2_690x144.png" alt="image" data-base62-sha1="3v5PhIBFWHeVH7oUsfqsWlx0Esa" width="690" height="144" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/188a54267f2dac53e41f46cae1dfe35292202762_2_690x144.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/188a54267f2dac53e41f46cae1dfe35292202762_2_1035x216.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/188a54267f2dac53e41f46cae1dfe35292202762_2_1380x288.png 2x" data-dominant-color="D2D3E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1683×352 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then I take a 3D screen shot:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5e6701e71884b5424014353e8dc39de6db70e56.png" alt="image" data-base62-sha1="pXa8g4sHesNXx6xotysbYDbPsSq" width="507" height="458"><br>
Next,I change the I-S Range in ROI,like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5ccb49596ec443ae766df21f19c35d001ee18a89.png" data-download-href="/uploads/short-url/deTsVMeWKTP2s1JY8zs9JlYQaxz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5ccb49596ec443ae766df21f19c35d001ee18a89_2_690x128.png" alt="image" data-base62-sha1="deTsVMeWKTP2s1JY8zs9JlYQaxz" width="690" height="128" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5ccb49596ec443ae766df21f19c35d001ee18a89_2_690x128.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5ccb49596ec443ae766df21f19c35d001ee18a89_2_1035x192.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5ccb49596ec443ae766df21f19c35d001ee18a89_2_1380x256.png 2x" data-dominant-color="CFD0E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1782×332 19.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Then,I take anther screen shot.<br>
0.1mm one step,the whole process continues when I reach say I-S Range  6.9 to 7.0 which means I have sliced all the png files from bottom to top.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59c3f327c4426a496fb9f409b2e08cba3b4415e7.jpeg" data-download-href="/uploads/short-url/cO6jywZtmsOtfCIvCCJ1K5hd5MH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59c3f327c4426a496fb9f409b2e08cba3b4415e7_2_690x135.jpeg" alt="image" data-base62-sha1="cO6jywZtmsOtfCIvCCJ1K5hd5MH" width="690" height="135" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59c3f327c4426a496fb9f409b2e08cba3b4415e7_2_690x135.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59c3f327c4426a496fb9f409b2e08cba3b4415e7_2_1035x202.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59c3f327c4426a496fb9f409b2e08cba3b4415e7_2_1380x270.jpeg 2x" data-dominant-color="C7CDE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1808×355 94.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @rbumm (2022-01-07 13:31 UTC)

<p>Thank you.</p>
<p>This can not be done with the Screen Capture Module alone and will probably need a small Python program that  (1) iterates through the I-S range values of Volume Rendering and (2) takes a screenshot of the 3D window with every new value pair.</p>
<p>It is quite easy to involve Slicer extensions in Python programs. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-using-maximum-intensity-projection" rel="noopener nofollow ugc">this link</a> in Slicer’s script repository for an example on how to programmatically call Volume Rendering and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-a-series-of-images-from-a-slice-view" rel="noopener nofollow ugc">this link</a> on how to save screenshots in a Python script.</p>
<p>Are you sure your workflow can not be simplified by just segmenting your structures with the “Segment Editor”? This extension offers excellent effects which can solve nearly every segmentation problem and you would not need to “stack” anything.</p>

---

## Post #12 by @jamesobutler (2022-01-07 15:27 UTC)

<p><a class="mention" href="/u/user4">@user4</a> It appears you are just trying to resample your volume along a newly defined set of axes? See some details at <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" class="inline-onebox" rel="noopener nofollow ugc">Overview | 3D Slicer segmentation recipes</a> where there is a “Option B. Create resampled volume with rotated axes” section.</p>

---

## Post #13 by @mikebind (2022-01-07 17:14 UTC)

<p>Stacking the set of screen captures you would gather using the procedure you outline, <a class="mention" href="/u/user4">@user4</a>, would not result in a 3D volume which corresponds to the original image volume geometry.  Because you are viewing the the slices from an oblique angle in the 3D view, the series of png images you would get out would be like frames of a movie showing the volume rendering of each slice from exactly the current perspective. Perhaps that is what you want, but I suspect not, because this is not what you would accomplish by applying transfer functions to the raw volume.</p>
<p>I noticed that this question is probably related to the prior discussion here: <a href="https://discourse.slicer.org/t/how-to-save-the-volume-pixel-data-in-display-area/20674" class="inline-onebox">How to save the volume pixel data in display area?</a></p>
<p>If your goal is to get a vessel mask, the segmentation approach suggested by <a class="mention" href="/u/rbumm">@rbumm</a> is likely to be the best one. Find a segmentation approach which identifies the voxels you want to include in your mask, convert the mask segment to a labelmap volume, and then use Mask Scalar Volume to apply the mask to your original volume.  There are many segmentation approaches which look like they would be easily successful for the data you have. A few suggestions of possible approaches would be:</p>
<ul>
<li>thresholding followed by getting rid of small islands</li>
<li>painting with a large brush and a restricted intensity range</li>
<li>grow from seeds</li>
</ul>
<p>You can get a sense of the segmentation tools available and how to use them here: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html" class="inline-onebox">Segment editor — 3D Slicer documentation</a></p>

---

## Post #14 by @user4 (2022-01-10 10:33 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="13" data-topic="21336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>Because you are viewing the the slices from an oblique angle in the 3D view, the series of png images you would get out would be like frames of a movie showing the volume rendering of each slice from exactly the current perspective.</p>
</blockquote>
</aside>
<p>Thanks Mike,I do this thing with a fixed perspective in display area and I will not change it.<br>
Later I will try it with the segmentation approach.</p>

---

## Post #15 by @user4 (2022-01-10 10:37 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="11" data-topic="21336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>(1) iterates through the I-S range values of Volume Rendering</p>
</blockquote>
</aside>
<p>I have seen through the script repository and still don’t know how to iterate through the I-S range.Can you show me some detailed code or something? It will be really really helpful!!</p>
<aside class="quote no-group" data-username="rbumm" data-post="11" data-topic="21336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>(2) takes a screenshot of the 3D window with every new value pair.</p>
</blockquote>
</aside>
<p>This step is already completed and I have sucessfully taken shots using python code.</p>

---

## Post #16 by @rbumm (2022-01-10 12:35 UTC)

<p>I do not have a complete working / sharable recipe for that, but you would probably need to limit volume rendering to a specific ROI like <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#limit-volume-rendering-to-a-specific-region-of-the-volume" rel="noopener nofollow ugc">shown here</a>.<br>
Generally, I would recommend following the segmentation approach.</p>

---

## Post #17 by @mikebind (2022-01-10 16:21 UTC)

<p>To iterate through the I-S range, you can set up the first range interactively (as you have already done).  Then, you can iterate through positions by getting the ROI node and calling <code>roi.SetCenterPositionWorld( newPos )</code>.</p>
<pre><code class="lang-auto">import numpy as np
roiName = 'R' # replace this with whatever your ROI is named
roi = getNode(roiName)
startingRoiCenter = np.zeros(3) # allocate position vector
roi.GetCenterPositionWorld(StartingRoiCenter) # fill in position vector
for centerSuperiorOffset in range(0,40,0.01):
    newRoiCenter = startingRoiCenter + np.array([0, 0, centerSuperiorOffset])
    roi.SetCenterPositionWorld(newRoiCenter)
    # Insert your screen capture code here
</code></pre>

---

## Post #22 by @user4 (2022-01-11 12:12 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="17" data-topic="21336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>roi.SetCenterPositionWorld( newPos )</p>
</blockquote>
</aside>
<p>Thanks Mike very very much for this code!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e43595a56db1e7e674421b8101d65b9e9ed84c2c.png" data-download-href="/uploads/short-url/wyPFoq1YA3Uzqk8JXlFbvTva60k.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e43595a56db1e7e674421b8101d65b9e9ed84c2c.png" alt="image" data-base62-sha1="wyPFoq1YA3Uzqk8JXlFbvTva60k" width="690" height="126" data-dominant-color="FADFDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1203×220 6.28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I haven’t seen your method but otherwise found this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcd9b249876dade6d3346f56d3e2b73c7e8eb0ba.png" data-download-href="/uploads/short-url/qWEaY1dK0jd2mbG6aX4GLyyWrPA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcd9b249876dade6d3346f56d3e2b73c7e8eb0ba.png" alt="image" data-base62-sha1="qWEaY1dK0jd2mbG6aX4GLyyWrPA" width="690" height="108" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1082×170 5.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I think this Get/Set method is what you mean?</p>
<p>So I have completed this code as follows:</p>
<pre><code class="lang-auto">suffix = 0
startingRoiCenter = np.array([0,0,-19.95]) 
for centerSuperiorOffset in np.arange(0,40,0.1):
    newRoiCenter = startingRoiCenter + np.array([0, 0, centerSuperiorOffset])
    roi.SetXYZ(newRoiCenter)
    take_one_screen_shot(suffix)
    suffix+=1
</code></pre>
<pre><code class="lang-auto"># Capture RGBA image
def take_one_screen_shot(suffix):
    renderWindow = view.renderWindow()
    renderWindow.SetAlphaBitPlanes(1)
    wti = vtk.vtkWindowToImageFilter()
    wti.SetInputBufferTypeToRGBA()
    wti.SetInput(renderWindow)
    writer = vtk.vtkPNGWriter()
    writer.SetFileName("c:/tmp/screen_shot"+str(suffix)+".png")
    writer.SetInputConnection(wti.GetOutputPort())
    writer.Write()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e4a486c1e8f384c504232e7e5079bcbbdb4af23.png" data-download-href="/uploads/short-url/ds821jIYuUM27Eo5hdsORH3x7cn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5e4a486c1e8f384c504232e7e5079bcbbdb4af23.png" alt="image" data-base62-sha1="ds821jIYuUM27Eo5hdsORH3x7cn" width="690" height="471" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×746 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>yeah,thanks for you,I did this slice thing along I-S range from -20 to +20 with step 0.1.<br>
However I still got a quesiton maybe you can help me again, I will be very grateful. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"><br>
I set the startingRoiCenter as follows:<br>
<code>startingRoiCenter = np.array([0,0,-19.95])</code><br>
-19.95 as a center and it gives both left range and right range 0.05,so the begining range is from -20 to -19.90.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08ba9f8eb16bed045700a28a044580ab77ad1daa.png" alt="image" data-base62-sha1="1fdEOq2pQa0Xl1VjFnkC9a0nx7I" width="559" height="142"><br>
run the code above and produced below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85af0c8f70551532c9e78ae93f69d68a147c8f6b.png" data-download-href="/uploads/short-url/j4CxKTPERpzLgwnAfXPZwtXbpAn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85af0c8f70551532c9e78ae93f69d68a147c8f6b.png" alt="image" data-base62-sha1="j4CxKTPERpzLgwnAfXPZwtXbpAn" width="690" height="180" data-dominant-color="F6F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">986×258 12.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I noticed the center is giving both sides 0.05mm,so it is 0.1mm between left and right.Is this number fixed?For example,say,I want to have a slice with <strong>0.15mm not 0.1mm</strong> from -20 to +20 along I-S orientation,how to set up the iteration?<br>
Thank you for your help again,it does help a lot!</p>

---

## Post #23 by @mikebind (2022-01-11 16:07 UTC)

<p>You’re welcome, I’m glad it was helpful!</p>
<p>Markups, including the ROI markup, has undergone a lot of revision recently, and the <code>SetCenterPositionWorld()</code> function is part of the updated versions (present in the current Slicer “preview” release).  It looks like you are using an older version of Slicer where the ROI is from the “Annotations” module instead (this was the former default for ROIs). You are correct that the analogous function for Annotations ROIs is <code>SetXYZ()</code>.</p>
<aside class="quote no-group" data-username="user4" data-post="22" data-topic="21336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/user4/48/13172_2.png" class="avatar"> user4:</div>
<blockquote>
<p>I noticed the center is giving both sides 0.05mm,so it is 0.1mm between left and right.Is this number fixed?For example,say,I want to have a slice with <strong>0.15mm not 0.1mm</strong> from -20 to +20 along I-S orientation,how to set up the iteration?</p>
</blockquote>
</aside>
<p>The thickness of the volume rendered region is not changed during the iteration in the code above, so the simplest way to change the thickness is to manually change it in the volume rendering module before you start (for example by entering -20 and -19.85 as the ends of the I-S range).</p>
<p>If you want to change this in python code, you can use the <code>SetRadiusXYZ()</code> function and change the Z radius to half your desired slice thickness. Both <a href="https://apidocs.slicer.org/master/classvtkMRMLAnnotationROINode.html">Annotation</a> and <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsROINode.html">Markups ROIs</a> have <code>SetRadiusXYZ()</code> methods.</p>

---

## Post #24 by @user4 (2022-01-12 02:52 UTC)

<p>Thanks Mike,<br>
it really works and you do help me a lot! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #25 by @user4 (2022-07-13 02:07 UTC)

<p>Hi,Mike.<br>
Sorry for reopening this topic,but I think you may help me.As we said before,</p>
<ol>
<li>iterates through the I-S range values of Volume Rendering</li>
<li>takes a screenshot of the 3D window</li>
</ol>
<p>No problem with the above two and I have created a python Script Module for that,however,every time I move the ROI and take a screenshot , the 3D window does not display the corresponding ROI area. Is there a way to dynamically display the ROI movement in real time?<br>
By the way, I attached the source code of the module.<a href="https://github.com/ningmenghongcha/takeScreenshots" rel="noopener nofollow ugc">https://github.com/ningmenghongcha/takeScreenshots</a></p>

---

## Post #26 by @muratmaga (2022-07-13 03:21 UTC)

<p>By the way did you check out the <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/Animator" rel="noopener nofollow ugc">Animator module in SlicerMorph extension</a>. It simplifies going ROI and volume rendering quite a lot. See an <a href="https://www.youtube.com/watch?v=9GBekYcJR4E" rel="noopener nofollow ugc">older demo here:</a></p>

---

## Post #27 by @mikebind (2022-07-13 15:55 UTC)

<p>You may just need to add a call to <code>slicer.app.processEvents()</code> in your loop to trigger the update of the 3D window display.</p>

---

## Post #28 by @user4 (2022-07-14 02:35 UTC)

<p>It really works!Thank you very very much,Mike.You saved my a lot of work!<br>
It seems like this function calls a thread to process the events,so I can do other things in Slicer application.<br>
I have a question as follows,<br>
At first,if I don’t call this function,the Slicer application looks dead and no response in that case user can not interfere the event.But if I call this function to update in real time,in the meantime,I can rotate the image in 3D window so the screenshots are not correct at last.<br>
Can I add a lock to prevent other changes made in 3D window, such as zoom-in or rotation when moving roi and taking screenshots?</p>

---

## Post #29 by @pieper (2022-07-14 03:26 UTC)

<p>Try passing the <code>qt.QEventLoop.ExcludeUserInputEvents</code> value as a flag to the <code>processEvents</code> call.</p>
<p><a href="https://doc.qt.io/qt-5/qcoreapplication.html#processEvents" class="onebox" target="_blank" rel="noopener">https://doc.qt.io/qt-5/qcoreapplication.html#processEvents</a></p>

---
