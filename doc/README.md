Meticoin Core
=============

Setup
---------------------
Meticoin Core is the original Meticoin client and it builds the backbone of the network. It downloads and, by default, stores the entire history of Meticoin transactions, which requires approximately 22 gigabytes of disk space. Depending on the speed of your computer and network connection, the synchronization process can take anywhere from a few hours to a day or more.

To download Meticoin Core, visit [meticoin.org](https://meticoin.org/).

Running
---------------------
The following are some helpful notes on how to run Meticoin Core on your native platform.

### Unix

Unpack the files into a directory and run:

- `bin/meticoin-qt` (GUI) or
- `bin/meticoind` (headless)

### Windows

Unpack the files into a directory, and then run meticoin-qt.exe.

### macOS

Drag Meticoin Core to your applications folder, and then run Meticoin Core.

### Need Help?

* See the documentation at the [Meticoin Wiki](https://meticoin.info/) for help and more information.
* Ask for help on [#meticoin](https://webchat.freenode.net/#meticoin) on Freenode. If you don't have an IRC client, use [webchat here](https://webchat.freenode.net/#meticoin).
* Ask for help on the [MeticoinTalk](https://meticointalk.io/) forums, in the [Technical Support board](https://meticointalk.io/c/technical-support).

Building
---------------------
The following are developer notes on how to build Meticoin Core on your native platform. They are not complete guides, but include notes on the necessary libraries, compile flags, etc.

- [Dependencies](dependencies.md)
- [macOS Build Notes](build-osx.md)
- [Unix Build Notes](build-unix.md)
- [Windows Build Notes](build-windows.md)
- [FreeBSD Build Notes](build-freebsd.md)
- [OpenBSD Build Notes](build-openbsd.md)
- [NetBSD Build Notes](build-netbsd.md)
- [Gitian Building Guide (External Link)](https://github.com/bitcoin-core/docs/blob/master/gitian-building.md)

Development
---------------------
The Meticoin repo's [root README](/README.md) contains relevant information on the development process and automated testing.

- [Developer Notes](developer-notes.md)
- [Productivity Notes](productivity.md)
- [Release Notes](release-notes.md)
- [Release Process](release-process.md)
- [Source Code Documentation (External Link)](https://doxygen.bitcoincore.org/)
- [Translation Process](translation_process.md)
- [Translation Strings Policy](translation_strings_policy.md)
- [JSON-RPC Interface](JSON-RPC-interface.md)
- [Unauthenticated REST Interface](REST-interface.md)
- [Shared Libraries](shared-libraries.md)
- [BIPS](bips.md)
- [Dnsseed Policy](dnsseed-policy.md)
- [Benchmarking](benchmarking.md)

### Resources
* Discuss on the [MeticoinTalk](https://meticointalk.io/) forums.
* Discuss general Meticoin development on #meticoin-dev on Freenode. If you don't have an IRC client, use [webchat here](https://webchat.freenode.net/#meticoin-dev).

### Miscellaneous
- [Assets Attribution](assets-attribution.md)
- [bitcoin.conf Configuration File](bitcoin-conf.md)
- [Files](files.md)
- [Fuzz-testing](fuzzing.md)
- [Reduce Memory](reduce-memory.md)
- [Reduce Traffic](reduce-traffic.md)
- [Tor Support](tor.md)
- [Init Scripts (systemd/upstart/openrc)](init.md)
- [ZMQ](zmq.md)
- [PSBT support](psbt.md)

License
---------------------
Distributed under the [MIT software license](/COPYING).
