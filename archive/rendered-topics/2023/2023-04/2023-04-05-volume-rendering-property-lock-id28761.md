---
topic_id: 28761
title: "Volume Rendering Property Lock"
date: 2023-04-05
url: https://discourse.slicer.org/t/28761
---

# Volume rendering property lock

**Topic ID**: 28761
**Date**: 2023-04-05
**URL**: https://discourse.slicer.org/t/volume-rendering-property-lock/28761

---

## Post #1 by @muratmaga (2023-04-05 17:05 UTC)

<p>Here is a use case, which comes up often for us, where the current volume rendering interface is quite clunky. I am looking for suggestions on how to implement in data module that will streamline this use case.</p>
<p>Basically I have dozens of microCT scans of similar organisms. I simply want to visualize them in 3D to look at the anatomy, go back and forth between them easily. These are scanned in the same way (furthermore registered into the same space) and I have custom volume property that performs OK for all the samples.</p>
<p>I can of course drag’n’drop each volume one at a time into viewer, but then I have to manually adjust the volume property, which involves a lot of clicking (plus this only changes the content in one viewer). Is it possible to set a lock in the volume property tab of volume rendering module?</p>
<p>Another, possibility I set one volume as an example, and then there I right click on it and create an action that says “apply volume rendering to all sibling volumes” or something along those lines. And then use the visibility button in the data module to turn volumes on/off.</p>
<p>I am also open to other suggestions.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6cdf805a1a2b364575ad83baeda2feecd1c20df.jpeg" data-download-href="/uploads/short-url/smHPaCKA04BSU7SlexGcZ3aXqV1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6cdf805a1a2b364575ad83baeda2feecd1c20df_2_690x393.jpeg" alt="image" data-base62-sha1="smHPaCKA04BSU7SlexGcZ3aXqV1" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6cdf805a1a2b364575ad83baeda2feecd1c20df_2_690x393.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6cdf805a1a2b364575ad83baeda2feecd1c20df_2_1035x589.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/6/c6cdf805a1a2b364575ad83baeda2feecd1c20df_2_1380x786.jpeg 2x" data-dominant-color="73727C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1095 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-04-05 21:19 UTC)

<p>Can you put them all in a Sequence and then do volume rendering on the proxy?</p>

---

## Post #3 by @muratmaga (2023-04-05 21:36 UTC)

<p>Not sure, never used the sequence module before… Let me try…</p>

---

## Post #4 by @muratmaga (2023-04-05 22:00 UTC)

<p>It sort of works. And I can see it being valuable if I want to make an animation of all samples. but the main issue is usability.</p>
<p>I am not sure why the volume name displayed doesn’t change as I increment over. It hurts the usability, since I don’t what volume I am looking at.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3187e260c97c38cb4a322cc54bc4412090177bb.jpeg" data-download-href="/uploads/short-url/rPTA6aKXaScbTgau6FHT07TcF1F.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3187e260c97c38cb4a322cc54bc4412090177bb_2_517x270.jpeg" alt="image" data-base62-sha1="rPTA6aKXaScbTgau6FHT07TcF1F" width="517" height="270" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3187e260c97c38cb4a322cc54bc4412090177bb_2_517x270.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3187e260c97c38cb4a322cc54bc4412090177bb_2_775x405.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3187e260c97c38cb4a322cc54bc4412090177bb_2_1034x540.jpeg 2x" data-dominant-color="9B9BA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1844×963 94.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e5e758afd7d0ab077b6f9a6a9c4b6ee30b941bd.jpeg" data-download-href="/uploads/short-url/4kEHw9CFTKTe76AAVTT33jRVUXH.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e5e758afd7d0ab077b6f9a6a9c4b6ee30b941bd_2_517x300.jpeg" alt="image" data-base62-sha1="4kEHw9CFTKTe76AAVTT33jRVUXH" width="517" height="300" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e5e758afd7d0ab077b6f9a6a9c4b6ee30b941bd_2_517x300.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e5e758afd7d0ab077b6f9a6a9c4b6ee30b941bd_2_775x450.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e5e758afd7d0ab077b6f9a6a9c4b6ee30b941bd_2_1034x600.jpeg 2x" data-dominant-color="A1A1AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1849×1077 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also how do I control the speed in contious play. I thought entering increment as 10 would give me 10 seconds for each volume, but it is about 1 second.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6a3abecf0e28d999fda5bad94358b32dfe6785.jpeg" data-download-href="/uploads/short-url/rjkN8c1d5OcOGDHWVRo6El593RX.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf6a3abecf0e28d999fda5bad94358b32dfe6785_2_638x500.jpeg" alt="image" data-base62-sha1="rjkN8c1d5OcOGDHWVRo6El593RX" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf6a3abecf0e28d999fda5bad94358b32dfe6785_2_638x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6a3abecf0e28d999fda5bad94358b32dfe6785.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6a3abecf0e28d999fda5bad94358b32dfe6785.jpeg 2x" data-dominant-color="F0F0F0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×669 98 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @pieper (2023-04-05 22:33 UTC)

<p>Probably it would be worth the effort to make a custom module that exposes the features you want.  This would be like the Animator (but much simpler) and use the Sequences under the hood.</p>

---

## Post #6 by @mikebind (2023-04-06 17:40 UTC)

<p>The playback speed is controlled by the frames per second set in the “Browsing” section rather than by the time stamp (many sequences will not have a time stamp or the time stamp will be unrelated to the rate at which it should be shown).  If you set 0.1 fps that should show each frame for 10 seconds.</p>

