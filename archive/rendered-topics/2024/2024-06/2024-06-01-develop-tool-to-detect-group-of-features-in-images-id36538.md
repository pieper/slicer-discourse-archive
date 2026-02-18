# Develop tool to detect group of features in images

**Topic ID**: 36538
**Date**: 2024-06-01
**URL**: https://discourse.slicer.org/t/develop-tool-to-detect-group-of-features-in-images/36538

---

## Post #1 by @sajad_amiri (2024-06-01 11:29 UTC)

<p>as a clinician and researcher I found that it is important to know which radiomics features occur in a specific  part of our dicom file, I have ideas to solve this, but I need a collaborative group</p>

---

## Post #2 by @lassoan (2024-06-01 11:30 UTC)

<p>We may be able to help but we would need a bit more information.</p>

---

## Post #3 by @sajad_amiri (2024-06-01 11:54 UTC)

<p>Hello, dear Andras.<br>
For instance, in Radiology, sometimes we refer to encapsulation. This is a clinical term that signifies certain characteristics, such as contrast features within specific pixels. By segmenting our Region of Interest (ROI) into multiple parts and assigning location data to each part, we can identify two neighboring high-contrast features. These neighboring features, with close proximity to each other in a circular pattern, indicate a nodule in our MRI, for example. The distinction between encapsulated and non-encapsulated lies in the presence of two contrasts: one between the tumor (lesion) and its capsule, and another between the capsule and the surrounding area. Inside the lesion, we observe hyper-intensity and heterogeneity, both of which contribute to a set of features within a specific area of our ROI or DICOM.</p>
<p>I am working on Radiomics and explainable AI in Cancer Imaging, I found there is a shortcoming in our features . we can made a new features and have a better AI models</p>

---

## Post #4 by @sajad_amiri (2024-06-01 12:04 UTC)

<p>furthermore we can set an appointment and I explain it on a DICOM file<br>
‬</p>

---

## Post #5 by @lassoan (2024-06-01 12:18 UTC)

<aside class="quote no-group" data-username="sajad_amiri" data-post="3" data-topic="36538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sajad_amiri/48/78661_2.png" class="avatar"> sajad_amiri:</div>
<blockquote>
<p>The distinction between encapsulated and non-encapsulated lies in the presence of two contrasts: one between the tumor (lesion) and its capsule, and another between the capsule and the surrounding area.</p>
</blockquote>
</aside>
<p>It would be nice to be able to develop this kind of classic, rule-based algorithms, but these approaches failed to lead to practically usable algorithms in the past several decades. Usually the problem is that you implement some high-level rule, that does not work quite well enough, so you need keep adding more and more small additional algorithms to address shortcomings, which makes the implementation slow, complex, hard to maintain, and hard to generalize for more data.</p>
<p>In contrast, learning from many examples (and let the AI model to figure out what features to recognize and how) seems to work very well and can reach human-level performance even from a reasonable number of examples (maybe even just few hundred cases). If the performance is not good enough then you can just add more data. If you have sufficient amount of training data then it is guaranteed that you can train a model that works well.</p>
<p>So, I would recommend to prepare a high-quality data set (manually annotate nodule locations and classification result) and train one of the most commonly used classifier networks on this data using <a href="https://monai.io/">MONAI</a>.</p>

---

## Post #6 by @sajad_amiri (2024-06-01 12:26 UTC)

<p>Thanks too much for your great answer , again I want to emphasis to add location , if we know which Radiomics features are where located and clinician knows the equal meaning of that features , it help clinician to make a better decision, it is important some changes happen in which part of our tumor(ROI)</p>

---

## Post #7 by @lassoan (2024-06-01 12:34 UTC)

<aside class="quote no-group" data-username="sajad_amiri" data-post="6" data-topic="36538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sajad_amiri/48/78661_2.png" class="avatar"> sajad_amiri:</div>
<blockquote>
<p>again I want to emphasis to add location</p>
</blockquote>
</aside>
<p>That’s why I recommended above to include the location in the training data set. You can train a network to recognize tumor locations and then extract a region around that position and use it as input for the classifier.</p>
<p>If the result you want is not a yes/no answer (e.g., encapsulated or not) but you want regions labeled in the image then you can segment the image and use that as training data.</p>

---

## Post #8 by @sajad_amiri (2024-06-01 12:37 UTC)

<p>It was simple example , i want to translate Radiologist reports to Radiomics features and help to to solve the explainable AI models , machine learning models and , explainable features for clinician</p>

---

## Post #9 by @Akiragi (2024-06-14 06:56 UTC)

<aside class="quote no-group" data-username="sajad_amiri" data-post="1" data-topic="36538" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sajad_amiri/48/78661_2.png" class="avatar"> sajad_amiri:</div>
<blockquote>
<p>as a clinician and researcher I found that it is important to know which radiomics features occur in a specific part of our dicom file, I have ideas to solve this, but I need a collaborative group</p>
</blockquote>
</aside>
<p>Thank you for  participating your  perceptivity. I feel great to hear about your interest in radiomics.  I’m interested in learning  further about your ideas and how we can work together and can you partake  further details about your proposed  results and what specific  moxie or  coffers you’re looking for in a  cooperative group? <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @Akiragi (2024-06-14 06:57 UTC)

<p>also you  have ideas so you can share here</p>

---

## Post #11 by @sajad_amiri (2024-06-14 09:35 UTC)

<p>Hello dear Akiragi,<br>
This is my gmail: <a href="mailto:sajadamiri19921400@gmail.com">sajadamiri19921400@gmail.com</a><br>
Please send me email</p>

---
