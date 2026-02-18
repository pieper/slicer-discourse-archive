# Is there a better solution for head registration?

**Topic ID**: 25356
**Date**: 2022-09-20
**URL**: https://discourse.slicer.org/t/is-there-a-better-solution-for-head-registration/25356

---

## Post #1 by @jay1987 (2022-09-20 12:09 UTC)

<p>we now have different registration solutions for head registration,like elastix,ants,brainsfit<br>
we now have different serials for registration,like T1,T2,Flair,PCA,CT<br>
if we choose T1 as fixed volume , Other serials as moved volume,what’s the better solution to make the better registration effect?</p>

---

## Post #2 by @pieper (2022-09-20 12:53 UTC)

<p>It sounds like you have a good solution.  Can you list any problems you have with the current approach?</p>

---

## Post #3 by @jay1987 (2022-09-20 13:02 UTC)

<p>i don’t have any good solution pieper,i’m just confusing<br>
i have some serials to registe,like T1,T2,CT,Flair<br>
I found some commercial software like brainlab don’t have registration options like [use rigid],[use affine] etc. so i wonder how to do in slicer can Implement this function</p>

---

## Post #4 by @ebrahim (2022-09-20 14:16 UTC)

<p>Check out the SlicerANTs extension; it offers options like rigid, rigid+scaling, and deformable registration via SyN</p>

---

## Post #5 by @jay1987 (2022-09-21 01:20 UTC)

<p>yes,Ants is a awesome extension,as well as elastix,brainsfit.<br>
in the hospital enviroment, many doctor in the small or middle hospital don’t known the different between rigid and affine ,so some commercial software only provide one registation button without options<br>
i want to Implement the button in slicer,and now have two directions<br>
1.find a way to give a score to  the result of registration ,run several registration,choose the biggest score<br>
2.find better parameters from modal A to modal B (like T1 to CT),and record the parameters in the database,when encounter the modal pairs latter,choose the parameters from database<br>
both directions have many problems to solve.is there a better solution to do this?</p>

---

## Post #6 by @ebrahim (2022-09-21 01:31 UTC)

<p>Here are my thoughts… but you are have thought about this more than me so don’t take me too seriously:</p>
<p>(1) will potentially take a long time, making registration take several times longer than any single processing. If that’s not a problem for your application, then maybe (1) sounds good. You could use normalized cross correlation for the score, for example. But taking so long to register is not good for an end user sort of thing.</p>
<p>(2) sounds interesting but I would start by experimenting with different modalities first. Maybe you can discover what approach is best for each pair of modalities, and then hard-code the choice of registration algorithm for each pair. If while doing this you feel that the process of discovery can be automated, then automate it once for yourself and hard-code the choice into your module. Having a system “learn” the best parameters while it is being used in a  hospital environment sounds to me like it introduces too many unnecessary failure points as well as makes it a less consistent and more difficult to understand system.</p>

---

## Post #7 by @jay1987 (2022-09-21 01:39 UTC)

<p>thanks erahim,thank you for you reply.<br>
Your ideas are important to me , I will seriously think about them.<br>
you have mentioned [normalized cross correlation] above, is there a vtk filter or extensions to do this algorithm in Slicer?</p>

---

## Post #8 by @ebrahim (2022-09-21 02:13 UTC)

<p>Maybe someone else can comment if there is a vtk filter, I don’t know</p>
<p>But it’s pretty quick to implement in python using numpy for example:</p>
<pre><code class="lang-python">import numpy as np

# create some random 3D image arrays with a bit of correlation to them
im1 = np.random.randn(50,50,50)
im2 = im1+np.random.randn(50,50,50)

# compute their NCC
mu1 = im1.mean() # means
mu2 = im2.mean()
alpha1 = (im1**2).mean() # second moments
alpha2 = (im2**2).mean()
alpha12 = (im1*im2).mean() # cross term
numerator = alpha12 - mu1*mu2
denominator = np.sqrt((alpha1 - mu1**2) * (alpha2-mu2**2))
ncc = numerator / denominator # be careful of division by zero!
print(ncc)
</code></pre>

---

## Post #9 by @jay1987 (2022-09-21 02:16 UTC)

<p>thanks,you help me a lot.<br>
your code is awesome.</p>

---

## Post #10 by @jay1987 (2022-10-08 09:29 UTC)

<p>dear ebrahim:<br>
i have integraged your code into the slicer enviroment , and find a problem . the value [denominator] is NAN,the value in [np.sqrt] is negative,should i force the result to positive?<br>
the code i have written pasted below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bedda78306c1a9264a527a509ad793f9e995f16.png" data-download-href="/uploads/short-url/foMGEfn2ADxdrgtiIPhZvVMhSUm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6bedda78306c1a9264a527a509ad793f9e995f16.png" alt="image" data-base62-sha1="foMGEfn2ADxdrgtiIPhZvVMhSUm" width="461" height="500" data-dominant-color="262725"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">709×768 38 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @ebrahim (2022-10-08 23:32 UTC)

