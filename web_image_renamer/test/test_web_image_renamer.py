import unittest
from app.web_image_renamer import PathObj

class TestWebImageRenamer(object):

    def setUp(self, tmpdir):
        p = tmpdir.mkdir("country").join("city")
        p.write("content")
        self.pobj = PathObj()
        assert p.read() == "content"
    

    def test_path_concatenates_correctly_path_as_list(self):
       pass 
