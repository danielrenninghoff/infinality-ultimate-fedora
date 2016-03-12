# Infinality-Ultimate-Bundle for Fedora

I've packaged the Infinality-Ultimate-Bundle by bohoomil for Fedora.
Please see [this](http://danielrenninghoff.com/2015/11/22/infinality-ultimate-bundle-packaged-for-fedora/) blogpost for more information and installation instructions.

## Compilation
You always need to add the ARCH variable when invoking make. This way, you can compile packages for different architectures.
Type ```make all ARCH=x86_64``` to create all packages.

To just create one package, use for example ```make pkg PKG=fontconfig-infinality-ultimate/ ARCH=x86_64```. Make sure to add a slash at the end of the package name.