<p>Hmm it should not be possible for the thing under the square root to be negative. This is because both <code>alpha1-mu1**2</code> and <code>alpha2-mu2**2</code> are necessarily nonnegative:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/ccc43183119df9d5920a460abb259d135fc951af.png" alt="image" data-base62-sha1="tdrKhboOEcY9Sf8Dsxecn7wSHIH" width="267" height="204"></p>
<p>Here for example <code>x_1, ..., x_N</code> stand for the image pixel/voxel values of <code>im1</code> and the greek letters <code>mu</code> and <code>alpha</code> are standing in for <code>mu1</code> and <code>alpha1</code>. As long as all image values are real (i.e. have no imaginary component) it should not be possible to get something negative.</p>
<p>The denominator contains the variances in the image values, so it can be zero (when an image is all one value, constant over space). Then you’d get a division by zero, but maybe there’s some floating point error that pushes it to the negative sometimes? If that is what’s happening then you can add a little smoothing factor to the denominator. It takes you a slightly away from true ncc but makes your calculation robust to images with vary small variance. So instead of <code>ncc=numerator / denominator</code> you can try <code>ncc = numerator / (denominator + 0.001)</code> or something like that.</p>
<p>Please verify first that when you get <code>denominator&lt;0</code> it’s a <strong>very</strong> small negative number. If it’s not small then something is wrong and please let me know! I use this NCC calculation for a few things and would like to fix it if something is wrong. Thanks!</p>

---

## Post #12 by @jay1987 (2022-10-09 01:41 UTC)

<p>thank you so much for reply.<br>
i paste the result i caculate from the code above<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9b496ab7bb795a4a30184401db3b10884744d00.png" alt="image" data-base62-sha1="zCZNyDOZZZzVxZNK9CYEqZ9NljG" width="372" height="137"></p>
<p>the value [alpha2-mu2**2] is negative</p>

---

## Post #13 by @ebrahim (2022-10-09 02:10 UTC)

<p>Hmm this is puzzling</p>
<p>It should not be possible that <code>(im2**2).mean()</code> is <code>545</code> while <code>im2.mean()</code> is 40.</p>
<p>The math above shows that <code>alpha2-mu2**2</code> equals <code>((im2-im2.mean())**2).mean()</code> and hence should not be negative.</p>
<p>Can you inspect <code>((im2-im2.mean())**2).mean()</code> and <code>((im2-mu2)**2).mean()</code> and <code>alpha2-mu2**2</code> … these should all be the same number.</p>
<p>Can you print out the image shapes; maybe there is some broadcasting that we are missing.</p>

---

## Post #14 by @jay1987 (2022-10-09 02:12 UTC)

<p>of course , i paste the result below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2995117eb994c4602eec8e4582ff8c1ea1bfb6a.png" alt="image" data-base62-sha1="rLv6KK9U7w9mJQvFvrFR1R0KzKa" width="423" height="184"></p>

---

## Post #15 by @ebrahim (2022-10-09 03:28 UTC)

<p>and the image shapes?<code>im1.shape</code>, <code>im2.shape</code></p>
<p>it’s so strange that<br>
<code>((im2-im2.mean())**2).mean()</code><br>
is coming out different from<br>
<code>(im2**2).mean() - im2.mean()**2</code></p>

---

## Post #16 by @jay1987 (2022-10-09 03:32 UTC)

<p>yes,it’s different.the shape information i pasted below<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea205eec5129b5f87e520c7aeaa3a96563e67bcd.png" alt="image" data-base62-sha1="xpb55WcChfRMmNxQqmc4qzIjYvj" width="411" height="211"></p>

---

## Post #17 by @ebrahim (2022-10-09 03:46 UTC)

<p>When I try on a random array it does work out:</p>
<pre><code class="lang-python">import numpy as np
im2 = np.random.rand(208,256,240)

# these two come out the same modulo float arithmetic errors
print(((im2-im2.mean())**2).mean())
print((im2**2).mean() - im2.mean()**2)
</code></pre>
<p>Maybe there is a problem in your definition of <code>alpha2</code>? Can you try printing those two quantities exactly?</p>
<pre><code class="lang-python">print(((im2-im2.mean())**2).mean())
print((im2**2).mean() - im2.mean()**2)
</code></pre>
<p>if they are different then there’s something we are fundamentally missing about how the arrays being handled. if they are the same then your definition of <code>alpha2</code> or <code>mu2</code> was messed up</p>

---

## Post #18 by @jay1987 (2022-10-09 03:50 UTC)

<aside class="quote no-group" data-username="ebrahim" data-post="17" data-topic="25356">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<pre><code class="lang-auto">print(((im2-im2.mean())**2).mean())
print((im2**2).mean() - im2.mean()**2)
</code></pre>
</blockquote>
</aside>
<p>the result is different<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eacaca64162d7f720a5b2d459e88fe123d3d0085.png" alt="image" data-base62-sha1="xv4cHI6Jxdut0JoPQgdGwAjF605" width="422" height="243"></p>

---

## Post #19 by @ebrahim (2022-10-09 03:58 UTC)

