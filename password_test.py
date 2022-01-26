
  
import unittest # Importing the unittest module
from user import Users
from credential import Credentials # Importing the user and credential class

class TestUsers(unittest.TestCase):
    
    pass
    Test class that defines test cases for the user class behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    pass
    def setUp(self):
        pass
        Set up method to run before each test cases.
        pass
        self.new_user = Users("kennedy Bernard", "teragram") # create new user
        
    def test_init(self):
        pass
        test_init test case to test if the object is initialized properly
        pass
        self.assertEqual(self.new_user.user_name,"Kennnedybenard")
        self.assertEqual(self.new_user.password,"teragram")
        
            
        
class TestCredentials(unittest.TestCase):
    
    '''
    Test class that defines test cases for the credential behaviours.
    
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_credential = Credentials("KennedyBenard", "Instagram", "KennedyBenard", "teragram") # create credentials object
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"KennedyBenard")
        self.assertEqual(self.new_credential.account,"Instagram")
        self.assertEqual(self.new_credential.account_username,"KennedyBenard")
        self.assertEqual(self.new_credential.account_password,"teragram")

if __name__== '__main__':
    unittest.main()        
        