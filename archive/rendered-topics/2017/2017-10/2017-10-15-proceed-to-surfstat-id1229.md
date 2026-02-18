# Proceed to surfstat

**Topic ID**: 1229
**Date**: 2017-10-15
**URL**: https://discourse.slicer.org/t/proceed-to-surfstat/1229

---

## Post #1 by @iPsych (2017-10-15 11:18 UTC)

<p>Deal all,<br>
I am trying to run more complex statistics using surfstat.<br>
However the result of SPHARM-PDM or SlicerSALT ( *ellalign.meta and *ellalign.coef) seems different from<br>
the structures of data used in existing tutorial.</p>
<p><a href="http://www.stat.wisc.edu/~mchung/research/amygdala/" class="onebox" target="_blank" rel="nofollow noopener">http://www.stat.wisc.edu/~mchung/research/amygdala/</a></p>
<p>Anybody has some experience on modify the data to be used in surfstat?</p>

---

## Post #2 by @styner (2017-10-16 12:57 UTC)

<p>Hi June, Indeed the coefficients themselves are not ready for surfstat, but you can use the vtk files to do the local shape analysis in surfstat. If you look at Moo’s amygdala  page, before running surfstat he calls his tool SPHARMrepresent2, which maps the coefficients to a sampled/triangulated surface/mesh. The vtk files from our tool is such a triangulated mesh that you can use in surfstat. You just need to first convert it into either obj or MGH-Freesurfer format.<br>
Martin</p>

---

## Post #3 by @SHKim (2017-10-16 13:30 UTC)

<p>Hi, June.</p>
<p>If you have vtk surfaces, first of all, you have to convert the surface format from vtk to freesurfer surface format. you can use “mris_convert”. And also, you can check your surfaces have same vertex number (after surface registration) which means all surfaces have correspondence point.</p>

---

## Post #4 by @iPsych (2017-10-16 14:18 UTC)

