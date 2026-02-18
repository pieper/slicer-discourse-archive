# 3D printing - PreForm integration extension

**Topic ID**: 11428
**Date**: 2020-05-06
**URL**: https://discourse.slicer.org/t/3d-printing-preform-integration-extension/11428

---

## Post #1 by @JanWitowski (2020-05-06 00:44 UTC)

<p>Hi,</p>
<p>I am doing research on medical image processing, including segmentation and 3D printing. Recently, I have been working on a small Slicer extension that integrates 3D Slicer with PreForm. PreForm is a software by Formlabs, a SLA 3D printers manufacturer (Somerville, MA), used for setting up SLA print jobs  and print management. There has been a need in medical 3D printing community (including RSNA’s 3D Printing Special Interest Group) to automatize workflow and integrate software for medical 3D printing purposes.</p>
<p>I have been in touch with <a class="mention" href="/u/gaurav">@Gaurav</a> from Formlabs and their team provided me with useful tips on how to run PreForm from the command line.</p>
<p>Proposed extension is very simple: you are able to directly open your segmentation as a mesh PreForm software. Seems straightforward but you often end up correcting your model for printing purposes, changing segmentation for better support generation, cropping the model, etc. This saves a lot of effort with saving, dragging, loading files.</p>
<p><img src="https://media.giphy.com/media/XEa6a50QLF8H91nSBk/giphy.gif" alt="" width="480" height="270"><br>
Extension supports exporting currently selected segment or all visible segments merged into one. It also supports setting a flag that allows for automatic mesh repair (on PreForm side) with Netfabb tool.</p>
<p>This integration/extension is being used by me and my colleagues right now to e.g. 3D print aortic aneurysm models and it will be a part of upcoming publication and hopefully RSNA abstract.</p>
<p>I would love to create a pull request to get this extension available in Slicer, but before I do so I wanted to post an information here and find out if there is more interest in this extension. I am in touch with Formlabs dev team, they are eager to collaborate and we might be able to talk to them about potential features. Also it’s my first extension so please free to suggest any better practices.</p>
<p>Extension is currently available for testing at <a href="https://github.com/jwitos/SlicerPreform" class="inline-onebox" rel="noopener nofollow ugc">GitHub - jwitos/SlicerPreform: PreForm integration with Slicer</a></p>
<p>Thank you,<br>
Jan</p>

---

## Post #2 by @Gaurav (2020-10-07 15:14 UTC)

<p>Hi Jan – can you send me an email or DM with your latest contact details? Hope all is well.</p>

---

## Post #3 by @Dexter777 (2023-06-27 00:28 UTC)

<p>Hi Jan,<br>
What’s new with your Slicer extension for 3d printing and RSNA? Does it work only with Formlabs printers?</p>
<p>Thanks.<br>
Richard</p>

---
