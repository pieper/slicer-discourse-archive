# Build and release VMTK via GitHub Actions

**Topic ID**: 19574
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/build-and-release-vmtk-via-github-actions/19574

---

## Post #1 by @rupertnash (2021-09-08 13:46 UTC)

<p>For $reasons I need VMTK available for multiple versions of python. So I created a simple Github workflow to build VTK, ITK, and VMTK and bundle up the binaries.</p>
<p>This is here: <a href="https://github.com/hemelb-codes/vmtk-build" rel="noopener nofollow ugc">https://github.com/hemelb-codes/vmtk-build</a></p>
<p>I don’t know if this is of any use to the community? For now, I only need this on Ubuntu, so that’s all I’ve done. If anyone wants other platforms, I’d be happy to accept PRs!</p>
<p>I’d be even happier if you wished to adopt the workflows to run in the main VMTK repo so that everyone can use these.</p>
<p>I’m somewhat cheekily calling the current main branch version 1.4.1-rc1 - apologies for any confusion.</p>

---

## Post #2 by @lassoan (2021-09-08 13:52 UTC)

<p>This is very useful, thank you for sharing. We are still in the process of testing our VMTK builds with VTK9 and ITK5, once we merge them into VMTK master, we’ll revisit continuous integration scripts and may use what you have implemented.</p>

---

## Post #3 by @rupertnash (2021-09-08 13:58 UTC)

<p>Yes - looking forward to VTK9 support (we are using that for another program within HemeLB so good to only require a single install). The new vtkPolyData interface is much nicer!</p>

---

## Post #4 by @lassoan (2021-09-08 15:03 UTC)

<p>If you want to give it a try, the VTK9 build is <a href="https://github.com/vmtk/vmtk/pull/372">here</a>, you can test it and give feedback.</p>

---

## Post #5 by @rupertnash (2021-09-10 09:17 UTC)

<p>Thanks - trying a build now: <a href="https://github.com/hemelb-codes/vmtk-build/actions/runs/1220650338" class="inline-onebox" rel="noopener nofollow ugc">VTK_PYTHON_VERSION must be major version only · hemelb-codes/vmtk-build@5525961 · GitHub</a></p>

---
