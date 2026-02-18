# Industry Standard Image Set for Radiomics Programs

**Topic ID**: 3662
**Date**: 2018-08-04
**URL**: https://discourse.slicer.org/t/industry-standard-image-set-for-radiomics-programs/3662

---

## Post #1 by @Candace_Moore (2018-08-04 21:27 UTC)

<p>I’ve developed some programming for texture analysis. Is there a standard image set I can test these on?</p>

---

## Post #2 by @lassoan (2018-08-04 21:42 UTC)

<p>There are thousands of images available freely on the cancer imaging archive (TCIA) website.</p>
<p>How do you plan to test? How do you plan to get gold standard to compare against?</p>
<p>Have you implemented similar features as in SlicerRadiomics/pyRadiomics?</p>

---

## Post #3 by @fedorov (2018-08-04 23:02 UTC)

<p>You could check out the Imaging Biomarker Standardization Initiative that focuses on standardizing definitions of the radiomics features and their testing: <a href="https://arxiv.org/abs/1612.07003">https://arxiv.org/abs/1612.07003</a></p>

---

## Post #4 by @fedorov (2018-08-05 23:07 UTC)

<p><a class="mention" href="/u/candace_moore">@Candace_Moore</a> also note that the IBSI group set up a dedicated forum, which might be best place to ask questions about radiomics feature standardization: <a href="https://groups.google.com/forum/#!forum/the_ibsi">https://groups.google.com/forum/#!forum/the_ibsi</a>. This forum is not linked from the document, and they are still working on a web site, so may not be easy to find. Hope this helps!</p>

---

## Post #5 by @Candace_Moore (2018-08-06 12:30 UTC)

<p>Thanks a lot. By the way this is Dr. Candace Makeda Moore. I wrote you an email asking the same, but you did not get back to me- probably did not see it. I’m a radiology resident who programs, among other things.</p>

---

## Post #6 by @fedorov (2018-08-06 12:53 UTC)

<p><a class="mention" href="/u/candace_moore">@Candace_Moore</a> yes, I realized that I forgot to respond to your email when I saw this post. I am glad you found the forum, since this is really the best place to discuss the topic and get different views!</p>

---

## Post #7 by @fedorov (2018-08-10 14:52 UTC)

<p>To add another piece of information provided to the user by email - this page might be of interest: <a href="http://www.radiomics.world/?q=node/28" class="inline-onebox">Radiomics.world - Home</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af31e1036d385bbac0890b3ef62f5438cfa529c5.png" data-download-href="/uploads/short-url/oZQqc6CQMNnd15LpoFjFpb5k6rj.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af31e1036d385bbac0890b3ef62f5438cfa529c5_2_690x329.png" alt="image" data-base62-sha1="oZQqc6CQMNnd15LpoFjFpb5k6rj" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af31e1036d385bbac0890b3ef62f5438cfa529c5_2_690x329.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af31e1036d385bbac0890b3ef62f5438cfa529c5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af31e1036d385bbac0890b3ef62f5438cfa529c5.png 2x" data-dominant-color="D6E5E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1010×483 92.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Candace_Moore (2018-08-10 15:14 UTC)

<p>Thanks a lot! I will try to evaluate the phantom with my program!</p>

---

## Post #9 by @fedorov (2018-08-10 15:27 UTC)

<p><a class="mention" href="/u/candace_moore">@Candace_Moore</a> great, I am glad this looks helpful.</p>
<p>Out of curiosity, what was your motivation to develop a new implementation of radiomics texture extraction? I assume you looked at <a href="http://pyradiomics.readthedocs.io/">pyradiomics</a>, since it was mentioned earlier - did it not include the specific texture type you wanted to see? Was it slow? Did you have any other concerns to justify new development?</p>

---

## Post #10 by @Candace_Moore (2018-08-10 15:53 UTC)

