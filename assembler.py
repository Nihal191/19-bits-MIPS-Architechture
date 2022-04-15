def convertBinToHex(bin):
    hex = " "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    return hex


def checkInstruction(instruction):
    convertInstruction = " "
    if instruction == "nop":
        convertInstruction = "0000"
    elif instruction == "lw":
        convertInstruction = "0001"
    elif instruction == "beq":
        convertInstruction = "0010"
    elif instruction == "sub":
        convertInstruction = "0011"
    elif instruction == "j":
        convertInstruction = "0100"
    elif instruction == "slt":
        convertInstruction = "0101"
    elif instruction == "and":
        convertInstruction = "0110"
    elif instruction == "sll":
        convertInstruction = "0111"
    elif instruction == "sw":
        convertInstruction = "1000"
    elif instruction == "addi":
        convertInstruction = "1001"
    elif instruction == "add":
        convertInstruction = "1010"
    else:
        convertInstruction = "Invalid instructions"
    return convertInstruction


def checkRegister(register):
    convertReg = ""
    if register == "R0":
        convertReg = "00000"
    elif register == "R1":
        convertReg = "00001"
    elif register == "R2":
        convertReg = "00010"
    elif register == "R3":
        convertReg = "00011"
    elif register == "R4":
        convertReg = "00100"
    elif register == "R5":
        convertReg = "00101"
    elif register == "R6":
        convertReg = "00110"
    elif register == "R7":
        convertReg = "00111"
    elif register == "R8":
        convertReg = "01000"
    elif register == "R9":
        convertReg = "01001"
    elif register == "R10":
        convertReg = "01010"
    elif register == "R11":
        convertReg = "01011"
    elif register == "R12":
        convertReg = "01100"
    elif register == "R13":
        convertReg = "01101"
    elif register == "R14":
        convertReg = "01110"
    elif register == "R15":
        convertReg = "01111"
    elif register == "R16":
        convertReg = "10000"
    elif register == "R17":
        convertReg = "10001"
    elif register == "R18":
        convertReg = "10010"
    elif register == "R19":
        convertReg = "10011"
    elif register == "R20":
        convertReg = "10100"
    elif register == "R21":
        convertReg = "10101"
    elif register == "R22":
        convertReg = "10110"
    elif register == "R23":
        convertReg = "10111"
    elif register == "R24":
        convertReg = "11000"
    elif register == "R25":
        convertReg = "11001"
    elif register == "R26":
        convertReg = "11010"
    elif register == "R27":
        convertReg = "11011"
    elif register == "R28":
        convertReg = "11100"
    elif register == "R29":
        convertReg = "11101"
    elif register == "R30":
        convertReg = "11110"
    elif register == "R31":
        convertReg = "11111"
    else:
        convertReg == "Invalid Register"

    return convertReg


def decimalToBinary(num):
    if (num < 0):
        num = 16 + num

    ext = ""
    result = ""

    while (num > 0):
        if num % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        # result = (num%2 == 0 ? "0" : "1") + result
        num = num // 2

    for i in range(5 - len(result)):
        ext = "0" + ext

    result = ext + result

    return result


readf = open("inputs.txt", "r")
writef = open("outputs.txt", "w")
writef.write("v2.0 raw\n\n\n")

for i in readf:
    splitted = i.split()

    if (splitted[0] == "nop" or splitted[0] == "sub" or splitted[0] == "slt" or splitted[0] == "and" or splitted[
        0] == "sll" or splitted[0] == "add"):
        con_inst = checkInstruction(splitted[0])
        con_rs = checkRegister(splitted[1])
        con_rt = checkRegister(splitted[2])
        con_rd = checkRegister(splitted[3])

        outr = con_inst + con_rs + con_rt + con_rd

        var1 = outr
        temp1 = outr[-4:]
        outr = outr[:-4]
        temp2 = outr[-4:]
        outr = outr[:-4]
        temp3 = outr[-4:]
        outr = outr[:-4]
        temp4 = outr[-4:]
        outr = outr[:-4]
        temp5 = "0" + outr[:3]

        con_temp1 = convertBinToHex(temp1)
        con_temp2 = convertBinToHex(temp2)
        con_temp3 = convertBinToHex(temp3)
        con_temp4 = convertBinToHex(temp4)
        con_temp5 = convertBinToHex(temp5)

        final = con_temp5 + con_temp4 + con_temp3 + con_temp2 + con_temp1

        writef.write(final + "\n")

    elif splitted[0] == "lw" or splitted[0] == "beq" or splitted[0] == "sw" or splitted[0] == "addi":
        conv_ins = checkInstruction(splitted[0])
        conv_rs = checkRegister(splitted[1])
        conv_rt = checkRegister(splitted[2])
        conv_im = decimalToBinary(int(splitted[3]))

        outi = conv_ins + conv_rs + conv_rt + conv_im

        var2 = outi
        tem1 = outi[-4:]
        outi = outi[:-4]
        tem2 = outi[-4:]
        outi = outi[:-4]
        tem3 = outi[-4:]
        outi = outi[:-4]
        tem4 = outi[-4:]
        outi = outi[:-4]
        tem5 = "0" + outi[:3]

        con_tem1 = convertBinToHex(tem1)
        con_tem2 = convertBinToHex(tem2)
        con_tem3 = convertBinToHex(tem3)
        con_tem4 = convertBinToHex(tem4)
        con_tem5 = convertBinToHex(tem5)

        final2 = con_tem5 + con_tem4 + con_tem3 + con_tem2 + con_tem1

        writef.write(final2 + "\n")

    elif splitted[0] == "j":
        conv_inst = checkInstruction(splitted[0])
        conv_target = decimalToBinary(int(splitted[1]))

        outj = conv_inst + "0000000000" + conv_target

        print(outj)

        var3 = outj
        t1 = outj[-4:]
        outj = outj[:-4]
        t2 = outj[-4:]
        outj = outj[:-4]
        t3 = outj[-4:]
        outj = outj[:-4]
        t4 = outj[-4:]
        outj = outj[:-4]
        t5 = "0" + outj[:3]

        con_t1 = convertBinToHex(t1)
        con_t2 = convertBinToHex(t2)
        con_t3 = convertBinToHex(t3)
        con_t4 = convertBinToHex(t4)
        con_t5 = convertBinToHex(t5)

        final3 = con_t5 + con_t4 + con_t3 + con_t2 + con_t1

        writef.write(final3 + "\n")

