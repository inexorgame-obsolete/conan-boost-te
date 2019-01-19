import os

from conans import ConanFile, tools


class BoostteConan(ConanFile):
    name = "boost-te"
    version = "19.Jan.19"
    license = "Boost Software License"
    author = "inexorgame info@inexor.org"
    url = "https://github.com/inexorgame/conan-boost-te"
    description = "Boost-Experimental Type Erasure Library."
    topics = ("Type Erasure", "TE", "Boost")
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def configure(self):
        if self.settings.compiler == "gcc" and self.settings.compiler.version < "6.1":
            raise ConanException("GCC > 6.1 is required")

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code
        in the folder and use exports instead of retrieving it with this
        source() method
        '''
        self.run("git clone https://github.com/boost-experimental/te")
        self.run("cd te && git checkout ebbee575d909ec846b623dcbcce2a6609e1fcfc4")

    def package(self):
        self.copy("*.hpp", dst="include", src=os.path.join("te", "include"))
