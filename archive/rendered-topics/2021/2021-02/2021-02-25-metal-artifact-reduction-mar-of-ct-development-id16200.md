---
topic_id: 16200
title: "Metal Artifact Reduction Mar Of Ct Development"
date: 2021-02-25
url: https://discourse.slicer.org/t/16200
---

# Metal artifact reduction (MAR) of CT development

**Topic ID**: 16200
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/metal-artifact-reduction-mar-of-ct-development/16200

---

## Post #1 by @full_stack_master (2021-02-25 03:46 UTC)

<p>I want to get the function of MAR<br>
I have developed the MAR function in my end but it takes much time (30 mins)<br>
I have used the 400 DICOM files for testing<br>
I want to reduce running time from 30mins to 1 min<br>
this is the code for 1 dicom file<br>
it takes 25s to complete 1 file</p>
<pre><code class="lang-python">def calc_mar1(self, shapes, image1):
    image = apply_voi_lut(image1, self.ds)
    tmp_image = image
    m = max(abs(np.min(image)),np.max(image))
    image = image + m
    omax = np.max(image)
    image = image / omax
    theta = np.linspace(0., 180., shapes[0], endpoint=False)
    sinogram = skimage.transform.radon(image, theta=theta, circle=True)
    if self.marthreshold &gt; 0 :
      eff = self.marthreshold
    else:
      eff = 0.65
    th = 190 * eff
    sinogram[sinogram &gt; th] =  th
    reconstruction_fbp = skimage.transform.iradon(sinogram, theta=theta, circle=True)
    tmp_image[tmp_image &lt; tmp_image * 0.995 ] = 0
    scaled_img = self.ds.WindowWidth * reconstruction_fbp - self.ds.WindowCenter 
    scaled_img = scaled_img + (tmp_image / (np.max(tmp_image))) * self.ds.WindowWidth
    self.tmpArray1.append(scaled_img)
</code></pre>

---

## Post #2 by @full_stack_master (2021-02-25 04:12 UTC)

<p>I have the code for MAR using DICOM files<br>
But it takes much time (25s for 1 file , 30 mins for 400 files)<br>
So I want you to reduce running time from 30mins to 1 min</p>
<pre><code class="lang-python">def calc_mar1(self, shapes, image1):

   image = apply_voi_lut(image1, self.ds)
   print(image)
   tmp_image = image
   m = max(abs(np.min(image)),np.max(image))
   image = image + m
   omax = np.max(image)
   image = image / omax
   theta = np.linspace(0., 180., shapes[0], endpoint=False)
   sinogram = skimage.transform.radon(image, theta=theta, circle=True)
   # print("Sinogram:===&gt;")
   # print(np.max(sinogram))
   if self.marthreshold &gt; 0 :
     eff = self.marthreshold
   else:
     eff = 0.65
   th = 190 * eff
   sinogram[sinogram &gt; th] =  th
   reconstruction_fbp = skimage.transform.iradon(sinogram, theta=theta, circle=True)
   # delta = np.pi / shapes[0]
   # reconstruction_fbp = RLIRadonTransform(shapes[0], shapes[0] + 1, sinogram, delta)
   tmp_image[tmp_image &lt; tmp_image * 0.995 ] = 0
   # print(window_width)
   scaled_img = self.ds.WindowWidth * reconstruction_fbp - self.ds.WindowCenter 
   print("tmp_image")
   print(np.max(tmp_image))
   print(np.max(scaled_img))
   scaled_img = scaled_img + (tmp_image / (np.max(tmp_image))) * self.ds.WindowWidth
   self.tmpArray1.append(scaled_img) 
   # print(self.tmpArray[index1])
   return
</code></pre>

---

## Post #3 by @full_stack_master (2021-02-25 04:14 UTC)

<pre><code class="lang-python">def calc_mar1(self, shapes, image1):

    image = apply_voi_lut(image1, self.ds)
    print(image)
    tmp_image = image
    m = max(abs(np.min(image)),np.max(image))
    image = image + m
    omax = np.max(image)
    image = image / omax
    theta = np.linspace(0., 180., shapes[0], endpoint=False)
    sinogram = skimage.transform.radon(image, theta=theta, circle=True)
    # print("Sinogram:===&gt;")
    # print(np.max(sinogram))
    if self.marthreshold &gt; 0 :
      eff = self.marthreshold
    else:
      eff = 0.65
    th = 190 * eff
    sinogram[sinogram &gt; th] =  th
    reconstruction_fbp = skimage.transform.iradon(sinogram, theta=theta, circle=True)
    # delta = np.pi / shapes[0]
    # reconstruction_fbp = RLIRadonTransform(shapes[0], shapes[0] + 1, sinogram, delta)
    tmp_image[tmp_image &lt; tmp_image * 0.995 ] = 0
    # print(window_width)
    scaled_img = self.ds.WindowWidth * reconstruction_fbp - self.ds.WindowCenter 
    print("tmp_image")
    print(np.max(tmp_image))
    print(np.max(scaled_img))
    scaled_img = scaled_img + (tmp_image / (np.max(tmp_image))) * self.ds.WindowWidth
    self.tmpArray1.append(scaled_img) 
    # print(self.tmpArray[index1])
    return
</code></pre>

---

## Post #4 by @lassoan (2021-02-25 06:11 UTC)

<p>Probably it would be hard to improve the performance of radon/iradon CPU implementation in scikit-image. I would suggest to try a GPU implementation, such as <a href="http://christian.mendl.net/software/radon_gpu_manuscript.pdf">this one</a> (it seems that they provide source code, but I did not check what they provide exactly).</p>

---

## Post #5 by @full_stack_master (2021-02-25 07:34 UTC)

<p>thanks for your great efforts<br>
I am sorry but how can we get the solution for MAR in 3d slicer?<br>
I can not see anything for this function now</p>

---

## Post #6 by @lassoan (2021-02-25 13:18 UTC)

<p>You can run the code snippets above in Slicer’s Python console or you can put them in a Python scripted module.</p>
<p>If you want a GPU-accelerated radon transform then check if you can find such a Python package. If there isn’t any then you can use any C++ implementations of the radon transform that you find, by building Slicer and a C++ loadable module.</p>

---
