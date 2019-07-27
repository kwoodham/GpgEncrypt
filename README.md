# GpgEncrypt
Encrypt and decrypt a file using GPG

**Note** This is my first plugin for fman - please let me know if you have issues.

## Prerequisites
This plugin assumes that you have a working installation of GPG and have set up a keyring. I am not providing any guidance on that, as there are many tutorials available online.

For convenience I am providing a copy of `gnugp.py` pulled from the tarball available at <https://pypi.org/project/python-gnupg/#files>. I have also included here a copy of [LICENSE.txt](./gnupg-LICENSE.txt) for gnupg.py from that tarball as well.

These commands assume the default for `gnupghome`. If this is not the case for you, you may have to provide this in the initialization: `gpg = GPG()`.

## Known limitations
- These commands assumes that only one file in the active directory is selected. I may provide a check on this in future versions (should be easy), or iterate through multiple selections (a little harder), but this first round assumes you have just the one file selected.
- I know there may be a use case for selecting a directory and recursing through each file within it, but I don't have need for such a feature (yet).

## First run
The first run of the `Gpg Encrypt` will prompt for a default recipient. This recipient should (obviously) be in your keyring. I don't do any checks on the availabity of the key.  From then on, it will still prompt you for the recipient, but this will be pre-populated with the default.

## Commands
- `GPG Encrypt` With one file selected, it will prompt for the recipient, and will encrypt to "filename.ext".gpg - if the gpg file exists, it will be overwritten. _(You have been warned!)_

- `GPG Decrypt` will reverse the process. Selected a GPG-encrypted file. The command will _always_ prompt for the passprase. I'm sorry this is clear text in the window - I don't know how to mask it, but it is not stored. A default filename is provided (the same as the input without the `.gpg` extension) for you to edit or accept as is.

Both commands give you the status message returned by gnupg encrypt or decrypt.

