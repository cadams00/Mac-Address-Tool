import sys


class Mac(object):
    def __init__(self, mac_address):
        self.mac_address = str.lower(mac_address)
        # forces string conversion
        self.mac_remove_extra_text()
        self.formatted_addresses = {}

    def mac_remove_extra_text(self):
        # print(self.mac_address)
        cleaned_mac = ''
        for i in self.mac_address:
            if i in '0123456789abcdefghijklmnopqrstuvwxyz':
                cleaned_mac += i
            self.mac_address = cleaned_mac
        # print(self.mac_address)
        return self.mac_address

    def mac_length_check(self):
        # print(self.mac_address)
        if len(self.mac_address) == 12:
            # print(self.mac_address)
            return True
        else:
            return False

    def mac_text_add(self):
        # print(self.mac_address)
        seperator = {0: ':', 1: '-', 2: '.'}
        count = 0
        while count < 3:
            blank_mac = ''
            num = 0
            for i in self.mac_address:
                # print(self.mac_address)
                if count > 1 and num % 4 == 0 and num != 0:
                    blank_mac += seperator[count] + str(i)
                    num += 1
                elif count > 1:
                    blank_mac += str(i)
                    num += 1
                elif num % 2 == 0 and num != 0:
                    blank_mac += seperator[count] + str(i)
                    num += 1
                else:
                    blank_mac += str(i)
                    num += 1
            self.formatted_addresses[count] = blank_mac
            count += 1


def main():
    args_input = None
    if len(sys.argv) > 1:
        args_input = sys.argv[1]
    else:
        args_input = input('What is the mac address? ')
    mac_to_test = Mac(args_input)
    if mac_to_test.mac_length_check():
        mac_to_test.mac_text_add()
        for n in mac_to_test.formatted_addresses:
            print(mac_to_test.formatted_addresses[n])
    else:
        print('Error: Length of input is not correct')

if __name__ == "__main__":
    main()
