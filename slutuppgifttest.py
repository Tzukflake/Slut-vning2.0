import unittest
import datetime
from slutuppgiftfinal import LibrarySystem

class TestLibrarySystem(unittest.TestCase):
    
    def setUp(self):
        self.library = LibrarySystem("Other Library")
        self.library.add_book("Dune", "Frank Herbert")
        
    def test_1_add_book(self):
        self.assertEqual(len(self.library.books), 1)
       
    def test_2_remove_book(self):
        self.library.remove_book("Dune")
        self.assertEqual(len(self.library.books), 0)

    def test_3_borrow_book(self):
        self.library.borrow_book("Dune")
        self.assertTrue(self.library.books[0].borrowed)

    def test_4_return_book(self):
         self.library.borrow_book("Dune")
         self.library.return_book("Dune", return_date = datetime.datetime.today() + datetime.timedelta(days=15))
         self.assertFalse(self.library.books[0].borrowed)
        
    def test_5_is_book_available(self):
         self.assertTrue(self.library.is_book_available("Dune"))
         
    def test_6_print_current_library(self):
         self.assertTrue(self.library.display_available_books())

    def test_7_calculate_days_borrowed(self):
        start_of_borrow_date = datetime.datetime.today()
        test_calculate = self.library.calculate_days_borrowed(borrow_date= start_of_borrow_date, return_date = start_of_borrow_date + datetime.timedelta(days=15))
        self.assertEqual(test_calculate, 15)

unittest.main()