<p>Thanks, Martin,<br>
I checked SPHARMrepresent2.<br>
However, it requires data format like below.<br>
A=<br>
x: [43x85 double]<br>
y: [43x85 double]<br>
z: [43x85 double]<br>
(SPHARMrepresent2(sphere,A,15,0.01)<img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>
<p>Since vtk data is just x,y,z coordinate, I think more data transfer or additional step is needed.</p>

---

## Post #5 by @iPsych (2017-10-16 14:20 UTC)

<aside class="quote no-group" data-username="SHKim" data-post="3" data-topic="1229">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/59ef9b/48.png" class="avatar"> SHKim:</div>
<blockquote>
<p>mris_convert</p>
</blockquote>
</aside>
<p>Thanks,<br>
Actually I transferred it to MNI obj format.<br>
freesurfer surface is better to process?</p>
<p>You mean using mris_convert,  convert vtk to mgz, right?<br>
Should I use ellaign.vtk or already aligned procalign.vtk?</p>

---

## Post #6 by @styner (2017-10-16 15:31 UTC)

<p>Sorry, that I was not clear. The vtk surfaces created by SALT would be similar to the surfaces created by SPHARMrepresent2. I.e. instead of using SPHARMrepresent2, you would be loading our surfaces.</p>

---

## Post #7 by @styner (2017-10-16 15:33 UTC)

<p>I think obj or freesurfer are equally good. I don’t think mris_convert converts from vtk, but rather only to vtk (I tried it on my local install, which is not the newest, and it did not work).</p>
<p>So, I would use your conversion from vtk to obj and then load those obj files into surfstat. For that purpose use the procalign.vtk surfaces.</p>
<p>Martin</p>

---

## Post #8 by @styner (2017-10-16 15:34 UTC)

<p>Let me know if your vtk to obj tool does not work, as I was told by SunHyung that he has such a tool that we can give to you.<br>
Martin</p>

---

## Post #9 by @iPsych (2017-10-16 16:07 UTC)

<p>Thanks.<br>
I also created python code using VTK, and it successfully converted vtk to obj.</p>
<p>However, I am stucked in below step. Brain, Age, Group is covariate. avsurf is average one.</p>
<p>slm0 = SurfStatLinMod( disp, Brain + Age + Group, avsurf);</p>
<p>When I load the obj transformed from vtk file, it looks like below.<br>
A=SurrfStatReadSurf(‘test.obj’)<br>
A =<br>
tri: [2880x3 int32]<br>
coord: [3x1442 double]</p>
<p>Making average surface from As are possible, but<br>
How should I calculate disp from them?</p>
<p>When I use surfstat, should I ignore ellalign.coef or should I use it in somewhere above?</p>

---

## Post #10 by @SHKim (2017-10-16 17:00 UTC)

<p>Hi, June</p>
<p>I am not sure what you are analyzing for your measurement. What is your dependent variable? “disp” , as you wrote, is a dependent variable that means you obtained any features from surface (e.g. surface area, cortical thickness, and any your interesting value). But the dimension of your disp has to same the number of vertex (e.g. 1442 in your case).<br>
Could you explain the “ellalign.coef”? Is it your interesting dependent variable? If so, is the dimension matching to the number of vertex?</p>

---

## Post #11 by @iPsych (2017-10-16 17:12 UTC)

<p>I am conducting shape analysis using SPHARM-PDM.<br>
disp is just difference from average shape in Moo K.s tutorial. (and same as me).<br>
Since I used different SPHARM method from Moo K., (He used matlab scripts to run SPHARM, and I used SPHARM-PDM made by Beatriz Paniagua.)</p>
<p>ellalign.coef is the result of SPHARM-PDM, and possibly coeffient values from comparision to standard sphere (r=1).</p>

---

## Post #12 by @SHKim (2017-10-16 18:00 UTC)

<p>Hi, June</p>
<p>If I understood correctly, you want to make “disp” from the average surface and each individual surfaces. And then you will put the “disp” as a dependent variable into glm. Did you obtain each surface that is generated by SPHARM-PDM? If so, I thought it is quite simple to get the “disp”. you can calculate the distance between two points ( e.g. between coord from individual and coord from average).</p>

---

## Post #13 by @iPsych (2017-10-16 18:03 UTC)

<p>Yes, that’s correct. I generate all surface by SPHARM-PDM, and use disp as dependent variable into glm.</p>

---

## Post #14 by @iPsych (2017-10-17 05:05 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33c219a7423256f2314948768430709c035bac0b.png" alt="21 PM" data-base62-sha1="7nScWw60rXFlq7Pe5aDADCQqeuv" width="551" height="408"></p>
<p>Thanks Sun Hyung and Martin.<br>
I am almost done.</p>
<p>I think something wrong in the last visualization part, and looking on it.</p>
<p>Bests,<br>
J.</p>

---

## Post #15 by @SHKim (2017-10-17 13:02 UTC)

<p>Hi, June</p>
<p>Great works. But I guess you are missing the surface smoothing. or when you visualized your values, the figure seems to use the vector information.</p>
<p>Sun Hyung</p>

---

## Post #16 by @Tspostma (2018-01-22 15:44 UTC)

<aside class="quote no-group" data-username="iPsych" data-post="14" data-topic="1229">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/i/e19b73/48.png" class="avatar"> iPsych:</div>
<blockquote>
<p>Sun Hyung and Martin</p>
</blockquote>
</aside>
<p>Dear all,</p>
<p>I’m trying to import procalign.vtk files generated by Slicer into Surfstat, but I’m struggling with the conversion from vtk to MNI obj. Is the tool that Martin mentioned earlier still available?</p>

---

## Post #17 by @SHKim (2018-01-22 16:41 UTC)

<p>you can use vtk library or here is simple c++ code: <a href="https://github.com/shykim/SurfaceConvert" rel="nofollow noopener">https://github.com/shykim/SurfaceConvert</a></p>
<p>best,<br>
Sun Hyung</p>

---
