from core import utils, validation, output_string

def main():
    print("start")
    while True:
        ip = utils.input_ip()
        if validation.valid_ip(ip):
            bin_ip = utils.get_bin_octets(ip)
            break
        print("\nTry again with valid IP\n")

    while True:
        mask = utils.input_subnet_mask()
        if validation.valid_mask(mask):
            bin_mask = utils.get_bin_octets(mask)
            splited_mask = utils.split_mask(bin_mask)
            break
        print("\nTry again with valid mask\n")

    network = utils.get_network_address(bin_ip, splited_mask)
    print(network)


if __name__ == '__main__':
    main()