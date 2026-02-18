# Trouble loading sample data in SlicerAutoscoperM

**Topic ID**: 41003
**Date**: 2025-01-09
**URL**: https://discourse.slicer.org/t/trouble-loading-sample-data-in-slicerautoscoperm/41003

---

## Post #1 by @Lauren_Welte (2025-01-09 00:38 UTC)

<p>We have downloaded 3D Slicer 5.6.2 and are using SlicerAutoscoperM version 52a6b2d (2024-12-18).</p>
<p>We have downloaded the sample data (wrist, knee and ankle).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/942c56771ea0e9ae0d93d72f27ecf9d65d49a787.png" data-download-href="/uploads/short-url/l8NEQxki7tLYFR3w8urVRa9gkQf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/942c56771ea0e9ae0d93d72f27ecf9d65d49a787_2_690x387.png" alt="image" data-base62-sha1="l8NEQxki7tLYFR3w8urVRa9gkQf" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/942c56771ea0e9ae0d93d72f27ecf9d65d49a787_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/942c56771ea0e9ae0d93d72f27ecf9d65d49a787_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/942c56771ea0e9ae0d93d72f27ecf9d65d49a787_2_1380x774.png 2x" data-dominant-color="99969B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1919×1079 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We then launch Autoscoper (Autoscoper opens), then we click “Load Wrist Data” and we get the following errors:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bb411b9fb4d01066d2c21b057163e9e07dde02b.png" data-download-href="/uploads/short-url/3X4GFK04sTVYIJ5Mf0wlGDyiI3h.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bb411b9fb4d01066d2c21b057163e9e07dde02b_2_690x370.png" alt="image" data-base62-sha1="3X4GFK04sTVYIJ5Mf0wlGDyiI3h" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bb411b9fb4d01066d2c21b057163e9e07dde02b_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bb411b9fb4d01066d2c21b057163e9e07dde02b_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1bb411b9fb4d01066d2c21b057163e9e07dde02b_2_1380x740.png 2x" data-dominant-color="F6F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×1030 84.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>We are running a Microsoft Windows 11 Education.<br>
The computer has :<br>
GPU processor:		NVIDIA RTX 2000 Ada Generation<br>
Driver version:		556.12</p>
<p>Let me know if we can provide any more details.</p>

---

## Post #2 by @Amy_Morton (2025-01-09 02:26 UTC)

<p>Thanks Lauren, (welcome to the discourse)</p>
<ol>
<li>In the extension index, under SlicerAutoscoperM what version do you see? ex:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf40700b57f0adadfbcd57e28320d7eba3e0f861.png" data-download-href="/uploads/short-url/tzqTosJtseHu30yubuGyJelYf4Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf40700b57f0adadfbcd57e28320d7eba3e0f861_2_690x240.png" alt="image" data-base62-sha1="tzqTosJtseHu30yubuGyJelYf4Z" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf40700b57f0adadfbcd57e28320d7eba3e0f861_2_690x240.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf40700b57f0adadfbcd57e28320d7eba3e0f861_2_1035x360.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cf40700b57f0adadfbcd57e28320d7eba3e0f861_2_1380x480.png 2x" data-dominant-color="524A4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×668 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>2.Try ‘Check for updates’ in the index and restart if any are available</p>
<ol start="4">
<li>
<p>You have a good chunk of errors/warnings in your python console- did you observe a successful PyAutoscoper install? (it won’t output every time- but it should if you install and update to the extension)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/859873afd06445ee577078732a6e573c882afefa.png" data-download-href="/uploads/short-url/j3Q84J8fdCunXoMvaoAw09pZo4q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859873afd06445ee577078732a6e573c882afefa_2_690x437.png" alt="image" data-base62-sha1="j3Q84J8fdCunXoMvaoAw09pZo4q" width="690" height="437" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859873afd06445ee577078732a6e573c882afefa_2_690x437.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859873afd06445ee577078732a6e573c882afefa_2_1035x655.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/859873afd06445ee577078732a6e573c882afefa_2_1380x874.png 2x" data-dominant-color="3E3B3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1454×922 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>If none of the above is relevant… can you launch Autoscoper in OpenCL  and successfully load sample data?</p>
</li>
</ol>

