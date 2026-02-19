---
topic_id: 34499
title: "Sorting Data By Type And Name In Scene"
date: 2024-02-23
url: https://discourse.slicer.org/t/34499
---

# Sorting data by type and name in Scene

**Topic ID**: 34499
**Date**: 2024-02-23
**URL**: https://discourse.slicer.org/t/sorting-data-by-type-and-name-in-scene/34499

---

## Post #1 by @S_Motch_Perrine (2024-02-23 15:10 UTC)

<p>I have a large number of files in my Scene, and would like to have them ordered by name. I’m sure there’s got to be a way to do this quickly, but I either can’t remember or find it quickly. Example… my files are all named like this and I would like them to appear in sequential order: Bone_001, Bone_002, etc. but they were loaded in an order so they appear in Scene in a different order, such as Bone_004, Bone_001, etc.  I have some models and some markups. How do I sort my data within the scene by type and file name? Thanks.</p>

---

## Post #2 by @pieper (2024-02-23 15:15 UTC)

<p>Currently you can drag and drop them in the Data module into the order you want, but I’m sure you could also resort them with a python script.  I don’t think we have any other GUI method for that right now.</p>

---

## Post #3 by @S_Motch_Perrine (2024-02-23 15:23 UTC)

<p>Thanks. I think it would be a very useful feature to be able to sort the data by type (i.e. planes, points, curves, models, volumes, etc.) in addition to by name.</p>

---

## Post #4 by @pieper (2024-02-23 15:31 UTC)

<p>Yes, that makes good sense.  You could add this to the feature requests area and people can vote for it.  This would be a good topic for a new developer since the implementation would be pure Qt and could be implemented as a python plugin.</p>
<aside class="onebox category-onebox" style="box-shadow: -5px 0px #F1592A;">
  <article class="onebox-body category-onebox-body">
    <h3>
      <a class="badge-category__wrapper" href="/c/support/feature-requests/9">
         <span class="badge-category__name">Feature requests</span>
       
      </a>
    </h3>
      <div>
        <span class="description">
          <p>This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes.</p>
        </span>
      </div>
  </article>
  <div class="clearfix"></div>
</aside>


---

## Post #5 by @muratmaga (2024-02-23 16:33 UTC)

<aside class="quote no-group" data-username="S_Motch_Perrine" data-post="1" data-topic="34499">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/s_motch_perrine/48/81028_2.png" class="avatar"> S_Motch_Perrine:</div>
<blockquote>
<p>How do I sort my data within the scene by type and file name? Thanks.</p>
</blockquote>
</aside>
<p>I am not sure if sorting is going to help you that much. I would suggest using the hierarchies. For example you can create a subject folder called Bone_001 and everything related to that (volumes, markups, segmentations, etc) would be nested under that.</p>
<p>You can even make Slicer save preserving that folder structure on the disk.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3cbc7dddd1fd06b070c72b985c0028e2c4ba5ac.png" data-download-href="/uploads/short-url/pEy43qMI3EAI4U3xnH1tTlaXoVm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3cbc7dddd1fd06b070c72b985c0028e2c4ba5ac_2_690x268.png" alt="image" data-base62-sha1="pEy43qMI3EAI4U3xnH1tTlaXoVm" width="690" height="268" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3cbc7dddd1fd06b070c72b985c0028e2c4ba5ac_2_690x268.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3cbc7dddd1fd06b070c72b985c0028e2c4ba5ac.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3cbc7dddd1fd06b070c72b985c0028e2c4ba5ac.png 2x" data-dominant-color="F4F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×346 20.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would that help?</p>

---

## Post #6 by @S_Motch_Perrine (2024-02-23 16:46 UTC)

<p>Thanks, Murat. I do use this feature sometimes, but there are times when I want to sort specifically by file type - which is then buried within the folders. For me, personally, I still want to be able to sort by file type and file names, although the folder feature is useful for some things, too.</p>

---

## Post #7 by @S_Motch_Perrine (2024-02-23 16:49 UTC)

<p>One way around this may be something else I wasn’t thinking of at first… Is there a way to easily export all of the measurements (along with their file names) for all curves, lines, etc. in a scene?</p>

---

## Post #8 by @muratmaga (2024-02-23 17:15 UTC)

<aside class="quote no-group" data-username="S_Motch_Perrine" data-post="7" data-topic="34499">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/s_motch_perrine/48/81028_2.png" class="avatar"> S_Motch_Perrine:</div>
<blockquote>
<p>a way to easily export all of the measurements (along with their file names) for all curves, lines, etc. in a scene?</p>
</blockquote>
</aside>
<p>If you make a folder in the scene and put all your markups under there, you can right click and choose Export File. It will export all of them as mrk.json. using their node names as file names.</p>

---
