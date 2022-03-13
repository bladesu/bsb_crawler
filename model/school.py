class School:
    __name = ""
    __subject = ""
    __address = ""
    __phoneNumber = ""
    __status = ""
    __fax = ""
    __email = ""

    def __init__(self) -> None:
        pass

    def __init__(self, name, subject, address , phoneNumber, status, fax, email) :
        self.__name = name
        self.__subject = subject
        self.__address = address
        self.__phoneNumber = phoneNumber
        self.__status = status
        self.__fax = fax
        self.__email = email

    def display(self):
        print("name:" + self.__name) 
        print("subject:" + self.__subject)
        print("address:" + self.__address) 
        print("phoneNumber:" +self.__phoneNumber)
        print("status:" + self.__status)
        print("fax:" + self.__fax)
        print("email:" + self.__email)
    
    def get_data_header_array():
        return ['name', 'subject', 'address', 'phoneNumber', 'status', 'fax', 'email'] 
    
    def to_array(self):
        return [self.__name, self.__subject, self.__address, self.__phoneNumber, self.__status, self.__fax, self.__email]

    
    