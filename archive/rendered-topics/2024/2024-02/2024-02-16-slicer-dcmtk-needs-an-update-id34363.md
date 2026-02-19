---
topic_id: 34363
title: "Slicer Dcmtk Needs An Update"
date: 2024-02-16
url: https://discourse.slicer.org/t/34363
---

# Slicer DCMTK needs an update

**Topic ID**: 34363
**Date**: 2024-02-16
**URL**: https://discourse.slicer.org/t/slicer-dcmtk-needs-an-update/34363

---

## Post #1 by @fedorov (2024-02-16 14:29 UTC)

<p>Slicer is using DCMTK version 3.6.6, which based on the tag in <a href="https://github.com/commontk/DCMTK/tree/patched-DCMTK-3.6.6_20210115" class="inline-onebox">GitHub - commontk/DCMTK at patched-DCMTK-3.6.6_20210115</a> is from October 2021! Current version of DCMTK is 3.6.8: <a href="https://git.dcmtk.org/?p=dcmtk.git;a=summary" class="inline-onebox">git.dcmtk.org Git - dcmtk.git/summary</a>.</p>
<p>Michael Onken has been trying to update DCMTK in dcmqi, see <a href="https://github.com/QIICR/dcmqi/pull/493" class="inline-onebox">WIP: Use DcmItem in API where possible. by michaelonken · Pull Request #493 · QIICR/dcmqi · GitHub</a>, but is struggling with CMake linked libraries configuration.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/lassoan">@lassoan</a> can we join forces to figure this out, and upgrade DCMTK both for Slicer and dcmqi? Anyone else with the knowledge of CMake/Superbuld who can help?</p>

---

## Post #2 by @jamesobutler (2024-02-16 14:34 UTC)

<p>Here was some existing work-in-progress to update to version 3.6.7:</p><aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/6709">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/6709" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/6709" target="_blank" rel="noopener nofollow ugc">COMP: Update DCMTK to version 3.6.7</a>
      </h4>

    <div class="branches">
      <code>Slicer:main</code> ← <code>jamesobutler:dcmtk-3.6.7-upgrade</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-28" data-time="16:16:30" data-timezone="UTC">04:16PM - 28 Nov 22 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="jamesobutler" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="1 commits changed 5 files with 19 additions and 18 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/6709/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+19</span>
            <span class="removed">-18</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">re #5944 

Updating DCMTK from 3.6.6 to 3.6.7 will include this bug fix for Ap<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/6709" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ple Silicon https://github.com/DCMTK/dcmtk/commit/5fba853b6f7c13b02bed28bd9f7d3f450e4c72bb

The upstream DCMTK repo is being used here because all previous backports are included in this latest version of DCMTK.