<p>I used to be an emergency doctor who knew almost nothing about radiology. Then a couple years ago I got married and had a tumor discovered in the span of two months. It was not even two years ago when I asked the secretary of the radiology department where I now work to see if I could meet the head of the department to talk about maybe training to become a radiologist-if I survived. The tumor turned out to be a benign one that just looked like a cancer. Lieing around recovering from a major surgery, I had a lot of time on my hands to play with images. I also used to be a failing artist who made some money as a programmer, so when I say play with images I mean do all sorts of stuff. I only discovered pyradiomics AFTER developing my program. Sadly, I think I may be ahead of the curve when it comes to most radiologists on this stuff. I now see that many radiologists hear about this at conferences, but the understanding of what it actually is seems low. And because many radiologists don’t understand it- they suffer both fear of the unknown and ignorance of the potential benefits. What keeps me motivated to keep making my (in some ways inferior) program is that maybe, just maybe, I could do work that will help someone else not have the anxiety of not understanding whether they have cancer until pathology comes back, the pain of major surgery, and a really ugly surgical scar they will have forever. Making the tool already has had the side effect that I am probably the most knowledgeable about radiomics where I work. I hope that in the future I can develop some novel texture features. I have ideas for things I have not read about. I hope that is on topic.</p>

---

## Post #11 by @fedorov (2018-08-10 16:12 UTC)

<p>Thanks for the story, and congratulations on your success in mastering radiomics!</p>
<p>Note that maintenance of an open source project is a non-trivial effort. pyradiomics <a href="https://github.com/Radiomics/pyradiomics/graphs/contributors">has been around for some time</a>, has <a href="https://github.com/Radiomics/pyradiomics/stargazers">a sizeable user base</a>, <a href="https://scholar.google.com/scholar?oi=bibs&amp;hl=en&amp;cites=12620308458045367421">academic papers that used it</a>, has <a href="http://pyradiomics.readthedocs.io/en/latest/">comprehensive documentation</a>, and it has been developed with significant resources investment.</p>
<p>At the same time, pyradiomics is open source and contributions and improvements are always welcomed.</p>
<p>If your goal is to help other users, it might be most productive and efficient to</p>
<ol>
<li>Identify missing functionality in pyradiomics (if any)</li>
<li>Improve pyradiomics to implement the missing features, so that they are quickly available to the large existing community of the library.</li>
</ol>
<p>My suggestion is the approach above is more productive as compared to developing yet another radiomics library that you would need to maintain on your spare time, which you could otherwise use to take rest from your emergency room duties, or to apply the library to seek new discoveries from the clinical images.</p>
<p>Of course, it is your decision in the end, but I wanted to share this suggestion based on my experience.</p>
<p>cc: <a class="mention" href="/u/joostjm">@JoostJM</a></p>

---

## Post #12 by @Candace_Moore (2018-08-10 16:29 UTC)

<p>I looked at some of the code behind Pyradiomics, and for my research purposes it turns out to be good that I developed my own. Specifically, I’m very interested in entropy, and I think my code gives me more choices about how I look at it. And now that I developed something people in my department can use easily, I’m motivated to add other variables that no one else has done yet. These new variables, I can test in my tool without bothering to deal with whatever it takes to make stuff for Pyradiomics (I have no idea)…and in all likelyhood just prove they are a useless waste of time. Or maybe not. I won’t know until I try, and the simpler the interface, the easier it will be to get my colleagues to try something they don’t understand.</p>

---

## Post #13 by @fedorov (2018-08-10 16:41 UTC)

<p>Sounds good, and good luck with your project!</p>

---

## Post #14 by @Candace_Moore (2018-08-11 12:36 UTC)

<p>Also, I will be happy to contribute my version of entropy calculations once I have real ‘proof’ that they work correctly. I’ll be happy to contribute a lot of things into the open source project, so long as it can be done in the framework of some kind of academic collaboration. Otherwise, I suspect my higher-ups won’t accept me spending my time this way.</p>

---
