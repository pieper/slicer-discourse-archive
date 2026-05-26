---
topic_id: 46227
title: "ALPACA error; Version 5.10.0 (stable)"
date: 2026-02-20
url: https://discourse.slicer.org/t/46227
last_bumped: 2026-02-23T17:42:47.834Z
---

# ALPACA error; Version 5.10.0 (stable)

**Topic ID**: 46227
**Date**: 2026-02-20
**URL**: https://discourse.slicer.org/t/alpaca-error-version-5-10-0-stable/46227

---

## Post #1 by @juliangallaun (2026-02-20 09:25 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322.jpeg" data-download-href="/uploads/short-url/4YSpoNet2TFp6ygLVtfOoaJQ84q.jpeg?dl=1" title="Screenshot_alpaca_error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322_2_690x247.jpeg" alt="Screenshot_alpaca_error" data-base62-sha1="4YSpoNet2TFp6ygLVtfOoaJQ84q" width="690" height="247" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322_2_690x247.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322_2_1035x370.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/2/22ea63882bcf80b0940b9d637f745a5123720322_2_1380x494.jpeg 2x" data-dominant-color="272525"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_alpaca_error</span><span class="informations">1525×548 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><span lang="EN-GB">Hello all,</span></p>
<p><span lang="EN-GB">  </span></p>
<p><span lang="EN-GB">I have a problem opening the ALPACA extension, with the stable version of 3D slicer 5.10.0 .</span></p>
<p><span lang="EN-GB">The error code says, it can’t find a certain file. I should have installed all additional extensions to run the extension. I reinstalled the extension again, without solving the problem. On the version 5.8.1 ALPACA works on my device.</span></p>
<p><span lang="EN-GB">Thank you for your help and advice.</span></p>

---

## Post #2 by @drnoorfatima (2026-02-20 10:29 UTC)

<p>Hi!</p>
<p>The issue is a missing itk Python package in Slicer 5.10.0’s environment. Open the Python Interactor in Slicer and run:</p>
<p>slicer.util.pip_install(‘itk’)</p>
<p>Then restart Slicer and try opening ALPACA again. That should fix it!</p>

---

## Post #3 by @juliangallaun (2026-02-20 10:58 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08.jpeg" data-download-href="/uploads/short-url/A5kWywGOC3iEFaiaBGHRun4Pxfq.jpeg?dl=1" title="Screenshot_alpaca_error1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08_2_690x275.jpeg" alt="Screenshot_alpaca_error1" data-base62-sha1="A5kWywGOC3iEFaiaBGHRun4Pxfq" width="690" height="275" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08_2_690x275.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08_2_1035x412.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fce8bae70387ab958e80d8bb49087b3f62ac4c08_2_1380x550.jpeg 2x" data-dominant-color="282524"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_alpaca_error1</span><span class="informations">1505×601 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I did run the command and this was the reply. Nothing changed regarding the problem.</p>

---

## Post #4 by @muratmaga (2026-02-20 16:43 UTC)

<p>It appears your slicer 5.10 installation is problematic for some reason. E.g., the real issue is the first error (Application Does Not exist).</p>
<p>I suggest freshly installing it to a new place (like your desktop), install SlicerMorph and retry.</p>

---

## Post #5 by @juliangallaun (2026-02-20 17:00 UTC)

<p>Ok, I did that and got the exact same error as the first time.</p>
<p>I did save it on the desktop as you suggested.</p>

---

## Post #6 by @muratmaga (2026-02-20 19:15 UTC)

<p>what happens when you do the <code>pip_install(“itk”)</code></p>

---

## Post #7 by @juliangallaun (2026-02-23 14:25 UTC)

<p><span lang="EN-GB">The second screenshot shows just that or did I do something wrong? It says the Application does not exist.</span></p>

---

## Post #8 by @muratmaga (2026-02-23 17:07 UTC)

<p>I think there is something weird going on with your installation, though don’t know why. I am going to assume you will get the same problem if you try to pip install another package, like <code>pip_install(“scipy”)</code></p>

---

## Post #9 by @juliangallaun (2026-02-23 17:21 UTC)

<p>Yes, the same error occurs. The Application does not exist.</p>

---

## Post #10 by @muratmaga (2026-02-23 17:37 UTC)

