---
topic_id: 1513
title: "Building The Ijk To Ras Transform From A Nrrd File"
date: 2017-11-23
url: https://discourse.slicer.org/t/1513
---

# Building the ijk to RAS transform from a nrrd file

**Topic ID**: 1513
**Date**: 2017-11-23
**URL**: https://discourse.slicer.org/t/building-the-ijk-to-ras-transform-from-a-nrrd-file/1513

---

## Post #1 by @dcantor (2017-11-23 23:58 UTC)

<p>Hi Slicers,</p>
<p>I am working on a project with Slicer generated nrrd files and after looking at the nrrd header I notice there is no info about the ijk to RAS matrix yet when I load that nrrd file into Slicer I obtain the matrix. So I think I figured out how to build it in code and I am looking for validation from someone who is more experienced than me. This is what I am doing:</p>
<ol>
<li>
<p>I read the nrrd header and obtain the <em>space direction</em> vectors (say <strong>a</strong>,<strong>b</strong>,<strong>c</strong>)</p>
</li>
<li>
<p>I build a 3x3 matrix (A) where the columns correspond to <strong>a</strong>, <strong>b</strong>, and <strong>c</strong>.</p>
</li>
<li>
<p>Given the <strong>t</strong> translation column vector (as defined in the nrrd <em>space origin</em> header), I can obtain world coordinates <strong>x</strong> for the index column vector <strong>v</strong> by:</p>
</li>
</ol>
<blockquote>
<p>x  = A*v + t</p>
</blockquote>
<ol start="4">
<li>since my nrrd volume appears to be in LPS frame (as per the <em>space</em> header), I have to multiply <strong>x</strong> by the LPS to RAS transform.</li>
</ol>
<p>Say that’s T =   [-1 0 0; 0  -1 0; 0 0 1], so:</p>
<blockquote>
<p>x_ras = T * x</p>
</blockquote>
<p>Is this correct?</p>
<p>Now, the IJK to RAS direction matrix reported in Slicer (Volumes module) seems to be:</p>
<blockquote>
<p>T*A</p>
</blockquote>
<p>is this correct?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2017-11-24 01:05 UTC)

<p>Almost correct. IJKToRAS is a homogeneous transformation matrix, which contains axis directions in the top-left 3x3 sub-matrix, origin in the first 3 values of 4th column, and [0,0,0,1] in the 4th row (so you don’t “add” the translation component but concatenate). In Matlab syntax:</p>
<pre><code>ijk_to_lps = [[space_directions, space_origin]; [0 0 0 1]]
lps_to_ras = diag([-1 -1 1 1])
ijk_to_ras = lps_to_ras * ijk_to_lps</code></pre>

---

## Post #3 by @dcantor (2017-11-24 03:40 UTC)

<p>Ok, the confusion was because in the volumes module the matrix appears as a 3x3 matrix. But it doesn’t matter, anyways the 4x4 form is equivalent as you show since you are operating in homogeneous coordinates.<br>
Thank you Andras.</p>

---

## Post #4 by @Optics_Bioeng (2023-06-25 06:04 UTC)

<p>Hello Slicers</p>
<p>OS: Windows11<br>
Slicer5.2.2</p>
<p>I’m beginner of 3DSlicer. I am working on a project with Slicer generated nrrd files too. This is what I want to do:</p>
<p>Step1. Forearm segmentation in Slicer and output as nrrd data.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f04c2e26e7f848f5f846e07c15d3e838889f7aa.jpeg" data-download-href="/uploads/short-url/8ZuhsuPV0O3KNXZYZ0nIabbKpRg.jpeg?dl=1" title="スクリーンショット 2023-06-25 143847" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f04c2e26e7f848f5f846e07c15d3e838889f7aa_2_658x500.jpeg" alt="スクリーンショット 2023-06-25 143847" data-base62-sha1="8ZuhsuPV0O3KNXZYZ0nIabbKpRg" width="658" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f04c2e26e7f848f5f846e07c15d3e838889f7aa_2_658x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3f04c2e26e7f848f5f846e07c15d3e838889f7aa_2_987x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f04c2e26e7f848f5f846e07c15d3e838889f7aa.jpeg 2x" data-dominant-color="3A3B43"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2023-06-25 143847</span><span class="informations">1207×917 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Step2. Calculate the centre of gravity for a particular slice using python and obtain its coordinate ijk</p>
<pre><code class="lang-python">import nrrd
tensor, header = nrrd.read("C:\\Users.....\\Segmentation.seg.nrrd", index_order ='C')
import cv2
def calc_center_gravity(tensor, gk):
    gravity = []
    img = tensor[gk]
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        M = cv2.moments(cnt)
        if M["m00"] == 0:
            continue
        gx = int(M["m10"] / M["m00"])
        gy = int(M["m01"] / M["m00"])
        plt.plot(gi, gj, marker='.')
        gravity.append((gi, gj, gk))
    plt.imshow(img, cmap="gray")
    plt.title(f"centre of gravity index\n (i, j, k)=({gi}, {gj}, {gk})")
    plt.show()
    return gravity
gravity = calc_center_gravity(tensor, 24)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/041b24419e1324ce74e7f121c807900df8aa52f2.png" alt="スクリーンショット 2023-06-25 145035" data-base62-sha1="Ak3KKf92BXSSjlfyEJYnFkmqqe" width="333" height="449"></p>
<pre><code class="lang-python">space_directions = header["space directions"]
space_origin = header["space origin"]
ijk2lps = np.vstack([np.hstack([space_directions, space_origin.reshape(-1, 1)]), np.array([0, 0, 0, 1])])
lps2ras = np.diag([-1, -1, 1, 1])
ijk2ras = np.dot(lps2ras, ijk2lps)
​
gravity_ijk = np.append(np.array(gravity[0]), 1).reshape(-1, 1)
gravity_ras = np.dot(ijk2ras, gravity_ijk)
gravity_ras
</code></pre>
<p>Step3. transform the acquired coordinate ijk to ras and markup it again in Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e16a2332c24267bca969603c0484aeb8a80f1284.jpeg" data-download-href="/uploads/short-url/wa6Pq8Robak7NBCsW8loTJLsOzi.jpeg?dl=1" title="スクリーンショット 2023-06-25 145822" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e16a2332c24267bca969603c0484aeb8a80f1284_2_652x500.jpeg" alt="スクリーンショット 2023-06-25 145822" data-base62-sha1="wa6Pq8Robak7NBCsW8loTJLsOzi" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e16a2332c24267bca969603c0484aeb8a80f1284_2_652x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e16a2332c24267bca969603c0484aeb8a80f1284_2_978x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e16a2332c24267bca969603c0484aeb8a80f1284.jpeg 2x" data-dominant-color="393B42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2023-06-25 145822</span><span class="informations">1197×917 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Problem<br>
Cannot convert nrrd centre-of-gravity coordinates ijk to slicer coordinates ras between step2 and 3<br>
Could you tell me what is wrong? Thank you!</p>

---

## Post #5 by @pieper (2023-06-25 18:07 UTC)

<p>You should be able to work from this example:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-centroid-of-a-segment-in-world-ras-coordinates" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---

## Post #6 by @Optics_Bioeng (2023-06-27 07:17 UTC)

<p>Thank you. I will have a try.</p>

---
