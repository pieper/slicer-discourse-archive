# Problems in use .nrrd format from 3d slicer in python.

**Topic ID**: 9449
**Date**: 2019-12-09
**URL**: https://discourse.slicer.org/t/problems-in-use-nrrd-format-from-3d-slicer-in-python/9449

---

## Post #1 by @11131 (2019-12-09 17:13 UTC)

<p>Hi.<br>
I’m dealing with MR DICOM now.<br>
In order to see the screen like the image of the slice obtained from the 3D Slicer as shown in the below picture(fig1.) in Python, I saved it in .nrrd format through the ‘save’ function in the 3d slicer.</p>
<p>fig1.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b59755414633fc35e99fec24484d45daffb5b7c.png" data-download-href="/uploads/short-url/fjEKG7joT70MnlyFdcdiR5CourW.png?dl=1" title="fig1." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b59755414633fc35e99fec24484d45daffb5b7c_2_308x250.png" alt="fig1." data-base62-sha1="fjEKG7joT70MnlyFdcdiR5CourW" width="308" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b59755414633fc35e99fec24484d45daffb5b7c_2_308x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b59755414633fc35e99fec24484d45daffb5b7c_2_462x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b59755414633fc35e99fec24484d45daffb5b7c_2_616x500.png 2x" data-dominant-color="0C0C0C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig1.</span><span class="informations">622×504 32.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>fig2.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/884885dc7d53836ba661cf3b87d579d2b6b458d1.png" alt="fig2." data-base62-sha1="jrCjz2MNzoLCmzqZO42s073w3Tz" width="301" height="250"></p>
<p>Then I looked at the 0th slice using the python code below and it is different(fig3.) from slice in 3D Slicer.</p>
<pre><code>import nrrd
data,_ = nrrd.read('C:/Users/user/Desktop/slicer/602 3D T1 
TFE AX F GD.nrrd')

plt.subplot(1,1,1)
plt.imshow(data.T[0], cmap="gray")
plt.axis('off')
</code></pre>
<p>fig3.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a462fb1f9b8e3004dc9599288440662268d7ffcd.png" alt="fig3." data-base62-sha1="nsemZB5ytDpEx53LkNFR54pAkEt" width="231" height="231"></p>
<p>The reason I want to get a slice of the 3D Slicer is that I want to get a slightly tilted volume as shown in fig2.<br>
Thank you for your help in this area.</p>

---

## Post #2 by @pieper (2019-12-09 17:41 UTC)

<p>This is normal - Slicer shows patient coordinates and it looks like your images are slightly rotated with respect to patient.</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>
<p>You can change this in slicer with the button labelled 4 in <a href="https://discourse.slicer.org/t/read-prostate-mr-image-failed/3423/2">this image</a>.</p>

---

## Post #3 by @11131 (2019-12-10 05:29 UTC)

<p>Thank you for your reply!</p>
<p>I used the link mentioned in the reply to confirm that the image is changing.</p>
<p>In addition, the link says that the volume is not transformed, but is a plane match orientation of volume axes. Is this possible in Python?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0add2e1e9cbe563fe0ce2a89b507993a6ab75ec.jpeg" data-download-href="/uploads/short-url/tM3Jem1JiagZCWpVq6Xe0T5F0rW.jpeg?dl=1" title="fig4." rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0add2e1e9cbe563fe0ce2a89b507993a6ab75ec_2_509x499.jpeg" alt="fig4." data-base62-sha1="tM3Jem1JiagZCWpVq6Xe0T5F0rW" width="509" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0add2e1e9cbe563fe0ce2a89b507993a6ab75ec_2_509x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0add2e1e9cbe563fe0ce2a89b507993a6ab75ec_2_763x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0add2e1e9cbe563fe0ce2a89b507993a6ab75ec.jpeg 2x" data-dominant-color="5A595A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">fig4.</span><span class="informations">845×829 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code>    for con in contours:
    index = np.array(con['uid'])
    num = int(con['number'])
    
    for c,i in zip(con['contours'],range(len(index))):
        idf = uids.index(index[i])
        origin = slices[idf+1].ImageOrientationPatient
        pos_r = slices[idf+1].ImagePositionPatient[1]
        pos_c = slices[idf+1].ImagePositionPatient[0]
        spacing_r = slices[idf+1].PixelSpacing[1]
        spacing_c = slices[idf+1].PixelSpacing[0]
        nodes = np.array(c).reshape((-1, 3))
        r = (np.inner((nodes[:, 1] - pos_r),origin[0]) + np.inner((nodes[:,1] - pos_r),origin[3])) / spacing_r
        c = (np.inner((nodes[:, 0] - pos_c),origin[1]) + np.inner((nodes[:,0] - pos_c),origin[4])) / spacing_c 
        rr, cc = polygon(r, c)
        label[idf, rr, cc] = num+1
</code></pre>
<p>In fact, using the code(read RT Structure’s Contour) above, I would like to reposition the misplaced contour of the structure as shown in the photo.</p>
<p>In my opinion, if I replace the tilted image before transforming it in the slicer, the contour and image will match.</p>
<p>Thank you for answering the previous question, and I would be grateful if you could give me a hint once more.</p>

---

## Post #4 by @pieper (2019-12-10 14:09 UTC)

<p>Hi Sangkyun <a class="mention" href="/u/11131">@11131</a> -</p>
<p>I’ll admit I don’t really understand the question fully, but I can say that if you are working with RT struct datasets I suggest using the SlicerRT extension for 3D Slicer.  This will handle the coordinate systems between contours and reference images according to the standard.  You should also be able to convert and resample the underlying data using python.  Hope that helps!</p>
<p>-Steve</p>

---

## Post #5 by @11131 (2019-12-11 13:12 UTC)

<p>What I want is to know what kind of processing in python to see images like fig1. And fig2.</p>

---
