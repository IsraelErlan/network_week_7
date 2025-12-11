def decimal_to_binary(num: int) -> str:
    lst = [128, 64, 32, 16, 8, 4, 2, 1]
    binary_result = ""
    for n in lst:
        if num >= n:
            binary_result += '1'
            num -= n
        else:
            binary_result += '0'
    return binary_result

def binary_to_decimal(num: str):
    power_of = 0
    decimal_result = 0
    for bit_idx in range(len(num)-1, -1, -1):
        if num[bit_idx] == '1':
            decimal_result += 2 ** power_of 
        power_of += 1
    return decimal_result

def input_ip() -> list:
    ip  = input("Please enter a valid IP address: ")
    ip_list = ip.split('.')
    return ip_list

def get_bin_octets(octets: list):
    res = ""
    for octet in octets:
        res += decimal_to_binary(int(octet))

    return res

def input_subnet_mask() -> list:
    subnet_mask  = input("Please enter a valid subnet mask: ")
    subnet_mask_list = subnet_mask.split('.')
    return subnet_mask_list



def get_CIDR(mask):
    return len(mask[0])
    

def split_mask( mask: str):
    for i in range(len(mask)):
        if mask[i] == '0':
            left = mask[0:i]
            right = mask[i:]
            return (left, right)

def get_network_address(ip: str, mask: tuple):
    count_ones = len(mask[0])
    bin_address = ip[0:count_ones] + mask[1]
    print(mask)
    
    address = ""
    print(bin_address)
    for i in range(0, 32, 8):
        address += str(binary_to_decimal(bin_address[i: i+8])) + '.'
        print(address)
    return address[:-1]


def get_broadcast_address(ip, mask):
   
    count_ones = len(mask[0])
    bin_broadcast = ip[0:count_ones] + '1' * len(mask[1])

    lst = bin_broadcast.split(len(8))
    
    broadcast = ""
    for i in lst:
        broadcast += binary_to_decimal(i) + '.'


def calculate_number_of_hosts(mask):
    return 2 ** len(mask[1]) -2


def get_ip_class(ip, mask):
    pass


