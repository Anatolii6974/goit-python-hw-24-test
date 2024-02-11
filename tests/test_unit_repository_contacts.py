import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import datetime
from unittest.mock import MagicMock
from datetime import date

from sqlalchemy.orm import Session

from src.schemas import ContactBase, ContactResponse
from src.database.models import Contact, User
from src.repository.contacts import (
    get_contacts,
    get_contact,
    create_contact,
    update_contact,
    remove_contact,
    search_contacts,
    get_birthday_per_week
)

class TestAsync(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)
        self.body = ContactBase(
            id=1,
            first_name = "John",
            last_name = "Baizley",
            email = "baizley@baroness.com",
            phone_number = "3332221100",
            birthday = date(year=1977, month=10, day=10),
            additional_data = "Created first contact for test"
        )
        
    async def test_get_contacts(self):
        expected_contacts = [Contact(), Contact(), Contact(), Contact()]
        self.session.query().filter().offset().limit().all.return_value = expected_contacts
        result = await get_contacts(skip=0, limit=3, db=self.session, user=self.user)
        self.assertEqual(result, expected_contacts)   

    async def test_get_contact(self):
        expected_contacts = Contact()
        self.session.query().filter().first.return_value = expected_contacts
        result = await get_contact(self.user.id, self.user, self.session)
        self.assertEqual(result, expected_contacts)     

    async def test_get_contact_not_found(self):
        expected_contacts = None
        self.session.query().filter().first.return_value = expected_contacts
        result = await get_contact(self.user.id, self.user, self.session)
        self.assertEqual(result, expected_contacts)    

    async def test_create_contact(self):
        result = await create_contact(self.body, self.user, self.session)
        self.assertEqual(result.first_name, self.body.first_name)
        self.assertEqual(result.last_name, self.body.last_name)
        self.assertEqual(result.email, self.body.email)
        self.assertEqual(result.phone_number, self.body.phone_number)
        self.assertEqual(result.birthday, self.body.birthday)
        self.assertEqual(result.additional_data, self.body.additional_data)    

    # async def test_update_contact(self):
    #     body = ContactResponse(
    #         id=1,
    #         first_name = "Sebastian",
    #         last_name = "Thomson",
    #         email = "thomson@baroness.com",
    #         phone_number = "7776665544",
    #         birthday = date(year=1977, month=10, day=12),
    #         additional_data = "I'am changed previous contact with id=1",
    #     )
    #     self.session.query().filter().first.return_value = self.body
    #     result = await update_contact(body.id, body, self.user, self.session)
    #     self.assertEqual(result.first_name, self.body.first_name)
    #     self.assertEqual(result.last_name, self.body.last_name)
    #     self.assertEqual(result.email, self.body.email)
    #     self.assertEqual(result.phone_number, self.body.phone_number)
    #     self.assertEqual(result.birthday, self.body.birthday)
    #     self.assertEqual(result.additional_data, self.body.additional_data)    

    async def test_remove_contact(self):
        expected_contacts = Contact()
        self.session.query().filter().first.return_value = expected_contacts
        result = await remove_contact(self.user.id, self.user, self.session)
        self.assertEqual(result, expected_contacts)   

    async def test_search_contacts(self):
        expected_contacts = []
        self.session.query().filter().all.return_value = expected_contacts
        result = await search_contacts(query="test@test.com", user=self.user, db=self.session)
        self.assertEqual(result, expected_contacts)    




if __name__ == '__main__':
    print(TestAsync.setUp)
    unittest.main()     