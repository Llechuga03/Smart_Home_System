import unittest
import smart_home_API

#class dedicated to testing the functionality of each function in smart_home_API
class TestSmartHomeAPI(unittest.TestCase):

    def test_create_user(self):
        '''Testing to see if creating a new user works'''

        user = {"id": 1, "name": "Bob", "email": "Bob@example.com", "homes": []}
        result  = smart_home_API.create_entity("users", user)
        self.assertEqual(result["name"], "Bob") #assert to check for equality

    def test_get_user(self):
        '''Testing to see if we can retrieve user info'''

        user = smart_home_API("users", 1)
        self.assertIsNotNone(user)
        self.assertEqual(user["name"], "Bob") #assert to check for equality
    
    def test_update_user(self):
        '''Testing to see if we can update existing user info'''

        updated_user = smart_home_API.update_entity("users", 1, {"email": "notBob@example.com"})
        self.assertEqual(updated_user["email"], "notBob@example.com") #assert to check for equality

    def test_delete_user(self):
        '''Testing to see if we can delete an existing user'''

        delete = smart_home_API.delete_entity
        self.assertTrue(delete)
        self.assertisNone(smart_home_API.get_entity("user", "1"))   #assert to check for Null (None) value

if __name__ == "__main__":
    unittest.main()