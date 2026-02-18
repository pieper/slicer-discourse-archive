# Active Learning Strategies in MONAI

**Topic ID**: 33400
**Date**: 2023-12-15
**URL**: https://discourse.slicer.org/t/active-learning-strategies-in-monai/33400

---

## Post #1 by @Spiros_Karkavitsas (2023-12-15 10:39 UTC)

<p>Hello</p>
<p>I have one basic question regarding the active learning appoach of MONAI label app in Slicer.</p>
<p>I understand the concept of active learning of MONAI. However, in the slicer I have two options: random or first</p>
<p>Initially, if you start from scratch the random approach is reasonable choice. However, if the accuracy of the model is improved and you select the strategy named as first then I do not get how the selection from the folder of unlabeled images is done.</p>
<p>I get the sense that the selection is done alphabetically and not based on a selection according to an uncertainty measurement.</p>
<p>Do I get it right?</p>
<p>Thank  you in advance for the time answering this question</p>

---

## Post #2 by @rbumm (2023-12-15 12:47 UTC)

<aside class="quote no-group" data-username="Spiros_Karkavitsas" data-post="1" data-topic="33400">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/spiros_karkavitsas/48/18224_2.png" class="avatar"> Spiros_Karkavitsas:</div>
<blockquote>
<p>I have one basic question regarding the active learning appoach of MONAI label app in Slicer.</p>
<p>I understand the concept of active learning of MONAI. However, in the slicer I have two options: random or first</p>
<p>Initially, if you start from scratch the random approach is reasonable choice. However, if the accuracy of the model is improved and you select the strategy named as first then I do not get how the selection from the folder of unlabeled images is done.</p>
<p>I get the sense that the selection is done alphabetically and not based on a selection according to an uncertainty measurement.</p>
<p>Do I get it right?</p>
</blockquote>
</aside>
<p>ChatGPT´s response:</p>
<p>Your understanding of the active learning approach in MONAI Label, particularly within the Slicer application, is on the right track. Active learning in this context is used to select which images from a pool of unlabeled data should be labeled next to improve the model’s performance most effectively.</p>
<p>In MONAI Label’s active learning implementation within Slicer, the options ‘random’ and ‘first’ refer to the strategies for selecting the next image to be annotated:</p>
<ol>
<li><strong>Random</strong>: This strategy selects an image at random from the pool of unlabeled images. This approach is useful, especially at the beginning when the model hasn’t been trained much and there’s no clear indication of which images might be more informative for the model.</li>
<li><strong>First</strong>: This strategy, as you noted, might seem to select the first image in the folder, which often is in alphabetical or some other predetermined order (like the order of file creation or modification). This method doesn’t necessarily select the most informative or uncertain images for labeling, but rather follows a fixed order.</li>
</ol>
<p>Ideally, in an advanced active learning setup, you would expect the system to select images based on some measure of uncertainty or informativeness. This means the system would analyze the pool of unlabeled images and prioritize those where the current model is least certain, as labeling these images would potentially provide the most significant improvement to the model.</p>
<p>However, it seems that in the current implementation of MONAI Label in Slicer, the ‘first’ strategy does not incorporate such an uncertainty-based selection mechanism. Instead, it follows a predetermined order, which might not be as efficient as an uncertainty-based approach in improving the model’s accuracy.</p>
<p>In practice, this means that if you’re looking to leverage the full potential of active learning, you might need to look for or implement a more sophisticated selection strategy that can assess and prioritize images based on the model’s uncertainty or other relevant criteria. This would ensure a more targeted and efficient learning process, leading to faster improvements in the model’s performance.</p>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> might validate and comment this information.</p>

---

## Post #3 by @Spiros_Karkavitsas (2023-12-15 12:56 UTC)

<p>Hello and thank you for the answer.</p>
<p>In short as I understand the active learning was not enabled during my training.</p>
<p>I am asking because I am writing a paper and I want to be as accurate as I can be regarding this.</p>
<p>Also, I found a couple of papers describing the MONAI Core and MONAI Label.</p>
<p>Which one of them should I cite ? I can imagine the latter but I would like your input on that.</p>
<p>Best<br>
Spiros</p>

---

## Post #4 by @rbumm (2023-12-15 14:05 UTC)

<aside class="quote no-group" data-username="Spiros_Karkavitsas" data-post="3" data-topic="33400">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/spiros_karkavitsas/48/18224_2.png" class="avatar"> Spiros_Karkavitsas:</div>
<blockquote>
<p>Which one of them should I cite ?</p>
</blockquote>
</aside>
<p>I would cite the latter.</p>

---
