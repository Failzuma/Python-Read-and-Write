import pymem, utility

process = pymem.Pymem("ac_client.exe")
current_ammo_base = process.base_address + 0x0016F338
ammo_decrement = process.base_address + 0xC73EF
utility.nopBytes(process.process_handle, ammo_decrement, 2)
current_ammo = utility.FindDMAAddy(process.process_handle, current_ammo_base, [0x0, 0xB8, 0x140], 32)
process.write_bytes(ammo_decrement, b"9090", 2)
process.write_int(current_ammo, 9999)