---

## Post #3 by @Lauren_Welte (2025-01-15 00:27 UTC)

<p>[1/2 as I am limited to 3 media items]<br>
This is the version we were using previously:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/187bb142747a30eebeb2125d409011fff34008d1.png" alt="image (1)" data-base62-sha1="3uAt58EUb9xgr1B8K96Cq2Xw8YV" width="690" height="63" data-dominant-color="DADAF3"></p>
<p>Then, I checked for updates, installed them, and restarted Slicer. This is the version we have now:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/3804d16bc23967b0ac9726280f0fb00b6a6c6d14.png" alt="image (2)" data-base62-sha1="7Zz3Mn2Co6o3rZW9SNZvLLKx9fm" width="690" height="72" data-dominant-color="DBDBF3"></p>
<p>This is Slicer opened fresh with AutoscoperM selected. (no errors in the console)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6b41250eb3ada6daf1e7c77977a9f97fb9c091d.png" data-download-href="/uploads/short-url/q4gHt9tibDWbnlanji1sxoYUAGx.png?dl=1" title="image (3)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6b41250eb3ada6daf1e7c77977a9f97fb9c091d_2_690x359.png" alt="image (3)" data-base62-sha1="q4gHt9tibDWbnlanji1sxoYUAGx" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6b41250eb3ada6daf1e7c77977a9f97fb9c091d_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6b41250eb3ada6daf1e7c77977a9f97fb9c091d_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b6b41250eb3ada6daf1e7c77977a9f97fb9c091d_2_1380x718.png 2x" data-dominant-color="B0AFB2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (3)</span><span class="informations">1919×1000 55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Lauren_Welte (2025-01-15 00:27 UTC)

<p>[2/2]</p>
<p>This is what the console looks like when we open AutoscoperM.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54b46f3be30fe262e0a67bf00ebbd6168f96bada.png" data-download-href="/uploads/short-url/c5kGzy2gFU8a5A2ZJ4J6vYyYTXQ.png?dl=1" title="image (4)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b46f3be30fe262e0a67bf00ebbd6168f96bada_2_690x369.png" alt="image (4)" data-base62-sha1="c5kGzy2gFU8a5A2ZJ4J6vYyYTXQ" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b46f3be30fe262e0a67bf00ebbd6168f96bada_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b46f3be30fe262e0a67bf00ebbd6168f96bada_2_1035x553.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54b46f3be30fe262e0a67bf00ebbd6168f96bada_2_1380x738.png 2x" data-dominant-color="DBDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (4)</span><span class="informations">1918×1028 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I click “Load Wrist Data” and I get this in the console, and Autoscoper closes.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d305ee7ccd62b61c2bdbd671d33c975b3df15ae.png" data-download-href="/uploads/short-url/mqyAZyJbehHzPXJQZBnHWas3D2K.png?dl=1" title="image (5)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d305ee7ccd62b61c2bdbd671d33c975b3df15ae.png" alt="image (5)" data-base62-sha1="mqyAZyJbehHzPXJQZBnHWas3D2K" width="690" height="170" data-dominant-color="FEF6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (5)</span><span class="informations">1918×473 27.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried with Open CL and the same thing happens.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c050e5954725765d3a9d45165d7eceeb0df9b8b4.png" data-download-href="/uploads/short-url/rriZGy7C2xhV8JodpSRnt5te9Fy.png?dl=1" title="image (6)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c050e5954725765d3a9d45165d7eceeb0df9b8b4_2_690x358.png" alt="image (6)" data-base62-sha1="rriZGy7C2xhV8JodpSRnt5te9Fy" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c050e5954725765d3a9d45165d7eceeb0df9b8b4_2_690x358.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c050e5954725765d3a9d45165d7eceeb0df9b8b4_2_1035x537.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c050e5954725765d3a9d45165d7eceeb0df9b8b4_2_1380x716.png 2x" data-dominant-color="C6C0C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (6)</span><span class="informations">1919×997 84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What do you think?</p>