<p>I don’t why. I Just did a fresh install of a 5.10 package I downloaded from <a href="http://download.slicer.org" rel="noopener nofollow ugc">download.slicer.org</a>, installed SlicerMorph and run ALPACA on my windows computer and everything worked as expected. I wonder if you have antivirus or centrally managed something that removes files. All I can say maybe try with a different computer</p>
<pre><code class="lang-auto">Python 3.12.10 (main, Feb 12 2026, 15:11:32) [MSC v.1944 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
[Qt] libpng warning: iCCP: profile 'ICC Profile': 'CMYK': invalid ICC profile color space
[Qt] libpng warning: iCCP: known incorrect sRGB profile
Collecting mistune
  Downloading mistune-3.2.0-py3-none-any.whl.metadata (1.9 kB)
Downloading mistune-3.2.0-py3-none-any.whl (53 kB)
Installing collected packages: mistune
Successfully installed mistune-3.2.0
Collecting itk~=5.4.0
  Downloading itk-5.4.5-cp311-abi3-win_amd64.whl.metadata (22 kB)
Collecting itk-core==5.4.5 (from itk~=5.4.0)
  Downloading itk_core-5.4.5-cp311-abi3-win_amd64.whl.metadata (22 kB)
Collecting itk-numerics==5.4.5 (from itk~=5.4.0)
  Downloading itk_numerics-5.4.5-cp311-abi3-win_amd64.whl.metadata (22 kB)
Collecting itk-io==5.4.5 (from itk~=5.4.0)
  Downloading itk_io-5.4.5-cp311-abi3-win_amd64.whl.metadata (22 kB)
Collecting itk-filtering==5.4.5 (from itk~=5.4.0)
  Downloading itk_filtering-5.4.5-cp311-abi3-win_amd64.whl.metadata (22 kB)
Collecting itk-registration==5.4.5 (from itk~=5.4.0)
  Downloading itk_registration-5.4.5-cp311-abi3-win_amd64.whl.metadata (22 kB)
Collecting itk-segmentation==5.4.5 (from itk~=5.4.0)
  Downloading itk_segmentation-5.4.5-cp311-abi3-win_amd64.whl.metadata (22 kB)
Requirement already satisfied: numpy in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk~=5.4.0) (2.0.2)
Downloading itk-5.4.5-cp311-abi3-win_amd64.whl (16 kB)
Downloading itk_core-5.4.5-cp311-abi3-win_amd64.whl (37.4 MB)
   ---------------------------------------- 37.4/37.4 MB 17.5 MB/s eta 0:00:00
Downloading itk_filtering-5.4.5-cp311-abi3-win_amd64.whl (23.6 MB)
   ---------------------------------------- 23.6/23.6 MB 17.4 MB/s eta 0:00:00
Downloading itk_io-5.4.5-cp311-abi3-win_amd64.whl (8.7 MB)
   ---------------------------------------- 8.7/8.7 MB 14.6 MB/s eta 0:00:00
Downloading itk_numerics-5.4.5-cp311-abi3-win_amd64.whl (19.7 MB)
   ---------------------------------------- 19.7/19.7 MB 20.8 MB/s eta 0:00:00
Downloading itk_registration-5.4.5-cp311-abi3-win_amd64.whl (9.5 MB)
   ---------------------------------------- 9.5/9.5 MB 13.8 MB/s eta 0:00:00
Downloading itk_segmentation-5.4.5-cp311-abi3-win_amd64.whl (5.0 MB)
   ---------------------------------------- 5.0/5.0 MB 23.5 MB/s eta 0:00:00
Installing collected packages: itk-core, itk-numerics, itk-io, itk-filtering, itk-segmentation, itk-registration, itk

Successfully installed itk-5.4.5 itk-core-5.4.5 itk-filtering-5.4.5 itk-io-5.4.5 itk-numerics-5.4.5 itk-registration-5.4.5 itk-segmentation-5.4.5
Collecting scikit-learn
  Downloading scikit_learn-1.8.0-cp312-cp312-win_amd64.whl.metadata (11 kB)
Requirement already satisfied: numpy&gt;=1.24.1 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from scikit-learn) (2.0.2)
Requirement already satisfied: scipy&gt;=1.10.0 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from scikit-learn) (1.13.1)
Collecting joblib&gt;=1.3.0 (from scikit-learn)
  Downloading joblib-1.5.3-py3-none-any.whl.metadata (5.5 kB)
Collecting threadpoolctl&gt;=3.2.0 (from scikit-learn)
  Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)
