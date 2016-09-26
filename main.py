class ContactList(list):

    def search(self, string):
        match = []
        for i in self:
            if string in i.name:
                match.append(string)
        return match


    def longest_name(self):
        longest = ""
        for contact in self:
            if len(contact.name) > len(longest):
                longest = contact.name
        if longest:
            return longest


class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts.clear()


class Supplier(Contact):


    all_orders = {}


    def __init__(self, name, email):
        super().__init__(name, email)


    def order(self, string):
        Supplier.all_orders[self.email] = [string]
        return Supplier.all_orders


# x = Supplier('snfac','a@bb.com')
# x.order('cat')
# print(x.all_orders)


# x=Contact('d','a')
# x=Contact('a','a')
# print([i.__dict__ for i in Contact.all_contacts])
# Contact.reset_contacts()
# print(Contact.all_contacts)
