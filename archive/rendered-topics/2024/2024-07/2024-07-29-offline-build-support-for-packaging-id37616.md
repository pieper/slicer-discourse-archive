# Offline build support for packaging

**Topic ID**: 37616
**Date**: 2024-07-29
**URL**: https://discourse.slicer.org/t/offline-build-support-for-packaging/37616

---

## Post #1 by @purepani (2024-07-29 20:05 UTC)

<p>Hi,<br>
I was attempting to package this software for NixOS, and it looks like the cmake makes many network calls during the build, which, for reproducibility, isn’t allowed in NixOS. While it is possible to work around this on the packaging side, any solution would be fragile, so I was wondering if it would be at all possible to restructure the build process so that CMAKE can be run fully offline. I’d be willing to help if needed.</p>

---

## Post #2 by @Fireye (2025-08-19 09:26 UTC)

<p>Are there any updates here? As a newer nix user it’s been unfathomably frustrating to even get this program running in the first place and it’d be beyond helpful to have it included in nixpkgs.</p>

---

## Post #3 by @purepani (2026-01-26 23:55 UTC)

<p>I had this PR for nixpkgs a while ago which used the binary. Not sure if it really still works but it’s there. <a href="https://github.com/NixOS/nixpkgs/pull/355116" class="inline-onebox" rel="noopener nofollow ugc">slicer3d: init at 5.6.2 by purepani · Pull Request #355116 · NixOS/nixpkgs · GitHub</a></p>

---
