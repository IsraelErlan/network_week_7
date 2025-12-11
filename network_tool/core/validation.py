def has_four_octets(octets_list: list): # The function accepts either IP or SUBNET
    return len(octets_list) == 4

def value_octets_valid(octets_list):
    for octet in octets_list:
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True

def valid_ip(ip: list):
    return has_four_octets(ip) and value_octets_valid(ip)

def valid_mask(mask: list):
    return has_four_octets(mask) and value_octets_valid(mask)


# def valid_mask(mask: list):

#     if not has_four_octets(mask):
#         return False

#     if mask[3] == '255':
#         return False
    
#     for octet in mask:
#         if octet == '255':
#             continue
        
#         octet = int(octet)
#         helper_calculate = 128

#         while octet > 0:
#             octet -= helper_calculate
#             helper_calculate /= 2

#         if octet < 0:
#             return False
        

        