```
List of changes:

$ git shortlog 0f9bf4d..DCMTK-3.6.7 --no-merges
Claus Stovgaard (2):
      Add DCMTK_NO_TRY_RUN for cross compiling
      Incorporate DCMTK_NO_TRY_RUN and DCMTK_ENABLE_STL

Jan Schlamelcher (13):
      Introduced a CMake option for static linking.
      Introduced CMake variable DCMTK_TLS_LIBRARY_POSTFIX.
      Documented DCMTK_TLS_LIBRARY_POSTFIX in INSTALL.
      Introduced OFdeprecated and OFdeprecated_msg.
      Introduced path separator conversion for OFpath.
      Fixed typo in previous commit.
      Enabled various compiler warnings by default.
      Fixed a stupid mistake in the previous commit.
      Added a workaround for preventing MSVC warning D9025.
      Fixed some warnings in dcmiod.
      Changed minimum required CMake version to 3.0.0.
      Various enhancements for DCMTK's CMake exports.
      Removed some dead code (CMake).

Joerg Riesmeier (114):
      Also updated GNU Autoconf files.
      Added support for another Value Type (CP-2053).
      Fixed typo and added space characters.
      Added missing object files to Makefile.
      Fixed wrong indentation.
      Removed unused variable (reported by gcc).
      Added missing "unistd" header include.
      Removed unused variable (reported by gcc).
      Made API documentation more consistent.
      Removed unused variable (reported by gcc).
      Rebuilt Makefile dependencies.
      Updated data dictionary for DICOM 2021a.
      Updated code definitions for DICOM 2021a.
      Updated Context Group classes for DICOM 2021a.
      Increased number of digits printed for FL values.
      Added support for two new Storage SOP Classes.
      Fixed typo and corrected line breaks in manpage.
      No need to convert ASCII or UTF-8 characters.
      Fixed comment on lossy JPEG vs. lossy JPEG-LS.
      Removed empty line.
      Removed outdated configure options (Autoconf).
      Added support for CP-2023.
      Added support for Patient's Size and Weight.
      Updated latest tested CMake version.
      Removed empty line from "verbatim" environment.
      Always begin condition text with a capital letter.
      Fixed issue when compiling without MT support.
      Minor changes to documentation.
      Fixed issue with findAndGetUint16Array and VR=AT.
      Fixed wrong class name in file header.
      Added typical error handling options to xml2dcm.
      Updated data dictionary for DICOM 2021b.
      Updated code definitions for DICOM 2021b.
      Added support for CID 247.
      Fixed issue caused by changed attribute name.
      Ignore missing binary value in meta header.
      Added new test case for Contour Data.
      Check whether call of saveFile() was successful.
      Added support for new Storage SOP Class.
      Added "Enhanced X-Ray Radiation Dose SR" to list.
      Modified overlay rendering for multi-frame images.
      Removed check on CMAKE_BACKWARDS_COMPATIBILITY.
      Added support for CP-1789 and CP-1998.
      Output helpful warning messages to logger.
      Added support for CP-2084.
      Removed empty line (added by previous commit).
      Fixed order of libraries to be linked.
      Added missing newline at end of file.
      Updated data dictionary for DICOM 2021c.
      Updated code definitions for DICOM 2021c.
      Added support for new Storage SOP Class.
      Added support for directory record "ANNOTATION".
      Minor fixes to syntax usage and formatting.
      Enhanced API documentation of putAndInsertXXX().
      Updated data dictionary for DICOM 2021d.
      Updated code definitions for DICOM 2021d.
      Updated Context Group classes for DICOM 2021d.
      Replaced old-style cast by OFstatic_cast().
      Fixed issue with unknown UID name.
      Check for space character in File-set ID.
      Replaced German umlaut by its transliteration.
      Removed trailing Unicode character from UID value.
      Converted non-ASCII characters to ASCII.
      Removed trailing Unicode character in manpage.
      Fixed further inconsistencies.
      Fixed typo in comment.
      Output more build options with --version.
      Removed useless typecasts from inline method.
      Added support for two new Storage SOP Classes.
      Enhanced Autoconf build system for OpenSSL checks.
      Fixed issue with findAndGetUint16Array() for OB.
      Fixed comment on Autoconf define HAVE_CXX.
      Changed order of OpenSSL libraries (Autoconf).
      Replaced OFListIterator by OFListConstIterator.
      Added missing spaces (removed by previous commit).
      Updated data dictionary for DICOM 2021e.
      Fixed Media Storage SOP Class UID in DICOMDIR.
      Updated code definitions for DICOM 2021e.
      Fixed typo.
      Removed extra space.
      Updated data dictionary for DICOM 2022a.
      Updated code definitions for DICOM 2022a.
      Removed email addresses and trailing spaces.
      Fixed spelling of attribute name in log message.
      Introduced plural form where appropriate.
      Added missing well-known frame of reference.
      Made use of DCM_PixelItemTag where appropriate.
      Updated Doxygen configuration files.
      Added check on empty Unique Keys in "strict mode".
      Extended comment on Type of Modality attribute.
      Do not set instance creator UID automatically.
      Made XML elements "date" and "time" optional.
      Do not create new document in readXML().
      Fixed typos and revised line breaks.
      Added check on missing Unique Key (strict mode).
      Specified "non-signficant characters" for VR UC.
      Removed misplaced comment character "//".
      Fixed "delimiter characters" for VR UC.
      Various minor fixes to "macros.txt".
      Fixed some outdated DIMSE Status strings.
      Replaced use of deprecated DIMSE Status Codes.
      Fixed documentation of default options.
      Minor fixes to documentation.
      Don't add Derivation Description to Icon Images.
      Fixed incorrect warning in JPEG-LS decoder.
      Made log output in this module more consistent.
      Fixed wrong VR in JSON example (see CP-2139).
      Fixed typo in comment.
      Replaced http:// by https:// in documentation.
      Updated copyright date.
      Updated data dictionary for DICOM 2022b.
      Updated code definitions for DICOM 2022b.
      Updated Context Group classes for DICOM 2022b.
      Fixed line breaks in CHANGES file.

Marco Eichelberg (154):
      Added support for stdin/stdout DICOM file I/O.
      Do not redirect stderr to stdout on Windows anymore.
      Fixed stdin/stdout DICOM file I/O on Win32.
      Improved performance of DcmStdinStream.
      Fixed minor warnings reported by gcc -Wextra.
      Fixed parentheses.
      Migrated dcmsign to OpenSSL high-level APIs.
      Adapted dcmpstat to commit d588139e2.
      Updated code handling Diffie-Hellman parameters.
      Restored compatibility with OpenSSL 1.0.1.
      Fixed minor warnings related to type conversions.
      New function ASC_closeTransportConnection().
      Added hints for a better detection of OpenJPEG.
      Added missing comma to dcm2json --write-meta.
      Expanded dcm2json manpage.
      Adjusted the number of digits printed for FL and FD.
      Fixed incorrect handling of malformed JPEG bitstream.
      Fixed commit e8161b1e4.
      Fixed minor warnings reported by Visual Studio.
      Fixed include of &lt;inttypes.h&gt;.
      Added include needed on BSD.
      Added includes needed on Solaris.
      Added missing include.
      Added includes needed on NetBSD.
      Fixed includes for VS 2008.
      Fixed compilation of arith.cc with DCMTK_ENABLE_CXX11=ON.
      Added further missing includes
      Added support for intermediate CAs and CRLs.
      Added functions for offline certificate verification.
      Revised error handling in module dcmtls.
      Fixed minor inconsistencies.
      Added missing include.
      Fixed compilation without OpenSSL.
      Added include missing on Windows.
      Fixed warning reported by Visual Studio.
      Fix for compilation of dcmtls on Solaris.
      Modifications for LibreSSL on OpenBSD.
      Added includes needed by VS2008.
      Moved inline methods to implementation file.
      Added DCMTK_OFSTD_EXPORT to class OFFile.
      Minor changes needed on Solaris.
      Added include needed by VS2008.
      Defined cmake_minimum_required() as interval.
      Fixed LFS and vsnprintf on Windows and Solaris.
      Added includes needed on Solaris.
      Don't mask error code of association negotiation failure.
      Removed "using namespace std" statements.
      Fixed TOC-TOU race in storescp directory creation.
      Fixed warnings about possible null ptr dereference.
      Fixed configure warnings reported by CMake 3.19.
      Fixed issue in CMake scripts.
      Check if policy CMP0103 exists before setting it.
      Define __STDC_FORMAT_MACROS in oftypes.h.
      Include &lt;cinttypes&gt; when compiling in C++11 mode.
      Replaced DCMTK_DIAGNOSTIC_MIN_GCC_VERSION macro.
      Fixed comments.
      Fixed warnings on Solaris with SunPro compiler.
      Added error messages for unsupported include macros.
      Special handling of preprocessor warnings for MSVC.
      Set CMake CMP0115 introduced with CMake 3.20 to OLD.
      Added default in switch statement.
      Attempt to make the ofthread unit test more robust.
      Fixed minor bug in ofthread unit test.
      Added debug output to ofstd_thread semaphore test.
      Added additional check to dcmtls_scp_tls test.
      Added checks to dcmtls test cases.
      Fixed possible race condition of ofthread test.
      Fixed storescu return code issues.
      Changed default TLS profile to BCP 195 ND.
      Use random port number for dcmtls unit tests.
      Switch stdin to binary mode on Windows.
      Accept forward slash as path separator on Windows.
      Fixed previous commit.
      Accept forward slash as path separator on Windows.
      Set TLS session ID and disable session caching.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Fixed minor warnings.
      Removed dead code that caused warnings on MSVC.
      Fixed minor warnings.
      Fixed minor warnings.
      Documented MSVC versions not supported anymore.
      Fixed issue that caused duplicate calls to the DicomImage constructor to fail when a compressed image is loadad and the result of DcmDataset::getCurrentXfer() is passed as the second parameter.
      Support "-" as special output filename.
      Moved xml2dcm functionality into a class.
      Added support for XML comment tags.
      Added support for XML import and OP output.
      Added missing linefeed.
      Fixed Makefiles.
      Fixed Makefiles.
      Fixed test for maximum supported file size.
      Fixed previous commit.
      Fixed compilation with shared libraries.
      Added explicit include for &lt;cerrno&gt;.
      Fixed double inclusion of libxml2.
      Fixed minor warnings.
      Send SpecificCharacterSet in BFS N-CREATE-RQ.
      Convert monochrome BMP images to MONOCHROME2.
      Added error code EC_SOPClassMismatch.
      Updated XML templates for img2dcm.
      Added multiframe support to img2dcm.
      Fixed minor warnings.
      Fixed bug in class Image2Dcm.
      Made file extensions explicit for CMake CMP0115.
      Enable compilation of DCMTK on DragonFly BSD.
      Fixed compilation on Solaris after previous commit.
      Send Illumination and RefAL only when non-empty.
      Fixed minor warning issued by gcc 10.2.1.
      Removed const qualifier in static function.
      Fixed Posix feature flags for Android build.
      Fixed warnings when compiling with OpenSSL 3.0.
      Removed definition of NEED_DARRAY macro.
      Fixed bug in SiCertificate::getCertCurveName().
      Check whether DICOM dataset contains extended chars.
      Fixed incorrect constructor call.
      Introduced configure tests for OpenSSL features.
      Added two additional configure tests needed on OpenBSD.
      Removed duplicate test.
      Enable C-GET for write protected storage areas.
      Fixed memory leak in DcmElement::getPartialValue().
      Renamed OpenSSL related feature test symbols.
      Fixed previous commit.
      Documented cross-compiling support.
      Improvements to pkg-config support.
      Fixed CMake OpenSSL feature tests.
      Added logger output for OpenSSL initialization.
      Fixed undefined behavior in handling A-ASSOCIATE-RJ.
      Removed dead code to avoid warning.
      Initialize buffer to zero.
      Corrected handling of character set for HG images.
      Updated warning message.
      Fixed indentation.
      Fixed issue with defragmentTCP() in non-blocking mode on Windows, where the WSAEWOULDBLOCK return code was not properly handled in the past.
      Added CMake option DCMTK_PORTABLE_LINUX_BINARIES.
      Replaced C_CHAR_UNSIGNED test by a compile-only one.
      Fixed further build error.
      Updated credits to include Segmed, Inc.
      Fixed various Doxygen warnings.
      Suppress warnings about attribute redeclaration.
      Fixed gcc -Wextrea warning caused by previous commit.
      Fixed warning caused by previous commit.
      Removed overly strict check in the JPEG decoder.
      Fixed typo.
      Fixed possible NULL pointer dereference.

Mathieu Malaterre (7):
      Extend JPEG parser to allow removal of COM segment
      Expose COM removal option to img2dcm
      Remove reference to the expired LZW patent from unisys
      Indicate that the input DICOM/JPEG-LS is not conforming
      Rework un-optimized huffman table checking of symbol table
      Clarify img2dcm documentation for JPEG+APP2 vs ICC Profile
      Document mechanism to add definition in CMake

Michael Onken (40):
      Updated version information for 3.6.6+ development.
      Fixed extra padding created for some segmentations.
      Removed USE_STD_CXX_INLUDES.
      Try to fix build for 744a94 on some platforms.
      Try fixing C includes for old compilers.
      Replaced bzero() with memset().
      Updated dependencies.
      Fixed building for Apple M1.
      Fix for Big Endian systems. Removed retired tag.
      Fixed HL7HierarchicDesignatorMacro.
      Enforce wlmscpfs' sleeping options.
      Updated copyright date and docs.
      Fix appn/comment combination of img2dcm options.
      Removed unused function and applied formatting.
      Try fix dcmect_tests for Big Endian platform.
      Added comment.
      Harmonize dictionary options.
      Fixed possible NULL pointer dereference.
      Fixed poss. NULL pointer dereference/double free.
      Added configure support for changes in a9697d
      Fixed bug introduced in a9697d.
      Fixed documentation.
      Print warning for old cmake dictionary options.
      Remove some typos in the codebase.
      Fixed bug when adding more than 65535 frames.
      Allow up to 2^31-1 frames in segmentations.
      Fixed build errors on some systems.
      Fixed build warnings.
      Fix some binary segmentation concatenations.
      Reformatted source code.
      Forbid insertion of encapsulated Pixel Data.
      Check return value for error.
      Fixed another issue with binary seg concatenations.
      Removed debug output.
      Fix for bug introduced in 1fd08a.
      Adapted DUL constant to reflect current behaviour
      Speed up dcmseg_bigdim and only run with std::map.
      Remove debugging output introduced in last commit.
      Fixed test by removing retired attribute.
      Prepared DCMTK Release 3.6.7.

Nikolas Goldhammer (4):
      Fixed confusing value of Host Type on Windows.
      Fixed a warning in the FindOpenJPEG module.
      Added flag DCMTK_USE_OWN_FINDOPENJPEG_MODULE.
      Improved detection of additional depencencies for statically linking.

Tai Chi Minh Ralph Eastwood (1):
      Add pkg-config support to DCMTK
```</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2024-02-16 19:28 UTC)

<p>I could help out with testing or if there is any specific issue to investigate, but in general <a class="mention" href="/u/jcfr">@jcfr</a> is probably the best person to work on this.</p>

---

## Post #4 by @jcfr (2024-02-16 20:13 UTC)

<p>I will follow-up when I have an update <img src="https://emoji.discourse-cdn.com/twitter/rocket.png?v=12" title=":rocket:" class="emoji" alt=":rocket:" loading="lazy" width="20" height="20"></p>

---
