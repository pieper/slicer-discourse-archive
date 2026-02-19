---
topic_id: 18095
title: "Grey Level Image Looking Blue Or Other Color"
date: 2021-06-12
url: https://discourse.slicer.org/t/18095
---

# Grey Level Image looking Blue (or other color)

**Topic ID**: 18095
**Date**: 2021-06-12
**URL**: https://discourse.slicer.org/t/grey-level-image-looking-blue-or-other-color/18095

---

## Post #1 by @MachadoL (2021-06-12 20:11 UTC)

<p>Hey guys recurrently I get into this situation. I have a gray scale medical image, but when I load the image inside 3D slicer… the image appears BLUE!<br>
Take a look. It is like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a68d7a88c9e53fb4218a2dbf2153176d20f44f13.jpeg" data-download-href="/uploads/short-url/nLonm31ojaDESFIHnHnpePuY2L9.jpeg?dl=1" title="WhatsApp Image 2021-06-11 at 17.49.48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a68d7a88c9e53fb4218a2dbf2153176d20f44f13_2_300x200.jpeg" alt="WhatsApp Image 2021-06-11 at 17.49.48" data-base62-sha1="nLonm31ojaDESFIHnHnpePuY2L9" width="300" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a68d7a88c9e53fb4218a2dbf2153176d20f44f13_2_300x200.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a68d7a88c9e53fb4218a2dbf2153176d20f44f13_2_450x300.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a68d7a88c9e53fb4218a2dbf2153176d20f44f13_2_600x400.jpeg 2x" data-dominant-color="6C6C6C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2021-06-11 at 17.49.48</span><span class="informations">1280×669 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But appears like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98cf839fe6636e9a5ed54744c0a9fe1bf4ff1b7e.jpeg" data-download-href="/uploads/short-url/lNPaHfKkiKp6UmlFW0rshj0b5ka.jpeg?dl=1" title="WhatsApp Image 2021-06-11 at 17.49.34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98cf839fe6636e9a5ed54744c0a9fe1bf4ff1b7e_2_300x300.jpeg" alt="WhatsApp Image 2021-06-11 at 17.49.34" data-base62-sha1="lNPaHfKkiKp6UmlFW0rshj0b5ka" width="300" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98cf839fe6636e9a5ed54744c0a9fe1bf4ff1b7e_2_300x300.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98cf839fe6636e9a5ed54744c0a9fe1bf4ff1b7e_2_450x450.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98cf839fe6636e9a5ed54744c0a9fe1bf4ff1b7e_2_600x600.jpeg 2x" data-dominant-color="032727"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">WhatsApp Image 2021-06-11 at 17.49.34</span><span class="informations">1070×1040 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Could’n find out why.<br>
Any help is welcomed.</p>
<p>Leo.</p>

---

## Post #2 by @steffen-o (2021-06-15 10:44 UTC)

<p>Did you change the color lookup table in the --&gt;Volumes Module --&gt;Display --&gt;Lookup table<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d05926b81bb7460878f451352e1b98673f7717f2.png" alt="image" data-base62-sha1="tJ8jOefD22ft3SnWXtGQYHfb0rM" width="666" height="325"></p>

---

## Post #3 by @lassoan (2021-06-15 17:16 UTC)

<p>I guess it is a secondary capture, stored as a color image. Older ITK versions did not always read color channels correctly, but current version should work well. Does the image appear correctly if you use the latest Slicer Preview Release?</p>

---

## Post #4 by @MachadoL (2021-06-15 19:08 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/steffen-o">@steffen-o</a>,<br>
I just got it. The original file is <strong>BPM</strong>… once converted to <strong>jpg or png…</strong>, it appears in GREY as it should.</p>
<p>If you have any practical way to do that without needing any other secondary software, but inside 3D Slicer, that would be great.</p>
<p>Thanks, Leo.</p>

---

## Post #5 by @lassoan (2021-06-15 21:13 UTC)

<p>It seems that ITK’s BMP reader still mixes up the channels if you use transparency. You can fix the order using this code snippet:</p>
<pre><code class="lang-python">volumeNode=slicer.util.loadVolume(r'c:\Users\andra\OneDrive\15-14-49.bmp')
a=slicer.util.arrayFromVolume(volumeNode)
a[:]=a[:,:,:,[1,2,3,0]]  # reorder color channels
slicer.util.arrayFromVolumeModified(volumeNode)
</code></pre>
<p>BMP is a very old file format that and transparency was never widely used or supported by applications. I would recommend to switch to the much more widely used png file format. I’ve submitted a bug report to ITK, but I will not be surprised if they don’t fix a very rarely used feature of an ancient file format.</p>
<aside class="onebox githubissue">
  <header class="source">

      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/2596" target="_blank" rel="noopener">github.com/InsightSoftwareConsortium/ITK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/InsightSoftwareConsortium/ITK/issues/2596" target="_blank" rel="noopener">BMP files with alpha channel are read with incorrect channel order</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-06-15" data-time="21:09:43" data-timezone="UTC">09:09PM - 15 Jun 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:Bug</span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When a 32-bit ARGB BMP file is loaded using ITK, the colors are all mixed up.

<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
### Description

BMP files with transparency are stored with ARGB channel order. It seems that ITK assumes RGBA order.

### Steps to Reproduce

Load this image using ITK: https://1drv.ms/u/s!Arm_AFxB9yqHxcpbEw34sbS-h1pjkA?e=cf39o8

```python
img = sitk.ReadImage('15-14-49.bmp')
myshow(img)  # incorrect
```

```python
nda = sitk.GetArrayFromImage(img)
img2=sitk.GetImageFromArray(nda[:,:,[1,2,3,0]])
myshow(img2)  # correct
```

![image](https://user-images.githubusercontent.com/307929/122123570-228c3a00-cdfc-11eb-80a6-4e536fb78faa.png)

### Expected behavior

Colors should appear correctly in an application, regardless of what file format is loaded from (png, jpg, bmp, ...)

### Actual behavior

Colors are not correct if BMP format is used (if transparency is stored with the image).

### Reproducibility

100%

### Versions

v5.2.0

### Environment

all (Windows and Linux tested)

### Additional Information

See original user report at https://discourse.slicer.org/t/grey-level-image-looking-blue-or-other-color/18095/3</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
