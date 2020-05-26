Signify
=======
This attempts to revert the code to Python 2 for use with Cuckoo Sandbox as a module.
Currently has breaking bugs that need to be resolved, and is on hold.
=======

Signify, a portmanteau of *signature* and *verify*, is a Python module that computes and validates signatures.
At this point it is mostly a library that verifies PE Authenticode-signed binaries.

This module is a forked from Google's ``verify_sigs`` module, updated to fit
modern Python standards and be compatible with Python 3. It is **not** a drop-in
replacement, as significant changes have occurred.

This module is compatible with Python 3.5+ and does not support Python 2.

Installation
------------
Clone and Run with::

    python test.py [file dir]

Thanks
------
Thanks to Germano Caronni (caronni@google.com, gec@acm.org) for writing the basis of this module.
And to ralphje for writing the signify module,
