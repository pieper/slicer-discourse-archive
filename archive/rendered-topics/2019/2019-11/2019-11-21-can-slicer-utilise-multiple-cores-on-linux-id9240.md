---
topic_id: 9240
title: "Can Slicer Utilise Multiple Cores On Linux"
date: 2019-11-21
url: https://discourse.slicer.org/t/9240
---

# Can Slicer utilise multiple cores on linux?

**Topic ID**: 9240
**Date**: 2019-11-21
**URL**: https://discourse.slicer.org/t/can-slicer-utilise-multiple-cores-on-linux/9240

---

## Post #1 by @pll_llq (2019-11-21 10:23 UTC)

<p>Hi, I have a 40 GB NRRD that I need to work with. Currently, when I ask Slicer to load this volume it takes forever (over 15 minutes) and fails from time to time. I see that Slicer utilises only 1 out of the 14 cores and only 1.5 GB out of the 88 GBs of RAM that are available in the machine. Is there any way I can speed up load load time by specifying to Slicer to use more that one core?</p>

---

## Post #2 by @pieper (2019-11-21 13:33 UTC)

<p>Hi -</p>
<p>For a file that size it’s probably best not to compress it.  You can save the file uncompressed using the options checkbox in the save dialog.</p>
<p>Here’s a way to set compression off for all volume nodes if you want that:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_file_type_for_saving_for_all_volumes_.28with_already_existing_storage_nodes.29" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_file_type_for_saving_for_all_volumes_.28with_already_existing_storage_nodes.29</a></p>
<p>There’s more information in this thread:</p>
<aside class="quote quote-modified" data-post="1" data-topic="4488">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-unset-default-compress-option-during-save/4488">How to unset default 'compress' option during save</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
Is there a way to default compress option to NO for save dialog? Compress option is not visible immediately to new Slicer users, and compressing single threaded such large dataset (2000^3) is extremely slow. We are talking about 15 sec for uncomressed data and dozens of minutes with compress enabled on an ssd. Again for a new user, it is not immediately clear to the user whether Slicer stalled/crashed or doing something. 
In case someone wants to see, here is a test dataset: 
<a href="https://ndownloader.figshare.com/files/12808130" class="onebox" target="_blank" rel="noopener">https://ndownl…</a>
  </blockquote>
</aside>


---

## Post #3 by @muratmaga (2019-11-21 16:52 UTC)

<p>We typically suggest suggest 4-8 times more memory than your dataset. If this is 40GB uncompressed dataset, you might be able to load it and get it displayed in SLicer but that’s about as much as you can do. Segmentation, visualization etc is unlikely to work.</p>
<p>As <a class="mention" href="/u/pieper">@pieper</a> said, make sure you are not compressing the data during save, and also use SSD which usually speeds up the sequential IO quite good.</p>

---

## Post #4 by @pll_llq (2019-11-21 18:09 UTC)

<p>Thanks <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/pieper">@pieper</a> I am using uncompressed NRRD that was saved from an industrial microCT machine and the machine has an SSD.<br>
Basically my task in Slicer is to identify intensities of different parts of the image and to crop the volume. I am not performing any segmentation tasks though I’ve tried and it also works okay. It’s just the IO time that is annoying.<br>
Anyway, thanks a lot for your input</p>

---

## Post #5 by @muratmaga (2019-11-21 19:00 UTC)

<p>I routinely work with datasets that are 2-16GB range. Provided that there is sufficient memory to load the data into Slicer, when IO takes that long (several minutes) the usual culprit is compression/decompression of the data at the load/save step, which is single-threaded.</p>

---

## Post #6 by @muratmaga (2019-11-21 21:52 UTC)

<p>Out of curiosity, I made a rough test.</p>
<p>Reading a sequence of 2200 PNG images that resulted in a 10GB volume took 3’ 25" on a 32GB laptop with a nvme drive (Using ImageStack from <a class="mention" href="/u/pieper">@pieper</a>). Saving same volume as nrrd without compression took about 4 seconds. Flushing the cache and reloading the uncompressed 10GB NRRD into a fresh instance of Slicer took 26 seconds.</p>

---
