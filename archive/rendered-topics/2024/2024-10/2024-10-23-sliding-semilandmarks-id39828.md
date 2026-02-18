# Sliding semilandmarks

**Topic ID**: 39828
**Date**: 2024-10-23
**URL**: https://discourse.slicer.org/t/sliding-semilandmarks/39828

---

## Post #1 by @Logan_Moore (2024-10-23 22:50 UTC)

<p>Hi guys,</p>
<p>I hope you are well, I just want to make sure I am understanding the workflow of Slicermorph and SlicermorphR correctly. Apologies if this seems simple but I must have have an error somewhere and it is driving me</p>
<p>When looking at the SlicermorphR page my code is essentially the same</p>
<pre><code class="lang-auto">##set your working directory!
files=dir(patt='json')
fixed.LMs &lt;- 1:2
semi.LMs &lt;- 3:82

#Array is LAND, DIM, IND
#where LAND is the number of landmarks
#where DIM is the number of dimensions
#where INd is the number of individuals

samples=gsub(".json","",fixed=T, files)
LMs &lt;- array(dim=c(82,3,10))

for (i in 1:10) LMs[,,i] = read.markups.json(files[i])
dimnames(LMs) &lt;- list(paste0("LM_",1:82), c("x", "y", "z"), samples)

#read in the curves file
curves&lt;-as.matrix(read.csv("curves.csv", header=FALSE))

#completes a GPA without sliding
defaultGPA&lt;- gpagen(A=LMs, surfaces = semi.LMs, ProcD = TRUE)
</code></pre>
<p>This runs and completes without issue, and everything is great, it is sliding that seems to be an issue.</p>
<p>If I understand correctly, I will run a PCA based on the newly acquired GPA.</p>
<p>Something like this:</p>
<pre><code class="lang-auto">DefaultPCA = gm.prcomp(defaultGPA$coords)
</code></pre>
<p>If I am sliding by Procrustes distance, it would look like this:</p>
<pre><code class="lang-auto">PDGPA&lt;- gpagen(A=LMs, curves=curves, surfaces = semi.LMs, ProcD = TRUE)
</code></pre>
<p>then</p>
<pre><code class="lang-auto">PDPCA = gm.prcomp(PDGPA$coords)
</code></pre>
<p>Then, to get it out, it would be the following?</p>
<pre><code class="lang-auto">geomorph2slicermorph2(gpa=defaultGPA, pca=DefaultPCA, paste0(output.path, "sliding'))

geomorph2slicermorph2(gpa=PDGPA, pca=PDPCA, paste0(output.path, "PDsliding')).
</code></pre>
<p>This then would give me files that I could then put back into Slicermorph to do visual analysis, correct?</p>
<p>Apologies again, I’ve been really wracking my brain on what is going wrong today.</p>

---

## Post #2 by @Logan_Moore (2024-10-23 23:53 UTC)

<aside class="quote no-group" data-username="Logan_Moore" data-post="1" data-topic="39828">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/logan_moore/48/69222_2.png" class="avatar"> Logan_Moore:</div>
<blockquote>
<p><code>geomorph2slicermorph2(gpa=defaultGPA, pca=DefaultPCA, paste0(output.path, "sliding'))</code></p>
</blockquote>
</aside>
<p>The good news is that its an output path issue, that bad news is that no matter how many times I format the output path, nothing shows up in the folder.</p>
<p>I currently altered it from the example as follows:</p>
<p>output.path=“C:/Users/Logan/Desktop/geomorph”</p>

---

## Post #3 by @Logan_Moore (2024-10-24 00:21 UTC)

<p>Alrighty guys, never mind me. I found my error, I was missing a singular “/” and it was dumping the materials to my desktop. Everything is working as intended.</p>

---

## Post #4 by @muratmaga (2024-10-24 00:50 UTC)

<p>Glad to hear that things are working. BTW the way, first GPA is redundant:</p>
<pre><code class="lang-auto">defaultGPA&lt;- gpagen(A=LMs, surfaces = semi.LMs, ProcD = TRUE)
</code></pre>
<p>Just do</p>
<pre><code class="lang-auto">PDGPA&lt;- gpagen(A=LMs, curves=curves, surfaces = semi.LMs, ProcD = TRUE)
PDPCA = gm.prcomp(PDGPA$coords)
geomorph2slicermorph2(gpa=PDGPA, pca=PDPCA, paste0(output.path, "PDsliding')).
</code></pre>

---

## Post #5 by @Logan_Moore (2024-10-29 02:02 UTC)

<p>Hi Murat,</p>
<p>I did adjust my code, as you suggested, my collaborates were really big on just wanting to see the output matched, so I did the regular GPA for that reason.</p>
<p>One quick follow-up: do you know why the slide landmarks and analysis won’t load into Slicermorph? I am on Slicer 5.6.2 with Slicermoprh version 5151748 and when I try to load an external analysis from R it just sits there blankly. I have included some data here for you to see (<a href="https://drive.google.com/drive/folders/1QYhMn4o3DRkgmaNVSiaU0QsQBlKkcl6q?usp=drive_link" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1QYhMn4o3DRkgmaNVSiaU0QsQBlKkcl6q?usp=drive_link</a>).</p>
<p>The original processed data still works, just not the items from Gemoorph2Slicermorph.</p>

---

## Post #6 by @muratmaga (2024-10-29 02:04 UTC)

<p>I don’t have permission to download the date.</p>

---

## Post #7 by @Logan_Moore (2024-10-29 02:05 UTC)

<p>Lets see if this one works: <a href="https://drive.google.com/drive/folders/1QYhMn4o3DRkgmaNVSiaU0QsQBlKkcl6q?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">5PDsliding - Google Drive</a></p>

---

## Post #8 by @muratmaga (2024-10-29 03:31 UTC)

<p>I successfully loaded this dataset into GPA module, no errors or anything?</p>
<p>I don’t know whether the results make sense, but at least you should be able to get without an issue.</p>
<p>I used a slightly newer version from October 11th. Try with a newer version, particularly if you are using the JSON formatted log files like the one your provided. The GPA in stable version is a bit stale. We are waiting for the new stable to come out in the next few weeks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/371c974dfa32cf1a8b4cd1fceb22820e6b02d3e0.png" data-download-href="/uploads/short-url/7Rxw2TmZJHsyIsB6sktC1NaBEQg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/371c974dfa32cf1a8b4cd1fceb22820e6b02d3e0_2_690x418.png" alt="image" data-base62-sha1="7Rxw2TmZJHsyIsB6sktC1NaBEQg" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/371c974dfa32cf1a8b4cd1fceb22820e6b02d3e0_2_690x418.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/371c974dfa32cf1a8b4cd1fceb22820e6b02d3e0_2_1035x627.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/371c974dfa32cf1a8b4cd1fceb22820e6b02d3e0_2_1380x836.png 2x" data-dominant-color="B4B4C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2359×1432 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Logan_Moore (2024-10-29 03:47 UTC)

<p>Ah, yes, thank you! It does seem to be an issue on 5.6.2. The preview build worked immediately. Thanks for the tip!</p>

---

## Post #10 by @muratmaga (2024-10-29 04:55 UTC)

<p>Yes, we need some of the features in the later preview version of Slicer, so SlicerMorph in 5.6.2 doesn’t have all the capability of later versions. A new stable will be out soon!</p>

---
