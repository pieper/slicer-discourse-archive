---
topic_id: 25876
title: "Removing An Axis Of Rotation"
date: 2022-10-24
url: https://discourse.slicer.org/t/25876
---

# Removing an axis of rotation

**Topic ID**: 25876
**Date**: 2022-10-24
**URL**: https://discourse.slicer.org/t/removing-an-axis-of-rotation/25876

---

## Post #1 by @Aamir_Khan (2022-10-24 21:18 UTC)

<p>Hi,</p>
<p>I have been trying develop a module where by:</p>
<ol>
<li>Specify the center of sphere (done)</li>
<li>Specify the radius of sphere (done)</li>
<li>USing dynamic modeler to specify the thickness of the sphere (done)</li>
<li>Using dynamic modeler to cut the sphere into half using a markup plane (done)</li>
<li>Now the generated hemisphere is to be rotated about the center.</li>
</ol>
<p>I am able to create a widget whereby I can rotate the hemisphere about the three axes. But I want to remove the option for rotating about its axis (i.e. the IS axis). How could I do this?</p>
<p>I am attaching the link for the code.</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/AMK-TUM/RotateSphere/tree/main/RotateSphere">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/AMK-TUM/RotateSphere/tree/main/RotateSphere" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/AMK-TUM/RotateSphere/tree/main/RotateSphere" target="_blank" rel="noopener nofollow ugc">RotateSphere/RotateSphere at main · AMK-TUM/RotateSphere</a></h3>

  <p><a href="https://github.com/AMK-TUM/RotateSphere/tree/main/RotateSphere" target="_blank" rel="noopener nofollow ugc">main/RotateSphere</a></p>

  <p><span class="label1">Contribute to AMK-TUM/RotateSphere development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thanks</p>

---

## Post #2 by @pieper (2022-10-24 22:05 UTC)

<p>This code should help:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point</a></p>

---

## Post #3 by @Aamir_Khan (2022-10-25 21:05 UTC)

<p>Thanks for the link. I have been struggling to restrict the option to rotate about just two axis and not three. I want to remove the rotation about the LR axis, i.e. remove the option to rotate the hemisphere about its axis.</p>

---

## Post #4 by @pieper (2022-10-25 22:17 UTC)

<p>Ah, I see, did you see this example then?</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-line" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-line</a></p>
<p>You could also look at how some map-like interactor styles allow you to rotate around the globe while keeping north pointing north.  This works in most the world but is undefined at the poles and gives some weird results.  I don’t have a good code reference but basically you map x/y rotations to changes in latitude/longitude and then always set the up vector to north projected onto the cross product of the tangents at that point.</p>

---
