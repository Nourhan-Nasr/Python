PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4 ]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32 ]
Rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 ]

opPC1 = ""
concatenateAfterShift = ""
ResultOfPC2 = ""
part1Shift = ""
part2Shift = ""

hexValue1 = input()
hexValue1 = int(hexValue1, 16)
hexValue = hex(hexValue1)
binValue = bin(int(hexValue, 16))[2:].zfill(64)
for i in range(56):
    opPC1 += binValue[PC1[i]-1]
part1=int(opPC1[0:28], 2)
part2=int(opPC1[28:56], 2)
part1Shift += opPC1[1:28]
part1Shift += opPC1[0]
part2Shift += opPC1[29:56]
part2Shift += opPC1[28]
concatenateAfterShift = part1Shift+part2Shift
for i in range(48):
    ResultOfPC2 += concatenateAfterShift[PC2[i]-1]
print(hex(int(ResultOfPC2, 2)).upper()[2:].zfill(12))
part1ShiftFor = ""
part2ShiftFor = ""
concatenateAfterShiftFor = ""
ResultOfPC2For = ""
for i in range(1, 16):
    part1ShiftFor += part1Shift[Rotations[i]:28]
    part1ShiftFor += part1Shift[0:Rotations[i]]
    part2ShiftFor += part2Shift[Rotations[i]:28]
    part2ShiftFor += part2Shift[0:Rotations[i]]
    concatenateAfterShiftFor = part1ShiftFor+part2ShiftFor
    for j in range(48):
        ResultOfPC2For += concatenateAfterShiftFor[PC2[j]-1]
    print(hex(int(ResultOfPC2For, 2)).upper()[2:].zfill(12))
    part1Shift = part1ShiftFor
    part2Shift = part2ShiftFor
    part1ShiftFor = ""
    part2ShiftFor = ""
    concatenateAfterShiftFor = ""
    ResultOfPC2For = ""
