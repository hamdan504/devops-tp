import unittest
<<<<<<< HEAD
from app import app
class TestApp ( unittest . TestCase ):
def test_home_route ( self ):
tester = app . test_client ( self )
response = tester . get (’/’)
self . assertEqual ( response . status_code , 200)
=======
# t
class TestApp ( unittest . TestCase ):
  def test_output ( self ):
    self.assertTrue ( True )
if __name__ == " __main__ ":
  unittest.main()
>>>>>>> origin/main
