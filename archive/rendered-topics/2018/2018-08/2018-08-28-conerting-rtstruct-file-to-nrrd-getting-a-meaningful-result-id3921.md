# Conerting RTstruct file to nrrd : Getting a meaningful result with correct dimensions?

**Topic ID**: 3921
**Date**: 2018-08-28
**URL**: https://discourse.slicer.org/t/conerting-rtstruct-file-to-nrrd-getting-a-meaningful-result-with-correct-dimensions/3921

---

## Post #1 by @sdoken (2018-08-28 13:38 UTC)

<p>Operating system: MacOS<br>
Slicer version: 4.9.0.-2018-08-04<br>
Expected behavior: Produce nrrd file with 15x512x512x128 dimensions<br>
Actual behavior: Finding nrrd file with 15x357x211x128 dimensions</p>
<p>Hi All,</p>
<ol>
<li>
<p>Would someone be able to post step by step instructions for converting an RTstruct file to an nrrd file?<br>
I am new to 3dslicer and am finding the program and its UI rather confusing. I believe screenshots would be helpful.</p>
</li>
<li>
<p>I tried to follow the question <a href="https://discourse.slicer.org/t/how-can-i-convert-an-rtstruct-to-an-nrrd/539">here</a> and I think that I did it correctly. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4f1ad09390382e66648c9596ce4313f836a3548.png" data-download-href="/uploads/short-url/wFkEovyGkmLA1GihijDxiMw44OY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4f1ad09390382e66648c9596ce4313f836a3548_2_690x431.png" alt="image" data-base62-sha1="wFkEovyGkmLA1GihijDxiMw44OY" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4f1ad09390382e66648c9596ce4313f836a3548_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4f1ad09390382e66648c9596ce4313f836a3548_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4f1ad09390382e66648c9596ce4313f836a3548_2_1380x862.png 2x" data-dominant-color="CDCCD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2196×1374 458 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However, I am getting what looks to me like a weird result because the dimensions of the nrrd coming from the rtstruct file are kind of weird.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58e2f53d4087519be82ca95a3be33bc9a5922267.png" data-download-href="/uploads/short-url/cGkgTRVYnLHdghBYcWclTno33r9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58e2f53d4087519be82ca95a3be33bc9a5922267_2_690x439.png" alt="image" data-base62-sha1="cGkgTRVYnLHdghBYcWclTno33r9" width="690" height="439" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58e2f53d4087519be82ca95a3be33bc9a5922267_2_690x439.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58e2f53d4087519be82ca95a3be33bc9a5922267_2_1035x658.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/58e2f53d4087519be82ca95a3be33bc9a5922267_2_1380x878.png 2x" data-dominant-color="F6F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1554×990 84.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Why would I get a (15, 357, 211, 128) matrix as a result of converting the rtstruct associated with a 512x512 image series. The 15 makes sense since there are 15 structures, the 128 makes sense since there are 128 images but why is it 357x211 and not 512x512?</p>
<p>This dimension issue is not only not making sense to me but is also causing the size mismatch issue when I try to run pyradiomics to calculate feature on the structures.</p>
<p>I am new to 3dslicer and image analysis and appreciate your patience very much. I have tried other software solutions like plastimatch to do this conversion and having a difficulty with the dimensions there as well where I will get a 3x512x512x128 instead of 15x512x512x128.</p>
<p>I am wondering if I should try to write a script that generates nrrds from RTstruct myself. Thanks a bunch again for any help.</p>

---

## Post #2 by @cpinter (2018-08-28 14:56 UTC)

<p>The dimensions you get are the union of the “effective extents” of your structures, i.e. the region that contains data. You can export it with any geometry if you set a reference volume in the Import/Export section of the Segmentations module.</p>
<p>You can also automatically do such conversion using <a href="https://github.com/SlicerRt/SlicerRT/tree/master/BatchProcessing">this module</a> in SlicerRT.</p>

---