Downloading scikit_learn-1.8.0-cp312-cp312-win_amd64.whl (8.0 MB)
   ---------------------------------------- 8.0/8.0 MB 82.5 MB/s eta 0:00:00
Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
Using cached threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Installing collected packages: threadpoolctl, joblib, scikit-learn

Successfully installed joblib-1.5.3 scikit-learn-1.8.0 threadpoolctl-3.6.0
Collecting itk-fpfh~=0.2.0
  Downloading itk_fpfh-0.2.1-cp311-abi3-win_amd64.whl.metadata (16 kB)
Requirement already satisfied: itk==5.4.* in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk-fpfh~=0.2.0) (5.4.5)
Requirement already satisfied: itk-core==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-fpfh~=0.2.0) (5.4.5)
Requirement already satisfied: itk-numerics==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-fpfh~=0.2.0) (5.4.5)
Requirement already satisfied: itk-io==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-fpfh~=0.2.0) (5.4.5)
Requirement already satisfied: itk-filtering==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-fpfh~=0.2.0) (5.4.5)
Requirement already satisfied: itk-registration==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-fpfh~=0.2.0) (5.4.5)
Requirement already satisfied: itk-segmentation==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-fpfh~=0.2.0) (5.4.5)
Requirement already satisfied: numpy in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-fpfh~=0.2.0) (2.0.2)
Downloading itk_fpfh-0.2.1-cp311-abi3-win_amd64.whl (459 kB)
Installing collected packages: itk-fpfh
Successfully installed itk-fpfh-0.2.1
Collecting itk-ransac~=0.2.1
  Downloading itk_ransac-0.2.1-cp311-abi3-win_amd64.whl.metadata (17 kB)
Requirement already satisfied: itk==5.4.* in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk-ransac~=0.2.1) (5.4.5)
Requirement already satisfied: itk-core==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-ransac~=0.2.1) (5.4.5)
Requirement already satisfied: itk-numerics==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-ransac~=0.2.1) (5.4.5)
Requirement already satisfied: itk-io==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-ransac~=0.2.1) (5.4.5)
Requirement already satisfied: itk-filtering==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-ransac~=0.2.1) (5.4.5)
Requirement already satisfied: itk-registration==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-ransac~=0.2.1) (5.4.5)
Requirement already satisfied: itk-segmentation==5.4.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-ransac~=0.2.1) (5.4.5)
Requirement already satisfied: numpy in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from itk==5.4.*-&gt;itk-ransac~=0.2.1) (2.0.2)
Downloading itk_ransac-0.2.1-cp311-abi3-win_amd64.whl (545 kB)
   --------------------------------------- 545.1/545.1 kB 17.7 MB/s eta 0:00:00
Installing collected packages: itk-ransac
Successfully installed itk-ransac-0.2.1
Collecting cpdalp
  Downloading cpdalp-1.2.0-py3-none-any.whl.metadata (2.8 kB)
Requirement already satisfied: numpy in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from cpdalp) (2.0.2)
Downloading cpdalp-1.2.0-py3-none-any.whl (18 kB)
Installing collected packages: cpdalp
Successfully installed cpdalp-1.2.0
Collecting pandas
  Downloading pandas-3.0.1-cp312-cp312-win_amd64.whl.metadata (19 kB)
Requirement already satisfied: numpy&gt;=1.26.0 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from pandas) (2.0.2)
Requirement already satisfied: python-dateutil&gt;=2.8.2 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from pandas) (2.9.0.post0)
Collecting tzdata (from pandas)
  Downloading tzdata-2025.3-py2.py3-none-any.whl.metadata (1.4 kB)
Requirement already satisfied: six&gt;=1.5 in c:\users\amaga\desktop\3d slicer 5.10.0\lib\python\lib\site-packages (from python-dateutil&gt;=2.8.2-&gt;pandas) (1.17.0)
Downloading pandas-3.0.1-cp312-cp312-win_amd64.whl (9.7 MB)
   ---------------------------------------- 9.7/9.7 MB 100.8 MB/s eta 0:00:00
Downloading tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Installing collected packages: tzdata, pandas

Successfully installed pandas-3.0.1 tzdata-2025.3

</code></pre>

---

## Post #11 by @juliangallaun (2026-02-23 17:42 UTC)

<p>You were right my antivirus was the cause of the problem now <span lang="EN-GB">everything </span>works fine.</p>

---