---

## Post #5 by @Amy_Morton (2025-01-15 13:56 UTC)

<ol>
<li>Let’s confirm the cfg location downloaded locally:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef917376ba3f73c7213b2bfc819011dd36d3186a.png" data-download-href="/uploads/short-url/ybjK3rPRYlPjyUOTFMlrPs6hTZM.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef917376ba3f73c7213b2bfc819011dd36d3186a_2_690x200.png" alt="image" data-base62-sha1="ybjK3rPRYlPjyUOTFMlrPs6hTZM" width="690" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef917376ba3f73c7213b2bfc819011dd36d3186a_2_690x200.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef917376ba3f73c7213b2bfc819011dd36d3186a_2_1035x300.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef917376ba3f73c7213b2bfc819011dd36d3186a_2_1380x400.png 2x" data-dominant-color="FBF1ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1639×477 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> ( I doubt there is an issue, but just to confirm)</li>
</ol>
<p>then<br>
2) Attempt to establish a socket connection via matlab  class:<br>
The MATLAB socket control file does not ship with the SlicerAutoscoper extension. It can be found <a href="https://github.com/BrownBiomechanics/Autoscoper/blob/main/scripts/matlab" rel="noopener nofollow ugc">here</a><br>
<a href="https://github.com/BrownBiomechanics/Autoscoper/blob/main/scripts/matlab" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/BrownBiomechanics/Autoscoper/blob/main/scripts/matlab</a></p>
<p>i) take a look at the readme and download AutoscoperConnection.m<br>
ii)  launch autoscoper within 3dslicer<br>
iii) open matlab (suggest ver &gt; 2022a)</p>
<p>copy the following into a new script, or run in command window:</p>
<pre><code class="lang-auto">local_AC_dir = uigetdir('C:\', 'Select directory containing recently downloaded AutoscoperConnection.m');
%path to AutoscoperConneciton class 
addpath(local_AC_dir);

localSampleDir = uigetdir('C:\', 'Select directory containing SampleData cfg file');

%openConnection('127.0.0.1');
aobj =  AutoscoperConnection();

cfgFileName =  fullfile(localSampleDir , '2023-07-20-Wrist.cfg');
loadTrial(aobj,cfgFileName);
</code></pre>

---

## Post #6 by @Lauren_Welte (2025-01-17 20:30 UTC)

<p>Thanks so much.</p>
<p>The configuration file is in the proper folder, so we were able to access that.</p>
<p>When we used the MATLAB socket, this is the error we are getting:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c82be90db3fa06a65ac1955bd820e56c79c0efc.png" data-download-href="/uploads/short-url/mkyBrF5jkF25ir13FxnD7zaWtwo.png?dl=1" title="image (8)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c82be90db3fa06a65ac1955bd820e56c79c0efc_2_690x357.png" alt="image (8)" data-base62-sha1="mkyBrF5jkF25ir13FxnD7zaWtwo" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c82be90db3fa06a65ac1955bd820e56c79c0efc_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c82be90db3fa06a65ac1955bd820e56c79c0efc_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c82be90db3fa06a65ac1955bd820e56c79c0efc_2_1380x714.png 2x" data-dominant-color="D7D5D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image (8)</span><span class="informations">1918×993 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Seems like something related to the operating system, but as far as I know it meets all the required specs.</p>

---

## Post #7 by @Amy_Morton (2025-01-21 21:34 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>  <a class="mention" href="/u/lauren_welte">@Lauren_Welte</a> is experiencing sample data launch issues with machine</p>
<p>Windows 11<br>
NVIDIA RTX 2000 Ada Generation</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/e/3e66e383dbd148a0b8b4301a338e46c3d2140f79.png" data-download-href="/uploads/short-url/8U22yAENx7k0Y24BSfiMGwmyjCF.png?dl=1" title="Screenshot 2024-12-19 124657" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e66e383dbd148a0b8b4301a338e46c3d2140f79_2_690x353.png" alt="Screenshot 2024-12-19 124657" data-base62-sha1="8U22yAENx7k0Y24BSfiMGwmyjCF" width="690" height="353" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e66e383dbd148a0b8b4301a338e46c3d2140f79_2_690x353.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e66e383dbd148a0b8b4301a338e46c3d2140f79_2_1035x529.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/e/3e66e383dbd148a0b8b4301a338e46c3d2140f79_2_1380x706.png 2x" data-dominant-color="111111"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-12-19 124657</span><span class="informations">1913×981 42.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(error in opencl and cuda launch - though different error reporting)<br>
We went through some obvious tests to rule out simple errors in the thread above</p>
<p>could you weigh in please?</p>

---

## Post #8 by @Amy_Morton (2025-02-03 16:05 UTC)

<p><a class="mention" href="/u/lauren_welte">@Lauren_Welte</a> are you able to successfully load sample data on any other machine in your institution? I’m wondering if you have security network traffic limitations that may be interfering with the IP based connection</p>

---

## Post #9 by @Lauren_Welte (2025-02-05 20:14 UTC)

<p>Hi Amy!  I am able to load the sample data on my other laptop both when wired into our network, and on our university wi-fi. The issue so far seems localized to that computer.</p>

---

## Post #10 by @jcfr (2025-02-06 15:32 UTC)

<p><a class="mention" href="/u/lauren_welte">@Lauren_Welte</a>  do you happen to have two video cards on your system ?</p>
<p>Related:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/windows-10-is-now-handling-the-gpu-selection/13064" class="inline-onebox">WIndows 10 is now handling the gpu selection</a></li>
<li><a href="https://www.makeuseof.com/windows-10-choose-preferred-gpu/">https://www.makeuseof.com/windows-10-choose-preferred-gpu/</a></li>
</ul>
<h2><a name="p-122225-details-1" class="anchor" href="#p-122225-details-1" aria-label="Heading link"></a>Details</h2>
<p>Since issues happen with both backend, we need to first confirm there are two video card and then ensure the NVIDIA one is used.</p>
<h3><a name="p-122225-cuda-backend-2" class="anchor" href="#p-122225-cuda-backend-2" aria-label="Heading link"></a>CUDA Backend</h3>
<p>Based on the screenshot shared above <sup class="footnote-ref"><a href="#footnote-122225-1" id="footnote-ref-122225-1">[1]</a></sup>, the code triggering the error when using the CUDA backend can be inspected here (line 400):</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/BrownBiomechanics/Autoscoper/blob/dd32d16390c71b46641173aac9ad311ead9dfd39/libautoscoper/src/View.cpp#L396-L405">
  <header class="source">

      <a href="https://github.com/BrownBiomechanics/Autoscoper/blob/dd32d16390c71b46641173aac9ad311ead9dfd39/libautoscoper/src/View.cpp#L396-L405" target="_blank" rel="noopener">github.com/BrownBiomechanics/Autoscoper</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/BrownBiomechanics/Autoscoper/blob/dd32d16390c71b46641173aac9ad311ead9dfd39/libautoscoper/src/View.cpp#L396-L405" target="_blank" rel="noopener">libautoscoper/src/View.cpp</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/BrownBiomechanics/Autoscoper/blob/dd32d16390c71b46641173aac9ad311ead9dfd39/libautoscoper/src/View.cpp#L396-L405" rel="noopener"><code>dd32d1639</code></a>
</div>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="396" style="counter-reset: li-counter 395 ;">
          <li>void View::render(unsigned int pbo, unsigned width, unsigned height)</li>
          <li>{</li>
          <li>#if defined(Autoscoper_RENDERING_USE_CUDA_BACKEND)</li>
          <li>  struct cudaGraphicsResource* pboCudaResource;</li>
          <li>  cutilSafeCall(cudaGraphicsGLRegisterBuffer(&amp;pboCudaResource, pbo, cudaGraphicsMapFlagsWriteDiscard));</li>
          <li></li>
          <li>  float* buffer = NULL;</li>
          <li>  size_t numOfBytes;</li>
          <li>  cutilSafeCall(cudaGraphicsMapResources(1, &amp;pboCudaResource, 0));</li>
          <li>  cutilSafeCall(cudaGraphicsResourceGetMappedPointer((void**)&amp;buffer, &amp;numOfBytes, pboCudaResource));</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The problematic call seems to be related to <code>cudaGraphicsGLRegisterBuffer</code><sup class="footnote-ref"><a href="#footnote-122225-2" id="footnote-ref-122225-2">[2]</a></sup>, note that is expected to be supported and not marked as deprecated.</p>
<h3><a name="p-122225-opencl-backend-3" class="anchor" href="#p-122225-opencl-backend-3" aria-label="Heading link"></a>OpenCL backend</h3>
<p>Based on the screenshot shared above <sup class="footnote-ref"><a href="#footnote-122225-3" id="footnote-ref-122225-3">[3]</a></sup>, the code triggering the error when using the OpenCL backend can be inspected here (line 739):</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/BrownBiomechanics/Autoscoper/blob/dd32d16390c71b46641173aac9ad311ead9dfd39/libautoscoper/src/gpu/opencl/OpenCL.cpp#L732-L742">
  <header class="source">

      <a href="https://github.com/BrownBiomechanics/Autoscoper/blob/dd32d16390c71b46641173aac9ad311ead9dfd39/libautoscoper/src/gpu/opencl/OpenCL.cpp#L732-L742" target="_blank" rel="noopener">github.com/BrownBiomechanics/Autoscoper</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/BrownBiomechanics/Autoscoper/blob/dd32d16390c71b46641173aac9ad311ead9dfd39/libautoscoper/src/gpu/opencl/OpenCL.cpp#L732-L742" target="_blank" rel="noopener">libautoscoper/src/gpu/opencl/OpenCL.cpp</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/BrownBiomechanics/Autoscoper/blob/dd32d16390c71b46641173aac9ad311ead9dfd39/libautoscoper/src/gpu/opencl/OpenCL.cpp#L732-L742" rel="noopener"><code>dd32d1639</code></a>
</div>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="732" style="counter-reset: li-counter 731 ;">
          <li>    pfn_clGetGLContextInfoKHR(prop, CL_DEVICES_FOR_GL_CONTEXT_KHR, 10 * sizeof(cl_device_id), devices_, &amp;size);</li>
          <li>    // Create a context using the supported devices</li>
          <li>    int _count = size / sizeof(cl_device_id);</li>
          <li>    if (used_device &gt;= _count)</li>
          <li>      used_device = 0;</li>
          <li>    // fprintf(stderr,"%d Devices \n",_count);</li>
          <li>    context_ = clCreateContext(prop, 1, &amp;devices_[used_device], NULL, NULL, &amp;err_);</li>
          <li>    CHECK_CL</li>
          <li>#else</li>
          <li>#  pragma OPENCL EXTENSION cl_khr_gl_sharing : enable</li>
          <li>    cl_context_properties prop[] = { CL_GL_CONTEXT_KHR,</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-122225-1" class="footnote-item"><p><a href="https://discourse.slicer.org/t/trouble-loading-sample-data-in-slicerautoscoperm/41003/6" class="inline-onebox">Trouble loading sample data in SlicerAutoscoperM - #6 by Lauren_Welte</a> <a href="#footnote-ref-122225-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-122225-2" class="footnote-item"><p><a href="https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__OPENGL.html#group__CUDART__OPENGL_1g0fd33bea77ca7b1e69d1619caf44214b" class="inline-onebox">CUDA Runtime API :: CUDA Toolkit Documentation</a> <a href="#footnote-ref-122225-2" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-122225-3" class="footnote-item"><p><a href="https://discourse.slicer.org/t/trouble-loading-sample-data-in-slicerautoscoperm/41003/4" class="inline-onebox">Trouble loading sample data in SlicerAutoscoperM - #4 by Lauren_Welte</a> <a href="#footnote-ref-122225-3" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---