<p>but with a random array like I showed in the code snippet above, those two numbers come out the same for you?</p>
<p>how about <code>im1</code>? are those numbers the same for you when you try with <code>im1</code>?</p>

---

## Post #20 by @jay1987 (2022-10-09 05:09 UTC)

<p>the result is different for m1,too<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d318bf3e45acd19258c67b8f395901920fe8ebb8.png" alt="image" data-base62-sha1="u7rLwF9VoUe98g8CPajmgEe1NBC" width="439" height="277"></p>

---

## Post #21 by @ebrahim (2022-10-09 05:47 UTC)

<p>What about the random array code snippet:</p>
<pre><code class="lang-python">import numpy as np
im2 = np.random.rand(208,256,240)
print(((im2-im2.mean())**2).mean())
print((im2**2).mean() - im2.mean()**2)
</code></pre>
<p>Do the two <code>print</code>s give almost the same value for you?</p>

---

## Post #22 by @jay1987 (2022-10-09 05:51 UTC)

<p>yes,i use random code , it’s the same<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/905e8b8cae625e834a58473ce5d0d5f6b1181aa6.png" alt="image" data-base62-sha1="kB9jHjBEPnaJMX6D29Vkd4oXgFg" width="446" height="31"></p>

---

## Post #23 by @ebrahim (2022-10-09 05:57 UTC)

<p>then I am super confused why it’s not working for these specific images… what it is about them that makes this fail?</p>
<p>I would be happy to look if you want to share the images. sharing <code>im1</code> would be sufficient</p>
<p>otherwise I would suggest doing some debugging because <code>((im2-im2.mean())**2).mean()</code> and <code>(im2**2).mean() - im2.mean()**2</code> should be almost equal for any real valued arrays, and please let me know if you discover the issue</p>

---

## Post #24 by @jay1987 (2022-10-09 06:21 UTC)

<p>okay,i will save the two images into  SlicerScarlarVolumeNode .mrb format<br>
here is the dropbox link</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.dropbox.com/s/gkfi9e3jnnq79ia/379.mrb?dl=0">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/metaserver/static/images/favicon-vfl8lUR9B.ico" class="site-icon" width="32" height="32">

      <a href="https://www.dropbox.com/s/gkfi9e3jnnq79ia/379.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">Dropbox</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/metaserver/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/gkfi9e3jnnq79ia/379.mrb?dl=0" target="_blank" rel="noopener nofollow ugc">379.mrb</a></h3>

  <p>Shared with Dropbox</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #25 by @ebrahim (2022-10-09 16:40 UTC)

<p>Thank you for sharing<br>
It was an integer overflow <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=12" title=":laughing:" class="emoji" alt=":laughing:" loading="lazy" width="20" height="20"></p>
<p>Your arrays have a dtype of 16 bit ints.</p>
<p>if you up to 32-bit then those numbers come out the same and you should no longer have a negative under the square root:</p>
<pre><code class="lang-python">im1 = im1.astype(np.int32)
im2 = im2.astype(np.int32)
</code></pre>

---

## Post #26 by @jay1987 (2022-10-10 01:36 UTC)

<p>thank you very much!<br>
it indeed is the problem of integer overflow.<br>
it’s now work!!</p>

---

## Post #27 by @jay1987 (2022-10-10 02:03 UTC)

<p>i paste my code in slicer here , i found the result of ncc related to the value of [default_sample_value],the [default_sample_value] is the blank area of moved image voxel value,do you have any suggestion on how to set the [default_sample_value] value?<br>
for example:<br>
for T1 as fixed image,CT as moved image ,the  [default_sample_value] set to -1000 can represent the register result quanlity<br>
but T1 as fixed image,Flair as moved image,the  [default_sample_value] set to -1000 can not represent the register result quanlity,set to 0 is better.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8b6821eb87bf5a57831b656b3d60804ab9e0ad9.png" data-download-href="/uploads/short-url/uV89EUZ38MBHNsTNuAjQCRmmZOV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8b6821eb87bf5a57831b656b3d60804ab9e0ad9.png" alt="image" data-base62-sha1="uV89EUZ38MBHNsTNuAjQCRmmZOV" width="413" height="500" data-dominant-color="282B29"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">540×653 28.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #28 by @ebrahim (2022-10-10 02:14 UTC)

<p>The default pixel value should be set based on what you want in the end, and what makes sense for the modality. Whatever value shows up in the "background’ of your image would make sense. For CT -1000 perhaps makes sense because the Hounsfield scale is designed so that air has value -1000. For any other modalities you can look at a sample image and check what is the voxel value in the background region.</p>
<p>I think the effect on NCC of your choice of default pixel value is not directly relevant to registration quality.  In fact, if you can do it then I think it’s best to compute NCC only in the intersection of the two image domains, where no value was sampled from outside the boundary of the moving image and the default pixel value is never used. I would say it’s good enough to just choose a default pixel value that makes sense for the modality, not one that maximizes NCC.</p>

---

## Post #29 by @jay1987 (2022-10-10 02:18 UTC)

<p>thank you , i understand your suggestion , i will try to compute NCC only in the intersection of the two image domains</p>

---
