# Problem in Volume Rendering

**Topic ID**: 6933
**Date**: 2019-05-27
**URL**: https://discourse.slicer.org/t/problem-in-volume-rendering/6933

---

## Post #1 by @doc-xie (2019-05-27 08:47 UTC)

<p>Hello everyone,<br>
In the Volume Rendering module, the image is very small location in the corner of the 3D tube. The information about this showed "irregular volume geometry detected. What is the reason about this and how to correct it?<br>
Thanks,<br>
Xie</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64633f7fbbadfdbd15c6fde4c62c87d7c2bc6a4f.png" data-download-href="/uploads/short-url/ek4nRVjhPLqLMIOaeYxXt7s3vyf.png?dl=1" title="40%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64633f7fbbadfdbd15c6fde4c62c87d7c2bc6a4f_2_675x500.png" alt="40%20PM" data-base62-sha1="ek4nRVjhPLqLMIOaeYxXt7s3vyf" width="675" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64633f7fbbadfdbd15c6fde4c62c87d7c2bc6a4f_2_675x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64633f7fbbadfdbd15c6fde4c62c87d7c2bc6a4f_2_1012x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64633f7fbbadfdbd15c6fde4c62c87d7c2bc6a4f_2_1350x1000.png 2x" data-dominant-color="C5C8DA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">40%20PM</span><span class="informations">2820×2088 800 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-05-27 12:28 UTC)

<p>885.15mm error indicates that there is an error in the DICOM series. You can use the DICOM module to inspect slice positions and find the offending file(s) as described <a href="https://discourse.slicer.org/t/problem-about-image-are-not-equally-spaced/4482/4">here</a>.</p>

---

## Post #4 by @doc-xie (2019-05-28 03:09 UTC)

<p>Hi Lassoan,<br>
After I reopened the Slicer and loaded the DICOM data again. The image looked like normally, but the error information showed as following.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/c/4c28d6255f322d1d2fd1c0698246b58b657c2f89.jpeg" data-download-href="/uploads/short-url/aRJMkEZGVb6zOs0wFFP9GBRScm5.jpeg?dl=1" title="43%20AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c28d6255f322d1d2fd1c0698246b58b657c2f89_2_673x500.jpeg" alt="43%20AM" data-base62-sha1="aRJMkEZGVb6zOs0wFFP9GBRScm5" width="673" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c28d6255f322d1d2fd1c0698246b58b657c2f89_2_673x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c28d6255f322d1d2fd1c0698246b58b657c2f89_2_1009x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4c28d6255f322d1d2fd1c0698246b58b657c2f89_2_1346x1000.jpeg 2x" data-dominant-color="B9BAC9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">43%20AM</span><span class="informations">2814×2088 898 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Here is the information about the CT data.</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://pan.baidu.com/s/1-6okRaFTuoj4-5GZ3pDK0A">
  <header class="source">
      <img src="https://pan.baidu.com/m-static/base/static/images/favicon.ico" class="site-icon" width="" height="">

      <a href="https://pan.baidu.com/s/1-6okRaFTuoj4-5GZ3pDK0A" target="_blank" rel="noopener nofollow ugc">pan.baidu.com</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://pan.baidu.com/s/1-6okRaFTuoj4-5GZ3pDK0A" target="_blank" rel="noopener nofollow ugc">百度网盘-链接不存在</a></h3>

  <p>百度网盘为您提供文件的网络备份、同步和分享服务。空间大、速度快、安全稳固，支持教育网加速，支持手机端。注册使用百度网盘即可享受免费存储空间</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Thanks,<br>
Xie</p>

---

## Post #5 by @pieper (2019-05-28 16:28 UTC)

<p>Hi <a class="mention" href="/u/doc-xie">@doc-xie</a> - If my translator app is working right, then it’s telling me I need to login to download.  Is there a way you can share a direct download link?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1383a0002fff442d8866b0ac9dd7b81479087c6.png" data-download-href="/uploads/short-url/rziCeplER7MnLjAxaNbmdCZwCVg.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1383a0002fff442d8866b0ac9dd7b81479087c6_2_455x500.png" alt="image" data-base62-sha1="rziCeplER7MnLjAxaNbmdCZwCVg" width="455" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c1383a0002fff442d8866b0ac9dd7b81479087c6_2_455x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1383a0002fff442d8866b0ac9dd7b81479087c6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1383a0002fff442d8866b0ac9dd7b81479087c6.png 2x" data-dominant-color="B7B7B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">496×544 26.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @doc-xie (2019-05-29 04:54 UTC)

<p>Hi Steve,<br>
Sorry for the complicated precess. I have uploaded the file successfully into Onedrive and sharing with you now.<br>
<a href="https://1drv.ms/x/s!AkUOMHTR1-SrcQ_bXr3B3D3c8Mk" class="onebox" target="_blank" rel="nofollow noopener">https://1drv.ms/x/s!AkUOMHTR1-SrcQ_bXr3B3D3c8Mk</a><br>
Thanks,<br>
Xie</p>

---

## Post #7 by @doc-xie (2019-05-29 04:55 UTC)

<p>Hi Lassoan,<br>
I have uploaded the file successfully into Onedrive and sharing with you now.<br>
<a href="https://1drv.ms/x/s!AkUOMHTR1-SrcQ_bXr3B3D3c8Mk" class="onebox" target="_blank" rel="nofollow noopener">https://1drv.ms/x/s!AkUOMHTR1-SrcQ_bXr3B3D3c8Mk</a><br>
Thanks,<br>
Xie</p>

---

## Post #8 by @pieper (2019-05-29 21:01 UTC)

<p>Hi <a class="mention" href="/u/doc-xie">@doc-xie</a> -</p>
<p>I believe <a class="mention" href="/u/lassoan">@lassoan</a> was thinking that you could type “Image” into the metadata filter field so that only the ImageOrientationPatient and ImagePositionPatient fields would show up and then it’s possible to quickly scroll through all of the image files and see how the numbers are changing.  In particular for an axial CT it’s the last number in the ImagePositionPatient that determines the relative locations of the slices and they should be smoothly incrementing slice by slice, but maybe they are not for this dataset.  If you find slice that appear out of place you could remove those from the directory and then try re-importing.  When you see an issue with irregular geometry and a very large error it can mean that there are missing slices or extra slices that throw off the computation and lead to the unusually large bounding box like in your first screenshot.  Unfortunately as Andras mentioned it probably means the data is non-standard in some way we can’t automatically account for.  If you find a way to share an anonymized copy that still exhibits this error we could look more closely.</p>

---