---

## Post #7 by @mikebind (2023-04-06 17:43 UTC)

<p>For the renaming, you need to check the “Rename” checkbox, then the proxy node will be renamed for each frame.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53da00b0d9b7161ddbc0e01ae24d08bd1a934332.jpeg" data-download-href="/uploads/short-url/bXMHjHL1tZ2IafnO7VjNGVVYwBI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53da00b0d9b7161ddbc0e01ae24d08bd1a934332_2_690x354.jpeg" alt="image" data-base62-sha1="bXMHjHL1tZ2IafnO7VjNGVVYwBI" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53da00b0d9b7161ddbc0e01ae24d08bd1a934332_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/53da00b0d9b7161ddbc0e01ae24d08bd1a934332_2_1035x531.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/53da00b0d9b7161ddbc0e01ae24d08bd1a934332.jpeg 2x" data-dominant-color="DEDEE4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1052×540 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @lassoan (2023-04-06 18:44 UTC)

<p>The other approach (right-click menu in subject hierarchy to apply same volume rendering settings to sibling nodes) is easy to do, too. You can create a custom <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#subject-hierarchy-plugin-offering-view-context-menu-action">subject hierarchy plugin that registers various context menu actions</a> to make the feature conveniently accessible in the Data module.</p>
<p>The need for a custom module for browsing a large number of cases (for review, annotation, segmentation, etc.) comes up very often, so it could be nice to come up with a solution that was a bit easier than writing a script from scratch and provided more features (e.g., convenient GUI). You could add a feature request for it.</p>

---

## Post #9 by @muratmaga (2023-04-06 19:38 UTC)

<p>0.1fps worked, thank you. But enabling rename had no effect on the volume label field. Still only displaying the name of the proxy node.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a1314e7ba112ea0454e8b7fba891a4a2639f6eb.jpeg" data-download-href="/uploads/short-url/8hKzGr5z7bIdpbZP7r6HymeMXmb.jpeg?dl=1" title="Screen Shot 2023-04-06 at 12.36.34 PM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a1314e7ba112ea0454e8b7fba891a4a2639f6eb_2_690x475.jpeg" alt="Screen Shot 2023-04-06 at 12.36.34 PM" data-base62-sha1="8hKzGr5z7bIdpbZP7r6HymeMXmb" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a1314e7ba112ea0454e8b7fba891a4a2639f6eb_2_690x475.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a1314e7ba112ea0454e8b7fba891a4a2639f6eb_2_1035x712.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a1314e7ba112ea0454e8b7fba891a4a2639f6eb_2_1380x950.jpeg 2x" data-dominant-color="9E9EA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-04-06 at 12.36.34 PM</span><span class="informations">3286×2264 546 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #10 by @mikebind (2023-04-06 20:53 UTC)

<p>Sorry, I forgot that the part that gets renamed is the “frame” or other index equivalent, not the whole proxy node name.  You can work around this by copying the name of the image volume over to the “frame” or “time” column in the Sequences module, Edit tab (the same place you manually entered the times earlier), and change the unit type from “numeric” to “text”.  This may work OK for you, but it isn’t a perfect workaround for two reasons.  First, the “index” is what is used to order the sequence items, so when you change from numeric to text indexing, the order of item display may change so that they are presented in alphabetical order rather than the order they were added to the sequence, which might be unexpected.   Second, if the name is long, it will end up being truncated in the slice annotation and you won’t be able to see the whole name.  You could address the first issue by prepending a string like ‘001_’ to your names to keep them in your original order, and you could partially address the second issue by keeping names short or making sure that the part you care about for distinguishing samples varies at the end of the name rather than the beginning.</p>

---

## Post #11 by @muratmaga (2023-04-06 21:16 UTC)

<p>Thanks. The moment you start modifying the objects names to make something to work, I think it is getting a little too hacky (and risky) for my taste.</p>
<p>It is good that I learned the sequences module, I can think of multiple ways it can be useful (without the need to display the object names). I think we will go down the route of syncing the rendering properties via subject hierarchy as I described above. That seems like a more robust solution.</p>

---

## Post #12 by @lassoan (2023-04-06 22:27 UTC)

<p>Using the index for labeling the the items is appropriate. The text mode is specifically implemented for this purpose.</p>
<p>I’ll modify the behavior so that when index is text then the input node’s name will be used as index.</p>
<p>If you want to display longer names then you can reduce the font size in slice view annotations.</p>

---

## Post #13 by @lassoan (2023-04-08 18:19 UTC)

<p>Bulk adding (and removing) of nodes to a sequence with automatic naming based on the original node name has been implemented. You can track its status in this pull request:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6930">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6930" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6930" target="_blank" rel="noopener">Sequence editing improvements and fixes</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>lassoan:sequence-editing-improvements-and-fixes</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-04-08" data-time="18:18:30" data-timezone="UTC">06:18PM - 08 Apr 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="3 commits changed 19 files with 1568 additions and 803 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6930/files" target="_blank" rel="noopener">
            <span class="added">+1568</span>
            <span class="removed">-803</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In Sequences module's Edit section, multiple candidate nodes can be selected and<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6930" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden"> added to the sequence at once, and multiple data nodes can be removed from the sequence at once.
Added an option to use the candidate node name as index value if index type is text.

Factored out sequence editing into a separate widget (qMRMLSequenceEditWidget). This simplifies the code and provides sequence editing GUI for other modules.

This implements the feature that was mentioned in this discussion:
https://discourse.slicer.org/t/volume-rendering-property-lock/28761/12?u=lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
