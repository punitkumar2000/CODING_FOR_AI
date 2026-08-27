'''
packet_scrambler
Author :Punit Kumar
Date:19.08.2026

This program performs four stages:

1.Validate the packet
2.Scramble the packet using slicing
3.Insert SYNC-BIT and remove zeros
4.Check memory integrity using unpacking
'''

def multidimentional_packet_scrambler(packet):

    # --------------------------------------------------
    # Stage 1: Input Validation and Test Data
    # --------------------------------------------------

    print("\n--- Stage 1: Input Validation and Test Data ---")
    if packet and len(packet) >= 10:
        print("Validation passed. Preprocessing packet...")
    else:
        print("Validation failed : packet is empty or too short.")

    # --------------------------------------------------
    # Stage 2: Middle-Out Swap
    # --------------------------------------------------

    mid = len(packet) // 2
    front_half = packet[:mid]
    back_half = packet[mid:]

    scrambled = back_half[::-1] + front_half

    print("\n--- Stage 2: Middle-Out Swap ---")
    print("Front Half:", front_half)
    print("Back Half:", back_half)
    print("Scrambled:", scrambled)
    
    print("Original packet:", packet)
    print("Same object:", id(packet) == id(front_half))

     # --------------------------------------------------
    # Stage 3: In-Place Correction
    # --------------------------------------------------
    
    middle_index = len( scrambled ) // 2
    if type(scrambled[middle_index]) is int:
        scrambled.insert(middle_index + 1, "SYNC−BIT")
    while 0 in scrambled:
        scrambled.remove(0)
    print("\n--- Stage 3: In-Place Correction ---")
    print("Final scrambled list:", scrambled)

    # --------------------------------------------------
    # Stage 4: Memory Integrity Check
    # --------------------------------------------------

    first, *middle, last = scrambled
    print("Original packet:", packet)
    print("Final scrambled:", scrambled)
    print(f"Header: {first} Footer: {last} Body length: {len(middle)}")


packet = [5,12,0,8,21,34,7,19,0,3]
multidimentional_packet_scrambler(packet)