import pytest 
import os

from _pytest.tmpdir import tmpdir
from app.web_image_renamer import PathObj

class TestWebImageRenamer(object):
  
    @pytest.fixture
    def path(self, tmpdir):
        #p = tmpdir.mkdir("country").mkdir("city").mkdir("thumbs").join("IMG_1234.jpg")
        #return p 
        pass


#    def setup_class(self, path):
#        #p.write("content")
#        self.pobj = PathObj(path)
#        #assert p.read() == "content"

    def test_path_concatenates_correctly_path_as_list(self, tmpdir, path):
        p = tmpdir.mkdir("country").mkdir("city").mkdir("thumbs").join("IMG_1234.jpg")
        touch(str(p))
        assert os.path.exists(p)
        self.pobj = PathObj(str(p))
        #self.pobj.full_path = './country/city/thumbs/IMG_1234.jpg' 
